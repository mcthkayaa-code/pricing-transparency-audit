# How this study was produced, and what its consistency figure measures

**A methods section. Owner-approved framing, 2026-08-17.**

This study is **AI-assisted research under named human editorial control.** The named editor is the
publication's owner and editor-in-chief, whose role was not nominal:

- fixed the research question and the design before any data existed;
- approved the protocol, the sampling rules and the codebook, and ratified the frozen frame;
- intervened on substance during the work, and **two of the largest corrections in the study came from
  those interventions rather than from any automated step** — a challenge that a figure was on a
  vendor's own page, which produced a retracted framing and a new archive route (D-056, D-057), and a
  challenge to the practice of filing gaps as limitations before they had been chased, which turned 21
  claimed access failures into one (D-050);
- reviews and signs off on the frozen dataset before anything is published. Nothing here is published
  on automated authority.

## What that framing does and does not cover

Editorial control governs **what is published**. It does not change **what a statistic measures**, and
this study reports one figure whose meaning depends on how the coding step was carried out. So that
step is described plainly below, and the figure is named for what it is rather than borrowed from a
convention that assumes something else.

**The figure is not reported as inter-coder reliability.** It is reported as **instrument consistency
under independent double reading**, because inter-coder reliability is a convention built on the
assumption that two readers' errors are largely uncorrelated — true of two people with different
training and blind spots, not guaranteed of two automated readings of the same input. Consistency is
still worth measuring: an instrument that two independent readings apply differently is broken whoever
applies it. It is simply a narrower claim than the conventional label would carry, and using the
narrower name is cheaper than using the wider one and then taking it back.

## How the coding step was carried out

**Every record was coded by a language model operating as an agent**, under the
documents-only protocol, with tool access limited to fetching and reading public web pages, writing its
own record, and running the study's validators. No human read a vendor's pricing page and coded a
variable from it.

Concretely:

- **Pass 1** — one agent per product, 76 agents, each given the product name and vendor URL and nothing
  from any other record.
- **Pass 2** — one agent per product for the 26 pre-registered double-coded products, each blind to
  pass 1: it could not read `records/pass1/`, and its assignment named the product and vendor only.
- **Adjudication** — one agent per disagreeing product, reading both prior records and both source
  sets, deciding by the codebook clause rather than by majority. **29 adjudicated records exist**: 24
  from the pre-registered double-coded set, 3 from the for-cause second codings, and 2 late ones. Both
  24 and 29 are true of different things and the paper says which.
- **Orchestration** — a further agent instance wrote the assignments, ran the tooling, maintained the
  deviations log, and made the rulings recorded in the adjudication queue. Its errors are logged
  alongside the coders' and are a substantial fraction of the log.

A human — the study's owner — set the research question, approved the protocol, ratified the frame, and
intervened repeatedly on substance. Two of the largest corrections in the study came from those
interventions rather than from any agent. That is documented rather than asserted: see D-050 and D-057.

## What this does to the figure

Krippendorff's alpha for this study is **0.811** across 26 products and 962 variable-instances, with a
median per-variable alpha of 0.770 and 17 of 37 variables reaching 0.800.

**That figure is agreement between two independent readings by the same model family**, which is why it
carries the consistency name set out above rather than the conventional one.

The difference is not a formality. Human coders bring idiosyncratic errors — different training,
different attention, different blind spots — and those errors are largely uncorrelated, which is what
makes their agreement informative about correctness. **Two instances of one model can fail the same way
on the same input.** Where they do, they agree, and the agreement statistic rises while accuracy does
not. An alpha computed between them is therefore **systematically optimistic** relative to the same
figure computed between humans, by an amount this study cannot quantify.

So the honest claim is narrow: **alpha 0.811 establishes that the instrument is applied consistently,
not that it is applied correctly.** Consistency is worth measuring — an instrument two independent
readers apply differently is broken regardless of who reads it — but it is a weaker claim than the
number's conventional reading, and every use of it in the paper is scoped accordingly.

## What can be measured about correctness, and what it says

The study has one direct check on whether agreement tracks correctness: **145 disputed variables went to
a third reading that worked from the documents rather than from the prior records.** Where the two
readers disagreed, the third reading either picked one of them or found something else.

| | count | share |
|---|---|---|
| third reading picked pass 1 | 64 | 44.1% |
| third reading picked pass 2 | 58 | 40.0% |
| **third reading found neither** | **23** | **15.9%** |

The 15.9% is the interesting figure and it conflates three different things, so it is decomposed:

- **13 of the 23 are one product** whose entry tier the sampling rules leave underdetermined. All
  thirteen resolved to `unknown` because the adjudicator refused to pick a side on a rule that does not
  decide. That is a finding about the instrument (queue item A-016), not about coder reliability.
- **6 are free-plan cap values** where the third reading wrote the fuller list that each reader had
  partially. Completeness merges, not disputes about fact.
- **4 are genuine reversals** — a third reading, from the same documents, reached what neither
  independent reader reached.

**Excluding the underdetermined-rule product: 4 genuine reversals in 132 disputed variables, 3.0%.**

So when two independent model readings disagree, a third reading usually confirms one of them and
rarely finds a third answer. That is a real and reassuring result about this design.

### Three products read twice for cause, reported separately

Three products received a blind second reading **because something had gone wrong on them** — a
disclosed blindness breach in each case — rather than because they were sampled. The pre-registration
committed to reporting their agreement **separately**, so that a re-read prompted by a problem could not
contaminate the planned statistic. That commitment is kept here.

| | raw agreement | α |
|---|---|---|
| product A | 23/36 = 63.9% | 0.603 |
| product B | 27/36 = 75.0% | 0.728 |
| product C | 30/36 = 83.3% | 0.823 |
| **pooled** | **80/108 = 74.1%** | **0.720** |
| the 26 pre-registered products | 82.2% | 0.811 |

**The pooled figure sits 8.1 points below the corpus, and publishing it without its decomposition would
mislead in both directions.** It invites the inference that records collected after a breach are worse,
which the individual figures do not support — one of the three is *above* the corpus. And it hides that
the low one is not noise.

Product A's 13 disagreements resolve to **four independent judgments**; the other nine are mechanical
cascades of them. All 13 went to a third reading, which **upheld the second coding on 8, the first on 3,
and neither on 2**. Two things in that resolution are worth stating because they cut against a tidy
story:

- **The first coding had credited the vendor with disclosures it did not make.** It read a free plan out
  of a data object the vendor's own front end suppresses with an explicit hide flag, and read an
  automatic-renewal position out of a sentence that grants cancellation rather than stating renewal.
  Nine of its values over-credited disclosure.
- **The second coding under-credited disclosure, and the cause was ours.** A rule barring values read
  from unrendered markup was pushed to the coder while it was working, without the caveat it is written
  with — that an embedded payload the page *renders* still counts. It applied the prohibition to a
  working FAQ whose answers a capture had simply failed to expand, and reversed five values to
  `unknown` on the strength of it. The third reading found **four of those five under-credited**; the
  fifth was `unknown` on both readings anyway, by different routes.

So of the three products read twice for cause, the lowest agreement figure decomposes into one
underdetermined codebook question, one first-reading over-read, and one instrument-delivery defect of
our own. **None of it is evidence that two independent readings of the same documents drift far apart**
— and one quarter of it is evidence that a mid-task instruction is a worse way to bind a coder than a
document is.

## The limitation that result does not touch, and the evidence that it bites

**Every figure above measures cases where the two readers disagreed.** None of it says anything about
cases where both agreed and both were wrong — which is precisely the correlated-error risk that makes a
model-coded alpha optimistic. Those cases are invisible to the reliability statistic by construction,
and this study has **direct evidence that they occur**:

- **Three coders independently reached the same wrong reading** of the codebook's `not_applicable`
  carve-out on output-related variables, and an adjudicator endorsed it in passing (D-046). One
  governing document did license the loose reading, which is a genuine mitigation — but four readers
  converging on one error is the shape correlated failure takes.
- **A regex classifier the orchestrator built made 50 errors, and 49 ran in the same direction** — toward
  the category that flattered the study's own headline (D-048). That is not a coder, but it is the same
  failure mode in the same pipeline: a systematic bias that no amount of internal agreement would have
  surfaced.
- **The orchestrator produced four confidently wrong numbers** by reading one storage shape when several
  existed (D-020, D-033, D-037, and once more inside D-047), each caught only because a total exceeded a
  known denominator or a second reading of the same file disagreed.

The paper states this plainly: **the reliability figure is bounded above by correlated error that the
design can detect only when it happens to disagree with itself.**

## What the design does about it, and what it cannot

Working:

- **Blind second coding**, with the mechanical exposure of the repository's own history disclosed and
  measured (D-014, D-017). Products never named anywhere a coder reads score *highest*, which is the
  opposite of exposure's expected signature.
- **Evidence required per value**, so a third reader can check the reading rather than the conclusion.
  Several reversals happened because a record's own quotation did not appear in its own saved source.
- **Third-pass adjudication that reads sources, not records**, which is where most of this study's
  substantive findings came from.
- **An audit of every machine-set classification** — 394 rows, 87.3% confirmed, and the 50 corrections
  moved the study's central figure nine points *against* its own thesis.
- **Seventy-seven logged deviations, including retracted headline claims**, kept in the open with the
  original wording struck through rather than deleted.
- **Agents that disclosed their own breaches** — three did, unprompted, in their own records, against
  their own interest.

Not working, and stated as such:

- **Nothing here establishes that model agreement predicts correctness in the general case.** The 3.0%
  reversal rate is conditional on disagreement.
- **No human independently re-coded any product**, so there is no human-versus-model comparison at all.
  That is the single most valuable robustness check the study lacks, and it is cheap: a human coding ten
  products against the same codebook would bound the correlated-error term directly. **It is recommended
  for wave 2 as the first thing to add.**
- **All readings come from one model family.** A second family reading the same products would separate
  instrument consistency from family-specific error. Also wave 2.

## Why this study is worth reading anyway

Not because the coders were reliable in the sense a human-coded study claims. Because **the instrument,
the deviations, the attributions and the corrections are all published**, and a reader can check any
value against the evidence recorded beside it. The design's defence is not that it did not err — it
erred constantly, and 57 entries say how — but that the errors are recoverable from the record.

A reader who distrusts the coders can still use the dataset, because every coded value carries the
document it came from, the reasoning applied, and where a value changed, what it was before and which
rule changed it.

## A note on venue, and why no referee raises the stakes rather than lowering them

This study is published on the authoring publication's own site, and possibly deposited on a preprint
host. **There is no peer review.** That changes what this section is for.

A referee would have forced the question this section answers. With no referee, nobody forces it — so
if it is omitted, the omission is not an oversight that review would have caught. It is a choice, made
by people who knew, and it reads that way to whoever notices later.

Two specific exposures follow from the venue rather than from the method:

**On our own site, credibility is the entire asset.** The publication's methodology page already
commits to not claiming work it has not done. Publishing a reliability figure that reads as human
inter-coder agreement, without saying who coded, would contradict that commitment on the same domain
that makes it — the same class of self-contradiction the publication has already had to correct
site-wide once.

**On a preprint host, the number becomes citable.** An alpha of 0.811 deposited without its
provenance can be cited as human inter-coder reliability by someone who never sees this repository.
That is a harm to other people's work, not only to ours, and it is not undone by the dataset being open.

**What replaces the referee here** is that the instrument, the deviations, the attributions and the
corrections are all published, and this section is published with them rather than left for a reader to
reconstruct. That is a weaker guarantee than review. It is stated as weaker.
