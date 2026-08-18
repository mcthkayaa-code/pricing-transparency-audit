#!/usr/bin/env python3
"""Report sources whose cited archive capture predates the coder's own read.

The final-day change sweep found one: a record pairing `access_date: 2026-08-12` with an
archive URL stamped `20260807`, five days earlier — **and on the far side of an edit that
same sweep demonstrated**, a pricing-page FAQ cut from 34 answers to 11. A reader following
that citation opens a materially different document from the one the coder read. The coded
values survive (the operative text is in both captures), so this is a provenance defect
rather than a value defect, but it is exactly the kind a reader hits and the study does not.

## THIS IS A REVIEW LIST, NOT A DEFECT COUNT

Read this before quoting any number it prints. **It measures the gap, not whether the gap is
wrong**, and there are at least three legitimate reasons a citation predates a read:

  * **No nearer capture exists.** A coder who read a page live and cited the newest capture
    available did the right thing. Most of the large gaps here are that: one product's
    documentation cites a capture from 2022 because the archive holds nothing newer.
  * **A discontinued product.** Records for vendors that shut down legitimately cite older
    material; there is nothing recent to cite.
  * **A deliberate bracketing choice.** One adjudication here cited captures from 2026-05-18
    and 2026-08-05 for a 2026-08-17 read, precisely so the evidence bracketed the collection
    window on both sides, and argued it in the record. This tool flags that as drift. It is
    the opposite of a defect.

**The discriminating question this tool cannot answer is whether a NEARER capture existed and
was not cited.** Answering it needs one archive query per source, and it is the check worth
building for wave 2 — ideally in the collector, so a coder cites the nearest capture at
collection time rather than having it audited afterwards.

So: the count below is a denominator for a reading, never a headline. The one confirmed
avoidable case is named in the deviations log, not inferred from this list.

    python3 tools/check_citation_recency.py            # sources 2+ days adrift
    python3 tools/check_citation_recency.py 14         # a wider threshold
"""

import datetime
import glob
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAMP = re.compile(r"web\.archive\.org/web/(\d{14})")


def sources(record):
    """Both registry shapes: `kind`/`accessed`/`archive` and `label`/`access_date`/`archive_url`."""
    for entry in (record.get("sources") or []):
        if not isinstance(entry, dict):
            continue
        accessed = str(entry.get("accessed") or entry.get("access_date") or "").strip()[:10]
        archive = str(entry.get("archive") or entry.get("archive_url") or "")
        label = str(entry.get("kind") or entry.get("label") or "")[:26]
        yield label, accessed, archive


def main(argv):
    threshold = int(argv[0]) if argv else 2
    adjudicated = {os.path.basename(p)[:-5]
                   for p in glob.glob(os.path.join(HERE, "records", "adjudicated", "*.yaml"))}

    rows, checked = [], 0
    for path in sorted(glob.glob(os.path.join(HERE, "records", "pass1", "*.yaml"))):
        slug = os.path.basename(path)[:-5]
        use = (os.path.join(HERE, "records", "adjudicated", f"{slug}.yaml")
               if slug in adjudicated else path)
        try:
            record = yaml.safe_load(open(use)) or {}
        except yaml.YAMLError:
            continue
        for label, accessed, archive in sources(record):
            stamp = STAMP.search(archive)
            if not (accessed and stamp):
                continue
            try:
                read = datetime.date.fromisoformat(accessed)
            except ValueError:
                continue
            captured = datetime.date(int(stamp.group(1)[:4]),
                                     int(stamp.group(1)[4:6]), int(stamp.group(1)[6:8]))
            checked += 1
            gap = (read - captured).days
            if abs(gap) >= threshold:
                rows.append((abs(gap), slug, label, accessed, stamp.group(1)[:8], gap))

    rows.sort(reverse=True)
    print(f"{checked} sources carry both an access date and a timestamped capture.")
    print(f"{len(rows)} of them are {threshold}+ days adrift.\n")
    print(f"{'product':<24}{'source':<28}{'read':<12}{'capture':<10}{'gap':>6}")
    print("-" * 82)
    for _, slug, label, accessed, cap, gap in rows:
        print(f"{slug:<24}{label:<28}{accessed:<12}{cap:<10}{gap:>+6}")

    behind = sum(1 for r in rows if r[5] > 0)
    print(f"\n{behind} cite a capture from BEFORE the read, {len(rows) - behind} from after.")
    print("A capture predating the read is the risky direction: the page can have changed in")
    print("between, and a reader following the citation sees the earlier document.")
    print("\nThis is a review list and not a defect count — read the module docstring before")
    print("quoting any figure from it. Most large gaps here are records citing the newest")
    print("capture that exists, which is correct behaviour, and one is a deliberate bracketing")
    print("choice argued in its own record.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
