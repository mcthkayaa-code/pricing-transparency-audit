#!/usr/bin/env python3
"""Emit the adjudication work-list: every variable where the two passes disagree.

Protocol §7.4 step 2 sends every disagreement to a third pass that reads both
records and both source sets. This produces that pass's input — one section per
product, each disagreeing variable with both coders' values, sources and evidence
side by side, so the adjudicator applies the codebook rule to the evidence rather
than to a summary of it.

It deliberately does NOT suggest a winner. Step 3 is explicit that majority
decides nothing: there are two prior records and their agreement is not evidence
of correctness, so a tool that nudged toward one side would be corrupting the
procedure it serves.

    python3 tools/disagreements.py            # all products, to stdout
    python3 tools/disagreements.py udio       # one product
    python3 tools/disagreements.py --counts   # per-product totals only
"""

import glob
import os
import sys

import yaml

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASS1 = os.path.join(HERE, "records", "pass1")
PASS2 = os.path.join(HERE, "records", "pass2")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_records import CODED
from agreement import _canon  # same numeric canonicalisation, so nobody adjudicates a trailing zero

# Free prose describing a coder's own arithmetic. Two coders never write the same
# sentence, so it disagrees on every product and is not a measurement — see the
# reliability write-up. It is listed for the adjudicator rather than dropped,
# because the arithmetic itself may still need reconciling.
PROSE = {"computation_assumptions"}


def load(path):
    with open(path) as handle:
        return yaml.safe_load(handle) or {}


def field(record, name):
    """Return (value, source, evidence) from whichever shape holds the field."""
    entry = (record.get("variables") or {}).get(name)
    if entry is None and name in record:
        entry = record[name]
    if isinstance(entry, dict):
        return (
            _canon(name, entry.get("value")),
            str(entry.get("source") or ""),
            str(entry.get("evidence") or ""),
        )
    if entry is None:
        return (None, "", "")
    return (_canon(name, entry), "", "")


# SILENT-SKIP GUARD (D-026). This module used to drop a variable that was absent from
# either record without saying so: the work-list would simply be shorter and the
# reliability n simply smaller, both invisibly — the same shape as D-020, where a tool
# read one storage format and lost five units without a word. Verified inert on this
# corpus (all 26 double-coded products carry all 37 variables in both passes, 962 units
# intact), so closing it changes no published figure. It stops the NEXT corpus from
# losing units in silence.
def report_absent(one, two, coded_names, label=""):
    missing = [n for n in coded_names if n not in one or n not in two]
    if missing:
        import sys as _s
        print(f"ABSENT FROM ONE PASS{(' '+label) if label else ''}: {len(missing)} -> {', '.join(missing)}", file=_s.stderr)
    return missing


def compare(product):
    one, two = load(os.path.join(PASS1, f"{product}.yaml")), load(os.path.join(PASS2, f"{product}.yaml"))
    rows = []
    for name in CODED:
        v1, s1, e1 = field(one, name)
        v2, s2, e2 = field(two, name)
        if v1 is None or v2 is None or v1 == v2:
            continue
        rows.append((name, (v1, s1, e1), (v2, s2, e2)))
    return rows, one, two


def main(argv):
    products = sorted(os.path.basename(p)[:-5] for p in glob.glob(os.path.join(PASS2, "*.yaml")))
    if argv and argv[0] != "--counts":
        products = [p for p in products if p in argv]

    if argv and argv[0] == "--counts":
        total = 0
        for product in products:
            rows, _, _ = compare(product)
            substantive = [r for r in rows if r[0] not in PROSE]
            total += len(substantive)
            print(f"  {product:<22} {len(substantive):>2} disagreements"
                  f"{'  (+prose)' if len(rows) != len(substantive) else ''}")
        print(f"\n{total} substantive disagreements across {len(products)} products")
        return 0

    for product in products:
        rows, one, two = compare(product)
        if not rows:
            print(f"\n## {product} — no disagreements\n")
            continue
        print(f"\n## {product} — {len([r for r in rows if r[0] not in PROSE])} substantive disagreements")
        print(f"pass 1 collected {one.get('collection_date')} · pass 2 collected {two.get('collection_date')}")
        reg1 = one.get("register_events") or []
        reg2 = two.get("register_events") or []
        if reg1 or reg2:
            print(f"register events — pass1: {len(reg1)}, pass2: {len(reg2)}  "
                  f"(§7.4.7/7.4.8: a vendor_edit entry may make a disagreement date_explained; "
                  f"a display_variant NEVER does)")
        for name, (v1, s1, e1), (v2, s2, e2) in rows:
            tag = "  [PROSE — not a measurement]" if name in PROSE else ""
            print(f"\n### {name}{tag}")
            print(f"  pass 1: {v1}")
            if s1:
                print(f"     source:   {s1}")
            if e1:
                print(f"     evidence: {e1[:300]}")
            print(f"  pass 2: {v2}")
            if s2:
                print(f"     source:   {s2}")
            if e2:
                print(f"     evidence: {e2[:300]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
