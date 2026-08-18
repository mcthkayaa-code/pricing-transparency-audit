#!/usr/bin/env python3
"""Cross-check a record's headline price against its stated first charge.

A representation misread (a superscript-cents layout read as whole dollars, a
monthly/annual toggle read in the wrong state, a plan grid whose rows shifted)
usually leaves the two money variables inconsistent with the billing basis that
joins them. This screen finds those pairs. It does NOT decide anything: a
mismatch is a place to look, because vendors legitimately advertise a round
annual total alongside a rounded monthly equivalent.

Run over the whole pass and read the FLAG lines as a work list.

    python3 tools/check_price_arithmetic.py                      # publishing rows
    python3 tools/check_price_arithmetic.py records/pass1/*.yaml  # one pass only
"""

import sys
import glob
import os
import re

import yaml

FIELD = "computation_assumptions"

# billing basis -> how many headline periods the first charge should cover
PERIODS = {
    "per_month_billed_annually": 12,
    "per_seat_per_month": 12,  # annual commitment is the common presentation
    "per_month_billed_monthly": 1,
    "per_year": 1,
    "one_time": 1,
}

# A vendor that prices an annual plan at a round total and prints the monthly
# equivalent rounded to cents leaves a gap of up to half a cent per month.
TOLERANCE = 0.06


def value(variables, name):
    entry = variables.get(name)
    return entry.get("value") if isinstance(entry, dict) else None


def computation_note(record):
    """Return whatever the record says about its own arithmetic, from either shape.

    `computation_assumptions` is defined by the template as a coded variable, but
    fourteen pass-1 records also or instead carry it as a top-level prose string
    (deviation D-010). Both carry the same thing — the coder's account of what was
    computed — so any check that reads only one shape draws a false conclusion
    about the other records.
    """
    parts = []
    for holder in (record.get("variables") or {}, record):
        entry = holder.get(FIELD)
        if isinstance(entry, dict):
            parts.append(str(entry.get("value") or ""))
            parts.append(str(entry.get("evidence") or ""))
        elif isinstance(entry, str):
            parts.append(entry)
    return " ".join(p for p in parts if p and p != "None").strip()


def money(raw):
    try:
        return float(raw)
    except (TypeError, ValueError):
        return None


def check(path):
    slug = os.path.basename(path)[:-5]
    try:
        record = yaml.safe_load(open(path)) or {}
    except yaml.YAMLError as exc:
        return f"PARSE {slug}: {exc}"

    variables = record.get("variables") or {}
    headline = money(value(variables, "headline_price_usd"))
    first = money(value(variables, "first_charge_amount_usd"))
    basis = value(variables, "headline_billing_basis")

    if headline is None or first is None:
        return None  # a status value on either side is a finding, not a mismatch
    if basis not in PERIODS:
        return f"BASIS {slug}: no period defined for {basis!r} (headline {headline}, first {first})"

    expected = headline * PERIODS[basis]
    gap = abs(expected - first)
    if gap > TOLERANCE * PERIODS[basis]:
        ratio = first / headline if headline else 0
        return (
            f"FLAG  {slug}: {headline} x {PERIODS[basis]} = {expected:.2f} "
            f"but first charge is {first:.2f} (off by {gap:.2f}, ratio {ratio:.2f}) [{basis}]"
        )

    # The relation holds. That is either because the vendor published the annual
    # total, or because the coder multiplied. The codebook allows multiplying
    # ONLY where a document states the plan is charged once for twelve months
    # (first_charge_amount_usd rule 2) and requires the arithmetic in
    # `computation_assumptions`. A silent multiplication is indistinguishable
    # from a read total in the value alone, so flag the missing note.
    if PERIODS[basis] > 1:
        note = computation_note(record)
        # A bare status with no prose does not answer the question; a status
        # accompanied by an explanation does (a coder may legitimately record
        # `not_applicable` because the vendor printed the annual total outright).
        informative = len(re.sub(r"\b(not_applicable|unknown|None)\b", "", note).strip()) > 40
        if not informative:
            return (
                f"PROV  {slug}: first charge is exactly {PERIODS[basis]}x the headline "
                f"but the record does not say where that figure came from — establish whether "
                f"the vendor published the total or the coder multiplied"
            )

    return None


def publishing_rows():
    """The rows the dataset actually publishes: adjudicated where one exists, else pass 1.

    This used to default to `records/pass1/*.yaml`, which silently excluded every
    adjudicated record — and the adjudicated row is the PUBLISHED one wherever it
    exists, so the check covered 76 records while the dataset shipped 22 rows it had
    never seen. Nothing announced the gap; the tool printed "checked 76 records" and
    looked complete.

    That is the shape this study keeps finding in its own instruments: a check whose
    scope quietly falls short of what it appears to certify. Pass explicit paths to
    override.
    """
    adjudicated = sorted(glob.glob("records/adjudicated/*.yaml"))
    covered = {os.path.basename(p) for p in adjudicated}
    primary = [p for p in sorted(glob.glob("records/pass1/*.yaml"))
               if os.path.basename(p) not in covered]
    return adjudicated + primary


def main(argv):
    paths = argv or publishing_rows()
    findings = [line for line in (check(p) for p in paths) if line]
    for line in findings:
        print(line)
    print(f"\nchecked {len(paths)} records, {len(findings)} to look at")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
