# I spent 4.1 billion tokens to investigate 76 AI platforms. They publish what they're selling — not what you're buying.

*A cross-sectional documentation audit of pricing transparency and subscription friction in consumer AI. 76 products, 15 categories, one pre-registered instrument, vendor documents only.*

**Wave 1. Collection window 2026-08-04 to 2026-08-17. Dataset frozen 2026-08-17.**

**Author and responsible human:** Mucahit Kaya, Founder and Editor, AI Tools Police.
**Study type:** Cross-sectional documentation audit of public vendor materials. Observational. No intervention, no human subjects, no personal data.
**Pre-registration:** `protocol-v1.md` v1.2, dated 2026-08-03, published before the window opened. Companion instruments: `sampling-rules.md`, `codebook-v1.md`.
**Status:** Preprint draft. Not peer reviewed.

---

## Abstract
A buyer of a consumer AI product must decide before paying. This study asks whether the vendor's own
public documents let her. Every product carrying a published AI Tools Police investigation at the frame
freeze — **76 products across 15 categories** — was coded against a pre-registered 37-variable instrument
inside one collection window, from official vendor documents only. **No product was used, trialled,
purchased or operated at any point.** The coding was AI-assisted under named human editorial control: no
human read a vendor's pricing page and coded a variable, and a named human editor set the questions,
ruled on the corrections and approved the frozen result.

**The central result is a contrast, not a level: these vendors disclose what a buyer needs in order to
sign up, and not what a buyer needs in order to budget.** A headline price is published by 67 of 72
applicable products, a refund position by 68 of 72, a cancellation route by 68 of 72. Against them,
**57 of the 64 products with a metered generation step do not document whether the buyer is charged when
a generation fails**, and the credit-to-output rate — the number that decides whether a published price
means anything — is published in full by 20 of 48. The contrast was reached twice by independent routes:
the per-variable consistency analysis found it first, in the gap between `headline_price_usd` (α 0.920)
and the entitlement variables (α 0.249 to 0.493), and the pre-registered index reaches it again from the
coded values rather than from coder agreement.

The AI Pricing Transparency Index, fixed before any datum existed, was computed for 72 of the 73 active
products: median **80.25**, range 26.9 to 93.0. **It measures level adequately and ranks poorly** — the
middle half sits inside about 16.6 points — so within that range it yields a band and not a ranking, and
this paper publishes no league table of the middle. Instrument consistency under independent double
reading was α 0.811, reported under that name and never as inter-coder reliability, because two automated
readings of the same input can fail identically, agree, and raise the statistic without raising accuracy.

**The frame is a census of one publication's editorial coverage, not a sample**: no confidence intervals,
no significance tests, and no sentence beginning "AI vendors generally". The study also publishes its
dated deviations, a blindness record of six self-disclosed breaches, and a companion note documenting
**33 ways a documents-only audit of live web pages goes wrong** — every one of which happened here.

---

## 1. Introduction

The question is narrow and it is the whole study: **can a prospective buyer determine an AI product's true
cost and subscription terms before paying, using only the vendor's public materials?**

It is a question about documents, which is why the documents are the data. A study that used the products
would answer a different question, and this publication runs no hands-on trials in any of its work. That is
a design choice stated at the front, not a shortfall admitted at the back.

Two features of consumer AI pricing make the question worth asking now. The first is **metering**. Many of
these products bill in an internal currency — credits, tokens, generations, minutes — whose exchange rate
into output is a separate disclosure from the price. A published $20 per month is not a price if the buyer
cannot say what $20 buys. The second is **failure**. Generative systems fail: a render errors, a clone is
rejected, a job dies halfway. Whether the meter runs during a failure is a term with direct financial
consequence and no natural home on a pricing page.

The study measures **determinability**, not generosity. A vendor stating "no refunds under any
circumstances" earns exactly the points a vendor stating a 30-day unconditional refund earns, because both
readers know what they are buying. The index carries the qualifier in its own name — a determinability
index — because a name containing the word "transparency" invites the opposite reading.

The headline result is a contrast between two kinds of disclosure that sit in the same documents and behave
completely differently. The terms a buyer needs **to become a customer** — price, annual condition, refund
position, exit route — are published by almost everybody here. The terms she needs **to forecast a bill** —
credit rate, rollover policy, failure-charge rule, the qualifying clause on an advertised allowance — are
frequently absent.

This paper also carries an unusual amount of material about its own errors: 79 dated deviations, three of
which retract a claim the study had already made in public, and a methods note documenting 33 tooling
failure modes that all occurred here. This is ordinary practice for an audit of live web documents, not a
confession. **A tool that reads less than it claims produces a number nobody can distinguish from a
result**, and the only defence is publishing what the tools did.

---

## 2. Prior work

This section is short and it is **not a literature review**. No systematic search was run and the study
claims no coverage of the field; what follows names the traditions this work sits beside.

Three literatures are adjacent. **Shrouded attributes and add-on pricing** in behavioural industrial
organisation formalise the case where a firm advertises a base price and leaves a required complement
undisclosed until the buyer is committed, with the result that competition need not force disclosure,
because a firm that unshrouds educates its rival's customers as well as its own. **Drip-pricing** research,
largely from consumer-protection regulators, measures the same shape empirically in airline, ticketing and
hospitality checkouts. **Dark-pattern measurement** work, which built large automated corpora of shopping
and subscription interfaces, contributed the methodological move this study depends on: treat document text
as data, code it against a fixed instrument, report prevalence rather than anecdote. Regulatory attention
to negative-option marketing and cancellation friction runs alongside all three.

What none of that covers is the object measured here. Metered generative pricing introduces a disclosure
with no analogue in an airline fee: the exchange rate between the vendor's internal currency and the
buyer's output, plus the treatment of a failed unit of work. A drip-pricing study asks whether the total
appears before checkout; this one asks whether the total is computable at all. Two boundaries follow. The
frame is a census of one publication's coverage, not a market sample, so nothing here supports a prevalence
claim about AI products at large. And this study measures documents, never outcomes: a documented refund
policy is coded as documented and never as honoured.

---

## 3. Method

### 3.1 Design and window

A cross-sectional documentation audit: one collection window, every product in the frozen frame coded
inside it, one standard instrument applied to all of them. Pricing pages change continuously, so a single
dated snapshot per product is the only honest unit of observation. The publication's own existing
investigations were **not** reused as study data and served only as a discovery aid for locating a vendor's
documents. Coded values carry collection dates from 2026-08-06 to 2026-08-17; the window opened at the
frame freeze on 2026-08-04 and closed when the final-day re-check completed on 2026-08-17, at the
protocol's stated 14-day maximum. The design answers no causal question and every planned statistic is
descriptive.

A final-day sweep tested whether any vendor materially changed a coded page inside the window. **No
headline price and no tier name changed on any testable page, and no coded value moves.** Four vendor edits
were found, all leaving the coded values intact. The honest denominator is reported with the result: only
42 of 76 pricing pages have two or more in-window captures and can be tested at all, and of those 42 only
28 span 24 hours or more — one tested pair sits 33 seconds apart, which has not been tested for change over
a seven-day window and is not counted as covered.

### 3.2 The frame: a census, not a sample

The frame is every product with a published AI Tools Police investigation live when the frame was frozen —
**76 products across 15 categories**, frozen 2026-08-04 and confirmed by the responsible human before
coding started. Every product in the frame is coded: no random selection, no sampling fraction, no sampling
error. Two consequences bind every sentence in this paper — **no inference to a wider population**, and **no
inferential statistics**, because confidence intervals and significance tests presuppose a sampling process
that does not exist here.

**And the frame is not neutral.** It reflects roughly two years of editorial coverage choices favouring
categories where buyer intent runs high and where affiliate programs exist, so those categories are
over-represented relative to any plausible population of AI products. Category sizes run from 1 to 9, which
rules out cross-category inferential comparison outright.

| Category | Products | Active | | Category | Products | Active |
|---|---|---|---|---|---|---|
| AI image generator | 9 | 9 | | AI music generator | 5 | 5 |
| AI website builder | 7 | 7 | | AI voice | 5 | 3 |
| AI bot checker | 6 | 6 | | Faceless video | 5 | 5 |
| AI detector | 6 | 6 | | AI presentation | 4 | 4 |
| AI humanizer | 6 | 6 | | AI design | 3 | 3 |
| AI resume builder | 6 | 6 | | AI data analysis | 2 | 2 |
| AI video generator | 6 | 5 | | AI headshot | 1 | 1 |
| AI avatar | 5 | 5 | | **Total** | **76** | **73** |

Three products sit in the discontinued stratum, enter no aggregate and no index under rule D8, and are
reported as a raw count under rule D3 (§4.8).

### 3.3 Instrument and the entry-tier rule

`codebook-v1.md` is the measurement instrument: 37 variables across twelve measurement domains, each with
its type, allowed values, decision rule, required evidence and a worked example. No variable could be
added, removed or redefined after the window opened.

Several variables reference the **entry paid tier**, and two readers applying that phrase loosely would
produce incomparable numbers, so it is fixed. Among plans that are generally available, purchasable without
contacting sales, standing rather than promotional, single-seat where plans scale by seat, and the smallest
published package where pricing is usage-based, the entry paid tier is the one with the **lowest
annual-equivalent cost of a single seat, computed in the pricing page's default display state**. The page
is read as it loads, the billing toggle is not switched to find a cheaper figure, a monthly figure is
multiplied by twelve, and feature sets do not enter, because this is a price rule and not a value rule.
Every eligible candidate that lost is recorded with its annual-equivalent figure. The rule proved
underdetermined for one product reached only through a large vendor's wider platform, where which
purchasable plan grants access to *this* product is genuinely contestable — an instrument limitation for
platform-embedded products, reported as one in §4.6 rather than absorbed into a reliability figure.

### 3.4 Collection procedure, and what was prohibited

Only official vendor sources are valid for coding. Pricing variables take the live pricing page first,
contractual variables the terms of service or dedicated policy page first, with documentation and help
centre second in both. Where sources of equal authority disagree the value is coded `conflicting`; where
one outranks the other the disagreement is still recorded with both URLs, because a gap between a marketing
claim and a contract is a finding rather than noise.

The documents-only rule prohibited, at every step: creating an account of any kind including a free one;
signing in; starting a checkout, building a cart or entering payment details; starting a trial; using the
product; contacting the vendor during the window; and coding any value from a third-party source. **No
checkout was opened at any point in this study, and no product was used.** The prohibition on contacting
the vendor is principled rather than pragmatic: a term a vendor explains privately by email is not a term a
buyer can determine before paying.

Reading a public page was permitted in full — scrolling, expanding an accordion, following an official
link, switching a billing toggle *after* recording the default state — with the line drawn at any action
that identifies the reader to the vendor or begins a transaction. **`unknown` is a result, not a failure**,
and coders were instructed never to close a gap by inference; absence of evidence is `unknown`, never
`not_applicable`. Every source page was snapshotted the day it was read, and no value could be coded from a
page not snapshotted that day.

### 3.5 Who coded, and what the consistency figure measures

This study is **AI-assisted research under named human editorial control**. The framing is stated here
rather than in a footnote because one of the figures it reports means something different depending on how
the coding step was carried out.

**Every record was coded by a language model operating as an agent**, under the documents-only protocol,
with tool access limited to fetching and reading public web pages, writing its own record, and running the
study's validators. **No human read a vendor's pricing page and coded a variable from it.** One agent per
product in pass 1, 76 of them, each given the product name and vendor URL and nothing from any other
record; one agent per product for the 26 pre-registered double-coded products in pass 2, each blind to
pass 1; one agent per disagreeing product for adjudication, reading both prior records and both source sets
and deciding by the codebook clause rather than by majority; and a coordinating instance that wrote the
assignments, ran the tooling and maintained the deviations log, whose own errors are a substantial fraction
of that log.

The named human editor's role was not nominal: he fixed the research question and the design before any
data existed, approved the protocol, sampling rules and codebook, ratified the frozen frame, intervened on
substance during the work, and signs off on the frozen dataset before publication. **Two of the largest
corrections in the study came from those interventions rather than from any automated step** — a challenge
that a figure was on a vendor's own page, which produced a retracted framing and a new archive route
(D-056, D-057), and a challenge to the practice of filing gaps as limitations before they had been chased,
which turned 21 claimed access failures into one (D-050).

**The reliability figure is therefore reported as instrument consistency under independent double reading,
never as inter-coder reliability.** The conventional label rests on an assumption — that two readers'
errors are largely uncorrelated — which holds for two people with different training and blind spots and is
not guaranteed of two automated readings of the same input. Two instances of one model family can fail the
same way on the same input; where they do, they agree, the statistic rises, and accuracy does not. An α
computed between them is **systematically optimistic** relative to the same figure computed between humans,
by an amount this study cannot quantify. So the claim is narrow: **α 0.811 establishes that the instrument
is applied consistently, not that it is applied correctly.** Editorial control governs what is published;
it does not change what a statistic measures, which is why the statistic was renamed rather than the
framing bent (D-064).

### 3.6 Second coding, adjudication, and the blindness record

Twenty-six products were selected for blind double coding by a deterministic published rule, at or above
the pre-registered target share of active products. Pass 2 could not read the pass-1 records and its
assignment named the product and vendor only. Where the passes disagreed, a third reading adjudicated from
the source documents rather than from the prior records, and the adjudicated row is the published row where
one exists. The dataset carries **29 adjudicated rows of 76**, and both adjudicator counts appearing in
this study's documents are true of different things: **24** came from the 26 pre-registered double-coded
products (two needed none), **3** are the for-cause codings below, and **2** are further products
adjudicated late in the window on specific evidentiary questions.

**The blindness record.** Six breaches occurred, and **all six were self-disclosed by the agent that
committed them**, unprompted, against their own interest. Three were pass-1 coders who opened a sibling
record to see what a finished one looks like (D-001, D-004, D-011). One was a pass-2 coder whose own
wildcard search over the study directory swept in a file naming its product with pass-1 figures (D-016).
Two were adjudicators who opened another product's record for formatting reference, because the rule
forbidding it offered no permitted alternative (D-031 and one further instance). In every case the fix was
a route rather than a firmer rule: a record template to answer the formatting need, relocation of every
coordinator-only artifact out of the directory a coder can glob, and an explicit list of files a coder may
open. The three products whose pass-1 coders breached received **for-cause blind second codings, reported
separately from the pre-registered 26** so that a re-read prompted by a problem could not contaminate the
planned statistic (§4.6).

**Two structural exposures were measured rather than assumed away.** The required reading list handed
pass-2 coders a document naming 13 of the 26 double-coded products alongside a coded value or status
(D-014) — the instructions handing over the answer, which is worse than a coder reaching for it. Five
records produced under the old reading list were quarantined, named, retained and re-coded from scratch,
and the pre-registered set stayed at 26 rather than being quietly reduced. The repository's own version
history names all 26 (D-017). Both are reported with their robustness check, and its weakness, in §4.6.

### 3.7 The index and its pre-registered sensitivity analyses

The **AI Pricing Transparency Index (APTI), a determinability index**, was fixed before any datum existed:
twenty items over six components, 100 points before any `not_applicable` removal.

| Component | Points | What it asks |
|---|---|---|
| A Headline price integrity | 20 | Is a price published, is the annual condition disclosed, is the first charge determinable |
| B Free tier and trial clarity | 15 | Free-tier position, free-tier restrictions, trial terms |
| C Unit-cost comprehensibility | 25 | Credit unit defined, credit-to-output rate published, cost per output computable, rollover documented, failed-generation charging documented |
| D Renewal and exit terms | 20 | Auto-renewal default and disclosure proximity, refund position, cancellation route |
| E Rights and restrictions | 10 | Commercial-use tier, watermark position, output ownership |
| F Residual undisclosed burden | 10 | Usage caps quantified, unquantified limit clause absent |

`APTI = 100 × (earned / available)`, with `not_applicable` items removed from numerator and denominator.
**Rule G1 is the study's central stance: an `unknown` item scores zero and stays in the denominator,
because an undisclosed term is the buyer's burden and not a missing observation.** A `conflicting` value
scores one third of the item. A **guard rule** withholds the index entirely where `available` falls below
50, so a score computed over a quarter of the instrument is never compared against one computed over all of
it.

Component C carries the most weight because credit metering is where a headline number and a real bill
diverge furthest, and because it is the one construct a reader cannot approximate by guessing. The weights
are a judgment made before any data existed — the only condition under which they can be honest — and they
are the one part of the instrument a referee cannot check from the data, which is why **S1**, which gives
each component an equal share regardless of its point total, was pre-registered. **S2** replaces rule G1
with "an `unknown` item is removed from numerator and denominator"; the protocol calls this **the most
favourable reading available to any vendor**. Both variants inherit every guard the primary carries; S2 in
particular **recomputes** `available` and re-applies the guard to the shrunken denominator, which lands on
the one product it most matters for (§4.9).

### 3.8 Reporting rules

Ten descriptive-reporting rules were fixed before collection. Four shape how this paper reads. **D2: every
percentage prints with its denominator, in the form "x of N"** — bare percentages appear nowhere here.
**D3: percentages are reported only for groups with n of 5 or more**, which is why several figures below
are counts where a percentage would have been easy and misleading. **D4: the median and interquartile range
lead**, with minimum and maximum, and the mean sits beside the median and never instead of it. **D10: every
index result is reported twice**, once over the full frame and once with `paid_submission = yes` records
removed. Rule D8 keeps discontinued products out of every aggregate; rule D1 shows `unknown`,
`not_applicable` and `conflicting` as their own rows rather than dropping them.

### 3.9 Seventy-nine deviations, dated, by class

`orchestrator/deviations-log.md` carries **78 numbered entries**, each dated and each stating what it
changed and in which direction. They are summarised by class with the log cited, rather than reproduced.

| Class | Examples | What the class is |
|---|---|---|
| **Retractions of the study's own claims** | D-021, D-060→D-063, D-050, D-074 | A published finding withdrawn on evidence, original wording struck through rather than deleted |
| Reading the vendor's page wrongly | D-003, D-005, D-007, D-009 | Static fetches, superscript-cents layouts, geo-served currency — each producing a corpus-wide re-read |
| **Reading our own data wrongly** | D-020, D-033, D-037, D-061, D-063 | One field or directory existing in several shapes or locations and a tool reading one. **Six occurrences, the most expensive class** |
| Checks that did not check | D-034, D-039, D-068 | Validators globbing paths that matched nothing; an entry point that never called its own logic |
| Blindness and exposure | D-001, D-004, D-011, D-013, D-014, D-016, D-017, D-031, D-032 | Six self-disclosed breaches plus two structural exposures created by our own instructions |
| Frame defects | D-002, D-008 | Wrong URLs in the frozen frame; two products carrying `active` status that were already discontinued |
| Retrievability and provenance | D-036, D-038, D-047, D-050, D-051, D-069, D-073, D-075, D-076 | Four archive sweeps and three retrieval sweeps, each moving the provenance and access-failure figures |
| Instrument gaps found by applying it | D-029, D-045, D-046, D-049, D-052, D-059, D-077 | Constructs with no codebook slot; a format rule breached corpus-wide; one test stated two ways in two documents |
| Coordination defects | D-015, D-040, D-041, D-054, D-071, D-072 | Assignments with wrong fields, manifests never on disk, briefs scoped from a report instead of a diff, commits scoped to a directory instead of to files |
| Freeze-day figure drift | D-078, D-079 | Five hand-typed figures found stale in four documents in one day, then six more found while this paper was drafted — every one caught by re-deriving rather than by reading. Two were the orchestrator's own, one of them in a conflicts-of-interest disclosure |

**Three deviations withdrew a claim the study had already made**, and they are the entries a sceptical
reader should open first:

1. **D-021.** The reliability comparison counted `10.0` against `10.00` as coder disagreement in nineteen
   instances across ten products. The study had published, prominently, that `headline_price_usd` reached
   only α 0.568, and built on it the claim that "a price two trained readers cannot reliably agree on IS
   the finding". Compared as numbers those variables are among the study's strongest — **0.920 (raw 24 of
   26)** and **0.881 (raw 23 of 26)**. The claim was withdrawn rather than softened, and what replaced it
   is this paper's central finding. The entry also records that the retracted claim was **still in
   circulation in the instructions the work ran on**, and that three adjudications had run under it.
2. **D-060, retracted by D-063.** The study reported that one publishing row had no re-examinable evidence
   at all — naming seven local files, none of which existed — and called it the worst provenance case in
   the corpus. All seven existed, at the study root rather than under the path the check globbed. Corrected
   corpus-wide: **0 of 76 publishing rows have no re-examinable evidence.** It is stated rather than
   quietly fixed because the error ran *against* the study, and an unearned confession is as false as an
   unearned defence.
3. **D-050, with the register sentence corrected by D-074.** The study had filed 21 values as
   `access_failure` — our instrument failing to reach a document that exists. Challenged, and chased: 20 of
   the 21 were retrievable. Separately, the limitations register had stated that the index "must not score
   an `instrument_gap` unknown as non-disclosure"; the pre-registered instrument does not implement that,
   and the sentence was corrected in the register rather than left standing (§4.7).

### 3.10 Figures that disagree across this study's own documents

The freeze sweep found five hand-typed figures gone stale in four documents in one day (D-078), including
the study quoting two values for its own headline reliability figure. None was wrong when written; each
went stale because data moved underneath a number derived by a tool and typed into prose. **A checker that
diffs prose figures against the tools is the highest-value wave-2 item.** Drafting this paper found more of
the same class, listed unreconciled rather than silently resolved, because after the freeze a correction is
a published erratum and not an edit.

| Figure | Value A | Value B | Reading |
|---|---|---|---|
| Deviations logged | **79** — a direct count of the log (D-001 to D-080, D-024 vacated) | 77, then 76 — the freeze stamp's table and its own prose, disagreeing with each other; the register §10 heading said 76 | **This row moved while the paper was being drafted, for exactly the reason the paper gives.** The audit that produced this table was itself logged, as D-079, which took the count to 78. The freeze stamp now interpolates the figure instead of carrying it as prose, and the register's heading dropped the number altogether. **It moved a third time on publication day:** checking the freeze stamp's own hashes against disk for the first time found one of them already stale, which became D-080 and took the count to 79. This paper prints 79 and re-derives it immediately before publication |
| `instrument_gap` unknowns on publishing rows | **48** — freeze stamp, register §4 table, D-078, and a direct count of the frozen long table | 46 — register §4 prose, `analysis-first-findings.md` §3a | 48 is what the frozen data holds; "46" appears only inside prose about one product |
| Products flagged `paid_submission = yes` | **1 of 76** — frozen dataset and the scoring tool's report | four — `analysis-first-findings.md` §1 | This paper reports the D10 result as a raw count under rule D3 |
| Primary interquartile range | 69.9 to 86.5, width 16.6 — exclusive quartiles, width from the rounded bounds | 70.0 to 86.4, width 16.4 — scoring tool, inclusive type-7 quartiles, width from unrounded values | A convention difference of about 0.2 of a point on a 100-point instrument. Both are printed below; no conclusion turns on which is used |
| Raw two-pass agreement | **791 of 962 (82.2%)** — reliability history table, D-067, D-078 | 788 of 962 (81.9%) — the same document's headline line | D-078 corrected the figure to 82.2%; one standalone line was not re-typed |

Two further pairs are **not** disagreements, recorded so a reader does not mistake them for any.
`analysis-first-findings.md` computes two item-level shares over the 72 products carrying a published score
while the scoring tool computes them over all 73 active products, which is why one document prints item F2
as an exact even split and the other as 37 of 73 against 36 of 73. And the share of unknowns charged to our
own instrument prints as 48 of 337 in the frozen tables and as "13%" in two prose sentences that predate
the last retrieval sweep.

---

## 4. Results

### 4.1 Vendors disclose what you need to sign up, not what you need to budget

Four items are satisfied at full marks by almost the entire corpus. Every one is a term a buyer needs **in
order to become a customer**.

| Item | Points | Scored full |
|---|---|---|
| A1 Headline price published | 8 | **67 of 72 (93.1%)** |
| A2 Annual-billing condition disclosed | 7 | **45 of 46 (97.8%)** |
| D3 Refund position documented | 6 | **68 of 72 (94.4%)** |
| D4 Cancellation route documented | 4 | **68 of 72 (94.4%)** |

Against them, the items the corpus fails. Every one is a term she needs **in order to forecast a bill**.

| Item | Points | Scored full | Scored zero |
|---|---|---|---|
| **C5 Failed-generation charging documented** | 3 | 7 of 64 (10.9%) | **57 of 64 (89.1%)** |
| E2 Watermark position determinable | 3 | 25 of 63 (39.7%) | **38 of 63 (60.3%)** |
| F2 No unquantified limit clause | 4 | 37 of 73 (50.7%) | 36 of 73 (49.3%) |
| C2 Credit-to-output rate published | 7 | 20 of 48 (41.7%) | 10 of 48 (20.8%) |
| C4 Rollover policy documented | 4 | 38 of 48 (79.2%) | 10 of 48 (20.8%) |
| B2 Free-tier restrictions disclosed | 5 | 24 of 60 (40.0%) | 1 of 60 |

**57 of the 64 products with a metered generation step do not document whether the buyer is charged when a
generation fails.** That is the sharpest single fact in this dataset. A buyer can learn the price of a plan
from 67 of 72 of these vendors, and can learn from 7 of 64 of them whether a failed output costs money.

**Fewer than half publish the rate that converts the vendor's currency into work.** Item C2 decides whether
a published price means anything, and it carries the index's second-highest weight for exactly that reason:
of the 48 products with a credit system, 20 publish it in full, 18 partially and 10 not at all.

The same shape appears at component level. **Component C, the unit-cost group, is where the corpus
separates** — an earned-points interquartile range of 14.5 points, wider than any other component, on the
lowest median earned share of the points available to it, 64.0%. **Component D, renewal and exit, separates
almost nothing** — an earned-points interquartile range of 2.0 points out of 20, on a median earned share
of 100.0%. D moves the level, not the ordering.

**This finding was reached twice by independent routes.** The per-variable consistency analysis found it
first, before any index score existed: vendors are legible about price — `headline_price_usd` at α 0.920,
`first_charge_amount_usd` at 0.881 — and illegible about entitlement, where `unquantified_limit_clause`
reaches 0.249, `free_plan_cap_value` 0.285, `cost_per_output_computable` 0.309 and `usage_cap_quantified`
0.493. What two careful independent readings of the same documents cannot agree on is not what a product
costs, but what you get for it. The index reaches the same conclusion from the coded values rather than
from reader agreement.

### 4.2 The distribution of the index

**72 of the 73 active products carry a published index.** One is withheld by the availability guard, its
`available` of 37.0 falling below the threshold of 50. Three discontinued products carry no score under
rule D8.

| | Full frame | `paid_submission` removed |
|---|---|---|
| n scored | 72 of 73 | 71 of 72 |
| **median** | **80.25** | **80.0** |
| interquartile range | 69.9 to 86.5 | 70.0 to 86.4 |
| min – max | 26.9 – 93.0 | 26.9 – 93.0 |
| mean, beside the median and never instead of it | 77.8 | 77.7 |

**The median is printed to two decimals deliberately.** It lands exactly on a rounding boundary: the 36th
and 37th of the 72 scores are 80.0 and 80.5, so round-half-even prints 80.2 and round-half-up prints 80.3 —
and **two of this study's own artifacts printed each, before anyone compared them.** Neither convention is
wrong and the data never disagreed. Quoting the figure to one decimal requires saying which convention is
in use; 80.25 removes the question. The same boundary explains a second pair of printed figures: under rule
D10, removing the record flagged `paid_submission = yes` moves the median from 80.25 to 80.0 — a quarter of
a point, printed as a 0.2-point move in one of this study's documents and as 0.3 in another. **The
conflict-of-interest robustness check the protocol requires therefore passes**; the flagged record is
reported as a raw count under rule D3 and is identifiable in the dataset by its own column.

| Band | Products |
|---|---|
| Determinable (85.0–100.0) | 24 of 73 (32.9%) |
| Mostly determinable (70.0–84.9) | 30 of 73 (41.1%) |
| Partly determinable (50.0–69.9) | 17 of 73 (23.3%) |
| Largely undeterminable (30.0–49.9) | **0 of 73** |
| Undeterminable (0.0–29.9) | 1 of 73 |
| Withheld by the guard rule | 1 of 73 |

### 4.3 The index measures level adequately and ranks poorly

66.1 points of observed range on a 100-point instrument, and **the middle half of the corpus packs into
about 16.6 points.** A single ten-point interval holds **29 of 72 products (40.3%)**, and the 30–49 band is
empty.

| Ten-point interval | Products |
|---|---|
| 90.0 – 99.9 | 9 of 72 (12.5%) |
| **80.0 – 89.9** | **29 of 72 (40.3%)** |
| 70.0 – 79.9 | 16 of 72 (22.2%) |
| 60.0 – 69.9 | 14 of 72 (19.4%) |
| 50.0 – 59.9 | 3 of 72 |
| 20.0 – 29.9 | 1 of 72 |

Twenty-three of the 72 published scores sit in a tie group and 11 distinct values are shared by two or more
products. Ties are reported as ties, with no tiebreaker and no forced ordering.

**For products inside the interquartile range, the index yields a band and not a ranking.** A two-point
difference between two products in the seventies is not a finding about either of them. **This study
publishes no league table of the middle**, and a reader who extracts one from the dataset is using the
instrument for something it has been measured as unable to do.

**Why it ranks poorly is specific.** The four items in §4.1's first table are near-invariant — 67 of 72, 45
of 46, 68 of 72 and 68 of 72 applicable products take the same full score — and together they carry **25 of
the index's 100 points while doing almost no discriminating work.** Component A sits at its ceiling for 61
of 72 products (84.7%), so an A-column difference is not one vendor disclosing more than another; it is the
point value of items removed as `not_applicable` for products with no annual billing option. Two items sit
at the **floor** instead — C5 for 57 of 64 and E2 for 38 of 63 — which is the opposite case: those items
are not failing to discriminate, the corpus is failing to disclose. Both are answerable in principle, since
7 and 25 products respectively do answer them, so a near-zero column is a disclosure failure and not an
unmeasurable construct.

### 4.4 A hypothesis that failed, recorded because it failed

The obvious inference from §4.3 is that a quarter of the index being nearly automatic must inflate every
score, making the high median an artifact. **That was tested rather than assumed, and it is wrong.**

| | median | interquartile width |
|---|---|---|
| primary index | 80.25 | 16.6 |
| four near-invariant items removed | **75.5** | **20.4** |

**The median falls 4.7 points.** Near-free items lift numerator and denominator together, so they barely
move the level. What they move is the spread: the interquartile range widens from 16.6 to 20.4 points once
they are gone. So the four items are dead weight for ranking and honest weight for level, and **the median
of 80.25 is a real result rather than a scoring artifact** — on this instrument, most of these products do
score well. The prediction is recorded alongside the result because a prediction that did not survive is
worth as much as one that did. (Both widths use the exclusive quartile convention of §3.10; on the
inclusive convention the comparison runs 16.4 to 19.7 and the conclusion is unchanged.) The weights are
frozen for this wave and stay frozen.

### 4.5 Sensitivity analyses

**S1, equal weights.** 19 of 73 products (26.0%) change band at all, and **no product moves more than one
band**, so the marking rule marks nothing this wave. The ordering this study reports is therefore not an
artifact of the weighting judgment.

**S2, `unknown` items removed** — the most favourable reading available to any vendor.

| | median | min | max | n |
|---|---|---|---|---|
| primary index | 80.25 | 26.9 | 93.0 | 72 |
| **S2, `unknown` removed** | **88.2** | **67.4** | 100.0 | 71 |

**Eight points of median is the price of this study's stance on `unknown`, and it is published rather than
argued about.** At the bottom of the distribution it is far more: the lowest S2 score is 67.4 against a
primary minimum of 26.9. 36 of 73 products (49.3%) change band under S2 and one moves two bands.

### 4.6 Instrument consistency

| Population | products | units | α |
|---|---|---|---|
| **All 26 pre-registered double-coded products** | 26 | 962 | **0.811** |
| Outside exposure tier A | 19 | 703 | 0.798 |
| Tier C — never named in anything a coder reads | 5 | 185 | 0.823 |

Raw two-pass agreement: **791 of 962 (82.2%)**. The whole progression is printed because the corrections
moved the figure **across the conventional 0.800 threshold**, and a reader is entitled to see that the
movement came from fixing comparisons rather than from choosing a friendlier method: 0.790 as first
published, 0.786 after the tool was made to read every storage shape (D-020), 0.807 after numbers were
compared as numbers (D-021), and **0.811** after eight out-of-enum values were corrected (D-022). The
margin over the conventional line is 0.011, well inside what a different defensible comparison choice could
move.

**The pooled figure flatters, and the per-variable table is the honest one:** median per-variable α
**0.770**, with **17 of 37 variables** reaching 0.800. Pooling 37 heterogeneous variables into one
coincidence matrix holding 193 distinct values, where the median variable has about five, inflates α
mechanically, since α = 1 − D₀/Dₑ and pooling enlarges Dₑ. The weakest variables are listed in §4.1 and
they are the study's finding rather than its noise. One is not a measurement at all:
`computation_assumptions` is a free-prose field recording a coder's own arithmetic, and it returns
α = −0.001; it is slated for reclassification as documentation in wave 2.

**One direct check on whether agreement tracks correctness exists.** 145 disputed variables went to a third
reading working from the documents rather than from the prior records: it picked pass 1 on 64 of 145
(44.1%), pass 2 on 58 of 145 (40.0%), and **neither on 23 of 145 (15.9%)**. That last figure conflates
three things. **13 of the 23 are one product** whose entry tier the sampling rules leave underdetermined,
all thirteen resolving to `unknown` because the adjudicator refused to pick a side on a rule that does not
decide; **6 are completeness merges** on free-plan cap values; **4 are genuine reversals.** Excluding the
underdetermined product: **4 of 132 disputed variables (3.0%) are genuine reversals.** When two independent
readings disagree, a third rarely finds a third answer.

**What that check cannot see is both readings being wrong together**, and the study has direct evidence it
happens: three coders independently reached the same wrong reading of a codebook carve-out and an
adjudicator endorsed it in passing (D-046), and a pattern classifier the study built made 50 errors of
which **49 ran toward the study's own headline** (D-048). The reliability figure is therefore **bounded
above by correlated error that the design can detect only when it happens to disagree with itself.**

**The exposure check, with its weakness stated.** If the structural exposures of §3.6 had inflated
agreement, exposed products would agree more. They do not: tier C — the five products never named anywhere
a coder reads — is the **highest** at 0.823, above the pooled 0.811 and above the 0.798 outside tier A, the
opposite of exposure's expected signature. That is evidence, not proof: five products and 185 units cannot
carry a robustness claim on their own, and this paper says so rather than presenting a tidy-looking figure.

**The three for-cause second codings, reported separately as promised.**

| | raw agreement | α |
|---|---|---|
| product A | 23 of 36 (63.9%) | 0.603 |
| product B | 27 of 36 (75.0%) | 0.728 |
| product C | 30 of 36 (83.3%) | 0.823 |
| **pooled** | **80 of 108 (74.1%)** | **0.720** |
| the 26 pre-registered products, for context | 791 of 962 (82.2%) | 0.811 |

All three were promised on 2026-08-06, 08-07 and 08-12 and carried out on 2026-08-17, eleven days late. The
pooled figure sits 8.1 points below the corpus, and **publishing it without its decomposition would mislead
in both directions.** It invites the inference that records collected after a breach are worse, which the
individual figures do not support — one of the three is *above* the corpus — and it hides that the low one
is not noise. Product A's 13 disagreements resolve to **four** independent judgments, the other nine being mechanical
cascades of them: one underdetermined codebook question; one first-reading over-read that credited a
vendor with disclosures it did not make, reading a free plan out of a data object the vendor's own front
end suppresses; one classification question the variable's own value list does not cover, which the
adjudication settled from the protocol's source hierarchy and which matched neither coder; and one
instrument-delivery defect of ours — a rule pushed to a running coder without the caveat it is written
alongside, which reversed five properly-disclosed variables to `unknown`.

**The same rule failed on product B as well, in the opposite direction and for the opposite reason.** On A
it arrived mid-task without its caveat and made the coder too strict; on B it never arrived at all, and
the coder read three values out of markup no page displays — too permissive. Both failures are ours, and
they are the same rule. Removing B's rule error lifts it to 27 of 33 (81.8%) at α 0.800, level with the
corpus figure. All three went to adjudication and all three
adjudications changed the published record. **None of this is evidence that two independent readings of the
same documents drift far apart, and one quarter of it is evidence that a mid-task instruction is a worse
way to bind a coder than a document is.**

### 4.7 Unknowns, and who they belong to

**337 of 2,812 coded values (12.0%) are `unknown`**, and every one carries an attribution kind. Collapsed
from variables to items, active products carry **184 of 1,316 applicable items (14.0%)** in an `unknown`
state.

| Kind | On the 76 publishing rows | Across all records, including the blind second pass |
|---|---|---|
| vendor silence | 283 of 337 (84.0%) | 492 of 581 (84.7%) |
| **instrument gap** | **48 of 337 (14.2%)** | 70 of 581 (12.0%) |
| access failure | 4 of 337 | 15 of 581 (2.6%) |
| unattributable on the record's own evidence | 2 of 337 | 4 of 581 |

The publishing-row column governs any figure a reader uses. Of the 337, **124 were decided by hand with a
written reason a reader can check** and 213 by pattern. **0 unknowns carry no attribution kind.**

**The instrument-gap figure is the largest single correction this study makes against its own headline.** A
vendor that publishes a quarterly billing cadence and receives `unknown` because the value list has no
quarterly value has disclosed fully; scoring it as opaque measures us. That share roughly doubled under an
audit and then fell back as retrieval sweeps moved values, settling at 48 of 337.

**The audit that moved it** read 394 pattern-set attributions row by row against their records' full
evidence, by two independent reviewers: **344 of 394 confirmed (87.3%), 50 wrong**, and **49 of the 50
errors had assigned `vendor_silence`** — a systematic bias toward the category that flatters this study's
own finding, now measured rather than suspected. Had the dataset frozen before that audit, the paper's
central quantity would have been wrong by nine points in the direction of its own thesis. Both reviewers
also **reversed their own initial flags** where the study's existing hand decisions had settled a boundary;
an audit that corrects in one direction only, without ever finding itself wrong, is not an audit.

**The access-failure figure moved further than anything else, and the path matters more than the
endpoint.** It stood at 21 values when the practice of filing gaps as limitations was challenged on the
ground that a shortcoming is only honest after you have actually tried. Three retrieval sweeps went back to
the documents, and **59 of 60 values held as `access_failure` proved retrievable** — not one reclassified
to flatter the study, each reduction coming from a document being fetched and read, each reclassification
running through `vendor_silence` or `instrument_gap` on stated evidence with a basis recorded per row. Note
the direction: ten retrievals found the construct **absent**, converting an assumed limitation of ours into
a verified finding about the vendor and making the study's headline **larger**, on evidence. **Four values
survive as `access_failure`**, including the cleanest instrument miss in the corpus — a pre-window capture
already carrying the sentence that answers the variable, on a document reachable throughout that our
procedure did not reach.

Unknowns are not spread evenly: the five most unknown-heavy products carry 13, 7, 6, 5 and 5 unknown items.
A score built largely from zeroed `unknown` items is a claim about disclosure and not a measurement of a
term, which is why per-product `unknown_count` and `determinability_rate` travel with every index value.
Across active products the item-level `unknown` count has median 2.0 (interquartile range 1.0 to 3.0, min
0.0, max 13.0, mean 2.5 beside the median), and `determinability_rate` has median 0.82 (interquartile range
0.75 to 0.89, min 0.32, max 1.0, mean 0.81 beside the median).

### 4.8 Provenance, and two products the frame described wrongly

Every cited archive capture was verified individually, across four sweeps: **469 of 516 exact (90.9%)**, 13
of 516 resolving to the nearest same-day capture, 20 of 516 citing a timestamp with no capture behind it,
13 of 516 withheld by the archive as a 403, 1 of 516 with no capture at all, and **0 of 516 unanswered**.
**482 of 516 citations resolve** (93.4% including the same-day nearest). The figure was **377 of 511
(73.8%) until the closing day**, when 92 citations the service had refused across three sweeps were
re-asked and every one answered — so the earlier number measured an outage and is now replaced by a
measurement of the archive. The 13 nearest-capture rows are reported separately, because the service
resolves an inexact citation to whatever is nearest *at request time*: this study watched one resolve to a
capture dated 13 August and, two days later, to one dated 16 August.

Two rows are findings rather than defects. **Thirteen "no capture exists" verdicts were actually 403s**,
recorded as absence because the verifier classified any unrecognised HTTP status as `missing` while its own
detail column printed `HTTP 403` beside every one from the first sweep; the study's genuine archival
absence is one citation. And **twelve of the thirteen belong to one vendor whose entire domain the archive
refuses**, on every URL form tried, while four peer domains returned 200 in the same run and nothing in
that vendor's own `robots.txt` asks archivers to stay out. That is a finding about the vendor — its
published pricing documents cannot be independently re-examined at any past date by anyone outside the
archive — noted rather than scored, because the index measures what a vendor discloses and not whether
third parties may keep a copy.

**No publishing-row value rests on a capture a reader cannot open**: 51 of 76 publishing rows have both a
resolving capture and a local file, 17 a resolving capture only, 8 local files only, and **0 have neither**.
For 159 coded values the local capture is the only surviving evidence, which is why the source directories
ship with the release. One provenance defect is **reported and deliberately not fixed**: a record pairing an
access date with an archive URL stamped five days earlier, across a demonstrated edit to that page. Its
coded values survive in both captures, no record was edited on freeze day, and that invariant was kept in
preference to the correction, as an owner decision in the open.

**Two products the frame called active had already been discontinued**, and how they were found matters
more than the count. The first was found by a coder that opened the vendor's own page and read "no longer
available", with the vendor's help centre dating the shutdown more than three months before the freeze; a
status verification sweep followed across every row not already evidenced active by its own coding — 31
rows, 30 confirmed, 1 changed. The second had filed for liquidation two months before the freeze and its
entire domain returned an HTTP 402 hosting error on every path, observed on three separate days by two
independent checkers. **The honest reading is specific.** Against the failure mode the freeze-time check
was designed for — a vendor that announces a shutdown on its own site — it looks broadly sound, since all
30 other rows confirmed cleanly. Against a failure mode it was never built for — a vendor that collapses
and stops paying its hosting bill, announcing nothing anywhere — it failed, and **both rows it missed are
of that second kind.** A future wave should test liveness directly rather than look only for announcements.
Both moved to the discontinued stratum with documented shutdown dates, and the reliability sample is
untouched because none of the three discontinued products is in it. What it would have cost is why rule D8
exists: 24 of one of those records' 37 variables are `unknown` because the product's pricing surfaces are
gone, so scored as active it would have entered the index as a near-total transparency failure — measuring
a dead product's missing pages rather than any vendor's disclosure practice.

### 4.9 The minimum score, and what may not be said with it

One product scores **26.9**, the minimum, and is the sole occupant of the lowest band. **It must never be
cited as this study finding a vendor opaque.**

Every reason is a fact about the instrument rather than about the vendor. Thirteen of its 20 items are
`unknown` and its `determinability_rate` is 0.32, the lowest in the corpus. **Twenty of the corpus's 48
`instrument_gap` unknowns sit on that one record** — unknowns attributed not to the vendor's silence but to
a codebook that had no slot for the vendor's arrangement, because the product is reached only through a
large vendor's wider platform and the instrument was built for standalone products. The gap to the next
product is 23.6 points, and that single record alone sets the primary minimum, the observed range, and the
sole occupancy of the lowest band.

**And the analysis designed to expose exactly this distortion cannot be computed for it.** S2 removes
`unknown` items; rule S2.2 re-applies the availability guard to the recomputed denominator; removing 13
unknown items drops this product's `available` to 25.0, below the threshold of 50; and the variant is
**suppressed**. The one product whose score is most distorted by our treatment of `unknown` is the one for
which the analysis meant to show that distortion is withheld.

That is not a defect in the protocol: the guard exists so that a score computed over a quarter of the
instrument is not published as though comparable. Nor is it a defect that the primary index scores this
record's `instrument_gap` unknowns as zero — the limitations register once required otherwise, and that
requirement was **corrected rather than left standing**, because attribution kinds were assigned *after*
collection, partly by a pattern classifier, and re-weighting a frozen instrument using post-hoc
attributions is what pre-registration exists to prevent. But it has a direct consequence for what may be
said, and this paper honours it: **the 26.9 is reported as a fact about an instrument meeting an unusual
product, or not at all.**

---

## 5. Limitations

This is not a softening appendix. It is the list of things a reader should know before using any number
above, ordered by how much it should change what the reader concludes, following `limitations-register.md`.

**1. The frame is a census of one publication's coverage, not a sample of anything.** 76 products, complete
enumeration, no random selection, no sampling error, no inference to any wider population. The frame
reflects roughly two years of editorial coverage choices favouring categories with high buyer intent and
available affiliate programs, so those categories are over-represented relative to any plausible population
of AI products. **Nothing here supports a sentence beginning "AI vendors generally".**

**2. The coding was AI-assisted, and that changes what the consistency figure means.** No human read a
vendor's pricing page and coded a variable. α 0.811 is instrument consistency under independent double
reading and never inter-coder reliability, because two automated readings of the same input can fail
identically, agree, and raise the statistic without raising accuracy. **The most valuable robustness check
this study lacks is a human coding ten products against the same codebook**; it would bound the
correlated-error term directly, and it is wave 2's first recommended addition. A second model family
reading the same products would help separate instrument consistency from family-specific error — but
only to the degree the two families' errors are independent, **which is the same assumption this
paragraph has just declined to grant two instances of one family.** It is a weaker check than a human
pass for exactly that reason, and it is listed second rather than first.

**3. Reliability is weaker per variable than the pooled figure suggests.** Median per-variable α 0.770, 17
of 37 variables reaching 0.800; the per-variable table is the honest one and this paper prints it beside
the headline. The weakest constructs are not the prices but the entitlement variables, and that contrast is
the study's central finding rather than its noise. It survived a correction that withdrew an earlier,
opposite claim.

**4. A seventh of unknowns are our instrument, not vendor opacity.** 48 of 337 unknowns on publishing rows
are `instrument_gap`, and a vendor penalised for a codebook with no slot for its arrangement would be a
measurement of us. The primary index scores those as zero — post-hoc re-weighting is exactly what
pre-registration prevents — and what honours the concern is S2, published beside the primary at a median of
88.2 against 80.25. One product defeats even that (§4.9).

**5. Provenance is good and not perfect.** 482 of 516 citations resolve; 20 of 516 cited timestamps have no
capture behind them; one publishing row is affected in its citation rather than its value.
`archive_status` as coded is wrong on 14 of 76 rows and **12 of those understate our own provenance**, so
the dataset carries three computed columns beside the coded field rather than overwriting it.

**6. One geographic vantage point.** Currency is served by inferred geography, and no locale path, URL
parameter or request header overrides it. **Every reader in this study sat in one country**, so for three
records a money variable is `unknown` or `instrument_gap` because a USD figure was not obtainable from
here. One of the original four turned out not to be a vantage-point problem at all: a US-served crawl of
that vendor contains **none** of the plan content, because the price is rendered at runtime — a class of
vendor whose price is unarchivable in principle. Wave 2 must give the protocol an executable route for a
US-denominated read rather than a test with no route.

**7. The protocol cannot classify the variance it can demonstrate.** It admits a display-variance
classification only on two archive snapshots, and **an archive can never capture a client-side A/B variant,
because the crawler does not execute the experiment script.** So this study can show that a vendor's price
was under live experiment — both arms sit in the page's own markup — and simultaneously cannot classify the
resulting two-pass disagreement as display variance under its own rule. The bar was held rather than
lowered: the adjudicator that met this fetched both passes' archives through the raw endpoint, took a fresh
third capture, found all three identical, and resolved the disagreement as an ordinary one. On one product
the machinery was found outright — a consent-gated pricing experiment where declining analytics cookies
deterministically serves the control arm, and where both arms carry identical headline price, billing basis
and credit allowances, so nothing coded is affected. The methodological point survives the null result:
where a vendor A/B-tests its pricing page, **"the default display state" is not a single fact about the
vendor at all** — it is a fact about which arm the reader was assigned. This study found the test only
because one coder noticed a script. **Neither the number of products under live pricing experiment during
the window, nor the direction such experiments push a transparency score, is knowable from this dataset.**

**8. A format rule was breached corpus-wide and not repaired.** The `computation_assumptions` field carries
a 300-character cap stated twice in the codebook, and **37 of the 115 values that carry content exceed it
(32%), the longest at 1,240 characters.** They are not truncated, deliberately: the overruns are arithmetic
derivations with source citations, which is the reproducibility the field exists for. It is non-compliance
with a pre-registered format rule, **disclosed rather than repaired**, and the honest reading is that the
rule was wrong for a field that turned out to be documentation.

**9. The blindness record, and what it does not establish.** Six breaches, all six self-disclosed by the
agent that committed them. Three for-cause second codings reported separately at 23 of 36 (63.9%), 27 of 36
(75.0%) and 30 of 36 (83.3%), pooled 80 of 108 (74.1%) at α 0.720, published with the decomposition because
bare they mislead in both directions. Two structural exposures measured rather than assumed away, with the
never-exposed products scoring highest — evidence, not proof, on five products and 185 units. One
adjudicator's resolution on a single variable is recorded as **not excludable** rather than cleared: three
of its four resolutions ran opposite to what it had seen, and the fourth cannot be excluded.

**10. Seventy-nine deviations, including retracted claims.** Every one dated, with what it changed and in
which direction. Three withdrew a claim the study had already made, including one headline finding that
turned out to be a float-formatting artifact, kept struck through rather than deleted. The coordinating
instance's own errors are a large share: six confidently wrong numbers produced by reading one storage
shape or location where several existed, three records broken by line surgery on YAML, two commits that
swept another agent's work in, and one doctrine ruling reversed after an audit it had itself commissioned
argued it out of the position. **That list is the study's actual warrant.** Not that it did not err — it
erred constantly — but that the errors are recoverable from the record.

Three further pre-registered limitations are restated without elaboration: documents-only measures what a
reader can determine and never what a buyer experiences after paying; English-language public pages only,
which understates disclosure for non-English-first vendors; and the index is USD-centric by construction,
with every `non_usd` value identifiable in the dataset so a reader can recompute without the deduction.

---

## 6. Discussion

### 6.1 What the contrast means

That the failing items are exactly the ones a buyer needs *after* committing has an unglamorous explanation
this study cannot test and therefore names as a hypothesis: the first set is what a conversion-optimised
pricing page is built to answer, and the second is what a support article gets around to. **This study does
not test vendor intent, and an undocumented term is coded as undocumented and never as concealment.** What
can be said is that the two kinds of disclosure are produced with visibly different levels of care.

The practical consequence is direct: **a published price is a weak signal in this market.** For a metered
product, the price and the credit-to-output rate are one disclosure with two halves, and 28 of the 48
products with a credit system publish that second half only partially or not at all. A buyer comparing two
products on their headline monthly figures may be comparing two numbers that do not denominate the same
thing.

The failed-generation result deserves separate emphasis because it is the cleanest. Failure is not an edge
case in generative systems; it is a routine operating condition. 57 of the 64 products with a metered
generation step publish nothing about who bears its cost. It is not a hard disclosure to write — 7 of 64
vendors wrote it — and its absence transfers a small, repeated, unquantifiable cost to the buyer.

### 6.2 What the index is good for, and what it is not

**It is good for a band.** Whether a product is Determinable, Mostly determinable or Partly determinable is
a claim this instrument supports, and the band table is where a reader should stop. It is also good for the
component profile: a product at ceiling on A and D and poor on C has a specific, nameable disclosure gap,
and that profile is more useful to a buyer than the composite.

**It is not good for ordering the middle.** 29 of 72 products sit inside a single ten-point interval and 23
of 72 sit in a tie group. This paper publishes no ranking of the middle, and a reader should treat any
derived from the dataset as unsupported by the measurement. Wave 2's weighting review should consider the
four near-invariant items as candidates for reduced weight **for the purpose of discrimination**, while
noting that they are honest weight for level and that the wave-1 weights are frozen and will not be changed
retroactively.

### 6.3 The tooling failure modes are a contribution in their own right

`methods-tooling-failure-modes.md` documents **33 ways a documents-only audit of live web pages goes
wrong**. Every one happened in this study, was caught, and is dated in the deviations log. For many readers
it will be the most useful part of this work, because almost none of these failures looks like an error
while it is happening — **they look like findings.** Three examples, each of which inverted an assumption
the study started with:

- **A missing decompressor manufactures findings rather than losing them.** Archive raw-content responses
  arrive as gzip, zstd and brotli. A zstd capture decoded as gzip-or-nothing does not come back empty; it
  comes back as **noise**, and a price regex run over that noise **mined a `$5` out of it**, presenting as
  a total price change 112 seconds after the previous capture — on a page whose two captures are
  byte-identical once properly decoded. A decoder must never fail silently into "empty" or into raw bytes.
- **A checker that examines zero rows and exits 0** is the terminal case of a check covering less than it
  claims. This study's structural validator defaulted to a path relative to the repository root while every
  instruction told agents to run it from the study directory. The glob matched nothing, the loop never
  entered, the tool printed nothing and returned success, and agents reported "validated OK" on the
  strength of that silence for days. Re-run properly it found 129 records and zero failures — so no record
  was ever wrong and **nobody had established that.** The guard is one line: **a check that finds nothing
  to check must fail.**
- **Distinguish "we could not ask", "we are not allowed to read it", and "it is not there."** Three
  different facts, merged three separate times in one function here — including a degraded endpoint
  answering **HTTP 200 with zero bytes**, which a naive enumerator reads as "this URL has no captures".
  Retried, the same URLs returned 12, 66 and 66 records. Treat a zero-length success as a failure to
  answer, and check whether the refusal is itself your finding.

Two observations generalise. **The direction of a tooling error is not random, and the reassuring direction
is more dangerous**, because nothing prompts a second look: three of this study's storage-shape defects ran
alarming and were investigated immediately, while the reassuring ones sat. And **almost none of these
defects was caught by the check designed to catch it.** What caught them was a total exceeding a known
denominator, two independent readings of the same file disagreeing, an agent reporting something against
its own interest, and being asked a blunt question by someone who had looked.

### 6.4 The independent audits, and what replaces peer review

This study is published on the authoring publication's own site and possibly deposited on a preprint host.
**There is no peer review.** A referee would have forced the question in §3.5, and with no referee nobody
forces it. The venue raises a specific hazard too: an α of 0.811 deposited without its provenance can be
cited as human inter-coder reliability by someone who never sees this repository, which is a harm to other
people's work and is not undone by the dataset being open. What partially replaces the referee is that the
instrument, the deviations, the attributions and the corrections are all published — a weaker guarantee
than review, stated as weaker. Alongside it, four internal audits ran and each found real defects:

- **A second session, started by the owner on the same task and working read-only, audited the remedy for
  the study's most material blindness defect and found three things wrong with it** (D-014 amended): a
  fifth contaminated record the first pass had missed, because agent instructions load at spawn and one run
  straddled the fix; an exposure scan wrong in both directions, having searched a file no coder reads while
  using a context test loose enough to count almost any nearby word; and an overstated control group — the
  clean comparison set was five products, not thirteen. All three findings were adopted.
- **A parallel session audited the reliability computation** and found the tool reading one storage shape
  and silently dropping five units — the exact defect the pre-freeze checklist names as a hard requirement,
  committed inside the tool that produces the published number (D-020).
- **Two independent reviewers audited every machine-set attribution**, 394 rows, and found the 50-error,
  49-in-one-direction bias of §4.7.
- **An independent audit of an earlier deviation entry** found two of its claims inaccurate, and the entry
  was corrected in place with the original visible (D-013 corrected).

The disclosure norm that made much of this possible is not enforceable and is worth stating: **every
blindness breach in this study was reported by the agent that committed it**, unprompted and against its
own interest, including breaches nobody would have detected. That held because breaches were fixed
structurally rather than punished.

### 6.5 What wave 2 should do

In the order the evidence supports: **a human codes ten products against the same codebook**; **a checker
that diffs prose figures against the tools**, the only defect class that recurred five times in one day;
**an executable route for a US-denominated read** plus a US-based archive as a standard second vantage
point; **explicit testing for pricing-experiment machinery** rather than hoping a coder notices a script;
**reclassification of the prose documentation field** before the numbers exist rather than after; **a
weighting review of the four near-invariant items**, with wave-1 weights preserved; and **codebook slots
for the arrangements the instrument had none for**, including platform-embedded products, one-time credit
grants, and a fourth attribution kind for documents withdrawn before the window.

---

## 7. Conclusion

Across 76 products in one publication's coverage, coded from vendor documents alone inside a single window,
**these vendors disclose what a buyer needs in order to sign up, and not what a buyer needs in order to
budget.** A headline price is published by 67 of 72 applicable products, the annual condition by 45 of 46,
a refund position by 68 of 72, a cancellation route by 68 of 72 — and **57 of the 64 products with a
metered generation step do not document whether a failed generation is charged**, while the
credit-to-output rate that makes a price meaningful is published in full by 20 of 48 applicable products.

The pre-registered index puts a median of 80.25 on that picture, with an interquartile range of 69.9 to
86.5. **It measures level adequately and ranks poorly**, and this paper refuses to publish a league table
of its middle. Instrument consistency under independent double reading is α 0.811 across 26 products and
962 variable-instances, with a median per-variable α of 0.770 — a figure about how consistently the
instrument was applied, never about whether it was applied correctly. The frame is a census, not a sample,
and carries no confidence intervals, no significance tests, and no claim about AI products at large.

What this study offers besides its result is its record: 79 dated deviations, three of which retract a
claim it had already made in public; six self-disclosed blindness breaches and three for-cause re-readings
reported separately with their decomposition; 48 of 337 unknowns on publishing rows charged to our own
instrument rather than to vendor silence; 482 of 516 citations verified to resolve; and 33 documented ways
a documents-only audit of live web pages goes wrong. **The design's defence is not that it did not err. It
erred constantly, and the log says how. The defence is that the errors are recoverable from the record, and
that a reader who distrusts the coders can still use the dataset, because every coded value carries the
document it came from, the reasoning applied, and — where a value changed — what it was before and which
rule changed it.**

---

## Data availability

`dataset/coded-values.csv` (76 publishing rows × 37 variables), `dataset/coded-long.csv` (2,812 value rows
with per-value source, evidence and attribution), `dataset/apti-scores.csv` (per-product item scores,
components, both sensitivity variants, `unknown_count`, `determinability_rate`),
`dataset/data-dictionary.md`, `codebook-v1.md`, `protocol-v1.md`, `sampling-rules.md`, the frozen frame
file, `orchestrator/deviations-log.md`, the archive-verification and unknown-attribution files, and
`orchestrator/freeze-stamp.md`, which carries a SHA-256 per file so a reader can verify the copy they hold
is the copy that was frozen. **The per-product source directories ship with the release**: for 159 coded
values the local capture is the only surviving evidence. Published under CC BY 4.0 with a DOI minted at
publication. No vendor page content is republished.

**Freeze semantics.** After the freeze stamp, a correction to the dataset is a published erratum and not an
edit. This is not a claim that the dataset is free of error — 79 deviations say otherwise — but that error
found after that point is disclosed rather than absorbed.

## Conflicts of interest, funding, and paid submissions

No external funding, no grant. No vendor paid for this study, contributed to its design, or saw any part of
it before publication.

AI Tools Police is reader-supported and holds affiliate relationships with many of the vendors in this
frame. Mitigations, all checkable by a reader: the coding rules are mechanical, with a written decision
rule and worked example per variable; the second coding is blind to the first record and to our own
published investigation of the product; the index measures determinability, so a vendor can raise its score
only by publishing clearer documents; no vendor saw the dataset, the index or this paper before
publication; and every value publishes its source URL, access date and archive link, so any reader can
re-code a product and challenge the result. These reduce the risk of motivated coding. They do not
eliminate it.

Some products in this frame entered our portfolio through our published paid submission options, which buy
review speed or a labeled placement and never a score or a ranking. Those records carry
`paid_submission = yes` in the dataset. Every index result in this paper is reported twice, once over the
full frame and once with flagged products removed, so that a reader can see the difference rather than
accept an assurance about it.

## AI-assistance disclosure

Data collection, the coding passes, and the drafting of this paper are AI-assisted and run under named
human editorial control. A named person is accountable for every published value, every index score and
every claim in every artifact. No source is cited that a person has not opened. Human review covers every
adjudicated record, every record carrying a `conflicting` value, and the frozen dataset as a whole. AI
assistance never substitutes for the decision rules in the codebook: the rules decide the value, the
assistance applies them and surfaces the evidence.

**Nothing in this paper is written up as first-hand product experience, because the method includes no
product use.** No product in this corpus was used, trialled, purchased, subscribed to, signed into, or
operated at any point, and no claim here depends on any of those.
