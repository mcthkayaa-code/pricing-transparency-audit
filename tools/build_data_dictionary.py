#!/usr/bin/env python3
"""Generate the dataset's data dictionary FROM the codebook, so it cannot drift from it.

The dataset is meant to be cited as a source. A reader who arrives at `coded-values.csv`
with nothing else must be able to use it, and 37 of its columns are codebook variable names
that mean nothing on their own. This emits `dataset/data-dictionary.md`: every column, what
it holds, and for the coded variables the definition and the full table of permitted values
with their meanings.

**Generated, never hand-written.** A dictionary maintained by hand beside a frozen codebook
drifts from it, and a reader has no way to tell which one is authoritative. This parses
`codebook-v1.md` and reports any variable whose entry it cannot read, rather than quietly
emitting a shorter dictionary than the dataset needs — the failure mode this study has found
in its own tools four times.

    python3 tools/build_data_dictionary.py
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODEBOOK = os.path.join(HERE, "codebook-v1.md")
OUT = os.path.join(HERE, "dataset", "data-dictionary.md")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_records import CODED

# Columns that are not codebook variables. Described here because they are administrative
# or computed, and a reader needs them defined in the same place as everything else.
NON_CODED = {
    "product_id": "Stable slug identifying the product. The join key, and the frame's own identifier.",
    "row_provenance": "`adjudicated` where a third reading resolved a disagreement between the two "
                      "blind coders, `primary` where the pass-1 record publishes unchanged. Pass 2 "
                      "never publishes: it is the blind second reading behind the reliability figure.",
    "product_name": "Vendor's name for the product, copied from the frozen frame. Where a vendor "
                    "rebranded during the window the frame name is kept and the new name appears in "
                    "`coder_note` and the source URLs (queue item A-006).",
    "category": "The authoring publication's own category for the product. Editorial, not a taxonomy.",
    "product_status": "`active` or `discontinued` as at the frame freeze. Three products were "
                      "discontinued; two of those statuses were stale in the frame and were corrected "
                      "when found (deviation D-008).",
    "paid_submission": "Whether the vendor paid the publication for a listing. Declared because it "
                       "is a conflict of interest, not because it changes a coded value.",
    "entry_tier_name": "The vendor's own name for the tier every tier-scoped variable is measured "
                       "against, selected under `sampling-rules.md` §7.2 by lowest annual-equivalent "
                       "single-seat cost in the pricing page's default display state.",
    "collection_date": "The date this product was coded. The window ran 2026-08-05 to 2026-08-13.",
    "coder_role": "`primary`, `second` or `adjudicated`.",
    "coder_pass": "1, 2 or 3.",
    "archive_status": "**As recorded by the coder**, and known to be unreliable: it captures what a "
                      "save request appeared to return rather than whether a capture exists. Verified "
                      "against the capture index, 14 of 76 rows disagree with it and 12 of those "
                      "understate their own coverage (deviation D-061). Use "
                      "`archive_status_verified` instead and keep this column for comparison.",
    "primary_source_url": "The pricing page or equivalent the record is anchored to.",
    "archive_status_verified": "**Computed at build time, not coded.** `archived` where at least one "
                               "cited capture resolves, `local_copy_only` where a local capture exists, "
                               "`NO_REEXAMINABLE_EVIDENCE` where neither does. **No row is the third "
                               "case.** One was reported as such and the report was RETRACTED: the "
                               "seven files it named as missing all existed, in a source directory the "
                               "checking tool did not know to look in (D-063). Verified across all 76 "
                               "rows: 68 `archived`, 8 `local_copy_only`, 0 with neither.",
    "resolving_captures": "Computed: how many of this row's cited archive captures were verified to "
                          "resolve at the timestamp they cite, out of 516 cited corpus-wide. **482 "
                          "resolve (93.4%).** Verification ran four times: three during the study, "
                          "when the service refused 92 citations and they were counted as unverified "
                          "rather than failed, and a fourth after it recovered, when all 92 answered "
                          "`ok` (D-073). Eight rows show 0 here; every one of them keeps local capture "
                          "files, and no row in the dataset has neither.",
    "local_source_files": "Computed: how many files exist under this product's `-sources/` directory. "
                          "For 159 coded values corpus-wide the local capture is the only surviving "
                          "evidence, which is why the release ships those directories.",
}


def entries():
    """variable -> {domain, type, index_item, definition, values_table} parsed from the codebook."""
    text = open(CODEBOOK).read()
    out, unparsed = {}, []
    for name in CODED:
        section = re.search(rf"^#### `{re.escape(name)}`(.*?)(?=^#### |\Z)", text, re.M | re.S)
        if not section:
            unparsed.append(name)
            continue
        body = section.group(1)
        meta = re.search(r"\*\*Domain\*\*\s*([^·\n]*)·\s*\*\*Type\*\*\s*([^·\n]*)"
                         r"(?:·\s*\*\*Index item\*\*\s*([^\n]*))?", body)
        definition = re.search(r"\*\*Definition\.\*\*\s*(.+?)(?:\n\n|\Z)", body, re.S)
        # The value cell is usually a backticked code (`yes`) but sometimes a bare word
        # ("money", "integer"). An earlier version of this regex excluded the backtick
        # character from the cell and so matched only the bare-word tables — it reported 12
        # variables as having no value table when the codebook gives 35 of them one, and
        # `check_value_enums.py`, which requires backticks, had already found only 2 missing.
        # Two parsers disagreeing is what surfaced it.
        rows = re.findall(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", body, re.M)
        rows = [(v.strip(), m.strip()) for v, m in rows
                if v.strip() not in ("Value", "---", ":---") and not set(v.strip()) <= {"-", ":"}]
        # 12 variables state their values in a **Values.** sentence rather than a table.
        # `check_value_enums.py` already had this fallback; this generator did not, and
        # reported them as tableless until the two were compared. Where the sentence is the
        # only statement of permitted values, it IS the value list and is carried verbatim.
        values_sentence = ""
        if not rows:
            found = re.search(r"\*\*Values\.\*\*\s*(.+?)(?:\n\n|\Z)", body, re.S)
            if found:
                values_sentence = " ".join(found.group(1).split())
        out[name] = {
            "domain": (meta.group(1).strip() if meta else ""),
            "type": (meta.group(2).strip() if meta else ""),
            "item": (meta.group(3).strip() if meta and meta.group(3) else ""),
            "definition": " ".join(definition.group(1).split()) if definition else "",
            "values": rows,
            "values_sentence": values_sentence,
        }
        if not definition or not (rows or values_sentence):
            unparsed.append(f"{name} (partial: "
                            f"{'no definition' if not definition else ''}"
                            f"{' and ' if not definition and not rows else ''}"
                            f"{'no value table' if not rows else ''})")
    return out, unparsed


def main():
    parsed, unparsed = entries()
    lines = [
        "# Data dictionary", "",
        "**Generated from `codebook-v1.md` by `tools/build_data_dictionary.py`. Do not hand-edit:**",
        "a dictionary maintained by hand beside a frozen codebook drifts from it, and a reader has no",
        "way to tell which is authoritative.", "",
        "Two files carry the data. `coded-values.csv` is one row per product and one column per",
        "variable. `coded-long.csv` is one row per (product, variable) and additionally carries the",
        "**source URL, the coder's evidence, and the attribution kind for every `unknown`** — it is the",
        "file that makes a value checkable rather than merely readable.", "",
        "Read `limitations-register.md` before using any figure, and `methods-who-coded.md` before",
        "reading the reliability statistic: **the coders were language models**, so α = 0.811 measures",
        "agreement between two independent model readings and not human inter-coder reliability.", "",
        "---", "", "## Values that appear across many variables", "",
        "| Value | Meaning |", "|---|---|",
        "| `unknown` | Could not be determined from the vendor's documents. **Every `unknown` in this "
        "dataset is attributed to a cause** in `coded-long.csv`: `vendor_silence` (84.2%), "
        "`instrument_gap` (12.2%, the codebook could not express what the vendor published), "
        "`access_failure` (2.9%), or `unattributable_weak_basis` (0.7%). |",
        "| `not_applicable` | The construct cannot exist for this product, on positive documentary "
        "evidence. Vendor silence is `unknown`, not this. |",
        "| `conflicting` | Two official sources of equal authority disagree. Both are recorded. |",
        "| `non_usd` | The vendor publishes a price in one currency and it is not USD, with no USD "
        "figure obtainable and no currency selector. |",
        "| `no_public_price` | A paid tier exists and its price is not published; a buyer must contact "
        "sales. |", "",
        "---", "", "## Administrative and computed columns", "",
    ]
    for name, description in NON_CODED.items():
        lines += [f"### `{name}`", "", description, ""]

    lines += ["---", "", f"## Coded variables ({len(CODED)})", "",
              "Each carries the codebook's own definition and its full table of permitted values. The",
              "decision rule a coder applied, the evidence required, and a worked example are in",
              "`codebook-v1.md` under the same heading.", ""]
    for name in CODED:
        info = parsed.get(name)
        lines.append(f"### `{name}`")
        lines.append("")
        if not info:
            lines += ["**NOT FOUND IN THE CODEBOOK.** Reported rather than omitted.", ""]
            continue
        meta = " · ".join(x for x in [f"Domain {info['domain']}" if info["domain"] else "",
                                     f"Type: {info['type']}" if info["type"] else "",
                                     f"Index item {info['item']}" if info["item"] else ""] if x)
        if meta:
            lines += [meta, ""]
        if info["definition"]:
            lines += [info["definition"], ""]
        if info["values"]:
            lines += ["| Value | Meaning |", "|---|---|"]
            for value, meaning in info["values"]:
                lines.append(f"| {value} | {meaning} |")
            lines.append("")
        elif info.get("values_sentence"):
            lines += [f"**Permitted values.** {info['values_sentence']}", ""]

    if unparsed:
        lines += ["---", "", "## Variables this generator could not fully read", "",
                  "Listed rather than silently emitted short. A dictionary that quietly covers less than",
                  "the dataset is the failure mode this study has found in its own tools four times.", ""]
        for item in unparsed:
            lines.append(f"- {item}")
        lines.append("")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w").write("\n".join(lines) + "\n")
    full = sum(1 for n in CODED if parsed.get(n) and parsed[n]["definition"]
               and (parsed[n]["values"] or parsed[n].get("values_sentence")))
    print(f"wrote {OUT}")
    print(f"{len(CODED)} coded variables · {full} with both a definition and a value table")
    print(f"{len(unparsed)} reported as unparseable or partial")
    for item in unparsed:
        print(f"   {item}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
