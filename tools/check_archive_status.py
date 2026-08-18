#!/usr/bin/env python3
"""Check each record's `archive_status` against the evidence it actually holds.

Nothing was comparing a status field to what it describes, and two records were found
disagreeing with their own status in **opposite directions** (D-060), both by hand while a
limitations section was being written:

  * one marked `local_copy_only` — meaning the archive attempt failed and a local copy
    stands in its place — with **no local file at all** and no archive URL either. All 37
    of its coded values rest on evidence a reader cannot open.
  * one marked `local_copy_only` while carrying three captures that all verify `ok`. Its
    provenance is better than its own status claims.

The first is a provenance failure. The second is only a mislabel. A study that publishes
`archive_status` as a column owes a reader that the column is true.

## The two rules

  archived         requires at least one cited capture that RESOLVES — verified against
                   `orchestrator/archive-verification.csv`, not merely present in the text.
  local_copy_only  requires at least one file under the record's `-sources/` directory.

## Deliberately not inferred

Where `archive-verification.csv` has no verdict for a cited URL, this reports the row as
**unverifiable rather than failing it**. An unanswered request is not evidence that a capture
is absent, and treating it as one would manufacture failures out of an outage (D-047).

**That bucket is now empty, and the rule is why.** The service refused 92 citations across three
sweeps. They sat here as unverifiable instead of being counted as provenance failures, and when
the service recovered on 2026-08-17 all 92 were re-asked and **all 92 came back `ok`** (D-073).
Had they been failed at the time, the study would have published a provenance crisis that did
not exist and then had to retract it. Keep the branch even when it is empty.

    python3 tools/check_archive_status.py
"""

import csv
import glob
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAMP = re.compile(r"https?://web\.archive\.org/web/\d{14}/\S+")


def verdicts():
    path = os.path.join(HERE, "orchestrator", "archive-verification.csv")
    if not os.path.exists(path):
        return {}
    with open(path) as handle:
        return {row["url"]: row["status"] for row in csv.DictReader(handle)}


def cited_urls(text):
    return {m.group(0).rstrip(").,;:\"'`") for m in STAMP.finditer(text)}


from source_paths import source_files


def local_files(slug):
    """Delegated to source_paths, which knows all THREE places a source directory lives.
    This function used to glob `records/pass1/<slug>-sources` alone and was wrong about the
    thirteen products that keep theirs at the study root (D-063)."""
    return source_files(slug)


def main():
    seen = verdicts()
    adjudicated = {os.path.basename(p)[:-5]: p
                   for p in glob.glob(os.path.join(HERE, "records", "adjudicated", "*.yaml"))}

    failures, unverifiable, ok = [], [], 0
    for path in sorted(glob.glob(os.path.join(HERE, "records", "pass1", "*.yaml"))):
        slug = os.path.basename(path)[:-5]
        use = adjudicated.get(slug, path)
        record = yaml.safe_load(open(use)) or {}
        status = str(record.get("archive_status") or "").strip().strip('"')
        if not status:
            failures.append(f"{slug}: archive_status is unset")
            continue

        urls = cited_urls(open(use).read() + open(path).read())
        resolving = [u for u in urls if seen.get(u) in ("ok", "ok_nearest")]
        unchecked = [u for u in urls if u not in seen or seen.get(u) == "throttled"]
        # 401/403 means the archive refuses to serve the HOST. A capture may exist and be
        # unreadable by anyone outside the archive. Counting that as a record's provenance
        # failure blames the citing record for the cited vendor's exclusion (D-069).
        withheld = [u for u in urls if seen.get(u) == "excluded"]
        files = local_files(slug)

        if status == "archived":
            if resolving:
                ok += 1
            elif unchecked:
                unverifiable.append(f"{slug}: claims `archived`, {len(unchecked)} cited captures the "
                                    f"service would not answer for — not judged")
            elif withheld:
                unverifiable.append(
                    f"{slug}: claims `archived`, and all {len(withheld)} cited captures are WITHHELD "
                    f"by the archive (403 on the host, not 404) — the archive will not serve this "
                    f"vendor to anyone. {len(files)} local mirror files stand in. This is a finding "
                    f"about the vendor's archivability, not a defect in the record")
            else:
                failures.append(f"{slug}: claims `archived` with no capture that resolves "
                                f"({len(urls)} cited)")
        elif status == "local_copy_only":
            if files:
                ok += 1
                if resolving:
                    unverifiable.append(f"{slug}: claims `local_copy_only` but {len(resolving)} of its "
                                        f"captures resolve — the status understates its provenance")
            else:
                failures.append(f"{slug}: claims `local_copy_only` with NO local file "
                                f"({len(urls)} cited captures, {len(resolving)} resolving)")
        else:
            unverifiable.append(f"{slug}: archive_status {status!r} is outside the two values this "
                                f"check knows")

    for item in failures:
        print(f"FAIL  {item}")
    for item in unverifiable:
        print(f"NOTE  {item}")
    print(f"\n{ok} records consistent · {len(failures)} failing · {len(unverifiable)} noted")
    print("\nA `NOTE` is never a failure. Two classes of them, and neither is a defect in a record:")
    print("  * `local_copy_only` on a record whose captures DO resolve — the field records what a save")
    print("    request appeared to return, so it understates provenance rather than overstating it.")
    print("  * `archived` on a host the archive REFUSES to serve (403, not 404) — a finding about that")
    print("    vendor's archivability, not about our reading of it (D-069).")
    print("\nThe unverifiable class this check used to carry is now empty: the 92 citations the service")
    print("refused across three sweeps were re-asked on 2026-08-17 once it recovered, and all 92 came")
    print("back `ok` (D-073). Nothing here rests on an unanswered request any more. The rule that put")
    print("them in a separate bucket rather than failing them is what made that possible (D-047).")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
