# Inter-coder reliability — pass 1 against pass 2

Computed 2026-08-14, after both passes closed and not before. No agreement figure was calculated at
any earlier point, deliberately: the orchestrator wrote every pass-2 assignment, and an early result
could have shaped the later ones (deviation D-013).

**Corrected 2026-08-15** after a parallel session audited the computation. The first version of
`agreement.py` read `computation_assumptions` only from `variables{}` and silently dropped the five
records that store it top-level — the exact defect the pre-freeze checklist names as a hard
requirement, committed in the tool that produces the published number. Every figure below is the
corrected all-shapes computation. What the first version reported is shown where it differs, because
the difference is small and hiding it would be worse than printing it.

26 products, 37 coded variables each, **962** comparable variable-instances.

## Headline

| Population | n | units | alpha |
|---|---|---|---|
| **All 26 products (pre-registered)** | 26 | 962 | **0.811** |
| Outside exposure tier A | 19 | 703 | 0.798 |
| Tier C — never named in coder-visible material | 5 | 185 | 0.823 |

Raw agreement: **791 of 962 = 82.2%**. *(This line read 788 / 81.9% until 2026-08-17 — the same stale
figure D-078 corrected in the tables below, in the one place the correction missed. Found by the
preprint draft checking every figure against the frozen data.)*

### How this figure moved, and why each move was a bug rather than a choice

| | units | raw | alpha |
|---|---|---|---|
| first published | 957 | 80.4% | 0.790 |
| after reading every storage shape (D-020) | 962 | 79.9% | 0.786 |
| after comparing numbers as numbers (D-021) | 962 | 81.9% | 0.807 |
| **after correcting 8 out-of-enum values (D-022)** | 962 | **82.2%** | **0.811** |
| re-verified at freeze, 2026-08-17 | 962 | **82.2%** | **0.811** |

Neither correction is an analytic decision. The first restored five units the tool had silently
dropped. The second stopped counting `10.0` against `10.00` as a disagreement — nineteen instances
where both coders read the same price and YAML serialised the float differently. Two identical
numbers are identical; treating them as disagreement was a defect in the comparison, of the same
class as reading one storage shape.

The full progression is printed because the corrections moved the headline **across the 0.800
threshold**, and a reader is entitled to see that the movement came from fixing comparisons rather
than from choosing a more flattering method.

## What the exposure tiers say

D-014 and D-017 established that half the reliability sample was named with coded values in material
coders were told to read, and that the repository's history names all 26. If that exposure had
inflated agreement, exposed products would agree more than unexposed ones.

They do not. **Tier C — the five products never named anywhere a coder reads — is the highest at
0.823, above the 0.811 pooled figure and the 0.798 for products outside tier A.** Exposure's expected signature is inflation among
the exposed; what the data shows is the opposite ordering by a margin far inside the noise of a
five-product estimate.

*The first version of this document claimed "the never-exposed group is not the highest". With the
five dropped units restored that sentence is false, and it is corrected rather than quietly
deleted. The substantive conclusion is unchanged and is now, if anything, better supported:
**exposure did not detectably inflate reliability.***

That remains evidence, not proof. Tier C is five products and 185 units, and no robustness claim
rests on it alone.

## What the headline number means, stated plainly

Krippendorff's convention treats alpha ≥ 0.800 as supporting firm conclusions and 0.667–0.800 as
supporting tentative ones. **At 0.811 this study clears the line, narrowly.**

That is stated with the same care the earlier sub-threshold figure was. The margin is 0.011, well
inside what a different defensible comparison choice could move, and the median per-variable alpha
below is 0.770 — so "clears the conventional threshold" is a fact about the pooled statistic and not
a licence to treat every variable as firmly measured.

Adjudication is therefore not optional tidying — it is what the published dataset rests on, and
protocol §7.4 already specifies the adjudicated row as the published one where it exists.

## The pooled figure flatters, and the per-variable table is the honest one

Alpha here is pooled across 37 heterogeneous variables into one coincidence matrix holding 193
distinct values, where the median variable has about five. Expected disagreement is 0.938 pooled
against roughly 0.620 averaged per variable, and since α = 1 − Do/De a larger De pushes alpha up.
This tool's own docstring warns that raw agreement is inflated when one value dominates a variable;
pooling reintroduces the same flattery into alpha.

| | value |
|---|---|
| pooled alpha (pre-registered method) | 0.811 |
| **median per-variable alpha** | **0.770** |
| variables reaching 0.800 | **17 of 37** |

Worst per-variable:

| Variable | alpha |
|---|---|
| `computation_assumptions` | −0.001 (free prose, not a measurement) |
| `unquantified_limit_clause` | 0.249 |
| `free_plan_cap_value` | 0.285 |
| `cost_per_output_computable` | 0.309 |
| `usage_cap_quantified` | 0.493 |
| `free_plan_cap_documented` | 0.571 |
| `failed_generation_charge_policy` | 0.604 |
| `auto_renewal_default` | 0.608 |

### A claim I made prominently and am now withdrawing

The previous version of this document reported `headline_price_usd` at α = 0.568 and
`first_charge_amount_usd` at 0.492, and used them to argue that "a price two trained readers cannot
reliably agree on IS the finding."

**That was substantially an artifact of float formatting.** Once numbers are compared as numbers,
those two variables are among the study's *strongest*:

| Variable | before | after |
|---|---|---|
| `headline_price_usd` | 0.568 | **0.920** (raw 24/26) |
| `first_charge_amount_usd` | 0.492 | **0.881** (raw 23/26) |

Two trained readers, working blind from a vendor's public documents, agree on the headline price 24
times out of 26. The claim is withdrawn rather than softened, and the correction runs against the
narrative the earlier version was building, which is the reason to state it plainly.

**What survives, and it is the more interesting version.** The genuine low-agreement variables are
not the prices — they are `unquantified_limit_clause` (0.249), `free_plan_cap_value` (0.285),
`cost_per_output_computable` (0.309) and `usage_cap_quantified` (0.493). What two careful readers
cannot agree on is not what a product costs, but **what you actually get for it**: whether a cap is
quantified, what the free tier's limit really is, whether cost per output can be computed at all,
and whether a discretionary fair-use clause qualifies an advertised allowance.

That is a sharper finding than the one it replaces. Vendors are largely legible about price and
largely illegible about entitlement.

### I checked whether the entitlement variables were another formatting artifact. They are not.

D-021 found that the price variables' apparent low agreement was substantially float formatting. The
obvious next question is whether `free_plan_cap_value` — third-worst at α = 0.285, and a free-text
format field — is the same story.

It is not. Of its 18 disagreements, **5 are wording on identical numbers** ("3 minutes maximum"
against "3 minutes max"; "50 Google Flow credits per day" against "50 credits per day"; one vendor's
own two names for the same two caps) and **13 are substantive**: different figures, different
completeness, or one coder finding a quantified cap where the other found none at all.

So roughly a quarter of that variable's disagreement is presentational and three quarters is real.
The low alpha stands, and it stands for the reason the write-up claims — two careful readers
genuinely cannot agree on what a free tier gives you. Reported here because the check was run
hoping for the D-021 answer and did not get it, and a study that only publishes the sensitivity
analyses that flatter it is doing something worse than not running them.

The five wording cases are not canonicalised the way the numeric fields were. Vendor label wording
is not mechanically normalisable — one of them is the vendor using two different names for the same
two caps on two of its own pages — so they go to adjudication like any other disagreement, which is
where two of them have already been resolved.

The paper publishes the per-variable table beside the pooled figure and discloses the pooling choice
explicitly.

## Sensitivity: the prose field (POST-HOC, reported as such)

`computation_assumptions` records a coder's own arithmetic in free prose. Two coders never write the
same sentence, so it returns α = −0.001 — literally no better than chance, because it is not a
measurement.

| Population | pre-registered | excluding the prose field |
|---|---|---|
| All 26 | **0.811** | 0.831 |
| Outside tier A | **0.798** | 0.818 |
| Tier C | 0.823 | 0.847 |

**The pre-registered figure of 0.811 is what the abstract carries.** The sensitivity sits beside it so a reader knows one documentation field
accounts for the gap — and because publishing only the higher number after seeing both is precisely
what this study has spent two weeks refusing to do.

> **Corrected at the freeze, 2026-08-17 (D-078).** The three figures above read 0.807, 0.795 and
> 81.9% until today, **while this document's own history table three sections up already recorded
> 0.811** as the value after D-022's out-of-enum corrections. One document, two figures for its own
> headline, and the stale one sat under the sentence "the pre-registered figure … is what the
> abstract carries". Established before correcting rather than assumed: `aiva` is the only
> reliability-sample record touched since this file was written and **none of its coded values
> changed**; the tool's only edit since was an inert reporting guard (D-026); and **the version of
> `agreement.py` as it stood when this file was written also returns 0.811** against today's
> records. Neither the data nor the tool moved the number — the prose was simply never updated
> when the history table was. The `excluding the prose field` column is left as written and is NOT
> re-verified here, because the tool does not compute it; it is flagged rather than silently
> carried.


Wave 2's codebook should classify `computation_assumptions` as documentation rather than a coded
variable, fixing it before the numbers exist rather than after.

## The outlier

`google-veo` agrees on 13 of 37, far below every other product. It is the one product reached only
through a large vendor's wider platform, where which purchasable plan grants access to THIS product
is genuinely contestable. Both coders documented their entry-tier reasoning and reasoned to different
answers from the same rule. That is an instrument limitation for platform-embedded products, not a
coder failure, and it goes to adjudication as one.
