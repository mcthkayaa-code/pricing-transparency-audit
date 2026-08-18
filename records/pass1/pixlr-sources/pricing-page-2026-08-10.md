# Source: Pixlr pricing page
URL: https://pixlr.com/pricing/
Accessed: 2026-08-10
Method: (1) WebFetch (rendered/summarized) + (2) raw `curl` static HTML fetch, cross-checked
Archive: https://web.archive.org/web/20260810104412/https://pixlr.com/pricing/
Network note: fetched from the sandboxed tool-execution environment (not a Turkey-geolocated
client); no currency/locale selector or geo-redirect was observed. Vendor's own currency
statement (ToS: "All Fees are quoted in United States Dollar (USD)") independently settles
the currency question regardless of collection geography — see license/tos evidence file.

## Discrepancy caught and resolved (binding "read a price twice" rule)

WebFetch's rendered summary claimed "Default toggle state: Annual selected by default."
Raw static HTML directly contradicts this and was trusted instead, on three independent
mechanical signals, all agreeing:

1. Container: `<div id="pricing-plans" class="pricing-grid monthley">` — base/default class
   is "monthley" (monthly), not "yearly".
2. Toggle control: `<input type="checkbox" class="toggle-check" id="payment-interval" checked>`
   — the checkbox is `checked` by default in server-rendered HTML.
3. CSS pairing: `#interval-toggle .toggle-check:checked + label .switch-interval-monthly { background:#1a1a1a; color:#fff; }`
   and `...:not(:checked) + label .switch-interval-yearly { ... }` — i.e. `checked` = the
   Monthly tab is the visually-active/highlighted one.

All three agree: MONTHLY is the true default display state. Coded from this, not from the
WebFetch summary. This is a coder-tooling misread (WebFetch), not a vendor-served
`display_variant` — documented per the binding instruction, not logged as a register event.

## Plan cards (server-rendered HTML, monthly default state)

Plus: monthly $2.49 ("per month"); yearly toggle shows struck-through $2.49, "Save 20%"
badge, $1.99 "per month". Features (raw HTML `<ul class="flist">`):
"Ad-Free", "Unlimited saves", "1 concurrent AI generation",
is-monthley: "80 monthly AI Credits", "Credits valid for 1 month"
is-yearly: "960 AI Credits valid for the year" (960/12 = 80/mo, consistent)

Premium: monthly $9.99 / yearly-toggle $7.99 per month. "1,000 monthly AI Credits"
(12,000/yr). "4 concurrent AI generations". "Access to all image, video & audio models".
"Private mode for AI Generations". Extended font/template library.

Ultra: monthly $24.99 / yearly-toggle $19.99 per month. "Up to 10,000 monthly AI Credits".
"Unlimited free \"fast\" image generations*" (asterisk ties to fair-use disclaimer).
"8 concurrent AI generations". Priority AI queue, extended high-res exports, private +
mature content access.

Ultra MAX: monthly $49.99 / yearly-toggle $39.99 per month. Doubles Ultra credits
(10,000/mo instead of 5,000 — i.e. base Ultra MAX tier credits = 5,000, doubled add-on
option takes it to 10,000; card copy: "Double the credits with Max, get 10,000 instead
of 5,000 monthly!").

Price figures independently confirmed in a second representation: plain-text regex match
in raw curl'd HTML found the exact same 8 unique dollar figures
($1.99 $2.49 $7.99 $9.99 $19.99 $24.99 $39.99 $49.99) embedded in unrelated copy
(an education-outreach email template quoting "Pixlr Plus at just $1.99/month (annual)
or $2.49/month"), and the Plus card credits figure (80/mo, 960/yr) appears verbatim in
raw server-rendered `<li>` markup, not just the i18n string bundle.

## Fair-use / discretionary clause (asterisk on "Unlimited*")

Page-wide footnote: "pricingDisclaimer":"* Subject to fair use. Availability of AI
services is not guaranteed and may vary based on demand and system capacity." — same-page
footnote, tied to every "Unlimited*" label on the page (Ultra's unlimited fast images,
and — per Terms of Use, see tos evidence file — "unlimited saves" too, since ToS states
the fair-use carve-out applies to any plan's "unlimited" claims).

## Credit-to-output "Estimated monthly usage" panel (per plan card)

Plus (80 credits/mo): "~80 AI images (fast)", "~16 AI images (pro)", "~80 AI edits (fast)",
"~4 AI videos (fast)"
Premium (1,000 credits/mo): "~1,000 AI images (fast)", "~200 AI images (pro)",
"~1,000 AI edits (fast)", "~50 AI videos (fast)"
Ultra: "Unlimited* AI images (fast)", "~5000 AI images (pro)", "~500 AI images (ultra)",
"~10,000 AI edits (pro)", "~500 AI videos (fast)"

All figures carry a "~" (approximate) qualifier — the page itself labels this section
"Estimated monthly usage", not a fixed rate table. No single "X credits = 1 image" sentence
was found anywhere in official documents.

## Pricing-page FAQ (pricingQuestion/pricingAnswer keys, rendered as an on-page accordion)

Q8/A8: "How do I cancel my subscription?" / "You can cancel at any time in your
Subscriptions page. Once you cancel you'll be able to access premium features until your
subscription period has ended."

Q9/A9: "What is the refund policy?" / "Pixlr is unable to process any refunds for your
subscription once your payment has been processed. If you subscribed via a mobile app
then all subscriptions are managed through your app store - to request a refund you'll
need to contact the store directly."

Q10/A10: "Does my AI-Credits Expire?" / "There are two types of AI-credits, the [o]nes you
have while your subscription is active are topped off each time the subscription renews,
i.e. if you are on a monthly premium subscription and have 863 credits left on the date of
the renewal that will be reset to 1000. If you cancel your subscription the subscription
credits will reset to 0. The second type of credits are the Credit Packs, these credits
will never expire[] and are counted separately from the subscription credits."

## Free trial (Premium only, not the entry tier Plus)

"metaDescriptionFreeTrial":"Try Pixlr Premium free for 7 days. Get access to all premium
features, templates, and content in Pixlr X and Pixlr E. Cancel anytime."
"free7DayTrial":"FREE 7-DAY TRIAL" / "freetrialStartYour7DaysTrialNow":"Start your 7 days
trial now". Every trial-related string names "Premium" specifically; none names "Plus".
No "credit card required" / "no credit card required" statement was found anywhere in the
fetched bundle (searched explicitly). "startTrial" flows into
"pleaseWaitWhileCheckoutLoading":"Please wait while checkout is loading" and
"checkoutCreditDebitCard" strings exist app-wide, but per the codebook's own Vendor-I
example this is UI/flow design, not a statement, and inference from it is barred —
coded `unknown` for trial_card_required, not inferred `yes`.

Trial converts to paid unless canceled: "cancelAnytimeOrAutoRenewalForAmount":"Cancel at
any time or auto-renewal %s for %s"; "yourFreeTrialAccessToPixlrWillEnd":"Your free trial
access to Pixlr will end"; "loosePremiumAccessAndCredit":"You'll lose access to Pixlr
Premium featur[es and credits if you cancel]" (cancel-flow warning strings, implying the
trial continues into a paid subscription by default).

## Free (no-cost) product tier

"metaDescriptionHomepage":"Pixlr is a free online AI photo editor and image generator...".
"indexTitle2024P4":"Pixlr gives you a[n]... image maker, and 20+ editing tools — 100% free,
right in your browser." "commonFreeSave":"daily free save!" / "bounceSnap":"Snap! You have
used all of your daily free saves!" (a daily save-limit exists for non-subscribers; no
numeric cap found anywhere in official documents). "pricingAdFree":"Ad-Free" listed as a
paid (Plus) feature/benefit, implying the free tier carries ads (paid removes them);
no explicit "we show ads" statement found, and no watermark statement tied to free-tier
exports specifically was found (see express/editor fetch notes).

New-user one-time credit bonus (distinct from the 7-day Premium trial and from any
standing free-plan feature): "As a new user, enjoy the freedom of generating 20 images
using 20 credits. Additionally, take advantage of our free trial to experience 250 credits
free of charge." Read as two separate one-time/promotional offers, not a recurring
free-plan allowance — excluded from `free_plan_cap_documented`, noted here for context only.
