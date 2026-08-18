#!/usr/bin/env python3
"""Diff the figures printed in prose against the figures the data actually yields.

This study's most frequent defect is not a wrong analysis. It is **a number that was correct when
it was typed and stopped being correct afterwards.** The deviation count alone has been wrong, at
different moments, inside the freeze stamp, the limitations register's heading, four places in the
paper, the press kit, and the export manifest's own description string — and every single instance
was caught by re-deriving it, never by reading it. Three were caught only because a grep happened
to be phrased widely enough, which is not a control.

So this checks prose against the tools. For each concept it knows, it computes the true value from
the dataset and then finds every place the prose states that value, in every phrasing the study
actually uses, and compares.

**A concept whose patterns match nothing anywhere is a FAILURE, not a pass.** That rule exists
because `validate_records.py` once exited 0 having examined zero records: a checker that silently
finds nothing to check is worse than no checker, since it reports success.

    python3 tools/check_published_figures.py
    python3 tools/check_published_figures.py --extra /path/to/press-kit.html
"""

import collections
import csv
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WORDS = {
    70: "Seventy", 71: "Seventy-one", 72: "Seventy-two", 73: "Seventy-three",
    74: "Seventy-four", 75: "Seventy-five", 76: "Seventy-six", 77: "Seventy-seven",
    78: "Seventy-eight", 79: "Seventy-nine", 80: "Eighty", 81: "Eighty-one",
    82: "Eighty-two", 83: "Eighty-three", 84: "Eighty-four", 85: "Eighty-five",
}

# Files whose prose makes numeric claims a reader can check. Paths are relative to the study root.
SURFACES = [
    "paper-draft.md",
    "orchestrator/freeze-stamp.md",
    "limitations-register.md",
    "analysis-first-findings.md",
    "../../../../site/content/research/pricing-transparency-audit.md",
    # The site states figures in COMPONENT SOURCE too, not only in the markdown. That is how five
    # of these went stale unnoticed: the sweep read the paper, the paper was clean, and a hardcoded
    # count in a React component kept serving the old number to every reader of the live page.
    "../../../../site/components/research/DataAvailability.tsx",
]


def truth():
    """Every figure computed from the files, never carried."""
    out = {}
    for folder in ("pass1", "pass2", "adjudicated", "for-cause"):
        out[folder] = len(glob.glob(os.path.join(HERE, "records", folder, "*.yaml")))

    log = open(os.path.join(HERE, "orchestrator", "deviations-log.md"), encoding="utf-8").read()
    ids = [int(x) for x in re.findall(r"^## D-(\d+)", log, re.M)]
    out["deviations"] = len(ids)
    out["max_deviation_id"] = max(ids)

    rows = list(csv.DictReader(open(os.path.join(HERE, "dataset", "coded-long.csv"))))
    out["coded_rows"] = len(rows)

    v = collections.Counter(r["status"] for r in csv.DictReader(
        open(os.path.join(HERE, "orchestrator", "archive-verification.csv"))))
    out["citations"] = sum(v.values())
    out["citations_resolving"] = v["ok"] + v["ok_nearest"]
    return out


def patterns(t):
    """(concept, expected, [regexes]) — each regex must capture the figure in group 1."""
    dev, mx = t["deviations"], t["max_deviation_id"]
    return [
        ("deviation count", dev, [
            r"(\d+) dated deviations",
            r"(\d+) deviations say otherwise",
            r"\|\s*Deviations logged\s*\|\s*\*\*(\d+)\*\*",
            r"deviations logged \| \*\*(\d+)\*\*",
            r"^### 3\.9 ([A-Z][a-z]+(?:-[a-z]+)?) deviations",
            r"^\*\*10\. ([A-Z][a-z]+(?:-[a-z]+)?) deviations",
            r"This is not a claim that the dataset is free of error\. (\d+) deviations",
        ]),
        ("highest deviation id", mx, [r"D-001 to D-0*(\d+)"]),
        ("cited captures", t["citations"], [r"\d+ of (\d+) citations resolve",
                                            r"(\d+) archive citations",
                                            r"\*\*total cited captures\*\* \| \*\*(\d+)\*\*"]),
        ("resolving captures", t["citations_resolving"], [r"(\d+) of \d+ citations resolve",
                                                          r"of which (\d+) resolve"]),
        # Phrasings that live only in the press kit. They are checked when it is passed with
        # --extra and reported as skipped when it is not — never silently dropped.
        ("blind pass-2 records", t["pass2"], [r"(\d+) blind second codings"], False),
        ("adjudicated records", t["adjudicated"], [r"(\d+) third readings"], False),
    ]


def as_int(raw):
    if raw.isdigit():
        return int(raw)
    for value, word in WORDS.items():
        if word.lower() == raw.lower():
            return value
    return None


def main(argv):
    t = truth()
    surfaces = list(SURFACES) + [a for a in argv if not a.startswith("--")]

    texts = {}
    for rel in surfaces:
        path = rel if os.path.isabs(rel) else os.path.join(HERE, rel)
        if os.path.exists(path):
            texts[os.path.normpath(rel)] = open(path, encoding="utf-8", errors="replace").read()
        else:
            print(f"note: surface not present, skipped — {rel}")
    if not texts:
        print("FAIL check_published_figures read ZERO surfaces.")
        return 2

    bad, checked, skipped = [], 0, []
    for entry in patterns(t):
        concept, expected, regexes = entry[0], entry[1], entry[2]
        required = entry[3] if len(entry) > 3 else True
        hits = 0
        for name, text in texts.items():
            for rx in regexes:
                for m in re.finditer(rx, text, re.M):
                    hits += 1
                    checked += 1
                    got = as_int(m.group(1))
                    if got != expected:
                        line = text[:m.start()].count("\n") + 1
                        bad.append(f"  {name}:{line}  {concept}: prose says "
                                   f"{m.group(1)!r}, data says {expected}")
        if hits == 0:
            if required:
                bad.append(f"  (nowhere)  {concept}: matched NOTHING — the phrasing changed and "
                           f"this check went blind. Expected {expected}.")
            else:
                skipped.append(f"{concept} (expected {expected})")

    if bad:
        print(f"FAIL check_published_figures {len(bad)} problem(s):")
        print("\n".join(bad))
        return 1
    if skipped:
        print("skipped, no surface here states them: " + "; ".join(skipped))
    print(f"OK check_published_figures {checked} stated figures across {len(texts)} surfaces "
          f"match the data.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
