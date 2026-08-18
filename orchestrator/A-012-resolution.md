# A-012 — the paid intro period

**Resolved 2026-08-17. Sweep item: one rule, applied to every affected record, settled here rather
than product by product.**

Several vendors sell a cheap **non-zero** time-limited intro period that auto-converts to a much
higher recurring rate. `trial_exists` is defined as a time-limited **free** trial, and its four
decision rules name free plans, money-back guarantees, silence and conflicts — never a paid intro
period. One coder read the construct and coded `yes`, documenting the departure. A coder reading the
definition literally codes `no`, which scores B3 full points for documented absence and sends the
other three trial variables to `not_applicable`. The instrument is frozen (codebook §11), so this
document decides the wave-1 treatment; it does not change the codebook.

---

## 1. The candidate list

The literal token `A-012` appears in exactly seventeen pass-1 records. Every one was opened and its
`coder_note` read. **Four are positive.** The deciding sentence is quoted from each record.

| # | Record | Class | The sentence that decides it |
|---|---|---|---|
| 1 | `pass1/openai-sora` | NEGATIVE | "No official document found described a paid, time-limited introductory price for Sora … the documented credit-purchase mechanism is not described as time-limited or introductory in any recoverable source." |
| 2 | `pass1/originality-ai` | NEGATIVE | "Not A-012 (PAYG is a standing one-time purchase, not a cheap time-limited intro period that auto-converts to a higher recurring rate — no such intro mechanic was found anywhere in the documents)." |
| 3 | `pass1/phrasly` | **POSITIVE** | "Phrasly sells a paid, time-limited intro period ('3 Day Access' / Trial Period): $2.00 USD … for 3 days, auto-converting to TRY 953.90/month billed annually … a materially HIGHER recurring rate than the 'Unlimited' tier's own direct-purchase price of TRY 524.43/mo." |
| 4 | `pass1/pika` | NEGATIVE | "A-012 does not apply — this is not a paid time-limited intro period, it is the ordinary 'no trial found' case." |
| 5 | `pass1/plus-ai` | NEGATIVE | "The trial is a genuinely free 7-day trial (1,000 AI credits at no charge, card on file for auto-conversion afterward), not a paid time-limited intro period." |
| 6 | `pass1/quillbot` | NEGATIVE | "No A-012 concern — the Monthly/Quarterly/Semi-Annual/Annual options are all standard ongoing recurring terms at their own stated recurring rate, not a cheap intro period that jumps to a higher rate after a short window." |
| 7 | `pass1/resume-io` | **POSITIVE** | "resume-io sells a cheap non-zero (not free) time-limited intro period ($2.95 for 7 days on the non-entry '7-day Trial' card) that auto-converts to a much higher recurring rate." |
| 8 | `pass1/rezi` | NEGATIVE | "No cheap non-zero time-limited paid intro period was found anywhere (Quarterly is a standing discounted recurring cadence, not a short intro period that converts to a higher rate)." |
| 9 | `pass1/shortsfaceless` | **POSITIVE** | "shortsfaceless sells a paid, non-zero, time-limited intro price ($9 for the first month against a standard $19/mo) at shortsfaceless.com/deal." |
| 10 | `pass1/synthesia` | NEGATIVE | "No paid time-limited intro period found (Synthesia's trial-adjacent offerings are a free plan and a free one-off 'try for free' video generator, not a discounted paid intro period)." |
| 11 | `pass1/teal` | NEGATIVE | "Teal documents no free trial AND no paid time-limited intro period of any kind (confirmed by a dedicated official FAQ …)." |
| 12 | `pass1/udio` | NEGATIVE | "Udio's trial (7 days) is a genuine FREE trial per ToS §3.5 and the help center; A-012 does not apply to this record." |
| 13 | `pass1/undetectable-ai` | NEGATIVE | "No paid time-limited intro period was found; the trial is free (not a low-cost paid tier), so the literal token is deliberately omitted." |
| 14 | `pass1/vidnoz` | NEGATIVE | "A-012 considered and NOT applied: no document states a specific, distinctly time-boxed low intro window (e.g. '$X for N days') before a rate change." |
| 15 | `pass1/wix` | NEGATIVE | "No paid time-limited intro period exists (standard upfront billing plus a 14-day money-back guarantee, not a discounted trial period)." |
| 16 | `pass1/writehuman` | NEGATIVE | "No paid time-limited intro period (A-012) exists for this product — all tiers are standard ongoing monthly/annual subscriptions." |
| 17 | `pass1/zety` | **POSITIVE** | "Zety's Pro Package sells a paid (non-free), time-limited intro period ($1.70 / 14 days) that auto-converts to a materially higher recurring charge ($23.95/4wk)." |

**Positive: 4 of 17.** The queue named three of them (zety, resume-io, phrasly) and did not name the
fourth. `shortsfaceless` was recorded as a positive by both its passes and coded `no` anyway — the
divergence in treatment the sweep exists to remove.

`myperfectresume` is the item's originating record and **does not contain the token**, so it is not
one of the seventeen. It is the fifth positive and is treated with them below. Full positive set for
the sweep: **myperfectresume, zety, resume-io, phrasly, shortsfaceless**, plus `elevenlabs` (see §2).

Three notes on the candidate list itself, none of which changes a classification:

- `pass1/undetectable-ai` states that "the literal token is deliberately omitted" — in a sentence
  containing the token. It is the clearest single illustration of why string matching could not
  produce this list.
- `pass1/openai-sora` is a NEGATIVE on the A-012 question, but its trial variables are `unknown`
  for an unrelated reason: the product is discontinued and its pricing and documentation classes
  could not be recovered, so rule 3's test for coding `no` was never met. This rule does not
  reach it.
- The token also appears in `pass1/phrasly-sources/terms-of-service.txt` — a coder's annotation
  inside a source capture, not a record and not the vendor's text. A naive `grep -rl` over
  `records/` returns it as an eighteenth path.

### 1.1 The token list has false negatives too, not only false positives

The queue documented the false positives. It did not know about the other direction.

**`pass1/elevenlabs` observed the construct and carries no token.** Its own `coder_note` quotes its
own saved capture: "Creator $22 (121,000 credits, **$11 for the first month**)". Its `trial_exists`
evidence nonetheless reads "No time-limited trial is described anywhere". Pass 2 flagged the same
figure explicitly under A-012; the adjudicator saw both and left the question to this sweep. So the
mechanism failed in both directions on a single product.

The reason is datable. All seventeen tokened records were collected on or after **2026-08-10**, the
day `myperfectresume` originated the item; `pass1/elevenlabs` was collected **2026-08-06**. The token
instruction lived in the coder agents' spawn prompt, not in the frozen instrument and not even in
`deviations-for-coders.md`, whose "Known open questions" section asks for a plain prose description
of the intro period and never mentions a token. **44 of the 76 pass-1 records were collected before
the item existed** and could not have carried it. Of the 32 collected on or after 2026-08-10, 17
recorded a check either way; the other 15 recorded nothing, so their silence is also uninformative.

Affirmative coverage from the token is therefore 17 of 76 records. The corpus-wide claim in this
document rests on a separate sweep of all 126 record files for intro-period language
(`first month`, `introductory`, `then $`, `limited-time`, `promo price`, `day access`, and
variants), which surfaced `pass1/elevenlabs` and nothing else new. **That sweep is itself a pattern
search and inherits the weakness this item is about**; it is a second net, not a proof of
completeness, and the paper should say so.

---

## 2. The rule

> **`trial_exists` asks whether the vendor documents a time-limited pre-commitment period of access
> to a paid tier. Zero cost is the paradigm case named in the definition, not a condition of the
> construct: a non-zero intro price does not remove the period from Domain 4. The period must end
> before the plan's first ordinary billing cycle completes; a discount applied to the first full
> cycle of a standing plan is a promotional price, not a trial, and stays out of Domain 4.**

Five arguments from the instrument's own text.

**The word "free" is the only word in the definition with no operative consequence anywhere.**
"Free" occurs three times in the entire codebook: in this definition, in `free_plan_exists` rule 1,
and inside a worked example in §5.2. No decision rule, no sub-variable and no scoring clause in the
codebook or in `protocol-v1.md` §8.3.3 turns on the trial's price being zero. "Time-limited", "of a
paid tier" and "documents" each do work in several places. A term that carries no consequence
anywhere in an instrument is describing the paradigm case, not stating a condition.

**Domain 4's own title carries no zero-cost requirement.** §9 titles the domain "Whether a trial
requires a payment card". A paid intro period is the maximal case of that question: the card is not
merely required, it is charged.

**The Domain 3 / Domain 4 boundary is drawn on time-limitedness, not price.** `free_plan_exists`
defines a free plan as "usable at no cost **and with no time limit imposed by a trial**", and its
rule 1 routes a time-limited free trial into Domain 4. Both constructs are free; what separates them
is the time limit. A paid intro period fails Domain 3 on both prongs and is excluded from Domain 4
by none of `trial_exists`'s four rules — rules 1 and 2 exclude only free plans and money-back
guarantees, each routed to a domain that does cover them. **No domain catches a paid intro period if
Domain 4 does not.**

**Rule 3, the only path to `no`, has a false antecedent on three of the four positives.** It reads:
"Where the pricing page and the documentation mention no trial, code `no`." Zety's pricing page
prints "With a 14 day trial for: $1.70". Resume.io's documents say "7-day Trial", "premium trial",
"7-day trial subscription". Phrasly's ToS §6 is headed "TRIAL" and grants "a 3-day trial ('Trial
Period')". For those three the antecedent is factually false and the rule cannot fire.
MyPerfectResume's documents never use the word (0 hits across 113,851 characters). So a
vocabulary-keyed reading would code four vendors selling one mechanism two different ways — and
would score the vendor that avoided the word **higher** than the three that used it. A transparency
index cannot reward a vendor for not naming the thing. The rule must key on the mechanism.

**The instrument already distinguishes a promotional plan from a promotional price, and already
excludes the former from the price domain.** `sampling-rules.md` §7.2 eligibility rule 3 requires
"a standing plan rather than a limited-time promotional plan". Every positive record applied it and
removed the teaser from entry-tier candidacy. That exclusion is protective: it stops a teaser being
mistaken for an ongoing price. Reading Domain 4 to exclude the same object is not the parallel move,
because it runs the other way — it removes the vendor's most prominent number from the instrument
altogether. And a coder with no stake in this item drew exactly the line drawn here:
`pass1/aragon-ai` records its packages as "not limited-time promotional plans in themselves; only
the '20% off' discount is framed as time-limited, per rule 3's plan-vs-price distinction."

### 2.1 Where the boundary falls, and why it is mechanical

The rule's second sentence turns on one published fact: **is the intro window shorter than the
plan's first ordinary billing cycle?**

| Record | Window | Cycle it converts into | In Domain 4? |
|---|---|---|---|
| myperfectresume | 14 days | every 4 weeks | yes — window < cycle |
| zety | 14 days | every 4 weeks | yes |
| resume-io | 7 days | every 4 weeks | yes |
| phrasly | 3 days | per month, billed annually | yes |
| shortsfaceless | first month | monthly | no — window = cycle |
| elevenlabs (Creator) | first month | monthly | no — window = cycle |

A trial is a period that ends **before** the buyer's first full commitment period, so a decision
point arrives before the ordinary billing rhythm begins. That is precisely why the card question
exists: a short window closes before any ordinary charge would fall due, so the vendor needs a card
on file to capture the conversion. A first-cycle discount has no such decision point — the buyer is
already on the plan, at the plan's own cadence, paying less for cycle one, and her steady state is
the standing price published on the card she compared.

This test was not fitted to the four positives. Applied to the whole corpus it also correctly
excludes a third pattern the wider sweep found and no coder tagged: a time-limited promotional
**price** on a standing plan, running for months or a first year — hailuo-ai ("$14.99/month,
limited-time offer at $7.99. The price will return to $14.99 after the promotion period"), lovo-ai
("1st Year 50% OFF" off a $48/mo standing rate), adobe-firefly ("Save 30%. First year only."),
aragon-ai ("20% off all packages limited time only!"). None is a pre-commitment access window; all
were correctly left out of Domain 4.

### 2.2 What follows for the other three trial variables on a positive record

- **`trial_card_required`** — its own rule 3 governs unchanged: "The absence of any statement is
  `unknown`. Do not infer…". The codebook's worked example rejects this exact inferential chain —
  automatic conversion implies stored payment details, "but implication is not a statement". A
  stated non-zero start price is the same species of implication: it establishes that money moves,
  not that the vendor stated a card is required. **`unknown` unless a document says it.**
- **`trial_length_days`** — the integer the vendor publishes. Where the product documents exactly
  one intro period and it sits on a non-entry candidate, §5.2's entry-tier scoping does not license
  `not_applicable`: that value asserts documented absence (§2.2), and `protocol-v1.md` §8.3.3 names
  `trial_exists = yes` with `trial_length_days = not_applicable` an unreachable pair "returned for
  re-coding". §5.2's scoping exists to disambiguate between several tier-specific trials, a case
  that does not arise on any positive record.
- **`trial_auto_converts`** — `yes` where the documents state conversion, `unknown` where they do
  not. Descriptive; no index item.

### 2.3 The reading rejected, and the reading nearly adopted

**`no` is rejected** because it would put a false statement in the published dataset — that the
vendor documents no time-limited trial, on records whose own pricing pages print the word "trial"
next to a price — and would pay the vendor full marks for it.

**`unknown` was seriously considered and rejected.** Its definition is "No official document states
a determinate value … The buyer cannot determine this before paying." On these records the documents
are unusually explicit: price, window, and converted rate are all published, three of the four on
the pricing page itself. `unknown` is this study's central quantity; inflating it with a case of full
disclosure would corrupt the headline number in the vendor-adverse direction, which is the mirror
image of the defect in `no`. The A-011 precedent for coding a published fact `unknown` does not
transfer: there the **value list** had no slot for a quarterly cadence and every available value
would have misstated the cadence. Here a value is available and states the mechanism correctly.

**The residual cost of `yes`, stated plainly:** the coded value carries the word "free" in its
definition and these periods are not free. That is a real imprecision. It is contained because each
record's `evidence` field states the price in full and the four variables together make the
mechanism legible — but a reader of the dataset must not read `trial_exists = yes` as "free" on
these five records, and the paper must say so where it reports Domain 4.

---

## 3. Per-record consequence

**No record is edited by this document.** Corrections are applied later as one batch under this rule.

### Positive, rule applies — `trial_exists = yes`

| Record | `trial_exists` | `trial_card_required` | `trial_length_days` | `trial_auto_converts` |
|---|---|---|---|---|
| `pass1/myperfectresume` | `yes` — holds | **`unknown` — CHANGES from `yes`** | `14` — holds | `yes` — holds |
| `pass1/zety` | `yes` — holds | `unknown` — holds | `14` — holds | `yes` — holds |
| `pass1/resume-io` | `yes` — holds | `unknown` — holds | **`7` — CHANGES from `not_applicable`** | `yes` — holds |
| `pass1/phrasly` | `yes` — holds | `unknown` — holds | `3` — holds | `yes` — holds |

**Two variable-level corrections, in two records.**

- **myperfectresume `trial_card_required` `yes` → `unknown`.** The coder inferred a card from the
  $2.95 charge and said so: "a real, non-zero, immediate charge necessarily requires payment
  details." Rule 3 bars the inference. **Direction: this costs the vendor 2 points on B3** (5 → 3).
  It is raised with the same care an owner-favourable correction would get.
- **resume-io `trial_length_days` `not_applicable` → `7`.** The record currently holds the exact
  combination §8.3.3 declares unreachable and returns for re-coding, so it has no valid B3 score
  until corrected. Rule G4 taken alone would count the `not_applicable` as determinate and compute 3,
  the same figure the corrected record earns, so **this correction is not made for the score** — it
  removes an invalid state, which is reason enough.

Zety and phrasly need no correction: both coders reached this rule independently, zety citing rule
3's false antecedent and the §8.3.3 impossible pair by name.

### Positive-shaped, rule does not apply — `trial_exists = no` stands

| Record | Construct | Verdict |
|---|---|---|
| `pass1/shortsfaceless`, `pass2/shortsfaceless` | `/deal`: "50% OFF FIRST MONTH", "$19" struck to "$9", "Get this special deal for the first month" | `no` holds; all three sub-variables `not_applicable` hold. Both passes already coded it this way. |
| `pass1/elevenlabs`, `pass2/elevenlabs`, `adjudicated/elevenlabs` | Creator: "First month 50% off" → $11, then the $22 standing rate; non-entry tier | `no` holds; all three sub-variables `not_applicable` hold. The adjudicated row's scope note explicitly deferred this here and is now answered. |

Two further boundary calls, both leaving the record as coded:

- **vidnoz** carries a rendered "25% OFF First Month" badge that describes nothing: under the
  monthly toggle its struck and shown prices are identical ($26.99 = $26.99), no "then $X" or "after
  first month" language exists anywhere on the page, and the refund policy documents annual billing
  as a single yearly deduction. Intro-period vocabulary without an intro-period mechanism.
  **NEGATIVE stands.**
- **d-id** publishes "Unlimited videos for your first month!" — a first-month **allowance**
  promotion at an unchanged price, correctly coded under `usage_cap_quantified`, not Domain 4.

**A-015's cross-reference is answered in the negative.** winston-ai's "2,000 credits / 14 day trial"
carries no non-zero price; it is a free construct and this rule has no bearing on it. A-015(a) must
be resolved on its own terms.

---

## 4. The scoring consequence, stated plainly

`protocol-v1.md` §8.3.3, item B3, worth 5 points: `trial_exists = no` scores **5**. `trial_exists =
yes` with both `trial_card_required` and `trial_length_days` determinate scores **5**; with one of
the two, **3**; with neither, **0**. `unknown` scores **0**.

**The literal reading would have given four vendors full marks for "documented absence of a trial"
while they sell a paid teaser that converts to between 1.8 and 4.4 times their own cheapest
published annual rate. This rule does not produce that outcome.** Under it the four score **3 of 5**
on B3 — `trial_exists = yes`, length determinate, card `unknown` — instead of 5 of 5.

Three further effects a reader is entitled to see named.

**The 2-point loss arrives partly by artifact.** `trial_card_required` lands on `unknown` only
because rule 3 bars inference from a charge, and it is that `unknown` that costs the 2 points. The
buyer plainly must supply a card to be charged $2.95. The instrument declines to record what it
cannot quote, which is the right general policy and produces a slightly accidental score here.

**A vendor with no trial at all still scores higher than these four**, 5 against 3. That is correct
on B3's own terms — there are no trial terms to fail to disclose — and it is worth stating because
it shows what B3 measures. **B3 cannot register the paid-teaser mechanism under any of its values.**
A vendor that sold the identical teaser and printed "credit card required" would score the full 5.
The mechanism is a friction finding; B3 is an item about determinability. Choosing `yes` over `no`
stops the index paying a bonus for concealment; it does not make the index able to see the
construct. Only a new coded variable can (§6).

**This rule is generous to the two Species-B vendors, and the generosity should be visible.**
shortsfaceless and elevenlabs keep 5 of 5 on B3. For elevenlabs the promo sits on a non-entry tier
and nothing about the entry tier's terms is affected. For shortsfaceless the case is weaker than the
rule's clean line suggests: **no document anywhere states what the buyer pays in month two.** That
is a genuine disclosure gap and this rule sends it out of Domain 4 without sending it anywhere else.
Its natural home is the A-domain — the same record codes `first_charge_amount_usd` as $19.00 while a
buyer arriving through the vendor's own footer-linked `/deal` page is first charged $9. That is
licensed by §7.2 rule 3 and is not corrected here, but it is the one place where this rule leaves a
real finding unrecorded, and it belongs in the limitations.

---

## 5. A finding for the paper

**The teaser is not a discount. It is a routing device into the vendor's most expensive cadence.**

In **4 of 4** cases where the rule applies, the rate the intro period converts to is higher — by a
wide margin — than the cheapest annual-equivalent the same vendor publishes on the same page.

| Record | Teaser | Window | Converts to | Converted, annualised | Vendor's own cheapest annual-equivalent | Ratio |
|---|---|---|---|---|---|---|
| zety | $1.70 | 14 days | $23.95 / 4 weeks | $311.35 | $71.40 (Annual Package) | **4.36×** |
| myperfectresume | $2.95 | 14 days | $23.95 / 4 weeks | $311.35 | $95.40 (1-Year Premium Access) | **3.26×** |
| resume-io | $2.95 | 7 days | $29.95 / 4 weeks | $389.35 | $199.80 (Quarterly) | **1.95×** |
| phrasly | $2.00 | 3 days | TRY 953.90 / mo billed annually | TRY 11,446.80 | TRY 6,293.16 (Unlimited) | **1.82×** |

**Spread 1.8×–4.4×, median 2.6×.** Figures are the records' own; annualisation uses 13 four-week
periods, the convention the records adopted (365/28 moves the first three ratios by ≤0.01).
Phrasly's ratio is currency-independent — both figures are TRY from one page on one read — and so
survives that record's `headline_price_usd` being `unknown`.

Three things sharpen it.

**Phrasly's ratio is the only like-for-like one, and it is the cleanest evidence.** Its two paths
share an identical cadence — both "per month, billed annually" — so its 1.82× cannot be attributed
to an annual-prepay discount. The other three compare a 4-weekly rate against an annual or quarterly
prepay, where some of the gap is the ordinary prepay discount. **That caveat does not deflate the
finding**, because in each of those three the vendor publishes no ordinary monthly plan at all: the
teaser is the only entrance to the 4-weekly cadence, and the annual prepay is the only alternative.
The cadence difference is not a confound. It is the trap.

**Measured as a daily rate, two of the four teasers are barely discounted and one is not discounted
at all.** Teaser price per day against converted price per day: zety 0.14, myperfectresume 0.25,
resume-io 0.39, **phrasly 1.02**. Phrasly's "$2.00 for 3 Day Access" is its full converted rate
prorated to three days, wrapped as a teaser. What is cheap about these offers is the absolute
number, not the rate — which is exactly the property a headline-price transparency audit is built to
detect.

**Two of the four are the same vendor family and publish an identical converted rate.** Zety's ToS
names "BOLD LLC" as the contracting party; MyPerfectResume's ToS governs the Bold.pro profile
product. Both convert to **$23.95 every 4 weeks** off different teasers ($1.70 and $2.95). The
teaser is the variable; the destination is the constant. Two records is an observation, not a
category claim, and it should be reported as one.

**Category concentration.** Three of the four sit in one stratum: 3 of the 6 AI-resume-builder
records in the frame sell the construct (myperfectresume, resume-io, zety), and the other 3
(jobscan, rezi, teal) document none. The fourth is an AI humanizer. Corpus-wide the construct
appears on 4 of 76 pass-1 records; within resume builders, on half of them. Given §1.1's coverage
limits the 4/76 figure is a floor, not an estimate.

**One reliability note that belongs beside the finding.** None of the four positive records is in the
double-coded subset, so the divergence in how primary coders treated this construct — four coding
`yes`, one coding `no` on shortsfaceless — cannot appear in the §7.6 agreement statistic at all.
Where the construct *is* double-coded, shortsfaceless, both coders agreed on the value this rule
overrides. `protocol-v1.md` §7.4 step 3 already says why that is not an objection: "agreement
between them is not evidence of correctness."

---

## 6. What wave 2 must change

The queue is right that the mechanism was wrong, and §1.1 locates the fault more precisely than
"a token in prose": the token lived in the coder agents' spawn prompt, so it could not reach the 44
records collected before the item existed, and the coder-facing `deviations-for-coders.md` never
mentioned it. Wave 2 should carry a **coded variable, `intro_period_present`** (`yes` / `no` /
`unknown` / `conflicting`), with four dependents — `intro_period_price_usd`,
`intro_period_length_days`, `intro_period_converts_to_usd` and `intro_period_cadence` — sitting in
Domain 4 beside the trial variables and gating them, so that a paid teaser is measured as itself
rather than borrowed into a variable defined as free. Because it is a coded field it is coded on
every record, its absence is a value rather than a silence, `validate_records.py` enforces it, and
`unknown` scores as a disclosure failure the way the rest of the instrument does. Wave 2's
`trial_exists` should then say "free" and mean it, with an explicit cross-reference to the new
variable, and its rule 3 should test for a **free** trial rather than for the word "trial" — the
defect that made three of these four records unreachable by their own decision rule. The mapping
back to wave 1 (codebook §11) is: wave-1 `trial_exists = yes` on these five records maps to wave-2
`trial_exists = no` **plus** `intro_period_present = yes`.

---

## 7. Owner review

The rule in §2 is the substantive choice; §2.1's window-versus-cycle boundary is the part most open
to disagreement, and overturning it in the permissive direction would move shortsfaceless and
elevenlabs to `yes` and cost each 2 points on B3. §4's disclosure of where the rule is generous is
written so that choice can be made on the merits. The two corrections in §3 are the only record
edits this document implies, they are named with their direction, and they are not applied here.
