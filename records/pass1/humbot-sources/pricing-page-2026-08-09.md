# Evidence: Humbot pricing page

- URL: https://humbot.ai/pricing (canonical; redirects/serves at https://humbot.ai when loaded directly, confirmed via `document.querySelector('link[rel=canonical]').href`)
- Accessed: 2026-08-09 (UTC ~15:05-15:20)
- Method: rendered read via Claude Browser tool (Chromium), plus inspection of the page's own embedded `window.__NEXT_DATA__.props.pageProps` JSON (same document, same load)
- Network note (D-003 / TR egress): our session's IP geolocated as Turkey. The page's `product.listPaymentPlatform` tRPC call returned `"currency":{"country":"Turkey","code":"TR","symbol":"₺","iso":"TRY"}`. On this session, ALL THREE plan cards (Basic/Unlimited/Pro) rendered their price figure as a bare "-" with the "/mo" suffix still printed (e.g. "- /mo") — not a TRY figure, a blank one. Console showed repeated React hydration errors (#418, #425, #423), consistent with a client-side crash formatting the price for TRY that leaves the placeholder unresolved. This is a vendor-side display bug correlated with our network's locale, not an absence of pricing.

## D-003 currency check (binding)

Attempt 1 (curl, US Accept-Language header): `curl -s -H "Accept-Language: en-US,en;q=0.9" https://humbot.ai/pricing` → HTTP 403 (Cloudflare bot block from this same egress; no content).

Attempt 2 (web.archive.org, most recent capture): `https://web.archive.org/web/2026/https://humbot.ai/pricing` redirected to nearest available capture `20250910052800` (2025-09-10, ~11 months stale — the plan grid in that capture differs from today's, e.g. it shows a "200 words/mo" tier not present today, so its NUMBERS are not used as current values). That archived HTML nonetheless contains the literal string "USD" 15 times and numerous two-decimal price figures, confirming the vendor's normal/default rendering path publishes USD figures rather than requiring a currency assumption. This satisfies the D-003 test: code the USD figure, log the local TRY/blank state as a `display_variant` register event (see record).

## Primary evidence: page's own embedded pricing data

The pricing page ships its full product/price catalog client-side regardless of the display bug, in `window.__NEXT_DATA__.props.pageProps.productsList`. Read via `javascript_tool` against the live, currently-loaded https://humbot.ai/pricing document (not a third-party source — this is the vendor's own document, merely read through its embedded data rather than its (broken-for-us) rendered text, per D-005). Relevant entries (price_cents = USD cents; duration_months: 1 = monthly SKU, 12 = one annual charge for 12 months):

```
Basic   | monthly | $11.99 | 3,000 basic words/mo, 1,000 advanced words/mo, 500-word input limit | price_1OceZhDTBvGUnRQvxSQ15ZRn
Basic   | annual  | $95.88 total ($7.99/mo equiv) | 3,000 basic words/mo, 1,000 advanced words/mo, 500-word input limit | price_1OceZgDTBvGUnRQvGweFDLE9
Pro     | monthly | $22.99 (base, 5,000 advanced words) | 30,000 basic words/mo, 1,200-word input limit | price_1OceZoDTBvGUnRQv5xdauQEv
Pro     | annual  | $119.88 total ($9.99/mo equiv, base 5,000 advanced words) | 30,000 basic words/mo, 1,200-word input limit | price_1OceZoDTBvGUnRQvEfLbQvuw
Unlimited | monthly | $59.99 (base, 10,000 advanced words) | "unlimited" basic words/mo (internally 3,000,000), 50,000-word input limit | price_1OceZxDTBvGUnRQv8x0s5CfE
Unlimited | annual  | $119.88 total ($9.99/mo equiv, base 10,000 advanced words) | same | price_1RgGagDTBvGUnRQvGVsI3HFZ
Free    | monthly/annual | $0.00 | 200 words/mo, 100-word input limit | price_free_monthly / price_free_yearly
One-time | single charge | $9.99 | 2,000 words, 600-word input limit (NOT shown on the visible /pricing grid; catalog SKU only) | price_1R4YuaDTBvGUnRQv0NsFMbyE
```

Pro and Unlimited each also carry additional SKUs for higher "advanced words" add-on tiers selectable via an in-card dropdown (e.g. Pro annual also offers 10k/20k/40k/60k advanced-word variants at $137.88/$155.88/$191.88/$227.88 total/yr respectively; Unlimited annual likewise at 20k/40k/60k/80k for $155.88/$191.88/$227.88/$263.88 total/yr). These are upsell variants of the same named plan, not separate entry-tier candidates. Every `productsList` entry carries `"currency":"USD"` explicitly, with a separate `more_currency` map (including `.try`) used only for localized display — i.e. USD is the base/canonical currency and TRY (and 30 others) are converted figures, not the other way round.

## Default display state observed (screenshot + DOM, unaffected by the price-text bug)

- Toggle: "Monthly" / "Yearly" pair, **"Yearly" pre-selected** (green checkmark) on load, before any interaction. Confirms `annual_default_toggle = annual_preselected`.
- Card order left-to-right: Basic, Unlimited (center, visually highlighted/bordered), Pro.
- Basic card: no dropdown (single SKU), shows "1,000 Advanced words/mo" fixed.
- Unlimited card: dropdown defaulted to "10,000" advanced words/mo.
- Pro card: dropdown defaulted to "5,000" advanced words/mo.
- These defaults match the "base" SKUs listed above (lowest-priced variant of each named plan), confirming which `productsList` row is the one actually displayed by default.
- Toggle tooltips (from `_extraProps.translation`): Yearly = "Get the best value with an annual subscription."; Monthly = "Enjoy the flexibility of month-to-month billing." No explicit "billed annually" string was found elsewhere on the page; the annual condition is disclosed only via the "Yearly"/"Monthly" toggle labels themselves, positioned directly above the plan-card row.
- A separate time-limited promotional popup mechanism exists (`updatePop.getPopByNowDate` / `marketingBackend.getMarketingBackendByNowDate` calls; strings "Back to School Offer", "Up To 87% OFF", "This exclusive offer expires in") but did not visibly trigger during this read (no popup appeared in the screenshot). Treated as a limited-time promotional layer, not part of the standing plan prices coded here (sampling-rules.md 7.2 eligibility criterion 3).

## Full-text render (get_page_text, https://humbot.ai/pricing, 2026-08-09)

Captured separately; key figures corroborated: "3,000 Basic words/mo", "1,000 Advanced words/mo", "Input limit: 500 words" (Basic); "Unlimited Basic words/mo", "10,000 Advanced words/mo", "Input limit: Unlimited words" (Unlimited); "30,000 Basic words/mo", "5,000 Advanced words/mo", "Input limit: 1,200 words" (Pro); "30-Day money back guarantee" (Security & Support section); FAQ: "you can try the Free plan to test out our features before subscribing"; "If you exceed your plan's limits, you will be notified and given the option to upgrade your plan"; "you can upgrade your plan at any time through your account settings. The new pricing will take effect from your next billing cycle."

## Second observation, same session (display_variant)

Later in the same browser session (after the DOM/network inspection above, no page reload triggered deliberately — the client-side hydration appears to have retried and recovered on its own), the SAME URL rendered fully: a **currency selector reading "TRY"** appeared next to the Monthly/Yearly toggle (not present/not usable on the first render), the Yearly toggle now carried an **"83% OFF"** badge, and all three price figures rendered in Turkish lira with a struck-through "monthly-billing" comparison price:

```
Basic:     ₺339 TRY/mo  (struck through: ₺509)
Unlimited: ₺424 TRY/mo  (struck through: ₺2.542)
Pro:       ₺424 TRY/mo  (struck through: ₺975)
```

These figures are an exact match to the `try` (cents) values in the embedded `productsList` divided by 100 (annual/12) and by 100 (monthly), respectively: Basic annual `try:406800` → 406800/12/100 = 339.00; Basic monthly `try:50900` → 509.00. Pro/Unlimited annual `try:508800` → 424.00; Pro monthly `try:97500` → 975.00; Unlimited monthly `try:254200` → 2542.00. This is independent visual corroboration that the USD base figures pulled from `productsList` (Basic $7.99/mo billed annually = $95.88/yr) are exactly what a real visitor is shown, merely converted to the locally-detected currency — the first render's blank "-" was a transient bug, not a different price.

Per protocol §6.8 rule 3, both states are logged here and in the record's `register_events` as a `display_variant` (not a `vendor_edit` — nothing indicates the document itself changed, only that its client-side render succeeded on a retry). The coded USD values are taken from the vendor's own embedded base-currency data (present in both renderings, per D-005/D-003 above), not from either display state's formatted text.

An attempt to interact with the "TRY" currency selector to force a USD render for a third, even more direct confirmation was made (click at its on-screen position) but did not open a functioning dropdown before the page's accessibility tree reverted to a stale/nav-only read; not pursued further since the numeric cross-check above already leaves no ambiguity.

## Archival

- `https://web.archive.org/save/https://humbot.ai/pricing` attempted twice (2026-08-09): both returned HTTP 520 (Internet Archive Save-Page-Now transient failure / crawler blocked). No new snapshot appeared in the CDX index for 2026 after either attempt (`https://web.archive.org/cdx/search/cdx?url=humbot.ai/pricing&output=json&from=20260101&to=20260810` → empty).
- `archive_status: local_copy_only` — this evidence file plus `productslist-2026-08-09.json` and `page-text-2026-08-09.txt` in this directory serve as the local copy.
- Nearest public archive reference (context only, not a source of current values): `https://web.archive.org/web/20250910052800/https://humbot.ai/pricing`.
