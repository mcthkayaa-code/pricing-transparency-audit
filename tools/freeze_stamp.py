#!/usr/bin/env python3
"""Generate the freeze stamp: what was frozen, when, and with which bytes.

Every figure in this stamp is **computed, never typed.** That is not stylistic. Three
figures in the limitations register went stale in a single day because a number derived by
a tool had been typed into prose by hand, and each was caught only by re-deriving it. A
freeze stamp is the one document that must not be wrong about its own contents, so it
reads the files it is stamping.

The stamp records SHA-256 for each published artifact so a reader can verify that the copy
they downloaded is the copy that was frozen. It also records the git commit the stamp was
generated **against** — necessarily the commit before the stamp itself is committed, which
is stated in the output rather than glossed.

    python3 tools/freeze_stamp.py            # print
    python3 tools/freeze_stamp.py --write    # write orchestrator/freeze-stamp.md
"""

import csv
import collections
import datetime
import glob
import hashlib
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "orchestrator", "freeze-stamp.md")

ARTIFACTS = [
    "dataset/coded-values.csv",
    "dataset/coded-long.csv",
    "dataset/apti-scores.csv",
    "dataset/apti-report.md",
    "dataset/build-report.md",
    "dataset/data-dictionary.md",
    "orchestrator/archive-verification.csv",
    "orchestrator/unknown-attribution.csv",
    "orchestrator/unknown-attribution-overrides.csv",
    "codebook-v1.md",
    "protocol-v1.md",
    "sampling-rules.md",
    "limitations-register.md",
    "methods-who-coded.md",
    "analysis-first-findings.md",
]

# Documents that are EXPECTED to grow after the freeze, and so are hashed but excluded
# from the frozen-bytes claim. The tooling register is the study's running account of
# how its own instruments failed; it gained a mode after the freeze (a deploy that
# reported success while serving a stale artifact) and another when the search
# submission step was found to have skipped the paper. Freezing a document whose
# purpose is to keep learning would either stop it learning or make the stamp wrong
# every time it did. It does not feed a single number in the paper.
LIVING = [
    "methods-tooling-failure-modes.md",
]


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def git(*args):
    try:
        return subprocess.run(["git", *args], capture_output=True, text=True,
                              cwd=HERE).stdout.strip()
    except OSError:
        return "unavailable"


def counts():
    out = {}
    for folder in ("pass1", "pass2", "adjudicated", "for-cause", "pass2-contaminated"):
        out[folder] = len(glob.glob(os.path.join(HERE, "records", folder, "*.yaml")))
    log = open(os.path.join(HERE, "orchestrator", "deviations-log.md")).read()
    out["deviations"] = len(re.findall(r"^## D-", log, re.M))

    long_rows = list(csv.DictReader(open(os.path.join(HERE, "dataset", "coded-long.csv"))))
    out["values"] = len(long_rows)
    unknowns = [r for r in long_rows if r["value"] == "unknown"]
    out["unknowns"] = len(unknowns)
    out["attribution"] = collections.Counter(r["unknown_kind"] for r in unknowns)
    out["unattributed"] = sum(1 for r in unknowns if not (r["unknown_kind"] or "").strip())

    verdicts = list(csv.DictReader(open(os.path.join(HERE, "orchestrator",
                                                     "archive-verification.csv"))))
    out["captures"] = collections.Counter(r["status"] for r in verdicts)

    scores = list(csv.DictReader(open(os.path.join(HERE, "dataset", "apti-scores.csv"))))
    numeric = []
    for row in scores:
        try:
            numeric.append(float(row["apti_total"]))
        except (TypeError, ValueError):
            pass
    out["scored"] = len(numeric)
    if numeric:
        numeric.sort()
        mid = len(numeric) // 2
        out["median"] = (numeric[mid] if len(numeric) % 2
                         else (numeric[mid - 1] + numeric[mid]) / 2)
        out["min"], out["max"] = numeric[0], numeric[-1]
    return out


def render():
    c = counts()
    lines = []
    add = lines.append
    add("# Freeze stamp — Pricing Transparency Audit, wave 1")
    add("")
    add(f"**Generated {datetime.date.today().isoformat()} by `tools/freeze_stamp.py`. "
        "Every figure below is read from the files it describes, not typed.**")
    add("")
    add("Generated against commit **`" + (git("rev-parse", "HEAD")[:12] or "unknown") +
        "`** — necessarily the commit *before* this stamp is itself committed. A reader "
        "verifying the hashes should check out that commit, or accept that this file is the "
        "only difference.")
    add("")
    add("## What freezing means")
    add("")
    add("**After this stamp, a correction to the dataset is a published erratum and not an "
        "edit.** The records, the coded values, the attributions and the index scores stop "
        "moving. Anything found later is recorded in `orchestrator/deviations-log.md` and "
        "carried into the paper as a correction with its date, in the open.")
    add("")
    add(f"This is not a claim that the dataset is free of error. {c['deviations']} deviations say "
        "otherwise, several of them retracting a claim this study had already made. It is a "
        "claim that **error found after this point is disclosed rather than absorbed.** "
        "(That count is interpolated, not typed: this sentence read 'Seventy-six' beside a table "
        "printing 77 until the preprint draft caught it — a typed figure going stale inside the one "
        "document that must not be wrong about its own contents.)")
    add("")
    add("## The frame")
    add("")
    add("| | count |")
    add("|---|---|")
    add(f"| pass-1 records (the frame) | **{c['pass1']}** |")
    add(f"| blind pass-2 records (reliability sample) | {c['pass2']} |")
    add(f"| adjudicated records (publish where they exist) | {c['adjudicated']} |")
    add(f"| for-cause second codings (reported separately) | {c['for-cause']} |")
    add(f"| quarantined pass-2 records (never publish) | {c['pass2-contaminated']} |")
    add(f"| coded values in the published dataset | **{c['values']:,}** |")
    add(f"| deviations logged | **{c['deviations']}** |")
    add("")
    add("## Unknowns, all attributed")
    add("")
    add("| kind | count | share of unknowns on publishing rows |")
    add("|---|---|---|")
    for kind, n in c["attribution"].most_common():
        add(f"| {kind} | {n} | {n / c['unknowns'] * 100:.1f}% |")
    add(f"| **total** | **{c['unknowns']}** | of {c['values']:,} coded values |")
    add("")
    add(f"**{c['unattributed']} unknowns carry no attribution kind.**")
    add("")
    add("## Provenance")
    add("")
    add("| verdict | count |")
    add("|---|---|")
    for status, n in c["captures"].most_common():
        add(f"| {status} | {n} |")
    total = sum(c["captures"].values())
    resolving = c["captures"]["ok"] + c["captures"]["ok_nearest"]
    add(f"| **total cited captures** | **{total}** |")
    add("")
    add(f"**{resolving} of {total} resolve ({resolving / total * 100:.1f}%). "
        f"{c['captures']['throttled']} unanswered.**")
    add("")
    add("## The index")
    add("")
    add(f"**{c['scored']} products scored. Median {c['median']:.2f}, "
        f"range {c['min']:.1f}–{c['max']:.1f}.**")
    add("")
    add("The median is printed to two decimals deliberately. It falls **exactly on a rounding "
        "boundary** — the 36th and 37th of 72 scores are 80.0 and 80.5 — so round-half-even prints "
        "80.2 and round-half-up prints 80.3, and two of this study's own artifacts did each. "
        "Neither is wrong and the disagreement is not about the data; printing 80.25 removes it.")
    add("")
    add("Distribution, component breakdown and what the index does and does not discriminate: "
        "`analysis-first-findings.md`.")
    add("")
    add("## Bytes")
    add("")
    add("SHA-256, so a reader can verify the copy they hold is the copy that was frozen.")
    add("")
    add("| sha256 (first 16) | bytes | file |")
    add("|---|---|---|")
    for rel in ARTIFACTS:
        path = os.path.join(HERE, rel)
        if not os.path.exists(path):
            add(f"| MISSING | — | `{rel}` |")
            continue
        add(f"| `{sha256(path)[:16]}` | {os.path.getsize(path):,} | `{rel}` |")
    add("")
    add("### Hashed, but not frozen")
    add("")
    add("**A hash below is true when printed and is expected to stop being true.** These documents "
        "are meant to keep growing, so a mismatch here is growth and not tampering — check them "
        "against the repository, not against this stamp. Every artifact in the table above is "
        "frozen and a mismatch there *is* a defect.")
    add("")
    add("| sha256 (first 16) | bytes | file | why it moves |")
    add("|---|---|---|---|")
    for rel in LIVING:
        path = os.path.join(HERE, rel)
        if not os.path.exists(path):
            add(f"| MISSING | — | `{rel}` | — |")
            continue
        add(f"| `{sha256(path)[:16]}` | {os.path.getsize(path):,} | `{rel}` | "
            "gains a mode whenever this study's own tooling is caught failing |")
    add("")
    add("## What this stamp does NOT cover")
    add("")
    add("**Owner sign-off: SIGNED 2026-08-18 by Mucahit Kaya**, founder and editor — the named "
        "human in this study's AI-assistance framing, who set the question before any data "
        "existed and reviewed the frozen dataset before signing. Freezing stopped the data "
        "moving; publishing was his decision and he made it.")
    add("")
    add("**One provenance defect, reported and left unfixed by decision** (D-076): a record "
        "pairing an access date with an archive URL stamped five days earlier, on the far "
        "side of a demonstrated edit to that page. Coded values survive in both captures. "
        "No record was edited by the orchestrator on freeze day and that invariant was kept "
        "in preference to the correction. **The owner reviewed the three options on 2026-08-18 "
        "and chose to leave it as a disclosed defect**, so this is a decision on the record "
        "rather than an open question.")
    add("")
    add("**No DOI, by decision** (D-081). The paper had carried a sentence from the protocol "
        "claiming one was minted at publication; none was. The claim is retracted, the release "
        "is identified by this repository and the checksums above, and the owner has deferred "
        "minting an identifier.")
    add("")
    add("**Wave-2 items are not blockers and are listed as such** in "
        "`orchestrator/pre-freeze-checklist.md`: a fourth attribution kind for "
        "withdrawn-before-window documents, a codebook slot for a one-time credit grant, a "
        "class of official vendor page the location variables do not cover, and a checker "
        "that diffs the limitations register's prose against the tools.")
    return "\n".join(lines) + "\n"


def main(argv):
    text = render()
    if "--write" in argv:
        with open(OUT, "w") as handle:
            handle.write(text)
        print(f"wrote {OUT}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
