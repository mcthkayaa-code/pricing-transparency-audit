# Final-day change sweep — did a coded pricing page move inside the window?

**Run 2026-08-17 by the orchestrator's sweep agent. Window under test: 2026-08-05 → 2026-08-13.
No record was edited. This document reports; the orchestrator decides what enters a record.**

The study codes 76 products as one frozen frame. That frame holds only if no vendor materially
changed a coded page between the first and last collection day. This sweep asks the public archive
for every capture of each product's pricing-class document inside the window, plus the nearest
capture on each side, and compares them on the four things the study codes: **prices, tier names,
caps, policy clauses.**

---

## 1. The honest denominator: 42 of 76, and only 16 of 76 with real reach

**42 of the 76 pricing pages have two or more content captures inside the window.** The other 34
cannot be tested for change at all — one capture is a photograph, not a comparison. That is the
number this report is about, and 76 is not covered.

But 42 overstates the reach, because two captures thirteen minutes apart test nothing about a
nine-day window. The layered figure:

| Test actually available | Products | of 76 |
|---|---|---|
| ≥2 in-window content captures | **42** | 55% |
| …of which ≥2 captures carried a readable price (not a shell) | **40** | 53% |
| …of which the captures span ≥24 hours | **28** | 37% |
| …of which the captures span ≥3 days | **16** | 21% |
| …spanning most of the window (≥7 days) | **4** | 5% |

Twelve of the 42 have all their captures inside a single day — `ismybrandinai` (33 seconds apart),
`decktopus` (13 minutes), `autoshorts-ai` (21 minutes), `apify-robots-checker`, `anomaly-ai`,
`hyperleap`, `nicepage`, `brandcited`, `humanizemy`, `humanizemy-ai-detector`, `sapling`,
`openai-sora`. For these, "no change found" means "no change during a few minutes on one day," which
is close to no information about the window.

**In 40 of the 42, our own coded read falls inside the span the captures bracket.** The two
exceptions are `openai-sora` (coded 08-10, both captures 08-12) and `autoshorts-ai` (coded 08-07,
both captures 08-06) — for those, the archive brackets a period adjacent to our read rather than
including it.

### Why the other 34 could not be tested

| Reason | Products | n |
|---|---|---|
| Exactly one in-window capture | adobe-express, aiclicks, beautiful-ai, colossyan, d-id, gptzero, heygen, ideogram, invideo-ai, jobscan, leonardo-ai, midjourney, mubert, murf-ai, myperfectresume, plus-ai, quillbot, recraft, stable-audio, udio, writehuman, zety | 22 |
| Zero in-window captures (archive holds the page, just not in the window) | copyleaks, gamma, julius-ai, phrasly, playht, teal, winston-ai, xseek, humbot, kling-ai, lovo-ai | 11 |
| **Archive refuses the host entirely (HTTP 403)** | hostinger | 1 |

Every one of those 34 negatives was re-run against **four URL variants** (± trailing slash, ± `www`)
in CDX **and** independently against the **Memento timemap**, because a trailing slash has moved a
timemap on this corpus from 0 captures to 66. The two indexes agreed in every case. The timemap
found the pages exist in the archive at other dates — `playht` has 704 mementos, `lovo-ai` 91,
`copyleaks` 97, `gamma` 87 — so these are true in-window absences, not lookup failures.

`hostinger` is not an absence. All four URL forms and the timemap return **HTTP 403**: the archive
refuses that host. Per the study's own rule, "we are not allowed to read it" is not "it is not
there," and this is already the documented finding that Hostinger's documents cannot be
independently re-examined at any past date by anyone.

**Two products have ≥2 captures that are all pre-hydration shells** carrying no price anywhere — not
in the DOM, not in JSON-LD, not in any script blob: **`canva`** (12 window captures, 4 distinct
bodies, all price-free) and **`adobe-firefly`** (6 captures, 3 distinct bodies, all price-free).
Their captures are readable and their absence of a price is a fact about the capture, not about the
vendor. This corroborates canva's existing `display_variant` register event, which already records
that the 2026-08-05 capture shows zero price digits.

---

## 2. Material changes found

**Four vendor edits established. One of them touches coded subject matter.** Prices and tier names
moved on none of the 76.

### 2.1 `suno` — a new quantified usage cap added to all three tiers · MATERIAL

The only sighting in this sweep that changes something the study measures.

| | |
|---|---|
| Document | `https://suno.com/pricing` (pricing class) |
| Last capture without the change | `https://web.archive.org/web/20260810033731/https://suno.com/pricing` — **2026-08-10 03:37:31 UTC** |
| First capture with the change | `https://web.archive.org/web/20260811053200/https://suno.com/pricing` — **2026-08-11 05:32:00 UTC** |
| Edit bounded to | **2026-08-10 03:37 → 2026-08-11 05:32 UTC** |
| Our coded read | 2026-08-12 (record `collection_date` 2026-08-13) — **after the edit** |

**Before** (2026-08-10, and identically in the four earlier captures 08-05 22:13, 08-07 14:54,
08-09 15:51, 08-10 03:02):

> Free Plan … 50 credits renew daily **No commercial use** …
> Pro Plan … 2,500 credits, refreshes monthly **Commercial use rights for new songs made** … 2 stem
> separation types (Auto; Split from mix). **Advanced Split stem separation** Upload up to 30 min …
> Premier Plan … 10,000 credits, refreshes monthly **Commercial use rights for new songs made** …

**After** (2026-08-11, and identically in the four later captures 08-11 15:42, 08-12 11:06,
08-13 06:26, 08-13 14:41):

> Free Plan … 50 credits renew daily **No monthly song downloads (starting 9/3/26)** No commercial use …
> Pro Plan … 2,500 credits, refreshes monthly **20 song downloads per month (starting 9/3/26)**
> Commercial use rights … 2 stem separation types (Auto; Split from mix). Upload up to 30 min …
> Premier Plan … 10,000 credits, refreshes monthly **60 song downloads per month (starting 9/3/26)**
> Commercial use rights …

Two distinct edits in one revision:

1. **A new quantified monthly cap on every tier** — Free: none; Pro: 20 song downloads/month;
   Premier: 60/month, each carrying a forward effective date of 9/3/26.
2. **"Advanced Split stem separation" removed from the Pro tier's feature list.** Premier still
   carries "3 stem separation types (Auto; Split from mix and Advanced split)". A plan-composition
   change, not a price change.

**Ruled out as a display variant.** All ten in-window captures carry identical locale markers
(`lang="en"`, the same currency-token set) and identical prices ($0 / $8 / $24, and the $72 annual
saving). The clause flips exactly once, in strict chronological order across ten captures, and never
reverts. Nothing here is geography or an A/B arm.

**Coded variables it would touch:** `usage_cap_quantified`, `free_plan_cap_documented`,
`free_plan_cap_value`, `unquantified_limit_clause`, and by extension `cost_per_output_unit` /
`credit_to_output_rate_published`.

**No coded value is stale.** Suno was read 2026-08-12 and 2026-08-13, both after the edit, and the
record already carries the new cap: `usage_cap_quantified` evidence reads "20 song downloads/month
effective 9/3/26 (quantified rate)". Suno is single-coded, so no cross-pass comparability issue
arises either. The register entry is owed under §6.6 item 2; re-collection under §6.6 item 3 is not.

**Incidental.** Both of suno's pricing-page sources carry `archive_status: local_copy_only`, yet the
public archive holds ten in-window captures of that exact URL, including two on the record's own
access dates (`20260812110657`, `20260813144109`). This is the pattern already documented as failure
mode 15 — records understating their own archival coverage. Flagged, not acted on.

### 2.2 `rezi` — 23 of 34 pricing-page FAQ answers removed · MATERIAL to the document

| | |
|---|---|
| Document | `https://www.rezi.ai/pricing` (pricing class) |
| Before | `https://web.archive.org/web/20260807062609/https://www.rezi.ai/pricing` — 2026-08-07 06:26:09 UTC |
| After | `https://web.archive.org/web/20260812065442/https://www.rezi.ai/pricing` — 2026-08-12 06:54:42 UTC |
| Our coded read | pricing page accessed **2026-08-12** (record `collection_date` 2026-08-10) |

The pricing page's FAQ block went from **34 answers to 11**. Nothing was added; 23 answers were
deleted, including three that restate coded facts:

- Removed: *"All Rezi plans include a worry-free 30-day money-back guarantee if you are dissatisfied
  with the software."*
- Removed: *"Rezi Pro costs $29 a month and enables you to create unlimited resumes with no
  restriction on the number of resumes…"*
- Removed: *"…there is no paywall preventing you from building and downloading your resume…"*

Prices (`$0 / $8 / $29 / $99 / $149`) and tier names (Free, Standard, Pro, Team, Enterprise,
Unlimited) are **identical** in both captures.

**Coded variables it would touch:** `refund_window_days`, `refund_policy_location`,
`free_plan_cap_documented`, `free_plan_cap_value`, `usage_cap_quantified`.

**No coded value is stale, on inspection of the raw source of both captures.** The operative
statements the record actually cites all survive the edit:

- The refund answer *"Rezi offers a 100% money-back guarantee on all paid plans (Pro and Lifetime).
  If you are unsatisfied, you can request a full refund within 30 days of your purchase"* is present
  in **both** captures, and so is the embedded JSON-LD `FAQPage` carrying it. `refund_window_days=30`
  and `refund_policy_location=multiple` hold.
- The free-tier and Pro caps are coded from the **compare table** ("1 Resume Limit", "3 Downloads",
  "Unlimited Resumes"), not from the deleted FAQ answers. Both captures carry them.

Worth noting for its own sake: the deleted sentence said *"All Rezi plans"* have the guarantee while
the surviving one says *"all **paid** plans (Pro and Lifetime)"*. The edit removed an internal
contradiction on the vendor's own page.

**One real defect this exposes, and it is ours.** The rezi record's pricing-page source carries
`access_date: 2026-08-12` against `archive_url: …/20260807062609/…` — a snapshot from **five days
before the read**, on the far side of a demonstrated edit, with `archive_status: archived`. §6.4
requires the value to rest on a same-day snapshot. The published archive link therefore shows a
reader a state of the page that is not the state the coder read. A 2026-08-12 capture exists
(`20260812065442`) and matches the access date exactly.

### 2.3 `freepik` (Magnific) — promotional badge dropped, new credit rate added

| | |
|---|---|
| Document | `https://www.magnific.com/pricing` (pricing class) |
| Before | `https://web.archive.org/web/20260807070007/https://www.magnific.com/pricing` — 2026-08-07 07:00:07 UTC |
| After | `https://web.archive.org/web/20260809100637/https://www.magnific.com/pricing` — 2026-08-09 10:06:37 UTC |
| Our coded read | 2026-08-07 (plus a D-007 live re-read 2026-08-10, post-edit) |

Pro plan card, verbatim:

- **Before:** "Includes 4M credits /year **+ 20% OFF**"
- **After:** "Includes 4M credits /year. **Best credit value**"

And a new row was added to the per-model credit-rate table: "**Seedance 2.5 720p New 1,760
credits/4s 136 videos 340 videos 2,272 videos**".

All three plan prices are **identical** across both captures ($20→$14.50 Premium, $45→$33.75
Premium+, $280→$210 Pro, all "Billed annually"), as are the credit allowances (240K / 600K / 4M per
year) and every pre-existing model rate row.

**Coded variables it would touch:** `credit_to_output_rate_published`, `credit_rate_location`,
`annual_condition_disclosure`.

**No coded value is stale.** `headline_price_usd=14.50` is coded from the **Premium** card, which
this edit does not touch. `credit_to_output_rate_published=yes` and `credit_rate_location=pricing_page`
are presence-and-location values that adding a model row cannot flip. The record cites the
`20260807070007` capture — the pre-edit state — which is the correct snapshot for a 2026-08-07 read.

### 2.4 `revid-ai` — pricing page copy rewritten, "Cancel anytime." added

| | |
|---|---|
| Document | `https://www.revid.ai/pricing` (pricing class) |
| Before | `https://web.archive.org/web/20260807215513/https://www.revid.ai/pricing` — 2026-08-07 21:55:13 UTC |
| After | `https://web.archive.org/web/20260813150947/https://www.revid.ai/pricing` — 2026-08-13 15:09:47 UTC |
| Our coded read | 2026-08-13 — after the edit |

Forty-six lines of page copy were rewritten: "Choose your plan / Replace 8+ tools with a simple AI
workflow / Trusted by 14,000+ creators" became "One membership. The whole growth loop. … Every plan
includes the full engine: rendering, publishing, performance stats, Auto-Mode, and agent access.
**Cancel anytime.**"

Prices (`$39 / $99 / $199`) and tier names (Hobby, Growth, Ultra) are **identical** in all three
captures.

**Coded variables it would touch:** `cancellation_self_serve`, `auto_renewal_default`.

**No coded value is stale.** `cancellation_self_serve=self_serve_documented` is evidenced from the
FAQ answer *"Yes, you can cancel your subscription at any time… by going to your account settings"*,
which pre-dates the rewrite, not from the new headline claim. The edit is bounded only loosely
(08-07 21:55 → 08-13 15:09) because the archive holds no capture in between.

---

## 3. Sightings I can show but cannot classify as change over time

Two products differ across in-window captures in ways that are **not** chronological. Both are
geography, demonstrated from the captures' own embedded markers — and both are `display_variant`,
not `vendor_edit`, because nothing establishes that the vendor edited the document.

### 3.1 `google-veo` — CAD and USD served from the same URL, interleaved

`https://one.google.com/about/plans`, five in-window captures:

| Capture | Prices | Currency tokens in the body |
|---|---|---|
| `…/20260807030124/…` 08-07 03:01 | $2.79 / $13.99 / $26.99 | **CAD ×21**, USD ×7 |
| `…/20260807100413/…` 08-07 10:04 | $1.99 / $9.99 / $19.99 | USD ×28 |
| `…/20260808062329/…` 08-08 06:23 | $1.99 / $9.99 / $19.99 | USD ×28 |
| `…/20260810113920/…` 08-10 11:39 | $1.99 / $9.99 / $19.99 | USD ×28 |
| `…/20260812211907/…` 08-12 21:19 | $2.79 / $13.99 / $26.99 | **CAD ×21**, USD ×7 |

Tier names (Basic, Plus, Pro) are identical throughout. The earliest and the latest captures agree
with each other and disagree with the three in between, so the sequence is not a change over time.
It is the same URL serving a Canadian price lineup with a bare "$" sign to some crawls and a US one
to others. This is direct archive evidence for the geography variance the record already logs from
Turkey (TRY), now shown a third way.

### 3.2 `picsart` — US and CA lineups, from the captures' own country fields

`https://picsart.com/pricing/`, two in-window captures:

| Capture | Prices | Embedded `countryCode` / `currency` |
|---|---|---|
| `…/20260810104533/…` 08-10 10:45 | $54, $114, $10.50, $15, $37.50, $47 | **US** / **USD ×20** |
| `…/20260812005542/…` 08-12 00:55 | $82, $159, $52.75, $9.16 | **CA** / **CAD ×20** |

Both carry the identical full 220-entry EUR price list and the same locale-path set, so the pages are
the same document served to two geographies. With only two captures, one from each country, a vendor
edit between them **cannot be excluded** — I can show geography explains the difference, and I cannot
show geography is the *only* thing that changed. Recorded as suspected-not-established.

### 3.3 What an absence of difference here does not prove

The corpus's own limitation applies to every "unchanged" verdict in this report and must be carried
with them: **an archive cannot capture a client-side variant.** The crawler does not execute the
experiment script, so a page under live A/B assignment is archived in one arm only. Two known cases
sit inside my testable set:

- **`beautiful-ai`** — the Pro price element carries `data-pricing-exp-false="$12"` and
  `data-pricing-exp-true="$14.50"` on the same node. It has only **one** in-window capture, so it is
  in the untestable 34 regardless.
- **`copyleaks`** — a cookie-consent-gated A/B test (`pricing-ab.js`); declining analytics cookies
  deterministically serves the control arm. It has **zero** in-window captures.

So for both A/B vendors this sweep is silent, and for every other product a clean diff rules out a
change **in the arm the crawler was assigned** and says nothing about the other arm. No number of
captures can close that gap.

### 3.4 Changes I looked at and am confident are noise

Eight products produced a signal difference that hand inspection resolved as churn the study does not
code. Listed so the negative is auditable rather than asserted:

| Product | What actually differed | Prices / tiers / caps |
|---|---|---|
| `elevenlabs` | JS-bundle number tokens only | all 16 prices, all 10 tier names identical across 6 captures |
| `undetectable-ai` | "Chat with PDF" removed from a feature nav | all 11 prices identical |
| `fotor` | AI-model list rotation ("Seedance 2.5", "FLUX 3", "Mini") | identical; the `3 Video` token was mined from the model name "FLUX 3 Video" |
| `speechify` | "SIMBA Voice Agents" product entry removed | identical |
| `wix` | nav item swapped, Domains ↔ Wixel | prices, tiers and all 8 storage/site caps identical |
| `godaddy` | "Airo AI Builder" added to nav; domain promo prices in a script | **no plan price in any of the 6 captures** — the page's prices are not in served HTML at all |
| `framer` | a live counter, "504,616,418,546 tokens processed this week" | identical |
| `resume-io` | blog-teaser carousel rotated ("Help 11 min" → "Career 7 min") | identical |

---

## 4. Recommendations, in §6.6 / §6.8 register-event form

§6.8 rule 3 routes a sighting to the change register; §6.6 item 2 fixes the form — product id, entry
type, variable class, both dates, both archive URLs. Six entries are owed. **None of them requires
re-collection under §6.6 item 3**, because in every case our coded read already sits on the correct
side of the edit or the coded value does not depend on what moved.

```yaml
# suno.yaml
register_events:
  - type: vendor_edit
    variable_class: pricing
    detail: >-
      Pricing page added a quantified monthly song-download cap to all three tiers
      (Free: none; Pro: 20/month; Premier: 60/month, each "starting 9/3/26") and
      removed "Advanced Split stem separation" from the Pro feature list. Edit
      bounded to 2026-08-10 03:37 - 2026-08-11 05:32 UTC across ten in-window
      captures; prices ($0/$8/$24) and locale markers identical throughout, so not
      a display variant. This record was read 2026-08-12, after the edit, and
      already codes the new cap. No re-collection owed.
    dates: [2026-08-10, 2026-08-11]
    urls:
      - https://web.archive.org/web/20260810033731/https://suno.com/pricing
      - https://web.archive.org/web/20260811053200/https://suno.com/pricing

# rezi.yaml
register_events:
  - type: vendor_edit
    variable_class: pricing
    detail: >-
      Pricing page FAQ reduced from 34 answers to 11 between 2026-08-07 06:26 and
      2026-08-12 06:54 UTC, deleting restatements of the refund guarantee and of the
      Pro/free usage caps. Prices and tier names unchanged. The operative refund
      answer (100% money-back, 30 days) and the compare-table caps this record
      actually cites survive in both captures, in HTML and in the JSON-LD FAQPage,
      so no coded value moves.
    dates: [2026-08-07, 2026-08-12]
    urls:
      - https://web.archive.org/web/20260807062609/https://www.rezi.ai/pricing
      - https://web.archive.org/web/20260812065442/https://www.rezi.ai/pricing

# freepik.yaml
register_events:
  - type: vendor_edit
    variable_class: pricing
    detail: >-
      Pro plan card's "+ 20% OFF" badge replaced by "Best credit value", and a new
      per-model credit rate row added ("Seedance 2.5 720p, 1,760 credits/4s"),
      between 2026-08-07 07:00 and 2026-08-09 10:06 UTC. All plan prices, all credit
      allowances and every pre-existing rate row identical. headline_price_usd is
      coded from the Premium card, which the edit does not touch.
    dates: [2026-08-07, 2026-08-09]
    urls:
      - https://web.archive.org/web/20260807070007/https://www.magnific.com/pricing
      - https://web.archive.org/web/20260809100637/https://www.magnific.com/pricing

# revid-ai.yaml
register_events:
  - type: vendor_edit
    variable_class: pricing
    detail: >-
      Pricing page copy rewritten between 2026-08-07 21:55 and 2026-08-13 15:09 UTC,
      adding the headline claim "Cancel anytime." Prices ($39/$99/$199) and tier
      names (Hobby/Growth/Ultra) identical. cancellation_self_serve is evidenced
      from the pre-existing FAQ answer, not from the new claim.
    dates: [2026-08-07, 2026-08-13]
    urls:
      - https://web.archive.org/web/20260807215513/https://www.revid.ai/pricing
      - https://web.archive.org/web/20260813150947/https://www.revid.ai/pricing

# google-veo.yaml  (adds archive-side evidence to the existing entry)
register_events:
  - type: display_variant
    variable_class: pricing
    detail: >-
      The same URL was archived in two currency states inside the window: captures
      2026-08-07 03:01 and 2026-08-12 21:19 carry CAD prices ($2.79/$13.99/$26.99,
      CAD x21 in body), captures 2026-08-07 10:04, 08-08 and 08-10 carry USD
      ($1.99/$9.99/$19.99). Earliest and latest agree, so not chronological. Tier
      names identical. Independent archive-side confirmation of the geography
      variance this record already logs from a Turkey read.
    dates: [2026-08-07, 2026-08-12]
    urls:
      - https://web.archive.org/web/20260807030124/https://one.google.com/about/plans
      - https://web.archive.org/web/20260807100413/https://one.google.com/about/plans

# picsart.yaml
register_events:
  - type: display_variant
    variable_class: pricing
    detail: >-
      Two in-window captures of the same URL carry different embedded countryCode /
      currency (US/USD 2026-08-10 vs CA/CAD 2026-08-12) and correspondingly different
      price lineups, with the identical 220-entry EUR list in both. Geography explains
      the difference; with one capture per country a concurrent vendor edit cannot be
      excluded, so this is typed display_variant and the possibility is recorded.
    dates: [2026-08-10, 2026-08-12]
    urls:
      - https://web.archive.org/web/20260810104533/https://picsart.com/pricing/
      - https://web.archive.org/web/20260812005542/https://picsart.com/pricing/
```

### One provenance defect, separate from the register

`rezi.yaml`'s pricing-page source pairs `access_date: 2026-08-12` with
`archive_url: …/20260807062609/…` and `archive_status: archived`. §6.4 requires a same-day snapshot,
the two dates straddle a demonstrated edit, and a matching 2026-08-12 capture
(`https://web.archive.org/web/20260812065442/https://www.rezi.ai/pricing`) exists. This is a
citation correction for the orchestrator, not a change-register entry.

---

## 5. What the paper can say, and what it cannot

**Can say:** across the 42 of 76 products whose pricing page has two or more in-window archive
captures, **four vendors edited their pricing page during the collection window**, one of them
(`suno`) adding a quantified usage cap that the study measures. **No product's headline price or tier
name changed inside the window on any testable page.** Two further products were served in two
geographic states inside the window, shown from the archive rather than inferred.

**Cannot say:** that the frame is clean. Thirty-four products could not be tested at all, twelve more
have captures spanning less than a day, and two vendors known to A/B-test their price are among the
untestable — one with a single capture, one with none. For every product in this report the
"unchanged" finding covers the arm the crawler was assigned and the days the crawler visited, and
nothing else.

**The negative means more today than it would have last week.** D-073 re-asked 92 previously refused
citations and all 92 returned `ok`, and this sweep's own 76 CDX queries returned one host-level
refusal and no service failures, so an in-window absence recorded today is evidence about the archive
rather than about our access to it.

---

## Method, and one trap it sprang

- **Registry shapes.** The 76 records store their sources in **fourteen** distinct key combinations,
  not two: the class key alone appears as `kind`, `document_class`, `doc_class`, `class`, `label`,
  `role`, `description`, `authority_class` and `authority_rank`; dates as `accessed` or
  `access_date`; archives as `archive` or `archive_url`. The extractor reads all of them and was
  checked to resolve a pricing-class document, an access date and an archive reference for
  **76 of 76** records with no fall-through.
- **Capture enumeration.** CDX `matchType=exact` over 2026-06-01 → 2026-09-01 per product, giving
  in-window captures plus the nearest on each side. Every negative re-run against four URL variants
  and against the Memento timemap.
- **Reading captures.** The `id_` raw endpoint, decompressed.
- **Comparison.** Prices, tier names near prices, caps, policy sentences, JSON-LD offers, and a
  separate script-blob channel so a page whose figures are server-embedded as JSON is not mistaken
  for a shell. Nav, cookie banners, A/B classes and analytics were not compared.
- **Sampling cap.** Where a page had more than six distinct in-window bodies (`godaddy` 83, `fotor`
  15, `speechify` 11, `suno` 10), six were read — first, last and four spread. A change is found;
  a change-and-revert entirely between two sampled captures would not be. `suno` was then re-read at
  **all ten** captures to confirm its transition is monotone.

**The trap this sweep sprang, recorded because it produced a false finding before it was caught.**
The study's tooling notes say raw archive responses are gzipped. They are also **zstd** and
**brotli**. A capture of `findanomaly.ai/pricing` stored as zstd, read as gzip-or-nothing, decoded to
binary noise — out of which the price regex mined a spurious `$5` while the real four prices
($0/$25/$45/$90) sat unread. It presented as a complete price change **112 seconds** after the
previous capture. Decompressed properly, the two captures are identical. The general defect is the
one this corpus keeps meeting: a reader that handles one encoding when there are several. The fix
applied here is to try every codec and return **`undecodable`** rather than empty when none works, so
the unclassified case is loud instead of silently becoming a finding. Of 120 capture bodies read in
this sweep, 0 finished as undecodable.

**And one earlier version of this sweep nearly recorded 64 fabricated absences.** Run with four
concurrent CDX workers, 64 of 76 products returned connection resets, which naively recorded would
have read as "64 pricing pages have no captures." Re-run sequentially, every one of those 64 returned
captures. The rewrite treats only a clean HTTP 200 with an empty body as evidence of absence.
