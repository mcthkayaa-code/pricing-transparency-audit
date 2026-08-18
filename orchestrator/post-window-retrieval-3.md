# Post-window supplementary retrieval — third sweep

**Run date: 2026-08-17. All readings in this file are post-window.**

The collection window closed **2026-08-13** and the frame is frozen. Nothing in this file has been
merged into any record, and **no coded value has been altered**. Every record referenced below is
untouched. This is a supplementary check that stands *beside* the frozen dataset.

## Why this sweep exists

Two things converged.

**The archive came back.** D-073 verified it: the 92 citations the service had refused across three
sweeps were re-asked and all 92 answered `ok`. Every thread the two prior sweeps recorded as *owed*
became runnable, and this sweep is the first that could read an archive capture since the first one.

**Five threads were explicitly owed.** D-051 left three (a `fail`/`error` scan of a recovered billing
article, one vendor's window-era capture, and a second retrieval arm for three currency records) and
D-050 left two (one vendor's captures and another's release notes, both blocked when the replay path
and the CDX index were down together). One coded value —
`openai-sora/failed_generation_charge_policy` — was deliberately **held** in `access_failure` pending
the first of these, on the sound principle that sweeping in a reclassification an agent marked
conditional would defeat the point of asking it to mark conditions.

**Scope.** Part 1 is those five threads. Part 2 was 14 remaining `access_failure` values; the
orchestrator narrowed it mid-run to **13 across five products**, removing `wix/output_ownership_statement`
because a research-adjudicator now owns that whole record. The 13 were verified row-by-row against
`orchestrator/unknown-attribution.csv` (`kind == access_failure`, 17 rows total: my 13, the three
`pass2/jobscan` rows the first sweep already handled, and the withdrawn wix row).

## Method

Same as the two prior sweeps: three independent routes minimum before declaring anything unreachable
— the live URL, an archive capture, and at least one alternative (timemap enumeration, trailing-slash
and locale variants, the `id_` raw endpoint, Common Crawl, the vendor's own content endpoint, or a
rendered read). Protocol §6.3 observed throughout: **no account created, no login, no terms or
consent accepted, no trial started, no checkout, no payment details, no CAPTCHA solved and no bot
wall evaded.** Canva's cookie banner was left unaccepted and the article body was read from the DOM
independently of consent state, the same condition the first sweep relied on. One document
(`main--da-cc--adobecom.aem.page`) returns HTTP 401 and was left closed.

Because the coordinator raised it mid-run, stated explicitly: **no finding in this sweep rests on a
non-English rendering.** Nothing here needed a locale variant, and the one translated-body trap the
coordinator warned about (a third-party viewer localising to the request locale) did not arise —
every document below was read in English from the vendor's own origin or from an archive capture of
it.

---

## Infrastructure note: the archive is *back*, not *healthy*, and it has a new trap

This matters for anyone re-running the work, and it changes the advice the first two sweeps gave.

| Endpoint | State today |
|---|---|
| `web.archive.org` homepage | **200** |
| **Replay path** (`/web/<ts>[id_]/<url>`) | **Works, but flaps.** 503 and 200 interleave on the *same* URL seconds apart. Success came on try 1, 2, 5, 6, 7, 8, 9, 12 and 13 across this run; two captures failed 14 and 16 consecutive tries and then were not retried |
| **Memento timemap** | **Works, with a new failure mode — see below** |
| **CDX index** (`/cdx/search/cdx`) | **Still 503**, a third consecutive day |
| `archive.org/wayback/available` | **429** |
| **Common Crawl index** | Up, but 504s under any pace faster than ~20s between requests |

**The new trap, and it is the mechanical lesson of this run: the Memento timemap returns HTTP 200
with a ZERO-BYTE body when it is degraded.** A naive enumerator counts `rel="memento"` occurrences in
an empty string, gets zero, and records "this URL was never archived". In this run that artefact hit
five URLs in a single batch, including one that in fact has 66 captures. Every one of them returned
real mementos on retry minutes later.

This is a sibling of sweep 2's trailing-slash finding, and it is worse, because a trailing-slash miss
is reproducible while this one is not: run it twice and you get two different "facts". **Treat a
zero-byte 200 as an outage, not as an answer.** The same discipline applies to Common Crawl's index,
where **404 means "no record in this index" and 502/504 mean "the service did not answer"** — two
outcomes that a `try/except` collapses into one.

Concretely: this sweep's first timemap batch returned "0 mementos" for the Canva watermarks article,
the Adobe Firefly plans page, the Hailuo subscribe page and the GPTZero pricing page. On retry those
are **12, (still inconclusive), 66 and 66**. Had I stopped at the first batch, this file would have
reported four documents as never archived, and three of those four would have been wrong.

---

# Part 1 — the five owed threads

## Thread 1 (D-051) · The `fail`/`error` scan of the recovered billing article — **RUN, and it closes the hold**

**What was owed.** Sweep 1 recovered the Sora Billing FAQ from two captures and keyword-scanned it
for `$`, `credit`, `trial`, `annual`, `yearly`, `refund`, `monthly`, `concurrent`, `resolution`,
`unlimited` and `watermark`. It **did not scan for `fail` or `error`**, which are the decisive terms
for `failed_generation_charge_policy`. Sweep 2 could not run the scan because replay was down, marked
its conclusion conditional, and said to hold the value. It was held.

**Captures read today, both in full:**

| Capture | Result |
|---|---|
| `https://web.archive.org/web/20260201090715id_/https://help.openai.com/en/articles/10245774-sora-billing-credits-faq` | **200, 54,221 bytes decompressed**, title "Sora - Billing FAQ \| OpenAI Help Center", 4,708 chars of visible text |
| `https://web.archive.org/web/20251124172907id_/https://help.openai.com/en/articles/10245774-sora-billing-credits-faq` | **200, 51,172 bytes decompressed**, same title, 4,560 chars |

Sweep 1's byte counts (54,221 and 51,164) and its 4,706-char text figure reproduce to within
whitespace. **This is also the first independent re-verification of sweep 1's Sora recovery** — the
thing sweep 2 named as its own central caveat ("fourteen of these twenty-five results are inherited,
not re-verified").

**The scan, on both captures:**

| term | 2026-02-01 | 2025-11-24 |
|---|---|---|
| `fail` | **0** | **0** |
| `unsuccessful` | **0** | **0** |
| `deduct` | **0** | **0** |
| `error` | 2 | 2 |

**Both `error` hits are unrelated.** They are one account-deletion FAQ, quoted in full so the negative
is checkable rather than asserted:

> "Why do I get the error, "You do not have an account because it has been deleted or deactivated"?
> If you get this error when you try to login or create an account it means the account associated
> with the email address you're trying to use to sign up for / login to an account underwent an
> account deletion…"

**Result: the scan is complete and the construct is absent.** The hold can be released. Detail and
the recommendation are under `openai-sora/failed_generation_charge_policy` in Part 2.

Also re-verified independently today: the **Sora collection capture 20260331195237** enumerates
exactly **13 articles**, matching sweep 1's list item for item.

## Thread 2 (D-051) · Adobe Firefly's window-era capture `20260806112138` — **RUN, and the route is structurally empty**

**What was owed.** Sweep 2 recovered Firefly's eleven-answer plans-page FAQ by reading `textContent`
of the collapsed accordion targets, found zero occurrences of "trial" and no `N-day` pattern, and
recorded a temporal caveat: the FAQ carries no last-updated stamp, so today's text might not be
window-era text. The record's own `sources` list names a window-era capture that would settle it.

**Capture read today:**
`https://web.archive.org/web/20260806112138id_/https://www.adobe.com/products/firefly/plans.html`
— **200, 4,635 bytes gzipped, 19,065 chars decompressed**, title "Compare plans that include
generative AI | Adobe Firefly".

**The capture does not contain the FAQ answers, and it cannot.** adobe.com serves this page as an
AEM/Franklin skeleton that assembles itself at runtime from document fragments. The served HTML
carries placeholder tokens (`{{individuals}}`, `{{students-and-teachers}}`) and **fragment references**,
one of which is the FAQ:

> `https://main--da-cc--adobecom.aem.page/cc-shared/fragments/products/firefly/plans/faq`

Scan of the whole window-era capture: **zero price figures** (all 17 `$` hits are JavaScript template
literals in a sitemap helper), **zero `N-day` patterns**, and two "trial" hits that are both the name
of a scheduled promo manifest (`free-trial-brick-rollout`, scheduled 2026-02-23 → 2030-12-31), not a
trial length.

**So the capture gives a partial temporal warrant and no more.** It establishes two things about the
window: the FAQ block *was* on the page, and the *served* document carried no trial length. It cannot
establish what the FAQ answers said, because those answers were never in the served document.

**One route did open, and it is worth recording.** The authoring origin the capture names
(`…aem.page`) returns **401** and was left closed. The *published* origin serves the same fragment
publicly:

`https://main--da-cc--adobecom.aem.live/cc-shared/fragments/products/firefly/plans/faq.plain.html`
— **200, 7,382 bytes**, a plain static document containing **all eleven questions** and the full
answers. Its `last-modified` header reads today's date, which is a publish/edge timestamp and carries
no evidentiary weight.

Read from that fragment, sweep 2's findings reproduce exactly: **`trial` 0, `day` 0, `\d{1,2}[- ]days?`
0**, and the cost answer verbatim —

> "Adobe Firefly offers a free plan with limited daily generations, plus four paid tiers: Adobe
> Firefly Standard: $9.99/month — 2,000 generative credits · Adobe Firefly Pro: $19.99/month — 4,000
> generative credits · Adobe Firefly Pro Plus: $49.99/month — 10,000 generative credits · Adobe
> Firefly Premium: $199.99/month — 50,000 generative credits plus unlimited Adobe Firefly Video Model
> access."

That is an **independent second route** to sweep 2's `textContent` read — a static document rather
than a rendered DOM — which removes any worry that the accordion read was a rendering artefact. It
does not remove the temporal caveat.

**Recommendation: the thread is closed as run, and sweep 2's temporal caveat on this record STANDS.**
`adobe-firefly/trial_length_days` is already `vendor_silence` and is not in my 13; nothing here moves
it. The finding to carry forward is methodological, and it extends D-057's class: **a page whose text
is assembled client-side from fragments is unarchivable in principle**, exactly as a page whose price
is rendered client-side is. The archive stores the skeleton. For this vendor an archive capture can
never window-date the FAQ, so the item should be retired from the owed list rather than re-queued.

## Thread 3 (D-051) · Arm 2 for the three currency records — **RUN; one decisive, two have no capture to read**

**What was owed.** A US-crawled capture for `canva`, `gptzero` and `phrasly`. Sweep 2 could not run
it. Of the three, only **gptzero/`headline_price_usd`** is still charged to `access_failure`; canva's
two currency values are already `instrument_gap` and phrasly's two went to adjudication as A-020. So
this thread is decisive for one value and completeness for the rest.

### gptzero — decisive, and it confirms D-057

Common Crawl index `CC-MAIN-2026-25` holds one record for `https://gptzero.me/pricing`. Fetched
properly — index lookup, then a WARC byte-range request — and decompressed:

- capture **`20260610145446`**, `WARC-Target-URI: https://gptzero.me/pricing`, 476,546 chars
- **`cf-ray: a09936914f539c5e-IAD`**

That `cf-ray` suffix is the load-bearing detail and it is stronger than the general claim that
Common Crawl runs on US infrastructure: **IAD is Cloudflare's Washington-Dulles edge.** The capture is
header-level proof of a document served to a client positioned in the United States.

**Result: RETRIEVED, and it does NOT address the construct.** The US-served document is a
pre-hydration shell. Scan: `PREMIUM` 0, `MOST POPULAR` 0, `billed annually` 0, `words per month` 0,
`Choose Plan` 0, `/month` 0, `priceCurrency` 0, `unit_amount` 0. The three apparent `USD`/`TRY`/`549`
hits are base64 blobs and a JS chunk id (`675549`); the only dollar figures in the whole document are
a placeholder plan card that renders zeroes before hydration —

> `<span class="title-large cl-mr-2">$0</span><span…>per <!-- -->year</span>` … `Save <!-- -->$0<span class="body-small">/year</span>`

This independently reproduces D-057 on the same capture, from a fresh index lookup and a fresh WARC
fetch. **A US reader is served no price by this document either.** The `unknown` is not about our
geography and it is not about our reach.

### canva and phrasly — no US-crawled capture exists to read

| query | CC-MAIN-2026-30 | CC-MAIN-2026-25 |
|---|---|---|
| `https://www.canva.com/pricing/` | **404 (no record)** | 504 (inconclusive) |
| `https://www.canva.com/help/watermarks-design/` | **404 (no record)** | 504 (inconclusive) |
| `https://phrasly.ai/pricing` | **404 (no record)** | **404 (no record)** |

Consistent with D-057, which found Common Crawl holds no capture of these pricing pages, only the
vendors' homepages. Arm 2 cannot be run for canva or phrasly because there is nothing to run it
against — which is a different and more honest statement than "Arm 2 is owed".

**Recommendation: thread closed.** For `gptzero/headline_price_usd` see Part 2; for canva and phrasly
no further Arm 2 work is possible and the item should be retired rather than re-queued.

## Thread 4 (D-050) · Hailuo's `/subscribe` captures — **RUN, and they confirm the study's one real access failure**

**What was owed.** Sweep 1 enumerated 59 captures of `https://hailuoai.video/subscribe`, attempted
two, and got neither; it recorded its conclusion as "unreachable, with one route still owed".

Timemap today: **66 mementos**, 2024-11-03 → 2026-08-07, including the two **in-window** captures
sweep 1 named. Both read in full:

| Capture | Result |
|---|---|
| `https://web.archive.org/web/20260807114246id_/https://hailuoai.video/subscribe` | **200, 645,309 chars decompressed** |
| `https://web.archive.org/web/20260806052203id_/https://hailuoai.video/subscribe` | **200, 640,382 chars decompressed** |

**Result: STILL UNREACHABLE — and this is now an exhausted route, not an owed one.**

Both in-window captures reproduce sweep 1's live reading of the same page exactly:

- **Visible text: 149 and 146 characters.** In full, the 08-07 capture: "Hailuo AI Subscription Plans
  for Video and Image Tools Home Design Hot Assets Tools Video H3 Image Audio **From /mo** Sign In
  Explore Mine Subscribe Menu"
- **No plan grid and no toggle element.** `aria-selected` 0, `checked` 0, `defaultValue` 0,
  `activeTab` 0, `selectedKey` 0, `data-state` 0.
- The i18n payload carries the same vendor-authored strings sweep 1 quoted from the live page —
  `"subscribe_toggle_yearly":"-46% OFF"`, `"subscribe_year_unit":"Yearly"`,
  `"subscription_annual_discount":"%s off billed annually"`,
  `"bk_hard_moss_charge_combo_desc_3":"Yearly Standard Subscription"` — and the price labels are
  still **format strings**, e.g. `"$$%.2f billed yearly"`.
- The only USD figures in the whole capture sit in the affiliate FAQ string, again as sweep 1 found:
  "$34.99 is the Pro Monthly Plan price, $1139.88 is the Unlimited Yearly Plan price".

The captures are **window-dated** (2026-08-06 and 2026-08-07, both inside the window), which makes
this the best-warranted negative in the file: on the two days the archive crawled this page during
the collection window, the served document contained no toggle in any state.

**Recommendation: `hailuo-ai/annual_default_toggle` stays `access_failure`,** and the study can now
say so with the archive route closed rather than pending. The plan UI is behind an authenticated
session the protocol forbids creating, and no capture of the public URL has ever contained it.

## Thread 5 (D-050) · "Sora - Release Notes" — **RUN, and it is the one thread that was not harmless**

**What was owed.** Sweep 1 queued this article against 18 enumerated captures, got none, and wrote:
"Neither is load-bearing — … the Sora collection enumeration already establishes that the Billing FAQ
was the only billing document."

**That reasoning is the thing this thread breaks.**

First the mechanics. The slug is not guessable: `…/10245775-sora-release-notes` returns an empty
timemap, and the article is `12593142-sora-release-notes`, recovered from the collection capture. Its
timemap returns **18 mementos**, matching sweep 1's count exactly. Two read in full:

| Capture | Result |
|---|---|
| `https://web.archive.org/web/20260327070818id_/https://help.openai.com/en/articles/12593142-sora-release-notes` | **200, 57,284 chars decompressed**, "Updated: 6 days ago", 8,498 chars of text — the last capture before the 2026-04-26 shutdown |
| `https://web.archive.org/web/20251118153743id_/https://help.openai.com/en/articles/12593142-sora-release-notes` | **200, 40,877 chars decompressed**, 3,947 chars of text |

**The release notes link out to a second billing document, and it is a Sora one.** The entry dated
**October 30, 2025**:

> "Today we're introducing ways to purchase additional usage in products like Codex and Sora. If you
> hit your included limits, you can seamlessly buy more credits right in the Codex dashboard or buy
> more video generations in the Sora app to keep going. Learn more in our article: **Using Credits for
> Flexible Usage in ChatGPT (Free/Go/Plus/Pro) & Sora**."

That article is `https://help.openai.com/en/articles/12642688-using-credits-for-flexible-usage-in-chatgpt-plus-pro`.
It sits in the **ChatGPT** collection, not the Sora collection — which is precisely why enumerating
the Sora collection did not find it. It has 6 captures. Three read in full:

| Capture | Title | `sora` count |
|---|---|---|
| `…/20251221123946id_/…` | "Using Credits for Flexible Usage in ChatGPT (Free/Go/Plus/Pro) **& Sora**" | **24** |
| `…/20260328012520id_/…` | same, "Updated: 17 days ago" | **28** |
| `…/20260731141818id_/…` | "Using Credits for Flexible Usage in ChatGPT (Free/Go/Plus/Pro)" — **Sora dropped from the title** | **0** |

**The two pre-shutdown captures publish a complete Sora 2 credit rate card**, verbatim from the
2026-03-28 capture:

> "**Rate Card** … **Sora 2** — Video Type / Unit / Credits\*: Sora 2, 10s · 1 Video Gens · 10 credits\* ·
> Sora 2, 15s · 2 Video Gens · 20 credits\* · Sora 2, 25s (ChatGPT Pro only) · 3 Video Gens · 30 Credits\*\*
> **Sora 2 Pro** (currently available for ChatGPT Pro users only): Standard Resolution, 10s · 4 Video
> Gens · 40 credits\*\* · Standard Resolution, 15s · 8 Video Gens · 80 credits\*\* · 25s · 12 Video Gens ·
> 120 credits\*\* · High Resolution, 10s · 25 Video Gens · 250 credits\*\* · High Resolution, 15s · 50
> Video Gens · 500 credits\*\*"

> "\*Credits per video will vary based on length, resolution, and other factors. Longer videos may cost
> more credits per second due to additional compute requirements."

and, in the same document:

> "Credits are a pay-as-you-go add-on for Codex & Sora when you need more usage beyond plan limits"
> · "**Nothing about your plan changes. You still get your plan's included usage.**"

> "Do credits expire or roll over? **Credits are valid for 12 months from purchase. Unused credits
> expire and do not roll over after the expiry date.**"

> "Currently, this includes Codex for Plus/Pro subscribers and **Sora for all users**."

**Why this matters beyond its own thread.** Sweep 1's central Sora claim — repeated into D-050 as the
study's strongest positive result — is that "**Sora - Billing FAQ is the only billing document that
ever existed in the collection**" and therefore "OpenAI never published a Sora credit definition". The
first half is true and remains true: within the *Sora collection*, it was the only billing document.
**The second half does not survive.** OpenAI published a Sora 2 credit unit ("1 Video Gens"), a Sora 2
credit-to-output rate card, and a credit expiry policy, in a ChatGPT-collection article the Sora
release notes linked to directly.

**And the timing is the whole finding.** By the window-era capture (2026-07-31, "Updated: yesterday",
i.e. ~2026-07-30, which predates the window close), **Sora had been removed from that article
entirely** — from its title and from all 46 occurrences of "credit" in its body, which by then read
"Credits currently can only be used with Codex (for Plus/Pro users only) and ChatGPT for Excel."

So at the coding date the vendor was silent, and before the shutdown it was not. That is neither
`vendor_silence` in the ordinary sense nor `access_failure`: it is **published-then-withdrawn**, and
the instrument's three-kind vocabulary has no slot for it. I have not tried to force it into one. See
the recommendation under Part 2 and the conditional flag at the end.

**One more document, reached from the same trail.** The credits article links to "Generating videos on
Sora" (`9957612`), a Sora-collection article sweep 1 enumerated but never read. Its timemap returns
**291 mementos**; the last pre-shutdown one (`20260414100838`, "Updated: 6 hours ago") reads in full
and carries the same tier table as the Billing FAQ, self-scoped identically to "Sora 1 on Web".
Its scan: `fail` 0, `error` 0, `deduct` 0, `credit` 0, `$` 0.

---

# Part 2 — the 13 remaining `access_failure` values

## `pass1/canva` — `free_plan_watermark`, `watermark_removal_tier`

**What was unreachable.** Per the record's own basis: the Help Centre article "Watermarks or Canva
logos are on my design" (`https://www.canva.com/help/watermarks-design/`), which the record correctly
declined to call vendor silence. Sweep 1 retrieved it by rendered read.

**Routes tried today**

| Route | Outcome |
|---|---|
| Ordinary rendered browser load (D-005) | **HTTP 200**, title "Watermarks or Canva logos are on my design - Canva Help Center", 112,030 chars of body text, 110 occurrences of "watermark". Cookie banner **not accepted**; body present in the DOM regardless |
| Timemap, first attempt | "0 mementos" — **the zero-byte artefact**, see the infrastructure note |
| Timemap, retry | **12 mementos**, 2022-10-05 → 2025-08-12 |
| Captures `20250812165803`, `20250621120452`, `20221005031835` (raw `id_`) | **All three retrieved, and all three are the same shell**: "Please update your browser / It seems you are using an old or unsupported browser", 342–364 chars, **`watermark` count 0**. Titles "Unsupported client – Canva" and "Amazingly Simple Graphic Design Software – Canva" |
| Common Crawl, `CC-MAIN-2026-30` | **404 — no record** |
| Page's own last-updated stamp | **None.** No `<time>` element, no `[datetime]`, no date meta tag |

**Result for both values: RETRIEVED, and the document ADDRESSES the construct — reproducing sweep 1
verbatim.** Every quotation sweep 1 took is present today, checked string by string:

`free_plan_watermark`:

> "Premium elements will have watermarks on your design if you're a Canva Free user. Learn more below."

> "As part of the Canva Print order process, we ask you to download and review a PDF proof. For Canva
> Free users, if you used premium elements in your design, this proof will be watermarked."

`watermark_removal_tier`:

> "Upgrade from Canva Free to Canva Pro or Canva Teams."

> "Upgrade to Canva Pro or Canva Teams for unlimited access to our extended library of premium images,
> videos, templates, and more for free."

> "Select the Remove watermarks button on an element to purchase it."

and the negative confirmation, under its own heading "I'm on Canva Pro or Canva Teams but I still see
watermarks":

> "If you're on Canva Pro or Canva Teams but still see watermarks on your design, you might be in the
> wrong account or team."

Source: `https://www.canva.com/help/watermarks-design/`, rendered read 2026-08-17.

**Window-dated: NO, and this sweep establishes that it cannot be.** Canva serves archive.org's crawler
an unsupported-client page, so all twelve captures spanning three years are shells; Common Crawl has
no record; and the article carries no last-updated stamp. There is **no route by which this text can
be dated to the window**. That is a firmer statement than sweep 1's silence on the question, and it
should replace the open temporal caveat rather than sit beside it.

**Recommendation: both stay in `access_failure`** — the document exists, addresses the construct, and
our instrument missed it, which is exactly what that label means. The coded `unknown`s do not change
(the reading is post-window). **Confidence: high on the retrieval, high on the label.**

## `pass1/gptzero` — `headline_price_usd`

**What was unreachable.** A resolved USD figure on `https://gptzero.me/pricing`. Note this row's
provenance: it is the only one of the 13 with `decided_by = pattern` rather than `hand` — machine-set
off the regex `\bcould not (?:be )?(?:open|reach|retriev|load|access|fetch|archiv)`, on an
adjudicated record whose own evidence says both passes AGREED and that the vendor's ToS §5 ("All
payments shall be in U.S. dollars") makes a USD figure plausible.

**Routes tried today.** Thread 3 above, in full. The decisive one:

**Common Crawl `CC-MAIN-2026-25`, capture `20260610145446`**, WARC byte-range fetch, 476,546 chars,
`cf-ray: a09936914f539c5e-IAD` — a document served to a **US-positioned client**.

**Result: RETRIEVED, and it does NOT address the construct.** The US-served document is a
pre-hydration shell with no plan cards and no price; its only dollar figures are `$0` placeholders.
Combined with sweep 2's exhaustive live work on the same page (no price API, no parameter or header
that changes the currency, and a JS-bundle audit showing the currency is server-supplied per request),
**no reading position available to this study — ours or a US one — obtains a USD figure from this
vendor's served document.**

**Window-dated: partially.** The capture is 2026-06-10, two months before the window rather than
inside it, so it dates the *mechanism* but not the window state. Sweep 2's independent live reading of
TRY 549/month billed annually — the exact figure the record coded and re-confirmed on 2026-08-10 —
supplies the window-era continuity.

**Recommendation: move from `access_failure` to `instrument_gap`,** joining its two Canva siblings.
The reasoning is sweep 2's and D-051's, now with the missing arm actually run: the vendor plainly
publishes a price, the document is fully readable, and what fails is D-007's "US reader" test, for
which the protocol supplies no executable route. **This is not a retrieval failure and the study
should stop calling it one. Confidence: high.**

## `pass1/hailuo-ai` — `annual_default_toggle`

**Result: STILL UNREACHABLE.** Thread 4 above. Two **in-window** captures (2026-08-06, 2026-08-07)
read in full; neither contains a plan grid, a toggle element, or any default-state markup.

**Window-dated: YES** — uniquely in this file, the evidence is from inside the collection window.

**Recommendation: stays `access_failure`.** This remains the study's single genuine, permanent access
failure across all 47 values ever charged to that label, and the archive route is now exhausted rather
than owed. **Confidence: high.**

## `pass1/openai-sora` — eight values

All eight sit on documents reached today. The evidence base is now **ten Sora-related documents**, all
recovered from the archive and all read in full: two Billing FAQ captures, two Release Notes captures,
three captures of the ChatGPT/Sora credits article, "Generating videos on Sora", "Creating videos with
Sora", and "Getting started with the Sora app" — plus the collection capture that enumerates the
estate.

**Combined scan across all ten** (this is the table the record's ten `unknown`s should be read
against):

| term | result across all ten documents |
|---|---|
| `fail`, `unsuccessful`, `deduct` | **0 in every document** |
| `annual`, `yearly`, `trial`, `$` | **0 in every document** |
| `free plan`, `free tier` | **0 in every document** |
| `error` | 2 (account deletion) + 1 + 1 (a usage-cap message) |
| `watermark` | present in 5 |
| `credit` | 0 in every Sora-collection document; 44–51 in the ChatGPT credits article |

**The temporal fact that governs all eight.** Sora shut down **2026-04-26**, before the window opened.
Every Sora document that addresses these constructs was **withdrawn before the coding date** — the
collection is 404, the Billing FAQ is 404 on both slugs, and the credits article had dropped Sora by
its 2026-07-31 capture. So for each value below, "the vendor documented it" and "a coder in the window
could have read it" are different claims, and only the first is true.

### `failed_generation_charge_policy` — **RETRIEVED, construct ABSENT. The held value's condition is met.**

The owed scan is run, on both Billing FAQ captures: `fail` 0, `unsuccessful` 0, `deduct` 0, and both
`error` hits are the account-deletion FAQ. Extended across all ten documents, `fail`/`unsuccessful`/`deduct`
are **0 everywhere**, and the only other `error` hits are Runway-style troubleshooting text and a
usage-cap message ("You've already generated X videos in the last day"). Nothing anywhere states what
happens to allowance when a generation fails.

**Recommendation: release the hold and move to `vendor_silence`.** This is the one value in the sweep
where the condition sweep 2 set has been met exactly as it specified it. **Confidence: high.**

### `annual_default_toggle` — **RETRIEVED, construct ABSENT.**

`annual` and `yearly` are **0 across all ten documents**, against a Billing FAQ that documents a single
cadence:

> "**Subscriptions for ChatGPT plans are charged on a calendar monthly basis**, from the subscription
> start date."

No document depicts a billing toggle in any state. **Recommendation: `vendor_silence`. Confidence:
high.**

### `mandatory_addon_present` — **RETRIEVED, and it ADDRESSES the construct — CONDITIONAL on the withdrawal question.**

The record's basis is that "the billing/credits documentation that would address a required add-on
charge returns HTTP 404 live". A credits document has now been found, and it addresses a required
add-on charge directly, in the negative:

> "Credits are a pay-as-you-go add-on for Codex & Sora when you need more usage beyond plan limits"

> "What changes for my plan? **Nothing about your plan changes. You still get your plan's included
> usage.**"

An optional pay-as-you-go add-on, explicitly not required. The Billing FAQ separately shows Sora
access carried no separate price at all ("Only ChatGPT Plus users can upgrade their plan").

**Window-dated: NO — and worse than not.** The document that says this had Sora removed from it by
2026-07-31. **Recommendation: hold. Conditional** on how the study treats published-then-withdrawn
documentation. If withdrawal-before-window counts as the vendor not having published *to a
window-era reader*, this is `vendor_silence`; if the question is whether the vendor ever documented
it, this is our miss and stays `access_failure`. I decline to choose. **Confidence: low on the label,
high on the retrieval.**

### `usage_cap_quantified` — **RETRIEVED, and it ADDRESSES the construct — but only PARTLY, and CONDITIONAL.**

The record coded this `unknown` because "the entry paid tier itself could not be identified". Three
documents now quantify caps, at three different levels of completeness.

The Billing FAQ publishes per-tier limits:

> "**ChatGPT Plus / ChatGPT Business** — Unlimited images and video · Up to 480p resolution and 10s
> duration videos · Up to 1 concurrent generation
> **ChatGPT Pro** — Unlimited images and video · Faster generations · Up to 1080p resolution and 20s
> duration videos · Up to 5 concurrent generations · Download videos without a watermark"

"Creating videos with Sora" (Sora 2 era, capture `20260329180344`) publishes the cap **mechanism** and
a quantified conversion:

> "**Usage limits.** Video generations contribute to the daily limit as follows: 10-second videos
> count as one video toward the daily limit. 15-second videos count as two videos toward daily limits.
> 25-second videos count as four videos toward the daily limit."

> "How do usage limits work on the Sora app? Video creation in the Sora app uses a **rolling 24-hour
> limit per account**: each submitted request counts immediately, and there's no midnight reset… If
> you hit the cap, you'll see an error like "**You've already generated X videos in the last day**"."

**The vendor's own sentence writes the number as `X`.** So the cap's mechanism is documented, and the
*relative* cost of each duration is quantified, but the **absolute daily allowance is not published
anywhere in the recovered estate**. That is a genuinely mixed answer and I am not going to round it to
either pole. Add the same withdrawal problem as above.

**Recommendation: hold. Conditional**, on two things: whether a quantified conversion with an
unquantified absolute counts as `all_caps_quantified`, and the withdrawal question. **Confidence: low
on the label.**

### `free_plan_watermark` — **RETRIEVED, and it ADDRESSES the construct.**

The record's evidence is "No document addresses watermarking of any Sora output tier." Two documents
do, in terms. "Creating videos with Sora" (`20260329180344`):

> "Why does my download have a watermark? **At launch, all exports include a moving visible watermark**
> and C2PA provenance."

> "**When a watermark is added.** A watermark will appear on downloaded videos in the following
> situations: The video includes any character… The video depicts a public figure · **You are not
> subscribed to ChatGPT Pro** · The video uses characters in features such as Cast, Remix, or Extend."

Corroborated independently by "Getting started with the Sora app" (`20260407214549`):

> "Are videos watermarked? Yes. **At launch, all Sora videos include a visible moving watermark.** They
> also embed C2PA metadata—an industry-standard, tamper-proof signature."

Note this is Sora **2**-era documentation, so unlike sweep 2's resolution of this value it does not
depend on the "Sora 1 on Web" scope caveat, and it does not depend on the free-plan cascade at all: it
states that any non-Pro download is watermarked. **Recommendation: this is a real retrieval that
addresses the construct; the withdrawal question still applies to the label. Conditional on that
alone. Confidence: high on the retrieval.**

### `free_plan_cap_documented`, `free_plan_cap_value`, `free_plan_duration` — **RETRIEVED, construct ABSENT — and sweep 2's resolution of these should be revisited.**

`free plan` and `free tier` are **0 across all ten documents**. No document describes a free-tier
allowance, a free-tier quantity, or whether any no-cost access was perpetual.

**But the sweep found a documentary contradiction that bears directly on how sweep 2 resolved these,
and it runs against sweep 2.** Sweep 2 resolved all four `free_plan_*` cascades as "addresses via
parent", on the Billing FAQ's statement that ChatGPT Free was ineligible for Sora. Three documents now
disagree with each other:

| Document | What it says about free access |
|---|---|
| Billing FAQ (Sora 1 on Web), `20260201090715` | "Currently ChatGPT **Free**, Enterprise, and Edu accounts are **not eligible** for Sora access" |
| "Generating videos on Sora" (Sora 1 on Web), `20260414100838` | "Currently ChatGPT **Enterprise and Edu** accounts are not eligible for Sora access" — **"Free" has been dropped** |
| Credits article (Sora 2 era), `20260328012520` | "Currently, this includes Codex for Plus/Pro subscribers and **Sora for all users**" |

The record codes Sora near its shutdown, i.e. the Sora 2 era, and the Sora 2-era document says access
was for **all users**. Sweep 2 marked these four "the softest of my 'addresses' findings" and said an
adjudicator who declined either step should move them to "construct absent". **On this evidence the
premise itself is contested, not merely soft.**

**Recommendation: treat these three as construct-absent and, separately, flag sweep 2's resolution of
the `free_plan_*` family as needing an adjudicator's second look.** I am explicitly **not**
recommending a coded value; the contradiction is real and it should be adjudicated rather than swept.
**Confidence: high that the construct is absent; high that sweep 2's parent step is now doubtful; low
on any label.**

## `pass1/runway` — `failed_generation_charge_policy`

**What was unreachable.** `https://help.runwayml.com/hc/en-us/articles/32880432736659-Why-am-I-receiving-errors-when-trying-to-generate`
— the record says it "appears to address this directly but could not be fetched or archived within
budget (403 / 520)". Sweep 1 retrieved it by rendered read and found the clause.

**Routes tried today**

| Route | Outcome |
|---|---|
| Ordinary rendered browser load (D-005) | **HTTP 200**, full article, 9,907 chars; headings include a dedicated "Credits for failed generations" |
| Timemap | **4 mementos**: 20250425090104, 20250522160223, 20250723184344, 20250917234151 |
| Capture `20250917234151` (raw `id_`) | **200, 28,033 chars decompressed**, title "Why am I receiving errors when trying to generate? – Runway", 3,020 chars of text |

**Result: RETRIEVED, it ADDRESSES the construct, and it is the only value in this sweep with a genuine
temporal warrant.**

Live rendered read today, reproducing sweep 1 verbatim:

> "**Generation errors** usually occur when the model is unable to produce a high-quality output with
> the provided inputs. This error indicates that the generation process was terminated, and **credits
> (if used) will be returned to your account within a few minutes.**"

> "**Credits for failed generations.** Credits are automatically returned to your account shortly after
> a generation error. If you don't see your credit balance increase, the generation likely failed
> before credits were charged."

**And the decisive new evidence: the archive capture of 2025-09-17 carries the substantive clause
already**, word for word:

> "Generation errors usually occur when the model is unable to produce a high-quality output with the
> provided inputs. This error indicates that the generation process was terminated, and **credits (if
> used) will be returned to your account within a few minutes.**"

> "Additionally, **your credits will be refunded automatically shortly after the error.**"

Source: `https://web.archive.org/web/20250917234151id_/https://help.runwayml.com/hc/en-us/articles/32880432736659-Why-am-I-receiving-errors-when-trying-to-generate`.

**Window-dated: effectively yes, by anticipation.** The capture is **2025-09-17, eleven months before
the window**. The dedicated "Credits for failed generations" heading is newer — it is absent from the
2025 capture and present live — but the policy statement itself was published long before the coding
date and is unchanged. A vendor cannot have added this text after 2026-08-13; it was there in 2025.

**Recommendation: stays `access_failure`.** The document exists, it addresses the construct directly,
it predates the window, and our instrument did not reach it. This is the cleanest instrument-miss in
the corpus. **Confidence: high.**

---

## Summary

| Outcome | Count |
|---|---|
| **RETRIEVED, and the document ADDRESSES the construct** | **6** |
| **RETRIEVED, and the construct is ABSENT** | **6** |
| **STILL UNREACHABLE** after three or more independent routes | **1** |
| **Total** | **13** |

**Retrieved: 12 of 13. Standing unreachable: 1.**

### By value

| Record | Value | Outcome | Window-dated | Recommendation |
|---|---|---|---|---|
| pass1/canva | `free_plan_watermark` | retrieved — addresses | **no, and cannot be** | stays `access_failure` |
| pass1/canva | `watermark_removal_tier` | retrieved — addresses | **no, and cannot be** | stays `access_failure` |
| pass1/gptzero | `headline_price_usd` | retrieved — absent | partial (2026-06-10, US-served) | → **`instrument_gap`** |
| pass1/hailuo-ai | `annual_default_toggle` | **still unreachable** | **yes** (in-window captures) | stays `access_failure` |
| pass1/openai-sora | `failed_generation_charge_policy` | retrieved — absent | pre-window docs | → **`vendor_silence`** (hold released) |
| pass1/openai-sora | `annual_default_toggle` | retrieved — absent | pre-window docs | → **`vendor_silence`** |
| pass1/openai-sora | `mandatory_addon_present` | retrieved — addresses | no (withdrawn pre-window) | **hold — conditional** |
| pass1/openai-sora | `usage_cap_quantified` | retrieved — addresses *(partly)* | no (withdrawn pre-window) | **hold — conditional** |
| pass1/openai-sora | `free_plan_watermark` | retrieved — addresses | no (withdrawn pre-window) | **hold — conditional** |
| pass1/openai-sora | `free_plan_cap_documented` | retrieved — absent | no (withdrawn pre-window) | **hold — conditional** |
| pass1/openai-sora | `free_plan_cap_value` | retrieved — absent | no (withdrawn pre-window) | **hold — conditional** |
| pass1/openai-sora | `free_plan_duration` | retrieved — absent | no (withdrawn pre-window) | **hold — conditional** |
| pass1/runway | `failed_generation_charge_policy` | retrieved — addresses | **yes** (2025-09-17, pre-window) | stays `access_failure` |

### Owed threads

| Thread | Status |
|---|---|
| D-051 · `fail`/`error` scan of the recovered billing article | **RUN — closed, hold released** |
| D-051 · Adobe Firefly window-era capture `20260806112138` | **RUN — closed; route structurally empty, caveat stands** |
| D-051 · Arm 2 for canva / gptzero / phrasly | **RUN — closed; decisive for gptzero, no capture exists for the other two** |
| D-050 · Hailuo `/subscribe` captures | **RUN — closed; conclusion confirmed from in-window captures** |
| D-050 · "Sora - Release Notes" | **RUN — closed, and it broke a claim (see below)** |

**No thread from D-050 or D-051 remains owed.** Two new ones are opened at the end of this file.

---

## The direction, stated plainly

The brief warned that every successful retrieval shrinks this study's headline finding, and told me to
retrieve anyway and report what I find. Both halves happened, and they did not cancel out.

**Shrinking the headline.** The Sora Release Notes thread — which sweep 1 called "not load-bearing"
and skipped — recovered a document that publishes a Sora 2 credit unit, a full credit-to-output rate
card and a credit expiry policy. **The claim that "OpenAI never published a Sora consumer price, trial
or credit definition at all", which D-050 carried as the strongest positive result of the whole
retrieval programme, is half wrong.** It never published a price or a trial; it did publish a credit
definition and a rate card, in a ChatGPT-collection article the Sora release notes linked to in the
very entry announcing the feature. Sweep 1 enumerated the Sora collection, correctly found one billing
document *in it*, and generalised to "the only billing document that ever existed". The generalisation
was one link away from being tested.

**Not shrinking it.** Nothing in this sweep converts a coded `unknown` into a determinate value,
because everything Sora-side was withdrawn before the window; the gptzero result narrows the claim
rather than answering it; and the canva and runway retrievals were already counted as instrument
misses by sweep 1. The one value that moves cleanly — `openai-sora/failed_generation_charge_policy` —
moves *toward* vendor silence, which makes the headline slightly larger, and it does so because the
scan sweep 2 asked for was finally run.

**And one correction that runs against a prior sweep rather than against a vendor.** Sweep 2 resolved
four Sora `free_plan_*` values via a parent step it flagged as soft. Three documents now contradict
each other on that parent, and the Sora 2-era one — the era the record actually codes — says the
opposite of the one sweep 2 relied on. That correction is worth more than the retrievals around it,
in the same way sweep 2's downward correction was.

---

## Caveats against my own findings

**First, the withdrawal problem is unresolved and it governs eight of the thirteen.** Every Sora
document was delisted before the window opened. "The vendor published this" and "a coder could have
read this during the window" are different claims and only the first is established. I have marked six
values conditional on it rather than picking a side, because the choice is a study-design question
about what `unknown` means in a cross-sectional frame, not a retrieval question. If the orchestrator
resolves it one way the six become `vendor_silence`; the other way they stay `access_failure`. **Do
not let this file's "addresses" column be read as a decision on that.**

**Second, only two of the thirteen carry real temporal warrants, and they run opposite ways.** Hailuo's
captures are inside the window and confirm unreachability; Runway's capture is eleven months before it
and confirms retrievability. Everything else is a 2026-08-17 reading with, at best, a continuity
argument.

**Third, I have established that two of my retrievals can never be window-dated.** Canva serves the
archive an unsupported-client shell and has no Common Crawl record and no on-page date stamp; Adobe
assembles its FAQ from fragments the archive does not store. Those are not open threads, they are
closed doors, and I would rather record them as such than leave them looking re-runnable.

**Fourth, my Sora enumeration is broader than sweep 1's but still not exhaustive.** I read 10 of the
13 collection articles' worth of relevant surface plus the ChatGPT credits article; I did not read
"Sora - Data Controls FAQ", "Sora - Supported Countries", "Blocking and reporting", "Sending Messages",
"Data Controls and Privacy" or "Generating content with characters", judging them off-construct. If
the Release Notes thread teaches anything it is that **an off-construct judgment is exactly how sweep 1
missed the credits article**, so treat my enumeration as better rather than complete.

**Fifth, `usage_cap_quantified` is genuinely mixed and I may be over-reading it as "addresses".** The
vendor documents the cap mechanism and quantifies each duration's cost against the cap, and then
writes the cap itself as "X". A reader could fairly say the construct is *not* addressed. I have
flagged it conditional for that reason as well as for the withdrawal question.

**Sixth, two capture fetches failed and were not retried to exhaustion** — `20260724041341` of the
credits article (14 tries) and `20260815135722` of "Generating videos on Sora" (14 tries). Neither is
load-bearing: the credits article has a closer window-era capture that I did read, and the
Generating-videos capture post-dates the shutdown and would show a 404 shell. But they are recorded
rather than hidden, per this file's lineage.

**Seventh, and against my own infrastructure advice: my "no record" findings on Common Crawl rest on
404s from a service that returned 504 to adjacent requests in the same minute.** The three 404s are
consistent with D-057's independent finding, which is why I report them, but a single 404 from a
flapping index is weaker evidence than it looks.

## Threads owed after this sweep

Both are new, and neither blocks a count above.

1. **The published-then-withdrawn category.** Six values hang on it. This needs a ruling from the
   orchestrator or an adjudicator, not more retrieval — the documents are already in hand and quoted
   above.
2. **Sweep 2's `free_plan_*` resolution for Sora.** Three recovered documents contradict each other on
   whether ChatGPT Free had Sora access, and the Sora 2-era one says it did. Sweep 2's four "addresses
   via parent" findings rest on the document that says it did not. This should go back to whoever owns
   that record.
