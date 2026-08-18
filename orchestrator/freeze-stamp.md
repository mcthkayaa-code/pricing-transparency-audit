# Freeze stamp — Pricing Transparency Audit, wave 1

**Generated 2026-08-18 by `tools/freeze_stamp.py`. Every figure below is read from the files it describes, not typed.**

Generated against commit **`e37290f21bcb`** — necessarily the commit *before* this stamp is itself committed. A reader verifying the hashes should check out that commit, or accept that this file is the only difference.

## What freezing means

**After this stamp, a correction to the dataset is a published erratum and not an edit.** The records, the coded values, the attributions and the index scores stop moving. Anything found later is recorded in `orchestrator/deviations-log.md` and carried into the paper as a correction with its date, in the open.

This is not a claim that the dataset is free of error. 79 deviations say otherwise, several of them retracting a claim this study had already made. It is a claim that **error found after this point is disclosed rather than absorbed.** (That count is interpolated, not typed: this sentence read 'Seventy-six' beside a table printing 77 until the preprint draft caught it — a typed figure going stale inside the one document that must not be wrong about its own contents.)

## The frame

| | count |
|---|---|
| pass-1 records (the frame) | **76** |
| blind pass-2 records (reliability sample) | 26 |
| adjudicated records (publish where they exist) | 29 |
| for-cause second codings (reported separately) | 3 |
| quarantined pass-2 records (never publish) | 5 |
| coded values in the published dataset | **2,812** |
| deviations logged | **79** |

## Unknowns, all attributed

| kind | count | share of unknowns on publishing rows |
|---|---|---|
| vendor_silence | 283 | 84.0% |
| instrument_gap | 48 | 14.2% |
| access_failure | 4 | 1.2% |
| unattributable_weak_basis | 2 | 0.6% |
| **total** | **337** | of 2,812 coded values |

**0 unknowns carry no attribution kind.**

## Provenance

| verdict | count |
|---|---|
| ok | 469 |
| redirect | 20 |
| ok_nearest | 13 |
| excluded | 13 |
| missing | 1 |
| **total cited captures** | **516** |

**482 of 516 resolve (93.4%). 0 unanswered.**

## The index

**72 products scored. Median 80.25, range 26.9–93.0.**

The median is printed to two decimals deliberately. It falls **exactly on a rounding boundary** — the 36th and 37th of 72 scores are 80.0 and 80.5 — so round-half-even prints 80.2 and round-half-up prints 80.3, and two of this study's own artifacts did each. Neither is wrong and the disagreement is not about the data; printing 80.25 removes it.

Distribution, component breakdown and what the index does and does not discriminate: `analysis-first-findings.md`.

## Bytes

SHA-256, so a reader can verify the copy they hold is the copy that was frozen.

| sha256 (first 16) | bytes | file |
|---|---|---|
| `f142b920ae7220b1` | 67,750 | `dataset/coded-values.csv` |
| `82d3ee5b9be4fbc6` | 1,170,324 | `dataset/coded-long.csv` |
| `f21ff60dbc5951aa` | 28,923 | `dataset/apti-scores.csv` |
| `8f1eb03bb077b846` | 34,748 | `dataset/apti-report.md` |
| `a0885a78a9f01092` | 2,144 | `dataset/build-report.md` |
| `9b9697de6d6bb6ce` | 25,118 | `dataset/data-dictionary.md` |
| `ccce856078b8bf3b` | 73,469 | `orchestrator/archive-verification.csv` |
| `f6938485519d8608` | 329,810 | `orchestrator/unknown-attribution.csv` |
| `f2c0ef57f0729165` | 111,749 | `orchestrator/unknown-attribution-overrides.csv` |
| `9221202c6ac67f19` | 79,933 | `codebook-v1.md` |
| `58bc478785841506` | 72,876 | `protocol-v1.md` |
| `5776d662f9f3f2ea` | 20,028 | `sampling-rules.md` |
| `89eccbc6b2634d4d` | 22,319 | `limitations-register.md` |
| `116b5d1b8cd894f1` | 14,988 | `methods-who-coded.md` |
| `510651fc3f019349` | 12,207 | `analysis-first-findings.md` |

### Hashed, but not frozen

**A hash below is true when printed and is expected to stop being true.** These documents are meant to keep growing, so a mismatch here is growth and not tampering — check them against the repository, not against this stamp. Every artifact in the table above is frozen and a mismatch there *is* a defect.

| sha256 (first 16) | bytes | file | why it moves |
|---|---|---|---|
| `add1a1d1409da8bc` | 24,344 | `methods-tooling-failure-modes.md` | gains a mode whenever this study's own tooling is caught failing |

## What this stamp does NOT cover

**Owner sign-off: SIGNED 2026-08-18 by Mucahit Kaya**, founder and editor — the named human in this study's AI-assistance framing, who set the question before any data existed and reviewed the frozen dataset before signing. Freezing stopped the data moving; publishing was his decision and he made it.

**One provenance defect, reported and deliberately not fixed** (D-076): a record pairing an access date with an archive URL stamped five days earlier, on the far side of a demonstrated edit to that page. Coded values survive in both captures. No record was edited by the orchestrator on freeze day and that invariant was kept in preference to the correction; it is an owner decision.

**Wave-2 items are not blockers and are listed as such** in `orchestrator/pre-freeze-checklist.md`: a fourth attribution kind for withdrawn-before-window documents, a codebook slot for a one-time credit grant, a class of official vendor page the location variables do not cover, and a checker that diffs the limitations register's prose against the tools.
