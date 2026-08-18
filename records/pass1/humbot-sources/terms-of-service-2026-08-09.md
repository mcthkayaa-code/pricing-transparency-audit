# Evidence: Humbot Terms of Service

- URL: https://humbot.ai/terms-of-service (canonical; browser reports current URL as https://humbot.ai after load, title "Terms of Service | Humbot" — same root-URL behavior as /pricing)
- Accessed: 2026-08-09
- Method: rendered read via Claude Browser tool, `get_page_text` (full page captured in one call, no truncation on the second attempt at max_chars=40000)
- Network note: page rendered fully in English with no currency/price content, so the TR-locale hydration bug seen on /pricing did not manifest here (no client-side price computation on this page).

## Full relevant text captured

Section "Billing, Subscription and Cancellation Policy":
> "Your subscription will automatically renew at the end of each period unless you cancel before the renewal date. Your payment method will be charged on the first day of each billing cycle, and a receipt will be sent to you via email after each payment. We reserve the right to change the prices of our services at any time, but we will notify you in advance to give you the opportunity to modify or cancel your subscription before the changes take effect."

> "You have the flexibility to cancel your Humbot subscription at any time. To do so, you can either follow the cancellation instructions found in your account settings or contact our support team for help. After cancellation, your subscription will remain active until the end of the current billing cycle..."

> "Please note that Humbot does not offer partial refunds or credits for subscription periods that are canceled. If you decide to cancel your subscription before the end of the subscribed period, you will not receive a refund for any remaining time. Similarly, we do not offer credits or prorated billing for subscriptions canceled in the middle of a billing cycle."

Section "Refund Policy" (embedded within the ToS page itself, same URL):
> "You may request a refund if, for any reason, you're unsatisfied with our services. A refund may be issued under certain conditions outlined below:
> - You are only eligible for a refund if you request it within 7 days of your purchase, and your word usage does not exceed 1000 words during this 7-day period.
> - To request a refund, you must contact our customer support team at hello@humbot.ai.
> - Refunds are only available for purchases made directly on our website at humbot.ai. Third-party purchases are subject to the vendor's policies.
> - Only the original purchaser is eligible for a refund. Refunds will not be provided if the subscription was gifted or resold.
> - We reserve the right to deny a refund request if we reasonably believe you are exploiting the refund policy or have violated this Terms."

Section "User's Representations" (list of things the user warrants/agrees to):
> "...you will not use the Website and/or Services for a commercial activity;..."
(Listed plainly among the other user warranties — e.g. age 18+, no impersonation, no fraud. No carve-out, no tier reference, no exception found anywhere else in the document.)

Intellectual Property section covers only Humbot's OWN "Materials" (site, software, trademarks) — "You have no rights in or to the Materials..." This does not address ownership of the humanized-text OUTPUT a user generates; no clause anywhere in the document states who owns generated outputs. Searched full text for "output", "ownership", "you own", "watermark" — none of those terms appear anywhere in the Terms of Service.

Footer confirms company identity: "Humbot is a cutting-edge, all-in-one AI study and writing assistant brought to you by EchoAl Limited, a Singapore-based company."

## Notable finding

The Terms of Service contains an unqualified prohibition on commercial use of the Service itself ("you will not use the Website and/or Services for a commercial activity"), with no tier-based exception found anywhere in the document. Coded `commercial_use_lowest_tier = not_granted` on this basis. This is a notable, surprising finding for a paid writing/study tool.

## Archival

- `https://web.archive.org/save/https://humbot.ai/terms-of-service` — result recorded in the main record's `sources` list.
