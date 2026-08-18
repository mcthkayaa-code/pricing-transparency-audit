#!/usr/bin/env python3
"""Check coded free-text values against the character caps the codebook sets for them.

Nothing measured this. `validate_records.py` checks presence, `check_value_enums.py`
checks categorical values against their tables, and neither looks at length — so a
format rule stated twice in the codebook went unenforced across the whole corpus
until an adjudicator noticed one record at 920 characters against a 300 cap.

Caps are read FROM the codebook rather than hardcoded, so this cannot drift from the
instrument it enforces. Two places state them: the type table's free-text row, and
each variable's own **Format.** line.

## This reports; it does not truncate

Truncating a coded value to satisfy a format rule would destroy the content the rule
exists to make usable. The overruns in this corpus are substantive arithmetic
derivations with source citations — the reproducibility the field exists to provide —
and the honest response is to publish the non-compliance rate, not to shorten the
evidence until the rule passes.

    python3 tools/check_free_text_caps.py
    python3 tools/check_free_text_caps.py --list    # every overrun, longest first
"""

import glob
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODEBOOK = os.path.join(HERE, "codebook-v1.md")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_records import CODED

NOT_A_VALUE = {"unknown", "not_applicable", "conflicting", "none", ""}


def caps():
    """variable -> character cap, parsed from each variable's own Format line."""
    text = open(CODEBOOK).read()
    out = {}
    for name in CODED:
        section = re.search(rf"^#### `{re.escape(name)}`(.*?)(?=^#### |\Z)", text, re.M | re.S)
        if not section:
            continue
        found = re.search(r"\*\*Format\.\*\*[^\n]*?max(?:imum)?\s+(\d{2,5})\s+char", section.group(1), re.I)
        if found:
            out[name] = int(found.group(1))
    return out


def entries(record):
    out = {}
    for name, entry in (record.get("variables") or {}).items():
        out[name] = entry
    for name in CODED:
        if name not in out and name in record:
            out[name] = record[name]
    return out


def main(argv):
    spec = caps()
    if not spec:
        print("No character caps parsed from the codebook. Reported, not assumed absent —")
        print("if the codebook states caps in a form this does not read, the check covers nothing.")
        return 1
    print(f"caps parsed from the codebook: {', '.join(f'{k}={v}' for k, v in sorted(spec.items()))}\n")

    rows, over = [], []
    for folder in ("pass1", "pass2", "adjudicated"):
        for path in sorted(glob.glob(os.path.join(HERE, "records", folder, "*.yaml"))):
            product = os.path.basename(path)[:-5]
            try:
                record = yaml.safe_load(open(path)) or {}
            except yaml.YAMLError:
                continue
            for name, cap in spec.items():
                entry = entries(record).get(name)
                if entry is None:
                    continue
                value = entry.get("value") if isinstance(entry, dict) else entry
                text = str(value or "").strip()
                if text.lower() in NOT_A_VALUE:
                    continue
                rows.append((folder, product, name, len(text)))
                if len(text) > cap:
                    over.append((folder, product, name, len(text), cap))

    over.sort(key=lambda r: -r[3])
    if "--list" in argv:
        for folder, product, name, length, cap in over:
            print(f"  {length:>5} / {cap}   {folder}/{product}  {name}")
    else:
        for folder, product, name, length, cap in over[:10]:
            print(f"  {length:>5} / {cap}   {folder}/{product}  {name}")
        if len(over) > 10:
            print(f"  ... {len(over) - 10} more (--list for all)")

    print(f"\n{len(rows)} capped values carry content · {len(over)} exceed their cap")
    if rows:
        print(f"non-compliance rate: {len(over) / len(rows) * 100:.0f}%")
    print("\nNot truncated, deliberately. The overruns are arithmetic derivations with source")
    print("citations — the reproducibility the field exists for — and shortening evidence until")
    print("a format rule passes would destroy what the rule is meant to make usable. The rate")
    print("is published instead.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
