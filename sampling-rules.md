# Sampling Rules v1.2

**Companion to** `protocol-v1.md` (Research Protocol v1.2) and `codebook-v1.md` (measurement instrument, v1.2).

> **Change log — v1.2 final referee clauses, 2026-08-03.** The v1.1 entry below now names the ground of its own minor bump, `protocol-v1.md` section 12.2's before-the-window clause, which the v1.2 entry already cited and which the v1.1 changes rested on. No sampling rule changes and the version does not move.

> **Change log — v1.2, 2026-08-03. Second referee pass.** Two rules that could not be executed as written are fixed. Section 7.2's sales-gated rule referred to "every entry-tier variable" without the set ever being named, and coded all of them `unknown` even where the vendor publishes the term. The set is now enumerated in `codebook-v1.md` section 5.2, which also fixes the rule — a term published for the gated tier is coded from the document publishing it — and section 7.2 points there rather than restating it. Section 9.1's placeholder rule forbade the protocol-date figures from appearing in "a published sentence", which this document's own section 2.1 does; its scope now matches `protocol-v1.md` section 1, and occurrences inside the pre-registration are labelled planning estimates. The price basis in section 7.2 also points at the new `protocol-v1.md` section 6.8 for the case where one URL serves two default display states. Frame definition, inclusion and exclusion criteria, strata, and the double-coding target are unchanged, so the bump is minor under `protocol-v1.md` section 12.2's before-the-window clause.

> **Change log — v1.1, 2026-08-03. Referee pass.** Three rules that two coders could have executed differently are closed. The entry paid tier now has a stated price basis, lowest annual-equivalent cost of a single seat read in the pricing page's default display state, with losing candidates recorded so the choice is checkable. The double-coding top-up in section 8.2 breaks category-size ties by category name in plain byte order rather than leaving the order to whoever runs it. The frame counts in published language become `[N]` and `[C]` placeholders set at freeze, so a protocol-date estimate cannot reach a headline. Frame definition, inclusion and exclusion criteria, strata, and the double-coding target are unchanged, which makes this a minor bump under `protocol-v1.md` section 12.2's before-the-window clause.

| Field | Value |
|---|---|
| Version | 1.2 |
| Date | 2026-08-03 |
| Revision date | 2026-08-03 |
| Status | Pre-registration. Frame not yet frozen. Data collection not started. |
| Responsible human | Mucahit Kaya |

---

## 1. Purpose

This document fixes which products enter the study, how the list is closed, how products are grouped for reporting, and what may be said about the results. It is binding from the protocol date. Every rule below is executable by a person holding only these three documents.

---

## 2. Target population and frame

### 2.1 Frame

The frame is **every product with a published AI Tools Police investigation live at the moment the frame is frozen**.

At protocol date the frame stands at 76 products across 15 categories. The number that governs the study is the number recorded at freeze, not this one.

### 2.2 Census, not sample

Every product in the frame is coded. There is no random selection, no sampling fraction, and no sampling error. The study is a complete enumeration of one publication's portfolio.

This has two consequences that bind every artifact from the study:

1. **No inference to a wider population.** The frame is not a random draw from AI products, from AI companies, or from any market. Results describe the frame and stop there.
2. **No inferential statistics in the primary analysis.** Confidence intervals and significance tests presuppose a sampling process that does not exist here. Protocol section 8.1 fixes this.

### 2.3 What the frame is not

The frame reflects our editorial coverage choices over roughly two years. Coverage favored categories where buyer intent runs high and where affiliate programs exist, so those categories are over-represented relative to any plausible population of AI products. This is stated in the limitations register and in the paper, not buried in a methods appendix.

---

## 3. Frame freeze procedure

Executed once, on day 1 of the collection window, before any coding starts.

1. Enumerate every published investigation live on aitoolspolice.com at the freeze moment.
2. For each, record: `product_id` (our review slug), `product_name`, `vendor_home_url`, `category`, `product_status`, `paid_submission`, `review_url`, `review_published_date`.
3. Record the freeze timestamp in ISO 8601 with a UTC offset, once, at the top of the file.
4. Write the result to `frame-frozen-<YYYY-MM-DD>.csv`. This file is the study population for the whole window and is published with the dataset.
5. Count and record: total products, count per category, count per status.
6. The responsible human confirms the frozen list before coding starts. Confirmation is dated in the file.

The frozen file is never edited after confirmation. Frame changes during the window are handled under section 10.

---

## 4. Inclusion criteria

A product enters the frame when all four hold at the freeze moment.

- **I1.** A published AI Tools Police investigation of the product is live on aitoolspolice.com.
- **I2.** The product is an AI-based software product or service offered to individual or small-team buyers. Every product in the current portfolio satisfies this by construction.
- **I3.** The vendor publishes public materials in English.
- **I4.** The product has a public web presence reachable without an account.

---

## 5. Exclusion criteria

A product leaves the frame only under E1 or E2. Both are recorded and reported, never silent.

- **E1. Vendor site unreachable throughout the window.** Every attempt across at least three separate days on at least two days apart returned no accessible official page. The product is reported in an inaccessible table with the dates attempted, and enters no aggregate.
- **E2. Not a product.** The published page covers a company, a concept, or a comparison rather than a purchasable product. No current portfolio entry falls here; the criterion exists so that a future wave has a rule.

### 5.1 What is not an exclusion

These cases stay in the frame. Each is a result, and removing any of them would delete the study's most important findings.

| Case | Handling |
|---|---|
| No public price at all. Pricing gated behind a sales contact. | Stays in. `headline_price_usd = no_public_price`. Item A1 scores 0. |
| Prices published only in a currency other than USD. | Stays in. Coded `non_usd` per protocol section 6.5. Excluded from monetary aggregates only. |
| Terms of service exists but no refund or cancellation policy anywhere. | Stays in. Coded `unknown`. |
| Free product with no paid tier. | Stays in. Paid-tier variables coded `not_applicable`. |
| One-time purchase, no subscription. | Stays in. Renewal variables coded `not_applicable`. |
| Product discontinued. | Stays in the frame, moves to the discontinued stratum under section 6.2. |
| Pricing page changed mid-window. | Stays in. Handled by protocol section 6.6. |
| We hold an affiliate relationship with the vendor. | Stays in. Disclosed under protocol section 10.2. |
| The product entered our portfolio through a paid submission. | Stays in. Flagged `paid_submission = yes`, reported both ways. |
| Our own published investigation contradicts the vendor's current documents. | Stays in. The vendor documents govern the coded value. Our page is corrected separately under the corrections policy. |

---

## 6. Strata

### 6.1 Category

Fifteen categories, taken from the published category structure of the site and recorded in the frozen frame file. At protocol date: AI image generators, AI website builders, AI video generators, AI resume builders, AI humanizers, AI detectors, AI bot checkers, faceless video tools, AI voice generators, AI music generators, AI avatar generators, AI presentation makers, AI design tools, AI data analysis tools, AI headshot generators.

Category sizes at protocol date run from 1 to 9 products. Reporting rules that follow from this:

- Category tables carry counts. Percentages appear only where a category holds 5 or more products, per protocol section 8.2 rule D3.
- No cross-category comparison is presented as a difference between populations.
- No category is merged with another to reach a reporting threshold. Merging would invent a grouping that our own site does not use.
- A product belongs to exactly one category, the one its published investigation carries. Products that plausibly fit two categories are not double-counted.

### 6.2 Status

| Stratum | Definition | Treatment |
|---|---|---|
| `active` | The product is offered for purchase or signup at freeze. | Primary stratum. Enters all aggregates and the index. |
| `discontinued` | The vendor has stopped offering the product, announced a shutdown, or ceased operating. | Coded from archived materials where those exist. Reported in a separate table. Excluded from every aggregate transparency metric and from the index. |

At protocol date exactly one product is known discontinued (PlayHT). Status is re-checked for every product at freeze rather than carried over from the review page, because a product may have shut down since publication. A product discovered to have shut down during the window is moved to `discontinued` and the move is dated.

---

## 7. Unit of analysis and plan selection

### 7.1 Unit

The unit of analysis is the **product**, not the plan and not the vendor. A vendor selling two products in our portfolio yields two records.

### 7.2 The entry paid tier

Several variables reference the entry paid tier. Without a fixed definition two coders would pick different plans and produce incomparable numbers, so the definition is fixed here.

**Eligibility.** A plan is a candidate for the entry paid tier when it satisfies all of:

1. Generally available to any buyer, rather than restricted to students, nonprofits, startups, or a named program.
2. Purchasable without contacting sales.
3. A standing plan rather than a limited-time promotional plan.
4. Where plans scale by seat, the single-seat variant.
5. Where the vendor publishes only usage-based pricing, the smallest published package or the published unit rate.

**Price basis.** Among the eligible candidates, the **entry paid tier** is the one with the **lowest annual-equivalent cost of a single seat, computed in the pricing page's default display state**. "Lowest-priced" on its own decides nothing, because a $12 monthly plan and a $9-per-month annual plan are the same product at two prices, and two coders reading the phrase differently would pick different tiers.

The basis breaks down to four rules a coder applies without judgment:

1. **Read the page as it loads.** The default display state is whatever the pricing page shows before any interaction, the same state `annual_default_toggle` records. Do not switch the billing toggle to find a cheaper figure. Where one URL loads in different states on different reads, `protocol-v1.md` section 6.8 governs: the coder records and archives the state observed, and never reloads hunting for a preferred one.
2. **Annualize whatever that state shows.** A monthly figure is multiplied by 12. An annual figure is taken as it stands. A figure already presented as "per month, billed annually" is multiplied by 12, because that is what the buyer pays across the year.
3. **One seat.** Where a plan is priced per seat, annualize the single-seat cost. Where a plan sells a minimum seat block, annualize the minimum block and record the minimum in `coder_note`, since a buyer cannot buy less.
4. **Compare candidates on that figure alone.** Feature sets do not enter the comparison. This is a price rule, not a value rule.

**Ties.** Where two eligible candidates carry the same annual-equivalent cost, break in this order: the plan the vendor visually marks as its first paid step; then the plan listed leftmost or topmost on the pricing page; then the plan whose published name sorts first in plain byte order.

**Recording the choice.** The chosen plan's name goes in `entry_tier_name`. **Every eligible candidate that lost goes in `coder_note`, with its name and its annual-equivalent figure.** A reader who disagrees with the selection can then see what was rejected and on what number, rather than having to reconstruct the page. Where only one candidate was eligible, `coder_note` says so.

**Where a vendor's only paid option requires contacting sales**, `headline_price_usd` is coded `no_public_price`. The entry-tier variables are enumerated in **`codebook-v1.md` section 5.2**, which governs how each of them is coded in that case and is not restated here: a term the vendor publishes for the sales-gated tier is coded from the document that publishes it, and only a term no official document settles is coded `unknown`. The set is named in the codebook because that is where a coder looks while coding.

### 7.3 Free-only products

Where a product has no paid tier at all and states so, entry-tier variables are coded `not_applicable` and the free-tier variables carry the record.

---

## 8. Double-coding subsample

### 8.1 Target

At least 25% of active products, with every category contributing at least one product.

### 8.2 Selection rule

Deterministic, published before the window opens, and reproducible by anyone holding the frozen frame file.

1. Take the frozen frame. Drop `discontinued` products.
2. Group by category.
3. Within each category, sort ascending by `product_id` using plain byte order.
4. Select the 1st, 5th, 9th, and every fourth product thereafter.
5. If any category ended with no selection, add its 1st product.
6. Count the selection. If it falls below 25% of active products, add the next unselected product from the largest category, then from the next largest, until the floor is met. **Where two categories hold the same number of active products, take the one whose category name sorts first in plain byte order.** Within a category, "next unselected" means next by the `product_id` sort already applied in step 3.
7. Record the selected list as `double-coded-selection.csv` and publish it with the dataset.

Under the category profile at protocol date this selects approximately 25 of 76 products, roughly a third of the frame, above the floor with margin. The surplus improves per-variable agreement estimates in small categories, where a 25% floor would otherwise leave a category with a single double-coded record.

### 8.3 Contingency

If collection capacity requires it, step 4 may be widened to every fifth product before the window opens, which yields about 26% and still clears the floor. The interval actually used is recorded in the dataset and stated in the paper. No other change to this rule is permitted once the window opens.

### 8.4 Blinding

The second coder receives `product_name` and `vendor_home_url` only. Not the first record, not any value from it, and not our published investigation of the product. Protocol section 7.3 governs.

---

## 9. Generalization language

The frame is a census of one publication's portfolio. The language in every artifact has to carry that, in the sentence making the claim, not in a distant methods note.

### 9.1 Required

- The first quantitative statement in any artifact carries the full frame: "Of the [N] AI products we investigated across [C] categories, x did not publish a refund policy."
- Every later percentage prints its denominator: "x of [N]".
- Category statements name the category and its size: "Of the [n] image generators in this audit, x ...".

**`[N]`, `[C]`, and `[n]` are placeholders, not estimates.** `[N]` is the count of products in the frozen frame, `[C]` the count of categories in it, `[n]` the size of the category being discussed. All three are set once, from the frame file produced under section 3, and none of them is written out with a number before that file is confirmed.

The protocol-date figures of 76 and 15 are working estimates for planning. They **never appear in a sentence reporting a result, in a title, in a headline, or in a chart caption**, which is the scope `protocol-v1.md` section 1 fixes for the study title and which these two documents now state identically. Occurrences in this pre-registration and its companions — the frame count in section 2.1, the category profile in section 6.1, the selection estimate in section 8.2, and the matching passages in `protocol-v1.md` — are labelled planning estimates and report no result, which is what lets a planning document state them at all. What the rule forbids is a number reaching a reader as a finding before the frame file it came from exists.

### 9.2 Allowed forms

- "Of the N products we investigated, x ..."
- "Among the N products in this audit, ..."
- "In our portfolio of N AI products, ..."
- "x of the N products we examined published ..."
- "None of the N products we investigated documented ..."

### 9.3 Forbidden forms

- "x% of AI companies ..."
- "x% of AI tools ..." or "x% of AI products ..." without the frame
- "The AI industry ..." as the subject of a finding
- "Most AI products ..." or "AI products typically ..."
- "Our research shows the market ..."
- Any bare percentage with no printed denominator
- Any phrasing implying a random sample, a representative sample, or a market survey
- Any headline that drops the frame while the body keeps it

### 9.4 Headline test

Before publication, each headline, subheading, social card, and chart title is read on its own, out of context. If a reader seeing only that fragment would take it as a claim about AI products in general, it is rewritten. The frame belongs in the fragment, not only in the paragraph beneath it.

The test also checks the numbers in the fragment. Every `[N]`, `[C]`, and `[n]` must have been resolved from the confirmed frame file, not from the protocol-date estimate, and the resolved figures must match across the study title, the paper, the dataset documentation, the reader-facing summary, and every chart caption. A headline carrying a stale count fails this test even where its framing is otherwise correct, because a number nobody can reconcile against the published frame file is worse than no number.

---

## 10. Frame changes during the window

1. A product whose investigation publishes after the freeze does not enter this wave. It is recorded in a deferred list for the next wave.
2. A product whose investigation is unpublished during the window stays in the frame if it was live at freeze. The change is noted in the record.
3. A product that shuts down during the window moves to `discontinued` with the date, and the move is reported.
4. A vendor that renames or rebrands a product during the window keeps its `product_id`. Both names are recorded.
5. A vendor that merges two products into one during the window keeps two records if both were live at freeze, with a note on each.
6. No product is added to the frame after freeze under any circumstances.

---

## 11. Frame file schema

`frame-frozen-<YYYY-MM-DD>.csv`, one row per product, published with the dataset.

| Column | Description |
|---|---|
| `product_id` | Our review slug. The join key across every study file. |
| `product_name` | Product name as the vendor writes it. |
| `vendor_home_url` | Vendor home page. |
| `category` | One of the 15 categories. |
| `product_status` | `active` or `discontinued`. |
| `paid_submission` | `yes` or `no`. Whether the product entered our portfolio through a published paid submission option. |
| `review_url` | Our published investigation. |
| `review_published_date` | ISO 8601. |
| `in_double_coded_set` | `yes` or `no`, written after section 8 runs. |
| `frame_note` | Free text. Any section 10 event affecting this row. |
