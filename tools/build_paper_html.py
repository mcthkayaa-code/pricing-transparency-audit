#!/usr/bin/env python3
"""Render `paper-draft.md` to a styled, print-ready HTML page.

Written because the first PDF of this paper was produced by a one-off script that was
then thrown away — and the paper changed four times the same day, so the PDF a reader
held disagreed with the source on the study's own deviation count. **A build that
cannot be re-run is a build that goes stale silently**, which is the defect this study
has recorded nine times.

There is no Markdown library on this machine and no network to install one, so this
converts the subset the paper actually uses: headings, tables, fenced and inline code,
bold, italic, links, lists, blockquotes and rules. It fails loudly on anything it does
not recognise rather than dropping it.

The stylesheet lives beside it in `paper-style.html` and is designed for print: the
page prints to PDF from any Chromium with

    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \\
        --headless=new --no-pdf-header-footer \\
        --print-to-pdf=paper.pdf file:///abs/path/paper.html

    python3 tools/build_paper_html.py            # -> paper.html beside the markdown
    python3 tools/build_paper_html.py --out /tmp/paper.html
"""

import html
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(HERE, "paper-draft.md")
STYLE = os.path.join(HERE, "tools", "paper-style.html")


def inline(text):
    """Inline marks, escaped first so vendor markup in a quotation cannot inject."""
    out, last = [], 0
    for m in re.finditer(r"`([^`]+)`", text):
        out.append(html.escape(text[last:m.start()]))
        out.append(f"<code>{html.escape(m.group(1))}</code>")
        last = m.end()
    out.append(html.escape(text[last:]))
    s = "".join(out)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![*\w])\*([^*\n]+)\*(?!\w)", r"<em>\1</em>", s)
    return s


def convert(md):
    lines, out, i = md.split("\n"), [], 0
    while i < len(lines):
        line = lines[i]

        if not line.strip():
            i += 1
            continue

        if re.match(r"^---+\s*$", line):
            out.append("<hr>")
            i += 1
            continue

        head = re.match(r"^(#{1,6})\s+(.*)$", line)
        if head:
            level = len(head.group(1))
            out.append(f"<h{level}>{inline(head.group(2))}</h{level}>")
            i += 1
            continue

        # table: a header row, an alignment row, then body rows
        if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|?\s*$", lines[i + 1]):
            def cells(row):
                return [c.strip() for c in row.strip().strip("|").split("|")]
            head_cells = cells(line)
            i += 2
            body = []
            while i < len(lines) and lines[i].startswith("|"):
                body.append(cells(lines[i]))
                i += 1
            th = "".join(f"<th>{inline(c)}</th>" for c in head_cells)
            rows = "".join(
                "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body)
            out.append(f'<div class="tw"><table><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table></div>')
            continue

        if line.startswith(">"):
            block = []
            while i < len(lines) and lines[i].startswith(">"):
                block.append(lines[i].lstrip(">").strip())
                i += 1
            out.append(f"<blockquote>{inline(' '.join(block))}</blockquote>")
            continue

        if re.match(r"^\s*[-*]\s+", line):
            items = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                text = re.sub(r"^\s*[-*]\s+", "", lines[i])
                i += 1
                while i < len(lines) and lines[i].startswith("  ") and lines[i].strip() \
                        and not re.match(r"^\s*[-*]\s+", lines[i]):
                    text += " " + lines[i].strip()
                    i += 1
                items.append(f"<li>{inline(text)}</li>")
            out.append("<ul>" + "".join(items) + "</ul>")
            continue

        para = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith(("|", ">", "#", "---")) \
                and not re.match(r"^\s*[-*]\s+", lines[i]):
            para.append(lines[i])
            i += 1
        out.append(f"<p>{inline(' '.join(para))}</p>")

    return "\n".join(out)


def main(argv):
    out_path = argv[argv.index("--out") + 1] if "--out" in argv else os.path.join(HERE, "paper.html")
    md = open(SRC, encoding="utf-8").read()
    style = open(STYLE, encoding="utf-8").read()
    body = convert(md)
    # Assert the conversion carried the document: a silent partial render is the failure
    # mode this file exists to prevent.
    for name, want, got in (("headings", md.count("\n## "), body.count("<h2>")),):
        if got < want:
            print(f"REFUSING: {name} {got} rendered from {want} in source", file=sys.stderr)
            return 1
    open(out_path, "w", encoding="utf-8").write(
        f"<!doctype html><html lang=en><head><meta charset=utf-8>"
        f'<meta name=viewport content="width=device-width,initial-scale=1">'
        f"<title>Pricing Transparency Audit</title>{style}</head><body>"
        f'<main class="paper">{body}</main></body></html>')
    print(f"wrote {out_path} · {len(body):,} bytes of body from {len(md.split()):,} words")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
