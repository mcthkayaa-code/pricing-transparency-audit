#!/usr/bin/env python3
"""The one place that knows where a product's saved source captures live.

**A product's `-sources/` directory sits in one of three places**, and which one is an
accident of when the record was collected:

    records/pass1/<slug>-sources/     59 products
    records/pass2/<slug>-sources/     26 products (the blind second reading)
    <slug>-sources/                   13 products, directly at the study root

Every tool that globbed only the first path was wrong about the other thirteen, and four of
them were: the provenance trace (D-037), the `archive_status` consistency check (D-061), the
dataset build's `local_source_files` column, and the quotation check. The damage was not
small — **D-060 reported a record as having no re-examinable evidence at all, naming seven
files as missing, and all seven exist at the study root.**

This module exists so that mistake cannot be made again with a source directory. It was the fifth
occurrence in this study of one defect: **a tool reading one location when there are several.** The
earlier four were a field stored in three shapes (D-020), a provenance check reading one field
(D-033), a citation trace keyed on one failure mode (D-037), and a status field trusted instead of
verified (D-061).

**It was not the last.** D-068 found the structural validator globbing `records/pass1/` alone when
live records sit in four folders — and defaulting to a path relative to the repository root, so run
from the study directory as every brief instructs, it matched nothing, printed nothing and exited 0.
Centralising the source-directory lookup here did not generalise: the same defect simply moved to a
different kind of location. Anywhere a tool names one folder, ask what the other folders are.

**What actually caught it:** not any of the four checks. The public-export tool refused to copy
files it had no rule for, printed them, and the paths had no `records/pass1/` prefix. A tool
that fails loudly on the unclassified found what four tools globbing one path missed.

    from source_paths import source_files, source_dirs
"""

import glob
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CANDIDATES = (
    os.path.join("records", "pass1", "{slug}-sources"),
    os.path.join("records", "pass2", "{slug}-sources"),
    # Added 2026-08-17 (D-074). An adjudicator that retrieves its own captures had nowhere
    # canonical to put them: no adjudicated record had a sources directory, and this tuple had
    # no entry for one. It saved to the study root instead — a location this module already
    # knows, so nothing was lost — and **flagged the gap rather than silently working around
    # it**, which is why the fix is here and not discovered later by a tool reporting a
    # confident wrong number. That is exactly how the first five occurrences were NOT found.
    os.path.join("records", "adjudicated", "{slug}-sources"),
    "{slug}-sources",
)


def source_dirs(slug, root=None):
    """Every existing source directory for this product, in the order searched."""
    base = root or HERE
    found = []
    for pattern in CANDIDATES:
        path = os.path.join(base, pattern.format(slug=slug))
        if os.path.isdir(path):
            found.append(path)
    return found


def source_files(slug, root=None):
    """Every file under every source directory for this product."""
    out = []
    for directory in source_dirs(slug, root):
        out += [p for p in glob.glob(os.path.join(directory, "**", "*"), recursive=True)
                if os.path.isfile(p)]
    return out


def source_bytes(slug, root=None):
    return sum(os.path.getsize(p) for p in source_files(slug, root))


def survey(root=None):
    """slug -> (dirs, file count, bytes) for every product with a pass-1 record."""
    base = root or HERE
    out = {}
    for path in sorted(glob.glob(os.path.join(base, "records", "pass1", "*.yaml"))):
        slug = os.path.basename(path)[:-5]
        dirs = source_dirs(slug, base)
        files = source_files(slug, base)
        out[slug] = (dirs, len(files), sum(os.path.getsize(p) for p in files))
    return out


if __name__ == "__main__":
    import collections
    data = survey()
    where = collections.Counter()
    for slug, (dirs, n, size) in data.items():
        if not dirs:
            where["NO SOURCE DIRECTORY"] += 1
            continue
        for d in dirs:
            where["study root" if not d.startswith(os.path.join(HERE, "records"))
                  else os.path.relpath(os.path.dirname(d), HERE)] += 1
    print(f"{len(data)} products with a pass-1 record\n")
    for place, count in where.most_common():
        print(f"  {place:<24}{count}")
    missing = [s for s, (d, _, _) in data.items() if not d]
    print(f"\nproducts with no source directory anywhere: {len(missing)}")
    for slug in missing:
        print(f"   {slug}")
