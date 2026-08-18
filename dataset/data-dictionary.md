# Data dictionary

**Generated from `codebook-v1.md` by `tools/build_data_dictionary.py`. Do not hand-edit:**
a dictionary maintained by hand beside a frozen codebook drifts from it, and a reader has no
way to tell which is authoritative.

Two files carry the data. `coded-values.csv` is one row per product and one column per
variable. `coded-long.csv` is one row per (product, variable) and additionally carries the
**source URL, the coder's evidence, and the attribution kind for every `unknown`** — it is the
file that makes a value checkable rather than merely readable.

Read `limitations-register.md` before using any figure, and `methods-who-coded.md` before
reading the reliability statistic: **the coders were language models**, so α = 0.811 measures
agreement between two independent model readings and not human inter-coder reliability.

---

## Values that appear across many variables

| Value | Meaning |
|---|---|
| `unknown` | Could not be determined from the vendor's documents. **Every `unknown` in this dataset is attributed to a cause** in `coded-long.csv`: `vendor_silence` (84.2%), `instrument_gap` (12.2%, the codebook could not express what the vendor published), `access_failure` (2.9%), or `unattributable_weak_basis` (0.7%). |
| `not_applicable` | The construct cannot exist for this product, on positive documentary evidence. Vendor silence is `unknown`, not this. |
| `conflicting` | Two official sources of equal authority disagree. Both are recorded. |
| `non_usd` | The vendor publishes a price in one currency and it is not USD, with no USD figure obtainable and no currency selector. |
| `no_public_price` | A paid tier exists and its price is not published; a buyer must contact sales. |

---

## Administrative and computed columns

### `product_id`

Stable slug identifying the product. The join key, and the frame's own identifier.

### `row_provenance`

`adjudicated` where a third reading resolved a disagreement between the two blind coders, `primary` where the pass-1 record publishes unchanged. Pass 2 never publishes: it is the blind second reading behind the reliability figure.

### `product_name`

Vendor's name for the product, copied from the frozen frame. Where a vendor rebranded during the window the frame name is kept and the new name appears in `coder_note` and the source URLs (queue item A-006).

### `category`

The authoring publication's own category for the product. Editorial, not a taxonomy.

### `product_status`

`active` or `discontinued` as at the frame freeze. Three products were discontinued; two of those statuses were stale in the frame and were corrected when found (deviation D-008).

### `paid_submission`

Whether the vendor paid the publication for a listing. Declared because it is a conflict of interest, not because it changes a coded value.

### `entry_tier_name`

The vendor's own name for the tier every tier-scoped variable is measured against, selected under `sampling-rules.md` §7.2 by lowest annual-equivalent single-seat cost in the pricing page's default display state.

### `collection_date`

The date this product was coded. The window ran 2026-08-05 to 2026-08-13.

### `coder_role`

`primary`, `second` or `adjudicated`.

### `coder_pass`

1, 2 or 3.

### `archive_status`

**As recorded by the coder**, and known to be unreliable: it captures what a save request appeared to return rather than whether a capture exists. Verified against the capture index, 14 of 76 rows disagree with it and 12 of those understate their own coverage (deviation D-061). Use `archive_status_verified` instead and keep this column for comparison.

### `primary_source_url`

The pricing page or equivalent the record is anchored to.

### `archive_status_verified`

**Computed at build time, not coded.** `archived` where at least one cited capture resolves, `local_copy_only` where a local capture exists, `NO_REEXAMINABLE_EVIDENCE` where neither does. **No row is the third case.** One was reported as such and the report was RETRACTED: the seven files it named as missing all existed, in a source directory the checking tool did not know to look in (D-063). Verified across all 76 rows: 68 `archived`, 8 `local_copy_only`, 0 with neither.

### `resolving_captures`

Computed: how many of this row's cited archive captures were verified to resolve at the timestamp they cite, out of 516 cited corpus-wide. **482 resolve (93.4%).** Verification ran four times: three during the study, when the service refused 92 citations and they were counted as unverified rather than failed, and a fourth after it recovered, when all 92 answered `ok` (D-073). Eight rows show 0 here; every one of them keeps local capture files, and no row in the dataset has neither.

### `local_source_files`

Computed: how many files exist under this product's `-sources/` directory. For 159 coded values corpus-wide the local capture is the only surviving evidence, which is why the release ships those directories.

---

## Coded variables (37)

Each carries the codebook's own definition and its full table of permitted values. The
decision rule a coder applied, the evidence required, and a worked example are in
`codebook-v1.md` under the same heading.

### `headline_price_usd`

Domain 1 · Type: money or categorical · Index item A1

The largest, most prominent price figure the vendor publishes for the entry paid tier on its pricing page.

| Value | Meaning |
|---|---|
| money | The published figure for the entry paid tier |
| `non_usd` | The vendor publishes no USD price. Currency code and verbatim figure go in `coder_note`. |
| `no_public_price` | The entry paid tier's price is not published; a buyer must contact sales |
| `not_applicable` | The product has no paid tier and the documents say so |
| `unknown` | A paid tier exists but no price figure could be located in any official document |
| `conflicting` | Two official sources of equal authority publish incompatible prices for the same tier. Both URLs recorded. |

### `headline_billing_basis`

Domain 1 · Type: categorical · Index item none, descriptive

What the headline figure represents.

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

### `first_charge_amount_usd`

Domain 1 · Type: money or categorical · Index item A3

The amount official documents state a buyer pays on the first transaction for the entry paid tier, in the billing configuration the pricing page presents by default.

| Value | Meaning |
|---|---|
| money | The stated first-charge amount |
| `non_usd` | The vendor publishes no USD first-charge figure. Currency code and verbatim figure go in `coder_note`. |
| `not_applicable` | No paid tier exists and the documents say so |
| `unknown` | A paid tier exists but no document states what the first transaction charges |
| `conflicting` | Two official sources of equal authority state incompatible first-charge amounts. Both URLs recorded. |

### `mandatory_addon_present`

Domain 1 · Type: categorical · Index item A3

Whether a buyer must pay a further charge, beyond the plan price, to use the entry paid tier as the pricing page advertises it.

| Value | Meaning |
|---|---|
| `no` | Documents state or show no such charge |
| `yes_amount_stated` | A required additional charge exists and its amount is published |
| `yes_amount_unstated` | A required additional charge exists and its amount is not published |
| `unknown` | The documentation could not be located, so whether one exists is unsettled |
| `not_applicable` | No paid tier, which requires `first_charge_amount_usd = not_applicable` on the same record |
| `conflicting` | Two official sources of equal authority state incompatible positions on a required charge. Both URLs recorded. |

### `annual_condition_disclosure`

Domain 2 · Type: categorical · Index item A2

How close the disclosure that a price requires annual prepayment sits to the price itself.

| Value | Meaning |
|---|---|
| `adjacent` | Inside the same visual price block: the same card, the same line, directly beneath the figure, or in the label of the toggle attached to it |
| `same_page_secondary` | Elsewhere on the pricing page: a footnote, small print below the plan grid, or an accordion on the same page |
| `one_click_away` | Only in a document reached by a link: terms, billing FAQ, help article |
| `absent` | The relevant document classes were read and none states the condition |
| `unknown` | The relevant documents could not be located |
| `not_applicable` | No annual billing option exists, or billing does not recur |
| `conflicting` | Two official sources of equal authority state incompatible conditions. Both URLs recorded. |

### `annual_default_toggle`

Domain 2 · Type: categorical · Index item none, descriptive

Which billing period the pricing page preselects when it loads.

| Value | Meaning |
|---|---|
| `annual_preselected` | The page loads showing annual pricing |
| `monthly_preselected` | The page loads showing monthly pricing |
| `no_toggle` | The page offers one billing period only |
| `unknown` | Could not be determined |
| `not_applicable` | Billing does not recur |
| `conflicting` | The vendor maintains two official pricing pages that load in different default states. Both URLs recorded. |

### `free_plan_exists`

Domain 3 · Type: categorical · Index item B1

Whether the vendor documents a plan usable at no cost and with no time limit imposed by a trial.

| Value | Meaning |
|---|---|
| `yes` | A no-cost plan is documented |
| `no` | The pricing page shows paid tiers only, or documents state there is no free plan |
| `unknown` | Documents do not settle it |
| `conflicting` | Two official sources of equal authority disagree about whether a free plan exists. Both URLs recorded. |

### `free_plan_cap_documented`

Domain 3 · Type: categorical · Index item B1

Whether the limits on the free plan carry published numbers.

| Value | Meaning |
|---|---|
| `all_quantified` | Every stated free-plan limit is quantified: it carries a number and the dimension that number counts, plus a period where the limit is a rate. Also where documents state explicitly that the free plan carries no limit in a given respect, on the test in `usage_cap_quantified` rule 3. |
| `some_quantified` | At least one limit is quantified and at least one is not |
| `none_quantified` | Limits are described without numbers |
| `unknown` | The free plan's limits are not described at all |
| `not_applicable` | No free plan |
| `conflicting` | Two official sources of equal authority state incompatible free-plan limits. Both URLs recorded. |

### `free_plan_cap_value`

Domain 3 · Type: free text · Index item none, descriptive

The quantified limits of the free plan, verbatim in structure.

### `free_plan_watermark`

Domain 3 · Type: categorical · Index item B2

Whether free-plan outputs carry vendor branding or a watermark, as documented.

| Value | Meaning |
|---|---|
| `yes` | Documents state free outputs are watermarked or branded |
| `no` | Documents state free outputs are not watermarked |
| `unknown` | Documents do not state it |
| `not_applicable` | No free plan, or the output type cannot carry a watermark |
| `conflicting` | Two official sources of equal authority state incompatible positions. Both URLs recorded. |

### `free_plan_duration`

Domain 3 · Type: categorical · Index item B2

Whether the free plan persists or expires.

| Value | Meaning |
|---|---|
| `perpetual` | Documents state the free plan continues without a time limit |
| `time_limited` | Documents state the free plan ends after a stated period |
| `unknown` | Documents do not state it |
| `not_applicable` | No free plan |
| `conflicting` | Two official sources of equal authority state incompatible durations. Both URLs recorded. |

### `trial_exists`

Domain 4 · Type: categorical · Index item B3

Whether the vendor documents a time-limited free trial of a paid tier.

**Permitted values.** `yes`, `no`, `unknown`, `conflicting`.

### `trial_card_required`

Domain 4 · Type: categorical · Index item B3

Whether documents state that starting the trial requires payment details.

| Value | Meaning |
|---|---|
| `yes` | Documents state a card is required |
| `no` | Documents state no card is required |
| `unknown` | Documents do not state it |
| `not_applicable` | No trial |
| `conflicting` | Two official sources of equal authority state incompatible positions. Both URLs recorded. |

### `trial_length_days`

Domain 4 · Type: integer or categorical · Index item B3

The trial's stated length in days.

**Permitted values.** An integer, or `unknown`, or `not_applicable`, or `conflicting`.

### `trial_auto_converts`

Domain 4 · Type: categorical · Index item none, descriptive

Whether documents state the trial becomes a paid subscription without a further action by the buyer.

**Permitted values.** `yes`, `no`, `unknown`, `not_applicable`, `conflicting`.

### `credit_system_present`

Domain 5 · Type: categorical · Index item none, gating

Whether the product meters use through an internal unit, whatever the vendor calls it: credits, tokens, points, coins, generations.

**Permitted values.** `yes`, `no`, `unknown`, `conflicting`.

### `credit_unit_defined`

Domain 5 · Type: categorical · Index item C1

Whether any official document says what one credit is.

| Value | Meaning |
|---|---|
| `yes` | A document defines the unit, for example "one credit equals one second of generated audio" |
| `no` | The relevant documents were read and none defines it |
| `unknown` | The documentation could not be located |
| `not_applicable` | No credit system |
| `conflicting` | Two official sources of equal authority define the unit incompatibly. Both URLs recorded. |

### `credit_to_output_rate_published`

Domain 5 · Type: categorical · Index item C2

Whether the conversion from credits to outputs is published for the product's outputs.

| Value | Meaning |
|---|---|
| `yes` | Rates are published for the principal output and for the other output types the plan advertises |
| `partial` | Rates are published for some output types but not the principal one, or only as a range |
| `no` | The relevant documents were read and no rate is published |
| `unknown` | The documentation could not be located |
| `not_applicable` | No credit system |
| `conflicting` | Two official sources of equal authority publish incompatible rates. Both URLs recorded. |

### `credit_rate_location`

Domain 5 · Type: categorical · Index item none, descriptive

Where a published rate lives.

**Permitted values.** `pricing_page`, `docs_help_center`, `terms`, `multiple`, `absent`, `not_applicable`, `unknown`, `conflicting`.

### `cost_per_output_unit`

Domain 6 · Type: categorical · Index item none, supporting

The unit in which this product's principal output is counted.

**Permitted values.** `per_video_minute`, `per_image`, `per_1k_words`, `per_audio_minute`, `per_page`, `per_headshot`, `per_document`, `per_presentation`, `per_seat_month`, `per_api_call`, `other`, `unknown`, `conflicting`.

### `cost_per_output_computable`

Domain 6 · Type: categorical · Index item C3

Whether a reader can calculate a cost per unit of principal output using only published figures and arithmetic.

| Value | Meaning |
|---|---|
| `yes` | Every figure needed is published, and the calculation needs no assumption about typical use |
| `partial` | The calculation is possible only for a secondary output, or only across a published range that yields a range rather than a figure |
| `no` | At least one required figure is not published |
| `unknown` | The documents needed could not be located |
| `conflicting` | Two official sources of equal authority publish incompatible figures among the calculation's inputs. Both URLs recorded. |

### `computation_assumptions`

Domain 6 · Type: free text · Index item none, supporting

The arithmetic behind any derived monetary value, written so a reader can repeat it.

### `credit_rollover_policy`

Domain 7 · Type: categorical · Index item C4

What the documents say happens to unused credits at the end of a billing period.

| Value | Meaning |
|---|---|
| `rolls_over` | Unused credits carry forward without a stated limit |
| `partial_rollover` | Credits carry forward subject to a stated cap or expiry |
| `expires_at_period_end` | Unused credits are lost at the end of the period |
| `unknown` | Documents do not state it |
| `not_applicable` | No credit system |
| `conflicting` | Two sources of equal authority state incompatible policies |

### `failed_generation_charge_policy`

Domain 8 · Type: categorical · Index item C5

What the documents say happens when a generation fails, errors, or produces nothing usable.

| Value | Meaning |
|---|---|
| `not_charged` | Documents state failed generations consume nothing, or are refunded automatically |
| `charged` | Documents state the attempt consumes the allowance regardless of outcome |
| `case_by_case` | Documents state a failed generation may be credited back on request |
| `unknown` | Documents do not state it |
| `not_applicable` | The product has no metered generation step |
| `conflicting` | Two sources of equal authority state incompatible policies |

### `auto_renewal_default`

Domain 9 · Type: categorical · Index item D1

Whether a subscription renews without a further action by the buyer.

| Value | Meaning |
|---|---|
| `on` | Documents state subscriptions renew automatically |
| `off` | Documents state subscriptions do not renew automatically |
| `no_recurring_billing` | The product is sold as a one-time purchase |
| `unknown` | Documents do not state it |
| `conflicting` | Two sources of equal authority state incompatible policies |

### `auto_renewal_disclosure_location`

Domain 9 · Type: categorical · Index item D2

Which document class discloses automatic renewal.

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

### `renewal_notice_commitment`

Domain 9 · Type: categorical · Index item none, descriptive

Whether the vendor commits to notifying the buyer before a renewal charge.

**Permitted values.** `advance_notice_stated`, `no_notice_stated`, `unknown`, `not_applicable`, `conflicting`.

### `refund_policy_exists`

Domain 10 · Type: categorical · Index item D3

Whether official documents state a refund position.

| Value | Meaning |
|---|---|
| `yes` | A refund is available under stated terms |
| `no_refunds_stated` | Documents state that no refunds are given |
| `unknown` | Documents do not state a position |
| `conflicting` | Two sources of equal authority state incompatible positions |
| `not_applicable` | The product has no paid tier and the documents say so, so there is nothing a refund could attach to |

### `refund_window_days`

Domain 10 · Type: integer or categorical · Index item none, descriptive

The number of days after purchase during which a refund may be requested.

**Permitted values.** An integer, or `0` where no refunds are given, or `unknown`, or `not_applicable`, or `conflicting`.

### `refund_conditions`

Domain 10 · Type: categorical · Index item none, descriptive

Whether qualifying conditions attach to a refund.

| Value | Meaning |
|---|---|
| `unconditional` | Within the window, no condition beyond the request |
| `conditional` | Conditions apply: usage thresholds, a stated reason, an approval step |
| `unknown` | Documents do not state it |
| `not_applicable` | No refund available |
| `conflicting` | Two official sources of equal authority state incompatible conditions. Both URLs recorded. |

### `cancellation_self_serve`

Domain 10 · Type: categorical · Index item D4

How the documents say a buyer cancels.

| Value | Meaning |
|---|---|
| `self_serve_documented` | Documents describe canceling from account settings without contacting anyone |
| `contact_required` | Documents state cancellation requires an email, a ticket, or a call |
| `unknown` | Documents do not describe a route |
| `conflicting` | Two sources of equal authority describe incompatible routes |
| `not_applicable` | Billing does not recur |

### `refund_policy_location`

Domain 10 · Type: categorical · Index item none, descriptive

Which document class carries the refund position.

**Permitted values.** `pricing_page`, `dedicated_refund_page`, `terms`, `help_center`, `multiple`, `absent`, `unknown`, `not_applicable`, `conflicting`.

### `commercial_use_lowest_tier`

Domain 11 · Type: categorical · Index item E1

The lowest tier at which documents grant the right to use outputs commercially.

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

### `watermark_removal_tier`

Domain 11 · Type: categorical · Index item E2

The lowest tier at which documents state outputs carry no vendor watermark or branding.

**Permitted values.** `no_watermark`, `free`, `lowest_paid`, `mid_tier`, `highest_tier`, `never_removed`, `unknown`, `not_applicable`, `conflicting`.

### `output_ownership_statement`

Domain 11 · Type: categorical · Index item E3

What the documents say about who holds rights in generated outputs.

| Value | Meaning |
|---|---|
| `user_owns` | Documents state the customer owns or holds full rights in outputs |
| `vendor_license_retained` | Documents state the vendor retains ownership and grants a license |
| `conditional` | Rights depend on tier, on use type, or on a subscription staying active |
| `unknown` | Documents do not address ownership |
| `conflicting` | Two sources of equal authority state incompatible positions |
| `not_applicable` | The product produces no output ownership could attach to, matching the `not_applicable` case on `commercial_use_lowest_tier` |

### `usage_cap_quantified`

Domain 12 · Type: categorical · Index item F1

Whether the limits attached to the entry paid tier carry published numbers.

| Value | Meaning |
|---|---|
| `all_caps_quantified` | Every stated limit is quantified: it carries a number and the dimension that number counts, plus a period where the limit is a rate. Also where documents state explicitly that the tier carries no usage limit. |
| `some_quantified` | At least one limit is quantified and at least one is not |
| `none_quantified` | Limits are stated without numbers |
| `unknown` | The tier's limits are not described |
| `not_applicable` | No paid tier |
| `conflicting` | Two official sources of equal authority state incompatible limits for the same tier. Both URLs recorded. |

### `unquantified_limit_clause`

Domain 12 · Type: categorical · Index item F2

Whether official documents condition use on a standard that carries no number.

| Value | Meaning |
|---|---|
| `present` | A clause limits use by an unquantified standard: fair use, reasonable use, excessive use, abuse thresholds, throttling at the vendor's discretion |
| `absent` | The terms and the plan documentation were read and contain no such clause |
| `unknown` | The terms could not be located |
| `conflicting` | Two official sources of equal authority disagree about whether use is subject to such a clause. Both URLs recorded. |

---

## Variables this generator could not fully read

Listed rather than silently emitted short. A dictionary that quietly covers less than
the dataset is the failure mode this study has found in its own tools four times.

- free_plan_cap_value (partial: no value table)
- computation_assumptions (partial: no value table)

