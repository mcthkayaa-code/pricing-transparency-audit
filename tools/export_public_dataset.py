#!/usr/bin/env python3
"""Assemble the public open-dataset release into `../pricing-transparency-public/`.

The study lives inside a PRIVATE site repository. Publishing the dataset must never mean
making that repository public: it holds the site, its commercial arrangements, and internal
tooling that is not part of this study. So this copies only what belongs in a public dataset
release into a separate tree, ready to become its own repository.

**The manifest is explicit and the exclusions are argued.** A release built by "copy the
directory and delete a few things" ships whatever nobody thought about; this one names every
file class it takes and refuses to run if it finds something it has no rule for.

    python3 tools/export_public_dataset.py            # dry run, prints the manifest
    python3 tools/export_public_dataset.py --write    # actually copy
"""

import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.abspath(os.path.join(HERE, "..", "pricing-transparency-public"))

def _failure_mode_count():
    """Read the count instead of carrying it.

    This one string went stale twice: it said 33 with 34 in the file, then 34 with 35 — inside
    the very tool that publishes the register whose entire subject is figures that quietly stop
    being true. Nothing would have caught it; the manifest prints and nobody re-counts.
    """
    path = os.path.join(HERE, "methods-tooling-failure-modes.md")
    with open(path, encoding="utf-8") as handle:
        return len(re.findall(r"^\*\*\d+\.", handle.read(), re.M))


# --- what ships, and why ------------------------------------------------------------------

INCLUDE_FILES = {
    # the instrument, pre-registered before collection
    "codebook-v1.md": "the measurement instrument",
    "protocol-v1.md": "the procedure, including the index definition and scoring rules",
    "sampling-rules.md": "frame definition, entry-tier selection, the double-coded subsample",
    # what a reader must read before using a number
    "limitations-register.md": "every limitation, with the figure and the deviation that established it",
    "methods-who-coded.md": "who coded and what the reliability figure does and does not establish",
    "methods-tooling-failure-modes.md":
        f"{_failure_mode_count()} failure modes, reusable by anyone coding web documents",
    # the binding corrections each role worked under
    "deviations-for-coders.md": "corrections a coder was bound by, with no product named",
    "deviations-for-adjudicators.md": "corrections an adjudicator was bound by, with no product named",
    "README.md": "the entry point: what this is, what a reader must read before using a number, the finding, the file map, and how to regenerate everything",
    "LICENSE.md": "CC BY 4.0 for what the study produced, and an explicit statement that the saved vendor captures are the vendors' copyright and are evidence rather than redistributed content",
    "CITATION.cff": "so the release is citable, and so GitHub renders a cite button",
    "paper-draft.md": "the preprint itself — a DRAFT, unsigned and not yet approved for publication. It ships with the dataset because a reader checking a figure needs the document that makes the claim, and because publishing the data while withholding the argument would be the wrong way round. Its status is stated in its own front matter",
    "analysis-first-findings.md": "the first reading of the index — the distribution, what it does and does not discriminate, the finding, and the three places the first analysis pass was wrong",
    "record-template.yaml": "the record shape, so a reader can see what a coder filled in",
    "frame-for-pass2.csv": "the coder-visible frame slice used to assign the blind second pass — part of the method, and a reader checking the reliability sample needs it",
}

INCLUDE_DIRS = {
    "dataset": "the CSVs, the generated data dictionary, and the build report",
    "records": "every record and every saved source capture — for 159 values the local "
               "capture is the only surviving evidence. Includes `for-cause/`: three products "
               "given a blind second coding because something went wrong on them rather than "
               "because they were sampled, whose agreement is reported SEPARATELY from the "
               "pre-registered reliability figure so the planned statistic stays uncontaminated. "
               "They ship because a reader checking that separation needs to see them",
    "tools": "every script, so a reader can regenerate the dataset and re-run every check",
    "orchestrator": "the deviations log, the adjudication queue and its resolutions, the "
                    "reliability computation, the provenance verification, the attribution "
                    "ledger, and the audits",
}

# --- what does NOT ship, and why ----------------------------------------------------------

EXCLUDE = {
    "paper-draft-tr.md":
        "A Turkish translation of the preprint, produced so the responsible human could read the "
        "paper in his own language before signing it. It is a REVIEW AID and not a publication "
        "artifact: the English text is the one that publishes, it is the one every figure was "
        "verified against, and shipping an unreviewed translation beside it would invite a reader "
        "to quote the wrong one. Excluded for that reason and not because it is private — if a "
        "Turkish edition is ever wanted, it gets its own review pass and its own place in this "
        "manifest.",
    "study-dossier.md":
        "An INTERNAL brief. It tells agents what the study is for, cross-references a separate "
        "trust dossier outside this study, and frames the publication's commercial position. "
        "Everything in it that a reader needs — the research question, the design, the "
        "conflicts statement — belongs in the paper's own words rather than as a leaked memo. "
        "Excluding it is not concealment: the conflicts disclosure it demands is published, in "
        "the limitations register and the paper.",
    "orchestrator/interim-signals.md":
        "Working notes that accumulated cross-product patterns mid-study, and which coders and "
        "adjudicators were deliberately barred from reading so a pattern could not steer a "
        "close call. Several of its observations were later corrected or withdrawn. Publishing "
        "half-formed conclusions beside the corrected ones invites a reader to cite the wrong "
        "one. The findings that survived are in the deviations log and the register.",
}

# Directory names that never ship from anywhere in the tree.
EXCLUDE_DIR_NAMES = {"pass2-contaminated"}
EXCLUDE_DIR_REASON = {
    "pass2-contaminated": "Quarantined records: a coder's required reading had disclosed "
                          "pass-1 findings, so these were withdrawn and the products re-coded "
                          "blind. They are kept in the private tree as evidence the quarantine "
                          "happened, and excluded here because publishing a withdrawn record "
                          "beside its replacement invites the wrong one to be used.",
}


def walk_study():
    for root, dirs, files in os.walk(HERE):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIR_NAMES and not d.startswith(".")]
        for name in files:
            if name.startswith("."):
                continue
            yield os.path.relpath(os.path.join(root, name), HERE)


def classify(rel):
    if rel in EXCLUDE:
        return "exclude", EXCLUDE[rel]
    top = rel.split(os.sep)[0]
    # Thirteen products keep their saved captures in a `<slug>-sources/` directory at the
    # STUDY ROOT rather than under records/. They are evidence and they ship. This tool is
    # what found that split, by refusing to copy files it had no rule for (D-063).
    if top.endswith("-sources") and os.sep in rel:
        return "include", "saved source captures (study-root layout)"
    if rel in INCLUDE_FILES:
        return "include", INCLUDE_FILES[rel]
    if top in INCLUDE_DIRS and os.sep in rel:
        return "include", f"under {top}/"
    return "UNRULED", "no rule covers this path"


def main(argv):
    write = "--write" in argv
    include, exclude, unruled = [], [], []
    for rel in sorted(walk_study()):
        verdict, why = classify(rel)
        (include if verdict == "include" else exclude if verdict == "exclude" else unruled
         ).append((rel, why))

    print(f"study root: {HERE}")
    print(f"destination: {DEST}\n")
    print(f"INCLUDE  {len(include)} files")
    for name, why in INCLUDE_FILES.items():
        print(f"    {name:<40} {why}")
    for name, why in INCLUDE_DIRS.items():
        n = sum(1 for r, _ in include if r.split(os.sep)[0] == name)
        print(f"    {name + '/':<40} {n} files — {why}")
    print(f"\nEXCLUDE  {len(exclude)} files")
    for rel, why in exclude:
        print(f"    {rel}\n        {why[:150]}")
    for d, why in EXCLUDE_DIR_REASON.items():
        print(f"    {d}/ (whole directory)\n        {why[:150]}")

    if unruled:
        print(f"\n*** {len(unruled)} FILES WITH NO RULE — refusing to write ***")
        for rel, _ in unruled[:30]:
            print(f"    {rel}")
        print("\nAdd each to INCLUDE_FILES, INCLUDE_DIRS or EXCLUDE with a reason. A release that")
        print("silently ships whatever nobody classified is how private material leaks.")
        return 1

    total = sum(os.path.getsize(os.path.join(HERE, r)) for r, _ in include)
    print(f"\ntotal to ship: {len(include)} files, {total / 1_048_576:.0f} MB")

    if not write:
        print("\nDRY RUN. Re-run with --write to copy.")
        return 0

    for rel, _ in include:
        src, dst = os.path.join(HERE, rel), os.path.join(DEST, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
    print(f"\ncopied {len(include)} files to {DEST}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
