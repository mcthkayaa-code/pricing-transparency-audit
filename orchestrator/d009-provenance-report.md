# D-009 provenance check — the five 12x-multiple records

Narrow follow-on to the D-009 sweep result (`deviations-log.md`, D-009, 2026-08-12). The sweep
re-read 25 of 42 in-scope records in a second representation and confirmed all of them; five
remaining records — colossyan, copyleaks, hostinger, humanizemy-ai-detector, humbot — were set
aside as a separate, genuinely open question: each shows `first_charge_amount_usd` exactly 12x
`headline_price_usd` with no computation recorded, so the record alone could not say whether the
vendor published the annual total or the coder multiplied a monthly figure by 12. This is that
check. Not a re-code: only `first_charge_amount_usd`, `computation_assumptions` and `coder_note`
were touched, on these five records only.

**Method.** For each record, the vendor's own pricing page (and, where cited, its Terms/FAQ) was
re-read independently — from this record's own local capture where one exists and is sufficient,
otherwise a fresh live render — and checked against codebook-v1.md's `first_charge_amount_usd`
decision rule (rule 2: a monthly figure may be multiplied by 12 only where a document states the
plan is charged once for twelve months; rule 3: absent that, the value is `unknown`, never
assumed). humanizemy-ai-detector was checked against its own page independently of the sibling
`humanizemy` record, which was not opened.

---

## Table

| record | case | evidence (URL + quoted wording) | value before → after |
|---|---|---|---|
| `colossyan` | **2** — coder computed; vendor documents state once-for-twelve-months | `https://www.colossyan.com/pricing/` FAQ: "annual plans can also be canceled, but since they are paid upfront for the year, your subscription stays active and fully accessible until the end of your current billing period." `https://www.colossyan.com/terms/` §3.3: "this payment is for the upcoming billing period (e.g. you pay in advance for each month or year of the Service depending on what Service Plan you selected)." Page itself prints no annual-total figure, only "$59 /mo" — confirms 708.00 is a coder computation, licensed by these two quotes. | 708.00 → 708.00 (unchanged) |
| `copyleaks` | **1** — vendor published the annual total directly | `https://copyleaks.com/pricing` (live render; local capture is a pre-JS shell with no price text): Personal plan card — "$13.99/month" with "Cancel anytime. $167.88 billed annually." printed directly beneath it. | 167.88 → 167.88 (unchanged) |
| `hostinger` | **1** — vendor published the annual total directly | `https://www.hostinger.com/horizons` (record's own local capture, `hostinger-sources/horizons-pricing-page.html.txt`): Explorer card — "Get 12 months for $83.88 (regular price $119.88). Renews at $6.99/mo." | 83.88 → 83.88 (unchanged) |
| `humanizemy-ai-detector` | **1** — vendor published the annual total directly | `https://humanizemy.ai/pricing` (record's own local capture, `humanizemy-ai-detector-sources/pricing-page-clean.txt`, and independently re-confirmed by a fresh live render): Basic card — "$12 /mo" / "$144 billed yearly" / "Save $72/yr", and beneath the CTA, "Renews automatically at $144 USD every 12 months until cancelled." Checked against this product's own page only; the sibling `humanizemy` record was not opened. | 144.00 → 144.00 (unchanged) |
| `humbot` | **1** — vendor published the annual total directly, in its own structured pricing data | `https://humbot.ai/pricing` (record's own local capture, `humbot-sources/productslist-2026-08-09.json`): the page's embedded `productsList` carries the Basic annual SKU (`price_id price_1OceZgDTBvGUnRQvGweFDLE9`) as `price:9588` (cents) / `duration:12` (months) — a fixed field in the vendor's own billing data. The record's own $7.99/mo headline figure is the *derived* value (95.88÷12), not the reverse. | 95.88 → 95.88 (unchanged) |

---

## What the check found

All five resolved determinately — none is the genuinely-indeterminate case-3 outcome (no document
states billing frequency, value forced to `unknown`). Four are Case 1: copyleaks, hostinger, and
humanizemy-ai-detector all print the annual dollar total in ordinary page text, verbatim, with no
arithmetic involved in the coding at all — "$167.88 billed annually," "Get 12 months for $83.88,"
"$144 billed yearly." colossyan is the one Case 2: the pricing page itself never prints an annual
total (only "$59/mo" and a "Yearly -34%" toggle), so 708.00 really is a coder computation — but a
licensed one, since the pricing FAQ and the Terms of Service both independently state the annual
plan is paid upfront for the year, which is what rule 2 requires before a monthly figure may be
multiplied by 12. That record's own `computation_assumptions` had already recorded this arithmetic
and both quotes correctly before this check started; the check re-verified the quotes live and
found nothing to correct.

The one record worth flagging rather than just confirming is humbot, and it is a difference in
evidentiary *form*, not a weaker result. Its pricing page failed to render any visible price text
to this TR-geolocated session (a client hydration bug already logged in the record as a
`display_variant`), so the $95.88 figure was never read as prose the way the other four were — it
was read from the page's own embedded Stripe-style product catalog, a `price`/`duration` field
pair the vendor's own front end uses to render the price once hydration succeeds. That is still
the vendor publishing the figure, not the coder computing it (the direction of derivation actually
runs the other way: the displayed $7.99/mo is 95.88÷12, not 95.88 = 7.99×12 performed by a coder),
and it matches how this same dataset already treats an embedded JS data payload elsewhere (the
D-009 sweep's krea-ai re-read). But a reader who holds "published" to mean "printed as legible
text on the page" rather than "present in the page's own served data" could reasonably read this
one differently, so it is named here rather than folded silently into the same bucket as the other
three Case-1 records.

Net effect on the dataset: zero values changed. All five `first_charge_amount_usd` figures stand
exactly as coded. What changed is that four records now carry the missing `computation_assumptions`
provenance note the codebook's own rule calls for, and all five carry a dated coder_note entry
documenting this check's evidence and verdict, so a later reader no longer has to re-derive
whether the 12x relationship was a vendor total or a coder's arithmetic.

## Five-record summary

- `colossyan`: case 2 — 708.00 → 708.00
- `copyleaks`: case 1 — 167.88 → 167.88
- `hostinger`: case 1 — 83.88 → 83.88
- `humanizemy-ai-detector`: case 1 — 144.00 → 144.00
- `humbot`: case 1 — 95.88 → 95.88
