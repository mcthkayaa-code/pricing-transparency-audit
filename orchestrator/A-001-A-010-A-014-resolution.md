# A-001, A-010 and A-014 — which purchasable thing is the entry tier

**Resolved 2026-08-17 by an adjudicator working across three records under delegated authority.**

These three items were grouped because they are one question asked at three vendors: *which purchasable
thing is this product's entry paid tier?* They are the widest-reaching open items in the study because
the answer is the antecedent of every variable the codebook defines relative to that tier.

They are governed by `orchestrator/A-013-A-019-resolution.md`, whose test is:

> A variable asks what a reasonably diligent reader of the vendor's published documents can obtain, from
> any standard reading position, without inspecting page internals.

**Summary of the three rulings**

| Item | Product | Ruling | Coded values changed |
|---|---|---|---|
| A-001 | canva | Entry tier is **Pro**, determinable. The item's premise no longer holds. | **0** |
| A-010 | humanizemy-ai-detector | Entry tier is **Basic**. The vocabulary split is right evidence applied to the wrong variable. | **3** |
| A-014 | rezi | §7.2's pricing-page anchor **holds**. Entry tier is **Pro**. The divergence is a finding. | **0** |

**Total coded values that would change: three, all on one record.**

---

## Disclosures, made first because they bear on how much weight these rulings carry

**I read the adjudication queue, three products' records, and one product's adjudicated record.**
`deviations-for-adjudicators.md` puts all four off limits, for the good reason that an adjudicator who
knows another product's values may resolve a close call toward cross-product consistency rather than
toward this vendor's documents. I read them because the assignment directed me to, and because two of
these items cannot be stated without them: A-010's whole question is what relationship this record
should have to its sibling's, and A-014's second question asks whether other products in the frame show
the same pattern. Neither is answerable from one record.

**One ruling is materially exposed by this.** On A-010 I saw the sibling's `output_ownership_statement`
value **before** I read the shared Terms of Service in the detector record's own source file. I then
verified the clause independently in `records/pass1/humanizemy-ai-detector-sources/terms-clean.txt` and
found that it names `/detect` on its face — a fact that decides the variable whichever record you come
to it from. But I cannot claim the reading was uninfluenced, and a reader should discount it
accordingly. The two variables where I reach a value the sibling also carries are flagged in place.

**I verified A-014's disputed quotations myself, live, on 2026-08-17**, rather than resting on the
record's account of them. Results are in that section. Archive replay returned HTTP 503 on the one
capture I tried, consistent with the outage the retrieval sweeps recorded.

**Provenance of this file, because the history does not read cleanly.** A concurrent session committed
this document, mid-draft, inside its own commit `193c564` ("D-052: A-020 recoded…"), which is the
unscoped-commit hazard `deviations-for-adjudicators.md` records as having "twice shipped one agent's work
inside another's commit". Nothing was lost and nothing of that session's work was disturbed. The version
in `193c564` is this file two edits short of finished; the completing commit is scoped to this path
alone. Anyone auditing when this resolution was written should read the later commit, not `193c564`.

---

## The cascade set, stated once for all three items

The assignment asked for the full cascade, on the premise that "roughly twenty variables" are defined
relative to the entry tier. **That figure is not what the instrument says, and the discrepancy matters
enough to correct before any of the three rulings is applied.**

`codebook-v1.md` §5.2 enumerates the entry-tier variables, and it was written precisely because "a rule
that turns on 'every entry-tier variable' is not executable until the set is written down":

> **The entry-tier variables are `first_charge_amount_usd`, `mandatory_addon_present`,
> `usage_cap_quantified`, `cost_per_output_computable`, `trial_length_days`, and `refund_window_days`.**

Six. §5.2 then adds `headline_price_usd` ("names the entry tier's price and is governed separately") and
expressly **excludes** the document-describing variables: "`annual_condition_disclosure`,
`annual_default_toggle`, `refund_policy_exists`, `auto_renewal_default` and the rest — are not
entry-tier variables, and nothing here changes how they are coded."

**The authoritative cascade set is ten coded variables:**

| # | Variable | Basis |
|---|---|---|
| 1 | `entry_tier_name` | The selection itself (codebook §6) |
| 2 | `headline_price_usd` | §5.2, governed separately |
| 3 | `headline_billing_basis` | "What the headline figure represents" — the headline figure is the tier's |
| 4 | `first_charge_amount_usd` | §5.2 |
| 5 | `mandatory_addon_present` | §5.2 |
| 6 | `usage_cap_quantified` | §5.2 |
| 7 | `cost_per_output_computable` | §5.2 |
| 8 | `computation_assumptions` | Records the arithmetic the tier price feeds |
| 9 | `trial_length_days` | §5.2 |
| 10 | `refund_window_days` | §5.2 |

Plus, derived and computed after freeze: `headline_vs_first_charge_gap_ratio`,
`cost_per_output_value_usd`, and the fourteen `apti_*` / `unknown_count` / `determinability_rate` values,
which move whenever any of the ten does.

**`cost_per_output_unit` is not in the set.** Its definition is "this product's principal output", a
product property. It is tier-*sensitive* in practice — a coder reads the entry tier's card to see what
is being sold — but a change of tier within one product does not change it.

**Where the "nineteen" came from, and why it should not be reused.** Queue item A-016 states that
google-veo's twenty `unknown` values are "one … tier question and 19 [that] cascade from it as their
antecedent", and asks the analysis to apply the APTI guard on that basis. The adjudicated record carries
**twenty-two** `unknown` coded values. Of those, six are in the cascade set above
(`headline_price_usd`, `headline_billing_basis`, `first_charge_amount_usd`, `trial_length_days`,
`cost_per_output_computable`, `usage_cap_quantified`). The other sixteen — `annual_default_toggle`,
`trial_exists`, `trial_card_required`, `trial_auto_converts`, the four credit variables,
`cost_per_output_unit`, `credit_rollover_policy`, `failed_generation_charge_policy`, the three
auto-renewal variables, `commercial_use_lowest_tier`, `unquantified_limit_clause` — are not defined
relative to the entry tier by any rule in the instrument.

A-016's *substance* survives this: those sixteen plausibly share a different single antecedent, namely
that the adjudicator could not establish **which vendor surface the product is sold on**, and the credit
system, trial and renewal terms differ between the two candidate surfaces. That is a real
common-antecedent argument and the guard should be applied to it. But it is not the tier question, and
stating it as "19 variables defined relative to the entry tier" invites the analysis to discount
nineteen unknowns on an authority the codebook does not give. **The guard should be applied to
whichever unknowns actually share an antecedent on the record, named individually, and the number
should not be inherited from A-016's row.** Direction: this correction makes the study's unknown burden
*larger* than A-016 implies, so it tells against the vendor.

---

## A-001 — canva

### 1. The rule that decides it

`sampling-rules.md` §7.2, price basis:

> Among the eligible candidates, the **entry paid tier** is the one with the **lowest annual-equivalent
> cost of a single seat, computed in the pricing page's default display state**.

and rule 2:

> **Annualize whatever that state shows.** A monthly figure is multiplied by 12. An annual figure is
> taken as it stands.

**The rule is currency-agnostic.** It says "lowest annual-equivalent cost", not "lowest USD cost", and
rule 2 says "whatever that state shows". `protocol-v1.md` §6.5 — the only place currency is regulated —
governs how a **money variable** is coded ("Reporting currency is USD… We do not invent an exchange
rate"). It says nothing about the comparison that selects a plan, and it does not need to: a comparison
between two figures in one currency, on one period, for one seat requires no exchange rate at all.

### 2. Ruling

**The entry paid tier is Pro. It is determinable, and it always was on this record's evidence.**

**A-001's premise does not survive its own record.** The item was raised against a state of the record
in which no price had been read at all — the note it produced reads "entry_tier_name = unknown …
flagged as an instrument-gap case, both Pro and Business unpriced". The D-005 re-collection replaced
that state. The record now reads both candidates in the pricing page's default display state, both
already captioned as annual per-person totals so rule 2's multiplication is not even needed: **Pro
₺1,920/yr against Business ₺3,400/yr**, with Free at ₺0 (not a paid tier), Enterprise sales-gated
(fails eligibility criterion 2) and the Education tab a named program (fails criterion 1). One eligible
candidate lost, and it is recorded with its figure as §7.2's recording clause requires. That is a
complete, executed §7.2 selection.

**The selection is reproducible even though the currency is not**, which is the point A-001 was really
worried about. `orchestrator/post-window-retrieval-2.md` fetched the `es_us` locale path — the one
United-States-country locale among the page's 105 hreflang alternates — and found ₺0 / ₺1,920 / ₺3,400,
the same three figures in the same order. So the *ordering* of the candidates held across a second,
independently chosen reading position while the *denomination* did not. Under the A-013 test, what a
reasonably diligent reader can obtain from any standard reading position includes "Pro is the cheaper
of the two eligible plans". That is the whole of what §7.2 asks.

**What actually fails here is narrower than the item claims, and it is already labelled.** Canva
publishes prices; it publishes a USD figure for the AI Pass add-on in its own help centre; what it does
not do is expose a USD *plan* price to a reader outside the United States, and D-007's test asks what
"a US reader" is served while the protocol supplies no executable route to occupy that position —
currency selection is IP-bound and no locale path, URL parameter or request header overrides it. The
second post-window sweep reclassified both money values from `access_failure` to `instrument_gap` on
exactly that ground, and those rows are in `unknown-attribution-overrides.csv`. **The instrument gap is
in the currency test, not in the tier rule.** A-001 conflated the two, and separating them is the
resolution: one variable class is defeated, ten are not.

### 3. Variables that change

**None. Zero coded values.** Verified against the record field by field:

| Cascade variable | Value | Changes? |
|---|---|---|
| `entry_tier_name` | `Pro` | No — confirmed under §7.2 |
| `headline_price_usd` | `unknown` (`instrument_gap`) | No — A-013's `unknown` arm, not `non_usd`, because the vendor's own help article makes served currency geography-dependent and names USD as the fallback |
| `headline_billing_basis` | `unknown` | No — this is A-009's separate instrument gap (an annual per-seat total fits none of the four recurring bases), not a tier question |
| `first_charge_amount_usd` | `unknown` (`instrument_gap`) | No — cascades from `headline_price_usd` |
| `mandatory_addon_present` | `no` | No |
| `usage_cap_quantified` | `some_quantified` | No — coded for Pro specifically |
| `cost_per_output_computable` | `yes` | No |
| `computation_assumptions` | ₺1,920/yr → ₺160.00/month | No |
| `trial_length_days` | `unknown` | No |
| `refund_window_days` | `0` | No |

**One derived-variable defect the enumeration surfaced, which is not an A-001 question but is a
consequence of this chain and has no rule.** `cost_per_output_computable = yes` is correct on its own
definition — every figure is published, the arithmetic needs no assumption, and the variable is not
denominated in USD. But the derived variable it feeds is: `cost_per_output_value_usd`, computed "only
where `cost_per_output_computable` is `yes`". For canva the only arithmetic available is
**₺160.00/seat-month**. Writing that into a field named `_usd` would state a TRY number as a USD one;
inventing a rate is forbidden by §6.5.

§6.5's protection does not reach this case: it excludes **`non_usd`** records from monetary aggregates,
and canva's money values are `unknown`. **Four records are in this state** — `pass1/canva`
(₺160.00/mo), `pass1/gptzero` (₺549/mo, ₺0.00183/word), `pass1/phrasly` (₺524.43/mo) and
`pass1/picsart` (₺83.25/mo) — all four with `unknown` money variables, so all four pass through the
`non_usd` filter. A fifth, `pass2/aiva` (€11/mo, €0.73/track), is genuinely `non_usd` and is caught.

**Recommended computation rule for wave 1:** `cost_per_output_value_usd` is `not_computable` wherever
the only available arithmetic is denominated in a currency other than USD, whatever the money
variables are coded, with the figure and its currency kept in `computation_assumptions`. This is an
instruction for the post-freeze computation under codebook §8, **not** a coded value and **not** a
codebook change, so it does not touch the §11 freeze. It should be applied to all five records at once
or to none.

### 4. Direction

**This ruling decreases the study's unknown burden relative to the alternative, and it favours the
vendor.** Stated plainly, and counted rather than asserted: the cascade set at canva currently holds
four `unknown` values (`headline_price_usd`, `headline_billing_basis`, `first_charge_amount_usd`,
`trial_length_days`). Had the tier been ruled undeterminable under §7.4 step 5, **five further coded
values would have become `unknown`** — `mandatory_addon_present` (`no`), `usage_cap_quantified`
(`some_quantified`), `cost_per_output_computable` (`yes`), `refund_window_days` (`0`), and
`entry_tier_name` itself against its own value table — with `computation_assumptions` falling to
`not_applicable`. Had §7.3 been reached instead, items A1, A2 and A3 would have left the index
together. Ruling the tier determinable forgoes all of that. It is the vendor-favourable outcome and I
reached it because §7.2 decides it, not because it is cheaper.

**One count moves against the vendor, in the same breath.** The correction to the "nineteen" figure
above means fewer unknowns can be discounted as cascades than the queue implied, at canva and at
google-veo both. That tells against the vendors, and it is raised with the same care as the ruling that
helps them.

**The unknown that remains is ours, and the record should say so.** The two money values are
`instrument_gap`, which is the honest label — but the gap is that this study's collection host sits in
Turkey and its own protocol asks a question about a reader in the United States. A reader is entitled
to see that named as a limitation of our design rather than as a fact about Canva's disclosure.

### 5. What the sampling rules and codebook should say in wave 2 and do not

- **§7.2 should state that the tier comparison is currency-agnostic** and that a comparison between two
  figures in one currency, on one period, for one seat is valid even where no USD figure exists. Two
  coders reading §7.2 alongside §6.5's "Reporting currency is USD" can reasonably conclude the
  selection needs a USD figure. This record's first pass concluded exactly that.
- **The codebook should carry the non-USD derived-value rule** recommended above, so that
  `cost_per_output_value_usd` cannot receive a foreign-currency number.
- **A-001's real content should be retired into the currency limitation.** There is no
  "eligible tiers exist but no price is documented anywhere" case in this corpus. The case that exists
  is "the price is documented, and our protocol asks about a reading position we cannot occupy", and
  wave 2's fix is the second currency variable A-013's resolution already proposes — plus a collection
  design that can occupy a US position, without which the D-007 test stays unexecutable.
- **A-009's gap is confirmed by this record from a second direction** and should be fixed with A-011's:
  the recurring-basis enum needs an annual-per-seat-total value.

---

## A-010 — humanizemy-ai-detector

Two questions: (a) is `entry_tier_name = Basic` right for a benefit that is bundled and not standalone;
(b) is the vocabulary-based split the right line for keeping the sibling's numeric caps off this record.

### 1. The rules that decide it

**On (a),** three rules, and they close the question between them.

`sampling-rules.md` §7.1:

> The unit of analysis is the **product**, not the plan and not the vendor. A vendor selling two
> products in our portfolio yields two records.

`sampling-rules.md` §7.2, eligibility — the complete list:

> A plan is a candidate for the entry paid tier when it satisfies all of: 1. Generally available to any
> buyer… 2. Purchasable without contacting sales. 3. A standing plan rather than a limited-time
> promotional plan. 4. Where plans scale by seat, the single-seat variant. 5. Where the vendor publishes
> only usage-based pricing, the smallest published package or the published unit rate.

`sampling-rules.md` §7.3:

> Where a product has **no paid tier at all and states so**, entry-tier variables are coded
> `not_applicable`.

**On (b),** the scoping clause in codebook §5.2 and the two variables' own first rules.

§5.2:

> Six coded variables take their value **for the entry paid tier** … **rather than for the product as a
> whole.**

`usage_cap_quantified`, definition and rule 1:

> **Definition.** Whether the limits attached to the **entry paid tier** carry published numbers.
> 1. List every limit the documents attribute to the **entry paid tier**.

`cost_per_output_computable`, rule 1:

> **The price input is fixed.** It is the **entry paid tier's price**…

### 2. Ruling

**(a) `entry_tier_name = Basic` is right, and it is the only admissible value.**

§7.2's eligibility list contains **no exclusivity requirement**. It asks whether a plan is generally
available, self-serve, standing, and single-seat. Basic, Pro and Ultra are all four; Basic wins the
price basis at $144.00/yr against $216.00 and $432.00. The two carve-outs that do adjust for how a plan
is packaged — rule 4 for seat-scaling and rule 5 for usage-only pricing — address packaging *within* a
product, not bundling *across* products. Reading an exclusivity requirement into the list at
adjudication would be legislating, not applying.

**`not_applicable` is unavailable** because §7.3's antecedent is not satisfied. Its test is "no paid
tier at all **and states so**". Here a paid tier exists and the vendor documents the detector as one of
its contents: all three cards carry "AI detection checks" as a separately checked feature line, and the
record establishes from raw HTML that these are genuine tier-differentiating grants rather than
decorative recaps — "Priority support" is crossed out on Basic while "AI detection checks" is checked on
all three. That is affirmative documentation of a paid detector benefit. It is *not* affirmative
documentation that no paid tier exists.

**`unknown` is unavailable** because `entry_tier_name`'s own value table scopes it to one case:
"`unknown` where the only paid option is gated behind a sales contact and no plan name is published for
it, which is the section 5.2 case". These plans are self-serve and named.

**The record's own contractual coding independently forces the same answer.** It codes
`auto_renewal_default`, `refund_policy_exists`, `refund_conditions`, `cancellation_self_serve` and both
disclosure-location variables from the shared subscription contract, on the stated reasoning that "a
buyer purchasing Basic/Pro/Ultra for the detector benefit is bound by the same single subscription
contract". A record cannot coherently hold that a buyer of this product's paid tier is bound by that
contract *and* that this product has no paid tier. `deviations-for-adjudicators.md` notes that a
record's neighbouring values constrain it; here they cohere with Basic and only with Basic.

**(b) The vocabulary split is sound evidence, and it was applied to the wrong variable. It changes one
value and leaves the other standing — and the asymmetry is a rule, not a compromise.**

The split does real work. `/detect` and `/cookies` meter the detector in "scans"; `/pricing` and
`/terms` meter in "requests" / "humanizations" / "runs", tracing to the free humanizer's own documented
"4 humanizations per day, up to 125 words per run"; and `/pricing`'s own detection FAQ distinguishes the
humanizer's internal pattern scanner from "the free /detect page [which] adds a trained model on top".
On that evidence the record is right that **no number is published for what "AI detection checks" grants
a paid subscriber**, and right that `/detect`'s "Paid plans raise that ceiling" supplies none.

Where it goes wrong is in what it did with the finding: it **deleted the quantified bullets from the
list** rather than recording them alongside the unquantified one.

**`usage_cap_quantified` → `some_quantified`.** This variable is scoped to the **tier**, and §5.2 says
so in terms — "for the entry paid tier … rather than for the product as a whole" — with rule 1
repeating it: "every limit the documents attribute to the entry paid tier". Basic's documented limits
are "80 requests / month" (a quantified rate), "Up to 1,000 words per request" (a quantified standing
limit) and "AI detection checks" (no number). That is the definition of `some_quantified`: "At least one
limit is quantified and at least one is not." `none_quantified` means "Limits are stated without
numbers", which is not true of the Basic card. Nothing is *borrowed* by coding it this way — the unit
of the variable is the tier, and both bullets are on the same card of the same tier. And the resulting
value states the buyer's actual position better than either alternative: she can size part of what she
is paying for, and not the part she came for.

**`cost_per_output_computable` → stays `no`.** Here §5.2's tier-scoping reaches only the **numerator**,
because that is all rule 1 claims: "The price input is fixed. It is the entry paid tier's price."
The denominator comes from `cost_per_output_unit`, which is a **product**-level variable — "this
product's principal output" — coded `other`, "per scan". So the calculation needs the tier price ($12/mo,
published) and the detector's paid allowance (unpublished). Rule 6 returns `no`.

Rule 5's `partial` does **not** rescue it. Its case is "the calculation is possible for a **secondary
output** but not the principal one", worked as a vendor publishing a credits-per-image rate while video
consumes credits by an unpublished rule — **two outputs of one product**. A humanization is not this
product's secondary output; it is the sibling product's principal output, and §7.1 keeps them in
separate records. Coding `partial` here would import the sibling's construct, which is exactly what the
record was right to refuse.

**(c) Domain 11, which the queue folded in "by the same reasoning" — and where the reasoning does not
hold.** The record codes all three domain-11 variables `not_applicable` from one test. The codebook
does not give them one test.

- **`watermark_removal_tier` → stays `not_applicable`.** Rule 3 is explicit: `not_applicable` "where
  the principal output is not a **media artifact** a watermark could mark, **for example a detection
  score or an analysis table**." A "Scan Report" carrying an "Overall AI Score" and a "Per-Pattern
  Breakdown" is that example, in the rule's own words. This is the legitimate case, and it is not
  reached by the A-018 line of rulings, which turned on a *rewritten essay* being a work product a mark
  could attach to. `free_plan_watermark = not_applicable` stands for the same reason and should not be
  "corrected" by anyone applying A-018 mechanically.
- **`commercial_use_lowest_tier` → `unknown`.** The codebook states this variable's `not_applicable`
  test in `output_ownership_statement`'s decision rule: it "requires that the product generates **no
  artifact at all**, which is the same test `commercial_use_lowest_tier` applies". A Scan Report is an
  artifact. The vendor's own documents confirm it: Terms §5 prohibits "Resell or redistribute **Service
  output** as a competing service without written permission" — unqualified across the Service, and a
  prohibition that presupposes output capable of commercial exploitation. So the construct exists.
  It is not `not_granted`, because §5 restricts one narrow use (reselling as a competitor) rather than
  commercial use generally, and no document addresses ordinary commercial use of a detection report.
  `unknown`, on codebook §2.2's rule that silence is not positive evidence of absence.
  *(This is the value the sibling's adjudicator reached on the same document. Disclosed above.)*
- **`output_ownership_statement` → `user_owns`.** Terms §6, read in full in this record's own source
  file: "You retain ownership of all text you submit to the Service. We claim no ownership over your
  inputs or outputs. **The Service itself — including the model prompts, the retrieval corpus, and the
  proprietary detection model behind /detect — is the property of Mihci AI Studios LLC.**" The record
  scoped this clause to the humanizer on the ground of "the clause's surrounding context". **The
  surrounding context names `/detect` by name.** The clause is site-wide, its subject is "all text you
  submit" (the detector's input is submitted text), and its object is "your inputs or outputs" without
  qualification. The vocabulary split cannot reach it: §6 uses neither "scans" nor "requests" — it uses
  "text", "inputs" and "outputs". Unconditional, with no tier and no active-subscription caveat, so
  `user_owns` rather than `conditional`. The reservation in the same clause is over *the Service*, not
  over outputs, and E3's decision rule bars only a marketing line from overriding "a terms clause that
  reserves a license"; §6 reserves none over outputs.

The apparent inconsistency between these three — one artifact test failing on E1 and E3 while E2's
holds — is what the codebook actually says. E2 asks whether the output is a **media** artifact a
watermark could mark; E1 and E3 ask whether the product generates **any** artifact at all. A detection
report is an artifact and is not a media artifact. Both answers follow.

### 3. Variables that change

| Variable | Current | New | Rule |
|---|---|---|---|
| `usage_cap_quantified` | `none_quantified` | **`some_quantified`** | §5.2 tier-scoping + `usage_cap_quantified` rule 1 |
| `commercial_use_lowest_tier` | `not_applicable` | **`unknown`** | E3's statement of E1's test ("no artifact at all") + Terms §5 |
| `output_ownership_statement` | `not_applicable` | **`user_owns`** | Terms §6, which names `/detect` |

**Three coded values. Explicitly unchanged:** `entry_tier_name` (`Basic`), `headline_price_usd`
(`12.00`), `headline_billing_basis` (`per_month_billed_annually`), `first_charge_amount_usd`
(`144.00`), `mandatory_addon_present` (`no`), `cost_per_output_computable` (`no`),
`cost_per_output_unit` (`other`), `computation_assumptions` (`not_applicable`), `trial_length_days`
(`not_applicable`), `refund_window_days` (`unknown`), `watermark_removal_tier` (`not_applicable`),
`free_plan_watermark` (`not_applicable`), `unquantified_limit_clause` (`absent`).

**Derived consequences.** Item F1 moves 0 → 3 of 6. Item E3 re-enters the index at 2 of 2. Item E1
re-enters at 0 of 5. So `apti_earned` +5 and `apti_available` +7; `unknown_count` +1;
`determinability_rate` gains one determinate item over two applicable ones. Whether `apti_total` rises
depends on this record's baseline ratio, which is computed after freeze: it rises if the baseline is
below 5/7, and falls otherwise. Component C is untouched; components E and F both move.

**The record's third flagged judgment call, `refund_policy_exists = yes`, is not in A-010's scope and I
did not reopen it.** For the correction batch's information only: the same clause was contested between
two coders on the sibling record and adjudicated `yes` there, so a reader comparing the two will find
them consistent.

### 4. Direction

**Two of the three changes favour the vendor; one tells against it; the study's unknown burden rises by
one.**

- Vendor-favourable: `usage_cap_quantified` +3 points, `output_ownership_statement` +2 of an available 2.
- Vendor-adverse: `commercial_use_lowest_tier` adds 5 points to the denominator and none to the
  numerator, and adds an `unknown` to the study's central quantity.

**The ruling on (a) is emphatically vendor-favourable and I want that on the record.** Coding
`not_applicable` would have sent every entry-tier variable on this record to `not_applicable` under
§7.3, removed items A1, A2 and A3 from the index, and erased the study's cleanest example of a real
buyer harm: a subscriber paying $144 a year for a bundle that lists AI detection as an included benefit
cannot find out how much detection she has bought. Holding Basic keeps that finding measurable. It also
means this vendor is scored on a paid tier that no buyer can purchase *for the detector alone*, which
is a genuine cost of §7.1's product-unit design and belongs in the limitations.

**Attribution kinds for the correction batch.** The new `commercial_use_lowest_tier = unknown` is
`vendor_silence`: the shared Terms were read in full, in this record's own source file, and the vendor
does not address ordinary commercial use of detector output. It is not an access failure — nothing was
unreachable.

### 5. What the sampling rules and codebook should say in wave 2 and do not

- **§7.2 needs a bundled-benefit rule.** Two products sharing one paid tier is now common (one vendor,
  two frame products, one pricing page). The rule should say explicitly that a plan is eligible for a
  product whose benefit the plan documents as included, that both records may name the same
  `entry_tier_name`, and that a record must state which of the tier's published limits it attributes to
  its own product.
- **§5.2's tier-scoping should say what it scopes.** The same clause reaches `usage_cap_quantified`'s
  whole limit list and only `cost_per_output_computable`'s numerator. Two careful coders will not derive
  that asymmetry from "rather than for the product as a whole"; this one did not.
- **Domain 11 should state its three `not_applicable` tests separately.** The record read one test
  across all three variables because E3's table cross-references E1 and E2's rule 3 supplies the vivid
  example, and "a detection score or an analysis table" then travelled to two variables it does not
  govern. E1 and E3's test ("no artifact at all") should be printed in each variable's own table
  instead of stated once inside E3's decision rule. This is the second time in this study that the
  watermark carve-out has been over-extended by a coder reading the example rather than the test
  (see A-018 and D-046).
- **`cost_per_output_computable` needs a value for "the entry tier's price buys this product's output,
  and no allowance for it is published, while the same tier's other product is fully computable".**
  `no` is correct and tells the reader nothing about how near the vendor came.

---

## A-014 — rezi

### 1. The rule that decides it

`sampling-rules.md` §7.2, price basis and rule 1:

> Among the eligible candidates, the **entry paid tier** is the one with the **lowest annual-equivalent
> cost of a single seat, computed in the pricing page's default display state**.
>
> 1. **Read the page as it loads.** The default display state is whatever the pricing page shows before
>    any interaction… **Do not switch the billing toggle to find a cheaper figure.**

and `headline_price_usd`'s definition:

> The largest, most prominent price figure the vendor publishes for the entry paid tier **on its
> pricing page**.

### 2. Ruling

**§7.2's pricing-page anchor holds. The entry paid tier is Pro at $29/month. No coded value changes.**

**First, the facts, verified independently today rather than taken from the record.** Fetched
2026-08-17, no login, no account:

| Check | Result |
|---|---|
| `https://www.rezi.ai/pricing`, live, desktop UA, `Accept-Language: en-US` | HTTP 200, 446,631 bytes. **`quarterly` appears 0 times.** Price figures present: $149, $29, $99, $8, $0 |
| `https://intercom.help/rezihelp/en/articles/8383549-subscription-plans`, live | HTTP 200. Carries **"Quarterly: $19/month (billed quarterly)"** verbatim |
| Cited archive capture of the `rezi-docs` page (`20260812071829`) | HTTP 503 — the outage both retrieval sweeps recorded, not a missing capture |
| Local source copies | Present and carrying the quoted text: `subscription-plans-intercom-full-text.txt`, `rezi-docs-subscription-plans-explained-full-text.txt`, `cancellation-policy-full-text.txt` |

**Both halves of the divergence are real and both are still live.** The record's account is accurate in
every particular I could check.

**Why the anchor holds.** Quarterly satisfies §7.2's eligibility list — generally available, self-serve,
standing (the Cancellation Policy administers "Quarterly Plans" as a live billing category with its own
refund windows), single-seat. But eligibility only admits a plan to the price comparison, and the price
comparison is defined over one thing: the annual-equivalent figure "computed in the pricing page's
default display state". Quarterly has no figure in that state, because it has no figure on that page in
any state. Its annual-equivalent under the rule is not high or low; it is **not computable**. There is
no reading of §7.2 on which an incomparable candidate wins a comparison.

**This is not the A-016 situation, and the difference matters.** There, §7.2 rule 5 was silent on a
question it had to answer — at which level the usage-based test runs — and both answers produced a
determinate but different tier, so the adjudicator coded `unknown` under `protocol-v1.md` §7.4 step 5.
Here §7.2 is not silent. It names where the comparison figure comes from, and that clause decides the
case as written. §7.2 leaves a **seam** — it does not name the state "eligible candidate with no
pricing-page figure" — but a seam in the wording is not an underdetermined outcome, and a coder flagging
a call because the result feels wrong is not the same as a rule that cannot reach one. I decline to
code `unknown` here.

**Three structural checks, each of which independently favours Pro.**

**(i) Selecting Quarterly would make the study score rezi's price as *less* determinable.**
`headline_price_usd` is definitionally a pricing-page figure. Quarterly's is not on the pricing page, so
the variable would be `unknown` on its own definition — **item A1 scoring 0 of 8 instead of 8 of 8** —
or, if codebook §3's hierarchy were stretched to let the help centre supply a rank-1 pricing value where
the pricing page is silent, `19.00` from a document that self-qualifies as non-authoritative (see (ii)).
Either way, the vendor is punished for publishing a cheaper plan in its help centre, and the more plans
a vendor documents off-page the worse it scores. An index that produces that gradient is measuring the
wrong thing.

**(ii) The cheaper figure is self-qualified by the vendor as not being anyone's actual price.** The
same help article that states "$19/month (billed quarterly)" also states: "**Pricing May Vary by
Region.** The prices shown above are our standard rates. Depending on your country or region, you may
see different pricing or special offers. To view the exact price available to you: 1. Open Rezi.
2. Click Upgrade." So what a reasonably diligent reader obtains about Quarterly under the A-013 test is
"a standard rate that may not be yours, with the real number behind a login" — while what she obtains
about Pro from the pricing page is $29, served unqualified, in USD, with no locale variance observed.
The two figures are not equally determinate even taken purely as prices. The disclaimer covers the $29
in that article too, but only Quarterly has *no* unqualified source anywhere.

**(iii) Selecting Quarterly would convert two determinate values into instrument-gap unknowns.**
`headline_billing_basis` is `per_month_billed_monthly` today and would become `unknown` — quarterly
prepay matches none of the codebook's recurring bases, which is A-011's gap, already reproduced on four
records. And under Domain 2, `annual_condition_disclosure` would stay `not_applicable` (its test is
annual prepayment specifically), so **item A2 and its 7 points would remain out of the index** even
though the buyer would now be committing three months up front. Honouring the cheaper plan would
therefore *reduce* what the instrument can say about rezi's prepayment disclosure. That is a reason to
fix Domain 2 in wave 2, not a reason to move the tier in wave 1.

### 3. Variables that change

**None. Zero coded values.** The record already anchored to the pricing page, documented both figures,
and recorded the divergence in `conflict_note` — which is precisely what codebook §3 requires: "Where a
higher source overrides a lower one, the disagreement goes in `conflict_note` with both URLs, even
where the hierarchy settles the value cleanly. A gap between a marketing page and a contract is a
result, not noise."

**The counterfactual cascade, enumerated because the ruling is only usable with it.** Had Quarterly been
selected, these would move — and the record's own list of five is right as far as it goes but misses
three:

| Cascade variable | Pro (ruled) | Quarterly (rejected) | In record's list? |
|---|---|---|---|
| `entry_tier_name` | `Pro` | `Quarterly` | Yes |
| `headline_price_usd` | `29.00` | `unknown` on the variable's definition, or `19.00` on a stretched §3 hierarchy | Yes |
| `headline_billing_basis` | `per_month_billed_monthly` | **`unknown`** (A-011 enum gap) | Yes |
| `first_charge_amount_usd` | `29.00` | `57.00` ($19 × 3) | Yes |
| `computation_assumptions` | $29.00/seat-month | $19.00/seat-month | Yes |
| `mandatory_addon_present` | `no` | `no` — unchanged | correctly omitted |
| `usage_cap_quantified` | `all_caps_quantified` | unchanged | stated unchanged |
| `cost_per_output_computable` | `yes` | `yes` — unchanged | stated unchanged |
| `trial_length_days` | `not_applicable` | unchanged | correctly omitted |
| `refund_window_days` | `30` | `30` — **value unchanged, evidence wrong** | **missed** |
| `headline_vs_first_charge_gap_ratio` (derived) | `1.00` | **`3.00`** | **missed** |
| `cost_per_output_value_usd` (derived) | `29.00` | `19.00` | **missed** |

Two of the three misses are worth naming. The derived **gap ratio would triple**, from 1.00 to 3.00 —
a headline-relevant number that a coder enumerating only coded variables will not see. And
`refund_window_days` keeps the value `30` while its **evidence sentence becomes wrong**: it quotes the
secondary window for the monthly plan ("Requests accepted within 7 days of your billing date"), where
the Quarterly plan's own line in the same document reads 14 days. A cascade audit that checks values
and not evidence would pass that through.

### 4. Direction

**This ruling decreases the study's unknown burden and favours the vendor, on both counts.**

It keeps `headline_billing_basis` determinate rather than adding an `unknown`, and it keeps item A1 at
its full 8 points rather than risking 0. Against that, it publishes $29 as rezi's entry price when the
vendor's cheapest generally-available recurring plan costs $19 — so the *price level* we report is
higher than the vendor's own cheapest, which is adverse to the vendor in the only sense a casual reader
will notice. Neither effect is why I ruled this way: §7.2 decides it, and `protocol-v1.md` §8.3.10 is
explicit that "the index scores determinability, not generosity". But a reader is entitled to both
directions rather than the convenient one.

**The construct this ruling declines to measure, stated plainly.** "What is the cheapest thing this
vendor will actually sell you" is a legitimate question, arguably the one a buyer cares most about, and
this study is not answering it. That is the same species of loss A-013's resolution recorded on
currency, and it belongs in the limitations next to it, not in a footnote.

### 5. The queue's standing question: is the shopper-versus-seller divergence a finding on its own, and
does anything else in the frame show it?

**Yes to the first, and yes to the second — it is a finding class, with three arms.** I swept every
record in `records/` for the pattern.

| Product | Arm of the pattern | Evidence |
|---|---|---|
| **rezi** | **Documented off-page, priced.** A cheaper generally-available recurring plan, with a figure, in two independent official documents, absent from the pricing page in every state. | `intercom.help/rezihelp/…/8383549-subscription-plans` ("Quarterly: $19/month (billed quarterly)"), `rezi.ai/rezi-docs/rezi-subscription-plans-explained`, and the Cancellation Policy's own Quarterly refund windows — against a pricing page where `quarterly` appears zero times. Verified live 2026-08-17. |
| **teal** | **Documented off-page, unpriced.** A fourth billing period is named in the ToS §5 and in the cancellation-policy help article's refund table, and **no price for it is published anywhere reachable without an account** — not on the pricing page, not in the "Teal vs Teal+" comparison doc. | The record excludes it as an eligible candidate with "no figure to annualize", which is the identical mechanic I apply to rezi's Quarterly, reached independently by that coder without needing adjudication. |
| **squarespace** | **Documented off-page, withdrawn — the clean case.** A help article documents older Personal/Professional/Premium plans and states verbatim "We no longer offer website platform plans on our pricing page". | The coder ran this exact check deliberately, recording that it was run "because a sibling product in this study had exactly that pattern (a cheaper plan documented only in help pages, absent from the pricing page)". Negative finding, affirmatively disclosed by the vendor. |

**Teal is the more serious disclosure failure of the three, and it reads as the milder one.** At rezi a
diligent reader can at least learn that a cheaper plan exists and roughly what it costs. At teal the
plan is named in the governing contract and its price exists nowhere a reader can reach — and because
annual cadences normally carry a discount, the plan the instrument could not score is very likely the
cheapest one. Both records handled it correctly and neither is marked down for it, because no variable
in the instrument asks the question.

**Two adjacent mechanisms found in the same sweep, which are not this class but bound it.**

- **vidnoz** — a cheaper Starter price almost certainly exists at the 300-credit slider position; the
  coder read the default handle and deliberately did not interact, applying §6.8's anti-cherry-picking
  principle to a slider by analogy with the billing toggle. Cheaper configuration, **on** the page,
  behind an interaction. Correctly not reported as a losing candidate figure ("unread, not merely
  lower").
- **squarespace, again** — the pricing page's own `OfferCatalog` JSON-LD lists a fourth "Plus" tier
  absent from the rendered page, and Basic offers ($25/mo, $228/yr) that match neither rendered toggle
  state. Cheaper-and-different prices **inside** the pricing page, never rendered. A-019's resolution
  settles the coding — unrendered markup is not disclosure — and the coder rightly coded from the
  rendered widget. But it is the same reader harm arriving by a third route.
- **revid-ai** — the FAQ states "Yearly billing is roughly 17% cheaper" while the coder could not get
  the annual control to respond. A cheaper *cadence* corroborated in prose with no figure; correctly not
  coded.

**What to report, and how.** Not "rezi hides a cheaper plan". The finding is structural and it is worth
a short section of its own:

> Across the frame, a product's pricing page is not a complete statement of what the vendor sells.
> In three products the vendor's own documentation describes a plan the pricing page omits: one priced
> and cheaper than the plan shown, one named in the governing contract with no price published anywhere
> a reader can reach, and one affirmatively disclosed as withdrawn. Two further mechanisms put a cheaper
> price on the pricing page itself where a reader cannot see it — behind a slider default, and in
> unrendered markup. **This study's entry-tier rule anchors to the pricing page, so in every one of
> these cases it measures what a shopper is shown rather than what the vendor will sell.** That is a
> deliberate choice for reproducibility, and it is a real limit on what the index's price figures mean.

Report it whether or not any coded value changes — none does — and report the count as **three of the
products investigated**, with the two adjacent mechanisms named separately so a reader can decide
whether to fold them in.

### 6. What the sampling rules and codebook should say in wave 2 and do not

- **§7.2 must name the state it currently leaves in a seam:** an eligible candidate with no figure in
  the pricing page's default display state. Say explicitly that it cannot enter the price comparison,
  that it is recorded in `coder_note` with its off-page figure and source, and that the divergence is
  reported. Two records reached that outcome independently; neither could point to a sentence for it.
- **Wave 2 should carry a dedicated coded variable for this class**, so it stops depending on whether a
  coder happened to look. Something like `cheaper_plan_documented_offpage`, with values for
  *priced off-page*, *named off-page without a price*, *documented as withdrawn*, *checked and absent*,
  and *not checked*. The squarespace record shows the check is answerable in minutes; the teal record
  shows the finding is invisible without it. A token in prose is not a mechanism — the A-012 grep defect
  established that at some cost.
- **Domain 2 is annual-specific and silently exempts every non-annual prepay product.**
  `annual_condition_disclosure`'s `not_applicable` is "No annual billing option exists", so a vendor
  whose entry tier demands a 90-day prepayment is never tested on disclosing it and **item A2's 7 points
  leave its index** — confirmed `not_applicable` on teal, jobscan and resume-io, all three
  quarterly-prepay entry tiers, and it would have hit rezi had this ruling gone the other way. **This is
  not my discovery: jobscan's adjudicator already identified the same root cause**, grouping
  `headline_billing_basis`, `annual_condition_disclosure` and `annual_default_toggle` as a
  "BILLING-CADENCE CLUSTER … all three disagreements share one root cause, Jobscan's entry tier billing
  quarterly rather than annually or monthly-only". Two adjudicators reaching it independently is the
  strongest evidence a wave-2 item can carry. Wave 2 should generalise the variable to *prepayment*
  rather than *annual* prepayment. A-011 reports this as an enum gap and understates it: the enum gap
  costs a descriptive value, while this costs a scored item worth 7 points.
- **The codebook should say that a cascade audit checks evidence text, not only values.**
  `refund_window_days` above keeps its value and loses its evidence.

---

## Totals

| | |
|---|---|
| Items resolved | 3 (A-001, A-010, A-014) |
| Coded values that would change | **3**, all on `pass1/humanizemy-ai-detector` |
| Records affected | 1 of 3 |
| Change to `unknown_count`, corpus-wide | **+1** (`humanizemy-ai-detector/commercial_use_lowest_tier`) |
| Derived-computation instructions recommended | 1, affecting 5 records (`cost_per_output_value_usd` where the arithmetic is non-USD) |
| Entry-tier selections confirmed | 3 of 3 — Pro, Basic, Pro |
| Entry-tier selections changed | 0 |
| Items coded `unknown` under §7.4 step 5 | 0 — and A-014's reason for declining is argued, not assumed |

**Net direction: these rulings favour the vendors and go against this study's headline number.** All
three decline an available route to a larger unknown count: canva's tier could have been ruled
undeterminable and taken five further cascade values to `unknown` with it; rezi's could have moved and
converted a determinate billing basis into an instrument-gap `unknown`; the detector's could have gone
`not_applicable` and removed three index items. Of the three coded changes, two add points to a vendor
and one takes them away. The single count that runs the other way is the correction to the "nineteen
cascade variables" figure, which means fewer unknowns may be discounted as cascades at canva and at
google-veo than the queue has been assuming.

**Nothing here has been applied to any record.** These are rulings; the corrections belong in the
batch, under one rule, dated.

## Owner review

One item on this page is a construct decision rather than a coding decision and should be read as
such: **A-014's ruling settles that this study's price figures describe what a shopper is shown, not
what the vendor will sell.** A-013's resolution made the parallel choice on currency and was flagged for
the same reason. Overturning A-014 would move five coded values and two derived values on one record,
add one instrument-gap `unknown`, and require the same treatment at teal — where there is no figure to
move to. The finding in §5 above should be published either way.
