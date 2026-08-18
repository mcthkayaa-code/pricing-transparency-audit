# A-013 and A-019 — what this instrument measures

**Resolved 2026-08-17 by the orchestrator, under delegated authority, and flagged for owner review
because it is the single most consequential interpretive choice in the study.**

Two queue items ask the same question at two different scales, and they cannot be answered
separately. A study that reads containment for one variable and visibility for another is measuring
two constructs and publishing them as one index.

- **A-013** (currency): a vendor's own help article states local-currency billing by default with USD
  as a fallback where the local currency is unsupported. Our coders were served a local-currency
  figure. Is the variable asking *does this vendor publish a USD price to anyone*, or *what currency
  is this buyer charged*?
- **A-019** (an allowance): a vendor's free-tier limit exists in the pricing page's inert embedded
  JSON — real vendor data, inside the document — and was never rendered to a reader across three
  loads. Is that documented or not?

---

## The rule

> **A variable asks what a reasonably diligent reader of the vendor's published documents can
> obtain, from any standard reading position, without inspecting page internals.**

Three clauses, each doing work:

**"a reader of the vendor's published documents"** — the unit stays the vendor's documentation, as
the protocol's documents-only design requires. Not the vendor's intentions, not its database, not
what a support agent would say if asked.

**"from any standard reading position"** — a plain browser, no account, no developer tools, but not
tied to one geography, one A/B arm, or one date. If the vendor serves a USD price to readers in the
United States, that price is obtainable and the study codes it.

**"without inspecting page internals"** — a reader reads a page. They do not read its JSON payload,
its JS bundles, or its DOM attributes. Data present only there is not disclosure.

## How each item resolves

**A-013 → vendor-centric.** The question is whether a USD price is obtainable from the vendor's
documents in some standard reading position, not what currency our particular coder was served. Where
a USD figure exists in a US-served state, it is the coded value and the local-currency state is a
display variant under protocol §6.8.

Where no USD figure is obtainable, the rule splits, and the split matters:

- **`non_usd`** where the vendor's documents establish a **single** currency with no alternative — no
  USD figure and no currency, locale or country selector anywhere. That is a positive, informative
  finding about the vendor, not an absence of one.
- **`unknown`** where the vendor serves currency by inferred geography and its own policy names USD as
  a fallback, so a local-currency reading cannot establish what a standard reader is served. Here
  `non_usd` would assert something about the vendor that a geography-bound reading cannot support.

*This split was written after checking the corpus rather than before. The first draft of this rule sent
every unobtainable-USD case to `unknown`, which would have been wrong for the one product that actually
codes `non_usd`: its record establishes by DOM scan that no USD figure and no currency selector exist
anywhere on the page. Publishing the first draft would have converted a correct, informative value into
a false unknown. The distinction above is the one the D-007 sweep had already drawn in practice —
two records recoded to USD found in their own archives, one left `unknown` because its vendor's policy
made the served currency geography-dependent.*

**A-019 → not disclosure.** A figure that exists only in unrendered markup fails the third clause. The
reviewer's `vendor_silence` classification stands.

## Why this reading and not the other

**It is already what the study did.** The D-007 sweep recoded two records to USD figures found in
archived US-crawled captures of the vendors' own pages. That was a vendor-centric act. The alternative
reading would make those two corrections wrong and require reverting them — and they were right: in
both cases the USD figure was sitting unopened in the record's own archive capture.

**D-003's founding logic says so explicitly.** It reasoned that a page rendered in local currency "may
be measuring us rather than the vendor." That is the whole argument for this rule, written before the
question was formally raised.

**The alternative is not reproducible.** A-017 established that this study met prices under live
client-side A/B assignment, and that an archive capture can never document a client-side variant
because the archive does not execute the experiment script. If the construct were "what this reader
was shown", then no reader — including a replication team — could reproduce a coded value, because
what they are shown depends on their geography, their A/B assignment, and the date. A transparency
index whose values cannot be re-derived is not an index.

**It keeps the measurement about the vendor.** Under the reader-centric reading, a vendor's score would
partly record where our coders sat. Two teams auditing the same vendor from different countries would
publish different transparency scores for identical vendor behaviour.

## What this reading costs, stated plainly

**It gives up a real and arguably more useful construct.** "What is a Turkish buyer actually charged,
in what currency, with what disclosure" is a legitimate question, it is what a buyer in that position
cares about, and this study is now explicitly not answering it. Our coders sat in exactly the position
that would have measured it, and we are declining the measurement on reproducibility grounds. That is
a real loss and it belongs in the limitations, not in a footnote.

**It is more generous to vendors on currency and less generous on rendering.** A vendor that publishes
USD somewhere gets credit even though most of its readers never see that state. A vendor whose figure
sits in unrendered JSON gets no credit even though the data is technically in the document it served.
Those pull in opposite directions, which is a sign the rule is tracking something other than vendor
favourability — but a reader is entitled to see both effects named.

**It cannot be applied retroactively without cost.** Pass 1 was coded vendor-centrically throughout
precisely so the class could be flipped together if adjudication chose otherwise (see A-013's original
entry). It chose not to flip. So no recoding follows from this decision — but that also means the
decision was made in a state where one answer was cheaper than the other, and a reader should know
that. **The rule above is the one I would give if both answers cost the same**, and the paragraph
above this one is the honest disclosure that they did not.

## What follows for wave 1

- **No coded value changes — verified, not assumed.** The corpus carries `non_usd` on exactly one
  product (six instances across the two passes and its adjudicated row), and its evidence establishes
  the single-currency case the rule permits. Every other money value is a figure, `unknown`, or
  `no_public_price`. Checked before this document was committed.
- The codebook does not change; it is frozen (§11).
- The paper states this rule in its methods, under its own heading, with the cost paragraph above.
- A-013 and A-019 are closed together, and the closure notes that they were never two questions.

## What wave 2 must do

State the rule in the codebook itself, in the definition of the variable class rather than in an
adjudication note, and give it a test rather than an example. Then add the currency question the study
declined here as a **second, separate variable** — "what currency is a reader in the study's own
jurisdiction served" — so the reproducible measure and the buyer-relevant measure can both be reported
instead of one being sacrificed to the other.

## Owner review

This is a construct decision, not a coding decision, and it determines what the paper's central claims
are claims *about*. It is recorded as resolved so the freeze is not blocked, and it is the first item
the owner should overturn if they disagree. Overturning it would require recoding the currency variable
class across the corpus and reverting the D-007 sweep, which is why it is flagged now rather than after
the analysis is built on top of it.
