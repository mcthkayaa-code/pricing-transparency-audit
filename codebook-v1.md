# Codebook v1.2

**Measurement instrument for** Pricing Transparency and Subscription Friction in Consumer AI Products.
**Companion to** `protocol-v1.md` (Research Protocol v1.2) and `sampling-rules.md` (frame and selection, v1.2).

> **Change log — v1.2, 2026-08-03. Second referee pass.** Three rules that could return two different values for one product are fixed. `cost_per_output_computable` gains a numbered step for the case where the calculation works for a secondary output but not the principal one — the case its value table already called `partial` while its numbered rules returned `no` — and its normalization rule drops the enumerated cases, the exclusive "instead", and the monthly-basis invariant in favour of one instruction: put price and allowance on the same period before dividing. New section 5.2 enumerates the entry-tier variables, which `sampling-rules.md` section 7.2 referred to without ever naming, and replaces the blanket `unknown` for a sales-gated tier with a rule that codes a published term from the document publishing it. `determinability_rate` picks up the item-level definition of determinacy now written into `protocol-v1.md` rule G0 and stops dropping items that rule G4 retains. The A3 impossible-pair guard is stated on the two variables as well as in the matrix, computation rule 4 carries the matrix-precedence clause G4 now has, `free_plan_cap_documented` prints the unlimited carve-out its twin `usage_cap_quantified` already carried, `annual_default_toggle` separates a display variant from a conflict between two official pages, `entry_tier_name` gains `unknown` for the sales-gated case, and section 2.3 states that its exception register covers coded variables only. No variable is added or removed and the item set is untouched, so the bump is minor under `protocol-v1.md` section 12.2's before-the-window clause.

> **Change log — v1.1, 2026-08-03. Referee pass.** The instrument no longer lets a coder reach a value the rules do not cover. `conflicting` is now on every coded variable's value list, `not_applicable` is added to `refund_policy_exists`, `output_ownership_statement`, and `refund_policy_location`, and the eight variables that cannot take a status value are named with their reasons in section 2.3 instead of being silently short. Three decision rules that two careful coders could have applied differently are fixed: what counts as a quantified limit now reads identically in `free_plan_cap_documented` and `usage_cap_quantified` and in both their value tables and their rules, `credit_unit_defined` states which output units count, and `cost_per_output_computable` fixes its price input, its billing basis, and its treatment of annual allowances. The variable counts in this header were wrong and are corrected to 15 administrative and 37 coded. `determinability_rate` no longer treats `absent` as non-determinate on the one item where it earns full points. No variable is added or removed and the item set is untouched, so the bump is minor under **`protocol-v1.md` section 12.2's before-the-window clause**. The value-list additions would change coded values if any existed; none do, because this pass is issued before the window opens, and `protocol-v1.md` section 12.1 records that.

| Field | Value |
|---|---|
| Version | 1.2 |
| Date | 2026-08-03 |
| Revision date | 2026-08-03 |
| Status | Pre-registration. Data collection not started. |
| Responsible human | Mucahit Kaya |
| Variables | 15 administrative, 37 coded, 16 derived |
| Domains covered | All 12 measurement domains. Map in section 9. |

> **All examples in this document use invented vendors: Vendor A, Vendor B, and so on. No example describes a real product, and no example may be quoted as a finding about any real company.**

---

## 1. How to use this codebook

1. Open one record per product, using the column order in section 10.
2. Work top to bottom. Variables are ordered so that gating questions come before the variables they gate.
3. For each variable, read the definition, then apply the decision rule in the order its steps are numbered. Stop at the first step that returns a value.
4. Code from documents only. Protocol section 6.3 lists what is prohibited.
5. Record the evidence with the value. A value without a source URL, an access date, and an archive reference is incomplete.
6. Never infer a value from marketing tone, from a competitor's page, from a third-party review, or from our own published investigation of the same product.
7. Where the documents do not settle it, code `unknown` and move on. Section 2 governs.

A coder holding these three documents and nothing else has everything needed to produce a comparable record.

---

## 2. The three special values

`unknown`, `not_applicable`, and `conflicting` are first-class values. Each one is recorded with its evidence and carried through to the published results, never treated as missing data.

| Value | Definition |
|---|---|
| `unknown` | No official document states a determinate value for this variable, or the relevant document could not be located. The buyer cannot determine this before paying. This is a finding. |
| `not_applicable` | An official document establishes that the construct does not exist for this product. Not "we did not find it". "It is documented as absent." |
| `conflicting` | Two or more official sources of equal authority for this variable state incompatible values, and the source hierarchy does not resolve which governs. Both URLs are recorded. |

### 2.1 Decision tree

Apply in order. Stop at the first step that returns a value.

1. Do official documents establish that the construct does not exist for this product? If yes, code `not_applicable`.
2. Do official documents state a determinate value? If yes, code that value.
3. Do two or more official sources state incompatible values? If the source hierarchy in protocol section 6.2 ranks one above the other for this variable class, code from the higher source and record the disagreement in `conflict_note`. If they rank equally, code `conflicting` and record both URLs.
4. Otherwise, code `unknown`.

### 2.2 The distinction that matters most

`not_applicable` requires positive documentary evidence of absence. A vendor whose documents never mention credits, in a product that plainly meters output, is `unknown` for the credit variables, not `not_applicable`. Getting this backwards would convert the study's central finding into a rounding error, since `unknown` scores zero in the index and `not_applicable` is removed from the denominator.

Where a variable's value list includes `absent`, that value replaces `unknown` for the specific case where the coder read the relevant document classes and found them silent. `unknown` on those variables means the documents could not be located at all. Both score zero, with one exception: on `unquantified_limit_clause`, item F2, `absent` earns full points because a documented finding that no discretionary clause exists is exactly what the item measures. `protocol-v1.md` rule G0 governs.

### 2.3 Which status values each variable carries

Section 5 forbids coding any value outside a variable's list. That rule only works if the lists are complete, so the availability of the three status values is fixed here rather than left to whether a value table happened to print a row.

**`conflicting` is available on every coded variable except those named below.** Two official sources of equal authority can disagree about anything a vendor publishes, and a coder who meets that disagreement on a variable whose list omits `conflicting` would be forced to invent a resolution the source hierarchy does not support. Every coded variable's value table in section 7 now prints the row.

**`unknown` is available on every coded variable except those named below.** It is the study's most important value and is never omitted.

**`not_applicable` is available on every coded variable except those named below.** It requires positive documentary evidence of absence, per section 2.2.

**This register covers coded variables only.** The administrative variables in section 6 — `entry_tier_name`, `coder_role`, `archive_status`, `recheck_date`, `conflict_note`, `coder_note`, and the rest — are not vendor statements about a product, so the three paragraphs above do not reach them. Each carries its own value list, fixed in section 6, and a status value appears on an administrative variable only where section 6 prints it. `entry_tier_name` is the one to watch, because it takes two of them: `not_applicable` where no paid tier exists, `unknown` where the only paid option is gated behind a sales contact and no plan name is published for it, and a plan name in every other case.

The exception register. These are the only variables missing a status value, and each is missing it for a stated reason:

| Variable | Status value unavailable | Why |
|---|---|---|
| `free_plan_exists` | `not_applicable` | Every product either documents a free plan or documents none. `no` is the determinate absence value, so `not_applicable` would duplicate it and would wrongly remove item B1 from the index. |
| `trial_exists` | `not_applicable` | Same construction. `no` carries documented absence and scores full points on B3. |
| `credit_system_present` | `not_applicable` | Same construction. `no` carries documented absence and is what removes C1, C2, and C4 from the index. |
| `auto_renewal_default` | `not_applicable` | `no_recurring_billing` already carries the one-time-purchase case as a determinate value scoring full points on D1. |
| `cost_per_output_unit` | `not_applicable` | Every product has a principal output unit, `per_seat_month` at minimum. |
| `cost_per_output_computable` | `not_applicable` | Follows from the line above. Item C3 applies to every product, so it never leaves the denominator. |
| `unquantified_limit_clause` | `not_applicable` | The clause is present in the documents or it is not. `absent` carries documented absence and `unknown` carries unreachable documents, which exhausts the possibilities. |
| `computation_assumptions` | `unknown`, `conflicting` | This field records the coder's own arithmetic, not a vendor statement. No vendor source can be silent about it and none can conflict with another. It carries `not_applicable` where no computation was performed. |

Eight exceptions across 37 coded variables. Nothing else is short a status value.

---

## 3. Source authority

Protocol section 6.2 is binding and is not restated here. Three reminders that coders get wrong:

- For **pricing variables** — price, plan composition, free tier, credits, trial terms — the **live pricing page ranks first**.
- For **contractual variables** — refund, cancellation, auto-renewal, output ownership, commercial-use rights — the **terms of service or dedicated policy page ranks first**, above the pricing page.
- **Documentation and the help center rank second in both classes.** The classes differ only in which document leads and where the pricing page falls.

Where a higher source overrides a lower one, the disagreement goes in `conflict_note` with both URLs, even where the hierarchy settles the value cleanly. A gap between a marketing page and a contract is a result, not noise, and it is reported as its own finding.

---

## 4. Evidence requirements

Every coded value other than `not_applicable` carries:

1. **Source URL.** The exact page, including anchor or section where a page is long.
2. **Access date.** ISO 8601, the date the page was read.
3. **Archive reference.** The public archive URL, or a local copy identifier where archiving failed. Protocol section 6.4 governs.

Qualifying source types, in the authority order of protocol section 6.2:

| Qualifies | Does not qualify |
|---|---|
| Vendor's live pricing page | Any third-party review or roundup |
| Vendor's official documentation or help center | Our own published investigation |
| Vendor's terms of service, refund policy, subscription policy | Vendor content republished on another site |
| Vendor's official billing or order FAQ | Affiliate pages, aggregators, app-store listings |
| Vendor's official blog post stating a policy | Social posts, support forum posts by non-staff |
| Public archive snapshot of any of the above | Screenshots or claims with no reachable source |

No value may be coded from a page that was not snapshotted on the date it was read.

---

## 5. Value formats

| Type | Format |
|---|---|
| Date | ISO 8601, `YYYY-MM-DD` |
| Money | Decimal, two places, no currency symbol, USD unless the value is `non_usd` |
| Integer | Plain digits, no separators |
| Categorical | Exactly one value from the variable's list, lowercase snake_case |
| List | Values separated by ` \| `, no spaces inside a value |
| Free text | Maximum 300 characters, single line, plain text |
| Boolean-style | Always encoded as `yes` / `no`, never `true` / `false` |

### 5.1 What counts as a quantified limit

Two variables turn on this test: `free_plan_cap_documented` for the free plan, and `usage_cap_quantified` for the entry paid tier. Both use the sentence below, word for word, in their value tables and in their decision rules. There is one test, not two.

> **A limit is quantified when it carries a number and the dimension that number counts, plus a period where the limit is a rate.**

The period requirement applies to rate-type limits only. Enumerated:

| Limit type | What it is | Requires | Qualifies | Does not qualify |
|---|---|---|---|---|
| **Rate** | A quantity consumed and replenished over time | number + dimension + period | "5 exports per month", "100 generations per day", "2 hours of transcription per month" | "5 exports", "100 generations", "generous monthly allowance" |
| **Standing** | A fixed ceiling that does not reset | number + dimension | "1 seat", "720p maximum resolution", "2 GB storage", "3 projects", "50 MB per file" | "limited resolution", "a small number of seats", "basic storage" |

A standing limit does not require a period, because it has none. "1 seat" is fully quantified: the buyer knows exactly what she gets, and there is no interval over which it refreshes. Demanding a period there would mark down a vendor for a precision the limit cannot have.

Words carrying no number never qualify, whatever the limit type: limited, basic, reduced, standard, generous, reasonable, plenty.

"Unlimited" is treated in `usage_cap_quantified` rule 3, which `free_plan_cap_documented` rule 3 applies unchanged to the free plan, and both value tables print the same carve-out. It is not covered by this section.

### 5.2 The entry-tier variables, and the sales-gated case

Six coded variables take their value **for the entry paid tier** selected under `sampling-rules.md` section 7.2, rather than for the product as a whole. They are named here, once, because a rule that turns on "every entry-tier variable" is not executable until the set is written down.

> **The entry-tier variables are `first_charge_amount_usd`, `mandatory_addon_present`, `usage_cap_quantified`, `cost_per_output_computable`, `trial_length_days`, and `refund_window_days`.**

`headline_price_usd` names the entry tier's price and is governed separately below. Variables that describe a document rather than a tier — `annual_condition_disclosure`, `refund_policy_exists`, `auto_renewal_default` and the rest — are not entry-tier variables, and nothing here changes how they are coded.

**The sales-gated case.** Where a vendor's only paid option requires contacting sales, the tier exists but its price is not published.

1. `headline_price_usd` is coded **`no_public_price`**, not `unknown`. The distinction is the finding: the vendor has published a decision to withhold the price, which is a different disclosure state from a price that could not be found.
2. **Where a term is published for the sales-gated tier in an official document, it is coded from that document, not `unknown`.** A vendor that gates its price and still publishes "14-day free trial" and "30-day refunds" has documented those terms, and coding them `unknown` would charge it for a gap that is not there.
3. Only an entry-tier variable that no official document settles is coded `unknown`, on the ordinary rule in section 2.1.
4. `first_charge_amount_usd` will normally be `unknown` in this case, because a first-charge amount cannot be stated where the price is not. That follows from the documents, not from a blanket rule, and a vendor that does publish a first-charge figure alongside a gated plan price is coded as publishing it.
5. `entry_tier_name` is coded `unknown` where no plan name is published for the gated option, and carries the published name where one is.

`protocol-v1.md` section 8.3.2.2 works through what this leaves item A3 scoring, and `sampling-rules.md` section 7.2 points here rather than restating the rule.

---

## 6. Administrative variables

Not domain-mapped. They identify the record and carry its evidence.

| Variable | Type | Values / format | Notes |
|---|---|---|---|
| `product_id` | string | Our review slug | Copied from the frozen frame. Join key across every study file. |
| `product_name` | string | Product name as the vendor writes it | Copied from the frozen frame. |
| `category` | categorical | One of the 15 categories | Copied from the frozen frame. |
| `product_status` | categorical | `active`, `discontinued` | Copied from the frozen frame, re-checked at collection. |
| `paid_submission` | categorical | `yes`, `no` | Whether the product entered our portfolio through a published paid submission option. Protocol section 10.3. |
| `entry_tier_name` | string | Plan name as published, or `not_applicable`, or `unknown` | The plan selected under `sampling-rules.md` section 7.2, by lowest annual-equivalent single-seat cost in the pricing page's default display state. `not_applicable` where no paid tier exists. **`unknown` where the only paid option is gated behind a sales contact and no plan name is published for it**, which is the section 5.2 case; where the gated option carries a published name, that name is recorded. Losing candidates go in `coder_note`. |
| `coder_role` | categorical | `primary`, `second`, `adjudicated` | One record per role. The adjudicated record is the published one. |
| `collection_date` | date | ISO 8601 | The date this record's values were read. **Every role writes its own.** A second coder never copies the primary record's date, because the reliability statistics compare the two dates against the change register to separate coder disagreement from vendor edits. Protocol section 7.4.1 governs. |
| `recheck_date` | date | ISO 8601 or `not_applicable` | Set where protocol section 6.6 triggered a re-collection. |
| `primary_source_url` | url | Pricing page URL | The page opened first. |
| `archive_url` | url | Archive URL or local copy id | For `primary_source_url`. |
| `archive_status` | categorical | `archived`, `local_copy_only`, `archive_failed` | `archive_failed` blocks coding. Protocol section 6.4. |
| `source_urls` | list | Pipe-separated URLs | Every official document opened for this record, with each one's own access date and archive reference in the evidence file. |
| `conflict_note` | free text | Free text or `not_applicable` | Any disagreement between sources, including one resolved by the hierarchy. Both URLs. |
| `coder_note` | free text | Free text or `not_applicable` | Anything a later reader needs to reproduce the coding. Always carries the entry-tier candidates that lost under `sampling-rules.md` section 7.2, with their annual-equivalent figures, or a statement that only one candidate was eligible. |

---

## 7. Coded variables by domain

### Domain 1. Headline price against the price actually charged

---

#### `headline_price_usd`
**Domain** 1 · **Type** money or categorical · **Index item** A1

**Definition.** The largest, most prominent price figure the vendor publishes for the entry paid tier on its pricing page.

**Values.** A money value, or `non_usd`, or `no_public_price`, or `not_applicable`, or `unknown`, or `conflicting`.

| Value | Meaning |
|---|---|
| money | The published figure for the entry paid tier |
| `non_usd` | The vendor publishes no USD price. Currency code and verbatim figure go in `coder_note`. |
| `no_public_price` | The entry paid tier's price is not published; a buyer must contact sales |
| `not_applicable` | The product has no paid tier and the documents say so |
| `unknown` | A paid tier exists but no price figure could be located in any official document |
| `conflicting` | Two official sources of equal authority publish incompatible prices for the same tier. Both URLs recorded. |

**Decision rule.**
1. Identify the entry paid tier under `sampling-rules.md` section 7.2, which selects by lowest annual-equivalent single-seat cost read in the pricing page's default display state. Record its name in `entry_tier_name` and every losing candidate in `coder_note`.
2. Take the price figure the vendor displays most prominently for that tier, in the page's default state as it loads. Do not switch a billing toggle before reading it.
3. If that figure is in USD, record it to two decimals.
4. If the vendor publishes only a non-USD figure, code `non_usd` and record the currency and figure verbatim in `coder_note`. Apply no conversion.
5. If the tier shows "Contact us" or equivalent instead of a figure, code `no_public_price`.
6. If usage-based pricing is the only paid option, record the published unit rate as the value and name the unit in `coder_note`.

**Evidence.** Pricing page. Where the figure appears in a plan card rendered by script, the archive reference must show it.

**Example.** Vendor A's pricing page loads with three cards, the annual toggle preselected. Starter shows "$8/mo, billed annually", Pro shows "$19/mo, billed annually", Business shows "$40/mo, billed annually". Starter is restricted to verified students, so it is not an eligible candidate. Among the eligible plans Pro carries the lowest annual-equivalent single-seat cost at 19 x 12 = 228, against Business at 480. `headline_price_usd = 19.00`, `entry_tier_name = Pro`, and `coder_note` records "Starter excluded, students only; Business eligible, annual-equivalent 480.00".

---

#### `headline_billing_basis`
**Domain** 1 · **Type** categorical · **Index item** none, descriptive

**Definition.** What the headline figure represents.

| Value | Meaning |
|---|---|
| `per_month_billed_annually` | A monthly figure charged as one annual payment |
| `per_month_billed_monthly` | A monthly figure charged monthly |
| `per_seat_per_month` | A per-seat monthly figure |
| `one_time` | A single purchase, no recurring billing |
| `usage_based` | A rate per unit of use |
| `unknown` | The basis is not stated |
| `not_applicable` | No paid tier |
| `conflicting` | Two official sources of equal authority state incompatible bases. Both URLs recorded. |

**Decision rule.**
1. Read the qualifier printed with the headline figure.
2. Where a per-seat figure and a per-month figure are both stated, code `per_seat_per_month`.
3. Where the qualifier is absent from the pricing page, check the billing FAQ and the terms. If neither states it, code `unknown`.

**Evidence.** Pricing page first, billing FAQ second.

**Example.** Vendor B shows "$12 per user / month" with an annual toggle preselected and "billed yearly" in the toggle label. `per_seat_per_month`, with the annual condition captured separately by `annual_condition_disclosure`.

---

#### `first_charge_amount_usd`
**Domain** 1 · **Type** money or categorical · **Index item** A3

**Definition.** The amount official documents state a buyer pays on the first transaction for the entry paid tier, in the billing configuration the pricing page presents by default.

**Values.** A money value, or `non_usd`, or `not_applicable`, or `unknown`, or `conflicting`.

| Value | Meaning |
|---|---|
| money | The stated first-charge amount |
| `non_usd` | The vendor publishes no USD first-charge figure. Currency code and verbatim figure go in `coder_note`. |
| `not_applicable` | No paid tier exists and the documents say so |
| `unknown` | A paid tier exists but no document states what the first transaction charges |
| `conflicting` | Two official sources of equal authority state incompatible first-charge amounts. Both URLs recorded. |

This variable and `mandatory_addon_present` jointly score item A3, which carries a published value-pair matrix in `protocol-v1.md` section 8.3.2.1. All thirty combinations of the two are scored there, so a coder never has to reason about how a pair adds up.

**The impossible pair.** `not_applicable` on either variable means the same thing — no paid tier exists — so the two can carry it only together. `first_charge_amount_usd = not_applicable` with any other value on `mandatory_addon_present`, and `mandatory_addon_present = not_applicable` with any other value here, are both unreachable and are returned for re-coding. The matrix marks those cells with a dagger and states what happens if a pair survives adjudication. Where both are `not_applicable`, item A3 leaves the index under `protocol-v1.md` rule G2, and the matrix governs that removal ahead of rule G4 under G4's own precedence clause.

**Decision rule.**
1. Read the pricing page in its default state. Note which billing period is preselected.
2. If the default is annual and the headline is a monthly figure, the first charge is the annual total the documents state. If the documents state only the monthly figure, multiply by 12 **only where the documents state that the plan is charged once for twelve months**. Record the arithmetic in `computation_assumptions`.
3. If the documents do not state the billing frequency, code `unknown`. Do not assume twelve months.
4. Add any mandatory add-on whose amount is stated. Record it in `coder_note`.
5. Exclude taxes, which vary by jurisdiction, and exclude usage overages. Note the exclusion in `coder_note`.
6. Where the vendor publishes no USD figure, code `non_usd`.

**Evidence.** Pricing page plus the billing FAQ or order help article. No checkout is opened at any point.

**Example.** Vendor C's pricing page opens with the annual toggle preselected, showing "$19/mo" with "billed annually" beneath, and its billing FAQ states annual plans are charged once for twelve months. `first_charge_amount_usd = 228.00` against `headline_price_usd = 19.00`.

---

#### `mandatory_addon_present`
**Domain** 1 · **Type** categorical · **Index item** A3

**Definition.** Whether a buyer must pay a further charge, beyond the plan price, to use the entry paid tier as the pricing page advertises it.

| Value | Meaning |
|---|---|
| `no` | Documents state or show no such charge |
| `yes_amount_stated` | A required additional charge exists and its amount is published |
| `yes_amount_unstated` | A required additional charge exists and its amount is not published |
| `unknown` | The documentation could not be located, so whether one exists is unsettled |
| `not_applicable` | No paid tier, which requires `first_charge_amount_usd = not_applicable` on the same record |
| `conflicting` | Two official sources of equal authority state incompatible positions on a required charge. Both URLs recorded. |

**Decision rule.**
1. List the features the pricing page attributes to the entry paid tier.
2. Check the documentation for any of those features that carries a separate charge, a required minimum credit purchase, a platform fee, or a compulsory onboarding fee.
3. Optional add-ons are not mandatory add-ons. Taxes are not add-ons. Overage charges for use beyond the plan are not add-ons.
4. Where a required charge exists and its amount is published, code `yes_amount_stated`.
5. Where the documentation was read and shows no such charge, code `no`. `unknown` is for the case where the documentation could not be located at all, which makes it rare on this variable and severe when it happens.
6. `unknown` and `yes_amount_unstated` score identically on item A3, at 2 of 5 where a numeric first charge exists. Both leave a buyer holding a plan price she cannot turn into a total. The matrix in `protocol-v1.md` section 8.3.2.1 states this and argues it; the coder's job is only to record which of the two states the documents are in.

**Evidence.** Pricing page plus product documentation.

**Example.** Vendor D lists voice cloning among the features of its $29 Studio plan, and its documentation states that voice cloning requires a separate $10 per month module. `yes_amount_stated`, with both figures in `coder_note`.

---

### Domain 2. Visibility of the annual-billing condition

---

#### `annual_condition_disclosure`
**Domain** 2 · **Type** categorical · **Index item** A2

**Definition.** How close the disclosure that a price requires annual prepayment sits to the price itself.

| Value | Meaning |
|---|---|
| `adjacent` | Inside the same visual price block: the same card, the same line, directly beneath the figure, or in the label of the toggle attached to it |
| `same_page_secondary` | Elsewhere on the pricing page: a footnote, small print below the plan grid, or an accordion on the same page |
| `one_click_away` | Only in a document reached by a link: terms, billing FAQ, help article |
| `absent` | The relevant document classes were read and none states the condition |
| `unknown` | The relevant documents could not be located |
| `not_applicable` | No annual billing option exists, or billing does not recur |
| `conflicting` | Two official sources of equal authority state incompatible conditions. Both URLs recorded. |

**Decision rule.**
1. Establish whether the headline figure depends on annual prepayment. If it does not, code `not_applicable`.
2. Read the price block containing the headline figure. If the condition is stated inside it, code `adjacent`.
3. Read the rest of the pricing page, including footnotes and small print. If stated there, code `same_page_secondary`.
4. Read the billing FAQ, the help center, and the terms. If stated only there, code `one_click_away`.
5. If none of them state it, code `absent`.

Font size is not part of this variable. Position is. A condition in small type inside the price card is `adjacent`.

**Evidence.** Pricing page, plus each further document opened.

**Example.** Vendor E shows "$19/mo" in a card and prints "annual plans are billed upfront" in a footnote below the plan grid, with nothing in the card itself. `same_page_secondary`.

---

#### `annual_default_toggle`
**Domain** 2 · **Type** categorical · **Index item** none, descriptive

**Definition.** Which billing period the pricing page preselects when it loads.

| Value | Meaning |
|---|---|
| `annual_preselected` | The page loads showing annual pricing |
| `monthly_preselected` | The page loads showing monthly pricing |
| `no_toggle` | The page offers one billing period only |
| `unknown` | Could not be determined |
| `not_applicable` | Billing does not recur |
| `conflicting` | The vendor maintains two official pricing pages that load in different default states. Both URLs recorded. |

**Decision rule.**
1. Load the pricing page. Read its state before any interaction.
2. Where the page offers annual and monthly options, record which is active on load.
3. Do not click the toggle before recording. Clicking a display toggle is permitted afterward for reading other variables, since it neither creates an account nor starts a purchase.
4. **A page that loads in different states on different reads is a display variant, not a conflict.** `conflicting` is reserved for the case where the vendor maintains **two official pricing pages** that load in different default states. Where the **same URL** serves different states — an A/B test, a page varying by inferred geography, a cookie-keyed toggle — `protocol-v1.md` section 6.8 governs: record the state this load showed, archive the page in it, and log both states in `coder_note`. Do not reload hunting for a preferred state, and do not average the two.

**Evidence.** Pricing page, archived in the default state it was read in. Every value anchored to that state rests on a snapshot showing it, per `protocol-v1.md` section 6.8.

---

### Domain 3. Real usability of the free plan

---

#### `free_plan_exists`
**Domain** 3 · **Type** categorical · **Index item** B1

**Definition.** Whether the vendor documents a plan usable at no cost and with no time limit imposed by a trial.

| Value | Meaning |
|---|---|
| `yes` | A no-cost plan is documented |
| `no` | The pricing page shows paid tiers only, or documents state there is no free plan |
| `unknown` | Documents do not settle it |
| `conflicting` | Two official sources of equal authority disagree about whether a free plan exists. Both URLs recorded. |

`not_applicable` is unavailable on this variable. Section 2.3 gives the reason: `no` already carries documented absence, and item B1 must stay in the index.

**Decision rule.**
1. A time-limited free trial is not a free plan. It is coded under domain 4.
2. A plan priced at zero with an ongoing allowance is a free plan.
3. Where the pricing page lists only paid tiers and no free option anywhere in the documents, code `no`. That is a determinate finding, not a gap, and it scores full points on item B1.

**Example.** Vendor F's pricing page shows a "Free" column with a monthly allowance and no expiry. `yes`.

---

#### `free_plan_cap_documented`
**Domain** 3 · **Type** categorical · **Index item** B1

**Definition.** Whether the limits on the free plan carry published numbers.

| Value | Meaning |
|---|---|
| `all_quantified` | Every stated free-plan limit is quantified: it carries a number and the dimension that number counts, plus a period where the limit is a rate. Also where documents state explicitly that the free plan carries no limit in a given respect, on the test in `usage_cap_quantified` rule 3. |
| `some_quantified` | At least one limit is quantified and at least one is not |
| `none_quantified` | Limits are described without numbers |
| `unknown` | The free plan's limits are not described at all |
| `not_applicable` | No free plan |
| `conflicting` | Two official sources of equal authority state incompatible free-plan limits. Both URLs recorded. |

**Decision rule.**
1. List every limit the documents attribute to the free plan: outputs, minutes, exports, seats, storage, resolution, queue priority.
2. **A limit is quantified when it carries a number and the dimension that number counts, plus a period where the limit is a rate.** Section 5.1 enumerates the two limit types and is binding. "5 exports per month" is a quantified rate. "1 seat" and "720p maximum resolution" are quantified standing limits and require no period. "Limited exports" is not quantified.
3. Where the documents describe the free plan as unlimited in some respect, apply the test in `usage_cap_quantified` rule 3: an explicit statement of no limit counts as quantified unless a clause elsewhere qualifies it without a number, in which case it does not and `unquantified_limit_clause` records the clause.
4. Code by how many of the listed limits are quantified.

**Example.** Vendor G's free plan states "10 images per month", "1 seat", and "limited resolution". The first is a quantified rate, the second a quantified standing limit, the third carries no number. `some_quantified`.

---

#### `free_plan_cap_value`
**Domain** 3 · **Type** free text · **Index item** none, descriptive

**Definition.** The quantified limits of the free plan, verbatim in structure.

**Format.** `quantity unit per period` for a rate, `quantity unit` for a standing limit, multiple caps separated by ` | `. For example `10 images per month | 1 seat`. Or `unknown`, or `not_applicable`, or `conflicting`.

**Decision rule.** Record only quantified limits, as section 5.1 defines them. Do not paraphrase an unquantified limit into a number. Where two official sources of equal authority publish incompatible caps, code `conflicting` and record both figures with both URLs in `conflict_note`.

---

#### `free_plan_watermark`
**Domain** 3 · **Type** categorical · **Index item** B2

**Definition.** Whether free-plan outputs carry vendor branding or a watermark, as documented.

| Value | Meaning |
|---|---|
| `yes` | Documents state free outputs are watermarked or branded |
| `no` | Documents state free outputs are not watermarked |
| `unknown` | Documents do not state it |
| `not_applicable` | No free plan, or the output type cannot carry a watermark |
| `conflicting` | Two official sources of equal authority state incompatible positions. Both URLs recorded. |

**Decision rule.** A pricing-table row reading "Watermark-free exports" under a paid tier, with the free column marked with a cross, is a documented `yes` for the free plan. A silent pricing table is `unknown`.

**Example.** Vendor H's feature grid has a row "No watermark" with a check under Pro and a cross under Free. `yes`.

---

#### `free_plan_duration`
**Domain** 3 · **Type** categorical · **Index item** B2

**Definition.** Whether the free plan persists or expires.

| Value | Meaning |
|---|---|
| `perpetual` | Documents state the free plan continues without a time limit |
| `time_limited` | Documents state the free plan ends after a stated period |
| `unknown` | Documents do not state it |
| `not_applicable` | No free plan |
| `conflicting` | Two official sources of equal authority state incompatible durations. Both URLs recorded. |

**Decision rule.** A plan the pricing page presents as a standing tier alongside paid tiers, with no expiry stated anywhere in the documents, is `perpetual`. A plan described as free "to start" or "for your first month" is `time_limited`.

This variable and `free_plan_watermark` jointly score item B2. Under `protocol-v1.md` rule G4, a `not_applicable` on either counts as determinate for that item, and B2 leaves the index only where both are `not_applicable`.

---

### Domain 4. Whether a trial requires a payment card

---

#### `trial_exists`
**Domain** 4 · **Type** categorical · **Index item** B3

**Definition.** Whether the vendor documents a time-limited free trial of a paid tier.

**Values.** `yes`, `no`, `unknown`, `conflicting`.

`not_applicable` is unavailable on this variable. Section 2.3 gives the reason: `no` already carries documented absence and scores full points on item B3.

**Decision rule.**
1. A free plan is not a trial. Domain 3 covers free plans.
2. A money-back guarantee is not a trial. Domain 10 covers refunds.
3. Where the pricing page and the documentation mention no trial, code `no`.
4. Where two official sources of equal authority disagree about whether a trial exists, code `conflicting` with both URLs.

---

#### `trial_card_required`
**Domain** 4 · **Type** categorical · **Index item** B3

**Definition.** Whether documents state that starting the trial requires payment details.

| Value | Meaning |
|---|---|
| `yes` | Documents state a card is required |
| `no` | Documents state no card is required |
| `unknown` | Documents do not state it |
| `not_applicable` | No trial |
| `conflicting` | Two official sources of equal authority state incompatible positions. Both URLs recorded. |

**Decision rule.**
1. Read the pricing page, the trial landing page, and the billing FAQ.
2. "No credit card required" printed on the trial call to action is a documented `no`.
3. The absence of any statement is `unknown`. Do not infer from the design of a signup link, and do not open the signup flow to check.

**Example.** Vendor I's pricing page says "Start 7-day trial" with no card statement, and its billing FAQ says trials convert automatically unless canceled. Automatic conversion implies stored payment details, but implication is not a statement. `unknown`, with the FAQ wording in `coder_note`.

---

#### `trial_length_days`
**Domain** 4 · **Type** integer or categorical · **Index item** B3

**Definition.** The trial's stated length in days.

**Values.** An integer, or `unknown`, or `not_applicable`, or `conflicting`.

**Decision rule.** Convert a stated period to days at 7 days per week and 30 days per month, and note the conversion. Where the length varies by tier, record the entry paid tier's trial. Where two official sources of equal authority state incompatible lengths, code `conflicting` with both figures and both URLs.

---

#### `trial_auto_converts`
**Domain** 4 · **Type** categorical · **Index item** none, descriptive

**Definition.** Whether documents state the trial becomes a paid subscription without a further action by the buyer.

**Values.** `yes`, `no`, `unknown`, `not_applicable`, `conflicting`.

**Decision rule.** Read the trial terms and the billing FAQ. A statement that the trial "converts", "continues", or "renews" unless canceled is `yes`. Where two official sources of equal authority disagree, code `conflicting` with both URLs.

---

### Domain 5. Comprehensibility of the credit system

---

#### `credit_system_present`
**Domain** 5 · **Type** categorical · **Index item** none, gating

**Definition.** Whether the product meters use through an internal unit, whatever the vendor calls it: credits, tokens, points, coins, generations.

**Values.** `yes`, `no`, `unknown`, `conflicting`.

`not_applicable` is unavailable on this variable. Section 2.3 gives the reason: `no` already carries documented absence, and it is `no` that removes C1, C2, and C4 from the index.

**Decision rule.**
1. A plan allowance stated directly in output units, for example "100 images per month", is not a credit system. Code `no`.
2. An intermediate currency that converts into outputs is a credit system. Code `yes`.
3. Where the documents mention a unit but never explain whether it meters output, code `yes` and let `credit_unit_defined` carry the opacity.
4. Where two official sources of equal authority disagree about whether the product meters through credits, code `conflicting` with both URLs.

This variable gates C1, C2, and C4. Getting it wrong removes three items from a product's denominator, so code `unknown` rather than guessing.

---

#### `credit_unit_defined`
**Domain** 5 · **Type** categorical · **Index item** C1

**Definition.** Whether any official document says what one credit is.

| Value | Meaning |
|---|---|
| `yes` | A document defines the unit, for example "one credit equals one second of generated audio" |
| `no` | The relevant documents were read and none defines it |
| `unknown` | The documentation could not be located |
| `not_applicable` | No credit system |
| `conflicting` | Two official sources of equal authority define the unit incompatibly. Both URLs recorded. |

**Decision rule.**
1. Read the pricing page, the documentation, and the help center.
2. A definition ties the unit to something a buyer recognizes: an output, a duration, a quantity of text.
3. **`credit_unit_defined` is `yes` where ANY official document converts credits into ANY output unit.** The output does not have to be the product's principal one. A vendor that defines a credit against a thumbnail export has still told the buyer what a credit is, and this variable asks only that.
4. **The principal-output requirement belongs to `credit_to_output_rate_published` alone.** That variable, and item C2, is where a definition tied only to a secondary output is marked down. Applying the principal-output test here as well would score the same omission twice.
5. Stating how many credits a plan includes is not a definition. "2,000 credits per month" without a conversion is `no`. A plan allowance is a quantity, not a unit definition, whatever the output it is attached to.

**Example.** Vendor J's docs state "1 credit renders 1 second of video at 720p". `yes`. Vendor J2 sells a video generator and defines a credit only against still-image exports, saying nothing about video. `credit_unit_defined = yes`, because a conversion into an output unit exists, and `credit_to_output_rate_published = partial`, because the rate is published for a secondary output and not the principal one.

---

#### `credit_to_output_rate_published`
**Domain** 5 · **Type** categorical · **Index item** C2

**Definition.** Whether the conversion from credits to outputs is published for the product's outputs.

| Value | Meaning |
|---|---|
| `yes` | Rates are published for the principal output and for the other output types the plan advertises |
| `partial` | Rates are published for some output types but not the principal one, or only as a range |
| `no` | The relevant documents were read and no rate is published |
| `unknown` | The documentation could not be located |
| `not_applicable` | No credit system |
| `conflicting` | Two official sources of equal authority publish incompatible rates. Both URLs recorded. |

**Decision rule.**
1. Identify the principal output, the one the product is sold to produce.
2. Look for a published rate for it: credits per image, per second, per thousand words.
3. A rate published as a range, for example "3 to 12 credits depending on complexity", with no rule for which applies, is `partial`.
4. Rates published for secondary features but not the principal output are `partial`. This is the only variable that applies the principal-output test; `credit_unit_defined` deliberately does not.

**Example.** Vendor K publishes credits per image but states that video "consumes credits based on length and quality" with no figures. Principal output is video. `partial`.

---

#### `credit_rate_location`
**Domain** 5 · **Type** categorical · **Index item** none, descriptive

**Definition.** Where a published rate lives.

**Values.** `pricing_page`, `docs_help_center`, `terms`, `multiple`, `absent`, `not_applicable`, `unknown`, `conflicting`.

**Decision rule.** Where the rate appears in more than one document class, code `multiple`. Where no rate is published, code `absent`. `conflicting` is reserved for the case where two equal-authority sources publish incompatible rates, which makes the location of the governing rate itself undeterminable; `multiple` is for agreement across classes, not disagreement.

---

### Domain 6. Computability of cost per output

---

#### `cost_per_output_unit`
**Domain** 6 · **Type** categorical · **Index item** none, supporting

**Definition.** The unit in which this product's principal output is counted.

**Values.** `per_video_minute`, `per_image`, `per_1k_words`, `per_audio_minute`, `per_page`, `per_headshot`, `per_document`, `per_presentation`, `per_seat_month`, `per_api_call`, `other`, `unknown`, `conflicting`.

**Decision rule.**
1. The principal output is what the product is sold to produce, as its own pricing page frames it.
2. Where a product sells unmetered access to software rather than a countable artifact, the unit is `per_seat_month`.
3. Where none of the listed units fits, code `other` and name the unit in `coder_note`.
4. Where two official sources of equal authority frame the principal output as different units, code `conflicting` with both URLs.
5. Every product has a unit, so `not_applicable` is unavailable on this variable. Section 2.3 gives the reason.

**Example.** Vendor L sells an unlimited-use writing assistant at a flat monthly price per user. `per_seat_month`.

---

#### `cost_per_output_computable`
**Domain** 6 · **Type** categorical · **Index item** C3

**Definition.** Whether a reader can calculate a cost per unit of principal output using only published figures and arithmetic.

| Value | Meaning |
|---|---|
| `yes` | Every figure needed is published, and the calculation needs no assumption about typical use |
| `partial` | The calculation is possible only for a secondary output, or only across a published range that yields a range rather than a figure |
| `no` | At least one required figure is not published |
| `unknown` | The documents needed could not be located |
| `conflicting` | Two official sources of equal authority publish incompatible figures among the calculation's inputs. Both URLs recorded. |

`not_applicable` is unavailable on this variable. Section 2.3 gives the reason: every product has a principal output unit, so item C3 applies to every product.

**Decision rule.**
1. **The price input is fixed.** It is the **entry paid tier's price**, as selected under `sampling-rules.md` section 7.2 and read **in the pricing page's default display state**. Not the cheapest plan on the page, not the plan whose allowance divides most neatly, and not a figure found by switching the billing toggle. Two coders computing the same product must start from the same number.
2. **`computation_assumptions` records the billing basis and the included allowance.** The billing basis is whichever of monthly or annual the default display state showed. The included allowance is the quantity of credits or outputs that price buys. Both go in the field with the arithmetic, because a cost per output is meaningless without them: $0.60 per video minute on an annual plan and $0.60 on a monthly plan are different claims.
3. **Put price and allowance on the same period before dividing.** Where either is published per year, convert it to a month; record every conversion in `computation_assumptions`. Both may need converting, one may, or neither. The instruction is the same in every case, and it is a single instruction because the quotient is a price per output unit rather than a price per month: dividing an annual price by an annual allowance and a monthly price by a monthly allowance give the same figure, so what matters is only that the two sides share a period.
4. Write the calculation you would perform. It must use published numbers only.
5. **If the calculation is possible for a secondary output but not the principal one, code `partial`** and name the output in `computation_assumptions`. This is the vendor that publishes a credits-per-image rate while its principal output, video, consumes credits by an unpublished rule. The reader can compute something, but not the thing the product is sold to produce, and `partial` is the value the table has always given that state.
6. If it needs a number the vendor does not publish, code `no`.
7. If it needs an assumption about how a typical buyer uses the product, code `no`. The reader's job is arithmetic, not estimation.
8. If it yields a range because the vendor publishes a range, code `partial`.
9. Record the calculation in `computation_assumptions` whenever the value is `yes` or `partial`.

**Example.** Vendor M's entry paid tier under `sampling-rules.md` section 7.2 is Creator, which the pricing page shows in its default annual state at "$30/mo, billed annually" with 1,000 credits per month, and the docs state one minute of video costs 20 credits. Price and allowance are already on the same period, so rule 3 converts nothing. 1,000 / 20 = 50 minutes per month; 30 / 50 = 0.60. `yes`, `cost_per_output_value_usd = 0.60`, unit `per_video_minute`, and `computation_assumptions` reads "Creator tier, $30/mo billed annually per default display state, 1,000 credits/mo included, 20 credits per video minute per docs; 1000/20=50 min, 30/50=0.60".

**Example, both sides annual.** Vendor M2 publishes its Creator tier as "$288 per year" with "14,400 credits per year" and the same 20-credits-per-video-minute rate. Rule 3 puts the two on one period: 288 / 12 = 24 per month, 14,400 / 12 = 1,200 credits per month, 1,200 / 20 = 60 minutes per month, 24 / 60 = **0.40**. Left on the annual period the arithmetic is 14,400 / 20 = 720 minutes per year and 288 / 720 = 0.40, the same figure, which is why rule 3 needs no invariant about which period the answer is expressed in. `yes`, `cost_per_output_value_usd = 0.40`, and `computation_assumptions` reads "Creator tier, $288/yr per default display state = $24/mo, 14,400 credits/yr = 1,200 credits/mo, 20 credits per video minute per docs; 1200/20=60 min/mo, 24/60=0.40".

**Example, secondary output only.** Vendor N publishes the same tier and allowance as Vendor M, publishes a rate of 5 credits per image, and states only that video "consumes credits based on length and quality". Its principal output is video. Rule 5 returns **`partial`**, not `no`: an image cost is computable and a video cost is not. `computation_assumptions` names the output the calculation was possible for, `cost_per_output_value_usd` stays `not_computable`, and item C3 scores 2.5 of 5. A vendor publishing no rate for any output at all reaches rule 6 instead and is coded `no`.

---

#### `computation_assumptions`
**Domain** 6 · **Type** free text · **Index item** none, supporting

**Definition.** The arithmetic behind any derived monetary value, written so a reader can repeat it.

**Format.** Free text, maximum 300 characters. Required whenever `cost_per_output_computable` is `yes` or `partial`, or whenever `first_charge_amount_usd` was calculated rather than read directly. Otherwise `not_applicable`.

`unknown` and `conflicting` are unavailable on this variable. Section 2.3 gives the reason: the field records the coder's own arithmetic rather than a vendor statement, so no source can be silent about it and none can conflict with another.

**Rule.** The text names every input figure and its source. Where it supports a `cost_per_output_computable` value, it must state the plan used, the **billing basis** from the default display state, the **included allowance**, and **every conversion made to put price and allowance on the same period** under that variable's rule 3, whether the price, the allowance, or both were converted. Where the value is `partial` because the calculation was possible only for a **secondary output**, the text names that output. An assumption that is not published is not permitted here; if one was needed, the value should have been coded `no` or `unknown`.

---

### Domain 7. Rollover of unused credits

---

#### `credit_rollover_policy`
**Domain** 7 · **Type** categorical · **Index item** C4

**Definition.** What the documents say happens to unused credits at the end of a billing period.

| Value | Meaning |
|---|---|
| `rolls_over` | Unused credits carry forward without a stated limit |
| `partial_rollover` | Credits carry forward subject to a stated cap or expiry |
| `expires_at_period_end` | Unused credits are lost at the end of the period |
| `unknown` | Documents do not state it |
| `not_applicable` | No credit system |
| `conflicting` | Two sources of equal authority state incompatible policies |

**Decision rule.**
1. Read the pricing page, the documentation, and the terms.
2. "Credits reset monthly" is `expires_at_period_end`.
3. "Credits roll over for up to 3 months" is `partial_rollover`.
4. Silence is `unknown`. Do not infer from a reset-sounding word in a feature grid without a statement.

---

### Domain 8. Charging for failed generations

---

#### `failed_generation_charge_policy`
**Domain** 8 · **Type** categorical · **Index item** C5

**Definition.** What the documents say happens when a generation fails, errors, or produces nothing usable.

| Value | Meaning |
|---|---|
| `not_charged` | Documents state failed generations consume nothing, or are refunded automatically |
| `charged` | Documents state the attempt consumes the allowance regardless of outcome |
| `case_by_case` | Documents state a failed generation may be credited back on request |
| `unknown` | Documents do not state it |
| `not_applicable` | The product has no metered generation step |
| `conflicting` | Two sources of equal authority state incompatible policies |

**Decision rule.**
1. A failure means a technical failure or an empty result, not an output the buyer dislikes.
2. `not_applicable` requires that the product does not meter generation at all, for example a flat-rate seat-based tool with no per-output accounting.
3. Silence is `unknown`, and this variable is silent often. That is the finding.

**Example.** Vendor O's help center states "credits are deducted when a job is submitted" and says nothing about failures. The statement covers submission, not outcome. `unknown`, with the wording in `coder_note`.

---

### Domain 9. Auto-renewal

---

#### `auto_renewal_default`
**Domain** 9 · **Type** categorical · **Index item** D1

**Definition.** Whether a subscription renews without a further action by the buyer.

| Value | Meaning |
|---|---|
| `on` | Documents state subscriptions renew automatically |
| `off` | Documents state subscriptions do not renew automatically |
| `no_recurring_billing` | The product is sold as a one-time purchase |
| `unknown` | Documents do not state it |
| `conflicting` | Two sources of equal authority state incompatible policies |

`not_applicable` is unavailable on this variable. Section 2.3 gives the reason: `no_recurring_billing` already carries the one-time-purchase case as a determinate value, so item D1 always sits in the index.

**Decision rule.**
1. The terms of service ranks first for this variable, above the pricing page.
2. "Your subscription will automatically renew unless canceled" is `on`.
3. A one-time purchase product with no subscription option is `no_recurring_billing`.
4. Where the terms state automatic renewal and the pricing page implies a fixed term, code from the terms and record the disagreement in `conflict_note`.

---

#### `auto_renewal_disclosure_location`
**Domain** 9 · **Type** categorical · **Index item** D2

**Definition.** Which document class discloses automatic renewal.

| Value | Meaning |
|---|---|
| `pricing_page` | Stated on the pricing page itself |
| `purchase_terms_doc` | Stated on a dedicated billing or subscription policy page |
| `help_center_only` | Stated only in a help center article |
| `terms_only` | Stated only in the terms of service |
| `multiple` | Stated in two or more of the above |
| `absent` | All four document classes were read and none states it |
| `not_applicable` | Billing does not recur |
| `unknown` | The documents could not be located |
| `conflicting` | Two official sources of equal authority state incompatible renewal positions, so no single class governs. Both URLs recorded. |

**Decision rule.** Check all four classes before coding. Code `multiple` where two or more state it in agreement, since proximity to the price is what this variable measures and repetition is the strongest form of it. Code `conflicting` where two or more state it in disagreement.

**Example.** Vendor P states automatic renewal in clause 7 of its terms and nowhere else. `terms_only`.

---

#### `renewal_notice_commitment`
**Domain** 9 · **Type** categorical · **Index item** none, descriptive

**Definition.** Whether the vendor commits to notifying the buyer before a renewal charge.

**Values.** `advance_notice_stated`, `no_notice_stated`, `unknown`, `not_applicable`, `conflicting`.

**Decision rule.** `advance_notice_stated` requires a stated commitment, ideally with a period. A statement that receipts are sent after charging is not advance notice. Where two official sources of equal authority state incompatible commitments, code `conflicting` with both URLs.

---

### Domain 10. Refund and cancellation terms

---

#### `refund_policy_exists`
**Domain** 10 · **Type** categorical · **Index item** D3

**Definition.** Whether official documents state a refund position.

| Value | Meaning |
|---|---|
| `yes` | A refund is available under stated terms |
| `no_refunds_stated` | Documents state that no refunds are given |
| `unknown` | Documents do not state a position |
| `conflicting` | Two sources of equal authority state incompatible positions |
| `not_applicable` | The product has no paid tier and the documents say so, so there is nothing a refund could attach to |

**Decision rule.**
1. The terms of service or a dedicated refund policy page ranks first.
2. `no_refunds_stated` is a determinate value, not a gap. A buyer who reads "all sales are final" knows exactly where they stand, and this variable measures that knowledge.
3. A statutory right mentioned for one jurisdiction only, with no general policy, is coded `yes` with the restriction recorded in `coder_note`.
4. `not_applicable` requires documented absence of any paid tier, per section 2.2. A product that sells something and says nothing about refunds is `unknown`, and item D3 scores zero. Confusing the two would move the study's most common finding out of the denominator.

**Example.** Vendor Q's terms state "Subscription fees are non-refundable except where required by law." `no_refunds_stated`, with the exception noted.

---

#### `refund_window_days`
**Domain** 10 · **Type** integer or categorical · **Index item** none, descriptive

**Definition.** The number of days after purchase during which a refund may be requested.

**Values.** An integer, or `0` where no refunds are given, or `unknown`, or `not_applicable`, or `conflicting`.

**Decision rule.** Where the window varies by plan, record the entry paid tier's window. Where a window is stated only for annual plans, record it and note the restriction. Where two official sources of equal authority state incompatible windows, code `conflicting` with both figures and both URLs.

---

#### `refund_conditions`
**Domain** 10 · **Type** categorical · **Index item** none, descriptive

**Definition.** Whether qualifying conditions attach to a refund.

| Value | Meaning |
|---|---|
| `unconditional` | Within the window, no condition beyond the request |
| `conditional` | Conditions apply: usage thresholds, a stated reason, an approval step |
| `unknown` | Documents do not state it |
| `not_applicable` | No refund available |
| `conflicting` | Two official sources of equal authority state incompatible conditions. Both URLs recorded. |

**Example.** Vendor R offers refunds within 14 days "provided fewer than 20 credits have been used". `conditional`.

---

#### `cancellation_self_serve`
**Domain** 10 · **Type** categorical · **Index item** D4

**Definition.** How the documents say a buyer cancels.

| Value | Meaning |
|---|---|
| `self_serve_documented` | Documents describe canceling from account settings without contacting anyone |
| `contact_required` | Documents state cancellation requires an email, a ticket, or a call |
| `unknown` | Documents do not describe a route |
| `conflicting` | Two sources of equal authority describe incompatible routes |
| `not_applicable` | Billing does not recur |

**Decision rule.** Both determinate values score identically in the index. The index measures whether a buyer can find out, not how easy the answer is. Friction is reported separately.

---

#### `refund_policy_location`
**Domain** 10 · **Type** categorical · **Index item** none, descriptive

**Definition.** Which document class carries the refund position.

**Values.** `pricing_page`, `dedicated_refund_page`, `terms`, `help_center`, `multiple`, `absent`, `unknown`, `not_applicable`, `conflicting`.

**Decision rule.** `multiple` is for agreement across two or more classes. `conflicting` is for disagreement between two of equal authority, which leaves the governing class undeterminable. `not_applicable` where `refund_policy_exists` is `not_applicable`, meaning no paid tier exists.

---

### Domain 11. Commercial-use rights

---

#### `commercial_use_lowest_tier`
**Domain** 11 · **Type** categorical · **Index item** E1

**Definition.** The lowest tier at which documents grant the right to use outputs commercially.

| Value | Meaning |
|---|---|
| `free` | Granted on the free plan |
| `lowest_paid` | Granted from the entry paid tier |
| `mid_tier` | Granted only above the entry paid tier and below the highest generally available tier |
| `highest_tier` | Granted only on the highest generally available tier |
| `enterprise_only` | Granted only under a contract negotiated with sales |
| `not_granted` | Documents state commercial use is not permitted on any published tier |
| `unknown` | Documents do not address commercial use |
| `not_applicable` | The product produces no output a commercial-use right could attach to |
| `conflicting` | Two official sources of equal authority state incompatible positions. Both URLs recorded. |

**Decision rule.**
1. The terms of service ranks first, then the pricing page feature grid.
2. A feature-grid row labeled "commercial license" with checks from a given tier upward determines the tier.
3. Where the terms grant commercial use generally and the grid restricts it to a tier, code from the terms and record the disagreement.
4. `not_granted` is determinate and scores full points. So does `free`. This variable measures whether a buyer can find out.

**Example.** Vendor S's grid shows "Commercial use" with a cross under Free and Starter and a check under Pro and Business, where Business is the highest published tier. `mid_tier`.

---

#### `watermark_removal_tier`
**Domain** 11 · **Type** categorical · **Index item** E2

**Definition.** The lowest tier at which documents state outputs carry no vendor watermark or branding.

**Values.** `no_watermark`, `free`, `lowest_paid`, `mid_tier`, `highest_tier`, `never_removed`, `unknown`, `not_applicable`, `conflicting`.

**Decision rule.**
1. `no_watermark` means documents state that no tier applies a watermark.
2. `never_removed` means documents state a watermark applies to every tier.
3. `not_applicable` where the principal output is not a media artifact a watermark could mark, for example a detection score or an analysis table.
4. `conflicting` where two official sources of equal authority name different tiers, with both URLs recorded.

---

#### `output_ownership_statement`
**Domain** 11 · **Type** categorical · **Index item** E3

**Definition.** What the documents say about who holds rights in generated outputs.

| Value | Meaning |
|---|---|
| `user_owns` | Documents state the customer owns or holds full rights in outputs |
| `vendor_license_retained` | Documents state the vendor retains ownership and grants a license |
| `conditional` | Rights depend on tier, on use type, or on a subscription staying active |
| `unknown` | Documents do not address ownership |
| `conflicting` | Two sources of equal authority state incompatible positions |
| `not_applicable` | The product produces no output ownership could attach to, matching the `not_applicable` case on `commercial_use_lowest_tier` |

**Decision rule.** The terms of service ranks first. A marketing line reading "your content is yours" does not override a terms clause that reserves a license; code from the terms and record the disagreement. `not_applicable` requires that the product generates no artifact at all, which is the same test `commercial_use_lowest_tier` applies; a product that generates artifacts and says nothing about who owns them is `unknown`.

**Example.** Vendor T's terms state the customer owns outputs "for as long as the subscription remains active". `conditional`.

---

### Domain 12. Undisclosed or unverifiable limits

---

#### `usage_cap_quantified`
**Domain** 12 · **Type** categorical · **Index item** F1

**Definition.** Whether the limits attached to the entry paid tier carry published numbers.

| Value | Meaning |
|---|---|
| `all_caps_quantified` | Every stated limit is quantified: it carries a number and the dimension that number counts, plus a period where the limit is a rate. Also where documents state explicitly that the tier carries no usage limit. |
| `some_quantified` | At least one limit is quantified and at least one is not |
| `none_quantified` | Limits are stated without numbers |
| `unknown` | The tier's limits are not described |
| `not_applicable` | No paid tier |
| `conflicting` | Two official sources of equal authority state incompatible limits for the same tier. Both URLs recorded. |

**Decision rule.**
1. List every limit the documents attribute to the entry paid tier.
2. **A limit is quantified when it carries a number and the dimension that number counts, plus a period where the limit is a rate.** Section 5.1 enumerates the two limit types and is binding. "100 generations per day" is a quantified rate. "1 seat" and "2 GB storage" are quantified standing limits and require no period. "Generous limits" is not quantified.
3. "Unlimited" counts as quantified only where no clause elsewhere qualifies it. Where a fair-use clause qualifies an unlimited claim, the limit is not quantified, and `unquantified_limit_clause` also records the clause.

**Example.** Vendor U advertises "unlimited generations" on its Pro tier, and its terms subject all plans to a fair-use policy with no figure. `none_quantified` for the unlimited claim, and `unquantified_limit_clause = present`.

**On coding the same page twice.** Rule 3 marks this vendor down on F1 and again on F2. That is intended, not an oversight, and `protocol-v1.md` section 8.3.10 argues it: F1 measures whether the buyer can size what she is buying, F2 measures whether a clause can shrink it afterward. Code both variables on their own definitions and do not adjust one to compensate for the other.

---

#### `unquantified_limit_clause`
**Domain** 12 · **Type** categorical · **Index item** F2

**Definition.** Whether official documents condition use on a standard that carries no number.

| Value | Meaning |
|---|---|
| `present` | A clause limits use by an unquantified standard: fair use, reasonable use, excessive use, abuse thresholds, throttling at the vendor's discretion |
| `absent` | The terms and the plan documentation were read and contain no such clause |
| `unknown` | The terms could not be located |
| `conflicting` | Two official sources of equal authority disagree about whether use is subject to such a clause. Both URLs recorded. |

`not_applicable` is unavailable on this variable. Section 2.3 gives the reason: `absent` carries documented absence and `unknown` carries unreachable documents, which exhausts the possibilities, so item F2 always sits in the index.

**`absent` here is determinate and earns full points.** This is the only place in the instrument where `absent` does. Elsewhere it records a disclosure that was never made; here it records a positive finding, that a coder read the terms in full and the vendor reserved no discretionary power over usage. `protocol-v1.md` rule G0 states the exception.

**Decision rule.**
1. Read the terms of service and the acceptable-use policy in full for this variable. A skim is not sufficient. `absent` is a claim about a document you have read to the end.
2. A clause that states a number, for example "requests are throttled above 100 per minute", is quantified and does not trigger `present`.
3. A prohibition on illegal or abusive content is not a usage limit and does not trigger `present`. This variable covers volume and intensity of use, not conduct.

**Example.** Vendor V's terms read "We may limit or suspend accounts whose usage substantially exceeds typical usage." No figure defines typical. `present`.

---

## 8. Derived variables

Derived variables are computed after the dataset is frozen and human sign-off is complete. A coder never enters them.

The `apti_*` variables implement the **AI Pricing Transparency Index (APTI), a determinability index**, defined in `protocol-v1.md` section 8.3. The subtitle travels with the name in every artifact: the index scores whether a buyer can determine a term before paying, not whether the term favors her.

| Variable | Formula | Notes |
|---|---|---|
| `headline_vs_first_charge_gap_ratio` | `first_charge_amount_usd / headline_price_usd` | Both must be money values. Otherwise `not_computable`. Rounded to two decimals. A value of 12.0 means the first charge is twelve times the advertised figure. |
| `cost_per_output_value_usd` | Product-specific arithmetic recorded in `computation_assumptions` | Only where `cost_per_output_computable` is `yes`. Where it is `partial`, this is `not_computable`, and `partial` covers both of that value's cases: in the **range** case the range goes in `coder_note`; in the **secondary-output** case there is no range to record, and `computation_assumptions` names the output the calculation was possible for. A range is recorded only in the range case, since a secondary-output figure is a single number for the wrong output rather than a spread for the right one, and publishing it as this product's cost per output would misstate what was computed. |
| `unknown_count` | Count of applicable index items whose **item-level** value is `unknown` | Applicable means not `not_applicable`. Item-level `unknown` is defined by `protocol-v1.md` rule G5: a single-variable item is `unknown` when its variable is, and a multi-variable item (A3, B1, B2, B3) is `unknown` when it scores zero and at least one sub-variable is `unknown`. Range 0 to 20. |
| `determinability_rate` | `determinate_items / applicable_items` | Determinate is defined once, in `protocol-v1.md` rule G0, which also fixes determinacy **at the item level**: an item is determinate when every sub-variable feeding it is determinate, and a multi-variable item with any non-determinate sub-variable is not. That is what makes this ratio computable for A3, B1, B2, and B3. `unknown` and `conflicting` are never determinate. **An item removed under G2 or G4 enters neither side of this ratio; a `not_applicable` sub-variable on a retained item counts as determinate**, so an item G4 keeps stays in the denominator and can be determinate. `absent` is non-determinate on items A2 and D2 and **determinate on item F2**, the one item where it earns full points. Rounded to two decimals. |
| `apti_earned` | Sum of points scored on applicable items | Protocol section 8.3. |
| `apti_available` | Sum of maximum points of applicable items | Protocol section 8.3.8. |
| `apti_total` | `100 x (apti_earned / apti_available)` | One decimal, half up. Suppressed where `apti_available < 50`. |
| `apti_band` | Lookup from `apti_total` | Protocol section 8.3.9. |
| `apti_component_a` … `apti_component_f` | `earned_c / available_c` per component | Published as earned and available, not only as a ratio. Six variables. |
| `apti_equal` | `(100 / k) x sum over components with available > 0 of (earned_c / available_c)` | Sensitivity analysis S1. Protocol sections 8.4 and 8.4.1. Suppressed wherever `apti_total` is suppressed, and where `k` is zero. |
| `apti_unknown_excluded` | `apti_total` recomputed with `unknown` items removed from numerator and denominator | Sensitivity analysis S2. Protocol sections 8.4 and 8.4.1. The guard is re-applied to the recomputed `available`, so this can be `suppressed` while `apti_total` publishes. Where recomputed `available` reaches zero, the value is `suppressed`, never 0.0 and never blank. |

Sixteen derived variables in total, counting the six component variables individually.

Computation rules that bind all of them:

1. `unknown` scores 0 and stays in the denominator.
2. `not_applicable` removes the item from numerator and denominator.
3. `conflicting` scores one third of the item's points, rounded to one decimal.
4. Items scoring from more than one variable — A3, B1, B2, B3 — are scored from the tables in `protocol-v1.md` sections 8.3.2.1, 8.3.3, and 8.3.3.1, not by combining the rules above. A `not_applicable` sub-variable counts as determinate and the item keeps its full point value, and the item is removed only where every sub-variable is `not_applicable`. **Where an item publishes its own value matrix, as A3 and B1 do, the matrix governs**, on the precedence clause in `protocol-v1.md` rule G4. The case this decides is the A3 matrix's `not_applicable` row, which removes the item where the general rule would keep it; the pair that difference turns on is unreachable in the first place, and both the matrix's dagger note and `first_charge_amount_usd` say so.
5. Derived values are computed for `active` products only.
6. Every derived value is reproducible from the published dataset by anyone applying these formulas. That is the point of publishing them.

---

## 9. Domain to variable map

| # | Measurement domain | Variables | Index items |
|---|---|---|---|
| 1 | Advertised headline price against the price actually charged | `headline_price_usd`, `headline_billing_basis`, `first_charge_amount_usd`, `mandatory_addon_present` | A1, A3 |
| 2 | Visibility of the annual-billing condition | `annual_condition_disclosure`, `annual_default_toggle` | A2 |
| 3 | Real usability of the free plan | `free_plan_exists`, `free_plan_cap_documented`, `free_plan_cap_value`, `free_plan_watermark`, `free_plan_duration` | B1, B2 |
| 4 | Whether a trial requires a payment card | `trial_exists`, `trial_card_required`, `trial_length_days`, `trial_auto_converts` | B3 |
| 5 | Comprehensibility of the credit system | `credit_system_present`, `credit_unit_defined`, `credit_to_output_rate_published`, `credit_rate_location` | C1, C2 |
| 6 | Computability of cost per output | `cost_per_output_unit`, `cost_per_output_computable`, `computation_assumptions`, `cost_per_output_value_usd` (derived) | C3 |
| 7 | Rollover of unused credits | `credit_rollover_policy` | C4 |
| 8 | Charging for failed generations | `failed_generation_charge_policy` | C5 |
| 9 | Auto-renewal | `auto_renewal_default`, `auto_renewal_disclosure_location`, `renewal_notice_commitment` | D1, D2 |
| 10 | Refund and cancellation terms | `refund_policy_exists`, `refund_window_days`, `refund_conditions`, `cancellation_self_serve`, `refund_policy_location` | D3, D4 |
| 11 | Commercial-use rights | `commercial_use_lowest_tier`, `watermark_removal_tier`, `output_ownership_statement` | E1, E2, E3 |
| 12 | Undisclosed or unverifiable limits | `usage_cap_quantified`, `unquantified_limit_clause`, plus `unknown_count` and `determinability_rate` (derived) | F1, F2 |

All twelve domains carry at least one variable and at least one index item.

---

## 10. Data form column order

One row per product per `coder_role`. The published dataset carries the `adjudicated` row where one exists and the `primary` row otherwise.

```
product_id, product_name, category, product_status, paid_submission, entry_tier_name,
coder_role, collection_date, recheck_date, primary_source_url, archive_url, archive_status,
source_urls,

headline_price_usd, headline_billing_basis, first_charge_amount_usd, mandatory_addon_present,
annual_condition_disclosure, annual_default_toggle,
free_plan_exists, free_plan_cap_documented, free_plan_cap_value, free_plan_watermark, free_plan_duration,
trial_exists, trial_card_required, trial_length_days, trial_auto_converts,
credit_system_present, credit_unit_defined, credit_to_output_rate_published, credit_rate_location,
cost_per_output_unit, cost_per_output_computable, computation_assumptions,
credit_rollover_policy,
failed_generation_charge_policy,
auto_renewal_default, auto_renewal_disclosure_location, renewal_notice_commitment,
refund_policy_exists, refund_window_days, refund_conditions, cancellation_self_serve, refund_policy_location,
commercial_use_lowest_tier, watermark_removal_tier, output_ownership_statement,
usage_cap_quantified, unquantified_limit_clause,

conflict_note, coder_note
```

A companion evidence file carries one row per coded value with `product_id`, `variable_name`, `source_url`, `access_date`, and `archive_url`. Derived variables are written to a separate computed file so that the coded record stays exactly as coded.

---

## 11. Instrument stability

No variable may be added, removed, or redefined after the collection window opens. A defect found during collection is recorded in the deviations log under protocol section 12.3 and fixed in a later version, never edited into this one. Wave 2 reuses this instrument, and any change carries an explicit mapping back to the wave-1 variable so that comparison stays possible.
