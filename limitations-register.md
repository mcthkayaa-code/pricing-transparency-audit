# Limitations register

**Compiled 2026-08-17 and refreshed against the tools at freeze time. Every figure here is computed
from the frozen records by a tool in `tools/`, and every claim names the deviation that established
it.**

**How that promise is actually kept, stated so a reader can judge it:** the figures are *derived* by
the tools and *typed* into this prose by hand, so between a data change and a refresh they can go
stale. They did, three times in one day, and each was caught by re-deriving rather than by reading.
Every figure below was re-derived from `tools/agreement.py`, `tools/attribute_unknowns.py`,
`tools/build_dataset.py` and `orchestrator/archive-verification.csv` immediately before the freeze
stamp, and the freeze is what stops them moving. A checker that diffs this prose against the tools
is a wave-2 item; until it exists, the refresh is a checklist step and is named as one.

This is not a softening appendix. It is the list of things a reader should know before using any number
in this study, ordered by how much they should change what the reader concludes.

---

## 1. The frame is a census of one publication's coverage, not a sample of anything

`sampling-rules.md` §2.2 and §2.3, fixed before collection. **76 products, complete enumeration, no
random selection, no sampling error, and no inference to any wider population.** Confidence intervals
and significance tests presuppose a sampling process that does not exist here, and the primary analysis
uses none.

**And the frame is not neutral.** It reflects roughly two years of editorial coverage choices that
favoured categories with high buyer intent and available affiliate programs, so those categories are
over-represented relative to any plausible population of AI products. Stated here and in the paper, not
buried.

**What that means for a reader:** every result describes these 76 products. Nothing here supports a
sentence beginning "AI vendors generally…".

## 2. AI-assisted under named human editorial control — and what that means for the consistency figure

Full treatment in `methods-who-coded.md`. In short: **every record was coded by an LLM agent** — 76
pass-1 agents, 26 blind pass-2 agents, 29 adjudicators, and an orchestrator whose own errors are a
substantial share of the deviations log. No human read a vendor's pricing page and coded a variable.

So **α = 0.811 is reported as instrument consistency under independent double reading**, and never as
inter-coder reliability. The conventional label assumes two readers whose errors are largely
uncorrelated — true of two people with different training and blind spots. Two automated readings of
the same input can fail identically, agree, and raise the statistic without raising accuracy. The figure
establishes that the instrument is applied **consistently**, not that it is applied **correctly**, and
every use of it in the paper is scoped to the narrower claim.

**One direct check exists.** Of 145 disputed variables sent to a third reading, it picked pass 1 in
44.1%, pass 2 in 40.0%, and neither in 15.9% — and that last figure decomposes into 13 values on one
product whose sampling rule is underdetermined, 6 completeness merges, and **4 genuine reversals: 3.0%
of the 132 excluding that product.** So when two model readings disagree, a third rarely finds a third
answer.

**What that check cannot see** is both readers being wrong together, and the study has direct evidence
it happens: three coders independently took the same wrong carve-out reading (D-046), and a classifier
the orchestrator wrote made 50 errors of which **49 ran toward the study's own headline** (D-048).

**The most valuable robustness check this study lacks is a human coding ten products against the same
codebook.** It would bound the correlated-error term directly. Recommended as wave 2's first addition.

## 3. Reliability is weaker per variable than the pooled figure suggests

| | value |
|---|---|
| pooled α, all 26 double-coded products | **0.811** |
| **median per-variable α** | **0.770** |
| variables reaching α ≥ 0.800 | **17 of 37** |

Pooling 37 heterogeneous variables into one coincidence matrix inflates α, and the reliability write-up
says so with the arithmetic. **The per-variable table is the honest one and the paper prints it beside
the headline.**

The weakest constructs are not the prices. Vendors are legible about price — `headline_price_usd`
reaches 0.920 — and illegible about **entitlement**: whether a cap is quantified, what a free tier's
real limit is, whether cost per output can be computed at all. That contrast is the study's central
finding and it survived a correction that withdrew an earlier, opposite claim (D-021).

## 4. 14% of unknowns are our instrument, not vendor opacity — and 1% are documents we could not reach

| kind | on the 76 **publishing rows** | across **all records** |
|---|---|---|
| vendor silence | 283 of 337 (**84.0%**) | 492 of 581 (84.7%) |
| **instrument gap** | **48 of 337 (14.2%)** | 70 of 581 (12.0%) |
| access failure | **4 of 337 (1.2%)** | 15 of 581 (2.6%) |
| unattributable on the record's own evidence | 2 of 337 (0.6%) | 4 of 581 (0.7%) |

**Every one of the 581 unknowns is attributed, 221 of them by hand with a written reason a reader can
check.** The publishing-row column is the one that governs any figure a reader uses; the all-records
column includes the blind second pass, which never publishes.

**The 14.2% is the largest single correction this study makes against its own headline.** A vendor that
publishes a quarterly billing cadence and receives `unknown` because the value list has no quarterly
value has disclosed fully; scoring it as opaque measures us. The affected records are named in
`orchestrator/A-009-A-011-A-016-A-017-resolution.md`.

**The access-failure figure moved further than anything else in this study, and the path matters more
than the endpoint.** It was 2.9% when this section was first written and it is 1.2% now. Not one value
was reclassified to flatter the study: **three retrieval sweeps went back to the documents**, and across
them **59 of 60 values held as `access_failure` proved retrievable** (47 of 47, then 12 of 13). Each
reduction came from a document being fetched and read, and each reclassification ran through
`vendor_silence` or `instrument_gap` on stated evidence, recorded in
`orchestrator/unknown-attribution-overrides.csv` with a basis per row.

**What survives as `access_failure` is four values, and they are the honest residue.** One product's
captures can never be window-dated — twelve captures, all browser-upgrade shells, no Common Crawl
record, no date stamp. Another is the cleanest instrument miss in the corpus: a capture dated
2025-09-17, comfortably pre-window, already carrying the sentence that answers the variable. The
document was reachable throughout and our procedure did not reach it. **`access_failure` has described
our reading of a document far more often than our reach to one**, and the paper reports it with that
denominator rather than as a bare percentage.

**This section previously read "the index must not score an `instrument_gap` unknown as
non-disclosure." That was a requirement the pre-registered instrument does not implement, and the
sentence is corrected here rather than left standing.** Protocol §8.3 scores an `unknown` item as zero
and says nothing about attribution kinds — which is correct, because those kinds were assigned *after*
collection, partly by a classifier. Re-weighting a frozen index using post-hoc attributions is what
pre-registration exists to prevent, so the scorer follows the protocol and the primary index does
score an `instrument_gap` unknown as zero.

**What honours the concern is sensitivity analysis S2**, pre-registered in §8.4, which removes
`unknown` items from numerator and denominator alike. Published beside the primary: **median 88.2
against 80.2, and a minimum of 67.4 against 26.9. Eight points of median is what this study's stance on
`unknown` costs a vendor**, and a reader can see it per product in `dataset/apti-scores.csv`.

**One product defeats even that, and it is named.** `google-veo` carries 20 of the corpus's 46
`instrument_gap` unknowns, scores 26.9 — the minimum, and the sole occupant of the lowest band — and
its S2 value is **suppressed**, because rule S2.2 re-applies the availability guard to the shrunken
denominator and 13 removed items put it below the threshold. So the product whose score is most
distorted by our treatment of `unknown` is the one where the analysis meant to reveal that distortion
cannot be computed. **Its 26.9 is not a finding about that vendor**, and `analysis-first-findings.md`
§3a states what may and may not be said with it.

**And that figure was 11.6% before an audit and 20.7% after it, before settling at 13%** as two
retrieval sweeps moved values back. The path is in D-048, D-050 and D-051; the point is that the number
moved a long way under scrutiny and could move again.

## 5. Provenance: 93% of citations resolve exactly, and nothing is left unanswered

Every cited archive capture was verified individually — three sweeps during the study (D-047), and a
fourth on the closing day once the service came back (D-073).

| | count |
|---|---|
| **exact cited capture served** | **469 of 516 (90.9%)** |
| nearest capture, same day | 13 |
| cited capture does not exist (service served another date) | 20 |
| archive withholds the whole host (403) | 13 |
| no capture at all (404) | 1 |
| **service would not answer** | **0** |

**482 of 516 citations resolve** (90.9% exact, 93.4% including same-day nearest). **The figure was
377 of 511 (73.8%) until the closing day**, and the difference is not new archiving — it is that
**92 citations the service had refused across three sweeps were re-asked once it recovered, and every
one of them answered.** 92 became `ok`; none turned out to be missing. The earlier number was a
measurement of an outage, published with that caveat attached, and it is now replaced by a
measurement of the archive.

The denominator grew from 511 to 516 because three products received a third reading in the closing
days and their adjudicated records cite five further captures.

**The 20 non-existent citations are the real residue, and they were traced rather than counted.** A
citation the service answers by serving a *different* date is not reproducible provenance (see §5b).
Nineteen of the twenty sit on pass-2 or superseded records that do not publish. **One touches a
publishing row** — a product whose `headline_price_usd` and `free_plan_cap_value` cite a timestamp
four days after the window that has no capture behind it.

**Both of its values were verified against the capture the service actually serves**, which is dated
*inside* the collection window: the free-plan allowance appears verbatim ("3 downloads per month"),
and the `non_usd` coding is correct because the page prices in EUR with no dollar figure anywhere.
So the defect is the cited timestamp, not the value or its evidence. **No publishing-row value in
this dataset rests on a capture a reader cannot open.**

**The last two rows read `14` and `0` until 2026-08-17.** The verifier classified any unrecognised HTTP
status as `missing`, so a 403 — the archive refusing to serve a *host* — was recorded as a statement
that no capture exists. Thirteen of the fourteen were 403s, and the tool's own `detail` column had said
`HTTP 403` beside every one of them from the first sweep. **The study's genuine archival absence is one
citation out of 511.** Corrected in D-069, from the recorded status codes rather than by re-asking the
service, and the verifier now carries `excluded` and `unclassified` outcomes so nothing lands in
`missing` again by default.

Twelve of the thirteen belong to **one vendor whose entire domain the archive refuses to serve** — a
403 on every URL form tried, while four other vendors' domains returned 200 in the same run, and with
nothing in that vendor's own `robots.txt` asking archivers to stay out. **That is a finding about the
vendor rather than a limitation of this study:** its published pricing documents cannot be
independently re-examined at any past date by anyone outside the archive. The thirteenth is a
video-share host that refuses archiving of user content. Both are noted in the dataset rather than
scored, because the index measures what a vendor discloses and not whether third parties may keep a
copy — a distinction worth revisiting in wave 2, since a claim nobody can check later is a weaker
disclosure than one they can.

**A capture that does not resolve exactly is not reproducible provenance.** The service resolves an
inexact citation to whatever is nearest at request time, and this study watched one such citation
resolve to a different date two days apart. So the 13 "nearest capture" rows are reported separately
rather than folded into the clean count.

**`archive_status` is wrong on 14 of 76 rows, and 12 of those understate our own provenance**
(D-061). The field records what a coder's save request appeared to return, not whether a capture
exists — and on five records a capture dated the collection day resolves today, so the failure note
was wrong when written rather than stale. The dataset therefore carries three COMPUTED columns
(`archive_status_verified`, `resolving_captures`, `local_source_files`) beside the coded field, which
is left exactly as written. Verified split: **68 archived, 7 local-copy-only, 1 with neither.**
Coded split, for comparison: 57 archived, 19 `local_copy_only`. **Four** records keep no local mirror at all — corrected from eighteen under D-063, which is why **the dataset release must ship the `-sources/` directories** —
for 159 coded values the local capture is the only surviving evidence (D-037).

### 5a. Every publishing row has re-examinable evidence — a retracted finding

An earlier version of this register said one row had **none**: that its `archive_status` claimed a
local copy, that it named seven local files, and that none existed. **That was wrong and is
retracted (D-063).** All seven exist, at the study root rather than under `records/pass1/`, and the
check that reported them missing globbed one of three possible locations.

Corrected, corpus-wide: **every one of the 76 publishing rows has either a resolving capture or a
local file.** 51 have both, 17 have a resolving capture only, 8 have local files only, **0 have
neither.** Four records keep no local mirror — three have no source directory and one has an empty
one — and all four have resolving captures.

It is stated here rather than quietly fixed because the error ran **against** this study: it
accused our own record-keeping of a failure that had not happened, and an unearned confession is as
false as an unearned defence. It was caught by the public-export tool refusing to copy files it had
no rule for.

### 5b. One record's `archive_status` is simply wrong

**`shortsfaceless`** is marked `local_copy_only` while carrying three archive captures that all verify
`ok`. Its archives resolve; the status understates its own provenance. Corrected in the record's prose
rather than silently, and noted because it is the mirror image of 5a: a status that claims less than the
record can support, where the other claims more.

## 6. One geographic vantage point

Currency is served by inferred geography and no locale path, URL parameter or request header overrides
it. **Every reader in this study sat in one country**, so for three records a money variable is
`unknown` or `instrument_gap` because a USD figure was not obtainable from here (D-056).

**One of the original four turned out not to be a vantage-point problem at all.** A US-served Common
Crawl capture — that crawler runs on US infrastructure — was fetched and contains **none** of the plan
content: that vendor's price is absent from served HTML from any geography, because it is rendered at
runtime (D-057). That is a **class of vendor whose price is unarchivable in principle**, determinable
only by a rendered read, and it extends A-017's finding about client-side A/B variants to client-side
price rendering generally.

**Wave 2 must give the protocol an executable route for a US-denominated read** rather than a test with
no route, and should add Common Crawl as a standard second vantage point.

## 7. The protocol cannot classify the variance it can demonstrate

Protocol §7.4.2 admits `variant_explained` only on two archive snapshots. **An archive can never capture
a client-side A/B variant, because the archive does not execute the experiment script.** So this study
can show that a vendor's price was under live experiment — both arms sit in the page's own markup — and
simultaneously cannot classify the resulting inter-coder disagreement as display variance under its own
rule (A-017).

The bar was held rather than lowered: the adjudicator that met this fetched both passes' archives through
the raw endpoint, took a fresh third capture, found all three identical, and resolved the disagreement as
an ordinary one. **Both facts belong in the record, because the gap between them would otherwise read as
an oversight.**

**And on one product the experiment machinery was found outright.** A second-pass coder identified a
cookie-consent-gated A/B test on a pricing page (`pricing-ab.js`), established that **declining analytics
cookies deterministically serves the control arm**, then fetched the treatment fragment and confirmed
both arms carry identical headline price, billing basis and credit allowances. **Nothing coded on that
product is affected**, and the coder's privacy-preserving consent choice happens to be the reproducible
one.

The methodological point survives the null result, and it is sharper than §7's opening: where a vendor
A/B-tests its pricing page, **"the default display state" is not a single fact about the vendor at all**
— it is a fact about which arm the reader was assigned. Protocol §6.8 tells a coder to record the state
they observed, which is the right instruction and is what makes the record honest. But this study found
the test only because **one coder noticed a script**, and a design that depends on that has no idea how
many other products were under experiment. Wave 2 should test for the machinery explicitly rather than
hope a coder spots it.

**Neither the number of products under live pricing experiment during the window, nor the direction such
experiments push a transparency score, is knowable from this dataset.**

## 8. A format rule was breached corpus-wide and not repaired

`computation_assumptions` carries a 300-character cap stated twice in the codebook. **37 of the 115
values that carry content exceed it, 32%, the longest at 1,240 characters** (D-045).

Not truncated, deliberately: the overruns are arithmetic derivations with source citations — the
reproducibility the field exists for — and shortening evidence until a format rule passes destroys what
the rule is meant to make usable. **It is non-compliance with a pre-registered format rule, disclosed
rather than repaired**, and the honest reading is that the rule was wrong for a field that turned out to
be documentation: the same field is reported at **α = −0.001** and is slated for reclassification.

## 9. The blindness record

Six blindness breaches, all six self-disclosed by the agent that committed them, plus three for-cause
blind second codings **reported separately from the pre-registered set** so the planned statistics stay
uncontaminated (D-001, D-004, D-011).

**All three were promised on 2026-08-06/07/12 and carried out on 2026-08-17, eleven days late.** Their
agreement, never pooled with the 26: **63.9% / 75.0% / 83.3%, pooled 74.1% at α 0.720**, against the
corpus's 82.2% / α 0.811. `methods-who-coded.md` publishes that comparison **with its decomposition**,
because bare it misleads in both directions — one of the three is above the corpus, and the low one
resolves into one underdetermined codebook question, one first-reading over-read, and one
orchestrator briefing defect. All three went to adjudication and all three adjudications changed the
published record.

Two structural exposures were found and measured rather than assumed away: required reading that named
13 of 26 double-coded products with their values (D-014), and the repository's own git history, which
names all 26 (D-017). **If exposure had inflated agreement, exposed products would agree more. They do
not** — the five products never named anywhere a coder reads score **highest** at α 0.823, above the
pooled 0.811. That is evidence, not proof: five products and 185 units cannot carry a robustness claim
alone, and the paper says so.

## 10. Every deviation is logged, including retracted claims

**The count is deliberately not printed in this heading.** It read 58, then 71, then 76, then 77 in
the space of a day, and each stale value was found by re-deriving rather than by reading — the
seventh instance of that defect (D-079). The live figure is computed by `tools/freeze_stamp.py` and
printed in `orchestrator/freeze-stamp.md`; `grep -cE "^## D-" orchestrator/deviations-log.md`
returns it in one command. A number that moves every time the study learns something does not belong
in hand-typed prose.

`orchestrator/deviations-log.md`. Every one dated, with what it changed and in which direction.
**Three withdrew a claim the study had already made**, including one headline finding about price
disagreement that turned out to be a float-formatting artifact (D-021), kept struck through rather than
deleted.

The orchestrator's own errors are a large share: **six** confidently wrong numbers produced by reading
one storage shape or one location where several existed, three records broken by line surgery on YAML,
two commits that swept another agent's work in, and one doctrine ruling reversed after an audit it had
itself commissioned
argued it out of the position.

**That list is the study's actual warrant.** Not that it did not err — it erred constantly — but that
the errors are recoverable from the record, and a reader can check any value against the evidence
recorded beside it.
