# First findings: what the index says

**Computed 2026-08-17, the first time the pre-registered index has been run against the data. Scores are
provisional until the freeze; the tool is `tools/score_apti.py` and its own output is
`dataset/apti-report.md`. This document is the reading on top of it, and every figure here was
recomputed independently of the tool before being written down.**

---

## 1. The distribution

**72 of 76 products carry a score.** One is suppressed by the §8.3.8 availability guard, three are
discontinued and excluded under rule D8.

| | value |
|---|---|
| **median** | **80.25** |
| interquartile range | 69.9 – 86.5 |
| min – max | 26.9 – 93.0 |
| mean, beside the median and never instead of it | 77.8 |

**The median is printed to two decimals because it lands exactly on a rounding boundary.** The
36th and 37th of the 72 scores are 80.0 and 80.5, so round-half-even gives 80.2 and round-half-up
gives 80.3 — and two of this study's own artifacts printed each before anyone compared them.
Neither convention is wrong and the data never disagreed; **80.25 is the figure, and quoting it to
one decimal requires saying which convention.**

| band | products |
|---|---|
| 20–29 | 1 |
| 30–49 | **0** |
| 50–59 | 3 |
| 60–69 | 14 |
| 70–79 | 16 |
| **80–89** | **29** |
| 90–100 | 9 |

**The 60s/70s split read 15 and 15 until the wix adjudication moved one product across the boundary
to exactly 70.0.** Recorded because the cause is new: earlier stale figures went stale when data moved
under a typed number, this one when a *later ruling* moved a score across a band edge. A banded table is
more fragile than the statistics it summarises, and the median, IQR, minimum and maximum were all
unaffected.

**One product of the 76 carries `paid_submission = yes`**, and it scores 83.8 — above the median.
Removing it moves the median 0.2 points. That is the conflict-of-interest check rule D10 requires,
and it is reported here as **a raw count rather than a distributional claim**, because rule D3 bars a
percentage for a group of fewer than five and a group of one supports no statement about how paid
submissions sit in a distribution.

**This paragraph said "the four products that paid a listing fee do not sit differently in the
distribution" until the preprint draft checked it against `dataset/apti-scores.csv`.** There is one,
not four, and the sentence made a distributional claim that n=1 cannot carry. The count was assumed
from a summary rather than read from the data — the same defect this study has now recorded seven
times, and the one place it appeared in a **conflict-of-interest disclosure**, which is the worst
place for it.

**Equalising the item weights moves no product more than one band.** So the ordering is not an artifact
of the weighting judgment, which is the one part of the index a referee cannot check from the data.

## 2. The index measures level adequately and ranks poorly

66.1 points of observed range, and **the middle half of the corpus packs into 16.6 points.** A single
ten-point interval holds **29 of 72 products (40.3%)**, and the 30–49 band is empty.

For products inside the interquartile range, **the index yields a band, not a ranking.** A two-point
difference between two products in the seventies is not a finding about either of them, and this study
will not publish a league table of the middle.

**Why it ranks poorly is specific and fixable.** Four items are near-universal — every one of them
scored at full marks by more than 93% of the corpus:

| item | points | scored full |
|---|---|---|
| A1 Headline price published | 8 | 93.1% |
| A2 Annual-billing condition disclosed | 7 | 97.8% |
| D3 Refund position documented | 6 | 94.4% |
| D4 Cancellation route documented | 4 | 94.4% |

**Those four carry 25 of the index's 100 points and do almost no discriminating work.**

**The obvious inference from that is wrong, and it was tested rather than assumed.** A quarter of the
index being nearly automatic looks like it should inflate every score and make the high median an
artifact. Removing all four and rescoring: **the median falls only 4.7 points, from 80.2 to 75.5.**
Near-free items lift the numerator and the denominator together, so they barely move the level.

What they do move is the spread: **the interquartile range widens from 16.6 to 20.4 points, about 23%
more discrimination, once they are gone.** So the four items are dead weight for ranking and honest
weight for level. **The median of 80.2 is a real result and not a scoring artifact** — on this
instrument, most of these products do score well.

## 3. The finding: vendors disclose what you need to sign up, and not what you need to budget

The four items nearly everyone satisfies are the four a buyer needs **to become a customer**: what it
costs, what the annual condition is, whether refunds exist, how to leave.

Set against them, the items the corpus fails:

| item | points | scored full | scored **zero** |
|---|---|---|---|
| **C5 Failed-generation charging documented** | 3 | **10.9%** | **89.1%** |
| E2 Watermark position determinable | 3 | 39.7% | 60.3% |
| F2 No unquantified limit clause | 4 | 50.0% | 50.0% |
| C2 Credit-to-output rate published | 7 | 41.7% | 20.8% |
| B2 Free-tier restrictions disclosed | 5 | 39.0% | 1.7% |

**57 of the 64 products with a metered generation step do not document whether you are charged when a
generation fails.** That is the sharpest single fact in this dataset. A buyer can learn the price of a
plan from 93% of these vendors and learn from 11% of them whether a failed output costs money.

**Fewer than half publish the rate that converts their currency into work.** C2 — the credit-to-output
rate — is the variable that decides whether a published price means anything at all, and it carries the
index's second-highest weight precisely because of that.

**Component C, the unit-cost group, is where the corpus separates**; component D, the renewal and
cancellation group, separates almost nothing (an earned-points interquartile range of 2.0 out of 20).

**This confirms the study's central finding by a second and independent route.** The reliability
analysis had already found it in the per-variable consistency figures: vendors are legible about price
— `headline_price_usd` reaches α 0.920 — and illegible about entitlement, and the limitations register
named that contrast as the central finding before any score existed. The index reaches the same
conclusion from the coded values rather than from coder agreement. Two routes, one answer, which is
the standard this study has held itself to throughout.

## 3a. What our stance on `unknown` costs a vendor — and the one product where it cannot be measured

The primary index scores an `unknown` item as zero. Sensitivity analysis **S2**, pre-registered in
§8.4, removes `unknown` items from both numerator and denominator instead — the protocol calls it "the
most favorable reading available to any vendor", and publishing it is how a reader sees what our stance
costs each product.

| | median | min | max | n |
|---|---|---|---|---|
| primary index | 80.2 | 26.9 | 93.0 | 72 |
| **S2, `unknown` items removed** | **88.2** | **67.4** | 100.0 | 71 |

**Eight points of median is the price of our stance on `unknown`, and it is published rather than
argued about.** At the bottom of the distribution it is far more than eight: the lowest S2 score is
67.4 against a primary minimum of 26.9.

**And one product exposes a gap between two documents this study has published.** `google-veo` scores
**26.9, the minimum, and is the only product in the `Undeterminable` band** — 13 of its 20 items are
`unknown` and its determinability rate is 0.32. But **20 of the 48 `instrument_gap` unknowns in the
whole corpus sit on that one record**: unknowns attributed not to the vendor's silence but to a
codebook that had no slot for the vendor's arrangement.

`limitations-register.md` §4 states that **the index must not score an `instrument_gap` unknown as
non-disclosure.** The pre-registered protocol §8.3 does not implement that — it says `unknown` scores
zero and never mentions attribution kinds, which were assigned after collection. **The scorer follows
the protocol, which is the right call**: re-weighting a frozen instrument using attributions decided
after seeing the data is what pre-registration exists to prevent.

So the register's requirement is honoured, as far as it can be, by **S2** — and S2 is
`suppressed` for `google-veo`. Rule S2.2 re-applies the §8.3.8 availability guard to the recomputed
denominator, removing 13 unknown items drops its `available` to 25.0, below the guard's threshold of
50, and the variant is withheld. **The one product whose score is most distorted by our treatment of
`unknown` is the one product for which the analysis designed to show that distortion cannot be
computed.**

That is not a defect in the protocol — the guard exists so that a score computed over a quarter of the
instrument is not published as though it were comparable — but it has a direct consequence for what may
be said:

**`google-veo`'s 26.9 must never be cited as this study finding a vendor opaque.** Its score is
dominated by items our instrument could not evaluate, the gap to the next product is 23.6 points, and
it alone sets the primary minimum, the observed range, and the sole occupancy of the lowest band. Every
one of those four figures is a fact about the instrument meeting an unusual product, not about the
vendor. The paper reports it as such or not at all.

## 4. What a reader must not take from this

**These are 72 products in one publication's coverage, not a sample of anything.** No confidence
interval, no significance test, no sentence beginning "AI vendors generally". `limitations-register.md`
§1 states the frame's biases; they are real and they favour categories with high buyer intent.

**12.4% of coded values are `unknown`, and 242 of those sit on scoring variables.** Where a product's
score rests on unknowns it is noisier than its two significant figures suggest; `google-veo` alone
carries 13 unknown items. Per-product `unknown_count` and `determinability_rate` ship in
`dataset/apti-scores.csv` so a reader can see which scores are thin.

**13% of unknowns are our instrument and not vendor opacity** (register §4), and the index does not
score an `instrument_gap` unknown as non-disclosure. A vendor penalised for a codebook that had no slot
for its arrangement would be a measurement of us.

**Two items score at the floor for most of the corpus, and that is the corpus, not the instrument.**
C5 and E2 are answerable in principle — 7 and 25 products respectively do answer them — so a near-zero
column is a disclosure failure and not an unmeasurable construct.

## 5. Where the analysis found its own errors

Recorded because a reader is entitled to know what the first pass got wrong.

**The tool's first version ranked components by percentage spread** and concluded that component F drove
the corpus's variation. That is wrong: the index is a points ratio, so a 10-point component swinging
across its whole range moves a score less than a 25-point component swinging across a third of its own.
Component C drives the spread. Both columns now print, so the mistake cannot recur silently.

**A hand computation disagreed with the tool on one of five products, and the hand pass was wrong.** It
read one variable as `not_applicable` and removed an item that all three storage shapes and the
adjudicated record's own prose say is `some_quantified` — a value carried across in error from the
product scored immediately before. Hand said 89.5, tool said 85.7. **The hand error ran 3.8 points high,
in the flattering direction.** The five hand-checked figures are now frozen inside the tool and
re-verified on every run.

**And the hypothesis in §2 above failed.** The expectation was that 25 near-free points would prove to
be inflating the median; the arithmetic says they move it 4.7 points. The expectation is recorded
alongside the result because a prediction that did not survive is worth as much as one that did.
