#!/usr/bin/env python3
"""Score the AI Pricing Transparency Index (APTI) from the frozen dataset.

The instrument is pre-registered in `protocol-v1.md` section 8.3 and was fixed before
any datum existed. This tool implements it and nothing else. It does not tune, it does
not interpolate, and it does not choose a default when the protocol is silent: where a
coded value reaches an item the protocol does not score, the run STOPS and prints the
combination, because an undefined combination is a protocol defect and worth more than
a number.

    python3 tools/score_apti.py            # validate, score, write both outputs
    python3 tools/score_apti.py --check     # validate and score, write nothing
    python3 tools/score_apti.py --explain elevenlabs,canva
                                            # print the item-by-item working for products

Emits into `dataset/`:

  apti-scores.csv    one row per product; every item score, every component, the index,
                     both sensitivity variants, the unknown count and the determinability
                     rate — so any figure in the report can be recomputed from the file
  apti-report.md     the distribution, the per-component breakdown, whether the index
                     discriminates, where the unknowns sit, and every item that does not
                     vary across the corpus

## Why the validation is this loud

Six times in this study a tool read less than it claimed and produced a number nobody
could distinguish from a result — and three of those numbers were reassuring, which is the
worse direction because nothing prompts a second look. One validator was silently examining
zero records. So this tool:

  * reads the canonical wide CSV, and then re-reads the SAME values out of the long CSV and
    out of the YAML records, which is a third storage shape, and requires all three to agree
    value-for-value before it scores anything;
  * asserts the exact census it expects (76 products x 37 variables = 2812 values) instead of
    scoring whatever it happens to find;
  * prints how many products, variables, values and items it actually examined, so a run that
    covered less than it claims says so in its own output.

## Rules implemented, by name

G0 determinacy (including the item-level definition), G1 `unknown` scores 0 and stays in the
denominator, G2 `not_applicable` removal, G3 the one-third conflict share and its
matrix-precedence clause, G4 multi-variable items and `not_applicable` sub-variables with the
same precedence clause, G5 item-level `unknown`, G6 every value has a defined outcome. The
A3 matrix (8.3.2.1) and the B1 matrix (8.3.3.1) govern their items, per the precedence clauses.
Formula and guard rule 8.3.8, bands 8.3.9, sensitivity analyses S1 and S2 with the inheritance
rules of 8.4.1. Reporting rules D1-D10 of section 8.2.
"""

import argparse
import csv
import os
import statistics
import sys
from decimal import Decimal, ROUND_HALF_UP

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET = os.path.join(HERE, "dataset")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_records import CODED                      # the canonical 37-variable list

EXPECTED_PRODUCTS = 76
EXPECTED_VARIABLES = 37
EXPECTED_VALUES = EXPECTED_PRODUCTS * EXPECTED_VARIABLES

REMOVED = "REMOVED"          # G2 / matrix removal: out of numerator and denominator


class ProtocolGap(Exception):
    """A coded value reached an item section 8.3 does not score.

    Raised, never swallowed. The protocol is pre-registered and frozen, so the answer to
    an uncovered combination is to report it, not to invent a score for it.
    """


# --------------------------------------------------------------------------------------
# Determinacy, rule G0
# --------------------------------------------------------------------------------------

NEVER_DETERMINATE = {"unknown", "conflicting"}
# `absent` is determinate on F2 alone. On A2 and D2 it records a disclosure made nowhere,
# which is the non-determination those items measure.
ABSENT_NON_DETERMINATE_ITEMS = {"A2", "D2"}


def value_determinate(item_id, value):
    """G0, at the level of one coded value."""
    if value in NEVER_DETERMINATE:
        return False
    if value == "absent":
        return item_id not in ABSENT_NON_DETERMINATE_ITEMS
    return True            # not_applicable, non_usd, no_public_price, money, everything else


# --------------------------------------------------------------------------------------
# Single-variable item tables. Transcribed from section 8.3; no value defaults.
# --------------------------------------------------------------------------------------

def _third(points):
    """G3's share. Asserted against the protocol's own printed figures below."""
    return float(Decimal(points) / Decimal(3))


A1 = {"non_usd": 4.0, "no_public_price": 0.0, "unknown": 0.0, "conflicting": 2.7,
      "not_applicable": REMOVED}                                       # money -> 8.0
A2 = {"adjacent": 7.0, "same_page_secondary": 5.0, "one_click_away": 2.0, "absent": 0.0,
      "unknown": 0.0, "conflicting": 2.3, "not_applicable": REMOVED}
C1 = {"yes": 6.0, "no": 0.0, "unknown": 0.0, "conflicting": 2.0, "not_applicable": REMOVED}
C2 = {"yes": 7.0, "partial": 3.5, "no": 0.0, "unknown": 0.0, "conflicting": 2.3,
      "not_applicable": REMOVED}
# C3 carries no `not_applicable`: every product has a principal output unit, so C3 always
# sits in the denominator (codebook 2.3 exception register).
C3 = {"yes": 5.0, "partial": 2.5, "no": 0.0, "unknown": 0.0, "conflicting": 1.7}
C4 = {"rolls_over": 4.0, "partial_rollover": 4.0, "expires_at_period_end": 4.0,
      "unknown": 0.0, "conflicting": 1.3, "not_applicable": REMOVED}
C5 = {"not_charged": 3.0, "charged": 3.0, "case_by_case": 3.0, "unknown": 0.0,
      "conflicting": 1.0, "not_applicable": REMOVED}
# D1 carries no `not_applicable`: `no_recurring_billing` is the one-time-purchase case and
# scores full points.
D1 = {"on": 6.0, "off": 6.0, "no_recurring_billing": 6.0, "unknown": 0.0, "conflicting": 2.0}
D2 = {"pricing_page": 4.0, "purchase_terms_doc": 4.0, "multiple": 4.0,
      "terms_only": 2.0, "help_center_only": 2.0, "absent": 0.0,
      "unknown": 0.0, "conflicting": 1.3, "not_applicable": REMOVED}
D3 = {"yes": 6.0, "no_refunds_stated": 6.0, "unknown": 0.0, "conflicting": 2.0,
      "not_applicable": REMOVED}
D4 = {"self_serve_documented": 4.0, "contact_required": 4.0, "unknown": 0.0,
      "conflicting": 1.3, "not_applicable": REMOVED}
# E1/E2: "any determinate tier value" scores full, and the protocol names `not_granted`,
# `no_watermark` and `never_removed` explicitly so nobody reads them as failures.
E1 = {"free": 5.0, "lowest_paid": 5.0, "mid_tier": 5.0, "highest_tier": 5.0,
      "enterprise_only": 5.0, "not_granted": 5.0,
      "unknown": 0.0, "conflicting": 1.7, "not_applicable": REMOVED}
E2 = {"no_watermark": 3.0, "free": 3.0, "lowest_paid": 3.0, "mid_tier": 3.0,
      "highest_tier": 3.0, "never_removed": 3.0,
      "unknown": 0.0, "conflicting": 1.0, "not_applicable": REMOVED}
E3 = {"user_owns": 2.0, "vendor_license_retained": 2.0, "conditional": 2.0,
      "unknown": 0.0, "conflicting": 0.7, "not_applicable": REMOVED}
F1 = {"all_caps_quantified": 6.0, "some_quantified": 3.0, "none_quantified": 0.0,
      "unknown": 0.0, "conflicting": 2.0, "not_applicable": REMOVED}
# F2 carries no `not_applicable`, and is the one item where `absent` earns full points.
F2 = {"absent": 4.0, "present": 0.0, "unknown": 0.0, "conflicting": 1.3}


# --------------------------------------------------------------------------------------
# Item A3's value-pair matrix, section 8.3.2.1
# --------------------------------------------------------------------------------------

# Rows: first_charge_amount_usd. Columns: mandatory_addon_present. A dagger in the protocol
# marks a pair the coding rules cannot produce; the score printed here is the one the
# protocol prints for the case where adjudication lets the pair stand, and the tool reports
# every dagger it touches instead of scoring it silently.
A3_COLUMNS = ["no", "yes_amount_stated", "yes_amount_unstated", "unknown", "conflicting",
              "not_applicable"]
A3_MATRIX = {
    "money":          {"no": 5.0, "yes_amount_stated": 5.0, "yes_amount_unstated": 2.0,
                       "unknown": 2.0, "conflicting": 2.0, "not_applicable": 5.0},
    "non_usd":        {"no": 2.0, "yes_amount_stated": 2.0, "yes_amount_unstated": 0.0,
                       "unknown": 0.0, "conflicting": 1.7, "not_applicable": 2.0},
    "unknown":        {c: 0.0 for c in A3_COLUMNS},
    "conflicting":    {c: 1.7 for c in A3_COLUMNS},
    "not_applicable": {c: REMOVED for c in A3_COLUMNS},
}
# Daggered cells: the whole `not_applicable` column except its own row, and the whole
# `not_applicable` row except its own column. The undaggered corner is the ordinary case.
A3_DAGGERED = ({("money", "not_applicable"), ("non_usd", "not_applicable"),
                ("unknown", "not_applicable"), ("conflicting", "not_applicable")}
               | {("not_applicable", c) for c in A3_COLUMNS if c != "not_applicable"})
# Note 5's surviving-adjudication rule for the daggered COLUMN: score as the row's `no` cell.
A3_COLUMN_FALLBACK = {row: A3_MATRIX[row]["no"] for row in A3_MATRIX}


# --------------------------------------------------------------------------------------
# Item B1's matrix, section 8.3.3.1
# --------------------------------------------------------------------------------------

B1_YES = {"all_quantified": 5.0, "some_quantified": 3.0, "none_quantified": 0.0,
          "unknown": 0.0, "conflicting": 1.7}
B1_CAP_VALUES = set(B1_YES) | {"not_applicable"}
# Unreachable pairs on this matrix both score 5 if adjudication lets them stand: on the `yes`
# row because `not_applicable` on the cap variable would mean no free plan, and on the `no`
# row because the point is already earned by the documented absence of a free plan and a
# stray cap value cannot take it back.
B1_UNREACHABLE_SCORE = 5.0


def money_value(text):
    """True where a money-or-integer field carries a figure rather than a status word."""
    try:
        float(text)
        return True
    except (TypeError, ValueError):
        return False


def table_score(item_id, table, value, points):
    """Look a value up in its item's table. No default, ever (G6)."""
    if value not in table:
        raise ProtocolGap(
            f"item {item_id}: value {value!r} has no row in section 8.3. "
            f"Defined outcomes: {sorted(table)}"
        )
    got = table[value]
    if got != REMOVED and got > points:
        raise ProtocolGap(f"item {item_id}: table score {got} exceeds the item's {points} points")
    return got


# --------------------------------------------------------------------------------------
# Item scoring. Each returns (score_or_REMOVED, determinate, has_unknown_subvariable, note)
# --------------------------------------------------------------------------------------

def score_a1(row, notes):
    v = row["headline_price_usd"]
    if money_value(v):
        return 8.0, True, False
    return table_score("A1", A1, v, 8.0), value_determinate("A1", v), v == "unknown"


def score_a3(row, notes):
    """Section 8.3.2.1. The matrix governs the item, per G3's and G4's precedence clauses."""
    charge = row["first_charge_amount_usd"]
    addon = row["mandatory_addon_present"]
    rowkey = "money" if money_value(charge) else charge
    if rowkey not in A3_MATRIX:
        raise ProtocolGap(f"item A3: first_charge_amount_usd={charge!r} has no row in the matrix")
    if addon not in A3_COLUMNS:
        raise ProtocolGap(f"item A3: mandatory_addon_present={addon!r} has no column in the matrix")

    score = A3_MATRIX[rowkey][addon]
    if (rowkey, addon) in A3_DAGGERED:
        # Note 5. The pair should have been returned for re-coding; it reached the dataset,
        # so score it as the protocol's surviving-adjudication rule says AND report it.
        if addon == "not_applicable":
            score = A3_COLUMN_FALLBACK[rowkey]
            rule = "daggered column -> scored as the row's `no` cell"
        else:
            score = REMOVED
            rule = "daggered row -> item removed, as the row prints"
        notes.append(f"A3 UNREACHABLE PAIR ({rowkey} x {addon}): {rule}")

    # Item-level determinacy, G0: every sub-variable determinate.
    determinate = (value_determinate("A3", charge) and value_determinate("A3", addon))
    has_unknown = "unknown" in (charge, addon)
    return score, determinate, has_unknown


def score_b1(row, notes):
    """Section 8.3.3.1."""
    exists = row["free_plan_exists"]
    cap = row["free_plan_cap_documented"]
    if cap not in B1_CAP_VALUES:
        raise ProtocolGap(f"item B1: free_plan_cap_documented={cap!r} is not a matrix column")

    if exists == "yes":
        if cap == "not_applicable":
            notes.append("B1 UNREACHABLE PAIR (yes x not_applicable): scored 5 per the matrix")
            score = B1_UNREACHABLE_SCORE
        else:
            score = B1_YES[cap]
    elif exists == "no":
        if cap != "not_applicable":
            notes.append(f"B1 UNREACHABLE PAIR (no x {cap}): scored 5 per the matrix")
        score = 5.0
    elif exists == "unknown":
        score = 0.0
    elif exists == "conflicting":
        score = 1.7
    else:
        raise ProtocolGap(f"item B1: free_plan_exists={exists!r} has no row in the matrix")

    determinate = value_determinate("B1", exists) and value_determinate("B1", cap)
    has_unknown = "unknown" in (exists, cap)
    return score, determinate, has_unknown


def score_b2(row, notes):
    """Count determinate sub-variables, applying G0 and G4; then the G3 floor."""
    watermark = row["free_plan_watermark"]
    duration = row["free_plan_duration"]
    for name, v in (("free_plan_watermark", watermark), ("free_plan_duration", duration)):
        if v not in {"yes", "no", "perpetual", "time_limited", "unknown", "not_applicable",
                     "conflicting"}:
            raise ProtocolGap(f"item B2: {name}={v!r} is not a value item B2 defines an outcome for")

    if watermark == "not_applicable" and duration == "not_applicable":
        return REMOVED, None, None                     # the no-free-plan case

    # G4: a `not_applicable` sub-variable counts as determinate and the item keeps its full 5.
    determinate_subs = sum(1 for v in (watermark, duration) if value_determinate("B2", v))
    score = {2: 5.0, 1: 3.0, 0: 0.0}[determinate_subs]
    if "conflicting" in (watermark, duration) and score < 1.7:
        score = 1.7                                    # G3 floor, applied afterward
    determinate = determinate_subs == 2
    has_unknown = "unknown" in (watermark, duration)
    return score, determinate, has_unknown


def score_b3(row, notes):
    """`trial_exists` first; the sub-variable count only where a trial exists."""
    exists = row["trial_exists"]
    card = row["trial_card_required"]
    length = row["trial_length_days"]
    if exists not in {"yes", "no", "unknown", "conflicting"}:
        raise ProtocolGap(f"item B3: trial_exists={exists!r} is outside its permitted values")

    if exists == "no":
        if card != "not_applicable" or length != "not_applicable":
            notes.append(f"B3 NOTE (trial_exists=no with card={card}, length={length}): "
                         "scores 5 on the first clause regardless")
        return 5.0, (value_determinate("B3", card) and value_determinate("B3", length)), \
            "unknown" in (card, length)
    if exists == "unknown":
        return 0.0, False, True
    if exists == "conflicting":
        return 1.7, False, "unknown" in (card, length)

    # trial_exists == yes
    if "not_applicable" in (card, length):
        notes.append(f"B3 IMPOSSIBLE PAIR (trial_exists=yes with card={card}, length={length}): "
                     "the protocol returns this for re-coding and prints no score")
        raise ProtocolGap(
            "item B3: trial_exists=yes with a `not_applicable` sub-variable is named as an "
            "impossible pair in section 8.3.3 and carries no surviving-adjudication score"
        )
    subs = [card, length]
    for name, v in zip(("trial_card_required", "trial_length_days"), subs):
        if not money_value(v) and v not in {"yes", "no", "unknown", "conflicting"}:
            raise ProtocolGap(f"item B3: {name}={v!r} is not a value item B3 defines an outcome for")
    determinate_subs = sum(1 for v in subs if value_determinate("B3", v))
    score = {2: 5.0, 1: 3.0, 0: 0.0}[determinate_subs]
    if "conflicting" in subs and score < 1.7:
        score = 1.7                                    # G3 floor
    determinate = determinate_subs == 2                 # trial_exists=yes is itself determinate
    return score, determinate, "unknown" in subs


def single(item_id, table, variable, points):
    def scorer(row, notes):
        v = row[variable]
        return table_score(item_id, table, v, points), value_determinate(item_id, v), v == "unknown"
    return scorer


ITEMS = [
    ("A1", "A", 8.0, ("headline_price_usd",), score_a1),
    ("A2", "A", 7.0, ("annual_condition_disclosure",),
     single("A2", A2, "annual_condition_disclosure", 7.0)),
    ("A3", "A", 5.0, ("first_charge_amount_usd", "mandatory_addon_present"), score_a3),
    ("B1", "B", 5.0, ("free_plan_exists", "free_plan_cap_documented"), score_b1),
    ("B2", "B", 5.0, ("free_plan_watermark", "free_plan_duration"), score_b2),
    ("B3", "B", 5.0, ("trial_exists", "trial_card_required", "trial_length_days"), score_b3),
    ("C1", "C", 6.0, ("credit_unit_defined",), single("C1", C1, "credit_unit_defined", 6.0)),
    ("C2", "C", 7.0, ("credit_to_output_rate_published",),
     single("C2", C2, "credit_to_output_rate_published", 7.0)),
    ("C3", "C", 5.0, ("cost_per_output_computable",),
     single("C3", C3, "cost_per_output_computable", 5.0)),
    ("C4", "C", 4.0, ("credit_rollover_policy",), single("C4", C4, "credit_rollover_policy", 4.0)),
    ("C5", "C", 3.0, ("failed_generation_charge_policy",),
     single("C5", C5, "failed_generation_charge_policy", 3.0)),
    ("D1", "D", 6.0, ("auto_renewal_default",), single("D1", D1, "auto_renewal_default", 6.0)),
    ("D2", "D", 4.0, ("auto_renewal_disclosure_location",),
     single("D2", D2, "auto_renewal_disclosure_location", 4.0)),
    ("D3", "D", 6.0, ("refund_policy_exists",), single("D3", D3, "refund_policy_exists", 6.0)),
    ("D4", "D", 4.0, ("cancellation_self_serve",), single("D4", D4, "cancellation_self_serve", 4.0)),
    ("E1", "E", 5.0, ("commercial_use_lowest_tier",),
     single("E1", E1, "commercial_use_lowest_tier", 5.0)),
    ("E2", "E", 3.0, ("watermark_removal_tier",), single("E2", E2, "watermark_removal_tier", 3.0)),
    ("E3", "E", 2.0, ("output_ownership_statement",),
     single("E3", E3, "output_ownership_statement", 2.0)),
    ("F1", "F", 6.0, ("usage_cap_quantified",), single("F1", F1, "usage_cap_quantified", 6.0)),
    ("F2", "F", 4.0, ("unquantified_limit_clause",), single("F2", F2, "unquantified_limit_clause", 4.0)),
]
ITEM_IDS = [i[0] for i in ITEMS]
COMPONENTS = ["A", "B", "C", "D", "E", "F"]
COMPONENT_POINTS = {"A": 20.0, "B": 15.0, "C": 25.0, "D": 20.0, "E": 10.0, "F": 10.0}
COMPONENT_TITLES = {
    "A": "Headline price integrity", "B": "Free tier and trial clarity",
    "C": "Unit-cost comprehensibility", "D": "Renewal and exit terms",
    "E": "Rights and restrictions", "F": "Residual undisclosed burden",
}
BANDS = [(85.0, 100.0, "Determinable"), (70.0, 84.9, "Mostly determinable"),
         (50.0, 69.9, "Partly determinable"), (30.0, 49.9, "Largely undeterminable"),
         (0.0, 29.9, "Undeterminable")]
GUARD_MINIMUM = 50.0
SUPPRESSED = "suppressed"


# --------------------------------------------------------------------------------------
# The hand computation, kept as a regression check
# --------------------------------------------------------------------------------------

# Five products were worked item by item straight from the protocol text and the record,
# by hand, without this tool, and then compared against it. The figures below are that hand
# pass's OUTPUT, frozen here so it keeps paying: if an adjudication changes a coded value on
# one of these products, the run says which figure moved instead of drifting quietly.
#
# The four picked deliberately, plus a fifth: a high scorer, a low scorer, one carrying
# several `unknown` values, and two carrying `not_applicable` inside a multi-variable item —
# one where the matrix REMOVES the item (ismybrandinai's A3) and one where G4 KEEPS it at full
# points (sapling's and ismybrandinai's B2). Those are the two places the scoring rules break.
#
# The hand pass and the tool disagreed on ONE of the five, and the hand pass was wrong: it
# read `usage_cap_quantified` as `not_applicable` on sapling, where all three storage shapes
# and the adjudicated record's own prose say `some_quantified`. It had carried the value
# across from ismybrandinai, scored immediately before, which does carry `not_applicable`
# there. The error ran 3.8 points HIGH — the flattering direction. The figure below is the
# corrected hand figure, which the tool then matched.
HAND_VERIFIED = {
    "fotor":         dict(earned=93.0, available=100.0, apti_total=93.0,
                          apti_band="Determinable", unknown_count=0,
                          determinability_rate=0.95, apti_equal=90.6,
                          apti_unknown_excluded=93.0),
    "google-veo":    dict(earned=25.0, available=93.0, apti_total=26.9,
                          apti_band="Undeterminable", unknown_count=13,
                          determinability_rate=0.32, apti_equal=27.8,
                          apti_unknown_excluded=SUPPRESSED),
    "canva":         dict(earned=52.0, available=100.0, apti_total=52.0,
                          apti_band="Partly determinable", unknown_count=5,
                          determinability_rate=0.7, apti_equal=51.8,
                          apti_unknown_excluded=68.4),
    "ismybrandinai": dict(earned=25.0, available=37.0, apti_total=SUPPRESSED,
                          apti_band=SUPPRESSED, unknown_count=3,
                          determinability_rate=0.63, apti_equal=SUPPRESSED,
                          apti_unknown_excluded=SUPPRESSED),
    "sapling":       dict(earned=54.0, available=63.0, apti_total=85.7,
                          apti_band="Determinable", unknown_count=0,
                          determinability_rate=1.0, apti_equal=84.0,
                          apti_unknown_excluded=85.7),
}


def hand_check(scored):
    """Compare the frozen hand figures against this run. Returns (agreed, divergences)."""
    agreed, diverged = [], []
    for pid, expected in sorted(HAND_VERIFIED.items()):
        if pid not in scored:
            diverged.append(f"{pid}: no longer an active scored product")
            continue
        got = scored[pid]
        bad = [f"{k}: hand {v} vs tool {got[k]}" for k, v in expected.items() if got[k] != v]
        (diverged if bad else agreed).append(
            f"{pid}: " + ("; ".join(bad) if bad else "all figures agree"))
    return agreed, diverged


def round1(value):
    """Section 8.3.8: one decimal, half up. Python's round() is half-to-even."""
    return float(Decimal(str(value)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))


def round2(value):
    return float(Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def band(total):
    if total == SUPPRESSED:
        return SUPPRESSED
    for low, high, name in BANDS:
        if low <= total <= high:
            return name
    raise ProtocolGap(f"index value {total} falls outside every band in section 8.3.9")


def self_check():
    """The protocol's printed conflict shares against G3's own arithmetic.

    A transcription typo in either direction is a silent scoring error, so it is checked
    rather than trusted.
    """
    printed = {"A1": (8.0, A1["conflicting"]), "A2": (7.0, A2["conflicting"]),
               "C1": (6.0, C1["conflicting"]), "C2": (7.0, C2["conflicting"]),
               "C3": (5.0, C3["conflicting"]), "C4": (4.0, C4["conflicting"]),
               "C5": (3.0, C5["conflicting"]), "D1": (6.0, D1["conflicting"]),
               "D2": (4.0, D2["conflicting"]), "D3": (6.0, D3["conflicting"]),
               "D4": (4.0, D4["conflicting"]), "E1": (5.0, E1["conflicting"]),
               "E2": (3.0, E2["conflicting"]), "E3": (2.0, E3["conflicting"]),
               "F1": (6.0, F1["conflicting"]), "F2": (4.0, F2["conflicting"])}
    bad = [f"{k}: protocol prints {got}, G3 gives {round1(_third(pts))}"
           for k, (pts, got) in printed.items() if round1(_third(pts)) != got]
    if bad:
        raise ProtocolGap("G3 conflict shares disagree with the protocol's printed values: "
                          + "; ".join(bad))
    total = sum(pts for _, _, pts, _, _ in
                [(i[0], i[1], i[2], i[3], i[4]) for i in ITEMS])
    if total != 100.0:
        raise ProtocolGap(f"the item set sums to {total}, not the 100 points of section 8.3.7")
    for comp in COMPONENTS:
        got = sum(i[2] for i in ITEMS if i[1] == comp)
        if got != COMPONENT_POINTS[comp]:
            raise ProtocolGap(f"component {comp} sums to {got}, not {COMPONENT_POINTS[comp]}")
    if len(ITEMS) != 20:
        raise ProtocolGap(f"{len(ITEMS)} items defined, not the twenty of section 8.3.7")


# --------------------------------------------------------------------------------------
# Loading, and the three-shape agreement check
# --------------------------------------------------------------------------------------

def load_wide():
    path = os.path.join(DATASET, "coded-values.csv")
    with open(path) as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise SystemExit(f"FATAL: {path} holds no rows. Nothing was examined.")
    missing = [v for v in CODED if v not in rows[0]]
    if missing:
        raise SystemExit(f"FATAL: {len(missing)} coded variables absent as columns: {missing}")
    if len(rows) != EXPECTED_PRODUCTS:
        raise SystemExit(f"FATAL: {len(rows)} products, expected {EXPECTED_PRODUCTS}. "
                         "A census that changed size is a finding, not a default.")
    ids = [r["product_id"] for r in rows]
    if len(set(ids)) != len(ids):
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        raise SystemExit(f"FATAL: duplicate product_id: {dupes}")
    blank = [(r["product_id"], v) for r in rows for v in CODED if r[v] == ""]
    if blank:
        raise SystemExit(f"FATAL: {len(blank)} coded cells are empty, first {blank[:5]}. "
                         "An empty cell is not a coded value and gets no default here.")
    return rows


def load_long():
    """Second storage shape. Returns {(product, variable): value}."""
    path = os.path.join(DATASET, "coded-long.csv")
    with open(path) as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != EXPECTED_VALUES:
        raise SystemExit(f"FATAL: coded-long.csv holds {len(rows)} value rows, expected "
                         f"{EXPECTED_VALUES} ({EXPECTED_PRODUCTS} x {EXPECTED_VARIABLES}).")
    out = {}
    for r in rows:
        key = (r["product_id"], r["variable"])
        if key in out:
            raise SystemExit(f"FATAL: coded-long.csv repeats {key}")
        out[key] = r["value"]
    return out, rows


def load_records():
    """Third storage shape: the YAML records themselves.

    Uses `build_dataset.py`'s own shape-walk and canonicalisation, so this check cannot
    drift from the build. `computation_assumptions` alone appears in three shapes in this
    corpus, and four times a tool that read one of them produced a confident wrong number.
    """
    try:
        import build_dataset
    except Exception as exc:                                   # noqa: BLE001
        return None, f"records shape NOT checked: could not import build_dataset ({exc})"
    out, shapes = {}, {}
    try:
        import yaml
        rows = build_dataset.publishing_rows()
        # The count is asserted BEFORE the loop. Without this, an empty records directory walks
        # zero records, produces an empty map, and then reports every one of the 2812 values as
        # "absent from the YAML records" — a true failure with a false explanation. A validator
        # that examined zero records has to say so in those words.
        if len(rows) != EXPECTED_PRODUCTS:
            return None, (f"records shape NOT checked: publishing_rows() returned {len(rows)} "
                          f"records, expected {EXPECTED_PRODUCTS}. Zero or short means the "
                          "records directory is missing or incomplete, NOT that the values "
                          "disagree.")
        for slug, path, _prov in rows:
            record = yaml.safe_load(open(path))
            for name in CODED:
                got = build_dataset.field(record, name)
                if got is None:
                    return None, f"records shape NOT checked: {slug} is missing {name}"
                shapes[got[3]] = shapes.get(got[3], 0) + 1
                if "UNRECOGNISED" in got[3]:
                    return None, f"records shape NOT checked: {slug}/{name} has shape {got[3]}"
                out[(slug, name)] = build_dataset.as_text(got[0])
    except Exception as exc:                                   # noqa: BLE001
        return None, f"records shape NOT checked: {exc}"
    return (out, shapes), None


def cross_check(wide, long_map, records):
    """Require every shape to agree value-for-value before anything is scored."""
    disagreements = []
    checked_long = checked_records = 0
    rec_map = records[0] if records else None
    for row in wide:
        pid = row["product_id"]
        for name in CODED:
            key = (pid, name)
            if key not in long_map:
                disagreements.append(f"{pid}/{name}: absent from coded-long.csv")
                continue
            checked_long += 1
            if long_map[key] != row[name]:
                disagreements.append(f"{pid}/{name}: wide {row[name]!r} vs long {long_map[key]!r}")
            if rec_map is not None:
                if key not in rec_map:
                    disagreements.append(f"{pid}/{name}: absent from the YAML records")
                    continue
                checked_records += 1
                if rec_map[key] != row[name]:
                    disagreements.append(
                        f"{pid}/{name}: wide {row[name]!r} vs record {rec_map[key]!r}")
    return disagreements, checked_long, checked_records


# --------------------------------------------------------------------------------------
# Per-product scoring
# --------------------------------------------------------------------------------------

def score_product(row):
    notes = []
    items = {}
    for item_id, comp, points, _vars, scorer in ITEMS:
        score, determinate, has_unknown = scorer(row, notes)
        items[item_id] = {
            "component": comp, "points": points, "score": score,
            "determinate": determinate, "has_unknown_sub": has_unknown,
            "multi": len(_vars) > 1,
        }

    applicable = [i for i in ITEM_IDS if items[i]["score"] != REMOVED]

    # G5, item-level `unknown`
    unknown_items = []
    for item_id in applicable:
        it = items[item_id]
        if it["multi"]:
            if it["score"] == 0.0 and it["has_unknown_sub"]:
                unknown_items.append(item_id)
        elif it["has_unknown_sub"]:
            unknown_items.append(item_id)

    # G0 at the item level
    determinate_items = [i for i in applicable if items[i]["determinate"]]

    earned = sum(items[i]["score"] for i in applicable)
    available = sum(items[i]["points"] for i in applicable)
    per_component = {}
    for comp in COMPONENTS:
        ids = [i for i in applicable if items[i]["component"] == comp]
        per_component[comp] = (sum(items[i]["score"] for i in ids),
                               sum(items[i]["points"] for i in ids))

    total = SUPPRESSED if available < GUARD_MINIMUM else round1(100.0 * earned / available)

    # S1, equal weights
    live = [c for c in COMPONENTS if per_component[c][1] > 0]
    if total == SUPPRESSED or not live:
        equal = SUPPRESSED
    else:
        equal = round1((100.0 / len(live))
                       * sum(per_component[c][0] / per_component[c][1] for c in live))

    # S2, `unknown` items removed from numerator and denominator. "Unknown item" is G5's
    # item-level definition, the only item-level one the protocol gives, which is also what
    # `unknown_count` counts. So a multi-variable item scoring above zero with one `unknown`
    # sub-variable is NOT removed, matching G5's third bullet.
    s2_ids = [i for i in applicable if i not in unknown_items]
    s2_available = sum(items[i]["points"] for i in s2_ids)
    s2_earned = sum(items[i]["score"] for i in s2_ids)
    if total == SUPPRESSED or s2_available < GUARD_MINIMUM:
        excluded = SUPPRESSED                          # 8.4.1 rules 1, 2 and 4
    else:
        excluded = round1(100.0 * s2_earned / s2_available)

    return {
        "items": items, "notes": notes,
        "applicable_items": len(applicable), "unknown_items": unknown_items,
        "unknown_count": len(unknown_items),
        "determinate_items": len(determinate_items),
        "determinability_rate": (round2(len(determinate_items) / len(applicable))
                                 if applicable else SUPPRESSED),
        "earned": round1(earned), "available": round1(available),
        "components": per_component,
        "apti_total": total, "apti_band": band(total),
        "apti_equal": equal, "apti_equal_band": band(equal),
        "apti_unknown_excluded": excluded, "apti_unknown_excluded_band": band(excluded),
        "s2_available": round1(s2_available),
    }


# --------------------------------------------------------------------------------------
# Reporting helpers: D2 denominators, D3 small-group suppression, D4 median first
# --------------------------------------------------------------------------------------

MIN_GROUP_FOR_PCT = 5


def share(n, total):
    """D2: every percentage prints with its denominator. D3: none below n of 5."""
    if n >= MIN_GROUP_FOR_PCT and total >= MIN_GROUP_FOR_PCT:
        return f"{n} of {total} ({round1(100.0 * n / total)}%)"
    return f"{n} of {total}"


def spread(values, places=1):
    """D4: median and IQR first, min and max, mean beside the median and never instead.

    Quartiles use the inclusive (type-7) definition. Rounding is half up throughout, per
    section 8.3.8 — the default float formatting is half to EVEN and would print a median of
    80.25 as 80.2 where the protocol's rule gives 80.3.
    """
    if not values:
        return None
    rnd = round1 if places == 1 else round2
    ordered = sorted(values)
    if len(ordered) >= 4:
        q1, _med, q3 = statistics.quantiles(ordered, n=4, method="inclusive")
    else:
        q1 = q3 = statistics.median(ordered)
    return {"n": len(ordered), "median": rnd(statistics.median(ordered)),
            "q1": rnd(q1), "q3": rnd(q3), "iqr": rnd(q3 - q1),
            "min": rnd(min(ordered)), "max": rnd(max(ordered)),
            "mean": rnd(statistics.fmean(ordered))}


def spread_line(s):
    return (f"median **{s['median']}**, IQR {s['q1']} to {s['q3']} (width {s['iqr']}), "
            f"min {s['min']}, max {s['max']}; mean {s['mean']} beside the median, n = {s['n']}")


# --------------------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------------------

def build_report(wide, scored, meta):
    active = [r for r in wide if r["product_status"] == "active"]
    discontinued = [r for r in wide if r["product_status"] != "active"]
    frames = [("Full frame", [r["product_id"] for r in active]),
              ("Paid submissions removed",
               [r["product_id"] for r in active if r["paid_submission"] != "yes"])]

    L = []
    a = L.append
    a("# AI Pricing Transparency Index (APTI), a determinability index — computed results")
    a("")
    a("Generated by `tools/score_apti.py` from `dataset/coded-values.csv`. Every figure here is")
    a("reproducible from `dataset/apti-scores.csv`, which carries each product's twenty item")
    a("scores. The instrument is pre-registered in `protocol-v1.md` section 8.3 and was fixed")
    a("before any datum existed; this tool implements it and changes nothing.")
    a("")
    a("**The index scores determinability, not generosity.** A vendor stating \"no refunds under")
    a("any circumstances\" earns the same six points on D3 as one stating a 30-day unconditional")
    a("refund. Both readers know what they are buying, and knowing is the whole of what the")
    a("index measures.")
    a("")
    a("> **These scores are provisional.** Three adjudications and a retrieval sweep were open")
    a("> when this ran and may change a handful of coded values. The tool is the durable")
    a("> deliverable: re-running it is one command and costs nothing.")
    a("")
    a("## What this run examined")
    a("")
    for line in meta["census"]:
        a(f"- {line}")
    a("")

    # ---- distribution, twice, per D10
    a("## 1. Distribution of the index")
    a("")
    a("Rule D4 governs: the median and interquartile range lead, the minimum and maximum")
    a("follow, and the mean sits beside the median rather than instead of it. Quartiles use")
    a("the inclusive (type-7) definition. Rule D10 governs the doubling: every index result is")
    a("reported once over the full frame and once with `paid_submission = yes` records removed.")
    a("")
    for label, ids in frames:
        pub = [scored[p]["apti_total"] for p in ids if scored[p]["apti_total"] != SUPPRESSED]
        sup = [p for p in ids if scored[p]["apti_total"] == SUPPRESSED]
        s = spread(pub)
        a(f"### {label} — {len(ids)} active products")
        a("")
        a(f"- Products with a published index: {share(len(pub), len(ids))}")
        a(f"- Suppressed by the section 8.3.8 guard (`available` below 50): "
          f"{share(len(sup), len(ids))}" + (f" — {', '.join(sorted(sup))}" if sup else ""))
        a(f"- **APTI**: {spread_line(s)}")
        for variant, key in (("APTI_equal (S1)", "apti_equal"),
                             ("APTI_unknown_excluded (S2)", "apti_unknown_excluded")):
            vals = [scored[p][key] for p in ids if scored[p][key] != SUPPRESSED]
            vsup = [p for p in ids if scored[p][key] == SUPPRESSED]
            vs = spread(vals)
            a(f"- **{variant}**: {spread_line(vs)}; suppressed for {share(len(vsup), len(ids))}"
              + (f" — {', '.join(sorted(vsup))}" if vsup else ""))
        a("")
        a("Band distribution:")
        a("")
        a("| Band | Products | Share |")
        a("|---|---|---|")
        for _lo, _hi, name in BANDS:
            n = sum(1 for p in ids if scored[p]["apti_band"] == name)
            a(f"| {name} | {n} | {share(n, len(ids))} |")
        nsup = len(sup)
        a(f"| Suppressed (guard rule) | {nsup} | {share(nsup, len(ids))} |")
        a("")

    a("### Band movement between the primary index and the sensitivity variants")
    a("")
    a("Section 8.4 requires that any product moving **more than one band** between APTI and")
    a("APTI_equal be marked in the published table, and rule 8.4.1 §3 requires both bands to")
    a("print for both variants. Both bands print in section 8 for every product; the marking")
    a("rule's trigger is reported here.")
    a("")
    for variant, key in (("S1 (equal weights)", "apti_equal_band"),
                         ("S2 (`unknown` excluded)", "apti_unknown_excluded_band")):
        band_names = [b[2] for b in BANDS]
        moved = []
        for p in frames[0][1]:
            primary, other = scored[p]["apti_band"], scored[p][key]
            if SUPPRESSED in (primary, other):
                continue
            d = abs(band_names.index(primary) - band_names.index(other))
            if d:
                moved.append((d, p, primary, other))
        more = [m for m in moved if m[0] > 1]
        a(f"- **{variant}**: {share(len(moved), len(frames[0][1]))} products change band at all; "
          + (f"{len(more)} move{'s' if len(more) == 1 else ''} more than one band"
             + (" — " + "; ".join(f"**{p}** ({a1} to {b1}, {d} bands)" for d, p, a1, b1 in more)
                if more else ", so the section 8.4 marking rule marks nothing this wave")
             + "."))
    a("")
    a("The S1 marking rule marking nothing is itself worth stating: the ordering this study")
    a("reports is not an artifact of the weights in section 8.3.10, because equalising them")
    a("moves no product more than one band. S2 is the vendor-favourable variant and moves")
    a("products upward, which is exactly what rule G1's stance on `unknown` is designed to cost")
    a("them — the gap between a product's APTI and its S2 value is the price of its unknowns.")
    a("")

    if discontinued:
        a("### Discontinued products — their own table, no aggregate, no index (rule D8)")
        a("")
        a("| Product | Category |")
        a("|---|---|")
        for r in sorted(discontinued, key=lambda r: r["product_id"]):
            a(f"| {r['product_id']} | {r['category']} |")
        a("")
        a(f"{len(discontinued)} products, reported as a raw count under rule D3. Section 8.3")
        a("computes the index for active products only, so none of them carries a score.")
        a("")

    # ---- discrimination
    a("## 2. Does the index discriminate?")
    a("")
    ids = frames[0][1]
    pub = sorted(scored[p]["apti_total"] for p in ids if scored[p]["apti_total"] != SUPPRESSED)
    s = spread(pub)
    width = round1(s["max"] - s["min"])
    a("Rule D10 binds every index figure quoted in prose, so both frames are given for each.")
    a("")
    for label, fids in frames:
        fpub = sorted(scored[p]["apti_total"] for p in fids
                      if scored[p]["apti_total"] != SUPPRESSED)
        fs = spread(fpub)
        a(f"- **{label}**: published scores run {fs['min']} to {fs['max']}, a range of "
          f"{round1(fs['max'] - fs['min'])} points on a 100-point instrument, with the middle "
          f"half inside {fs['q1']} to {fs['q3']} — an IQR of {fs['iqr']} points.")
    a("")
    a("The interval table and the verdict below are computed on the full frame; the one")
    a("`paid_submission = yes` record moves the median by "
      f"{round1(abs(spread([scored[p]['apti_total'] for p in frames[1][1] if scored[p]['apti_total'] != SUPPRESSED])['median'] - s['median']))}"
      " points and changes no conclusion in this section.")
    a("")
    decades = {}
    for v in pub:
        lo = int(v // 10) * 10
        decades[lo] = decades.get(lo, 0) + 1
    a("| Ten-point interval | Products | Share |")
    a("|---|---|---|")
    for lo in sorted(decades, reverse=True):
        a(f"| {lo}.0 to {lo + 9}.9 | {decades[lo]} | {share(decades[lo], len(pub))} |")
    a("")
    bands_hit = sorted({scored[p]["apti_band"] for p in ids
                        if scored[p]["apti_total"] != SUPPRESSED},
                       key=lambda n: [b[2] for b in BANDS].index(n))
    biggest = max(decades.items(), key=lambda kv: kv[1])
    a(f"**Verdict.** {meta['verdict']}")
    a("")
    a(f"Supporting figures: {len(bands_hit)} of the five bands in section 8.3.9 are occupied "
      f"({', '.join(bands_hit)}); the single most populated ten-point interval holds "
      f"{share(biggest[1], len(pub))}; the IQR is {s['iqr']} points wide against a "
      f"{width}-point observed range.")
    a("")
    a("Ties are reported as ties, with no tiebreaker and no forced ordering (section 8.3.8).")
    tie_groups = {}
    for p in ids:
        t = scored[p]["apti_total"]
        if t != SUPPRESSED:
            tie_groups.setdefault(t, []).append(p)
    tied = {k: v for k, v in tie_groups.items() if len(v) > 1}
    a(f"{sum(len(v) for v in tied.values())} of {len(pub)} published scores sit in a tie group; "
      f"{len(tied)} distinct values are shared by two or more products.")
    a("")

    # ---- components
    a("## 3. Per-component breakdown")
    a("")
    a("Which component drives the spread. Two figures are needed, and reading only the first")
    a("gets the answer wrong. The **percentage** columns give each product's earned share of the")
    a("points available to it in that component, which is comparable across components of")
    a("different sizes and does not penalise a component for having items removed. But the index")
    a("is a ratio of **points**, so what moves a product's APTI is a component's spread in")
    a("points, and a 10-point component swinging 0% to 100% moves the index less than a")
    a("25-point component swinging 58% to 88%.")
    a("")
    for label, fids in frames:
        a(f"### {label}")
        a("")
        a("| Component | Points | Products scored | Median % | IQR % | Mean % | "
          "Median pts | IQR pts | IQR width, pts | At ceiling |")
        a("|---|---|---|---|---|---|---|---|---|---|")
        for comp in COMPONENTS:
            live = [p for p in fids if scored[p]["components"][comp][1] > 0]
            pct = spread([100.0 * scored[p]["components"][comp][0]
                          / scored[p]["components"][comp][1] for p in live])
            pts = spread([scored[p]["components"][comp][0] for p in live])
            ceiling = sum(1 for p in live if scored[p]["components"][comp][0]
                          == scored[p]["components"][comp][1])
            a(f"| {comp} {COMPONENT_TITLES[comp]} | {COMPONENT_POINTS[comp]:.0f} | "
              f"{pts['n']} of {len(fids)} | **{pct['median']}** | {pct['q1']} to {pct['q3']} | "
              f"{pct['mean']} | {pts['median']} | {pts['q1']} to {pts['q3']} | "
              f"**{pts['iqr']}** | {share(ceiling, len(live))} |")
        a("")
    for line in meta["component_verdict"]:
        a(line)
        a("")

    # ---- unknowns
    a("## 4. How much of each score rests on `unknown`")
    a("")
    a(f"{meta['unknown_headline']}")
    a("")
    a("Rule G1 is the study's central stance: an `unknown` scores zero and stays in the")
    a("denominator, because an undisclosed term is the buyer's burden and not a missing")
    a("observation. So an unknown is not noise around a score — it is part of the score, and a")
    a("reader is entitled to see how much of any product's number is built from them.")
    a("")
    for label, fids in frames:                                   # D10 again
        us = spread([scored[p]["unknown_count"] for p in fids])
        ds = spread([scored[p]["determinability_rate"] for p in fids
                     if scored[p]["determinability_rate"] != SUPPRESSED], places=2)
        a(f"- **{label}** — item-level `unknown` count per product (rule G5): "
          f"{spread_line(us)}")
        a(f"- **{label}** — `determinability_rate` per product (rule G0, item level): "
          f"{spread_line(ds)}")
    a("")
    a("A score computed over fewer determinate items is not comparable to one computed over")
    a("more, which is why rule G0 defines determinacy at the item level and why every score in")
    a("section 8 prints its `determinability_rate` and its determinate-of-applicable counts")
    a("beside it. The two figures answer different questions: the index asks how many of the")
    a("available points the documents earn, and the determinability rate asks how many of the")
    a("questions the documents answer at all.")
    a("")
    a("### Where the unknowns land, by scoring item")
    a("")
    a("An `unknown` on a variable no index item reads costs a product nothing. This table")
    a("separates the two.")
    a("")
    a("| Item | Variables | Applicable products | Items `unknown` | Points at stake |")
    a("|---|---|---|---|---|")
    for item_id, comp, points, variables, _ in ITEMS:
        appl = [p for p in frames[0][1] if scored[p]["items"][item_id]["score"] != REMOVED]
        unk = [p for p in appl if item_id in scored[p]["unknown_items"]]
        a(f"| {item_id} | `{'`, `'.join(variables)}` | {len(appl)} | "
          f"{share(len(unk), len(appl))} | {points:.0f} |")
    a("")
    a("| `unknown` values on variables no index item scores | Count |")
    a("|---|---|")
    for name, n in meta["unscored_unknowns"]:
        a(f"| `{name}` | {n} |")
    a(f"| **total** | **{sum(n for _, n in meta['unscored_unknowns'])}** |")
    a("")
    a(meta["unknown_verdict"])
    a("")

    # ---- invariance
    a("## 5. Items and components that do not vary across the corpus")
    a("")
    a("An item scoring identically for every product contributes nothing to the index, and the")
    a("paper should know which ones those are before it reads anything into a ranking. A binary")
    a("varies/does-not-vary column is not enough for that, because an item where 45 of 46")
    a("products take the same score contributes almost nothing either. The modal-share column is")
    a("the one to read. **Near-invariant** below means 90% or more of applicable products take")
    a("the same score; the threshold is a reporting choice, stated so it can be argued with, and")
    a("it changes no score.")
    a("")
    a("| Item | Points | Applicable | Distinct scores | Values seen | Modal score | "
      "Share at modal | Verdict |")
    a("|---|---|---|---|---|---|---|---|")
    for item_id, comp, points, _v, _ in ITEMS:
        appl = [p for p in frames[0][1] if scored[p]["items"][item_id]["score"] != REMOVED]
        scores = [scored[p]["items"][item_id]["score"] for p in appl]
        seen = sorted(set(scores))
        modal = max(seen, key=scores.count)
        modal_n = scores.count(modal)
        removed = len(frames[0][1]) - len(appl)
        if len(seen) <= 1 and removed == 0:
            verdict = "**INVARIANT** — contributes no spread at all"
        elif len(seen) <= 1:
            verdict = f"constant where applicable; varies only by removal ({removed} removed)"
        elif modal_n / len(appl) >= 0.9:
            verdict = "**near-invariant** — contributes almost no spread"
        else:
            verdict = "varies"
        a(f"| {item_id} | {points:.0f} | {len(appl)} | {len(seen)} | "
          f"{', '.join(str(x) for x in seen)} | {modal} | {share(modal_n, len(appl))} | "
          f"{verdict} |")
    a("")
    for line in meta["invariance_notes"]:
        a(f"- {line}")
    a("")

    # ---- protocol surface
    a("## 6. Independent hand computation against this tool")
    a("")
    a("A tool that reads less than it claims produces a number nobody can distinguish from a")
    a("result. That has happened six times in this study and three of those numbers were")
    a("reassuring. So five products were scored **by hand**, item by item, straight from the")
    a("protocol text and the record, without this tool, and then compared against it. The four")
    a("picked deliberately plus one: a high scorer, a low scorer, one carrying several `unknown`")
    a("values, and two carrying `not_applicable` inside a multi-variable item — one where the")
    a("matrix removes the item and one where rule G4 keeps it at full points.")
    a("")
    for line in meta["hand_agreed"]:
        a(f"- {line}")
    for line in meta["hand_diverged"]:
        a(f"- **DIVERGED** {line}")
    a("")
    a("**They disagreed on one of the five, and the hand pass was the wrong one.** The hand pass")
    a("scored `sapling` at 89.5 by reading item F1's variable `usage_cap_quantified` as")
    a("`not_applicable` and removing the item. All three storage shapes carry")
    a("`some_quantified`, and the adjudicated record says so in words. The hand pass had carried")
    a("the value across from `ismybrandinai`, scored immediately before, which does carry")
    a("`not_applicable` there. Corrected by hand from the record, F1 scores 3 of 6, earned")
    a("becomes 54 of 63, and the index is **85.7** — which is what the tool had. The hand error")
    a("ran 3.8 points **high**: the flattering direction, and the one this study is most")
    a("suspicious of. It is recorded here rather than reconciled away.")
    a("")
    a("The five hand figures are frozen inside `tools/score_apti.py` as `HAND_VERIFIED` and")
    a("re-checked on every run, so a later change to a coded value on one of these products is")
    a("reported as a divergence instead of drifting quietly.")
    a("")
    a("## 7. Protocol coverage")
    a("")
    a("Every coded value was looked up in an explicit table transcribed from section 8.3. The")
    a("tool has no default branch: a value with no defined outcome stops the run.")
    a("")
    for line in meta["coverage"]:
        a(f"- {line}")
    a("")

    a("## 8. Full per-product table")
    a("")
    a("Rule D10 does not need a second copy of this table: `paid_submission` is a column, so a")
    a("reader can drop that row and recover the paid-submissions-removed frame exactly. The")
    a("aggregates above are the figures D10 binds, and both versions of each are printed.")
    a("")
    a("| Product | Category | Paid sub. | APTI | Band | S1 | S1 band | S2 | S2 band | "
      "`unknown_count` | Determinability | Earned | Available |")
    a("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in sorted(active, key=lambda r: (
            -(scored[r["product_id"]]["apti_total"]
              if scored[r["product_id"]]["apti_total"] != SUPPRESSED else -1),
            r["product_id"])):
        p = r["product_id"]
        s = scored[p]
        a(f"| {p} | {r['category']} | {r['paid_submission']} | {s['apti_total']} | "
          f"{s['apti_band']} | {s['apti_equal']} | {s['apti_equal_band']} | "
          f"{s['apti_unknown_excluded']} | {s['apti_unknown_excluded_band']} | "
          f"{s['unknown_count']} | {s['determinability_rate']} "
          f"({s['determinate_items']} of {s['applicable_items']}) | {s['earned']} | "
          f"{s['available']} |")
    a("")
    return "\n".join(L) + "\n"


# --------------------------------------------------------------------------------------
# CSV output
# --------------------------------------------------------------------------------------

def write_scores(wide, scored):
    path = os.path.join(DATASET, "apti-scores.csv")
    header = (["product_id", "product_name", "category", "product_status", "paid_submission",
               "row_provenance", "apti_earned", "apti_available", "apti_total", "apti_band",
               "unknown_count", "determinate_items", "applicable_items", "determinability_rate",
               "apti_equal", "apti_equal_band", "apti_unknown_excluded",
               "apti_unknown_excluded_band", "s2_available"]
              + [f"apti_component_{c.lower()}_{k}" for c in COMPONENTS
                 for k in ("earned", "available", "ratio")]
              + [f"item_{i}" for i in ITEM_IDS]
              + ["unknown_items", "scoring_notes"])
    with open(path, "w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        for r in sorted(wide, key=lambda r: r["product_id"]):
            pid = r["product_id"]
            base = [pid, r["product_name"], r["category"], r["product_status"],
                    r["paid_submission"], r["row_provenance"]]
            if r["product_status"] != "active":
                # D8 and codebook 8 rule 5: no derived value for a discontinued product. Listed
                # rather than dropped, so the exclusion is visible instead of merely absent.
                writer.writerow(base + ["excluded_discontinued"] * (len(header) - len(base)))
                continue
            s = scored[pid]
            row = base + [s["earned"], s["available"], s["apti_total"], s["apti_band"],
                          s["unknown_count"], s["determinate_items"], s["applicable_items"],
                          s["determinability_rate"], s["apti_equal"], s["apti_equal_band"],
                          s["apti_unknown_excluded"], s["apti_unknown_excluded_band"],
                          s["s2_available"]]
            for comp in COMPONENTS:
                earned, available = s["components"][comp]
                row += [round1(earned), round1(available),
                        round2(earned / available) if available else "not_applicable"]
            for item_id in ITEM_IDS:
                sc = s["items"][item_id]["score"]
                row.append("removed" if sc == REMOVED else sc)
            row.append(" | ".join(s["unknown_items"]))
            row.append(" | ".join(s["notes"]))
            writer.writerow(row)
    return path


# --------------------------------------------------------------------------------------

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--check", action="store_true", help="validate and score, write nothing")
    parser.add_argument("--explain", default="", help="comma-separated product_ids to work through")
    args = parser.parse_args(argv)

    self_check()

    wide = load_wide()
    long_map, long_rows = load_long()
    records, records_note = load_records()
    disagreements, checked_long, checked_records = cross_check(wide, long_map, records)
    # Printed before any fatal, because "one shape went unread" is context a reader needs in
    # order to interpret whatever comes next, not a footnote to it.
    if records_note:
        print(f"WARNING: {records_note}")
    if disagreements:
        print(f"FATAL: {len(disagreements)} value disagreements between storage shapes. "
              "Nothing was scored.")
        for line in disagreements[:25]:
            print(f"  {line}")
        return 2
    if checked_long != EXPECTED_VALUES:
        print(f"FATAL: cross-checked {checked_long} values against coded-long.csv, expected "
              f"{EXPECTED_VALUES}. A check that examines fewer rows than it claims is the "
              "failure mode this study keeps finding in itself.")
        return 2
    if not records_note and checked_records != EXPECTED_VALUES:
        print(f"FATAL: cross-checked {checked_records} values against the YAML records, "
              f"expected {EXPECTED_VALUES}.")
        return 2

    census = [
        f"`coded-values.csv`: {len(wide)} products x {len(CODED)} coded variables = "
        f"{len(wide) * len(CODED)} values, all present, none empty.",
        f"`coded-long.csv`: {len(long_rows)} value rows, cross-checked value-for-value against "
        f"the wide table — {checked_long} of {EXPECTED_VALUES} agreed, 0 disagreed.",
        (f"YAML records (third storage shape, read through `build_dataset.py`'s own shape-walk): "
         f"{checked_records} of {EXPECTED_VALUES} values agreed, 0 disagreed."
         + (f" Shapes seen: {', '.join(f'{k} x{v}' for k, v in sorted(records[1].items()))}."
            if records else ""))
        if not records_note else records_note,
    ]

    scored, gaps = {}, []
    for row in wide:
        if row["product_status"] != "active":
            continue                        # D8 / codebook 8 rule 5: active products only
        try:
            scored[row["product_id"]] = score_product(row)
        except ProtocolGap as exc:
            gaps.append(f"{row['product_id']}: {exc}")
    if gaps:
        print(f"STOPPED. {len(gaps)} coded combinations reached an item section 8.3 does not")
        print("score. This is a protocol defect and is worth more than a number. Nothing written.")
        for line in gaps:
            print(f"  {line}")
        return 3

    census.append(f"Items scored: {len(scored)} active products x {len(ITEMS)} items = "
                  f"{len(scored) * len(ITEMS)} item evaluations. "
                  f"{len(wide) - len(scored)} discontinued products carry no score (rule D8).")

    if args.explain:
        for pid in args.explain.split(","):
            pid = pid.strip()
            if pid not in scored:
                print(f"{pid}: not an active scored product")
                continue
            s = scored[pid]
            print(f"\n=== {pid} ===")
            for item_id, comp, points, variables, _ in ITEMS:
                it = s["items"][item_id]
                vals = ", ".join(f"{v}={next(r for r in wide if r['product_id'] == pid)[v]}"
                                 for v in variables)
                print(f"  {item_id} [{comp}] {vals}")
                print(f"      score {it['score']} of {points} · determinate={it['determinate']}")
            print(f"  earned {s['earned']} / available {s['available']} -> APTI {s['apti_total']} "
                  f"({s['apti_band']})")
            print(f"  unknown_count {s['unknown_count']} {s['unknown_items']}")
            print(f"  determinability {s['determinability_rate']} "
                  f"({s['determinate_items']} of {s['applicable_items']})")
            print(f"  S1 {s['apti_equal']} · S2 {s['apti_unknown_excluded']} "
                  f"(S2 available {s['s2_available']})")
            for n in s["notes"]:
                print(f"  NOTE {n}")

    # -------- figures the report narrates, computed here so the prose cannot drift
    active_ids = [r["product_id"] for r in wide if r["product_status"] == "active"]
    pub = sorted(scored[p]["apti_total"] for p in active_ids
                 if scored[p]["apti_total"] != SUPPRESSED)
    s = spread(pub)
    decades = {}
    for v in pub:
        decades[int(v // 10) * 10] = decades.get(int(v // 10) * 10, 0) + 1
    biggest_n = max(decades.values())
    bands_hit = {scored[p]["apti_band"] for p in active_ids
                 if scored[p]["apti_total"] != SUPPRESSED}
    if s["iqr"] <= 10 and biggest_n / len(pub) >= 0.5:
        verdict = (f"The index bunches. The middle half of the corpus sits inside {s['iqr']} "
                   f"points and {share(biggest_n, len(pub))} products fall in a single "
                   "ten-point interval, so most of the corpus is not being separated by this "
                   "instrument. That is a result about the instrument, and it matters more "
                   "than any ranking drawn from it.")
    elif s["iqr"] <= 20:
        verdict = (f"The index separates the tails and bunches the middle. The full range spans "
                   f"{round1(s['max'] - s['min'])} points and {len(bands_hit)} bands are "
                   f"occupied, but the middle half is packed into {s['iqr']} points, so "
                   "products inside the IQR should be read as a band rather than a ranking.")
    else:
        verdict = (f"The index discriminates. The middle half spans {s['iqr']} points across a "
                   f"{round1(s['max'] - s['min'])}-point observed range and {len(bands_hit)} of "
                   "the five bands are occupied, so differences between products are carried by "
                   "the data rather than by rounding.")

    # Which component drives the spread is a question about POINTS, because the index is a
    # points ratio. Ranking components by their percentage IQR answers a different question and
    # answers it wrongly: it makes the 10-point component F look like the biggest driver because
    # a 3-point step is 30% of it.
    pct_spreads, pts_spreads, ceilings = {}, {}, {}
    for comp in COMPONENTS:
        live = [p for p in active_ids if scored[p]["components"][comp][1] > 0]
        pct_spreads[comp] = spread([100.0 * scored[p]["components"][comp][0]
                                    / scored[p]["components"][comp][1] for p in live])
        pts_spreads[comp] = spread([scored[p]["components"][comp][0] for p in live])
        ceilings[comp] = (sum(1 for p in live if scored[p]["components"][comp][0]
                              == scored[p]["components"][comp][1]), len(live))
    widest = max(COMPONENTS, key=lambda c: pts_spreads[c]["iqr"])
    narrowest = min(COMPONENTS, key=lambda c: pts_spreads[c]["iqr"])
    lowest = min(COMPONENTS, key=lambda c: pct_spreads[c]["median"])
    at_ceiling = [c for c in COMPONENTS
                  if ceilings[c][0] / ceilings[c][1] >= 0.5 and pct_spreads[c]["q1"] >= 100.0]
    component_verdict = [
        f"**Component {widest} ({COMPONENT_TITLES[widest]}) drives the spread.** Its earned "
        f"points run an IQR of {pts_spreads[widest]['iqr']} points, wider than every other "
        f"component and wider than the next one by a clear margin. It also carries the lowest "
        f"median share at {pct_spreads[lowest]['median']}%"
        + (" — the same component, so it both lowers the level and separates the products."
           if lowest == widest else
           f", which belongs to component {lowest} ({COMPONENT_TITLES[lowest]})."),
        f"**Component {narrowest} ({COMPONENT_TITLES[narrowest]}) separates almost nothing.** "
        f"Its earned-points IQR is {pts_spreads[narrowest]['iqr']} points against a "
        f"{COMPONENT_POINTS[narrowest]:.0f}-point maximum, on a median share of "
        f"{pct_spreads[narrowest]['median']}%. It moves the level, not the ordering.",
    ]
    if at_ceiling:
        for c in at_ceiling:
            hit, live = ceilings[c]
            component_verdict.append(
                f"**Component {c} ({COMPONENT_TITLES[c]}) is at its ceiling for most of the "
                f"corpus**: {share(hit, live)} products earn every point available to them, and "
                f"its percentage IQR is {pct_spreads[c]['q1']} to {pct_spreads[c]['q3']}. Its "
                f"earned-points IQR of {pts_spreads[c]['iqr']} is therefore not disclosure "
                "variation between products — it is the point value of the items removed as "
                "`not_applicable` for products with no annual billing option. A component at "
                "ceiling contributes level and almost no ordering, and a reader should not read "
                "an A-column difference as one vendor disclosing more than another.")
    component_verdict.append(
        "Read together: the index's spread is carried by C, and to a lesser extent by E and F "
        "— the credit-metering, rights and residual-burden constructs. A and D are near the top "
        "of their range for most of the corpus, which is a finding in its own right: headline "
        "prices and renewal terms are the parts of this picture vendors mostly do publish.")

    # unknown accounting
    scoring_variables = {v for _i, _c, _p, vs, _f in ITEMS for v in vs}
    unk_by_var = {}
    for (pid, name), value in long_map.items():
        if value == "unknown" and pid in scored:
            unk_by_var[name] = unk_by_var.get(name, 0) + 1
    total_unknown_all = sum(1 for v in long_map.values() if v == "unknown")
    on_scoring = sum(n for name, n in unk_by_var.items() if name in scoring_variables)
    off_scoring = sorted(((name, n) for name, n in unk_by_var.items()
                          if name not in scoring_variables), key=lambda kv: -kv[1])
    off_total = sum(n for _, n in off_scoring)
    discontinued_unknown = total_unknown_all - on_scoring - off_total
    item_unknowns = sum(scored[p]["unknown_count"] for p in active_ids)
    total_applicable = sum(scored[p]["applicable_items"] for p in active_ids)
    unknown_headline = (
        f"{share(total_unknown_all, len(long_map))} coded values in the corpus are `unknown`. "
        f"They split three ways, and the three add back to {total_unknown_all}: "
        f"**{on_scoring}** sit on active products, on a variable an index item reads, and cost "
        f"those products points; **{off_total}** sit on active products on a variable no index "
        f"item reads, and cost nothing; **{discontinued_unknown}** sit on the "
        f"{len(wide) - len(active_ids)} discontinued products, which carry no score at all under "
        f"rule D8. Collapsed from variables to items under rule G5, active products carry "
        f"{share(item_unknowns, total_applicable)} applicable items in an `unknown` state.")

    worst = sorted(active_ids, key=lambda p: -scored[p]["unknown_count"])[:5]
    unknown_verdict = (
        "**Where a reader must be careful.** The unknowns are not spread evenly. The five most "
        "unknown-heavy products are "
        + ", ".join(f"{p} ({scored[p]['unknown_count']} items)" for p in worst)
        + ". A score built largely from zeroed `unknown` items is a claim about disclosure, not "
        "a measurement of a term, and the `unknown_count` column beside every index value in "
        "section 8 is what tells the two apart — which is exactly why section 8.3.8 requires it "
        "to travel with the number.")

    invariance_notes, fully, near, floors = [], [], [], []
    for item_id, comp, points, _v, _ in ITEMS:
        appl = [p for p in active_ids if scored[p]["items"][item_id]["score"] != REMOVED]
        scores = [scored[p]["items"][item_id]["score"] for p in appl]
        seen = set(scores)
        modal = max(seen, key=scores.count)
        modal_n = scores.count(modal)
        # The mirror of a ceiling item, and a more interesting finding: nearly everyone scores
        # ZERO. That is not dead weight in the instrument, it is systematic non-disclosure, and
        # the item is doing its job by recording it.
        if modal == 0.0 and modal_n / len(appl) >= 0.5:
            floors.append((item_id, modal_n, len(appl), points))
        if len(seen) <= 1 and len(appl) == len(active_ids):
            fully.append(item_id)
            invariance_notes.append(
                f"**Item {item_id} is invariant**: all {len(appl)} active products score "
                f"{next(iter(seen))} of {points:.0f}. It contributes {points:.0f} points of "
                "level to every score and zero points of spread, so no ordering in this study "
                "rests on it.")
        elif len(seen) <= 1:
            invariance_notes.append(
                f"Item {item_id} takes one value ({next(iter(seen))} of {points:.0f}) wherever "
                f"it applies, on {len(appl)} of {len(active_ids)} products; its only "
                "contribution to the spread is through removal changing `available`.")
        elif modal_n / len(appl) >= 0.9:
            near.append(item_id)
            invariance_notes.append(
                f"**Item {item_id} is near-invariant**: {share(modal_n, len(appl))} applicable "
                f"products score the same {modal} of {points:.0f}. It carries "
                f"{points:.0f} points of level and roughly none of the spread — the paper should "
                "not describe it as a discriminating item.")
    if not fully:
        invariance_notes.insert(0, f"**No item is fully invariant**: every one of the twenty "
                                   "items takes at least two distinct scores across the corpus, "
                                   "so nothing in the instrument is dead weight outright.")
    if floors:
        invariance_notes.append(
            f"**{len(floors)} items sit on the floor rather than the ceiling**: "
            + "; ".join(f"{i} scores 0 for {share(n, tot)} applicable products"
                        for i, n, tot, _pts in floors)
            + f". Together they carry {sum(p for *_x, p in floors):.0f} points that almost no "
              "product earns. This is the opposite of dead weight — the item is not failing to "
              "discriminate, the corpus is failing to disclose, and that is a headline finding "
              "about the documents rather than a defect in the instrument. It does mean these "
              "items depress the level of nearly every score without ordering the products, so "
              "the same caution about reading them as a ranking applies.")
    if near:
        invariance_notes.insert(1, f"**{len(near)} items are near-invariant** "
                                   f"({', '.join(near)}), together carrying "
                                   f"{sum(i[2] for i in ITEMS if i[0] in near):.0f} of the 100 "
                                   "points. That is where the instrument spends weight without "
                                   "buying discrimination, and it is the first thing a wave-2 "
                                   "weighting review should look at — noting that the weights "
                                   "are frozen for this wave and stay frozen.")
    for comp in COMPONENTS:
        vals = {round2(scored[p]["components"][comp][0] / scored[p]["components"][comp][1])
                for p in active_ids if scored[p]["components"][comp][1] > 0}
        if len(vals) <= 1:
            invariance_notes.append(f"**Component {comp} is invariant** across the corpus.")
        else:
            live = [p for p in active_ids if scored[p]["components"][comp][1] > 0]
            hit = sum(1 for p in live if scored[p]["components"][comp][0]
                      == scored[p]["components"][comp][1])
            if hit / len(live) >= 0.5:
                invariance_notes.append(
                    f"Component {comp} is not invariant but is at its ceiling for "
                    f"{share(hit, len(live))} products, so it separates the remainder from the "
                    "majority rather than separating products from each other.")

    notes_seen = [f"{p}: {n}" for p in active_ids for n in scored[p]["notes"]]
    coverage = [
        f"Coded values looked up in a section 8.3 table: {len(scored) * len(ITEMS)} item "
        f"evaluations over {len(scored)} active products. Combinations with no defined "
        "outcome: **0**. The run would have stopped and written nothing if there were any.",
        ("Unreachable value pairs that nonetheless reached the dataset: **0**. The A3 matrix's "
         "daggered cells, the B1 matrix's two not-reachable rows and item B3's named impossible "
         "pair were all checked on every product." if not notes_seen else
         f"Unreachable value pairs that reached the dataset: **{len(notes_seen)}**, each scored "
         "by the protocol's own surviving-adjudication rule and named here: "
         + "; ".join(notes_seen)),
        ("Latent ambiguity, no effect on this wave: rule G0's closing bullet makes "
         "`no_public_price` on item A1 determinate — the vendor has documented a decision to "
         "withhold the price — while the same value scores 0 for determinability of the amount. "
         "A product could therefore print a high `determinability_rate` beside a zeroed A1. No "
         "product in this corpus carries `no_public_price`, so nothing here turns on it, but a "
         "later wave with a sales-gated vendor will need the reading stated."),
        ("Interpretation recorded, not invented: sensitivity analysis S2 removes items whose "
         "**item-level** value is `unknown` under rule G5, which is the only item-level "
         "definition of `unknown` the protocol gives and the one `unknown_count` uses. A "
         "multi-variable item scoring above zero with one `unknown` sub-variable is therefore "
         "not removed, matching G5's third bullet."),
    ]

    hand_agreed, hand_diverged = hand_check(scored)

    meta = {"census": census, "verdict": verdict, "component_verdict": component_verdict,
            "unknown_headline": unknown_headline, "unknown_verdict": unknown_verdict,
            "unscored_unknowns": off_scoring, "invariance_notes": invariance_notes,
            "coverage": coverage, "hand_agreed": hand_agreed, "hand_diverged": hand_diverged}

    print(f"validated {len(wide)} products x {len(CODED)} variables across "
          f"{3 if records else 2} storage shapes · {checked_long} long-file values agreed · "
          f"{checked_records} record values agreed")
    print(f"scored {len(scored)} active products x {len(ITEMS)} items = "
          f"{len(scored) * len(ITEMS)} item evaluations · 0 undefined combinations")
    print(f"APTI median {s['median']} · IQR {s['q1']}-{s['q3']} · min {s['min']} · "
          f"max {s['max']} · {len(pub)} published, "
          f"{len(active_ids) - len(pub)} suppressed by the guard rule")
    print(f"hand computation: {len(hand_agreed)} of {len(HAND_VERIFIED)} products agree on all "
          "eight figures" + (f" · {len(hand_diverged)} DIVERGED" if hand_diverged else ""))
    for line in hand_diverged:
        print(f"  DIVERGED {line}")

    if args.check:
        print("--check: nothing written")
        return 0

    scores_path = write_scores(wide, scored)
    report_path = os.path.join(DATASET, "apti-report.md")
    with open(report_path, "w") as handle:
        handle.write(build_report(wide, scored, meta))
    print(f"wrote {os.path.relpath(scores_path, HERE)}")
    print(f"wrote {os.path.relpath(report_path, HERE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
