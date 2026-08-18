#!/usr/bin/env python3
"""Build the publishable dataset from the frozen records.

Emits three files into `dataset/`:

  coded-values.csv      one row per product, one column per coded variable — the table
                        most readers will use
  coded-long.csv        one row per (product, variable) carrying the value, its source,
                        the coder's evidence, and the unknown-attribution kind. This is
                        the file that makes a value checkable rather than merely readable.
  build-report.md       what the build did, what it could not do, and every count a
                        reader would otherwise have to take on trust

## The publishing row

Adjudicated where an adjudicated record exists, pass 1 otherwise. Pass 2 never publishes:
it is the blind second reading that produces the reliability statistic. Two products have
no adjudicated row because their two coders agreed on all 37 variables (D-025).

## Four hard requirements, each from a deviation that cost something

**Parse, never text-match (D-010).** Records legitimately differ at the text level in ways a
parser erases — one record quotes a value where others leave it bare, and both are the same
string once parsed. An independent audit's text-keyed bucketing dropped exactly one record
and reported a 76-product corpus as 75.

**Read every storage shape (D-020, D-033, D-037).** `computation_assumptions` alone appears
inside `variables{}` as a dict, inside `variables{}` as a bare string, and at the top level
as a string. Four separate times in this study a tool read one shape and produced a
confident wrong number — twice alarming, twice reassuring, and the reassuring direction is
worse because nothing prompts a second look. So this reads every shape and **reports any
shape it does not recognise instead of skipping it.**

**Never coerce yes/no (D-006).** Bare `no` is a YAML boolean. Values are emitted as the
strings the codebook defines.

**Never change a coded value at build time — report the contradiction instead (D-010's spirit).**
The first version of this build blanked any derived per-output figure to `not_computable`
wherever a money value was `unknown` or `non_usd`, on the D-053 reasoning that a USD figure
cannot come from a non-USD one. Two things were wrong with that.

It fired on the wrong records: five of the ten it caught have a perfectly good USD headline
price and an `unknown` FIRST CHARGE for unrelated reasons — a pay-per-event product with no
determinate first transaction, an unstated billing cadence, a dead product. Blanking their
derived figures would have been a fabrication.

And more fundamentally, **a build that rewrites a coded value is the orchestrator making a
coding decision at build time**, which is exactly what this study forbids everywhere else.
Canonicalising a storage shape is not the same act as changing a value.

So the build now REPORTS the case and changes nothing: where a record carries a determinate
derived per-output value while its headline price is not a USD number, that is a
contradiction for adjudication, and it goes in the build report by name.

    python3 tools/build_dataset.py
"""

import csv
import glob
import os
import sys

import yaml

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "dataset")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_records import CODED
from source_paths import source_files as _source_files

ADMIN = ["product_id", "product_name", "category", "product_status", "paid_submission",
         "entry_tier_name", "collection_date", "coder_role", "coder_pass",
         "archive_status", "primary_source_url"]

# `archive_status` records the outcome a coder's save request APPEARED to return, not
# whether a capture exists. Verified against the capture index, 12 records understate
# their own provenance and one overstates it — and on five of them a capture dated the
# COLLECTION DAY resolves today, so the "archive failed" note was wrong when written
# rather than merely stale (D-061). The coder's observation is preserved as coded and a
# COMPUTED column carries what is actually true, the same way the unknown attributions
# sit in a sidecar rather than overwriting a value.
PROVENANCE = ["archive_status_verified", "resolving_captures", "local_source_files"]

MONEY = {"headline_price_usd", "first_charge_amount_usd"}
# Only `cost_per_output_computable` bears a price claim. `cost_per_output_unit` names WHAT
# a product sells — video-minutes, words, seats — and carries no price and no currency, so a
# non-USD or unresolved headline cannot contradict it. The first version of this build
# lumped them together and reported ten contradictions, of which SIX were its own conflation
# (A-021). Corrected after an adjudicator read the codebook entries and said so.
PRICE_BEARING_DERIVED = {"cost_per_output_computable"}


def field(record, name):
    """(value, source, evidence) from whichever shape holds the field, or None.

    Returns the shape name as a fourth element so the caller can report shapes the
    build does not recognise rather than silently treating them as absent.
    """
    variables = record.get("variables") or {}
    if name in variables:
        entry, where = variables[name], "variables"
    elif name in record:
        entry, where = record[name], "toplevel"
    else:
        return None

    if isinstance(entry, dict):
        return (entry.get("value"), entry.get("source"), entry.get("evidence"), f"{where}/dict")
    if isinstance(entry, (str, int, float, bool)) or entry is None:
        return (entry, None, None, f"{where}/{type(entry).__name__}")
    return (entry, None, None, f"{where}/UNRECOGNISED:{type(entry).__name__}")


def as_text(value):
    """The string the codebook defines, never a coerced Python type."""
    if value is True:
        return "yes"
    if value is False:
        return "no"          # D-006: a bare `no` parsed as boolean; restore the coded string
    if value is None:
        return ""
    return str(value).strip()


def publishing_rows():
    adjudicated = {os.path.basename(p)[:-5]: p
                   for p in glob.glob(os.path.join(HERE, "records", "adjudicated", "*.yaml"))}
    rows = []
    for path in sorted(glob.glob(os.path.join(HERE, "records", "pass1", "*.yaml"))):
        slug = os.path.basename(path)[:-5]
        rows.append((slug, adjudicated.get(slug, path), "adjudicated" if slug in adjudicated else "primary"))
    return rows


def attribution():
    path = os.path.join(HERE, "orchestrator", "unknown-attribution.csv")
    if not os.path.exists(path):
        return {}
    out = {}
    with open(path) as handle:
        for row in csv.DictReader(handle):
            out[(row["pass"], row["product"], row["variable"])] = (row["kind"], row.get("decided_by", ""))
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    attrib = attribution()
    rows = publishing_rows()

    shapes, unrecognised, missing, notes = {}, [], [], []
    seen_captures = {}
    _vpath = os.path.join(HERE, "orchestrator", "archive-verification.csv")
    if os.path.exists(_vpath):
        with open(_vpath) as _h:
            seen_captures = {r["url"]: r["status"] for r in csv.DictReader(_h)}
    wide, long = [], []

    for slug, path, provenance in rows:
        record = yaml.safe_load(open(path))          # parse, never text-match
        if not isinstance(record, dict):
            unrecognised.append(f"{slug}: record did not parse to a mapping")
            continue

        flat = {"product_id": slug, "row_provenance": provenance}
        for key in ADMIN:
            got = field(record, key)
            flat[key] = as_text(got[0]) if got else ""
        flat["product_id"] = slug

        # computed provenance, never trusted from the record
        import re as _re
        # both files, because a capture may be cited in the pass-1 record, the adjudicated
        # row, or only one of them
        _text = open(path).read()
        if provenance == "adjudicated":
            _text += open(os.path.join(HERE, "records", "adjudicated", f"{slug}.yaml")).read()
        _urls = {m.group(0).rstrip(").,;:\"'`")
                 for m in _re.finditer(r"https?://web\.archive\.org/web/\d{14}/\S+", _text)}
        _resolving = [u for u in _urls if seen_captures.get(u) in ("ok", "ok_nearest")]
        # all three locations, via source_paths — this globbed pass1 alone and undercounted
        # thirteen products (D-063)
        _files = _source_files(slug)
        flat["resolving_captures"] = len(_resolving)
        flat["local_source_files"] = len(_files)
        flat["archive_status_verified"] = ("archived" if _resolving else
                                           "local_copy_only" if _files else "NO_REEXAMINABLE_EVIDENCE")

        # Is the headline price a NUMBER? A per-output cost in USD needs a USD numerator,
        # and it does not matter why the headline is not one. `first_charge_amount_usd`
        # is deliberately NOT part of this test: it is `unknown` on several records for
        # reasons that have nothing to do with currency — a pay-per-event product with no
        # determinate first transaction, an unstated billing cadence — and those records
        # have a perfectly good USD headline.
        # A-021 settled this construct and the flag that used to live here is gone.
        #
        # `cost_per_output_computable` is CURRENCY-NEUTRAL by the instrument's own
        # pre-registered design: protocol 8.3.10 and section 9 limitation 12, both written
        # before any of these records were collected, apply the USD-centric deduction to items
        # A1 and A3 only and never to C3. So a determinate value beside a non-USD or unresolved
        # headline is not a contradiction — it is a cost computed in the vendor's own currency,
        # which the instrument always permitted.
        #
        # Three successive heuristics tried to flag this as a problem and each was wrong. The
        # first conflated a unit LABEL with a price claim and produced six false flags. The
        # second could not tell a published euro price from no price at all. The third keyed on
        # the attribution sidecar and still misfired, because `vendor_silence` on
        # `headline_price_usd` correctly means "no USD price published" and says nothing about
        # whether a price exists in another currency.
        #
        # The real answer is that A-021 read all six records and found zero contradictions, so
        # there is no case in this corpus for a flag to catch. What the build reports instead is
        # the FACT — which rows compute a per-output cost in a currency other than USD — because
        # a reader is entitled to know that a full-credit disclosure score can sit beside a
        # derived figure that is not dollar-comparable.
        headline_text = as_text((field(record, "headline_price_usd") or (None,))[0])
        non_usd_basis = headline_text in ("unknown", "non_usd", "not_applicable")

        for name in CODED:
            got = field(record, name)
            if got is None:
                missing.append(f"{slug}/{name}")
                flat[name] = ""
                continue
            value, source, evidence, shape = got
            shapes[shape] = shapes.get(shape, 0) + 1
            if shape.count("UNRECOGNISED"):
                unrecognised.append(f"{slug}/{name}: {shape}")

            text = as_text(value)
            if (name in PRICE_BEARING_DERIVED and non_usd_basis
                    and text not in ("", "unknown", "not_applicable", "no", "not_computable")):
                notes.append(f"{slug}: per-output cost computable, basis is {headline_text!r} "
                             f"— the derived figure is not dollar-comparable")

            flat[name] = text
            key = ("adjudicated" if provenance == "adjudicated" else "pass1", slug, name)
            kind, decided = attrib.get(key, ("", ""))
            long.append({
                "product_id": slug, "variable": name, "value": text,
                "unknown_kind": kind if text == "unknown" else "",
                "attribution_decided_by": decided if text == "unknown" else "",
                "source": "" if source is None else (source.get("url") if isinstance(source, dict) else str(source)),
                "evidence": "" if evidence is None else str(evidence).replace("\n", " "),
                "row_provenance": provenance,
            })
        wide.append(flat)

    with open(os.path.join(OUT, "coded-values.csv"), "w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["product_id", "row_provenance"] + ADMIN[1:] + PROVENANCE + CODED)
        writer.writeheader()
        writer.writerows(wide)
    with open(os.path.join(OUT, "coded-long.csv"), "w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["product_id", "variable", "value", "unknown_kind",
                                                   "attribution_decided_by", "source", "evidence",
                                                   "row_provenance"])
        writer.writeheader()
        writer.writerows(long)

    adj = sum(1 for _, _, p in rows if p == "adjudicated")
    unknowns = sum(1 for r in long if r["value"] == "unknown")
    unattributed = sum(1 for r in long if r["value"] == "unknown" and not r["unknown_kind"])
    report = [
        "# Dataset build report", "",
        f"- **{len(wide)} publishing rows** — {adj} adjudicated, {len(wide) - adj} primary. "
        "Pass 2 never publishes; it is the blind second reading behind the reliability figure.",
        f"- **{len(long)} coded values** = {len(wide)} x {len(CODED)}.",
        f"- **{unknowns} unknowns**, of which **{unattributed} carry no attribution kind**.", "",
        "## Storage shapes encountered", "",
        "Reported because four separate times in this study a tool read one shape and produced a",
        "confident wrong number (D-020, D-033, D-037, and once inside D-047).", "",
    ]
    for shape, count in sorted(shapes.items(), key=lambda kv: -kv[1]):
        report.append(f"- `{shape}` — {count}")
    report += ["", "## Anything the build could not handle", ""]
    report.append(f"- unrecognised shapes: **{len(unrecognised)}**" + ("" if not unrecognised else ""))
    for item in unrecognised[:20]:
        report.append(f"  - {item}")
    report.append(f"- coded variables absent from a publishing row: **{len(missing)}**")
    for item in missing[:20]:
        report.append(f"  - {item}")
    report += ["", "## Per-output costs computed on a non-USD basis", ""]
    if notes:
        report.append("Not contradictions. **A-021** established that `cost_per_output_computable` is")
        report.append("currency-neutral by the instrument's pre-registered design — protocol 8.3.10 and")
        report.append("section 9 limitation 12 apply the USD-centric deduction to items A1 and A3 only,")
        report.append("never to C3 — so a cost computed in the vendor's own currency is computable.")
        report.append("")
        report.append("Listed because a reader is entitled to know that a **full-credit disclosure score**")
        report.append("can sit beside a **derived figure that is not dollar-comparable**. That asymmetry is")
        report.append("the honest cost of a currency-neutral construct, and A-021 names it too.")
        report.append("")
        for item in notes:
            report.append(f"- {item}")
    else:
        report.append("None.")
    report += ["", "## What ships with this dataset", "",
               "The `records/*/*-sources/` directories must be published alongside these CSVs. For 159",
               "coded values the local capture is the only surviving evidence, because their archive",
               "citation resolves to a different capture or to none (D-037). A release of the CSVs alone",
               "would look complete and be unverifiable.", ""]
    with open(os.path.join(OUT, "build-report.md"), "w") as handle:
        handle.write("\n".join(report) + "\n")

    print(f"{len(wide)} rows x {len(CODED)} variables -> dataset/coded-values.csv")
    print(f"{len(long)} value rows with evidence -> dataset/coded-long.csv")
    print(f"unknowns {unknowns} · unattributed {unattributed} · unrecognised shapes {len(unrecognised)} · missing {len(missing)}")
    for shape, count in sorted(shapes.items(), key=lambda kv: -kv[1]):
        print(f"   shape {shape:<24} {count}")
    if notes:
        print(f"{len(notes)} per-output costs on a non-USD basis (reported as fact, not as a defect)")
    return 1 if (unrecognised or missing) else 0


if __name__ == "__main__":
    sys.exit(main())
