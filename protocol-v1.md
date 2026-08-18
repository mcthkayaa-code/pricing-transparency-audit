# Research Protocol v1.2

**Pricing Transparency and Subscription Friction in Consumer AI Products: A Cross-Sectional Documentation Audit**

> **Change log — v1.2 final referee clauses, 2026-08-03.** Four clauses the second pass left short are closed, with no change to the version. Item B1's `yes` / `not_applicable` cell now prints the score it takes if adjudication lets the unreachable pair stand, on the convention the `no` row already used, which makes rule G6 and the paragraph under that matrix true of every cell in it. Section 8.3.2.2 no longer states as a blanket rule that a sales-gated price forces `first_charge_amount_usd` to `unknown`: that is the ordinary case, and where a vendor publishes a first-charge figure alongside the gated price, `codebook-v1.md` section 5.2 rule 4 governs and A3 scores from the matrix's money row. The section 6.6 change register gains an entry-type field, `vendor_edit` or `display_variant`, so that rule D9 counts document movement only, while the display variants section 6.8 rule 3 logs feed the section 7.6 display-variance table rather than inflating a movement count. Sections 7.4 step 8 and 7.4.1 take the type name so that a `display_variant` row cannot be read as the register evidence a `date_explained` classification requires. Index weights, the item set, the variable set, and the frame definition are unchanged, so this pass sits inside **section 12.2's before-the-window clause** and the version stays at 1.2.

> **Change log — v1.2, 2026-08-03. Second referee pass.** Every scoring surface is closed against a coder reaching a state the rules do not define. Item B1's value-pair matrix now covers all twenty-four combinations, item A3's dagger note carries its converse, item B3 names its one impossible pair, and rule G4 takes the same matrix-precedence clause rule G3 already carried, which removes the contradiction between G4 and the A3 matrix's `not_applicable` row. Rule G0 gains an item-level definition of determinacy, so `determinability_rate` no longer leaves the four multi-variable items undefined. The mid-window change register re-opens contractual documents as well as pricing pages, because section 6.2's contractual class moves inside a week as readily as a price does. New section 6.8 fixes what a coder does when one pricing page loads in different default states across two reads, section 7.4.2 classifies that disagreement `variant_explained`, and the exposure joins the limitations register at item 13. Section 8.2 states as rule D10 the twice-reported index that section 10.3 already promised. Section 12.2 gains the before-the-window clause that versions 1.1 and 1.2 both actually rest on, and the v1.1 entry's citation below is corrected to name it. Index weights, the item set, the variable set, and the frame definition are unchanged.

> **Change log — v1.1, 2026-08-03. Referee pass.** The scoring rules are closed: `determinate` is defined as a global term, item A3 carries a full value-pair matrix, every index item now states its `unknown`, `conflicting`, and `not_applicable` outcome, multi-variable items carry an explicit rule for a `not_applicable` sub-variable and an item-level `unknown` definition, and both sensitivity analyses inherit the suppression guard and the band table. The two weighting judgments a referee could not check — the F1/F2 double count and the `non_usd` deduction — are now argued in the open, and USD-centricity joins the limitations register. Reliability gains a date-drift rule so that a mid-window price change is not scored as coder disagreement. The eight questions previously left open are ratified and folded into the binding sections, so section 13 is removed: nothing in it was still open. Index weights, the item set, the variable set, and the frame definition are unchanged, which makes this a minor bump under **section 12.2's before-the-window clause**.

| Field | Value |
|---|---|
| Protocol version | 1.2 |
| Protocol date | 2026-08-03 |
| Revision date | 2026-08-03 |
| Study status | Pre-registration. Data collection has not started. |
| Responsible human | Mucahit Kaya, Founder and Editor, AI Tools Police |
| Contact | info@aitoolspolice.com |
| Companion documents | `sampling-rules.md` (frame and selection), `codebook-v1.md` (measurement instrument) |
| Registration statement | This protocol is published before the collection window opens. The research question, the variable set, the index weights, and the analysis plan below are fixed as of the protocol date. |

Every section of this protocol is binding on the study.

---

## 1. Study identification

- **Working title.** Pricing Transparency and Subscription Friction in Consumer AI Products: A Cross-Sectional Audit of [N] Products Across [C] Categories.
- **Title placeholders.** `[N]` and `[C]` are placeholders, not estimates. Both are set once, from the frozen frame file produced under `sampling-rules.md` section 3, and the title is not written out with numbers before that moment. At protocol date the frame would give 76 and 15, but the protocol-date figure never enters a sentence reporting a result, a title, a headline, or a chart caption. `sampling-rules.md` section 9.4 extends the same rule to every published fragment.
- **Wave.** 1 of an intended annual series.
- **Study type.** Cross-sectional documentation audit of public vendor materials. Observational. No intervention, no human subjects, no personal data.
- **Planned outputs.** An academic preprint, an open dataset with a published codebook and per-value sources, a per-product **AI Pricing Transparency Index (APTI), a determinability index**, a reader-facing summary on aitoolspolice.com, and corrections to our own published investigations where the audit finds a discrepancy.
- **Dataset license and identifier.** The dataset, the codebook, and the frame file are published under **CC BY 4.0**. A **DOI is minted through Zenodo at publication**, not reserved beforehand, and the preprint cites it. Reuse requires attribution and nothing else.

---

## 2. Research question and non-claims

### 2.1 Primary question

**Can a prospective buyer determine an AI product's true cost and subscription terms before paying, using only the vendor's public materials?**

### 2.2 Operational sub-questions

- **RQ1.** For each product, which of the twelve cost and terms constructs defined in the codebook can be determined from official public documents, and which cannot?
- **RQ2.** Where a headline price is advertised, how far does it sit from the amount the vendor's own documents say a buyer pays at first charge?
- **RQ3.** Where output is metered through credits, is the credit-to-output rate published well enough for a reader to compute a cost per output?
- **RQ4.** Where are renewal, refund, and cancellation terms disclosed, and how far are those disclosures from the price a buyer sees first?
- **RQ5.** Across the portfolio, how much of the total cost picture stays undeterminable before purchase?

### 2.3 What this study does not claim

These non-claims are fixed before collection and must appear in every published artifact from this study.

1. It does not test whether AI products are expensive, or whether any price is fair. Cost level is not the subject. Determinability of cost is.
2. It does not measure product quality, output quality, or performance.
3. It does not measure what buyers experience after paying. A documented refund policy is recorded as documented, not as honored.
4. It does not test vendor intent. An undocumented term is coded as undocumented, never as concealment.
5. It does not generalize to the AI market. The frame is our own published portfolio, described in `sampling-rules.md`.
6. It does not rank vendors by value for money. A clear disclosure of an unfavorable term scores exactly as high as a clear disclosure of a favorable one.
7. It involves no product use, so it supports no first-hand performance claim of any kind.

---

## 3. Design and rationale

The design is a cross-sectional documentation audit. One collection window, every product in the frozen frame coded inside it, one standard instrument applied to all of them.

The design follows from the question. The question asks what a diligent reader can work out from public materials before paying. That is a property of the documents, so the documents are the data. Using a product would answer a different question, and this publication does not run hands-on trials in any of its work. The method here is documentary by design, and the study says so plainly rather than treating it as a shortfall.

A cross-sectional design also fits the object being measured. Pricing pages change continuously, so a single dated snapshot per product is the only honest unit of observation. Anything longer would blend states of the world that never coexisted. The narrow window keeps the products comparable to each other, and dating every record keeps them comparable to a later wave.

Data already held in our published investigations is not reused as study data. Those pages were verified on scattered dates over more than a year, and mixing them would break the one property the design depends on. Existing pages serve as a discovery aid for locating a vendor's documents, and nothing more.

The design cannot answer causal questions and is not asked to. Every planned statistic is descriptive.

---

## 4. Sample

The full definition lives in `sampling-rules.md`. Summary:

- **Frame.** Every product with a published AI Tools Police investigation live at the moment the frame is frozen. At protocol date this is 76 products across 15 categories.
- **Census, not sample.** All products in the frame are coded. No random selection takes place, and no inference to a wider population is drawn. Published findings carry the frame in the sentence: "of the N products we investigated".
- **Strata.** Product category (15 categories) and product status (active or discontinued).
- **Discontinued products.** Coded from archived materials where those exist, reported in a separate table, excluded from all aggregate transparency metrics and from the index.
- **Known imbalance.** Category sizes run from 1 to 9 products. This rules out cross-category inferential statistics. Section 8.2 fixes the reporting rule for small groups.

---

## 5. Variables and instrument

`codebook-v1.md` is the measurement instrument. It defines every variable, its type, its allowed values, the decision rule a coder applies, the evidence required, and a worked example. It covers all twelve measurement domains and maps each variable to its domain.

No variable may be added, removed, or redefined after the window opens. A defect discovered during collection is handled under the deviation rule in section 12.3.

---

## 6. Data collection procedure

### 6.1 Window

- Target length 7 days. Maximum 14 days.
- The window opens on the date the frame is frozen and closes on the date the final-day re-check completes.
- Every record carries its own collection date. A record collected on day 6 is dated day 6, not dated to the window.

### 6.2 Source hierarchy

Only official vendor sources are valid for coding. Third-party sources, our own published investigations, and vendor marketing carried on other sites are discovery aids only and never a coded value's source.

Authority depends on the class of variable being coded, because the document that governs a price is not the document that governs a contract term. The two-class hierarchy below is binding. It refines the single hierarchy in the study dossier, and that refinement is ratified rather than provisional.

| Variable class | Authority order (highest first) |
|---|---|
| **Pricing variables.** Price, plan composition, free-tier limits, credit rates, trial terms | 1. Live pricing page. 2. Official product documentation or help center. 3. Terms of service or dedicated policy page. 4. Other official vendor pages. |
| **Contractual variables.** Refund, cancellation, auto-renewal, output ownership, commercial-use rights | 1. Terms of service or the dedicated policy page. 2. Official product documentation or help center, including billing and order help articles. 3. Live pricing page. 4. Other official vendor pages. |

Documentation and the help center sit second in both classes. The classes differ only in which document leads and where the pricing page falls.

Where two sources disagree and one outranks the other for that variable class, the value is coded from the higher source, and the disagreement is recorded in `conflict_note` with both URLs. Where two sources of equal authority disagree, the value is coded `conflicting`.

A gap between what a marketing page claims and what the contract says is a finding in its own right, not noise to be resolved and forgotten. Every such divergence stays in `conflict_note` with both URLs even where the hierarchy settles the coded value cleanly, and the count of records carrying one is reported in the paper.

### 6.3 Documents-only rule

The following are prohibited at every step of this study. A coder who cannot proceed without one of them codes `unknown` and moves on.

1. Creating an account of any kind, including a free account.
2. Signing in with an existing account.
3. Starting a checkout, building a cart, or entering payment details.
4. Starting a trial.
5. Using the product.
6. Contacting the vendor for clarification during the window. This prohibition is ratified, not provisional. A term a vendor explains privately by email is not a term a buyer can determine before paying, so resolving an `unknown` that way would answer a question this study is not asking.
7. Coding any value from a third-party source.

"Checkout-equivalent documentation" means an official vendor page that states what a buyer is charged at purchase, such as a billing FAQ, an order help article, or the terms of service. It never means a live checkout flow. No checkout is opened at any point in this study.

Reading a public page is permitted in full. A coder may scroll a pricing page, expand an accordion on it, and switch a monthly or annual display toggle after recording the page's default state, because none of those creates an account or starts a purchase. Following a link from an official page to another official page is likewise permitted. The line is drawn at any action that identifies the reader to the vendor or begins a transaction.

`unknown` is a result, not a failure. The volume of `unknown` values is one of the study's primary findings, and coders are instructed never to close a gap by inference.

### 6.4 Archival

- Every source page is snapshotted on the date it is read.
- Snapshotting means submission to a public web archive, with the returned archive URL stored in the record.
- If submission fails twice, a local HTML copy is saved under the product's record and `archive_status` is coded `local_copy_only`.
- Where no snapshot of any kind can be taken, `archive_status` is coded `archive_failed` and no value may be coded from that page.
- **No value may be coded from a page that has not been snapshotted the same day.**

**What the published dataset carries.** Every published value carries its source URL and its public archive link. Where public archiving failed, the record carries the `archive_status` flag in place of the archive link, and the local snapshot is retained privately for audit. **No local HTML is published**, and no vendor page content is republished in any form. A reader who wants to check a flagged value has the source URL, the access date, and a stated reason the archive link is missing; a reader who wants the snapshot itself can request the audit copy. This keeps the evidence trail intact without redistributing vendor pages.

### 6.5 Currency

- Reporting currency is USD.
- Where a vendor publishes its own USD price, that figure is used exactly as published.
- Where a vendor publishes no USD price, the variable is coded `non_usd`, the currency code and the published figure are recorded verbatim in the note field, and no conversion is applied. We do not invent an exchange rate.
- `non_usd` records are excluded from monetary aggregates and included in every determinability variable and in the index.

### 6.6 Mid-window change rule

1. On the final day of the window, the primary pricing page of every product in the frame is re-opened and compared against its collection-day snapshot. **The same re-check covers every contractual document a coded value was taken from** — the terms of service, the refund or cancellation policy page, the billing help article, and any other official page a contractual value was read from. The list is mechanical rather than a judgment: it is the record's `source_urls`, and each document is compared against its own archive reference. Section 6.2's contractual class carries roughly fifteen variables, and a refund window or a renewal clause can be rewritten inside a week as readily as a price can, so a register that re-opened pricing pages alone would leave those variables unchecked and would let a contractual edit reach the reliability statistics disguised as coder disagreement.
2. Any difference is logged in the change register with the product id, the **entry type**, the variable class affected, both dates, and both archive URLs. The entry type is `vendor_edit` or `display_variant`: `vendor_edit` records that the document itself changed between the two reads, `display_variant` that the same unedited document was served in two different default display states, which is the section 6.8 case. Both are found by the same comparison, which is why they share one register, and they are reported separately wherever the register is reported.
3. Where a change affects a coded value, the affected variables are re-collected in full, with a new date and a new snapshot.
4. The later read is the published value. The earlier record is retained in the dataset, not overwritten.
5. The change register is published with the dataset and reported in the paper as a count and a list, broken out by entry type and by variable class. Movement in a vendor's published prices or in its published terms inside a one-week window is itself a result.

### 6.7 Execution sequence

Applied to each product in the frozen frame, in this order.

1. Open the record from the standard data form, in the codebook's column order.
2. Open the vendor's live pricing page. Record the URL and the access date in ISO 8601 format.
3. Snapshot the page under section 6.4. Record the archive URL and `archive_status`. The snapshot must show the page in the default display state that section 6.8 requires the coder to record.
4. Code every variable whose authority class puts the pricing page first, following each variable's decision rule exactly.
5. Open the terms of service, the refund or cancellation policy page, and the billing help center articles. Repeat steps 2 and 3 for each document opened.
6. Code every variable whose authority class puts a contractual document first.
7. Apply section 6.2 where sources disagree. Record `conflict_note` where a higher source overrides a lower one.
8. Where no official document states a determinate value after steps 4 through 7, code `unknown`. Do not infer a value from marketing language, from a competitor's page, from a third-party review, or from our own published investigation of the same product.
9. Code `not_applicable` only where an official document establishes that the construct does not exist for this product. Absence of evidence is `unknown`, not `not_applicable`.
10. Apply the currency rule in section 6.5.
11. Close the record. A record is complete when every variable carries a value, and every value other than `not_applicable` carries at least one source URL, an access date, and an archive reference.
12. Route the product to second coding if the selection rule in `sampling-rules.md` section 8 includes it.
13. After the final-day re-check in section 6.6, freeze the record.

### 6.8 The default display state is an observation, not a constant

Several rules anchor a coded value to the pricing page's **default display state**: the entry-tier price basis in `sampling-rules.md` section 7.2, `headline_price_usd`, `first_charge_amount_usd`, `annual_default_toggle`, and the price input to `cost_per_output_computable`. All of them assume the page has one default state. It may not. A vendor can run an A/B test, vary the page by inferred geography, or key the preselected billing toggle to a cookie, and two readers loading the same URL on the same day can then see different states through no fault of either.

The rule, binding on every coder and every pass:

1. **The coder records the state observed, and archives the page in it.** The default display state is whatever that load showed before any interaction. It is never reconstructed from what the page showed on a different read or to a different reader.
2. **The archive snapshot is the proof.** Every value anchored to the default state rests on a snapshot that shows the state it was read in. Section 6.4 already forbids coding from an unsnapshotted page; this adds that the snapshot must show the state, not merely the page.
3. **A coder who notices a variant records it.** Where the same URL visibly loads in a different state on a later read within the same pass, the coder logs both states, both times, and both snapshots in `coder_note` and reports the product to the change register under section 6.6. **The entry is typed `display_variant`, not `vendor_edit`**, because nothing here establishes that the vendor edited the document, and section 8.2's rule D9 counts edits only.
4. **No coder reloads to hunt for a preferred state.** Reloading until the page serves the cheaper display would manufacture a value the buyer may never see. Where a reload happens for an unrelated reason and the state differs, rule 3 applies.
5. **Cookies and consent are handled as the privacy rule requires**, declining non-essential cookies, and the coder records that the page was read in that condition. A default state observed after declining non-essential cookies is the state this study codes, because it is the state a reader who declines them sees.

What this rule does not do is make the state determinate. It makes the state **recorded**, which is what lets a disagreement between two passes be diagnosed rather than argued about. Section 7.4.2 handles the diagnosis, and item 13 of section 9 records what remains exposed.

---

## 7. Reliability plan

### 7.1 Primary coding

One primary coding pass per product completes the full form under section 6.7. Coding passes are AI-assisted and run under named human editorial control, as described in section 11.

### 7.2 Second coding

- **Share.** At least 25% of active products, stratified so that every category contributes at least one product.
- **Selection.** Deterministic and published in advance. `sampling-rules.md` section 8 gives the rule. Under the current category profile it selects roughly 25 of 76 products, about a third of the frame, comfortably above the floor.
- **Contingency.** If collection capacity requires it, the selection interval may be widened to every fifth product, which yields about 26% and still meets the floor. The interval actually used is recorded in the dataset and stated in the paper. No other change to the selection rule is permitted after the window opens.
- **Date on the record.** The second coder writes their own `collection_date` on their own record. The two passes will rarely land on the same day, and a reliability figure computed without knowing the gap would silently charge the coders for the vendor's edits.

### 7.3 Blinding

The second coder receives the product name and the vendor's home URL. Nothing else. The second coder does not see the first record, does not see any partial values from it, and does not see our published investigation of the product. The second pass locates the vendor's documents independently, which also tests whether the documents are findable at all.

### 7.4 Adjudication

1. Records are compared variable by variable after both passes close.
2. Every disagreement goes to a third adjudication pass that reads both records and both sets of sources.
3. The adjudicator decides by applying the codebook decision rule to the evidence. Majority does not decide anything, because there are only two prior records and agreement between them is not evidence of correctness.
4. The adjudicator records a dated note stating which rule resolved the disagreement.
5. Where the rule cannot resolve it, the value is coded `unknown` and the note explains why. An unresolvable disagreement between two careful readers is itself evidence that the documents do not determine the answer.
6. Adjudicated values replace both prior values in the published dataset. Both prior values are retained in the reliability file.
7. **Date drift.** Before a disagreement is adjudicated, the two records' `collection_date` values are compared against the change register in section 6.6. Where the register shows the vendor changed the relevant page between the two dates, and the change accounts for the difference, the disagreement is classified `date_explained` in the reliability file. The adjudicator still decides the published value under step 3, using the later read.
8. **Display variance.** Where the two records' archive snapshots of the same URL show different default display states and **no** `vendor_edit` entry in the change register accounts for the difference, the disagreement is classified `variant_explained`. The adjudicator codes from the **later snapshot** and records which snapshot was used. Section 7.4.2 governs.

#### 7.4.1 Date-explained disagreements

A `date_explained` disagreement is not a measurement failure. It is the instrument correctly recording two different states of the world. Counting it against agreement would understate the instrument and overstate the vendors, since a fast-moving pricing page would read as coder unreliability.

- `date_explained` disagreements are **excluded from the primary agreement statistic** in section 7.6.
- They are **reported separately**, as a count, a per-variable breakdown, and a list of the products involved.
- The classification requires a matching `vendor_edit` entry in the change register. A disagreement with no such entry is an ordinary disagreement, whatever the dates say, and a `display_variant` entry never supplies it, since it records no edit. Coders and the adjudicator may not reclassify a disagreement as date-explained to improve a figure.

#### 7.4.2 Variant-explained disagreements

A `variant_explained` disagreement is the case section 6.8 anticipates: two passes archived the same URL in different default display states, and no change-register entry says the vendor edited the page between them. The likeliest explanations are an A/B test, geographic variation, or a cookie-keyed billing toggle.

- **The classification requires two archive snapshots showing the two states.** A coder's recollection of what the page looked like is not evidence, and a disagreement with no such snapshot pair is an ordinary disagreement. This mirrors the register requirement in section 7.4.1 and exists for the same reason: neither classification may be reached for by anyone who wants a better figure.
- **`variant_explained` disagreements stay inside the primary agreement statistic** in section 7.6. This is the deliberate difference from `date_explained`, and the reasoning is worth stating because the two look alike. A date-explained disagreement records two states of the world that a reader could not have seen at once; a variant-explained disagreement records two states the vendor was serving **simultaneously**, either of which a real buyer could meet on a single visit. The term is then not determinate for that buyer, which is the property this study measures, so the disagreement is a genuine one and is counted as such.
- **They are also reported separately**, as a count, a per-variable breakdown, and a list of the products involved, so that a reader can see how much of the measured disagreement is display variance rather than misreading.
- The adjudicator codes from the later snapshot under section 7.4 step 8. The later snapshot is chosen because it is the one closest to the final-day re-check, not because it is more authoritative; the choice is a tiebreaker, and section 9 item 13 records that it is one.

### 7.5 Human sign-off

Mucahit Kaya reads every adjudicated record and every record carrying a `conflicting` value, and signs off the frozen dataset before any artifact is published. Sign-off is dated and recorded in the dataset. After sign-off the dataset is frozen; later changes run through the corrections policy and a version bump under section 12.

### 7.6 Agreement statistics reported

- **Primary.** Per-variable percent agreement across the double-coded subset, computed before adjudication, published as a table covering every variable. Disagreements classified `date_explained` under section 7.4.1 are excluded from this statistic, and the excluded count prints in the table beside each affected variable.
- **Secondary.** Krippendorff's alpha across the double-coded subset, for variables where at least two values were observed. Alpha is unstable at this subset size and is published for transparency, not used as a pass or fail gate. Alpha uses the same exclusion.
- **Third.** A separate date-drift table: the count of `date_explained` disagreements, the variables affected, and the products involved. It is published whether the count is zero or large, because it measures how fast the documents move rather than how well the coders read them.
- **Fourth.** A display-variance table alongside it: the count of `variant_explained` disagreements under section 7.4.2, the variables affected, and the products involved, published on the same terms whether the count is zero or large. **The same table carries the `display_variant` entries from the section 6.6 change register**, counted on their own line, which is how a variant observed inside a single pass under section 6.8 rule 3 reaches a reader at all, and which is the count section 9 item 13 promises. Unlike the date-drift table it is not an exclusion table, since those disagreements remain inside the primary statistic; it reports how much of the measured disagreement came from a vendor serving two states at once.
- **Threshold, fixed here.** Any variable with percent agreement below 80% is flagged low-reliability. Every finding that rests on a flagged variable carries an explicit reliability caveat in the paper, next to the finding rather than in a footnote.
- Agreement is reported whatever it turns out to be. A poor figure is published, not suppressed.

---

## 8. Pre-registered analysis plan

### 8.1 Principles

1. Every statistic in sections 8.2 through 8.5 is fixed as of the protocol date.
2. All primary analysis is descriptive. No hypothesis test, no p-value, and no confidence interval appears in the primary results. The frame is a census of our own portfolio, so inferential statistics would imply a sampling process that does not exist.
3. Analysis for this wave produces no trend claims. There is no prior wave.

### 8.2 Descriptive statistics

- **D1.** For every categorical variable, a frequency table over its allowed values, with `unknown`, `not_applicable`, and `conflicting` shown as their own rows rather than dropped.
- **D2.** Every percentage prints with its denominator, in the form "x of N". Bare percentages are not published in any artifact from this study.
- **D3.** Percentages are reported only for groups with n of 5 or more. Smaller groups are reported as raw counts.
- **D4.** For continuous variables, the median and interquartile range, plus the minimum and maximum. The mean is not the primary summary, because n is small and the distributions are skewed by outliers. Where a mean is shown, it sits beside the median, never instead of it.
- **D5.** Monetary aggregates exclude `non_usd` records. The count of excluded records prints with every monetary aggregate.
- **D6.** Determinability reporting: the share of applicable index items coded `unknown`, computed overall, per measurement domain, and per product.
- **D7.** Category-level tables are descriptive. No inferential test, no significance claim, and no statement that one category differs from another as populations.
- **D8.** Discontinued products appear in their own table and enter no aggregate and no index.
- **D9.** The change register from section 6.6 is reported as a count of products whose pages moved inside the window, with the list, broken out by variable class so that pricing movement and contractual movement are separable. The count covers `vendor_edit` entries only, because D9 measures how far the documents moved. A `display_variant` entry is not movement — it records one unedited document served in two states — and those entries are reported in the display-variance table under section 7.6 instead, so that neither figure absorbs the other.
- **D10.** Every index result is reported twice, once over the full frame and once with `paid_submission = yes` records removed, per section 10.3. This binds the primary APTI table, both sensitivity analyses, the component tables, and every index figure quoted in prose or in a chart, in the paper and in the reader-facing summary alike.

### 8.3 The AI Pricing Transparency Index (APTI)

The index scores **determinability**, meaning how much of a product's cost and terms a reader can establish from public documents before paying. It does not score generosity, value, or consumer-friendliness. A vendor that clearly states "no refunds under any circumstances" earns the same points as a vendor that clearly states a 30-day unconditional refund, because both readers know what they are buying. Friction outcomes are reported separately as descriptive findings under section 8.2, not folded into the index.

The index is computed only for active products.

#### 8.3.1 Global scoring rules

**G0. `determinate`, defined once for the whole study.** A coded value is **determinate** when official documents settle what the term is, so that a reader could state it before paying. Every scoring rule below uses the word in this sense, and so does `determinability_rate` in `codebook-v1.md` section 8.

- `unknown` is never determinate.
- `conflicting` is never determinate.
- `not_applicable` **is** determinate. A construct the documents establish does not exist is a question the reader has answered, not a question left open. It still leaves its item out of the index under G2, because determinacy and index membership are separate properties, **except as a sub-variable of a multi-variable item, where G4 governs.**
- `absent` is determinate on item F2 alone, the one item where `absent` earns full points. There, `absent` records that the coder read the terms and the plan documentation and found no unquantified limit clause, which is a documented finding. On items A2 and D2 the same value records that a required disclosure was made nowhere, which is precisely the non-determination those items measure, so there `absent` is not determinate and scores zero.
- Every other value on every variable's list is determinate.
- **Determinacy at the item level.** The bullets above define determinacy for a coded value. An **item** is determinate when every sub-variable feeding it is determinate; a multi-variable item with any non-determinate sub-variable is not. A single-variable item inherits its variable's determinacy directly. This is the definition `determinability_rate` uses in `codebook-v1.md` section 8, and it is what makes that ratio computable for A3, B1, B2, and B3, whose determinacy would otherwise be undefined. Item-level determinacy and item score are separate properties: item B2 with one determinate and one `unknown` sub-variable scores 3 of 5 and is **not** determinate, because the reader still cannot state one of the two terms.

**G1.** `unknown` scores 0 and stays in the denominator. This is the study's central stance: an undisclosed term is the buyer's burden, not a missing observation.

**G2.** `not_applicable` removes the item from the numerator and from the denominator.

**G3.** `conflicting` scores one third of the item's points, rounded to one decimal, because the buyer can see both statements and cannot determine which governs. On a multi-variable item, a `conflicting` sub-variable is treated as non-determinate when the item's row is applied, and the item's score is then raised to one third of the item's points if the row returned less. Where an item publishes its own value matrix, the matrix governs and G3 adds nothing to it.

**G4. Multi-variable items and `not_applicable` sub-variables.** Four items score from more than one variable: A3, B1, B2, B3. On these, a sub-variable coded `not_applicable` **counts as determinate**, and the item keeps its full point value. The item does not shrink, and no item carries a fractional maximum. An item becomes `not_applicable` itself, and leaves numerator and denominator under G2, only where **every** one of its sub-variables is `not_applicable`. **Where an item publishes its own value matrix, the matrix governs and G4 adds nothing to it.**

The precedence clause matters on A3, and it is the reason the clause is written here rather than assumed. The A3 matrix in section 8.3.2.1 removes the item wherever `first_charge_amount_usd = not_applicable`, including where `mandatory_addon_present` carries an ordinary value. Read without the precedence clause, G4 would instead keep A3 in the index at its full 5. The matrix wins, and note 5 under it explains why the pair the conflict turns on cannot legitimately occur in the first place: `first_charge_amount_usd = not_applicable` means no paid tier exists, which forces `mandatory_addon_present` to `not_applicable` as well, which is the every-sub-variable case G4 and the matrix already agree on. The clause settles the reading; the note removes the state.

The case G4 settles on its own, where no matrix intervenes: a product whose principal output cannot carry a watermark, which does publish a free plan documented as perpetual, has `free_plan_watermark = not_applicable` and `free_plan_duration = perpetual`. Both count as determinate, so item B2 scores its full 5 rather than being marked down for a question that does not exist. A product with no free plan at all has both sub-variables `not_applicable`, so B2 leaves the index entirely.

**G5. Item-level `unknown`.** The derived `unknown_count` counts items rather than variables, so an item needs an unknown state of its own.

- A single-variable item is `unknown` when its variable is `unknown`.
- A multi-variable item, meaning A3, B1, B2, or B3, is `unknown` when it scores zero **and** at least one of its sub-variables is `unknown`.
- A multi-variable item scoring above zero is never counted as `unknown`, even where one sub-variable is. The partial credit already records the partial disclosure, and counting it twice would inflate the study's headline figure in our own favor.
- An item scoring zero with no `unknown` sub-variable, such as a documented free plan whose caps are all unquantified, is a disclosure failure of a different kind and is not counted as `unknown`.

**G6.** Any other value scores as specified in the item's row below. Every item's row states an outcome for `unknown`, `conflicting`, and `not_applicable`, so no coded value can reach an item without a defined score.

#### 8.3.2 Component A. Headline price integrity (20 points)

| Item | Points | Scoring |
|---|---|---|
| A1 Headline price published | 8 | Numeric USD price for the entry paid tier, or a published unit rate for a usage-priced product: 8. `non_usd`: 4. `no_public_price`, the price gated behind a sales contact: 0. `unknown`: 0. `conflicting`: 2.7. `not_applicable`: item removed. |
| A2 Annual-billing condition disclosed | 7 | `adjacent`: 7. `same_page_secondary`: 5. `one_click_away`: 2. `absent`: 0. `unknown`: 0. `conflicting`: 2.3. `not_applicable`: item removed. |
| A3 First-charge amount determinable | 5 | Scored from the value-pair matrix in section 8.3.2.1. |

##### 8.3.2.1 Item A3 value-pair matrix

A3 scores from two variables, `first_charge_amount_usd` and `mandatory_addon_present`, and the pair has thirty combinations. All thirty are scored here rather than left to a coder's reading. A combination that one coder scores 0 and another scores 5 does not measure anything.

The principle behind the numbers: A3 asks whether a buyer can state, as a single figure, what her card is charged the first time. Five points means she can. Two means she can state a figure that is a floor rather than a total, or can state it only in a currency the vendor never converted to USD. One point seven is the G3 conflict share. Zero means she can state no figure at all.

Rows are `first_charge_amount_usd`. Columns are `mandatory_addon_present`.

| | `no` | `yes_amount_stated` | `yes_amount_unstated` | `unknown` | `conflicting` | `not_applicable` |
|---|---|---|---|---|---|---|
| money value | 5 | 5 | 2 | 2 | 2 | 5 † |
| `non_usd` | 2 | 2 | 0 | 0 | 1.7 | 2 † |
| `unknown` | 0 | 0 | 0 | 0 | 0 | 0 † |
| `conflicting` | 1.7 | 1.7 | 1.7 | 1.7 | 1.7 | 1.7 † |
| `not_applicable` | item removed † | item removed † | item removed † | item removed † | item removed † | item removed |

What the matrix rests on:

1. **A stated add-on amount costs nothing.** A buyer given a $29 plan price and a mandatory $10 module can add. Both figures are published, so the first charge is determinable, and `money` with `yes_amount_stated` scores the full 5.
2. **An unknown add-on scores as an unstated one, and this is a judgment we are making in the open.** In both states the buyer holds a numeric plan price and cannot bound the total, so her position is identical and the score is identical at 2. Scoring `unknown` at 0 would put a buyer who knows the plan price level with one who knows nothing, which is false. Scoring it at 5 would treat silence as a guarantee that no add-on exists, which is the inference section 6.3 forbids. Two is the honest middle, written down so that no coder has to invent it.
3. **`non_usd` compounds.** A vendor publishing only a non-USD figure scores 2 where the add-on position is settled and 0 where it is not, because the buyer then faces two open quantities at once rather than one. Section 8.3.10 argues the `non_usd` deduction itself.
4. **`first_charge_amount_usd = unknown` fails the item outright.** The item is named for the amount. Where the amount is undeterminable, no state of the add-on variable rescues it, and the G3 floor does not reach across from the other sub-variable.
5. **† A daggered cell holds a value pair the coding rules cannot produce.** Both `not_applicable` values in this pair mean the same thing — no paid tier exists — so neither variable can carry it alone.
   - **The column.** `mandatory_addon_present = not_applicable` cannot co-occur with any first-charge value other than `not_applicable`. A record landing in the daggered right-hand column is returned for re-coding. If the pair survives adjudication, the cell scores as its row's `no` column.
   - **The row, which is the converse.** `first_charge_amount_usd = not_applicable` cannot co-occur with any other add-on value; a record landing in the `not_applicable` row with any other column is returned for re-coding. If the pair survives adjudication, the item is removed, as the row prints.
   - **The undaggered corner.** `not_applicable` on both is the reachable, ordinary case: no paid tier exists, every sub-variable of A3 is `not_applicable`, and the item leaves the index under G2 with G4 and the matrix agreeing.
   - This row is where the matrix and rule G4 would part company if the pair were reachable. G4's precedence clause fixes the reading — the matrix governs — and this note removes the state that made the question live.
6. Where A3 scores above zero on a computed rather than a directly read figure, `computation_assumptions` records the arithmetic under `codebook-v1.md` section 7.

##### 8.3.2.2 A1 and A3 interaction

A1 and A3 read different variables and score independently. Four pairings the coding rules produce in the ordinary case are nonetheless stated here so a reader can check them rather than discover them.

- **A1 = `no_public_price`.** The entry tier's price is gated behind a sales contact, so ordinarily no official document states what the first transaction charges and `first_charge_amount_usd` is `unknown`. The matrix's `unknown` row scores 0 whatever the add-on column holds, so the pair scores 0 of 13. What A1 = `no_public_price` does **not** do is force `unknown` across the rest of the record: `codebook-v1.md` section 5.2 enumerates the entry-tier variables and fixes the rule, which is that a term the vendor publishes for the gated tier is coded from the document publishing it. A sales-gated vendor that publishes a 14-day trial and a 30-day refund window is coded as publishing them, and can score on B, C, D, and F while scoring 0 of 13 here. Where the vendor publishes a first-charge figure alongside the gated price, `codebook-v1.md` section 5.2 rule 4 governs and A3 scores from the matrix's money row.
- **A1 = `not_applicable`.** No paid tier exists, so `first_charge_amount_usd` is `not_applicable` too. A1, A2, and A3 leave the index together and the free-tier items carry the record.
- **A1 = `unknown`.** A paid tier exists but no price figure could be located in any official document, so no first-charge figure can exist either. A3 is 0.
- **A1 = `non_usd` with A3 = a money value** is legitimate, not a coding error. A vendor may headline a euro figure on the pricing page and state a USD total in a billing article. Each item scores on its own value: A1 4, A3 from the matrix's money row.

The reverse pairing, A1 as a money value with A3 `unknown`, is legitimate and expected to be common. It is the case where a pricing page publishes a monthly figure and no document anywhere states the billing frequency.

#### 8.3.3 Component B. Free tier and trial clarity (15 points)

| Item | Points | Scoring |
|---|---|---|
| B1 Free-tier position determinable | 5 | Scored from the matrix in section 8.3.3.1. |
| B2 Free-tier restrictions disclosed | 5 | Count the determinate sub-variables among `free_plan_watermark` and `free_plan_duration`, applying G0 and G4. Both determinate: 5. One: 3. Neither: 0. A `conflicting` sub-variable is non-determinate for the count, and the G3 floor of 1.7 applies afterward. The item is `not_applicable`, and removed, only where both sub-variables are `not_applicable`, which is the no-free-plan case. |
| B3 Trial terms determinable | 5 | `trial_exists = no`: 5. `trial_exists = yes` with `trial_card_required` and `trial_length_days` both determinate: 5. One of the two: 3. Neither: 0. `trial_exists = unknown`: 0. `trial_exists = conflicting`: 1.7. `not_applicable` is unavailable on `trial_exists`, so B3 is never removed from the index. **Impossible pair.** `not_applicable` on `trial_card_required` or on `trial_length_days` means no trial exists, so `trial_exists = yes` with either sub-variable `not_applicable` is not reachable and is returned for re-coding. Where `trial_exists = no`, both sub-variables are `not_applicable` and the item scores 5 on the first clause, not on the count. |

##### 8.3.3.1 Item B1 matrix

B1 scores from `free_plan_exists` and `free_plan_cap_documented`.

| `free_plan_exists` | `free_plan_cap_documented` | Points |
|---|---|---|
| `yes` | `all_quantified` | 5 |
| `yes` | `some_quantified` | 3 |
| `yes` | `none_quantified` | 0 |
| `yes` | `unknown` | 0 |
| `yes` | `conflicting` | 1.7 |
| `yes` | `not_applicable` | Not reachable. `not_applicable` on the cap variable means no free plan exists. Return for re-coding; if the pair survives adjudication, score 5. |
| `no` | `not_applicable` | 5 |
| `no` | any cap value other than `not_applicable` | Not reachable. `free_plan_exists = no` establishes that no free plan exists, so no free-plan limit can be documented, unquantified, unknown, or in conflict. Return for re-coding; if the pair survives adjudication, score 5. |
| `unknown` | any value | 0 |
| `conflicting` | any value | 1.7 |

`free_plan_exists` carries four values and `free_plan_cap_documented` six, so the pair has twenty-four combinations, and all twenty-four are scored above. The two not-reachable rows follow the convention item A3's matrix uses: an unreachable pair is returned for re-coding rather than left to a coder's reading, and a score is nonetheless printed for the case where adjudication lets the pair stand, so that no record can reach this item without a defined outcome.

`free_plan_exists = no` scores the full 5. A vendor publishing only paid tiers has told the buyer exactly where she stands, and B1 measures whether she can find that out rather than whether she likes the answer. That is also why the surviving-adjudication score on the `no` row is 5 rather than the cap variable's own score: the point is already earned by the documented absence of a free plan, and a stray cap value cannot take it back. `free_plan_exists` carries no `not_applicable` value, so B1 never leaves the index.

#### 8.3.4 Component C. Unit-cost comprehensibility (25 points)

| Item | Points | Scoring |
|---|---|---|
| C1 Credit unit defined | 6 | `yes`: 6. `no`: 0. `unknown`: 0. `conflicting`: 2.0. `not_applicable`, where no credit system exists: item removed. |
| C2 Credit-to-output rate published | 7 | `yes`: 7. `partial`: 3.5. `no`: 0. `unknown`: 0. `conflicting`: 2.3. `not_applicable`, where no credit system exists: item removed. |
| C3 Cost per output computable | 5 | `yes`: 5. `partial`: 2.5. `no`: 0. `unknown`: 0. `conflicting`: 1.7. Never `not_applicable`; every product has a principal output unit, including a seat-month, so C3 always sits in the denominator. |
| C4 Rollover policy documented | 4 | `rolls_over`, `partial_rollover`, or `expires_at_period_end`: 4. `unknown`: 0. `conflicting`: 1.3. `not_applicable`, where no credit system exists: item removed. |
| C5 Failed-generation charging documented | 3 | `not_charged`, `charged`, or `case_by_case`: 3. `unknown`: 0. `conflicting`: 1.0. `not_applicable`, where the product has no metered generation step: item removed. |

#### 8.3.5 Component D. Renewal and exit terms (20 points)

| Item | Points | Scoring |
|---|---|---|
| D1 Auto-renewal default documented | 6 | `on`, `off`, or `no_recurring_billing`: 6. `unknown`: 0. `conflicting`: 2.0. `not_applicable` is unavailable on this variable, since `no_recurring_billing` carries the one-time-purchase case, so D1 always sits in the denominator. |
| D2 Auto-renewal disclosure proximity | 4 | `pricing_page`, `purchase_terms_doc`, or `multiple`: 4. `terms_only` or `help_center_only`: 2. `absent`: 0. `unknown`: 0. `conflicting`: 1.3. `not_applicable`, where billing does not recur: item removed. |
| D3 Refund position documented | 6 | `yes` or `no_refunds_stated`: 6. `unknown`: 0. `conflicting`: 2.0. `not_applicable`, where the product has no paid tier and so nothing to refund: item removed. |
| D4 Cancellation route documented | 4 | `self_serve_documented` or `contact_required`: 4. `unknown`: 0. `conflicting`: 1.3. `not_applicable`, where billing does not recur: item removed. |

#### 8.3.6 Component E. Rights and restrictions (10 points)

| Item | Points | Scoring |
|---|---|---|
| E1 Commercial-use tier determinable | 5 | Any determinate tier value, including `not_granted`: 5. `unknown`: 0. `conflicting`: 1.7. `not_applicable`, where the product produces no output a commercial-use right could attach to: item removed. |
| E2 Watermark position determinable | 3 | Any determinate tier value, including `no_watermark` and `never_removed`: 3. `unknown`: 0. `conflicting`: 1.0. `not_applicable`, where the principal output is not an artifact a watermark could mark: item removed. |
| E3 Output ownership stated | 2 | `user_owns`, `vendor_license_retained`, or `conditional`: 2. `unknown`: 0. `conflicting`: 0.7. `not_applicable`, where the product produces no output ownership could attach to: item removed. |

#### 8.3.7 Component F. Residual undisclosed burden (10 points)

| Item | Points | Scoring |
|---|---|---|
| F1 Usage caps quantified | 6 | `all_caps_quantified`: 6. `some_quantified`: 3. `none_quantified`: 0. `unknown`: 0. `conflicting`: 2.0. `not_applicable`, where no paid tier exists: item removed. |
| F2 No unquantified limit clause | 4 | `absent`: 4. `present`: 0. `unknown`: 0. `conflicting`: 1.3. `not_applicable` is unavailable on this variable, so F2 always sits in the denominator. This is the one item in the index where `absent` earns full points, and under G0 it is the one place `absent` counts as determinate. |

Twenty items. One hundred points before any `not_applicable` removal: A 20, B 15, C 25, D 20, E 10, F 10.

#### 8.3.8 Index formula

```
earned    = sum of points scored on applicable items
available = sum of maximum points of applicable items
APTI      = 100 x (earned / available)
```

- Rounded to one decimal, half up.
- **Guard rule.** If `available` is below 50, no index is published for that product. Its component scores and its unknown count are published instead, with a note. This prevents a product measured on a quarter of the instrument from being compared against one measured on all of it.
- **Ties.** Reported as ties. No tiebreaker, no forced ordering.
- **Companion figure.** Every published index value prints alongside `unknown_count`, the number of applicable items coded `unknown`. Two products can reach the same score by different routes, and the reader is shown which.

#### 8.3.9 Bands (fixed here)

| Range | Band |
|---|---|
| 85.0 to 100.0 | Determinable |
| 70.0 to 84.9 | Mostly determinable |
| 50.0 to 69.9 | Partly determinable |
| 30.0 to 49.9 | Largely undeterminable |
| 0.0 to 29.9 | Undeterminable |

The band is assigned from the rounded value.

#### 8.3.10 Why these weights

The weights are a judgment made before any data exists, which is the only condition under which they can be honest. Component C carries the most weight because credit metering is where a headline number and a real bill diverge furthest, and because it is the one construct a reader cannot approximate by guessing. A and D follow, since a price a buyer cannot pin down and a renewal a buyer cannot anticipate are the two failures with direct financial consequence. B sits lower because free-tier and trial terms are recoverable later at no cost. E and F carry the least weight because they bind fewer buyers, though they bind those buyers hard. Section 8.4 publishes an equal-weight variant so readers can see how much of any ordering comes from this judgment rather than from the data.

**The index scores determinability, not generosity.** This bears repeating at the point where the weights are set, because a name containing the word "transparency" invites the opposite reading. A vendor stating "no refunds under any circumstances" earns the same 6 points on D3 as a vendor stating a 30-day unconditional refund. A vendor whose terms grant no commercial use at all earns the same 5 points on E1 as one granting it on the free plan. Both readers know what they are buying, and knowing is the whole of what the index measures. Every artifact from this study names the index as the **AI Pricing Transparency Index (APTI), a determinability index**, so the qualifier travels with the number.

**F1 and F2 double-count one vendor behavior, deliberately.** A pricing page advertising an unlimited allowance that a fair-use clause silently qualifies degrades F1, because the cap is no longer quantified, and scores F2 as `present`, because the qualifying clause carries no number. The same page is therefore marked down twice, and we intend it. The two items measure different reader harms: F1 asks whether a buyer can size the allowance she is paying for, F2 asks whether a clause can shrink that allowance after she has paid. A vendor that publishes real numbers and carries no discretionary clause is in a materially different position from one doing either, and the index says so twice because the buyer carries the burden twice. The pair is 10 of 100 points, so the compounding is bounded, and both items are reported separately in section 8.2 so a reader who disagrees can unpick them.

**`non_usd` is deducted rather than treated as neutral.** Items A1 and A3 dock a product that publishes no USD figure. The reason is a determinability claim about a specific reader: this index reports in USD, and a buyer reading in USD cannot state what she will pay without an exchange rate we refuse to invent under section 6.5. The deduction describes her position, not the vendor's conduct, which is why it is partial rather than a zero — the figure is published, just not in the currency the index reads. This makes the index USD-centric, the limitation is recorded as item 12 of section 9, and every `non_usd` value is identifiable in the published dataset so a reader can recompute without the deduction.

### 8.4 Pre-registered sensitivity analyses

Both are planned analyses, not exploratory ones. Both are published in the paper and in the dataset.

- **S1. Equal weights.** Each component contributes an equal share regardless of its point total.
  ```
  APTI_equal = (100 / k) x sum over components with available > 0 of (earned_c / available_c)
  ```
  where `k` is the number of components with available points above zero. Any product that moves more than one band between APTI and APTI_equal is marked in the published table.
- **S2. Unknown excluded.** Recompute with rule G1 replaced by "an `unknown` item is removed from the numerator and the denominator", everything else unchanged. This is the most favorable reading available to any vendor, and publishing it lets a reader see exactly what our stance on `unknown` costs each product.

#### 8.4.1 Rules S1 and S2 inherit

Both variants are index values and are governed by the same guards as APTI itself. Publishing a sensitivity figure under looser rules than the primary would let the variant carry a claim the primary is not allowed to make.

1. **The guard rule in section 8.3.8 applies to S1 and S2.** A product whose APTI is suppressed for `available` below 50 has its S1 and S2 values suppressed with it. No product appears in a sensitivity table that does not appear in the primary table.
2. **S2 recomputes `available`, and the guard is re-applied to the recomputed figure.** Removing `unknown` items shrinks the denominator, so a product that clears 50 on the primary computation can fall below it on S2. Where that happens, S2 is reported as `suppressed` for that product while its primary APTI still publishes.
3. **The band table in section 8.3.9 applies to S1 and S2**, assigned from each variant's own rounded value. Band movement between the primary and a variant is the finding S1 exists to surface, so both bands print.
4. **Where a recomputed `available` reaches zero, the output is reported as `suppressed`.** It is not reported as 0.0, which would read as a product scoring nothing, and not left blank, which would read as an omission. Under S2 this is the product every one of whose applicable items is `unknown`: the most undeterminable record in the study, and the one the vendor-favorable variant cannot score at all. That result is stated in the paper in those words rather than dropped from the table.
5. The same applies to S1 where `k` reaches zero, meaning no component has available points above zero. That state can only arise alongside a suppressed primary APTI, so rule 1 has already caught it.

### 8.5 Reliability reporting

Section 7.6 statistics are published as their own table in the paper and as a file in the dataset, whatever the values are.

### 8.6 Exploratory work

Anything not specified in sections 8.2 through 8.5, and anything run after the dataset is unblinded, is labeled **exploratory** in the section heading where it appears, not only in a footnote. Exploratory results support no headline, no title, and no summary claim in any artifact from this study.

---

## 9. Limitations register

This register is published in full in the protocol and in the paper. It is not shortened for the reader-facing summary.

1. **The frame is our portfolio, not the market.** Products entered our coverage through editorial and commercial-interest choices, which over-represents categories with strong buyer intent. No finding generalizes to AI products at large.
2. **Category strata are small and unequal.** Sizes run from 1 to 9. Small strata carry counts only, never percentages, and never a cross-category comparison.
3. **Documents-only measures what a reader can determine, not what a buyer experiences.** A documented refund policy is not a honored refund policy. Post-purchase reality sits outside this design.
4. **One window is one snapshot.** Prices move continuously. Section 6.6 measures movement inside the window and reports it, which bounds the problem without solving it.
5. **Partial double-coding.** At least a quarter of active products are coded twice. The rest rest on a single pass plus human review of flagged records. Coding is AI-assisted throughout, under named human editorial control.
6. **English-language public pages only.** A vendor that documents a term clearly in another language is coded as not documenting it, which understates disclosure for non-English-first vendors.
7. **The index is a construct we defined.** It has no external validation, and a different reasonable weighting would produce a different ordering. Sensitivity analysis S1 quantifies that exposure rather than hiding it.
8. **Archiving is imperfect.** Pricing tables rendered by script resist public archiving. A local copy is weaker evidence than a public archive link, and records affected are flagged with `archive_status`.
9. **Undisclosed does not mean nonexistent.** A vendor may explain a term inside a signed-in account. Our `unknown` counts measure public disclosure before purchase, which is the question, and not the vendor's internal clarity.
10. **We hold affiliate relationships with many audited vendors.** Section 10 sets out the mitigations. They reduce the risk of motivated coding. They do not eliminate it, and the published per-value sources exist so a reader can check us.
11. **No prior wave.** Wave 1 establishes a baseline. Nothing in it supports a claim about a trend.
12. **The index is USD-centric.** Items A1 and A3 deduct points where a vendor publishes no USD figure, because the index reports in USD and section 6.5 forbids inventing an exchange rate. For a buyer reading in the vendor's own currency those terms may be perfectly determinable, and the deduction does not describe her. Section 8.3.10 argues why the deduction is kept. Every `non_usd` value is identifiable in the published dataset, so a reader who wants the index without the deduction can recompute it.
13. **A pricing page may not have one default display state.** Several coded values anchor to the state the page loads in, and a vendor running an A/B test, varying the page by inferred geography, or keying the billing toggle to a cookie can serve two states at once. Section 6.8 makes the observed state recorded and archived rather than assumed, section 7.4.2 classifies a two-pass disagreement `variant_explained` and keeps it inside the primary agreement statistic, and the adjudicator's rule of coding from the later snapshot is a tiebreaker rather than a claim that the later state is the true one. What remains exposed is that a single-coded product yields one observation of a state that may not be unique, with nothing to compare it against, and that no method available to a documents-only study can detect a variant a coder was never served. Records where a variant was observed are flagged, and the count is published under section 7.6.

---

## 10. Ethics, conflicts of interest, and funding

### 10.1 Funding

No external funding. No grant. No vendor paid for this study, contributed to its design, or saw any part of it before publication. The work is produced with the publication's own resources.

### 10.2 Affiliate relationships

AI Tools Police is reader-supported and holds affiliate relationships with many of the vendors in this frame. Purchases made through links on our site may earn us a commission at no additional cost to the buyer. Our published affiliate standards apply to this study without exception.

Mitigations, all of them checkable by a reader:

1. Coding rules are mechanical. Every variable has a written decision rule with a worked example, so a coded value follows from the document rather than from a judgment about the vendor.
2. Second coding is blind to the first record and to our own published investigation of the product.
3. The index measures determinability. A vendor cannot raise its score by paying us. It can raise its score only by publishing clearer documents, which is the outcome the study wants.
4. No vendor sees the dataset, the index, or the paper before publication. Vendors may report factual errors afterward through the same corrections process open to any reader.
5. The dataset publishes the source URL, the access date, and the archive link behind every value, so any reader can re-code a product and challenge our result.

### 10.3 Paid submissions

Some products entered our portfolio through our published paid submission options, which buy review speed or a labeled placement and never a score or a ranking. Those records are flagged in the dataset with `paid_submission = yes`, and index results are reported both with and without them. The flag exists because a reader deserves to see the relationship rather than take our word about its irrelevance.

The disclosure wording in the paper is fixed here: "Some products in this frame entered our portfolio through our published paid submission options, which buy review speed or a labeled placement and never a score or a ranking. Those records carry `paid_submission = yes` in the dataset. Every index result in this paper is reported twice, once over the full frame and once with flagged products removed, so that a reader can see the difference rather than accept an assurance about it." The reader-facing summary carries the same statement in the same place relative to the first index figure.

### 10.4 Other conflicts

At protocol date the responsible human holds no investment in, no employment relationship with, and no personal relationship with any covered company. If one arises during the study it is disclosed on the affected record and in the paper, and the responsible human steps back from any judgment affecting that record.

### 10.5 Human subjects and personal data

None. The study collects public corporate documents. No individual is a subject, and no personal data is processed.

### 10.6 Archiving ethics

Public pages are snapshotted for verification. The dataset links to archived copies rather than republishing vendor page content, and this holds without exception. Where public archiving failed, the record carries its `archive_status` flag and the local snapshot stays private, available for audit on request and published nowhere. Verification does not require us to redistribute another company's pages, so we do not.

### 10.7 Dataset license

The dataset, the codebook, and the frame file are published under CC BY 4.0, with a DOI minted through Zenodo at publication. Attribution is the only condition. A license this permissive is the point: a reader who thinks our coding is wrong should be able to take the data and show that it is wrong, without asking us first.

### 10.8 Correction of our own pages

Every discrepancy the window finds between a vendor's current documents and our published investigation of that product is corrected on our page under our published corrections policy, on the policy's own clock, independently of this study's publication schedule.

---

## 11. AI-assistance disclosure

Data collection, the coding passes, and drafting for this study are AI-assisted and run under named human editorial control, consistent with our published AI transparency policy.

What that means in practice:

- A named person, Mucahit Kaya, is accountable for every published value, every index score, and every claim in every artifact.
- No source is cited that a person has not opened.
- Nothing is written up as first-hand product experience, because the method includes no product use.
- Human review covers every adjudicated record, every record carrying a `conflicting` value, and the frozen dataset as a whole.
- AI assistance never substitutes for the decision rules in the codebook. The rules decide the value; the assistance applies them and surfaces the evidence.

### 11.1 How the second coding pass is described publicly

The ceiling is fixed here and binds every artifact from this study, including the paper, the dataset documentation, the reader-facing summary, and any correspondence about the method.

The second pass is described as an **independent second coding pass, AI-assisted under named human editorial control** — the same level of detail our published AI transparency policy uses, and no more. What is public is what a reader needs to judge the work: that the pass is independent, that it is blind to the first record under section 7.3, that the selection rule is deterministic and published, that adjudication is a third pass, and that a named person signs off. Those are checkable claims and they are all published.

What stays unpublished is the internal tooling: how the passes are orchestrated, what runs them, and how the work is divided internally. That detail would not let a reader check a single value, and it is not published anywhere, in any artifact, at any level of abstraction.

---

## 12. Update policy and versioning

### 12.1 Status of this version

Version 1.0 was the pre-registration. Versions 1.1 and 1.2 are referee passes over it, each issued **before the window opens and before any data exists**. All three are published before collection starts. None is edited after the window opens.

The distinction matters for section 12.2. Versions 1.1 and 1.2 both adjust value lists and tighten decision rules, changes that would alter coded values if any existed. None do. The versioning rules below govern changes made once records are in the dataset, and from the moment the window opens they apply in full: a defect found during collection goes to the deviations log under section 12.3 and is fixed in a later version, never edited into a live instrument.

### 12.2 Versioning rules

- **Major bump** (2.0, 3.0) for any change to the index weights, the item set, the variable set, or the frame definition.
- **Minor bump** (1.1, 1.2) for a clarification that cannot change a coded value.
- **The before-the-window clause.** Before the window opens, any change that leaves the index weights, the item set, the variable set, and the frame definition intact is a minor bump, whether or not it would have changed a coded value had one existed. None does exist, so none can change, and a referee pass is free to correct a value list or tighten a decision rule without a major bump. This is the clause versions 1.1 and 1.2 both rest on, and every changelog in the three documents cites it by this name. **Once the window opens the clause above governs**: a change that could alter a coded value is no longer a minor bump, and under section 12.3 it is not made to a live instrument at all.
- Every version carries a dated changelog entry stating what changed and why. Superseded versions stay accessible at their own addresses. Nothing is edited in place.

### 12.3 Deviations

A deviation from this protocol during collection is recorded in a deviations log published with the dataset, with the date, the reason, and the records affected. A deviation is never handled by editing the protocol.

### 12.4 Annual repetition

The study is designed to repeat annually with the same instrument. Wave 2 reuses the wave-1 codebook. Any variable that changes is versioned with an explicit mapping to its wave-1 form so that comparison stays possible, and any variable that cannot be mapped is reported as a break in the series rather than quietly compared.

### 12.5 Weight stability

Index weights are never changed retroactively. If a later wave changes them, the earlier wave is recomputed under both weightings and both figures are published side by side.
