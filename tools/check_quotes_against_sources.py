#!/usr/bin/env python3
"""Check that phrases a record quotes actually appear in that record's own saved sources.

An adjudicator found a record whose `credit_rate_location` rested on a figure it
said appeared in a vendor FAQ — and the record's OWN saved capture of that FAQ did
not contain the figure anywhere. The record contradicted its own evidence file.
Nothing in the toolset was comparing the two.

That is the local, offline half of the problem D-023 opened. D-023 was a record
citing an archive capture that never existed; `verify_archives.py` checks that
remotely. This checks the cheaper and more common case: the capture exists, is
saved right here, and does not say what the record claims it says.

## What it does

For every coded variable, pull the double-quoted phrases out of the `evidence`
text — the places where a coder asserts the vendor's own words — and look for each
in the record's `-sources/` files. Report the ones that are absent.

## THIS IS A REVIEW AID FOR ONE PRODUCT, NOT A CORPUS-WIDE GATE

Read this before believing any number it prints. The corpus-wide count went 1179,
then 1011, then 909 as three real defects were fixed in the tool itself — a quote
parser that mis-paired on short phrases, a comparison that matched plain text
against raw HTML, and a matcher that could not handle a coder's ellipsis. Each fix
was correct. **None of them reached the real problem.**

The real problem is that a double-quoted phrase in an evidence field is not
necessarily a claim about the vendor's words. Coders also quote:

  * **search terms they looked for and did NOT find** — `"unsuccessful"`, `"fail"`.
    These SHOULD be absent from the capture; that absence is the coded finding.
    Flagging them inverts the check.
  * codebook enum values (`"per_month_yearly"`), JSON field names
    (`"creditDetail"`), their own constructed examples (`"N credits = 1 dashboard"`),
    and their own prose.

Separating those from genuine vendor quotations needs the sentence, not the quote
marks. So this tool cannot be a mechanical gate, and no figure from it belongs in
the paper.

**What it IS good for:** an adjudicator running it on their own product, reading the
list with the record open. That is how the motivating case was found — an
adjudicator noticed a figure absent from a capture the record itself had saved.

Two further limits, stated so they are never mistaken for coverage:

  * **40 records keep no local mirror** and cannot be checked at all. They are named
    in the output rather than passing silently.
  * **Records below a 50% resolve rate are not assessable** — captures mirroring one
    page while the evidence quotes eight documents will miss nearly everything, which
    measures mirroring, not accuracy. Those are listed with their rates, not flagged.

    python3 tools/check_quotes_against_sources.py pass1/framer   # the intended use
    python3 tools/check_quotes_against_sources.py                # whole corpus, noisy
"""

import glob
import html
import os
import re
import sys
import unicodedata

import yaml

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_records import CODED
from source_paths import source_files as _source_files

# Phrases shorter than this are too common to mean anything ("yes", "free", "Pro").
MIN_LEN = 12
# A coder's own shorthand, not a claim about the vendor's words.
SKIP = re.compile(r"^(?:unknown|not_applicable|conflicting|n/?a|none|see .*)$", re.I)


def norm(text, markup=False):
    """Fold quotes, whitespace and case so retyping does not read as absence.

    With markup=True, strip HTML tags and decode entities first. The saved captures
    are raw HTML: a phrase a coder read on screen as `Simple & transparent pricing`
    is stored as `Simple &amp; transparent pricing`, very often with tags between the
    words. Comparing a plain-text quotation against raw markup reports almost every
    ACCURATE quotation as missing — an earlier version of this tool did exactly that
    and produced a four-figure flag count that was entirely its own defect.
    """
    if markup:
        text = re.sub(r"<(script|style)\b.*?</\1>", " ", text, flags=re.S | re.I)
        text = re.sub(r"<[^>]+>", " ", text)
        text = html.unescape(text)
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("‘", "'").replace("’", "'")
    text = text.replace("“", '"').replace("”", '"')
    text = text.replace("–", "-").replace("—", "-").replace(" ", " ")
    return re.sub(r"\s+", " ", text).strip().lower()


def quoted(evidence):
    """Phrases the coder presents as the vendor's own words.

    Quotes are paired by POSITION, not matched by a regex with a length filter.
    The regex version mis-parsed badly: when a quoted phrase was shorter than the
    minimum it failed to match there, then re-anchored on that phrase's CLOSING
    quote and swallowed the coder's own prose up to the next opening quote — so
    a coder's parenthetical was reported as a vendor quotation the sources did not
    contain. It produced 1179 flags, nearly all of them the tool misreading itself.

    Splitting on the quote character makes odd-indexed segments the quoted ones,
    which is right whenever the quotes balance. Where they do not, the record is
    reported as unparseable instead of being scanned with the alignment inverted.
    """
    parts = evidence.split('"')
    if len(parts) % 2 == 0:          # unbalanced quotes: pairing is not knowable
        return None
    out = []
    for index in range(1, len(parts), 2):
        phrase = parts[index].strip()
        if len(phrase) < MIN_LEN or SKIP.match(phrase) or phrase.startswith("http"):
            continue
        out.append(phrase)
    return out


def present(phrase, blob):
    """Is this quotation supported by the capture?

    Coders elide with `...` inside a quotation — "we will notify you... before your
    next renewal" is two fragments of vendor text with the coder's ellipsis between
    them, and it can never match verbatim. So every fragment long enough to be
    distinctive must appear; the elided middle is not checked, which is the entire
    point of an ellipsis.
    """
    fragments = [f.strip(" .,;:") for f in re.split(r"\.{3}|…", phrase)]
    fragments = [f for f in fragments if len(f) >= MIN_LEN]
    if not fragments:                      # nothing distinctive left to check
        return True
    return all(norm(f) in blob for f in fragments)


def source_blob(folder, product):
    """All captures for this product, from every location source_paths knows about.
    This used to look only under `records/<folder>/`, missing the thirteen products whose
    directory sits at the study root (D-063)."""
    paths = sorted(_source_files(product))
    if not paths:
        return None
    chunks = []
    for path in paths:
        if not os.path.isfile(path):
            continue
        try:
            with open(path, encoding="utf-8", errors="ignore") as handle:
                chunks.append(handle.read())
        except OSError:
            continue
    return norm(" ".join(chunks), markup=True) if chunks else ""


def entries(record):
    out = {}
    for name, entry in (record.get("variables") or {}).items():
        out[name] = entry
    for name in CODED:
        if name not in out and name in record:
            out[name] = record[name]
    return out


def main(argv):
    only = set(argv)
    unchecked, checked, flagged, unbalanced, counted = [], 0, [], [], {}

    for folder in ("pass1", "pass2", "adjudicated"):
        for path in sorted(glob.glob(os.path.join(HERE, "records", folder, "*.yaml"))):
            product = os.path.basename(path)[:-5]
            tag = f"{folder}/{product}"
            if only and tag not in only and product not in only:
                continue
            try:
                record = yaml.safe_load(open(path)) or {}
            except yaml.YAMLError:
                continue
            blob = source_blob(folder, product)
            if not blob:
                unchecked.append(tag)
                continue
            checked += 1
            counted[tag] = [0, 0]
            for name, entry in entries(record).items():
                if name not in CODED or not isinstance(entry, dict):
                    continue
                evidence = str(entry.get("evidence") or "")
                phrases = quoted(evidence)
                if phrases is None:
                    unbalanced.append(f"{tag}:{name}")
                    continue
                for phrase in phrases:
                    counted[tag][1] += 1
                    if present(phrase, blob):
                        counted[tag][0] += 1
                    else:
                        flagged.append((tag, name, phrase))

    # Scope the finding to records where the check can actually SEE. A record whose
    # captures mirror one page while its evidence quotes eight documents will miss
    # nearly every quotation, and that measures mirroring, not accuracy. Where MOST
    # quotations resolve, the document IS mirrored — and the few that do not are the
    # real signal: the case that motivated this tool was a figure absent from a
    # capture the record itself had saved.
    ASSESSABLE = 0.50
    by_record = {}
    for tag, name, phrase in flagged:
        by_record.setdefault(tag, []).append((name, phrase))
    rates = {}
    for tag, (found, total) in counted.items():
        rates[tag] = found / total if total else 1.0

    real = [(t, rows) for t, rows in by_record.items() if rates.get(t, 0) >= ASSESSABLE]
    blind = sorted(t for t in by_record if rates.get(t, 0) < ASSESSABLE)

    for tag, rows in sorted(real):
        found, total = counted[tag]
        print(f"\n[{tag}] — {found}/{total} quotations resolve against its own captures, "
              f"so the documents ARE mirrored. These do not:")
        for name, phrase in rows:
            print(f"    {name}\n      \"{phrase[:150]}\"")

    print(f"\n{checked} records checked · {sum(t for _, t in counted.values())} quotations examined")
    print(f"{sum(f for f, _ in counted.values())} resolve against the record's own captures "
          f"({sum(f for f,_ in counted.values())/max(1,sum(t for _,t in counted.values()))*100:.1f}%)")
    print(f"\n{sum(len(r) for _, r in real)} quotations WORTH READING — missing from captures that "
          f"otherwise resolve.")
    print(f"\n{len(blind)} records fall below the {ASSESSABLE:.0%} threshold and are NOT assessable:")
    for tag in blind:
        found, total = counted[tag]
        print(f"    {tag:<28} {found}/{total} resolve — captures too partial to judge the rest")
    if unbalanced:
        print(f"{len(unbalanced)} evidence fields have unbalanced quotes and were NOT scanned")
        print("  (pairing is not knowable there; scanning anyway would invert the alignment")
        print(f"   and manufacture flags): {', '.join(unbalanced[:6])}"
              f"{' ...' if len(unbalanced) > 6 else ''}")
    print(f"\n{len(unchecked)} records keep NO local capture and could not be checked at all:")
    print("  " + ", ".join(unchecked))
    print("\nThis is a review list, not a verdict. A quoted phrase can be legitimately")
    print("absent — read live and never mirrored, cited by URL without saving, or")
    print("rendered by a runtime call no saved artifact can hold. What it finds is worth")
    print("a look; what it cannot see is named above rather than counted as clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
