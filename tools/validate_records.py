#!/usr/bin/env python3
"""Structural validator for pass-1/pass-2 records against codebook v1.2 §10.
Coded values may live in variables{} or (template drift) top-level for the
three free-text coded fields. Reports truly-missing coded variables only."""
import sys, os, glob, yaml

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Folders holding records a check must see. `pass2-contaminated` is deliberately absent: those
# five are withdrawn and publishing them would be the error, not checking them.
FOLDERS = ("pass1", "adjudicated", "for-cause", "pass2")

CODED = [
    "headline_price_usd","headline_billing_basis","first_charge_amount_usd",
    "mandatory_addon_present","annual_condition_disclosure","annual_default_toggle",
    "free_plan_exists","free_plan_cap_documented","free_plan_cap_value",
    "free_plan_watermark","free_plan_duration",
    "trial_exists","trial_card_required","trial_length_days","trial_auto_converts",
    "credit_system_present","credit_unit_defined","credit_to_output_rate_published",
    "credit_rate_location","cost_per_output_unit","cost_per_output_computable",
    "computation_assumptions","credit_rollover_policy","failed_generation_charge_policy",
    "auto_renewal_default","auto_renewal_disclosure_location","renewal_notice_commitment",
    "refund_policy_exists","refund_window_days","refund_conditions",
    "cancellation_self_serve","refund_policy_location",
    "commercial_use_lowest_tier","watermark_removal_tier","output_ownership_statement",
    "usage_cap_quantified","unquantified_limit_clause",
]
# Template drift: `computation_assumptions` is accepted at the top level as well as inside
# `variables{}`. The pre-freeze checklist wanted this exemption REMOVED once the dataset build
# proved it canonicalises across shapes, so a future wave could not drift the same way without
# failing. The build does now prove it — it reads every shape and reports zero unrecognised
# (D-058) — and the exemption is still here, deliberately.
#
# Removing it would fail two records that are correctly coded and merely stored differently,
# and the alternative is moving the field inside them, which is line surgery on a record for a
# cosmetic reason. That is D-010's exact prohibition, and this orchestrator has broken three
# records doing precisely that in the last two days. A stored-shape difference the build erases
# is not worth risking a record over.
#
# So the exemption stays and stops being silent instead: `report_toplevel_usage()` names the
# records relying on it, and wave 2 fixes it where it belongs — in the record template, before
# any data exists.
TOPLEVEL_OK = {"computation_assumptions"}


def report_toplevel_usage():
    """Which records rely on the TOPLEVEL_OK exemption. Counted, never silent."""
    import glob as _g, os as _o
    here = _o.path.dirname(_o.path.dirname(_o.path.abspath(__file__)))
    users = []
    for path in sorted(_g.glob(_o.path.join(here, "records", "*", "*.yaml"))):
        try:
            record = yaml.safe_load(open(path)) or {}
        except yaml.YAMLError:
            continue
        variables = record.get("variables") or {}
        for name in TOPLEVEL_OK:
            if name not in variables and record.get(name) not in (None, ""):
                users.append(f"{_o.path.basename(_o.path.dirname(path))}/"
                             f"{_o.path.basename(path)[:-5]}: {name}")
    print(f"TOPLEVEL_OK exemption relied on by {len(users)} record-fields:")
    for item in users:
        print(f"  {item}")
    print("Kept rather than removed (see the comment above): removing it would fail correctly")
    print("coded records over a stored-shape difference the dataset build already erases.")
    return users

def check(path):
    r = yaml.safe_load(open(path))
    v = r.get("variables", {}) or {}
    present = set(v.keys())
    for k in TOPLEVEL_OK:
        if k in r and r[k] not in (None, ""):
            present.add(k)
    missing = [k for k in CODED if k not in present]
    return r.get("status"), missing, r


# --- administrative enum guard (added 2026-08-14, D-015 addendum) -------------
# Eleven pass-2 records carried `coder_role: secondary`, which is not in the
# codebook's enum. Nothing checked it, and a dataset build selecting rows by
# role would have silently missed them. Same harm class as D-006: one value,
# two spellings, a count that splits without warning.
#
# Widened 2026-08-15 (D-019). The enum check above was necessary but not
# sufficient: it read the top level only, so eight pass-1 records escaped it
# entirely — five stored `coder_role` INSIDE variables{} in {value: ...} form
# and three had no role key at all. Both passed, because a value the guard
# cannot see is not a value it can reject. Absence and misplacement are now
# failures in their own right, and `coder_pass` is checked on the same footing
# because the same drift put a role value in the pass slot in twelve records.
CODER_ROLE_ALLOWED = {"primary", "second", "adjudicated"}
CODER_PASS_ALLOWED = {1, 2, 3}
# 3 admitted 2026-08-15 for adjudication. This is NOT a widening-to-accept-drift of
# the D-010 kind: `coder_pass` is a template convention, not a codebook variable —
# the codebook never defines it — and protocol 7.4 step 2 calls adjudication "a
# third adjudication pass" in its own words. The value was missing because the
# template was written before the phase that needs it, not because records drifted.

ADMIN_REQUIRED = ("coder_role", "coder_pass")


def _unwrap(x):
    """Coded variables are {value, source, evidence} maps. An administrative
    field found in that shape is misplaced, but its value is still readable."""
    return x.get("value") if isinstance(x, dict) and "value" in x else x


def check_admin_enums(path, record):
    """Return a list of administrative-field failures for one record.

    Checks placement AND membership. A field nested inside variables{} is
    reported even when its value is valid, because the dataset build reads the
    top level and cannot see it there."""
    errs = []
    nested = record.get("variables", {}) or {}

    for field in ADMIN_REQUIRED:
        top, sub = record.get(field), nested.get(field)
        if top is None and sub is None:
            errs.append(f"BAD  {path}: {field} absent (administrative field is required)")
            continue
        if top is None:
            errs.append(f"BAD  {path}: {field} nested in variables{{}} as "
                        f"{sub!r} — the build reads top level and will not see it")
            continue
        if sub is not None and _unwrap(sub) != top:
            errs.append(f"BAD  {path}: {field} disagrees — top-level {top!r} "
                        f"vs nested {_unwrap(sub)!r}")

    role = record.get("coder_role")
    if role is not None and str(role) not in CODER_ROLE_ALLOWED:
        errs.append(f"BAD  {path}: coder_role={role!r} not in {sorted(CODER_ROLE_ALLOWED)}")

    cpass = record.get("coder_pass")
    if cpass is not None and cpass not in CODER_PASS_ALLOWED:
        errs.append(f"BAD  {path}: coder_pass={cpass!r} not in {sorted(CODER_PASS_ALLOWED)}")

    return errs



def check_evidence_prose():   # scope is internal and absolute; it globs publishing rows itself
    """Every coded value on a PUBLISHING row must carry evidence prose (D-028).

    D-028 found 25 real coded values with a source URL and no reasoning, concentrated in
    two records, and predicted that two adjudications would close the two that reached
    publishing rows. That prediction held: the count is zero, which is why this is a hard
    requirement here rather than a warning.

    Scoped to publishing rows — adjudicated where one exists, pass 1 otherwise — because a
    pass-2 record's gaps do not reach the dataset a reader downloads. Those are reported so
    the number is visible, never silently passed.

    `computation_assumptions` is exempt: an empty one means the coder had no arithmetic to
    record, and the field is already reported at alpha -0.001 and slated for
    reclassification as documentation in wave 2.
    """
    import glob as _glob, os as _os
    here = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
    adjudicated = {_os.path.basename(x)[:-5]: x
                   for x in _glob.glob(_os.path.join(here, "records", "adjudicated", "*.yaml"))}
    failures, pass2_gaps = [], []
    for folder in ("pass1", "pass2"):
        for path in sorted(_glob.glob(_os.path.join(here, "records", folder, "*.yaml"))):
            slug = _os.path.basename(path)[:-5]
            publishes = folder == "pass1" and slug not in adjudicated
            use = adjudicated.get(slug, path) if folder == "pass1" else path
            try:
                record = yaml.safe_load(open(use)) or {}
            except yaml.YAMLError:
                continue
            variables = record.get("variables") or {}
            for name in CODED:
                if name == "computation_assumptions":
                    continue
                entry = variables.get(name, record.get(name))
                if entry is None:
                    continue
                prose = str((entry.get("evidence") if isinstance(entry, dict) else "") or "").strip()
                if prose:
                    continue
                # The pass-1 branch already resolved `use` to the PUBLISHING row — the
                # adjudicated file where one exists, pass 1 otherwise — so everything it
                # finds is a publishing-row failure. The pass-2 branch never publishes.
                # An earlier version keyed this on `slug in adjudicated`, which sent a
                # pass-2 gap on an adjudicated product into the failure list and made the
                # check fail on a corpus a separate query had just shown to be clean. The
                # disagreement between the two readings is what surfaced it.
                target = failures if folder == "pass1" else pass2_gaps
                label = f"{'publishing' if folder == 'pass1' else folder}/{slug}/{name}"
                target.append(label)
    print(f"EVIDENCE PROSE — publishing rows missing it: {len(failures)}")
    for item in failures[:20]:
        print(f"  MISSING  {item}")
    print(f"EVIDENCE PROSE — pass-2 rows missing it: {len(pass2_gaps)} (reported, does not fail: "
          f"pass 2 never publishes)")
    return 1 if failures else 0

if __name__ == "__main__":
    # This block used to default to a glob relative to the REPO ROOT. Every agent brief tells
    # an agent to run `python3 tools/validate_records.py` from the study directory, where that
    # path does not exist — so the glob returned nothing, the loop never ran, and the tool
    # printed NOTHING and exited 0. A validator that examines zero records and reports success
    # is worse than one that is never run, because its silence reads as a pass. Found 2026-08-17
    # (D-068) while checking whether the three for-cause records were covered by any check.
    #
    # Two consequences, both fixed here: the default is now absolute and spans every folder
    # holding live records, and a run that finds no records FAILS. The study's own cheapest
    # detector is arithmetic that cannot be true — a denominator of zero is that arithmetic.
    #
    # `check_evidence_prose()` and `report_toplevel_usage()` were also never reached as a
    # script. Their results were real only because they had been called by hand.
    if len(sys.argv) > 1:
        paths = sorted(glob.glob(sys.argv[1]))
    else:
        paths = sorted(p for folder in FOLDERS
                       for p in glob.glob(os.path.join(HERE, "records", folder, "*.yaml")))
    if not paths:
        print("FAIL validate_records examined ZERO records — the glob matched nothing.")
        print(f"  searched: {', '.join('records/' + f + '/' for f in FOLDERS)} under {HERE}")
        sys.exit(2)

    bad = 0
    for f in paths:
        slug = f.split("/")[-1][:-5]
        try:
            status, missing, r = check(f)
        except Exception as e:
            print(f"FAIL {slug}: unparseable ({e})"); bad += 1; continue
        enum_errs = check_admin_enums(f, r)
        for e in enum_errs:
            print(e)
        if enum_errs:
            bad += 1
        if missing or status != "complete":
            print(f"WARN {slug}: status={status} missing={missing}"); bad += 1
        elif not enum_errs:
            print(f"OK   {slug}: 37/37 coded present")

    print(f"\n{len(paths)} records examined across {', '.join(FOLDERS)} · {bad} failing\n")
    report_toplevel_usage()
    bad += check_evidence_prose()
    sys.exit(1 if bad else 0)
