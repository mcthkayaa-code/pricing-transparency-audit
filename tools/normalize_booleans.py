#!/usr/bin/env python3
"""Repair YAML boolean coercion in coded values.

Unquoted `yes` / `no` in YAML parse as booleans, so the same coded value ends up
stored two ways across records. This rewrites `value: yes` -> `value: "yes"` (and
`no`, plus YAML's other boolean spellings) INSIDE the variables block, leaving
prose, evidence text and every other field untouched. Idempotent.

It ALSO fixes the top-level administrative fields that carry yes/no semantics.
The original D-006 pass scoped itself to the variables block, so `paid_submission`
kept parsing as a boolean in sixteen records — the record template itself still
showed it unquoted. That field decides which products enter the paper's
"excluding paid submissions" figures, so two spellings of one value would split
those counts exactly as D-006 warned.
"""
import glob, re, sys

# Top-level admin fields whose values are yes/no rather than prose.
ADMIN_BOOL_FIELDS = ("paid_submission",)

BOOLS = r"(?:yes|no|true|false|on|off|True|False|Yes|No|On|Off|TRUE|FALSE|YES|NO)"
# `value:` lines, and the compact `{ value: yes, source: ... }` form
LINE = re.compile(rf"^(\s*value:\s*){BOOLS}(\s*(?:#.*)?)$")
INLINE = re.compile(rf"(\{{\s*value:\s*){BOOLS}(\s*,)")
ADMIN_LINE = re.compile(rf"^((?:{'|'.join(ADMIN_BOOL_FIELDS)}):\s*){BOOLS}(\s*(?:#.*)?)$")

CANON = {"yes": "yes", "true": "yes", "on": "yes", "no": "no", "false": "no", "off": "no"}

def canon(m_text):
    return CANON[m_text.strip().lower()]

def fix(path):
    src = open(path, encoding="utf8").read()
    out, changed, in_vars = [], 0, False
    for line in src.splitlines(True):
        if re.match(r"^variables:\s*$", line):
            in_vars = True
        elif re.match(r"^\S", line) and not line.startswith("variables:"):
            in_vars = False
        if in_vars:
            m = LINE.match(line.rstrip("\n"))
            if m:
                raw = line.rstrip("\n")[len(m.group(1)):]
                raw = raw[: len(raw) - len(m.group(2))]
                line = f'{m.group(1)}"{canon(raw)}"{m.group(2)}\n'
                changed += 1
            else:
                new, n = INLINE.subn(
                    lambda mm: f'{mm.group(1)}"{canon(mm.group(0)[len(mm.group(1)):-len(mm.group(2))])}"{mm.group(2)}',
                    line)
                if n:
                    line, changed = new, changed + n
        else:
            # top-level admin fields with yes/no semantics
            am = ADMIN_LINE.match(line.rstrip("\n"))
            if am:
                raw = line.rstrip("\n")[len(am.group(1)):]
                raw = raw[: len(raw) - len(am.group(2))] if am.group(2) else raw
                line = f'{am.group(1)}"{canon(raw)}"{am.group(2)}\n'
                changed += 1
        out.append(line)
    if changed:
        open(path, "w", encoding="utf8").write("".join(out))
    return changed

if __name__ == "__main__":
    pat = sys.argv[1] if len(sys.argv) > 1 else "Data/seo/research/pricing-transparency/records/pass*/*.yaml"
    total = 0
    for f in sorted(glob.glob(pat)):
        n = fix(f)
        if n:
            print(f"{f.split('/')[-1][:-5]}: {n} value(s) quoted")
            total += n
    print(f"total: {total}")
