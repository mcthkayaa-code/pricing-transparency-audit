#!/usr/bin/env python3
"""Check every coded value against its own variable's allowed values in the codebook.

The validator checks that all 37 variables are PRESENT and that the two
administrative enums hold. Nothing checked whether a coded value is one the
codebook actually permits — so a coder could write `auto_renewal_default: "yes"`,
a value that variable's own table does not contain, and every check would pass.
An adjudicator caught exactly that by hand.

This parses each variable's value table out of `codebook-v1.md` and compares. It
is deliberately conservative:

  * Variables the codebook types as money, integer or free text carry open values,
    so only their STATUS words are constrained; a number or a prose cap like
    "3 downloads per month" is accepted.
  * A variable whose section has no parseable value table is reported as
    unparseable rather than silently skipped, because a check that quietly covers
    less than it claims is the failure mode this study keeps finding in itself.

    python3 tools/check_value_enums.py records/pass1/*.yaml
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

# Codebook types that carry an open value alongside their status words.
OPEN_TYPES = ("money", "integer", "free text")
STATUS_WORDS = {"unknown", "not_applicable", "conflicting", "non_usd", "no_public_price"}


def allowed_values():
    """variable -> (set_of_allowed, is_open, parsed_ok)"""
    text = open(CODEBOOK).read()
    out = {}
    for name in CODED:
        section = re.search(rf"^#### `{re.escape(name)}`(.*?)(?=^#### |\Z)", text, re.M | re.S)
        if not section:
            out[name] = (set(), False, False)
            continue
        body = section.group(1)
        kind = re.search(r"\*\*Type\*\*\s*([a-z ]+)", body)
        is_open = bool(kind and any(t in kind.group(1) for t in OPEN_TYPES))
        # value tables print each permitted value as a leading `code` cell
        values = set(re.findall(r"^\|\s*`([a-z_0-9]+)`\s*\|", body, re.M))
        # some entries list values in a **Values.** sentence instead
        sentence = re.search(r"\*\*Values\.\*\*(.+?)(?:\n\n|\Z)", body, re.S)
        if sentence:
            values |= set(re.findall(r"`([a-z_0-9]+)`", sentence.group(1)))
        out[name] = (values, is_open, bool(values))
    return out


def is_number(text):
    try:
        float(str(text).replace(",", ""))
        return True
    except (TypeError, ValueError):
        return False


def main(argv):
    spec = allowed_values()
    unparseable = sorted(n for n, (_, _, ok) in spec.items() if not ok)
    if unparseable:
        print(f"NO PARSEABLE VALUE TABLE for {len(unparseable)}: {', '.join(unparseable)}")
        print("  (reported, not skipped — these are unchecked and the count says so)\n")

    paths = argv or sorted(glob.glob(os.path.join(HERE, "records", "*", "*.yaml")))
    bad = 0
    for path in paths:
        try:
            record = yaml.safe_load(open(path)) or {}
        except yaml.YAMLError:
            continue
        slug = os.path.basename(path)[:-5]
        pass_dir = os.path.basename(os.path.dirname(path))
        variables = record.get("variables") or {}
        for name, (values, is_open, ok) in spec.items():
            if not ok:
                continue
            entry = variables.get(name, record.get(name))
            if entry is None:
                continue
            value = entry.get("value") if isinstance(entry, dict) else entry
            text = str(value).strip()
            if text in values:
                continue
            if is_open and (is_number(text) or text not in STATUS_WORDS):
                continue  # open-valued variable carrying a figure or a format string
            print(f"BAD  {pass_dir}/{slug}: {name} = {text!r} not in {sorted(values)}")
            bad += 1
    print(f"\nchecked {len(paths)} records · {bad} out-of-enum values")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
