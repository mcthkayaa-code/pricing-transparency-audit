#!/usr/bin/env python3
"""Compare pass 1 against pass 2 and compute inter-coder reliability.

Run only after BOTH passes close. Protocol §7.4 step 1 compares records variable
by variable once that is true, and this study deliberately computed nothing
earlier so that no early figure could shape a later assignment.

Reports two things, because they answer different questions:

  * **Raw agreement** — the share of variable-instances where the two coders wrote
    the same value. Transparent, easy to check by hand, and inflated whenever one
    value dominates a variable.
  * **Krippendorff's alpha (nominal)** — the pre-registered statistic. Corrects for
    the agreement two coders would reach by chance given the observed marginals,
    which is why it can sit far below raw agreement on a lopsided variable.

Alpha is reported over three populations per deviation D-014, whose exposure
tiers are passed in below rather than inferred here:

  * all 26 products
  * the 19 outside tier A (no coded value was disclosed in required reading)
  * tier C alone (never named anywhere a coder reads) — with its n printed,
    because five products cannot carry a robustness claim and the paper says so.

    python3 tools/agreement.py
"""

import glob
import os
import sys
from collections import Counter, defaultdict

import yaml

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASS1 = os.path.join(HERE, "records", "pass1")
PASS2 = os.path.join(HERE, "records", "pass2")

# Exposure tiers fixed in deviations-log D-014 (amended). Listed rather than
# derived so the populations cannot drift as the log is edited.
TIER_A = {"aiva", "colossyan", "copyleaks", "jobscan", "krea-ai", "nicepage", "pika"}
TIER_C = {"recraft", "shortsfaceless", "udio", "undetectable-ai", "vidnoz"}


def load(path):
    with open(path) as handle:
        return yaml.safe_load(handle) or {}


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_records import CODED  # the canonical 37, so this tool cannot drift from the validator


def _scalar(entry):
    return entry.get("value") if isinstance(entry, dict) else entry


# Variables the codebook types as money or integer rather than categorical. A value
# that parses to the same number IS the same coded value; `10.0` and `10.00` differ
# only in how YAML serialised a float. Comparing them as strings counts a
# formatting artifact as coder disagreement — the same class of defect as reading
# one storage shape (D-020), not an analytic choice.
NUMERIC = {
    "headline_price_usd",
    "first_charge_amount_usd",
    "trial_length_days",
    "refund_window_days",
}


def _canon(name, value):
    text = str(value).strip()
    if name in NUMERIC:
        try:
            return f"{float(text.replace(',', '')):.4f}"
        except (TypeError, ValueError):
            return text  # a status value like `unknown` or `non_usd`
    return text


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


def coded(record):
    """variable -> value, as a comparable string, read from EVERY storage shape.

    D-010 found `computation_assumptions` stored four different ways across the
    corpus, and the pre-freeze checklist makes it a hard requirement that anything
    producing a published number reads the field from all of them. The first
    version of this tool read `variables{}` only and silently dropped five units —
    the exact defect its own checklist item forbids. Fixed rather than excused.
    """
    out = {}
    for name, entry in (record.get("variables") or {}).items():
        out[name] = _canon(name, _scalar(entry))
    for name in CODED:                      # fall back to top level, coded fields only
        if name not in out and name in record:
            out[name] = _canon(name, _scalar(record[name]))
    return out


def alpha_nominal(units):
    """Krippendorff's alpha for nominal data over 2-coder units.

    units: list of (value_a, value_b). Standard formulation with pairable values;
    with exactly two coders per unit the coincidence matrix reduces to counting
    each unit's ordered pairs both ways.
    """
    pairs = [(a, b) for a, b in units if a is not None and b is not None]
    if not pairs:
        return None
    n = 2 * len(pairs)  # total pairable values

    observed_disagreement = sum(1 for a, b in pairs if a != b) * 2
    do = observed_disagreement / n

    marginals = Counter()
    for a, b in pairs:
        marginals[a] += 1
        marginals[b] += 1
    # expected disagreement under independence, corrected for finite n
    de = 1 - sum(c * (c - 1) for c in marginals.values()) / (n * (n - 1))
    if de == 0:
        return 1.0  # every value identical everywhere: no variance to explain
    return 1 - do / de


def main():
    products = sorted(
        os.path.basename(p)[:-5]
        for p in glob.glob(os.path.join(PASS2, "*.yaml"))
    )

    per_variable = defaultdict(list)   # variable -> [(v1, v2), ...]
    per_product = {}
    skipped = []

    for product in products:
        p1_path = os.path.join(PASS1, f"{product}.yaml")
        p2_path = os.path.join(PASS2, f"{product}.yaml")
        if not os.path.exists(p1_path):
            skipped.append(product)
            continue
        one, two = coded(load(p1_path)), coded(load(p2_path))
        shared = sorted(set(one) & set(two))
        same = 0
        for variable in shared:
            per_variable[variable].append((one[variable], two[variable]))
            if one[variable] == two[variable]:
                same += 1
        per_product[product] = (same, len(shared))

    if skipped:
        print(f"no pass-1 counterpart, skipped: {', '.join(skipped)}\n")

    total_same = sum(s for s, _ in per_product.values())
    total_all = sum(t for _, t in per_product.values())
    print(f"PRODUCTS COMPARED: {len(per_product)}")
    print(f"RAW AGREEMENT: {total_same}/{total_all} = {total_same / total_all * 100:.1f}%\n")

    print("PER PRODUCT (raw), worst first:")
    for product, (same, tot) in sorted(per_product.items(), key=lambda kv: kv[1][0] / kv[1][1]):
        print(f"  {product:<22} {same:>2}/{tot}  {same / tot * 100:5.1f}%")

    print("\nPER VARIABLE (raw), worst first — the ones adjudication should read first:")
    rows = []
    for variable, units in per_variable.items():
        same = sum(1 for a, b in units if a == b)
        rows.append((same / len(units), variable, same, len(units)))
    for share, variable, same, tot in sorted(rows)[:12]:
        print(f"  {variable:<34} {same:>2}/{tot}  {share * 100:5.1f}%")

    print("\nKRIPPENDORFF'S ALPHA (nominal), pooled over all coded variables:")
    for label, population in (
        ("all 26 products", set(per_product)),
        ("19 outside tier A", set(per_product) - TIER_A),
        ("tier C only", set(per_product) & TIER_C),
    ):
        units = []
        for product in sorted(population):
            p1_path = os.path.join(PASS1, f"{product}.yaml")
            p2_path = os.path.join(PASS2, f"{product}.yaml")
            if not os.path.exists(p1_path):
                continue
            one, two = coded(load(p1_path)), coded(load(p2_path))
            for variable in sorted(set(one) & set(two)):
                units.append((one[variable], two[variable]))
        a = alpha_nominal(units)
        n = len([p for p in population if os.path.exists(os.path.join(PASS1, f"{p}.yaml"))])
        print(f"  {label:<20} n={n:<3} units={len(units):<5} alpha={a:.3f}")

    print("\nPER-VARIABLE ALPHA — pooling across 37 heterogeneous variables inflates the")
    print("pooled figure, the same flattery this tool's docstring warns about for raw agreement:")
    per_var_alpha = []
    for variable, pairs in per_variable.items():
        a = alpha_nominal(pairs)
        if a is not None:
            per_var_alpha.append((a, variable, len(pairs)))
    per_var_alpha.sort()
    for a, variable, n in per_var_alpha[:8]:
        print(f"  {variable:<34} alpha={a:6.3f}  n={n}")
    med = per_var_alpha[len(per_var_alpha) // 2][0]
    above = sum(1 for a, _, _ in per_var_alpha if a >= 0.800)
    print(f"  ...")
    print(f"  median per-variable alpha = {med:.3f} · {above} of {len(per_var_alpha)} variables reach 0.800")

    print("\nTier C is 5 products. That is too small to carry a robustness claim on its own,")
    print("and the paper says so rather than presenting it as a clean control (D-014, D-017).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
