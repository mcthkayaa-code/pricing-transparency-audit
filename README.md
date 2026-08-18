# Pricing Transparency and Subscription Friction in Consumer AI Products

**A cross-sectional documentation audit of 76 products across 15 categories. Wave 1. Dataset frozen
2026-08-17.**

76 consumer AI products were coded against a **pre-registered 37-variable instrument**, inside one
collection window, **from official vendor documents only**. No product was used, trialled, purchased or
operated at any point. This is an audit of what vendors publish, not a review of what they do.

## Read this before you use a number

**Start with [`limitations-register.md`](limitations-register.md).** It lists ten limitations, each with
the figure that established it. A number taken from here without it will be over-read. In particular:

- **The frame is a census of one publication's editorial coverage, not a sample.** No confidence
  intervals, no significance tests, and nothing here supports a sentence beginning "AI vendors
  generally". It describes these 76 products.
- **The coding was AI-assisted under named human editorial control.** Every record was coded by a
  language model operating as an agent; no human read a vendor's pricing page and coded a variable; a
  named human editor set the questions, ruled on the corrections and approved the frozen result. What
  that does to the reliability figure is set out in [`methods-who-coded.md`](methods-who-coded.md).
- **α = 0.811 is reported as instrument consistency under independent double reading, never as
  inter-coder reliability.** Two automated readings of the same input can fail identically, agree, and
  raise the statistic without raising accuracy.
- **14.2% of `unknown` values are our instrument, not vendor opacity** — cases where the vendor
  documented something our codebook had no slot for. The register names them.

## The finding

**These vendors disclose what a buyer needs in order to sign up, and not what a buyer needs in order to
budget.**

| what a buyer needs to sign up | published by |
|---|---|
| a headline price | 67 of 72 |
| the annual-billing condition | 45 of 46 |
| a refund position | 68 of 72 |
| a cancellation route | 68 of 72 |

| what a buyer needs to budget | published by |
|---|---|
| whether a **failed** generation is charged for | **7 of 64** |
| the credit-to-output rate, in full | 20 of 48 |
| a determinable watermark position | 25 of 63 |

**57 of the 64 products with a metered generation step do not document whether you are charged when a
generation fails.** That is the sharpest single fact in the dataset.

The contrast was reached twice by independent routes — the per-variable consistency analysis found it
first, and the pre-registered index reaches it again from the coded values. Full reading:
[`analysis-first-findings.md`](analysis-first-findings.md) and [`paper-draft.md`](paper-draft.md).

## What is in here

| path | what it is |
|---|---|
| `dataset/coded-values.csv` | 76 rows × 37 variables, one row per product. **Start here.** |
| `dataset/coded-long.csv` | 2,812 rows, one per coded value, each with its evidence and `unknown_kind` |
| `dataset/apti-scores.csv` | the index, its components, every item, and both sensitivity analyses |
| `dataset/data-dictionary.md` | every column and every allowed value |
| `protocol-v1.md` · `sampling-rules.md` · `codebook-v1.md` | the instruments, **published before the window opened** |
| `records/pass1/` | the 76 primary records, with per-value evidence and sources |
| `records/pass2/` | 26 blind second codings — the reliability sample. **These never publish into the dataset** |
| `records/adjudicated/` | 29 third readings; where one exists it is the row that publishes |
| `records/for-cause/` | 3 second codings prompted by a problem, reported **separately** from the pre-registered 26 |
| `*-sources/` | verbatim vendor captures. For 159 coded values this is the only surviving evidence |
| `orchestrator/` | the audit trail: 78 dated deviations, the adjudication queue, the reliability computation, the archive verification, the freeze stamp |
| `tools/` | every script. The dataset regenerates from the records with `python3 tools/build_dataset.py` |

## Reproducing it

```
python3 tools/build_dataset.py      # records -> dataset/*.csv
python3 tools/score_apti.py         # dataset -> apti-scores.csv, apti-report.md
python3 tools/validate_records.py   # structural check, fails loudly on zero records
python3 tools/agreement.py          # the reliability figures
```

Standard library only, no dependencies beyond PyYAML. `orchestrator/freeze-stamp.md` carries a SHA-256
for every published artifact, so you can verify the copy you hold is the copy that was frozen.

## The part that may be most useful if you don't care about pricing

[`methods-tooling-failure-modes.md`](methods-tooling-failure-modes.md) documents **33 ways a
documents-only audit of live web pages goes wrong.** Every one happened here, was caught, and is dated
in the log — a rendered figure that is not the figure in the markup, an archive that answers HTTP 200
with an empty body, a decompressor that fails into noise a price regex then mines a number out of.
Almost none of them looks like an error while it is happening. They look like findings.

## Status and licence

**This is a preprint dataset. It has not been peer reviewed.** The paper is a draft.

Corrections after the freeze are published errata rather than silent edits, and go into
`orchestrator/deviations-log.md` with their date. If you find something wrong, that is the outcome this
release is built for — please open an issue.

Licensing is split and [`LICENSE.md`](LICENSE.md) explains why: **everything this study produced is CC
BY 4.0**, and the saved vendor captures are the vendors' copyright and are included as evidence, not
redistributed content.
