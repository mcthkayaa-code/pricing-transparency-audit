#!/usr/bin/env python3
"""Attribute every coded `unknown` to one of three kinds, from the coder's own evidence.

An `unknown` is not one thing, and the difference decides what the paper may say.
`failed_generation_charge_policy` is `unknown` on 61 of 76 products. If those are
vendor silence, that is a FINDING about vendors — they do not document whether a
failed output is charged for. If they are access failures, it is a LIMITATION of
this instrument. Same number, opposite sentence.

The three kinds, as fixed in the pre-freeze checklist:

  vendor_silence  the vendor never published it. The coder read the documents the
                  protocol directs them to and the construct is not addressed.
  access_failure  it is published, or plausibly published, but the instrument could
                  not reach it — a document that would not load, an archival attempt
                  that failed, a page behind a login the protocol forbids opening.
  instrument_gap  the vendor documented the construct in a form the codebook has no
                  slot for — a pay-per-event product met with a variable that assumes
                  a billing period, an allowance described qualitatively where the
                  format wants a number.

## This tool does not mutate records

D-010: a line-surgery script that edited records broke eight of them and was deleted,
and the rule since is that records are never rewritten in place. So this WRITES A
SIDECAR — `orchestrator/unknown-attribution.csv` — keyed by (pass, product, variable).
The dataset build joins it at freeze time.

## What it will not do

**It never defaults to `vendor_silence`.** That is the category favourable to the
study's own finding, and a classifier that resolves its uncertainty toward the
flattering answer is doing the thing this study has spent weeks refusing to do.
Anything the rules do not clearly decide comes out as `NEEDS_HAND_REVIEW` and is
counted in the summary, loudly.

**An access signal beats a silence signal.** Where the evidence says both "no
document states it" AND that some relevant document could not be retrieved, the
result is a hand review, not silence. A coder who searched four documents and
failed to open a fifth has not established that the vendor is silent — the answer
may be in the document that would not open.

    python3 tools/attribute_unknowns.py            # write the sidecar, print a summary
    python3 tools/attribute_unknowns.py --review   # print only what needs a human
"""

import csv
import glob
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "orchestrator", "unknown-attribution.csv")
OVERRIDES = os.path.join(HERE, "orchestrator", "unknown-attribution-overrides.csv")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_records import CODED


def load_overrides():
    """Hand decisions on values the patterns could not classify.

    The alternative was to keep extending the pattern lists until the residue
    disappeared, and that is the exact behaviour this tool exists to prevent —
    tuning a classifier until it stops disagreeing with you is guessing toward the
    answer you want, dressed as engineering. A hand decision with a written reason
    is auditable; a pattern added to make a number go down is not.

    Each row carries WHY, and the output marks these `hand` rather than `pattern`
    so a reader can separate what was classified from what was judged.
    """
    if not os.path.exists(OVERRIDES):
        return {}
    out = {}
    with open(OVERRIDES) as handle:
        for row in csv.DictReader(handle):
            key = (row["pass"].strip(), row["product"].strip(), row["variable"].strip())
            out[key] = (row["kind"].strip(), row["basis"].strip())
    return out

# --- signals -----------------------------------------------------------------
# Ordered by precedence: an ACCESS or GAP signal outranks a SILENCE signal,
# because both describe a reason the silence may be ours rather than the vendor's.

ACCESS = [
    # NOTE both corrections below came from reading records the patterns got wrong,
    # in both directions. They are correctness fixes to which sentences the patterns
    # match, not additions made to shrink the review pile — the difference matters,
    # and the second kind is what the overrides file exists to avoid.
    r"\bnot re-?attempted\b",
    # "could not be fetched/archived" was missing, and it is how a coder actually
    # described the study's clearest access failure — a help article that answers the
    # variable directly, returning 403/520 and never retrieved.
    r"\bcould not (?:be )?(?:open|reach|retriev|load|access|fetch|archiv)",
    r"\bfailed to (?:open|load|retriev|fetch|archiv)", r"\bwould not load\b",
    r"\barchival attempts?\b.{0,60}\b(?:fail|exhaust|beyond)", r"\bnot retrieved\b",
    r"\bunreachable\b", r"\breturned (?:a )?(?:404|403|500|error)", r"\btimed out\b",
    r"\bbehind (?:a )?(?:login|paywall|account)", r"\brequires? (?:an? )?(?:account|login|sign)",
    r"\bnot accessible\b", r"\bcaptcha\b", r"\bcloudflare-blocked\b",
    r"\bblocked\b.{0,30}\b(?:live|fetch|retriev|access)",
    # REMOVED: a bare `rate.?limit`. It fired on vendors DOCUMENTING their own rate
    # limits as a product feature — "a quantified 30,000-requests/hour rate limit is
    # documented" is the vendor being transparent, the opposite of us being blocked.
    # It mis-flagged three records whose evidence was in fact thorough vendor silence.
]

GAP = [
    r"\bcodebook has no\b", r"\bno slot\b", r"\bformat (?:permits|allows) no\b",
    r"\bvariable assumes\b", r"\bassumes a (?:billing )?period\b",
    r"\bthis variable (?:assumes|presupposes)\b", r"\bqualitativ\w+ but never numeric",
    r"\bdescribed qualitativ", r"\bno determinate\b", r"\bpay-?per-?event\b",
    r"\bnot (?:a )?(?:periodic|subscription)\b.{0,40}\bvariable\b",
    r"\binstrument gap\b", r"\bthe (?:codebook|format) (?:has|offers) no\b",
    # The quarterly-cadence family (queue item A-011). Two blind coders independently
    # hit a vendor billing every three months and found the variable's closed list has
    # no such value. That is the definition of a gap in the instrument, and the coders
    # named it as one rather than forcing a wrong category.
    r"\bnone of the codebook'?s? allowed values\b", r"\bclosed value list\b",
    r"\bno category for\b", r"\bhas no (?:allowed )?value\b",
    r"\brather than forcing\b", r"\bforcing an inaccurate\b", r"\binstrument-frozen\b",
    r"\bno (?:allowed )?value\b.{0,40}\bdescribes?\b",
]

SILENCE = [
    r"\b(?:is|are|remain)s? silent\b", r"\bno document\b", r"\bneither states\b",
    r"\bnone (?:of the documents )?(?:state|address|mention)", r"\bnot addressed\b",
    r"\bdoes not appear\b", r"\bzero occurrences?\b", r"\bno statement\b",
    r"\bno (?:such )?(?:clause|commitment|figure|mention)\b", r"\bnever states\b",
    r"\bdocumented silence\b", r"\bnot stated\b", r"\bfinds only unrelated\b",
    r"\bno occurrences?\b", r"\bnowhere (?:in|on)\b", r"\bwithout addressing\b",
    r"\bread in full\b.{0,80}\bsilent\b",
    # Coders write silence a dozen ways. These were added after reading the residue
    # the first pass could not classify — same construct, different sentence, and a
    # pattern list that only covers the phrasings I happened to imagine is the
    # keyword-search failure this study already caught in a coder.
    r"\bno\b.{0,50}\b(?:located|found)\b", r"\bneither grants\b", r"\bstates no\b",
    r"\bno official document\b", r"\bdoes not (?:state|address|specify|mention|define)\b",
    r"\bnot (?:specified|documented|disclosed|defined)\b", r"\bno day count\b",
    r"\bno (?:public|published)\b.{0,30}\b(?:statement|figure|policy)\b",
    r"\bnothing (?:in|on)\b.{0,50}\b(?:states|addresses)\b", r"\bfails? to (?:state|address)\b",
    r"\bwas not (?:stated|addressed|found)\b", r"\bcannot be determined from\b",
]


# Negation is checked NARROWLY, and the first attempt at it was wrong in a way worth
# recording. A reviewer found a record whose evidence says "not instrument gap"
# classified AS an instrument gap, because the pattern matched the bare phrase.
# Coders rule categories out by name — "Not access failure (document fully read) or
# instrument gap" — so a matcher blind to that reads their exclusions as assertions.
#
# My first fix suppressed any match with a negator in the preceding 60 characters,
# and it moved 15 records OUT of vendor_silence wrongly. The reason is obvious in
# hindsight: evidence describing silence is written in negatives. "A summary claimed
# 'no watermarks' but no official document states this" and "implication is not a
# statement - no document contains an explicit..." are both textbook vendor silence,
# and both tripped a broad negator window. An over-correction is as much a defect as
# the thing it corrects.
#
# So negation applies ONLY to the phrases that NAME a category, and only when the
# negator is immediately adjacent. A silence description is never suppressed.
# Underscore added 2026-08-17 (D-070). The class was `[- ]`, so the CANONICAL spelling of
# these three categories -- `vendor_silence`, `instrument_gap`, `access_failure`, the form used
# in the codebook, in every record and in this tool's own output column -- did not match. A
# coder writing `unknown_kind=vendor_silence` in their evidence was invisible to the classifier
# that reads evidence for exactly that. Corpus damage was one row, and in the safe direction:
# 9 unknowns declare a kind explicitly, 8 were assigned the declared kind by prose inference
# anyway, and the ninth was left NEEDS_HAND_REVIEW rather than guessed at. The negation guard
# below is unchanged and still applies -- widening what counts as a category NAME does not
# widen what counts as an assertion of it (D-042).
CATEGORY_NAMES = re.compile(r"\b(?:instrument[-_ ]gap|access[-_ ]failure|vendor[-_ ]silence)\b", re.I)
IMMEDIATE_NEGATOR = re.compile(r"\b(?:not|neither|nor|n't|never|rather than|rules? out|excluding)\b"
                               r"[\s,;:()\[\]\-]{0,12}$", re.I)


def hits(patterns, text):
    """Patterns that match text.

    A match is skipped only when the matched span NAMES a category and a negator sits
    immediately before it — "not instrument gap", "neither access failure nor". Every
    other match stands, including the many that describe silence in negative terms.
    """
    found = []
    for pattern in patterns:
        for match in re.finditer(pattern, text, re.I):
            span = text[match.start():match.end()]
            if CATEGORY_NAMES.search(span) and IMMEDIATE_NEGATOR.search(text[max(0, match.start() - 24):match.start()]):
                continue                     # the coder ruled this category OUT by name
            found.append(pattern)
            break
    return found


def classify(evidence):
    """-> (kind, why). Never returns vendor_silence on ambiguous evidence."""
    text = evidence or ""
    if not text.strip():
        return "NEEDS_HAND_REVIEW", "no evidence text recorded"
    a, g, s = hits(ACCESS, text), hits(GAP, text), hits(SILENCE, text)
    if a and s:
        return "NEEDS_HAND_REVIEW", "silence AND an unretrieved document — silence may be ours"
    if a and not g:
        return "access_failure", f"access signal: {a[0]}"
    if g and not a:
        return "instrument_gap", f"format/construct signal: {g[0]}"
    if g and a:
        return "NEEDS_HAND_REVIEW", "both a format signal and an access signal"
    if s:
        return "vendor_silence", f"silence signal: {s[0]}"
    return "NEEDS_HAND_REVIEW", "no signal matched"


def entries(path):
    record = yaml.safe_load(open(path)) or {}
    out = {}
    for name, entry in (record.get("variables") or {}).items():
        out[name] = entry
    for name in CODED:                     # every storage shape, per D-020
        if name not in out and name in record:
            out[name] = record[name]
    return out


def main(argv):
    review_only = "--review" in argv
    derived_kind = {}
    overrides = load_overrides()
    rows = []
    for folder in ("pass1", "pass2", "adjudicated"):
        for path in sorted(glob.glob(os.path.join(HERE, "records", folder, "*.yaml"))):
            product = os.path.basename(path)[:-5]
            for name, entry in entries(path).items():
                if name not in CODED:
                    continue
                value = entry.get("value") if isinstance(entry, dict) else entry
                if str(value).strip() != "unknown":
                    continue
                evidence = str((entry.get("evidence") if isinstance(entry, dict) else "") or "")
                kind, why = classify(evidence)
                derived = kind          # kept: the declared-vs-derived check below must compare
                                        # against what the PATTERN concluded, not against a value a
                                        # hand override may have set to match the declaration and so
                                        # agree with it trivially.
                decided_by = "pattern"
                override = overrides.get((folder, product, name))
                if override:
                    kind, why = override
                    decided_by = "hand"
                rows.append({
                    "pass": folder, "product": product, "variable": name,
                    "kind": kind, "decided_by": decided_by, "basis": why,
                    "evidence": evidence.replace("\n", " ")[:600],
                })
                derived_kind[(folder, product, name)] = derived

    if not review_only:
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        with open(OUT, "w", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=["pass", "product", "variable", "kind", "decided_by", "basis", "evidence"],
            )
            writer.writeheader()
            writer.writerows(rows)

    counts = {}
    for row in rows:
        counts[row["kind"]] = counts.get(row["kind"], 0) + 1
    total = len(rows)

    if review_only:
        for row in rows:
            if row["kind"] == "NEEDS_HAND_REVIEW":
                print(f"\n[{row['pass']}/{row['product']}] {row['variable']}\n  why: {row['basis']}\n  {row['evidence'][:300]}")
        return 0

    print(f"{total} `unknown` values across pass1 + pass2 + adjudicated\n")
    # Every kind present, never a hardcoded list. A fixed list printed the three
    # expected categories and silently omitted a fourth that hand review had to
    # invent — `unattributable_weak_basis`, for records whose own evidence cannot
    # support ANY attribution. One row vanished from the summary while sitting in
    # the CSV, which is the reporting failure this study keeps finding in its tools.
    ordered = ["vendor_silence", "access_failure", "instrument_gap"]
    ordered += sorted(k for k in counts if k not in ordered and k != "NEEDS_HAND_REVIEW")
    ordered.append("NEEDS_HAND_REVIEW")
    for kind in ordered:
        n = counts.get(kind, 0)
        by_hand = sum(1 for r in rows if r["kind"] == kind and r["decided_by"] == "hand")
        tail = f"   ({by_hand} by hand)" if by_hand else ""
        print(f"  {kind:<20} {n:>4}  {n / total * 100:5.1f}%{tail}")
    hand = counts.get("NEEDS_HAND_REVIEW", 0)
    decided = sum(1 for r in rows if r["decided_by"] == "hand")
    print(f"\nwrote {OUT}")
    print(f"{decided} of {total} decided by hand and recorded with a reason in the overrides file.")
    print(f"\n{hand} still need a human. That number is printed rather than absorbed: the")
    print("classifier refuses to guess, and it never guesses toward vendor_silence, which")
    print("is the category that would flatter this study's own headline finding.")

    # --- declared vs derived (added 2026-08-17, D-070 corrected) -------------------------
    # `classify()` derives a kind from a coder's REASONING and deliberately ignores any
    # `unknown_kind=<x>` label the coder wrote, because a label is cheap and reasoning is
    # checkable. That is the right design and it stays. But it means an explicit declaration
    # is silently unused, so a coder declaring one kind while their own prose supports another
    # would never surface anywhere. Nothing compared the two until this ran.
    declared_rows, agree, differ, unmatched = 0, 0, [], []
    for row in rows:
        found = re.search(r"unknown_kind\s*[=:]\s*([a-z_]+)", row["evidence"] or "", re.I)
        if not found:
            continue
        declared_rows += 1
        want = found.group(1).strip().lower()
        got = derived_kind[(row["pass"], row["product"], row["variable"])]
        if got == want:
            agree += 1
        elif got == "NEEDS_HAND_REVIEW":
            unmatched.append((row, want))
        else:
            differ.append((row, want, got))

    print(f"\nDECLARED vs DERIVED — {declared_rows} of {total} unknowns state a kind in their own prose")
    print(f"  {agree:>4} the PATTERN independently derived the declared kind (hand overrides excluded from this)")
    print(f"  {len(unmatched):>4} declared a kind the reasoning did not signal (left for a human, never taken on the label)")
    print(f"  {len(differ):>4} DERIVED A DIFFERENT KIND THAN DECLARED — read these, they are the ones that matter")
    for row, want, got in differ:
        print(f"       [{row['pass']}/{row['product']}] {row['variable']}: declared {want}, derived {got}")
    for row, want in unmatched:
        print(f"       [{row['pass']}/{row['product']}] {row['variable']}: declared {want}, no prose signal")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
