# Post-window supplementary retrieval

**Run date: 2026-08-17. All readings in this file are post-window.**

The collection window closed **2026-08-13** and the frame is frozen. Nothing in this file has been
merged into any record, and **no coded value has been altered**. Every record referenced below is
untouched. This is a supplementary check that stands *beside* the frozen dataset: it asks, of the 21
values the unknown-attribution pass marked `access_failure`, whether the document the coder could not
reach was in fact reachable, and if so what it says.

That question is answerable after the window because it is a question about *our instrument*, not
about the vendors' state on the coding date. Where a retrieved document carries its own
last-updated stamp that predates the window, that is noted, because it tells us the text we read
today is the text that was there then. Where it does not, the finding is weaker and is labelled as
such.

**Scope: 21 values across 8 records** (`orchestrator/unknown-attribution.csv`, `kind == access_failure`).

**Method.** Three independent routes minimum before declaring anything unreachable: the live URL, a
Wayback capture from any date, and at least one alternative route (sitemap, differently-cased or
trailing-slash URL, locale variant, embedded data layer, the vendor's own help-centre API, or a
different host serving the same document). Protocol limits observed throughout: **no account
created, no login, no terms accepted, no trial started, no CAPTCHA solved and no bot wall evaded.**
Where Cloudflare or a bot wall blocked a route it is recorded as a block, not worked around. Ordinary
rendered browser page loads were used, which this study already permits under deviation D-005
(letting a public page's own scripts render is reading a document).

**Two infrastructure notes that shaped the run.**

1. Archive.org's **CDX index was down all day** (HTTP 503 on `web.archive.org/cdx/search/cdx`, 502 on
   `archive.org/wayback/available`). The **Memento timemap** endpoint
   (`web.archive.org/web/timemap/link/<URL>`) stayed up and was used instead to enumerate captures.
   Anyone re-running this should know the timemap is a working substitute when CDX is not.
2. Archive.org's **replay path was intermittently "Temporarily Offline"** (an 11,832-byte error page).
   Retry loops of up to 40 attempts at 20-second intervals were needed. This matters for reading the
   original records: an attempt that "failed" against archive.org may have hit an outage rather than
   an absent capture.

A third note, and the single most useful mechanical lesson of the run: **archive.org's `id_` (raw)
modifier returns the capture gzip-compressed.** Fetched with plain `curl` and inspected as text it
looks like binary noise, and a naive text extraction of it yields nothing. Two of this study's
"empty archived app shell" conclusions look consistent with that artefact. Decompress before judging
a capture empty.

---

## Record: `pass1/canva` — 2 values

Both values rest on one document, which the record names in full and which the record's own
`coder_note` says was not re-attempted this pass ("the prior pass's 2-3 archival attempts for it
(beyond this study's 2-retry cap) already failed").

**Document the coder could not reach:** Canva Help Centre, "Watermarks or Canva logos are on my
design" — `https://www.canva.com/help/watermarks-design/`

**Routes tried today**

| Route | Outcome |
|---|---|
| `curl` with a desktop UA + `Accept-Language: en-US` | **HTTP 403** (755,050-byte Cloudflare challenge body) — reproduces the record's finding |
| `WebFetch` | **HTTP 403 Forbidden** |
| Ordinary rendered browser load (D-005) | **HTTP 200, full article, 12,952 chars of body text** |

No challenge was solved and no consent banner was accepted; the article body was already in the DOM
independent of consent state (the same condition this study's own picsart record relied on).

### `free_plan_watermark`

**Result: RETRIEVED, and it addresses the construct.**

The article's opening line, above its own table of contents, states the free-tier watermark position
directly:

> "Premium elements will have watermarks on your design if you're a Canva Free user. Learn more
> below."

Corroborated inside the same article, in the Canva Print section:

> "As part of the Canva Print order process, we ask you to download and review a PDF proof. For Canva
> Free users, if you used premium elements in your design, this proof will be watermarked."

Rendered on the same page as a "People also viewed" excerpt of a **separate** article ("I want to
remove the 'designed with Canva' watermark on my published website") — recorded here as a second,
distinct document rather than as this article's text:

> "If you're on a Canva Free plan, a "Designed with Canva" footer will appear on all your published
> websites, regardless of whether you're using a free Canva domain or your own custom domain."

Source: `https://www.canva.com/help/watermarks-design/`, read 2026-08-17.

**Note for the adjudicator, not a recoding:** the vendor's position is *conditional* — free-tier
output is watermarked **where premium elements are used**, not unconditionally. The record's `unknown`
was reached on the basis of documented silence plus an unreachable article. The silence was real in
the four documents actually searched; the article is not silent.

### `watermark_removal_tier`

**Result: RETRIEVED, and it addresses the construct.**

The article's "How to remove watermarks on your design" section names both removal routes:

> "Upgrade from Canva Free to Canva Pro or Canva Teams."

> "Upgrade to Canva Pro or Canva Teams for unlimited access to our extended library of premium images,
> videos, templates, and more for free."

and a per-element purchase alternative that is not a tier at all:

> "Download your design to purchase all the premium elements you used."
> "Select the Remove watermarks button on an element to purchase it."

Confirmed negatively by the troubleshooting section, which presupposes Pro/Teams are watermark-free:

> "If you're on Canva Pro or Canva Teams but still see watermarks on your design, you might be in the
> wrong account or team."

Source: `https://www.canva.com/help/watermarks-design/`, read 2026-08-17. Pro is this record's coded
entry tier.

**Blunt version: this article was sitting one ordinary browser load away for both passes, and it is
the one document in Canva's estate written specifically about the construct.** The record correctly
declined to call it vendor silence. It was ours.

---

## Record: `pass1/hailuo-ai` — 1 value

### `annual_default_toggle`

**Document the coder could not reach:** the rendered plan-card / billing-toggle UI at
`https://hailuoai.video/subscribe` — specifically its *default, pre-interaction* state.

**Routes tried today**

| Route | Outcome |
|---|---|
| Live rendered browser load, direct to `/subscribe` | **Client-side redirected to the homepage** before any plan card or toggle mounted — reproduces the record's finding exactly |
| Live SSR HTML (`curl`, desktop UA, `Accept-Language: en-US`) | HTTP 200, 624,889 bytes — but **no rendered plan cards and no toggle element**. Stripping `<script>` *and* `<style>`, the entire visible server-rendered text is 149 chars: "Hailuo AI Subscription Plans for Video and Image Tools / Home Design Hot Assets Tools Video H3 Image Audio / **From /mo** / Sign In Explore Mine Subscribe Menu" |
| Alternative URL surfaces: `/pricing`, `/price`, `/plans`, `/membership`, `/subscribe/`, `/en/subscribe` | All HTTP 200 but all serve the same client-rendered shell (602–625 KB); none exposes a server-rendered plan grid |
| Wayback: 59 captures of `/subscribe` enumerated via timemap (2024-11-03 → 2026-08-07, including two in-window: 20260806052203, 20260807114246) | **Not readable during this run** — archive.org's replay path was "Temporarily Offline"; two capture fetches (in-window 20260807114246 and an early 20250119181431) were left retrying for 40 attempts each and did not return content. Independently, archive.org's crawler does not execute the client-side widget, which is the same failure mode this study already documented for canva and picsart, so a capture would be unlikely to carry the rendered toggle even once replay recovers |

**Result: STILL UNREACHABLE.** The default state of the billing toggle cannot be observed from any
public document. The plan UI is gated behind an authenticated session, and the protocol forbids
creating one. This is a permanent access failure and the record's `unknown` is correctly attributed.

**But the run did convert part of the record's open question into documented fact,** and this is
worth carrying into the paper because the record explicitly flagged it for adjudication. The
`/subscribe` i18n payload contains, as vendor-authored strings:

> `"subscribe_toggle_yearly":"-46% OFF"`
> `"subscribe_toggle_yearly_march_sale":"-60% OFF"`
> `"subscribe_year_unit":"Yearly"`
> `"subscription_annual_discount":"%s off billed annually"`
> `"bk_hard_moss_charge_combo_desc_3":"Yearly Standard Subscription"`

and the affiliate FAQ in the same payload states a concrete annual figure:

> "$34.99 is the Pro Monthly Plan price, $1139.88 is the Unlimited Yearly Plan price"

So a yearly billing option, a yearly discount, and a yearly Standard SKU demonstrably exist. The
record's UNRESOLVED RENDERED FINDING (a "From $9.99/mo" homepage widget it could not explain) is also
partly resolved: the SSR markup ships that widget as literal "**From /mo**" with the figure injected
client-side, confirming it is a client-fetched teaser rather than a server-published price.

**These strings remain what the record called them — i18n templates, not values.** Every price label
is a format string (`"$$%.2f billed yearly"`, `"%s off billed annually"`), so none of them supplies a
figure, and none of them says which side of the toggle loads first. The variable stays unanswerable.
The record's judgment not to code from this payload was right.

---

## Record: `pass1/lovo-ai` — 1 value

### `failed_generation_charge_policy`

**Document the coder could not reach:** the help.lovo.ai **Payment-and-Billing section**
(`https://help.lovo.ai/hc/en-us/sections/21880949692825-Payment-and-Billing`), and within it the
article the record saw only as a related-link title, "What happens if I hit my credit limit?"
(exact URL unresolved at coding time).

**Routes tried today**

| Route | Outcome |
|---|---|
| Live static fetch | Cloudflare managed challenge, **HTTP 403** — reproduces the record's finding. Not solved |
| Ordinary rendered browser load | **HTTP 200.** Section listing and article both render normally |
| The help centre's own public article API, called from its own origin (`/api/v2/help_center/en-us/articles.json`, paginated) | **HTTP 200 — all 53 articles enumerated** |

Note that help.lovo.ai is still served even though the lovo.ai apex returned HTTP 402
`DEPLOYMENT_DISABLED` during the window; the two hosts failed independently.

**Section contents, now fully enumerated** (the record could not see this list at all): "What happens
if I hit my credit limit?", "Can I cancel my subscription?", "Can I get a refund after subscribing?",
"Can I upgrade my plan? How do I change my plan?", "What are the available payment options? Which
credit cards are accepted? Do you accept PayPal?"

**Result: RETRIEVED, and it does NOT address the construct.**

The article the record identified as the likely home of this value is, in full (byline "Jason",
"2 years ago Updated"):

> "**What happens if I hit my credit limit?**
> Once you hit your monthly limit, you need to upgrade your subscription. If you require more than
> 20 hours per month, please contact us at hello@lovo.ai"

Source: `https://help.lovo.ai/hc/en-us/articles/22141281216025-What-happens-if-I-hit-my-credit-limit`,
read 2026-08-17.

It is about exhausting the **monthly allowance ceiling**. It says nothing about what happens to
allowance when a generation fails or errors.

To make that negative load-bearing rather than a one-article miss, every article in the help centre
was enumerated (53 total) and title+body regex-matched for
`/fail|error|unsuccessful|refund.{0,20}credit|credit.{0,20}refund|deduct/i`. **One of 53 matched, and
it is unrelated:** "My email verification has failed / I have not received the email verification
link."

**This one runs the other way.** The record reasoned that "the section that would answer it was never
read". The section has now been read, along with the other 52 articles, and the construct is absent
from the entire help centre. The original `unknown` was vendor silence, not our failure, and the
attribution should be revisited from `access_failure` to vendor silence. The record's coded value
does not change; only the reason it carries.

---

## Record: `pass1/openai-sora` — 10 values

Ten of the 21 sit on one named document. The record's account of it is that it "returns HTTP 404 live
with only an empty, contentless archive.org shell recoverable" and was "unrecoverable within this
session's 2-attempt effort cap".

**Document the coder could not reach:** "Sora Billing & Credits FAQ",
`https://help.openai.com/en/articles/10245774-sora-billing-credits-faq`

**Routes tried today**

| Route | Outcome |
|---|---|
| Live URL, `curl` | **HTTP 403** |
| Live URL, rendered browser | Renders OpenAI's help-centre **not-found** page. The parent collection `https://help.openai.com/en/collections/11106745-sora` likewise returns "UH OH. THAT PAGE DOESN'T EXIST." Both are genuinely deleted, consistent with the product shutdown |
| Archive.org **CDX index** | HTTP 503 all day (see infrastructure note) |
| Archive.org **timemap** | **Worked. 31 unique captures enumerated, 2024-12-09 → 2026-06-13** |
| Capture **20260613054113** (the one the record checked) | Retrieved. **The record's description is accurate**: 10,139 bytes, no `<title>`, 41 chars of visible text — "Enable JavaScript and cookies to continue". A bot-wall interstitial that archive.org captured instead of the article |
| Capture **20251124172907** | **Retrieved — full article text**, 51,164 bytes decompressed, title "Sora - Billing FAQ \| OpenAI Help Center" |
| Capture **20260201090715** (closest pre-shutdown) | **Retrieved — full article text**, 54,221 bytes decompressed, stamped "Updated: 4 days ago" |
| Sora **collection** captures via timemap (36 enumerated) | Latest pre-shutdown capture 20260331195237 retrieved, enumerating all 13 Sora help articles |

**The document was recoverable the whole time.** The record checked the single most recent capture,
found a bot-wall shell, and generalised from it. Thirty earlier captures were never enumerated. Two
of them carry the complete article. The `id_` gzip artefact described in the infrastructure note is
the likely reason a fetch that did reach content still looked empty.

### The article, and its own scope limit

Both recovered captures open with the same caveat, which constrains everything below:

> "Please note that the following experience only applies to **Sora 1 on Web**. It does not apply to
> the Sora app or Sora 2 on web."

The two captures differ only in the tier table, so the document was live and maintained:

- 2025-11-24 ("Updated: 2 months ago") — Plus/Business: "Unlimited images and video / Up to 5s videos
  at 720p or 10s at 480p / Up to 2 concurrent generations"
- 2026-02-01 ("Updated: 4 days ago") — Plus/Business: "Unlimited images and video / **Up to 480p
  resolution and 10s duration videos / Up to 1 concurrent generation**"

Quotations below are from the **2026-02-01** capture, the closest to the frozen window, at
`https://web.archive.org/web/20260201090715id_/https://help.openai.com/en/articles/10245774-sora-billing-credits-faq`.

### Was there any other Sora billing document? No.

The collection capture of 2026-03-31 (last before the 2026-04-26 shutdown) lists the complete Sora
help estate — 13 articles: Blocking and reporting on the Sora app; Creating images on Sora; Creating
videos with Sora; Data Controls and Privacy on the Sora app; Generating content with characters;
Generating videos on Sora; Getting started with the Sora app; Sending Messages in the Sora App;
**Sora - Billing FAQ**; Sora - Data Controls FAQ; Sora - Release Notes; Sora - Supported Countries;
Sora App and Sora 2 - Supported Countries.

**"Sora - Billing FAQ" is the only billing document that ever existed in the collection.** There was
never a Sora 2 billing or credits FAQ. (A supplementary fetch of "Sora - Release Notes" was queued
against 18 enumerated captures and had not returned content when this file was written; it is not
relied on for anything below.)

Worth recording precisely because the record leans on the document's name: the article's canonical
title and slug are **"Sora - Billing FAQ"** / `10245774-sora-billing-faq`. The record refers to it
throughout as the "Sora **Billing & Credits** FAQ" and reasons from that name that it is "the document
that would define what one credit equals in output terms". The document has never had "credits" in
its title, and contains the string "credit" **zero** times.

### Keyword scan of the recovered article (2026-02-01 capture, 4,706 chars of visible text)

`$` = **0** · `credit`/`Credit` = **0** · `trial`/`Trial` = **0** · `annual` = **0** ·
`yearly` = **0** · `refund` = **0** · `monthly` = 2 · `concurrent` = 2 · `resolution` = 2 ·
`Unlimited`/`unlimited` = 4 · `watermark` = 1

The same scan on the 2025-11-24 capture returns the same zeroes.

### Value-by-value

**`usage_cap_quantified` — RETRIEVED, and it addresses the construct.**
The record coded this unknown because "the entry paid tier itself could not be identified". The
article publishes per-tier caps explicitly:

> "**ChatGPT Plus / ChatGPT Business** — Unlimited images and video · Up to 480p resolution and 10s
> duration videos · Up to 1 concurrent generation
> **ChatGPT Pro** — Unlimited images and video · Faster generations · Up to 1080p resolution and 20s
> duration videos · Up to 5 concurrent generations · Download videos without a watermark"

together with an unquantified carve-out in the same document:

> "Limits may be enforced to prevent abuse and ensure a stable and equitable experience for all users."

> "**Understanding Unlimited Usage.** ChatGPT Pro and Plus plans offer unlimited access to Sora.
> However, usage must adhere to our Terms of Use, which prohibits, among other things: Abusive usage,
> such as automatically or programmatically extracting data. Sharing your account credentials or
> making your account available to anyone else. Reselling access or using ChatGPT to power
> third-party services. We have guardrails in place to help prevent misuse and are always working to
> improve our systems. This may occasionally involve a temporary restriction on your usage."

Quantified limits (resolution, duration, concurrency) alongside an unquantified abuse/guardrail
clause. The construct is addressed on both sides.

**`mandatory_addon_present` — RETRIEVED, and it addresses the construct.**
The record coded unknown because "the billing/credits documentation that would address a required
add-on charge returns HTTP 404 live". The article states the access structure:

> "How do I upgrade my plan? **Only ChatGPT Plus users can upgrade their plan.**"

> "Currently ChatGPT Free, Enterprise, and Edu accounts are **not eligible for Sora access**."

> "Is Sora part of ChatGPT Business? We're still working to release a business version of Sora, but in
> the meantime we are offering Sora access to our ChatGPT Business users if they wish to try the
> consumer version of Sora under our consumer Terms of Use."

Sora carried no separate price and no separate add-on: access was a feature of a ChatGPT
subscription, and the upgrade path ran through ChatGPT's own settings ("select **My plan**… select
**Manage plan**… Click on the **Get Pro** button"). No required extra charge is documented anywhere in
the article.

**`annual_default_toggle` — RETRIEVED, and it addresses the construct (weakest of the three; an
adjudicator could reasonably move this to "silent").**
The article never uses "annual" or "yearly", depicts no billing toggle, and states a single cadence:

> "What is my billing date? Your billing date is the day of the month on which you first initiated
> your plan, which is also the day that you will receive your monthly subscription charge.
> **Subscriptions for ChatGPT plans are charged on a calendar monthly basis**, from the subscription
> start date."

I count this as addressing the construct because it documents monthly-only billing with no annual
alternative to toggle to, and shows an upgrade flow with a single "Get Pro" control rather than a
priced plan grid. It is flagged as the weakest of the ten so the count can be adjusted rather than
argued about.

**`first_charge_amount_usd` — RETRIEVED, and it does NOT address the construct.**
The article contains **no price figure of any kind** — zero `$` characters. The record's reasoning
("no pricing page or billing document stating a first-charge amount could be located or recovered")
is now half-wrong: the document was recoverable, and it states no first-charge amount.

**`trial_exists` — RETRIEVED, and it does NOT address the construct.**
Zero occurrences of "trial". The record's reasoning is explicit that "the live pricing page and
product documentation classes, which rank above the terms for this variable, could not be reached for
Sora". The product-documentation class has now been reached, in the one billing document that ever
existed, and it is silent on trials.

**`trial_length_days` — RETRIEVED, and it does NOT address the construct.** Cascades from
`trial_exists`; the retrieved document states no trial length.

**`trial_auto_converts` — RETRIEVED, and it does NOT address the construct.** As above; no conversion
behaviour is stated.

**`credit_unit_defined` — RETRIEVED, and it does NOT address the construct.**
The record names this document as the one "that would define what one credit equals in output terms".
It contains the string "credit" **zero** times. What it describes instead is unmetered access —
"ChatGPT Pro and Plus plans offer unlimited access to Sora" — i.e. for Sora 1 on Web there was no
credit currency to define. Because the article self-scopes to Sora 1, it cannot settle the unit for
the Sora 2 era on which the record's `credit_system_present = yes` rests (that value comes from the
discontinuation FAQ's "purchased ChatGPT/Sora credits can still be used for Codex"). Combined with
the collection enumeration showing no other billing document ever existed, the honest reading is that
**OpenAI never published a Sora credit definition** — not that we failed to reach one.

**`credit_to_output_rate_published` — RETRIEVED, and it does NOT address the construct.** Same
document, same zero "credit" count, no rate of any kind.

**`cost_per_output_computable` — RETRIEVED, and it does NOT address the construct.** The record states
that price, allowance and rate "are all unknown because the document that would state them could not
be recovered". The document has been recovered and states none of the three.

### What this record's coverage claim should become

The record's ten `unknown`s do not change. What changes is the reason. Three of the ten are answered
by a document the study said it could not read. Seven are answered "the vendor never said" by the
same document — which is a materially stronger and more publishable finding than "we could not get
in". And the specific claim that the Sora Billing FAQ "could not be recovered in any state" is false:
it has 31 captures, two of which were read today in full.

---

## Record: `pass1/picsart` — 1 value

### `cost_per_output_computable`

**Document the coder could not reach:** a USD-denominated reading of `https://picsart.com/pricing/`.
The record coded this unknown because `headline_price_usd` is unknown, and says in terms: "the
currency block, not a missing figure, is what prevents computation."

**Routes tried today**

| Route | Outcome |
|---|---|
| Live pricing page, `curl`, desktop UA, `Accept-Language: en-US` | **HTTP 200, 1,215,376 bytes with real price content.** This contradicts the record's "static fetch/curl returns empty JS-shell" — at least today, it does not |
| `?country=US`, `?currency=USD&country=US` | HTTP 200 but identical TRY payload; params ignored |
| `picsart.com/us/pricing/` · `picsart.com/en/pricing/` | 2,962-byte stub · 0 bytes |
| hreflang alternates | 17 locales enumerated, all **language** paths (`/zh/`, `/fr/`, `/de/`…); no country or currency variant exists |
| support.picsart.com help centre, **all 117 articles** via its own public API | No currency policy, no dollar plan price (detail below) |

**The decisive route was the live page's own data layer.** The pricing page embeds a
machine-readable, **country-keyed, multi-currency price table** — a `"prices":[…]` array per
`product_id` — carrying every locale's figure inside the same document. The record read the rendered
TRY text and then went to archive.org hunting a US-crawled view; the vendor was publishing all
currencies in the page itself.

**Consistency check against the frozen coding.** `pro_web_yearly` value = **TRY 999**; 999 ÷ 12 =
**TRY 83.25/mo**, exactly the figure the record coded on 2026-08-10. The Pro price is unchanged since
the window, so what follows is not an artefact of reading a different price.

**Result: RETRIEVED, and it does NOT address the construct.**

The vendor's own price table has **no US row and no USD figure for the Pro entry tier**, while
carrying one for the Ultra tier in the same array:

| product_id | entries | currencies | US / USD row |
|---|---|---|---|
| `pro_web_yearly` (entry tier) | 33 | AUD, BRL, CAD, CNY, EUR, GBP, INR, JPY, MXN, MYR, PLN, TRY | **ABSENT** |
| `pro_web_monthly` (entry tier) | 33 | same 12 | **ABSENT** |
| `power_web_monthly_1500` (Ultra) | 34 | same 12 **+ USD** | `{country_code: US, currency: USD, value: 47}` |
| `power_web_yearly_1500` | 34 | + USD | `{US, USD, 450}` |
| `power_web_monthly_2500` / `power_web_yearly_2500` | 34 | + USD | `{US, USD, 75}` / `{US, USD, 720}` |
| `power_web_monthly_5000` / `power_web_yearly_5000` | 34 | + USD | `{US, USD, 145}` / `{US, USD, 1390}` |
| `power_web_monthly_10000` / `power_web_yearly_10000` | 34 | + USD | `{US, USD, 250}` / `{US, USD, 2400}` |

Pro's 33 country rows are TR, SE, SI, SK, RO, PT, NL, MT, LU, LT, LV, IE, HU, GR, FI, CZ, EE, BE, AT,
DE, FR, IT, ES, CN, JP, GB, AU, CA, BR, IN, MX, PL, MY. There is no `US` row and no null/default row.
Pro's published figures include TRY 999/yr, EUR 84/yr, GBP 84/yr, TRY 149/mo, EUR 12/mo, GBP 14/mo.

**Arm 1 (vendor's own currency disclosure) re-run far past the record's six articles.** Every article
in support.picsart.com was enumerated via the help centre's public API from its own origin — **117
articles** — and matched for `/currency|USD|US dollar|exchange rate|local currency|\$\d/i`. Four
matched; none is a currency-policy statement and **none quotes a plan price**. The only "currency"
sentence in the entire help centre concerns app-store billing:

> "For any questions or issues related to currency transactions or payment methods associated with
> store purchases, please reach out to the support services for Apple, Google, or Microsoft, depending
> on your purchase platform." — "How to change your payment method"

**Interpretation.** This is a retrieval success whose content runs against the `access_failure`
attribution. The complete price table was one request away. It shows the vendor does not publish a
US/USD price for the Pro entry tier at all, while publishing one for Ultra in the same array. So
`headline_price_usd = unknown` and `cost_per_output_computable = unknown` both stand — but the reason
is a **documented gap in the vendor's own price table for that tier**, not a currency block on our
side and not a failure to reach a US view. The record's sentence "the currency block, not a missing
figure, is what prevents computation" should be retired: on this evidence it is a missing figure.

The record's non-qualifying App Store sanity check ("Picsart Pro Annual $83.99") is also worth
re-reading in this light: the web Pro tier appears not to be sold to US web buyers at all, which is a
more interesting explanation of the web-vs-app-store divergence the record logged than a plan-naming
mismatch.

---

## Record: `pass1/runway` — 1 value

### `failed_generation_charge_policy`

**Document the coder could not reach:**
`https://help.runwayml.com/hc/en-us/articles/32880432736659-Why-am-I-receiving-errors-when-trying-to-generate`
The record says a help-centre article "appears to address this directly but could not be fetched or
archived within budget (403 / 520)".

**Routes tried today**

| Route | Outcome |
|---|---|
| `curl`, desktop UA | **HTTP 403** — reproduces the record's finding |
| `WebFetch` | **HTTP 403 Forbidden** |
| Ordinary rendered browser load (D-005) | **HTTP 200, full article.** Title "Why am I receiving errors when trying to generate? – Runway"; breadcrumb Runway › Troubleshooting › Platform Troubleshooting › Generation Troubleshooting |

**Result: RETRIEVED, and it addresses the construct — directly, and with a dedicated section.**

> "**Generation errors** usually occur when the model is unable to produce a high-quality output with
> the provided inputs. This error indicates that the generation process was terminated, and **credits
> (if used) will be returned to your account within a few minutes.**"

and under its own heading:

> "**Credits for failed generations.** Credits are automatically returned to your account shortly
> after a generation error. If you don't see your credit balance increase, the generation likely
> failed before credits were charged. See How to troubleshoot a credit discrepancy for more
> information."

Source: URL above, read 2026-08-17.

The record's instinct was exactly right — the article does address this directly, and it says credits
are returned. Its judgment not to code from an unread article was also right. The gap was purely
retrieval, and a rendered load closes it.

**Collateral, offered because the record explicitly invites it.** The same domain, unreachable to
static fetchers, renders normally. That bears on two other blocked leads in this record which were
*not* in my 21 and which I did not code or re-read: `help.runwayml.com/.../Free-plan-details` (the
record's `free_plan_watermark = unknown` rests on it being unread) and
`help.runwayml.com/.../Requesting-a-refund-for-your-plan-or-payment` (the record's `conflict_note`
says "A future coder with access to the help-center domain should re-verify this article directly
and, if confirmed, take it to adjudication"). **help.runwayml.com is accessible by rendered read.**
That invitation can now be taken up.

---

## Record: `pass1/wix` — 2 values

**Document the coder could not reach:** `https://www.wix.com/about/terms-of-use`, Sections 2-19. The
record's account is careful and specific: only Section 1 and an Israel-residents addendum render,
confirmed by DOM heading enumeration across a raw fetch and a full browser render.

**Routes tried today**

| Route | Outcome |
|---|---|
| `https://www.wix.com/about/terms-of-use` (English, `x-default`), `curl` | **HTTP 200, 752,178 bytes — and only 2 substantive `<h2>` headings: "1. Introduction" and "Addendum - Subscription and Payment Terms for Residents of the State of Israel".** Zero occurrences of "Output", "Licensed Content", "Intellectual Property". **The record's finding reproduces exactly** |
| `?lang=en` · `/en/about/terms-of-use` · trailing slash | 6 `<h2>` stubs · 0 · 0 |
| **hreflang alternates** (the page's own `<link rel="alternate">` set, 20 locales) | **The document is served complete in other locales** |
| `tr.wix.com/about/terms-of-use`, rendered browser | **HTTP 200, 20 `<h2>`, 110 headings, 107,743 chars — Sections 1-19 present** |
| `de.wix.com/about/terms-of-use`, `curl` | **HTTP 200, 20 `<h2>` — independent second locale confirming the same clauses** |

**Heading counts by locale — English is uniquely broken:**

| locale | `<h2>` | | locale | `<h2>` |
|---|---|---|---|---|
| **www (en)** | **6** | | de | 20 |
| **ja** | **2** | | fr | 20 |
| tr | 20 | | nl | 20 |
| es | 17 | | pl | 20 |

German confirms the full spine: 1. Einleitung / 2. Ihre Pflichten / 3. Inhalte und Eigentumsrechte /
4. Datenschutz / 5. KI-Dienste / 6. Gebühren / 7. Kündigung / 8. E-Commerce / 9. Video-Dienste /
10. Dienste von Drittanbietern / 11. Logo Maker / 12. Wix Studio / 13. Fehlverhalten und
Urheberrechte / 14. Gewährleistungsausschluss / 15. Haftungsbeschränkung / 16. Schadloshaltung /
17. Allgemein / 18. Geltendes Recht / 19. Verzicht auf Sammelklagen.

**This is a locale-specific content defect on the vendor's side, not a bot wall and not a coder
error.** The record diagnosed the English failure correctly and verified it properly. It then
concluded the sections were "absent from the document as served" — true of the English rendering,
false of the document. The body was retrievable in at least six other languages the whole time.

### `output_ownership_statement`

**Result: RETRIEVED, and it addresses the construct.**

Section **5.4** exists and is titled, in so many words, Output Ownership. Turkish
(`tr.wix.com/about/terms-of-use`, rendered read, 2026-08-17), "5.4. Çıktı Sahipliği":

> "Herhangi bir şekilde kullanmayı, yayınlamayı, iletmeyi veya sergilemeyi tercih ettiğiniz bir Çıktı
> sizin Kullanıcı İçeriğiniz (yukarıda tanımlandığı gibi) olarak kabul edilir ve bu Şartlar tüm
> çıktılara, geçerli yasaların izin verdiği ölçüde, Kullanıcı İçeriği kapsamında uygulanır. Siz (veya
> Son Kullanıcılarınız) ile Wix arasında olduğu gibi, Çıktının Wix'e ait önceden var olan herhangi bir
> fikrî mülkiyeti içermediği bir çerçevede, Wix bir Çıktı üzerinde herhangi bir mülkiyet hakkı talep
> etmez."

German (`de.wix.com/about/terms-of-use`, 2026-08-17), "5.4. Eigentum an den Ausgaben" — independent
second locale, same clause:

> "Wenn Sie sich für eine beliebige Verwendung, Veröffentlichung, Übertragung oder Anzeige einer
> Ausgabe entscheiden, gilt diese als Ihr Benutzerinhalt (wie oben definiert) und die
> Nutzungsbedingungen sind soweit gesetzlich zulässig anwendbar, als ob es sich um einen
> Benutzerinhalt handeln würde. Im Verhältnis zwischen Ihnen (oder Ihren Endbenutzern) und Wix erhebt
> Wix keinerlei Ansprüche auf Eigentumsrechte an der Ausgabe, insoweit diese keinerlei bereits zuvor
> bestehendes geistiges Eigentum von Wix beinhaltet."

In substance: an Output the user chooses to use, publish, transmit or display is treated as that
user's User Content, and as between the user and Wix, **Wix claims no ownership right in an Output**,
to the extent the Output contains no pre-existing Wix intellectual property.

Corroborated by Section 3.1 ("Fikri Mülkiyetiniz" / Your Intellectual Property):

> "Wix ile sizin aranızda, Kullanıcı İçeriğiniz ve sizin tarafınızdan oluşturulan, geliştirilen veya
> Wix Hizmetlerine bağlanan diğer tüm materyallerle ilgili tüm fikri mülkiyet hakları size ait
> olacaktır… Wix, Kullanıcı İçeriğiniz veya Wix Hizmetlerine bağladığınız içerik üzerinde mülkiyet
> hakkı talep etmez."

with the plain-language box: "İçeriğinize ait tüm haklar tarafınıza aittir." Section 5.5 separately
grants Wix a non-exclusive, sublicensable, worldwide licence over Inputs and Outputs for service
improvement, tool training and third-party processing — a licence, not an ownership claim, the same
distinction this study's runway record already draws.

**Note for the adjudicator, not a recoding:** the record discarded an unverifiable third-party
paraphrase of a "Section 2.1" ownership clause. That was the right call — ownership of Output lives in
**5.4**, and of User Content in **3.1**. Section 2 is "Your Obligations". The discarded paraphrase was
pointing at the wrong section, which vindicates the fabrication-warning discipline that discarded it.

### `commercial_use_lowest_tier`

**Result: RETRIEVED, and it does NOT address the construct.**

A full-text scan of the complete (Turkish) body: "ticari" ×7, "yeniden sat" ×1, "Lisanslı İçerik" ×4,
and **zero** matches for "makul kullanım" / "aşırı kullanım" / "adil kullanım" (reasonable / excessive
/ fair use). Every commercial-use clause found runs the other way — it restricts commercial
exploitation of **Wix's** assets, not the user's outputs, and none carries a tier gate. Section 2.3,
among prohibited conduct:

> "Wix Koşullarında açıkça izin verilen durumlar dışında, Lisanslı İçeriği ve/veya Wix Hizmetlerini
> herhangi bir şekilde kullanmak veya erişimini satmak, lisanslamak veya herhangi bir ticari amaçla
> istismar etmek"

Section 3.2 grants a limited licence to build the User Platform, display it to End Users and offer
User Products, conditioned on compliance and on "uygulanabilir tüm Ücretleri zamanında ödemeniz"
(timely payment of all applicable Fees) — a payment condition, not a plan-tier condition. Section 8
(E-Ticaret) imposes seller obligations for selling User Products, again with no tier gate.

So the first-ranked document has been read and it contains **no tier-differentiated commercial-use
grant or restriction on the user's own outputs**. The record's `unknown` stands, and the attribution
should move from `access_failure` toward vendor silence on the tier question specifically — with the
caveat below.

**Caveat that keeps this honest.** The clauses quoted are the vendor's Turkish and German renderings,
not its English text, and the English text is the one that did not render. For a contractual variable
this is a real evidentiary difference: a translation is the vendor's own publication but is not the
governing English wording. I would put this to adjudication as "document retrieved in six non-English
locales; English rendering defective; construct absent from the retrieved text" rather than as a
clean vendor-silence finding.

---

## Record: `pass2/jobscan` — 3 values

**Document the coder could not reach:** `https://www.jobscan.co/terms-of-service`, in English. The
record documents four independent failed attempts (WebFetch, two browser navigations, a Wayback
capture, an archive.ph attempt), all rendering Turkish body text.

**Root cause, found today.** The ToS body is not on jobscan.co at all. The wrapper page renders an
empty `<main>` — 514 chars of site chrome, `lang="en-US"` — and injects the policy through a
third-party iframe:

`https://app.termly.io/policy-viewer/iframe-content.html?policyUUID=186bf27c-eb55-4548-a82c-ea2013d118a0&viewMethod=embedded`

Rendering that iframe from this (Turkey-egressing) network **reproduces the original failure exactly**:
55,043 chars, all Turkish — "HİZMET ŞARTLARI", "Son güncelleme tarihi 16 Mart 2026". The Turkish was
never the vendor's document. It is **Termly's client-side viewer localising to the request locale**,
which is why four different routes to jobscan.co all returned Turkish: they were all rendering the
same third-party widget.

**Routes tried today**

| Route | Outcome |
|---|---|
| `curl`, desktop UA | **HTTP 403** |
| `WebFetch` | HTTP 200 but **nav and footer only** — no substantive legal text ("does not contain the actual Terms of Service document text") |
| Rendered browser load of jobscan.co/terms-of-service | 514 chars, empty `<main>`, one iframe |
| Rendered browser load of the Termly iframe | 55,043 chars, **Turkish** — original failure reproduced |
| `iframe-content.html` via `curl` | 1,246-byte client-side shell |
| Network-trace to Termly's own content endpoint, then `curl` with `Accept-Language: en-US,en;q=0.9` | **HTTP 200, 196,176 bytes, ENGLISH — the complete document** |

Working route:
`GET https://app.termly.io/api/v1/consumer/policies/186bf27c-eb55-4548-a82c-ea2013d118a0/content`
with an English `Accept-Language` header. 29 numbered sections recovered: 1. OUR SERVICES,
2. INTELLECTUAL PROPERTY RIGHTS, 3. USER REPRESENTATIONS, 4. USER REGISTRATION, 5. PURCHASES AND
PAYMENT, 6. SUBSCRIPTIONS, 7. PROHIBITED ACTIVITIES, 8. USER GENERATED CONTRIBUTIONS,
9. CONTRIBUTION LICENSE, 10. SOCIAL MEDIA, 11. THIRD-PARTY WEBSITES AND CONTENT, 12. ADVERTISERS,
13. SERVICES MANAGEMENT, 14. PRIVACY POLICY, 15. COPYRIGHT INFRINGEMENTS, 16. TERM AND TERMINATION,
17. MODIFICATIONS AND INTERRUPTIONS, 18. GOVERNING LAW, 19. DISPUTE RESOLUTION, 20. CORRECTIONS,
21. DISCLAIMER, 22. LIMITATIONS OF LIABILITY, 23. INDEMNIFICATION, 24. USER DATA,
25. ELECTRONIC COMMUNICATIONS, 26. CALIFORNIA USERS AND RESIDENTS, 27. MISCELLANEOUS,
28. RESPONSIBLE USE OF JOBSCAN, 29. CONTACT US.

**Strongest temporal warrant in this file:** the retrieved document self-dates
**"Last updated March 16, 2026"**. That precedes the collection window and the record's 2026-08-15
coding date, so the English text read today is the same version that was on the site when the coder
was blocked. For this record the post-window caveat is close to weightless.

### `commercial_use_lowest_tier`

**Result: RETRIEVED, and it addresses the construct.**

Section 2 (Intellectual Property Rights):

> "The Content and Marks are provided in or through the Services "AS IS" for your **personal,
> non-commercial use or internal business purpose only**."

> "…we grant you a non-exclusive, non-transferable, revocable license to: access the Services; and
> download or print a copy of any portion of the Content to which you have properly gained access,
> **solely for your personal, non-commercial use or internal business purpose**."

Section 7 (Prohibited Activities):

> "The Services **may not be used in connection with any commercial endeavors** except those that are
> specifically endorsed or approved by us."

> "Use the Services as part of any effort to compete with us or otherwise use the Services and/or the
> Content for **any revenue-generating endeavor or commercial enterprise**." [listed as prohibited]

Section 28 (Responsible Use of Jobscan):

> "Jobscan's **Free and Premium** subscriptions are services that may be used only by individuals
> seeking employment and/or career information. Individuals are not permitted to share accounts or
> utilize these services on behalf of others. Jobscan does permit employment professionals (e.g.,
> career coaches, recruiters, resume writers, etc.) to use Jobscan's services on behalf of more than
> one individual with the purchase of a **Jobscan Coach** subscription."

The restriction is stated identically for Free and Premium — **no tier gate** — and the only route to
professional/third-party use is a separately named product (Jobscan Coach) outside this record's
entry tier. The record's statement that "no other accessible document addresses commercial use of
Jobscan-generated content" was true of the documents it could reach; the first-ranked document
addresses it at length.

### `output_ownership_statement`

**Result: RETRIEVED, and it addresses the construct — with a scope caveat the adjudicator must weigh.**

Section 9 (Contribution License):

> "You waive all moral rights in your Contributions, and you warrant that moral rights have not
> otherwise been asserted in your Contributions. **We do not assert any ownership over your
> Contributions. You retain full ownership of all of your Contributions and any intellectual property
> rights or other proprietary rights associated with your Contributions.**"

preceded, in the same section, by a broad licence grant running the other way:

> "…royalty-free, fully-paid, worldwide right, and license to: use, copy, reproduce, distribute, sell,
> resell, publish, broadcast, retitle, store, publicly perform, publicly display, reformat, translate,
> excerpt (in whole or in part), and exploit your Contributions (including, without limitation, your
> image, name, and voice) for any purpose, commercial, advertising, or otherwise…"

And separately, for feedback, ownership runs to Jobscan:

> "By directly sending us any question, comment, suggestion, idea, feedback, or other information
> about the Services ("Submissions"), you agree to assign to us all intellectual property rights in
> such Submission."

**Scope caveat.** "Contributions" is defined in Section 8 as content posted through interactive
surfaces — "The Services may invite you to chat, contribute to, or participate in blogs, message
boards, online forums, and other functionality during which you may create, submit, post, display,
transmit, publish, distribute, or broadcast content and materials to us or through the Services". The
ToS never uses "AI", "artificial" or "output"; "resume" appears twice and "generat" only inside
"revenue-generating". So the document contains a clear ownership statement about user content in the
Services, but does not speak explicitly to AI-generated resume or cover-letter output. **This is the
same construct-scope ambiguity the record already identified in the SaaS Agreement's "Customer
Content"** — and the record was right to refuse to treat that as conclusive. Whether Section 9 reaches
generated output is a coding judgment, not a retrieval question; I record it as "addresses" because
the first-ranked document does carry an on-point ownership clause, and flag the ambiguity so an
adjudicator can move it.

### `unquantified_limit_clause`

**Result: RETRIEVED, and it addresses the construct.**

The codebook requires reading the terms of service **and** the acceptable-use policy in full before
`absent` may be coded; the record could code neither way because the ToS was unreadable. Both are now
read: the full 29-section ToS, and Section 28 "RESPONSIBLE USE OF JOBSCAN", which is the
acceptable-use content (there is no separate AUP document).

Zero matches for "fair use" and "throttl". Section 13 (Services Management) carries a discretionary,
unquantified clause tied to resource consumption:

> "We reserve the right, but not the obligation, to: … (3) in our sole discretion and without
> limitation, refuse, restrict access to, limit the availability of, or disable (to the extent
> technologically feasible) any of your Contributions or any portion thereof; (4) **in our sole
> discretion and without limitation, notice, or liability, to remove from the Services or otherwise
> disable all files and content that are excessive in size or are in any way burdensome to our
> systems**; and (5) otherwise manage the Services in a manner designed to protect our rights and
> property and to facilitate the proper functioning of the Services."

The other two "excessive" hits are not usage-volume clauses and are excluded on the codebook's own
rule: "excessive use of capital letters and spamming" (conduct), and arbitration fees "determined by
the arbitrator to be excessive".

**This also bears on a caveat the record itself raised.** `usage_cap_quantified` was coded
`all_caps_quantified` from the entry tier's four "Unlimited" claims, with an explicit note that the
ToS — "a plausible location for a qualifying fair-use clause" — could not be read. It has now been
read. There is no fair-use clause, but there *is* a sole-discretion clause permitting Jobscan to
restrict availability of a user's Contributions and to disable content "excessive in size or … in any
way burdensome to our systems". That is the qualifying-clause question the record flagged, now
answerable. `usage_cap_quantified` was not one of my 21 and I have not re-read it against the
codebook; I flag it because the record asked for exactly this.

---

## Summary

| Outcome | Count |
|---|---|
| **RETRIEVED, and it addresses the construct** — the vendor documented the thing and our instrument missed it | **10** |
| **RETRIEVED, and it does NOT address the construct** — the original `unknown` was vendor silence, and the attribution should be revisited | **10** |
| **STILL UNREACHABLE** after three or more independent routes | **1** |
| **Total** | **21** |

### By record

| Record | Value | Outcome |
|---|---|---|
| pass1/canva | `free_plan_watermark` | retrieved — addresses |
| pass1/canva | `watermark_removal_tier` | retrieved — addresses |
| pass1/hailuo-ai | `annual_default_toggle` | **still unreachable** |
| pass1/lovo-ai | `failed_generation_charge_policy` | retrieved — silent |
| pass1/openai-sora | `mandatory_addon_present` | retrieved — addresses |
| pass1/openai-sora | `annual_default_toggle` | retrieved — addresses *(weakest; could move to silent)* |
| pass1/openai-sora | `usage_cap_quantified` | retrieved — addresses |
| pass1/openai-sora | `first_charge_amount_usd` | retrieved — silent |
| pass1/openai-sora | `trial_exists` | retrieved — silent |
| pass1/openai-sora | `trial_length_days` | retrieved — silent |
| pass1/openai-sora | `trial_auto_converts` | retrieved — silent |
| pass1/openai-sora | `credit_unit_defined` | retrieved — silent |
| pass1/openai-sora | `credit_to_output_rate_published` | retrieved — silent |
| pass1/openai-sora | `cost_per_output_computable` | retrieved — silent |
| pass1/picsart | `cost_per_output_computable` | retrieved — silent |
| pass1/runway | `failed_generation_charge_policy` | retrieved — addresses |
| pass1/wix | `output_ownership_statement` | retrieved — addresses |
| pass1/wix | `commercial_use_lowest_tier` | retrieved — silent |
| pass2/jobscan | `commercial_use_lowest_tier` | retrieved — addresses |
| pass2/jobscan | `output_ownership_statement` | retrieved — addresses *(scope caveat)* |
| pass2/jobscan | `unquantified_limit_clause` | retrieved — addresses |

### What this means for how the study describes its own coverage

**20 of 21 were retrievable.** One was genuinely, permanently out of reach. The study has earned the
right to claim exactly one access failure among these, not twenty-one.

**Say plainly that the instrument under-retrieved, and say how.** Four distinct mechanisms account
for almost all of it, and none of them is exotic:

1. **A bot wall was treated as an absent document.** Canva, Runway and LOVO help-centre articles all
   return 403 to static fetchers and render normally in an ordinary browser. The study already had
   the rule that authorises this (D-005) and applied it to pricing pages, but not to help-centre
   articles, where it applied equally.
2. **A single archive capture was generalised to the archive.** The Sora Billing FAQ has 31 captures.
   The coder checked the most recent, correctly found a bot-wall shell, and concluded the document was
   unrecoverable. Thirty earlier captures existed; two carry the complete article. Compounding this,
   archive.org's `id_` responses are gzipped, so a capture that *was* retrieved could still read as
   empty.
3. **A locale or a translation layer was mistaken for the document.** Wix's Terms of Use renders
   Sections 2-19 in at least six languages and not in English. Jobscan's ToS is served by a
   third-party viewer that localises client-side; the English text sits behind that widget's own
   content endpoint. In both cases the document existed and was reachable; the *English rendering*
   was the broken thing.
4. **A rendered figure was read where a data layer was available.** Picsart's pricing page ships a
   country-keyed, multi-currency price table in its own payload. Reading the rendered TRY text and
   then hunting archive.org for a US view was the long way round, and it failed where one request
   would have succeeded.

**The finding is not uniformly embarrassing, and the paper should not present it that way.** Ten of
the twenty retrievals came back *silent* — including seven of the ten Sora values. For Sora
especially, the supplementary check produces a stronger claim than the original: the only Sora billing
document that ever existed has been recovered and enumerated against the complete Sora help
collection, and OpenAI never published a Sora consumer price, trial or credit definition at all. That
is a substantive result about vendor disclosure. The same is true for LOVO (53 articles, construct
absent) and Picsart (117 articles plus the vendor's own price table, no US/USD Pro row).

**Concretely, the attribution file should be revisited for 10 values** that are currently charged to
our access failure but which the retrieved documents show to be vendor silence: seven Sora values,
`picsart/cost_per_output_computable`, `wix/commercial_use_lowest_tier`, and
`lovo-ai/failed_generation_charge_policy`. That is a reclassification within `unknown`, not a change
to any coded value.

**Two caveats against my own findings.** First, everything here is a 2026-08-17 reading of a live
web, and only the Jobscan ToS ("Last updated March 16, 2026") and the Picsart Pro price
(TRY 999/yr = 83.25/mo, identical to the coded figure) carry independent evidence that what I read is
what was there during the window. The Canva, Runway and Wix readings do not, and a vendor could have
published or restored text between 2026-08-13 and today. Second, the Wix clauses are Turkish and
German renderings, not the governing English wording, which is a real evidentiary limitation for a
contractual variable and should be put to adjudication as such rather than counted as settled.

**One incomplete thread, recorded rather than hidden.** Archive.org's replay path was intermittently
offline throughout, and two threads did not finish: the Hailuo `/subscribe` captures (2 of 59
attempted, neither returned) and the "Sora - Release Notes" article (18 captures enumerated, none
returned). Neither is load-bearing — Hailuo's toggle would not survive a non-JS crawl in any case,
and the Sora collection enumeration already establishes that the Billing FAQ was the only billing
document — but both should be re-run when archive.org is healthy, and the Hailuo conclusion should be
read as "unreachable, with one route still owed" rather than fully exhausted.
