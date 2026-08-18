# Synthesia — local audit notes (coder: pass 1 primary, 2026-08-12)

All values coded from the archived snapshots listed in the record's `sources:` block.
This file is a local index of the load-bearing quotes for audit convenience only;
it is not published and is not itself a coded source.

## Price conflict (first_charge_amount_usd = conflicting)
- Pricing page, default Yearly tab (DOM w-tab-pane w--tab-active), raw HTML:
  `<span currency-symbol="">$</span><span yearly-per-month-starter="" price="">18</span><span month="">/mo</span>`
  -> $18/mo x 12 = $216.00/yr
- Same page, FAQPage JSON-LD (script[type="application/ld+json"]), answer to
  "How much does Synthesia cost?":
  "For Starter plan users, Synthesia costs $29 per month or $264 if you go with an
  annual plan.For Creator plan users, Synthesia costs $89/month or $804/year if you
  pay annually."
  -> $264/12 = $22.00/mo (Starter), $804/12 = $67.00/mo (Creator) — both clean
  numbers that do not match the live $18/$64 card figures, consistent with the FAQ
  predating the page's own "NEW LOWER PRICES - Save 38%" banner.

## Credit unit (credit_unit_defined / credit_to_output_rate_published = yes)
help.synthesia.io credits article, both in main body and in the expanded
"How are credits calculated?" FAQ entry:
  "Each second of a video uses 2 credits. Ex: A one-minute video will consume 120 credits."
Credit allowances by plan (same article): Basic 1,200/mo; Starter 1,200/mo or
14,500/yr; Creator 3,600/mo or 44,000/yr.

## Commercial use (commercial_use_lowest_tier = free)
help.synthesia.io "Synthesia Video Licensing" article — table applies by AVATAR
TYPE (stock/synthetic vs custom), not by plan tier:
  Allowed: training videos, FAQ videos, YouTube/Facebook/Instagram/other social
  sharing, product videos on website, "any use that does not include paid promo",
  TikTok videos.
  Not allowed: paid TV ads, paid Facebook/Instagram/YouTube/TikTok/Snapchat ads,
  paid programmatic advertising, "any form of paid promotion", broadcasting TV
  without permission.
Basic (free) plan includes 9 stock AI avatars per the pricing-page compare table,
so this licence reads as tier-independent from the free plan up.

## Refund (refund_policy_exists = no_refunds_stated)
ToS: "Payment obligations are non-cancelable and, except as expressly stated in
the Contract, fees paid are non-refundable."
Help center: "As outlined in Synthesia's Customer Terms of Service, all purchases
are non-cancelable and, except where the Contract expressly states otherwise,
non-refundable." / "purchases are non-cancelable and non-refundable, even if the
subscription wasn't used."
Narrow carve-out (not enough to flip the code, noted for the reader): ToS,
"Effect of Termination" — "Upon any termination for cause by Customer, we will
refund Customer any prepaid fees covering the remainder of the term."

## Renewal (auto_renewal_default = on, renewal_notice_commitment = no_notice_stated)
ToS: "all subscriptions automatically renew ... for additional periods equal to
one (1) year or the preceding term, whichever is shorter."
Help center (plan management article): "Paid plans renew automatically at the
same per-unit price as your current term."
Help center (refund/billing article): "Check your next renewal date under
Billing in your account settings well before it arrives, since a reminder email
isn't guaranteed for every plan."

## Cancellation (cancellation_self_serve = self_serve_documented)
Help center (plan management article): "Self-serve cancellation is available on
the Starter and Creator plans." Steps: profile icon > Account info > Billing >
three-dot menu > Cancel your subscription.

## Unquantified limit clause (unquantified_limit_clause = present)
Acceptable Use Policy, General Requirements / prohibited conduct:
  "Excessively, disproportionately or unreasonably consuming compute or
  AI-generation resources."
Corroborating (pricing page, Enterprise row only, not entry tier): "Unlimited
personal avatars (subject to reasonable consumption and compute)."

## Entry-tier candidates (sampling-rules 7.2)
- Starter: $18/mo default Yearly = $216.00/yr — WINNER (lowest annual-equivalent)
- Creator: $64/mo default Yearly = $768.00/yr — losing candidate
- Enterprise: "Let's talk" / Book demo, no published price — excluded, sales-gated
- "Personal" plan (help center only): maintenance mode, closed to new signups —
  excluded, fails "generally available to any buyer"
