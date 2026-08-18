# Source: Pixlr Express (free editor product page)
URL: https://pixlr.com/express/
Accessed: 2026-08-10
Method: WebFetch (rendered/summarized). No raw curl cross-check performed for this page
(budget: capped at two fetch attempts per source; one WebFetch attempt made, sufficient to
establish "free to use" and to establish that watermark/daily-limit/ads are NOT stated,
which is itself the finding for those variables).
Archive: not attempted separately (this URL is secondary; primary pricing-class evidence
comes from https://pixlr.com/pricing/, already archived).

Findings: "Welcome to the free modern AI powered photo editor by Pixlr" confirms
free-to-use. No statement found on: ads, daily save/export limits, watermarks, or account
requirement. One incidental credit-cost mention: an "Extract layers" tool costs "40c"
(credits) — a single feature's credit price, not a free-plan cap and not the principal
output; not coded into any variable, noted for context only.

---

# Source: Pixlr Editor (free editor product page)
URL: https://pixlr.com/editor/
Accessed: 2026-08-10
Method: WebFetch (rendered/summarized).
Findings: "free advanced photo editor", "Start editing" with no paywall mentioned for basic
access. No statement found on ads, watermarks, save/export limits, or account requirement.
Confirms free-to-use claim; does not resolve free_plan_watermark (coded `unknown`).

---

# Source: Pixlr AI Image Generator (product/docs-class page)
URL: https://pixlr.com/ai/ai-image-generator/
Accessed: 2026-08-10
Method: WebFetch (rendered/summarized).
Findings: "250 free AI credits that can produce up to 75 images" during the 7-day trial
(250/75 ~= 3.3 credits/image at whatever quality tier the trial uses — not identified as
"fast" vs "pro" in this source, and presented as a trial-specific figure, not the entry
tier's own rate; not used as the basis for cost_per_output_computable, which is keyed to
the entry paid tier Plus per sampling-rules.md 7.2, not the trial). FAQ: "you can use the
images for commercial purposes" (consistent with the License Agreement's unconditional
grant). No card-required statement found for the trial. No credit-card requirement stated.
No watermark statement found.

Note: no credit card required/required statement located after two total location attempts
(WebSearch for the dedicated trial landing page returned no results; two guessed URLs
https://pixlr.com/freetrial/ and https://pixlr.com/free-trial/ both 404). trial_card_required
coded `unknown` per the codebook's explicit rule against inferring from checkout-flow design.
