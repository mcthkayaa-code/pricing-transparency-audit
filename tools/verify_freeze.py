#!/usr/bin/env python3
"""Check the freeze stamp against the bytes on disk.

The stamp invites a reader to verify that the copy they hold is the copy that was frozen. That
invitation went untested for a day: one artifact had already drifted from its recorded hash and
nothing anywhere would have said so, because no check read the stamp back.

This is the study's most frequent defect in its purest form — **a claim nobody re-derived.** The
stamp is the one document that must not be wrong about its own contents, so it gets a checker.

The three-column table is the frozen set: a mismatch there is a defect and exits non-zero. The
four-column table below it is the living set: those are hashed for reference and are expected to
move, so a mismatch is reported and forgiven.

    python3 tools/verify_freeze.py
"""

import hashlib
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAMP = os.path.join(HERE, "orchestrator", "freeze-stamp.md")

FROZEN = re.compile(r"^\| `([0-9a-f]{16})` \| [\d,]+ \| `([^`]+)` \|$", re.M)
LIVING = re.compile(r"^\| `([0-9a-f]{16})` \| [\d,]+ \| `([^`]+)` \| [^|]+ \|$", re.M)


def digest(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()[:16]


def main():
    if not os.path.exists(STAMP):
        print("FAIL verify_freeze no freeze stamp at orchestrator/freeze-stamp.md")
        return 2
    text = open(STAMP, encoding="utf-8").read()

    frozen = FROZEN.findall(text)
    living = LIVING.findall(text)
    if not frozen:
        print("FAIL verify_freeze the stamp listed ZERO frozen artifacts — "
              "the table format changed and this checker went blind.")
        return 2

    failures = []
    for want, rel in frozen:
        path = os.path.join(HERE, rel)
        if not os.path.exists(path):
            failures.append(f"  MISSING   {rel}")
        elif (got := digest(path)) != want:
            failures.append(f"  MISMATCH  {rel}\n            stamp {want}  disk {got}")

    for want, rel in living:
        path = os.path.join(HERE, rel)
        if os.path.exists(path) and digest(path) != want:
            print(f"note: {rel} has moved since the stamp. Expected — it is a living document.")

    if failures:
        print(f"FAIL verify_freeze {len(failures)} of {len(frozen)} frozen artifacts do not match:")
        print("\n".join(failures))
        return 1

    print(f"OK verify_freeze {len(frozen)} frozen artifacts match the stamp; "
          f"{len(living)} living documents checked for reference.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
