# A-009, A-011, A-016, A-017 — the instrument-gap family

**Resolved 2026-08-17 by the orchestrator. Zero coded values change. What changes is what the dataset
records about these values and what the paper is permitted to say about them.**

Four queue items, one question: **when a vendor publishes something the instrument cannot express, what
does wave 1 do?** The codebook is frozen (§11), so none of these is fixed by editing it. Each has been
coded `unknown` and attributed `instrument_gap`, and the four together are the reason that attribution
category exists.

| | the vendor publishes | the instrument cannot hold it |
|---|---|---|
| **A-009** | a plan price captioned as an annual per-seat total | `headline_billing_basis` has four recurring values, none of them that |
| **A-011** | a quarterly prepay cadence, on four records | the same value list has no quarterly value |
| **A-016** | prices on two official surfaces | `sampling-rules.md` §7.2 does not say whether its usage-based carve-out runs at the vendor-wide or product-attributable level, so which surface is the entry tier is undetermined |
| **A-017** | a price under live client-side A/B assignment, with both arms in the page's own markup | protocol §7.4.2 admits `variant_explained` only on two archive snapshots, and **an archive can never capture a client-side variant** because it does not execute the experiment script |

## The wave-1 treatment

**1. The value is `unknown` and the attribution is `instrument_gap`.** Both already hold across all four.
This is the whole point of separating the kinds of `unknown`: a reader can see that 67 of the corpus's 550
unknowns are the instrument's failure to express something published, not a vendor's failure to publish.

**2. The published dataset carries the vendor's actual figure in prose.** Every affected record states in
its evidence or `coder_note` what the vendor publishes — the quarterly amount, the annual per-seat total,
the two surfaces' prices. **Nothing is lost, it is only uncounted**, and a reader who wants the figure has
it. That is the honest position for a frozen instrument: record what you cannot score.

**3. The index must not score an `instrument_gap` unknown as non-disclosure.** This is A-016's substantive
demand and it generalises to all four. A vendor that publishes a quarterly price and receives an `unknown`
because our list lacks the word "quarterly" has disclosed fully; scoring it as opaque measures us. The APTI
guard is checked against these records specifically before any score is published.

**4. And the guard must use the corrected dependency count, not A-016's.** A-016 states that a
platform-embedded product's unknowns are "one tier question and 19 cascading". **That is wrong.** Codebook
§5.2 enumerates **six** entry-tier variables, ten with the price group; the other sixteen of that record's
unknowns share a different antecedent — which vendor surface the product is sold on. Inheriting 19 would
credit that vendor with far more dependent-unknown relief than its record supports. **Correcting it makes
that vendor look more opaque, which is why it is stated here rather than left in a footnote** (D-053).

## A-017 needs one thing the others do not

The other three are gaps in a value list. A-017 is a gap in an **evidentiary rule**, and it produces a
sentence the paper must carry:

> This study can demonstrate that a vendor's price was under live experiment — both arms are present in the
> page's own markup — and it simultaneously cannot classify the resulting inter-coder disagreement as
> display variance under its own protocol, because §7.4.2 admits only archive evidence and no archive can
> record a client-side variant.

Both halves are true and the gap between them is exactly the kind of thing a reader would otherwise assume
was an oversight. **The bar was correctly held**: the adjudicator that met this fetched both passes' archive
URLs through the raw endpoint, took a fresh third capture, found all three showing the same state, and
resolved the disagreement as an ordinary one. It did not lower the bar to reach a tidier statistic. The
limitation is the protocol's, and it is disclosed as such.

## What wave 2 must change

- **`headline_billing_basis`**: add quarterly prepay and annual-per-seat-total. Two independent blind coders
  hit the quarterly gap on the same products and reached `unknown` by the same route (A-011) — that is the
  instrument failing twice under independent observation, the strongest evidence a queue item can carry.
- **`sampling-rules.md` §7.2**: state which level the usage-based carve-out tests. Platform-embedded AI
  products are becoming the norm, not the exception.
- **Protocol §7.4.2**: admit a second evidence form for script-driven variants — the page's own markup
  carrying both arms, plus a dated screenshot of each state. Do not lower the archive bar; add a route that
  can actually be satisfied.
- **The dependency map should be explicit in the codebook**, not derived by a reader. The 19-versus-6 error
  above happened because nothing states which variables depend on the entry tier.

## What a reader should take from this section

Sixty-seven of 550 unknowns — **12.2%** — are this instrument's inability to express something a vendor
published. That is the largest single correction this study makes against its own headline, and it is
larger than the 3% attributable to documents we could not reach. **The instrument, not vendor opacity, is
the second-biggest source of unknowns in this dataset**, and wave 1's contribution is to have measured that
rather than to have fixed it.
