# Source: https://sapling.ai/pricing
# Accessed: 2026-08-12
# Method: rendered browser read (mcp Claude_Browser preview_start + navigate), viewport 1280x900 desktop,
#         accessibility tree (read_page) + get_page_text + screenshot cross-check. No cookie-consent banner observed.

## Screenshot-confirmed plan grid (default load state, no interaction)

FREE
$0 / mo
Buttons: Add to Chrome, Google Docs, Add to Outlook, Add to Word (browser-extension installs; no detector CTA)

PRO
$25 / month        <- large heading, most prominent figure, this is the DEFAULT state
Subscribe          <- primary CTA; opens payment dialog stating "You are subscribing to Sapling Pro ($25/month)."
Annual ($12 / mon)  <- secondary link/button, NOT a toggle switch (no checked/aria-selected state; separate href="javascript:void(0);" CTA)
Try it free
"For individuals."

ENTERPRISE
Contact Us
Get started (-> /teams?plan_page=True) / Contact Us (-> /contact?enterpriseplan=True)
"For teams."
"Starts at 10 seats, $15/seat/month"

API
Metered
Subscribe (-> /create-api-checkout-session) / Pricing (-> /docs/api/pricing) / Docs
"For developers."

## Banner text (top of page, before any interaction)
"Haven't yet registered? Just sign up (no credit card required) to start a free 1-month trial of Sapling Pro."

## Comparison table (accessibility-tree extraction)
Row "Snippets": Free=20, Pro=Unlimited, Enterprise=Unlimited
Row "Unlimited use on premium domains" (Pro/Enterprise feature)
Row "AI detector (longer queries)" -- listed under Pro/Enterprise feature column, NOT under Free
Row "API": "Separate usage-based plan." with its own Subscribe / Talk with us CTAs

## FAQ (accordion, pricing page)
Q: "Do you offer a free trial?"
A (partial, accordion truncated in extraction): "Yes, for individuals. Once you [register] and confirm your email, you'll automatically be enrolled in a free t[rial]..."
Q: "What if I have more questions?" -> points to /billing_faq

## Payment dialog text (opened by "Subscribe" CTA on Pro card, closed without entering any payment info per documents-only rule)
"You are subscribing to Sapling Pro ($25/month)."

## Currency
No currency selector or country picker present anywhere on the page. All figures shown with "$" only.
