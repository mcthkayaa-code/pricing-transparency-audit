#!/usr/bin/env python3
"""Emit a pass-2 brief's assignment block, generated from the frame.

The orchestrator typed these fields by hand for the first ten pass-2 assignments
and got three of them wrong — one with the wrong vendor domain entirely, pointing
at a different company. A coder caught it because the brief also told it to read
the frame, but relying on the coder to catch the assignment's own errors is not a
control, it is luck.

This prints the block to paste. It never invents a value: everything comes from
`frame-for-pass2.csv`, which is itself derived from the frozen frame.

    python3 tools/brief_fields.py anomaly-ai
    python3 tools/brief_fields.py --all-pending
"""

import csv
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRAME = os.path.join(HERE, "frame-for-pass2.csv")
SELECTION = os.path.join(HERE, "orchestrator", "double-coded-selection.csv")
PASS2 = os.path.join(HERE, "records", "pass2")


def rows(path):
    with open(path) as handle:
        return list(csv.DictReader(line for line in handle if not line.startswith("#")))


def block(row):
    return (
        f"- **product_id:** `{row['product_id']}` · **product_name:** {row['product_name']} · "
        f"**vendor_home_url:** {row['vendor_home_url']}\n"
        f"- **category:** {row['category']} · **paid_submission:** \"{row['paid_submission']}\" · "
        f"**product_status:** {row['product_status']}\n"
        f"- **Record:** `Data/seo/research/pricing-transparency/records/pass2/{row['product_id']}.yaml`\n"
        f"- **Sources dir:** `Data/seo/research/pricing-transparency/records/pass2/"
        f"{row['product_id']}-sources/`\n"
        f"- `coder_pass: 2`, `coder_role: second`  (the codebook enum is primary|second|"
        f"adjudicated — NOT 'secondary'), write your OWN `collection_date`."
    )


def done():
    found = set()
    for path in glob.glob(os.path.join(PASS2, "*.yaml")):
        if re.search(r'^status:\s*"?complete', open(path).read(), re.M):
            found.add(os.path.basename(path)[:-5])
    return found


def main(argv):
    frame = {r["product_id"]: r for r in rows(FRAME)}

    if argv and argv[0] == "--all-pending":
        selected = [r["product_id"] for r in rows(SELECTION)]
        finished = done()
        pending = [p for p in selected if p not in finished]
        print(f"# {len(pending)} of {len(selected)} pass-2 records outstanding, alphabetical:\n")
        for product in sorted(pending):
            print(f"## {product}\n{block(frame[product])}\n")
        return 0

    if not argv:
        print(__doc__)
        return 2

    for product in argv:
        if product not in frame:
            print(f"# {product}: NOT IN FRAME — check the id", file=sys.stderr)
            return 1
        print(block(frame[product]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
