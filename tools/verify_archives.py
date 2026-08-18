#!/usr/bin/env python3
"""Verify that every cited archive capture actually exists at its cited timestamp.

This is the only provenance check the dataset has. 509 distinct timestamped
captures are cited across the records, and 18 records keep no local mirror of
what they read, so archive.org IS the evidence a reader can re-examine (D-033).

And it is known to be fallible: one record cited a dated capture that never
existed. The URL 302-redirected to another pass's earlier capture — the response
carried `x-archive-redirect-reason: found capture at …` — and the quoted figure
appeared nowhere on any date (D-023).

Outcomes per URL — and the whole point of the list is that only ONE of them means
the capture is not there:

  ok           200 at the cited timestamp. The capture is there.
  redirect     archive.org served a DIFFERENT timestamp. The citation points at a
               capture that does not exist; whatever was quoted from it must be
               re-verified against the capture actually served.
  missing      404 — archive.org answered, and there is no capture.
  throttled    the service refused to answer (503/429/no response). This says
               NOTHING about the capture. It is recorded separately and re-run
               later, never counted as a provenance failure.
  excluded     401/403 — the archive refuses to serve this HOST. A capture may well
               exist; nobody outside the archive can read it. Not absence, and not
               a defect in the citing record.
  unclassified any other status. Named rather than bucketed, because the two
               corrections below both came from a status quietly landing in a
               bucket that asserted more than the response supported.

**`throttled` was added** after the first full sweep logged 110 citations as `missing`
on the strength of empty responses. Re-tested one at a time and slowly, every one of
them returned 503: archive.org had throttled this study partway through the run,
exactly as D-012 records.

**`excluded` was added on 2026-08-17 (D-069)** for the same reason one status code
over. 403 had been falling through to `missing`, and it turned out to account for
**13 of the 14 rows this tool called missing** — twelve for one vendor whose entire
domain the archive refuses, one for a video-share host. The study's real archival
absence is a single citation out of 511. The evidence was in this tool's own `detail`
column the whole time, which recorded `HTTP 403` beside a verdict of `missing`.

"We could not ask", "we are not allowed to read it" and "the capture is not there"
are three different facts. A checker that merges any of them manufactures a
provenance crisis out of someone else's policy.

## Reads every storage shape, deliberately

Archive URLs live in the top-level `sources` registry under `archive` in some
records and `archive_url` in others, and also inside per-variable `source` dicts.
A checker that reads one shape produces a confident wrong number — that is D-020,
and D-033 is the same defect committed a second time while auditing for it. So
this walks the whole parsed document and collects every web.archive.org URL it
finds, wherever it sits.

## Polite and resumable

archive.org rate-limits this study (D-012). Requests are spaced, and results are
appended to the output as they come, so an interrupted run resumes without
re-requesting what it already has.

    python3 tools/verify_archives.py                # verify all, resuming
    python3 tools/verify_archives.py --delay 2.0    # slower
    python3 tools/verify_archives.py --report       # summarise what exists so far
"""

import csv
import glob
import os
import re
import subprocess
import sys
import time

import yaml

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "orchestrator", "archive-verification.csv")
STAMP = re.compile(r"web\.archive\.org/web/(\d{4,14})")


def walk(node, found):
    """Collect every web.archive.org URL anywhere in the document."""
    if isinstance(node, dict):
        for value in node.values():
            walk(value, found)
    elif isinstance(node, list):
        for item in node:
            walk(item, found)
    elif isinstance(node, str):
        for match in re.finditer(r"https?://web\.archive\.org/web/\S+", node):
            url = match.group(0).rstrip(").,;:\"'`>]}*")
            # `/web/2026/<target>` is "latest capture in 2026", a wildcard the
            # service resolves at request time. It is not a citation OF a capture,
            # so a redirect from it is correct behaviour rather than a bad citation.
            # Counting those as failures buried the real ones on the first run.
            stamp = STAMP.search(url)
            if not stamp or len(stamp.group(1)) < 14:
                continue
            # A timestamp with no target URL after it cites nothing.
            after = url.split(stamp.group(1), 1)[1].lstrip("/")
            if not after.startswith("http"):
                continue
            found.add(url)


def cited():
    """-> {url: [(pass, product), ...]} across every record and storage shape."""
    out = {}
    for folder in ("pass1", "pass2", "adjudicated"):
        for path in sorted(glob.glob(os.path.join(HERE, "records", folder, "*.yaml"))):
            product = os.path.basename(path)[:-5]
            try:
                record = yaml.safe_load(open(path)) or {}
            except yaml.YAMLError:
                continue
            found = set()
            walk(record, found)
            for url in found:
                out.setdefault(url, []).append((folder, product))
    return out


def check(url, timeout=25):
    """-> (status, served_timestamp, detail). Uses curl: WebFetch refuses archive.org."""
    cited_stamp = STAMP.search(url)
    cited_stamp = cited_stamp.group(1) if cited_stamp else ""
    try:
        proc = subprocess.run(
            # A one-byte ranged GET, not HEAD: archive.org answers HEAD unreliably
            # and the first run logged "no response" for captures that are in fact
            # present. This keeps the transfer trivial while using real GET
            # semantics, and -D - keeps the headers the redirect check reads.
            ["curl", "-sS", "-o", "/dev/null", "-D", "-", "--max-time", str(timeout),
             "-r", "0-0", "-A", "aitoolspolice-research/1.0 (pricing transparency audit)", url],
            capture_output=True, text=True, timeout=timeout + 10,
        )
    except (subprocess.TimeoutExpired, OSError) as exc:
        # A request that never completed is not a capture that is not there. This returned
        # `missing` until D-069 — the same conflation as the 403 fall-through below, in the
        # one branch where the study never even reached the service.
        return "throttled", "", f"request failed locally: {type(exc).__name__}"

    head = proc.stdout or ""
    code = ""
    first = re.search(r"^HTTP/[\d.]+ (\d{3})", head, re.M)
    if first:
        code = first.group(1)

    reason = re.search(r"^x-archive-redirect-reason:\s*(.+)$", head, re.M | re.I)
    location = re.search(r"^location:\s*(.+)$", head, re.M | re.I)

    served = ""
    if location:
        got = STAMP.search(location.group(1))
        if got:
            served = got.group(1)

    if reason or (served and cited_stamp and not served.startswith(cited_stamp[:8])):
        detail = reason.group(1).strip() if reason else f"redirected to {served}"
        return "redirect", served, detail
    if code in ("200", "206"):          # 206 = the ranged GET succeeded
        return "ok", cited_stamp, ""
    if code in ("301", "302") and served and served.startswith(cited_stamp[:8]):
        return "ok", served, "same-day canonical redirect"
    if code == "404":
        return "missing", "", "404 — no capture"
    if code in ("429", "503", "502", "504", ""):
        return "throttled", "", f"service refused: HTTP {code or 'no response'}"
    if code in ("401", "403"):
        # A 403 is the archive REFUSING to serve a domain, not a statement that no capture
        # exists. It fell through to `missing` here until 2026-08-17 (D-069), which asserted
        # absence on 13 of the 14 rows this tool called missing — the same conflation D-047
        # fixed for 503, one status code over. Verified as a domain property, not a property
        # of this study's requests: cdx queries for hostinger.com return 403 on every URL form
        # while squarespace.com, wix.com, canva.com and gptzero.me return 200 in the same run.
        return "excluded", served, f"HTTP {code} — archive refuses this host, capture not readable"
    return "unclassified", served, f"HTTP {code} — no rule for this status; NOT treated as absence"


def load_done():
    if not os.path.exists(OUT):
        return {}
    with open(OUT) as handle:
        return {row["url"]: row for row in csv.DictReader(handle)}


def main(argv):
    delay = 1.0
    if "--delay" in argv:
        delay = float(argv[argv.index("--delay") + 1])

    urls = cited()
    done = load_done()

    if "--report" in argv:
        counts = {}
        for row in done.values():
            counts[row["status"]] = counts.get(row["status"], 0) + 1
        print(f"{len(urls)} distinct archive URLs cited · {len(done)} verified so far\n")
        for status in ("ok", "ok_nearest", "redirect", "missing", "throttled", "excluded", "unclassified"):
            print(f"  {status:<10} {counts.get(status, 0)}")
        bad = [r for r in done.values() if r["status"] != "ok"]
        if bad:
            print(f"\n{len(bad)} not clean:")
            for row in bad:
                print(f"  [{row['records']}] {row['status']}: {row['detail']}\n    {row['url'][:130]}")
        return 0

    # A throttled row is not a result. Re-ask for those on the next run.
    todo = [u for u in sorted(urls)
            if u not in done or done[u].get("status") == "throttled"]
    if "--redo-throttled" in argv:
        keep = {u: r for u, r in done.items() if r.get("status") != "throttled"}
        with open(OUT, "w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=["url", "records", "status", "served", "detail"])
            writer.writeheader()
            writer.writerows(keep.values())
        done = keep
    print(f"{len(urls)} distinct archive URLs cited across all records")
    print(f"{len(done)} already verified · {len(todo)} to go · {delay}s spacing\n")

    # Rows are MERGED by URL, never appended blindly. A re-run of the throttled
    # rows appended a second row for each instead of replacing it, and the file
    # went to 607 rows for 511 URLs — every summary computed from it double-counted
    # until the duplicates were noticed. Same family as reading one storage shape:
    # a tool quietly producing a number nobody can reconcile.
    merged = dict(done)
    new = not os.path.exists(OUT)
    with open(OUT, "a", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["url", "records", "status", "served", "detail"])
        if new:
            writer.writeheader()
        for i, url in enumerate(todo, 1):
            status, served, detail = check(url)
            writer.writerow({
                "url": url,
                "records": "; ".join(f"{p}/{s}" for p, s in urls[url]),
                "status": status, "served": served, "detail": detail,
            })
            handle.flush()
            merged[url] = {"url": url, "records": "; ".join(f"{p}/{s}" for p, s in urls[url]),
                           "status": status, "served": served, "detail": detail}
            if status != "ok":
                print(f"  [{i}/{len(todo)}] {status.upper()}  {url[:110]}\n        {detail}")
            elif i % 25 == 0:
                print(f"  [{i}/{len(todo)}] ok so far")
            time.sleep(delay)

    with open(OUT, "w", newline="") as handle:      # rewrite deduplicated
        writer = csv.DictWriter(handle, fieldnames=["url", "records", "status", "served", "detail"])
        writer.writeheader()
        writer.writerows(merged.values())

    print("\ndone — run with --report for the summary")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
