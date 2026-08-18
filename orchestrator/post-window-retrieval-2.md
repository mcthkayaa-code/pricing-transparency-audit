# Post-window supplementary retrieval — second sweep

**Run date: 2026-08-17. All readings in this file are post-window.**

The collection window closed **2026-08-13** and the frame is frozen. Nothing in this file has been
merged into any record, and **no coded value has been altered**. Every record referenced below is
untouched. This is a supplementary check that stands *beside* the frozen dataset.

## Why this sweep exists

The first sweep (`post-window-retrieval.md`) took the 21 values the unknown-attribution pass had
marked `access_failure` and found **20 of 21 retrievable**. The orchestrator acted on its
reclassification list: the ten values it named are now `vendor_silence` in
`orchestrator/unknown-attribution.csv`.

Separately, an audit of the machine-set attributions moved **25 further values into
`access_failure`**, and that audit finished after the first sweep had already run. The study was
therefore asserting a retrieval limitation on 25 values **nobody had tried to retrieve** — the same
defect the first sweep was commissioned to correct, reintroduced by fixing something else. This
sweep covers those 25.

## Work-list verification

`orchestrator/unknown-attribution.csv` currently carries **36** rows with `kind == access_failure`,
all `decided_by = hand`. The assigned list of 25 was checked row-by-row against it:

- **The list has not drifted.** All 25 assigned pass/product/variable triples are present in the CSV
  as `access_failure`.
- The other **11** `access_failure` rows are all first-sweep values (canva ×2, hailuo-ai ×1,
  openai-sora ×3, runway ×1, wix `output_ownership_statement`, jobscan ×3). They are out of scope here.
- The **10** values the first sweep recommended reclassifying were confirmed to now read
  `vendor_silence` (lovo-ai ×1, picsart `cost_per_output_computable`, openai-sora ×7,
  wix `commercial_use_lowest_tier`). The chain of custody is intact.

Note one easily-missed distinction: the first sweep handled **`wix/commercial_use_lowest_tier`**;
this sweep handles **`wix/unquantified_limit_clause`**. Different variables on the same document.

## Method

Three independent routes minimum before declaring anything unreachable: the live URL, an archive
capture from any date, and at least one alternative (sitemap, differently-cased or trailing-slash
URL, locale variant, embedded data layer, the vendor's own content endpoint, or same-origin fetch
from a rendered page). Protocol limits observed throughout: **no account created, no login, no terms
accepted, no trial started, no CAPTCHA solved and no bot wall evaded.** Ordinary rendered browser
page loads were used, which deviation D-005 already permits.

## Infrastructure note that shaped this run, and constrains it

**Archive.org's replay path was down for the entire run.** Every request to
`web.archive.org/web/<timestamp>[id_]/<url>` returned HTTP 503 with the 11,832-byte "Internet
Archive: Temporarily Offline" page — on approximately 100 attempts across three retry loops of 40–45
tries at 15-second intervals, plus later spot checks. The **CDX index** was also still 503, now a
second consecutive day. The **Memento timemap** endpoint stayed up and was used for enumeration.

This is worse than the first sweep met, which got intermittent replay successes. The practical
consequence is stated plainly: **no archive capture could be read today.** Three threads that would
otherwise have been run were blocked by it and are recorded as owed:

1. Independent re-verification of the Sora Billing FAQ captures the first sweep recovered.
2. The window-era Adobe Firefly capture (`20260806112138`), which the record's own `sources` list
   names and which would have removed this file's temporal caveat on that record entirely.
3. Arm 2 (US-crawled capture) for canva, gptzero and phrasly.

`timetravel.mementoweb.org` was tried as a substitute aggregator and did not connect.

---

## Record: `pass1/adobe-firefly` — 1 value

### `trial_length_days`

**Document the coder could not reach:** the FAQ answer content on
`https://www.adobe.com/products/firefly/plans.html`. The record's `register_events` carries a
`data_quality_note`: the FAQ "rendered only as collapsed question text; the answer content did not
expand through repeated browser-automation click attempts on the accordion control."

**Routes tried today**

| Route | Outcome |
|---|---|
| `curl`, desktop UA, HTTP/2 | **Connection failure** (exit 92) — no response body |
| `curl --http1.1` | **Timeout** (exit 28) — adobe.com's apex answers `HEAD` with 200, but this path did not complete to a static fetcher |
| Ordinary rendered browser load (D-005) | **HTTP 200, full page**, 256,184 chars of DOM |
| Rendered DOM, `innerText` of the FAQ region | **Reproduces the record's failure** — only the eleven question titles are present |
| Rendered DOM, **`textContent` of each `aria-controls` target** | **All eleven FAQ answers recovered in full**, 5,626 chars |
| Archive capture `20260806112138` (the record's own archived source, window-era) | **Blocked** — archive.org replay 503 all run |

**Root cause, and it is a new under-retrieval mechanism.** The accordion triggers carry
`aria-controls="accordion-1-content-N"`. Those content elements **exist in the DOM at load, populated,
but hidden**. `innerText` returns the empty string for a hidden element; `textContent` returns the
real text. A coder who clicks to expand and then reads rendered text gets nothing; a coder who reads
`textContent` gets the whole FAQ without interacting with the page at all.

**Result: RETRIEVED, and it does NOT address the construct.**

The recovered FAQ contains **zero occurrences of "trial"**, zero occurrences of "day", and zero
occurrences of any `N-day` pattern. Across the *entire* rendered page, "trial" appears six times and
every one is the "Free trial" call-to-action label on a plan card; the regex `\b\d{1,2}[- ]days?\b`
matches **nowhere on the page**.

The most on-point answer, "How much does Adobe Firefly cost?", is recovered in full and says nothing
about a trial:

> "Adobe Firefly offers a free plan with limited daily generations, plus four paid tiers: Adobe
> Firefly Standard: $9.99/month — 2,000 generative credits · Adobe Firefly Pro: $19.99/month — 4,000
> generative credits · Adobe Firefly Pro Plus: $49.99/month — 10,000 generative credits · Adobe
> Firefly Premium: $199.99/month — 50,000 generative credits plus unlimited Adobe Firefly Video Model
> access. All paid plans include unlimited standard image and vector generations. Generative credits
> are used for premium features such as video, audio, and partner model outputs."

Source: `https://www.adobe.com/products/firefly/plans.html`, read 2026-08-17.

**Temporal warrant, partial.** The recovered FAQ states Standard at **$9.99/month with 2,000
generative credits** and Pro at **$19.99/month with 4,000** — matching this record's coded
`headline_price_usd = 9.99` and its coded 2,000-credit entry-tier allowance exactly, and the live
cards still read "US$9.99/mo" and "US$19.99/mo". That is consistency, not proof: the FAQ carries no
last-updated stamp, and today's page also runs a promotion ("Ends Aug 26") on the Pro Plus and
Premium cards that post-dates the coding date. I could not confirm the FAQ text against the record's
own window-era capture because archive.org was down.

**The sharp version, and it is not a criticism of the coder's judgment.** This same record solved
this exact problem on a *different* Adobe page — its `sources` note for the Subscription and
Cancellation Terms reads "Read via an archived raw-HTML snapshot after the in-page accordion could
not be expanded through the browser automation." The technique was in hand and was not carried across
to the plans-page FAQ. The record was right not to code from an unread document. The gap was purely
retrieval.

**Collateral, not coded and not mine to code.** The recovered FAQ also answers, in terms, three other
variables on this record: "Is there a free version" (`free_plan_exists`), "generative credits ... reset
each billing cycle and **do not roll over**" (`credit_rollover_policy`, which the record already coded
`expires_at_period_end` from the helpx FAQ — now corroborated on the pricing page itself), and "Are
Adobe Firefly outputs safe for commercial use?" — the very question the record had to substitute
Adobe Express's pricing-page FAQ for. Its answer is now readable at source:

> "Outputs from Adobe Firefly AI models are safe for commercial use. Adobe Firefly models are trained
> on licensed content and public domain content where copyright has expired... Eligible enterprise
> customers can also receive IP indemnification for select Adobe Firefly outputs."

---

## The currency-block cluster: `canva`, `gptzero`, `phrasly`, `picsart` — 7 values

Four records, seven values, one shared shape. Each was coded `unknown` under the D-007 currency
re-check because no USD figure could be read, and the audit charged each to `access_failure` on the
reasoning that the vendor plainly publishes *a* price. They do not all resolve the same way, and the
differences are the finding.

### `pass1/picsart` — `headline_price_usd`, `first_charge_amount_usd`

**Document the coder could not reach:** a USD-denominated reading of `https://picsart.com/pricing/`.

**Routes tried today**

| Route | Outcome |
|---|---|
| Live pricing page, `curl`, desktop UA, `Accept-Language: en-US` | **HTTP 200, 1,215,328 bytes with real price content** |
| The page's own embedded price table | **Fully enumerated — 348 price rows across 10 products** |
| Archive captures | Blocked (replay 503) |

**Result: RETRIEVED, and it does NOT address the construct.**

This independently reproduces the first sweep's finding on the sibling variable
`cost_per_output_computable`, from a fresh fetch and a fresh parse. The pricing page embeds a
country-keyed, multi-currency table (`{"currencySymbol","currency","country_code","value","initial_value"}`)
carrying every locale's figure. For the **Pro entry tier there is no US row and no USD row at all**,
while every Ultra tier in the same array carries one:

| product_id | rows | TR | US / USD |
|---|---|---|---|
| `pro_web_yearly` (entry tier) | 33 | TRY 999 | **ABSENT** |
| `pro_web_monthly` (entry tier) | 33 | TRY 149 | **ABSENT** |
| `power_web_monthly_1500` | 34 | TRY 2,210 | USD 47 |
| `power_web_yearly_1500` | 34 | TRY 21,165 | USD 450 |
| `power_web_monthly_2500` / `power_web_yearly_2500` | 34 | TRY 3,391 / 33,864 | USD 75 / 720 |
| `power_web_monthly_5000` / `power_web_yearly_5000` | 34 | TRY 6,556 / 62,850 | USD 145 / 1,390 |
| `power_web_monthly_10000` / `power_web_yearly_10000` | 34 | TRY 11,300 / 108,510 | USD 250 / 2,400 |

Pro's 33 country codes: AT AU BE BR CA CN CZ DE EE ES FI FR GB GR HU IE IN IT JP LT LU LV MT MX MY NL
PL PT RO SE SI SK TR. Currencies: AUD BRL CAD CNY EUR GBP INR JPY MXN MYR PLN TRY. No `US`, no `USD`,
no default row.

**Temporal warrant, strong.** `pro_web_yearly` = **TRY 999**; 999 ÷ 12 = **TRY 83.25/mo**, exactly the
figure the record coded on 2026-08-10, and the same figure the first sweep read on 2026-08-17. The
price is unchanged, so this is not an artefact of reading a different price.

Both values therefore stand as `unknown`, but the reason is a **documented gap in the vendor's own
price table for that tier** — the same conclusion the study already accepted for
`picsart/cost_per_output_computable`, which is now `vendor_silence`. These two should follow it.

### `pass1/canva` — `headline_price_usd`, `first_charge_amount_usd`

**Document the coder could not reach:** a USD-denominated reading of `https://www.canva.com/pricing/`.
Entry tier is Pro.

**Routes tried today**

| Route | Outcome |
|---|---|
| Live pricing page, `curl`, desktop UA, `Accept-Language: en-US` | **HTTP 403**, 755,004-byte Cloudflare challenge body — reproduces the record |
| Ordinary rendered browser load (D-005) | **HTTP 200**, 888,147 chars. TRY only |
| Search of the rendered payload for a multi-currency table | **None exists.** `USD` appears **0** times in the entire document; the only currency code present is `TRY` |
| **`es-US` locale path** `https://www.canva.com/es_us/precios/` — the one United-States-country locale among the page's 105 hreflang alternates | **HTTP 200, Spanish page, identical TRY figures** (₺0 / ₺1,920 / ₺3,400), `USD` count 0 |
| Seven help/product/newsroom pages via `curl` | **All HTTP 403** |
| The same seven fetched **same-origin from the rendered canva.com page** | **All HTTP 200.** Only one USD figure anywhere: `/help/ai-pass/` → "USD $100". No plan price in USD, and no plan price in TRY either |
| Archive captures (625 mementos enumerated via timemap) | Blocked (replay 503) |

**Result: RETRIEVED, and it does NOT address the construct — but "vendor silence" is the wrong name for it.**

The document was read in full, hydrated, and contains no USD figure. But Canva is not silent about
price: it publishes ₺1,920/yr for Pro to this reader, and it publishes "USD $100" for the AI Pass
add-on in a help article, so it uses USD in its documentation where it chooses to. What it does not do
is expose a USD *plan* price to a reader outside the United States. **Canva's currency selection is
IP-bound and no locale path overrides it** — confirmed here on `es_us`, and independently confirmed by
the record itself, which logged the same result for `/en_us/pricing/`.

`first_charge_amount_usd` cascades from `headline_price_usd` with no independent evidence.

### `pass1/gptzero` — `headline_price_usd`

**Document the coder could not reach:** a resolved USD figure on `https://gptzero.me/pricing`. Entry
tier is Premium.

**Routes tried today**

| Route | Outcome |
|---|---|
| Live page, `curl`, desktop UA, `Accept-Language: en-US` | HTTP 200, 232,389 bytes — **pre-hydration shell**, exactly as the record describes. `USD` 0, `currency` 0, `TRY` 0. The `$` hits are a `$0/mo billed annually` placeholder, the `$288/year` educator-program figure, and React RSC reference tokens (`$1`, `$7`) — **the record's reading of this page is correct in every particular** |
| Ordinary rendered browser load (D-005) | **HTTP 200, fully hydrated.** Premium reads **"TRY 549 / month, billed annually"**; Professional TRY 1,049. No USD anywhere |
| Network trace of a full reload | **No price API call exists.** Only static chunks and RSC requests — the figure is server-rendered per request, geo-selected |
| Same-origin probes: `/pricing` with `Accept-Language: en-US` + `CF-IPCountry: US`, `?country=US&currency=USD`, `/us/pricing`, `/en-US/pricing` | All identical or 404. No parameter or header changes the currency |
| Vendor API host `api.gptzero.me` — five plan/pricing endpoint guesses, plus `/api/plans`, `/api/pricing` | All 404 |
| JS bundle audit (31 chunks, 2.3 MB) | Confirms the mechanism: plans carry `priceData.unit_amount` + `priceData.currency`, formatted by `formatLocalizedPrice(amount, currency)`, with a server-supplied currency |
| Archive captures | **66 mementos enumerated** — but only under the *trailing-slash* URL (see below). Replay 503, so none readable |

**A retrieval trap worth recording.** The Memento timemap returns **0 mementos** for
`https://gptzero.me/pricing` and **66 mementos** for `https://gptzero.me/pricing/`. A single trailing
slash is the difference between "this URL was never archived" and 66 captures. Anyone re-running an
Arm 2 check should query both forms.

**Result: RETRIEVED, and it does NOT address the construct — same shape as Canva.**

**Temporal warrant, strong.** The rendered page today shows **TRY 549/month billed annually**, which
is the exact figure the record coded and re-confirmed on 2026-08-10. Unchanged since the window.

Note also that an archive capture *structurally cannot* settle this variable for GPTZero: the price is
injected into a server-rendered response chosen by IP, and archive.org's crawler stores the response
it received, which for this page is the pre-hydration shell. Arm 2 was never going to work here, on
any capture, which is worth saying rather than leaving as an open lead.

### `pass1/phrasly` — `headline_price_usd`, `first_charge_amount_usd`

**Document the coder could not reach:** a USD figure on `https://phrasly.ai/pricing`. Entry tier is
Unlimited.

**Routes tried today**

| Route | Outcome |
|---|---|
| Live page, `curl`, desktop UA | **HTTP 403**, 5,656 bytes — Cloudflare. Reproduces the record |
| Ordinary rendered browser load (D-005) | **HTTP 200**, 305,848 chars |
| **The page's own embedded Paddle price catalogue** | **Recovered in full — USD-denominated, including the entry tier** |
| JSON-LD structured data on the same page | `"lowPrice":"0.00","highPrice":"19.99","priceCurrency":"USD"` |
| Archive captures (19 mementos enumerated) | Blocked (replay 503) |

**Result: RETRIEVED, and it ADDRESSES the construct.**

Phrasly's pricing page carries its Paddle catalogue in its own payload, with USD as the base currency
and per-market overrides. For `productType: "UNLIMITED"` — this record's entry tier — the catalogue
publishes:

| product | billing cycle | base `unitPrice` | USD overrides also present |
|---|---|---|---|
| Unlimited, Monthly | month × 1 | **2000 USD** ($20.00) | 1299 ($12.99), 1099 ($10.99) |
| Unlimited, Yearly | year × 1 | **13188 USD** ($131.88) | 8599, 8499, 7299 |
| Unlimited, Monthly (Trial) | month × 1 | 3999 USD ($39.99) | 2599, 2199 |
| Unlimited, Yearly (Trial) | year × 1 | 23988 USD ($239.88) | 15499, 15599, 13199 |
| 3 Day Access | — | 200 USD ($2.00) | — |

Non-USD overrides in the same catalogue cover BRL, ZAR and INR. **There is no TRY entry** — so the
TRY figure the coder read is Paddle's runtime conversion of a USD base price, not a published TRY
price.

**Temporal warrant, strong, and it closes the arithmetic.** The rendered page today shows Unlimited at
**"TRY 1,197.03 → TRY 526.43 / month, per month, billed annually"**, against the record's coded
"TRY 524.43 active / TRY 1,192.49 struck-through / per month, billed annually" — a 0.4% difference,
consistent with FX drift over four days. And 526.43 × 12 = TRY 6,317/yr; 6,317 ÷ 131.88 = **47.9
TRY/USD**, the same implied rate as the record's own 524.43 × 12 = 6,293 ÷ 131.88 = **47.7**. The
catalogue's yearly base of **$131.88** divides to **$10.99/month**, which is itself present in the
catalogue as an override. The record's coded TRY figure and this USD figure are the same price.

**Caveat I want on the record, because this is the one value where retrieval may bear on the coded
value.** The codebook defines `headline_price_usd` as "the largest, most prominent price figure the
vendor publishes for the entry paid tier on its pricing page", read "in the page's default state as it
loads". A catalogue object in the payload is **not a displayed figure**, and the catalogue carries a
base price *plus three USD overrides* for the annual product, so it does not by itself settle which
USD figure a US reader is shown. What it does settle is that the record's premise — "no document
anywhere stating a USD number for the Unlimited tier" — is false. Whether that supports recoding, or
only reclassification, is an adjudication question and I have not taken it.

`first_charge_amount_usd` follows: if the default state is annual, the catalogue's annual base of
**$131.88** is the first-charge figure, subject to the same caveat.

---

## Record: `pass1/wix` — 1 value

### `unquantified_limit_clause`

**Document the coder could not reach:** `https://www.wix.com/about/terms-of-use`, Sections 2–19. The
record is explicit and correct: "the Terms of Use body did not render beyond Section 1 ... so it could
not be read to the end — coding `absent` would misrepresent a document that was not actually
readable." The codebook agrees: rule 1 requires reading the terms in full, and "`absent` is a claim
about a document you have read to the end."

**Routes tried today**

| Route | Outcome |
|---|---|
| `https://www.wix.com/about/terms-of-use`, `curl`, `Accept-Language: en-US` | HTTP 200, 753,091 bytes — and only **2** substantive `<h2>`: "1. Introduction" and the Israel-residents addendum. 11,060 chars of body text. **Reproduces the record exactly** |
| `tr.wix.com/about/terms-of-use`, `curl` | **HTTP 200, 20 `<h2>`, 110,302 chars — Sections 1–19 present** |
| `de.wix.com/about/terms-of-use`, `curl` | **HTTP 200, 20 `<h2>`, 117,317 chars — independent second locale** |

This confirms the first sweep's diagnosis on the sibling variables: a **locale-specific content defect
on the vendor's side**, English uniquely broken, the body retrievable in other languages the whole
time.

**Result: RETRIEVED, and it ADDRESSES the construct.**

Both locale bodies were read to the end and scanned for unquantified-limit language. The decisive
clause sits in Section 2's prohibited-conduct list. Turkish (`tr.wix.com/about/terms-of-use`,
2026-08-17):

> "...Wix Hizmetleri üzerine **makul olmayan, aşırı veya orantısız büyüklükte bir yük** getiren, veya
> Wix Hizmetlerinin veya bunları barındıran veya kullanıma sunan sunucuların veya ağların işleyişine
> başka şekillerde müdahale eden veya işleyişi kesintiye uğratan..."

German (`de.wix.com/about/terms-of-use`, 2026-08-17), independent second locale, same clause:

> "...dafür zu sorgen, dass die Infrastruktur der Dienste von Wix ... einer **unzumutbaren und
> unverhältnismäßigen Last** ausgesetzt sind, oder dafür zu sorgen, dass der Betrieb der Dienste von
> Wix, der Server oder der Netzwerke, die sie hosten oder zur Verfügung stellen, in anderer Weise
> gestört oder unterbrochen werden..."

In substance: conduct that places an **unreasonable, excessive or disproportionate load** on Wix's
services or infrastructure is prohibited. No number defines any of the three standards.

Full-text counts, Turkish body: `makul` ×5, `aşırı` ×1, `orantısız` ×1, `takdir` (discretion) ×23,
`kısıtla` ×7, `sınırla` ×8. German: `Ermessen` ×19, `unverhältnis` ×1, `beschränk` ×13. The three
`makul`/`aşırı`/`orantısız` hits that matter all sit in the one clause quoted above; the other `makul`
occurrences are account-ownership determination, marketing-licence scope, DMCA discretion and a
force-majeure "reasonable control" clause, none of which is a usage limit.

**Two caveats, both real.**

1. **This is a coding judgment I have not taken.** Codebook rule 3 excludes "a prohibition on illegal
   or abusive content ... This variable covers volume and intensity of use, not conduct." The clause
   is *about* volume and intensity of use — an excessive load on infrastructure — but it *sits in* a
   prohibited-conduct list beside vulnerability scanning and service interference. The `present` value
   list explicitly names "excessive use" and "abuse thresholds", which points the other way. An
   adjudicator should settle it. What the retrieval establishes is that the document is readable and
   the clause exists; the record could not establish either.
2. **The clauses quoted are the vendor's Turkish and German renderings, not its English text, and the
   English text is the one that did not render.** For a contractual variable this is a real
   evidentiary difference. I would put this to adjudication as "document retrieved in two non-English
   locales; English rendering defective; an unquantified-load clause is present in the retrieved
   text" rather than as a settled `present`.

**Collateral, offered because it bears on two other variables on this record and I did not code
either.** Section 6.2 of the same body carries what reads as an advance-renewal-notice commitment for
annual subscriptions — "...yenilenmesinden önce, yenileme tarihinden en az otuz [gün]" (at least
thirty days before the renewal date) — which is `renewal_notice_commitment` territory. Section 6.6
("Ücretsiz Deneme") states that trial duration and terms are set by Wix at its sole discretion, which
bears on the trial variables. Both were unreadable in English for the same reason and both are now
readable.

---

## Record: `pass2/jobscan` — 2 values

**Document the coder could not reach:** `https://www.jobscan.co/terms-of-service`, in English. The
record documents four independent failed attempts, all rendering Turkish body text.

**Routes tried today**

| Route | Outcome |
|---|---|
| `curl`, desktop UA | **HTTP 403** |
| Termly content endpoint with English `Accept-Language` (the route the first sweep found) | **HTTP 200, 196,159 bytes, ENGLISH — complete document**, 49,138 chars of plaintext |

The working route is unchanged:
`GET https://app.termly.io/api/v1/consumer/policies/186bf27c-eb55-4548-a82c-ea2013d118a0/content`
with `Accept-Language: en-US,en;q=0.9`.

**One new fact that strengthens the first sweep's root-cause finding.** The endpoint's own response
carries `"locale":"en"` and **`"created_locales":["en"]`** — English is the *only* locale ever
authored for this policy. The Turkish the coder met four times was never a vendor translation; it was
Termly's client-side viewer localising to the request locale. There is no governing-language ambiguity
here at all.

**Temporal warrant, strongest in either sweep.** The document self-dates **"Last updated March 16,
2026"**, which precedes both the window and this record's 2026-08-15 coding date. The English text
read today is the version that was on the site when the coder was blocked.

### `credit_rollover_policy`

**Result: RETRIEVED, and it does NOT address the construct.**

The codebook directs reading "the pricing page, the documentation, and the terms". The terms are now
read in full. Counts across the 49,138-character body: `unused` **0**, `roll over` **0**, `rollover`
**0**, `carry forward` **0**, `expire` **0**, and `credit` **1** — that single occurrence being
"...or to payments or the granting of credits by any means other than electronic means", in
Section 25 on electronic signatures, which is not a product credit at all.

The first-ranked document is silent on credit rollover. The record's coded `unknown` stands; the
reason is vendor silence, and the adjudicated record for this product independently reached the same
conclusion ("Both passes agree; genuine silence, not an access limitation").

### `renewal_notice_commitment`

**Result: RETRIEVED, and it does NOT address the construct — with the nearest clauses recovered so an
adjudicator can see exactly what silence looks like here.**

Section 6 (SUBSCRIPTIONS) is read in full. It contains four sub-clauses, and the two that bear on this
variable run as follows.

**Billing and Renewal:**

> "Your subscription will continue and automatically renew unless canceled. You consent to our
> charging your payment method on a recurring basis **without requiring your prior approval for each
> recurring charge**, until such time as you cancel the applicable order."

**Fee Changes:**

> "We may, from time to time, make changes to the subscription fee and will communicate any price
> changes to you in accordance with applicable law."

So the document does commit to communicating **price changes**, deferred to applicable law with no
stated period — and it affirmatively disclaims any need for prior approval of a **routine renewal
charge**. Under the codebook, `advance_notice_stated` "requires a stated commitment, ideally with a
period", and nothing here states one for the renewal charge itself.

The audit's basis for charging this to `access_failure` was that the adjudicated row "found the
answer-relevant clause there (ToS Section 6 'Fee Changes'), proving the unread document was material."
The document was material, and it has now been read: its materiality is that it establishes the
silence rather than filling it.

**A note for the adjudicator, not a recoding.** The codebook's value list distinguishes
`no_notice_stated` from `unknown`, and on a completed full read of the first-ranked document the
determinate value looks reachable. The adjudicated record codes `unknown`. That is a coding judgment
and I have not taken it; I record only that the read is now complete.

**Collateral, not mine to code.** The same Section 6 states: "We offer a **7-day free trial** to new
users who register with the Services. The account will be charged according to the user's chosen
subscription at the end of the free trial." That is `trial_length_days` and `trial_auto_converts` for
this product, in the document that could not be read.

---

## Record: `pass1/openai-sora` — 14 values

Fourteen of the 25 are one discontinued product, and the first sweep already did the decisive work.
Per this sweep's brief, the task here was to determine which of the fourteen the existing evidence
base reaches, not to re-run an enumeration that has been done.

**What the first sweep established, and what I could and could not re-verify today**

| Established by the first sweep | Re-verified today? |
|---|---|
| The Billing FAQ is 404 live, both slug variants, and the parent collection is 404 | **Yes** — same-origin fetch from a rendered help.openai.com page: `10245774-sora-billing-credits-faq` → **404**, `10245774-sora-billing-faq` → **404**, `collections/11106745-sora` → **404** |
| 31 archive captures exist for the Billing FAQ | **Yes** — timemap returns **31 mementos**, matching exactly |
| Two of those captures carry the complete article (2025-11-24, 2026-02-01) | **No** — archive.org replay 503 on every attempt all run |
| The 2026-03-31 collection capture enumerates 13 Sora articles, of which "Sora - Billing FAQ" is the only billing document | **No** — same blocker |
| Keyword scan of the recovered article: `$`=0, `credit`=0, `trial`=0, `annual`=0, `yearly`=0, `refund`=0, `watermark`=1 | **No** — same blocker |
| The discontinuation FAQ is live and states credits carry to Codex | **Yes** — read in full today (below) |

**This is the central caveat on this record's fourteen results: they rest on the first sweep's
retrieval, which I could not independently re-verify today.** The two facts I could check
independently — the 404 status and the capture count of 31 — both matched the first sweep precisely,
which is some corroboration of its account, but it is not the same as re-reading the article.

**The scope limit that constrains everything below**, quoted by the first sweep from both captures:

> "Please note that the following experience only applies to **Sora 1 on Web**. It does not apply to
> the Sora app or Sora 2 on web."

The record codes Sora as it stood near shutdown, i.e. the Sora 2 / Sora app era. So every finding
below is a finding about the only billing document OpenAI ever published for Sora, self-scoped to Sora
1 on Web. The first sweep already applied this caveat to `credit_unit_defined`; it applies with equal
force to the free-plan and watermark values here.

**One further document, read live today.** `https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation`
(stamped "Updated: 18 days ago", i.e. ~2026-07-30, which **predates the window close**) is reachable
by rendered browser and was read in full. It is short and it is entirely about shutdown mechanics:
discontinuation dates, data export, data deletion, and one refund pointer —

> "What if I need a refund? For refund questions, please see How do I request a refund for my ChatGPT
> subscription? Note that any purchased ChatGPT/Sora credits can still be used for Codex, if you so
> choose."

It states no price, no free tier, no trial, no credit definition, no rate, and no rollover or expiry
policy. It confirms credits existed in the Sora 2 era, which is what the record already coded
`credit_system_present = yes` from, and it adds nothing further.

### Value-by-value

**`headline_price_usd` — RETRIEVED, construct absent.** The Billing FAQ contains zero `$`. It is the
only billing document that ever existed in the collection, and Sora access was a feature of a ChatGPT
subscription rather than a separately-priced product. The record's sibling `first_charge_amount_usd`
was reclassified to `vendor_silence` on exactly this evidence; this value rests on the same sentence
in the record and should follow it.

**`headline_billing_basis` — RETRIEVED, addresses.** The article states the cadence directly:

> "What is my billing date? Your billing date is the day of the month on which you first initiated
> your plan... **Subscriptions for ChatGPT plans are charged on a calendar monthly basis**, from the
> subscription start date."

*Weak in one respect, and I flag it rather than argue it:* the record's own reasoning is "no headline
figure was located ... so no billing basis could be read", and this variable is defined as "what the
headline figure represents". A monthly-only cadence is documented; whether that answers a variable
about a figure that does not exist is a coding judgment.

**`annual_condition_disclosure` — RETRIEVED, construct absent.** Zero occurrences of "annual" or
"yearly" in the article, against a documented monthly-only cadence. The record's own basis is that
"the last reachable pre-shutdown ChatGPT pricing capture does not mention Sora at all" — the Sora
billing document has now been read and it states no annual condition either.

**`free_plan_exists` — RETRIEVED, addresses.** This is the strongest of the fourteen. The article
states, in terms:

> "Currently ChatGPT Free, Enterprise, and Edu accounts are **not eligible for Sora access**."

and, on upgrades, "Only ChatGPT Plus users can upgrade their plan." The record coded `unknown` because
"No official document states either that a no-cost Sora plan existed or that none did". A document
states it. Scope caveat: Sora 1 on Web.

**`free_plan_cap_documented` — RETRIEVED, addresses via the parent.**
**`free_plan_cap_value` — RETRIEVED, addresses via the parent.**
**`free_plan_watermark` — RETRIEVED, addresses via the parent.**
**`free_plan_duration` — RETRIEVED, addresses via the parent.**

All four are cascades the record itself wrote as cascades ("Follows `free_plan_exists = unknown`").
Each carries `not_applicable` for the no-free-plan case in the codebook, so the documented
ineligibility of ChatGPT Free resolves all four. **These are the softest of my "addresses" findings**
and I mark them so: the document does not describe free-plan caps, watermarks or duration — it
establishes that the free tier had no access, from which the four values follow *only if* an
adjudicator accepts that as "no free plan" for Sora, and *only* within the Sora-1-on-Web scope. An
adjudicator who declines either step should move all four to "construct absent".

**`trial_card_required` — RETRIEVED, construct absent.** Zero occurrences of "trial" in the article.
Its three siblings — `trial_exists`, `trial_length_days`, `trial_auto_converts` — were reclassified to
`vendor_silence` on precisely this scan. This is the fourth trial variable and was left behind.

**`credit_rate_location` — RETRIEVED, construct absent.** The article contains the string "credit"
**zero** times, and it is the only billing document that ever existed. Note the codebook's own
distinction for this variable: `absent` means "no rate is published", `unknown` means the documents
could not be located. The documents have been located. Its siblings `credit_unit_defined` and
`credit_to_output_rate_published` are already `vendor_silence`.

**`credit_rollover_policy` — RETRIEVED, construct absent.** Same zero "credit" count in the Billing
FAQ. Additionally checked today: the discontinuation FAQ, the only other Sora document that mentions
credits, states a *migration* ("can still be used for Codex"), not a period-end rollover or expiry
policy. Nothing published states what happened to unused credits at the end of a billing period.

**`failed_generation_charge_policy` — RETRIEVED, construct absent (WEAK — see the flag).** This is
**the one value of the fourteen that the existing evidence does not directly reach**, and I am
flagging it as the brief asks. The first sweep's keyword scan of the recovered article covered `$`,
`credit`, `trial`, `annual`, `yearly`, `refund`, `monthly`, `concurrent`, `resolution`, `unlimited`
and `watermark` — it **did not scan for `fail` or `error`**, which are the decisive terms here. I
could not run that scan today because archive.org's replay path was down.

What supports "absent" is structural rather than direct: the article documents *unmetered* access
("ChatGPT Pro and Plus plans offer unlimited access to Sora") and contains no credit currency at all
for Sora 1 on Web, so there is no allowance a failed generation could consume; and the collection
enumeration establishes no other billing document existed. That is a real argument, but it is
inference from absence, not a completed scan.

**Recommendation: treat this one as conditional.** If the orchestrator wants the scan before moving
it, it should stay in `access_failure` until archive.org is healthy and the 2026-02-01 capture can be
re-read for `/fail|error|unsuccessful|deduct/i`. That is a ten-minute job once replay returns.

**`commercial_use_lowest_tier` — RETRIEVED, construct absent.** The record's decisive clause is "no
Sora-specific documentation was reachable to check further"; the Sora documentation has now been
reached. The article's only commercial-adjacent text is its restatement of the Terms of Use under
"Understanding Unlimited Usage" — prohibiting "Reselling access or using ChatGPT to power third-party
services" — which restricts resale of *access*, not commercial use of *outputs*, and carries no tier
gate. No grant of output commercial-use rights appears in it. Combined with the record's own full-text
keyword search of the Terms of Use ('commercial', 'business purpose', 'monetiz', 'resell'), the
document classes are now read and the construct is absent.

**`watermark_removal_tier` — RETRIEVED, addresses.** The article's tier table names the tier directly.
For ChatGPT Pro:

> "**ChatGPT Pro** — Unlimited images and video · Faster generations · Up to 1080p resolution and 20s
> duration videos · Up to 5 concurrent generations · **Download videos without a watermark**"

and the Plus/Business row above it carries no such line. The record's basis was "no Sora product
documentation was reachable to check further" — it was reachable, and it answers this variable
explicitly. Scope caveat: Sora 1 on Web. This value's sibling `free_plan_watermark` was resolved above
by a different route.

---

## Summary

| Outcome | Count |
|---|---|
| **RETRIEVED, and it addresses the construct** — the vendor documented the thing and our instrument missed it | **10** |
| **RETRIEVED, and it does NOT address the construct** — the original `unknown` was not a retrieval failure | **15** |
| **STILL UNREACHABLE** after three or more independent routes | **0** |
| **Total** | **25** |

One of the 15 (`openai-sora/failed_generation_charge_policy`) is **conditional** on a keyword scan
that could not be run today. If the orchestrator declines the inference, the counts become
addresses 10 / absent 14 / unreachable 1.

### By record

| Record | Value | Outcome |
|---|---|---|
| pass1/adobe-firefly | `trial_length_days` | retrieved — silent |
| pass1/canva | `headline_price_usd` | retrieved — silent (geo-bound currency) |
| pass1/canva | `first_charge_amount_usd` | retrieved — silent (cascade) |
| pass1/gptzero | `headline_price_usd` | retrieved — silent (geo-bound currency) |
| pass1/openai-sora | `headline_price_usd` | retrieved — silent |
| pass1/openai-sora | `headline_billing_basis` | retrieved — addresses *(weak; could move to silent)* |
| pass1/openai-sora | `annual_condition_disclosure` | retrieved — silent |
| pass1/openai-sora | `free_plan_exists` | retrieved — addresses |
| pass1/openai-sora | `free_plan_cap_documented` | retrieved — addresses *(via parent)* |
| pass1/openai-sora | `free_plan_cap_value` | retrieved — addresses *(via parent)* |
| pass1/openai-sora | `free_plan_watermark` | retrieved — addresses *(via parent)* |
| pass1/openai-sora | `free_plan_duration` | retrieved — addresses *(via parent)* |
| pass1/openai-sora | `trial_card_required` | retrieved — silent |
| pass1/openai-sora | `credit_rate_location` | retrieved — silent |
| pass1/openai-sora | `credit_rollover_policy` | retrieved — silent |
| pass1/openai-sora | `failed_generation_charge_policy` | retrieved — silent **(conditional; scan not run)** |
| pass1/openai-sora | `commercial_use_lowest_tier` | retrieved — silent |
| pass1/openai-sora | `watermark_removal_tier` | retrieved — addresses |
| pass1/phrasly | `headline_price_usd` | **retrieved — addresses (USD figure recovered)** |
| pass1/phrasly | `first_charge_amount_usd` | **retrieved — addresses (USD figure recovered)** |
| pass1/picsart | `headline_price_usd` | retrieved — silent (no US row in vendor's table) |
| pass1/picsart | `first_charge_amount_usd` | retrieved — silent (cascade) |
| pass1/wix | `unquantified_limit_clause` | retrieved — addresses |
| pass2/jobscan | `credit_rollover_policy` | retrieved — silent |
| pass2/jobscan | `renewal_notice_commitment` | retrieved — silent |

---

## What should be reclassified out of `access_failure`, and to what

**All 25 should leave `access_failure`.** Not one of them turned out to be a document this study could
not reach. The targets differ, and the difference matters more than the count.

The available vocabulary in `unknown-attribution.csv` is `vendor_silence`, `instrument_gap`,
`access_failure`, `unattributable_weak_basis`.

The arithmetic, so the groups below can be checked against the 25: **20 → `vendor_silence`** (12 in
the first group plus the 8 in the second), **3 → `instrument_gap`**, **2 → adjudication**.

**→ `vendor_silence` (12 values).** The relevant document class was read and the vendor never
published the thing.

| Record | Values |
|---|---|
| pass1/adobe-firefly | `trial_length_days` |
| pass1/openai-sora | `headline_price_usd`, `annual_condition_disclosure`, `trial_card_required`, `credit_rate_location`, `credit_rollover_policy`, `commercial_use_lowest_tier`, `failed_generation_charge_policy` *(conditional — see below)* |
| pass1/picsart | `headline_price_usd`, `first_charge_amount_usd` |
| pass2/jobscan | `credit_rollover_policy`, `renewal_notice_commitment` |

*(That is 12 rows. The eight values whose retrieved document also answers the construct are grouped
separately below, because for those the reclassification is not the whole finding.)*

**→ `vendor_silence`, and additionally the retrieved document *answers* the construct (8 values).**
These are the values where the coded `unknown` is contradicted by the document, so the reclassification
is the smaller half of the finding and the adjudicator should look at the value itself:

| Record | Values |
|---|---|
| pass1/openai-sora | `headline_billing_basis`, `free_plan_exists`, `free_plan_cap_documented`, `free_plan_cap_value`, `free_plan_watermark`, `free_plan_duration`, `watermark_removal_tier` |
| pass1/wix | `unquantified_limit_clause` |

**→ `instrument_gap` (3 values): the currency cluster where the vendor does publish a price.**

| Record | Values | Why not `vendor_silence` |
|---|---|---|
| pass1/canva | `headline_price_usd`, `first_charge_amount_usd` | Canva publishes ₺1,920/yr for Pro to this reader and "USD $100" for AI Pass in its own help centre. It is not silent about price. What defeats the coding is that D-007's test asks what "a US reader" is served, and the protocol supplies no executable route to occupy that position — currency selection is IP-bound and no locale path, parameter or header overrides it |
| pass1/gptzero | `headline_price_usd` | Same. GPTZero publishes TRY 549/mo billed annually to this reader, server-selected by IP, with no client-side price API and no parameter that changes it |

The precedent for this label on a price variable is already in the file:
`adjudicated/google-veo/headline_price_usd` is `instrument_gap` because "the adjudicator coded unknown
under protocol 7.4 step 5 for an underdetermined rule, not for vendor silence." The same reasoning
fits here.

**→ adjudication, not a clerical reclassification (2 values).**

| Record | Values | Why |
|---|---|---|
| pass1/phrasly | `headline_price_usd`, `first_charge_amount_usd` | These are the only two values in either sweep where a **USD figure for the entry tier was actually recovered** ($131.88/yr = $10.99/mo for Unlimited, from the vendor's own catalogue on its own pricing page, corroborated to within 0.4% by the record's coded TRY figure at a consistent implied FX rate). The record's stated premise — that no document anywhere states a USD number for this tier — does not survive. Whether a catalogue object counts as "the most prominent figure the vendor publishes ... in the page's default state" is a codebook question I have not answered. They should not stay in `access_failure` under any reading |

**Conditional, and the one thing I would hold back.** `openai-sora/failed_generation_charge_policy`
should move to `vendor_silence` *if* the orchestrator accepts inference from the article's documented
absence of any credit currency. If it wants the direct scan first, leave this single row in
`access_failure` and re-read the 2026-02-01 capture for `/fail|error|unsuccessful|deduct/i` once
archive.org's replay path is healthy.

**How many of the 25 the study is entitled to keep calling access failures: zero** — or one, if the
Sora `failed_generation_charge_policy` scan is required before moving it.

Taken with the first sweep, the study has attempted retrieval on all 46 values ever charged to
`access_failure`, and **exactly one is a genuine, permanent access failure**:
`hailuo-ai/annual_default_toggle`, where the plan UI sits behind an authenticated session the protocol
forbids creating.

---

## New under-retrieval mechanisms, added to the first sweep's four

The first sweep named four mechanisms: a bot wall read as an absent document; a single archive capture
generalised to the archive; a locale or translation layer mistaken for the document; and a rendered
figure read where a data layer was available. This sweep met all four again and adds three.

5. **Collapsed accordion content is present in `textContent` and empty in `innerText`.** Adobe
   Firefly's eleven FAQ answers were in the DOM at load, fully populated, behind
   `aria-controls` targets. A coder who clicks to expand and reads rendered text gets nothing and
   concludes the content is unreachable; reading `textContent` returns all 5,626 characters with no
   interaction at all. The same record had already solved the identical problem on a different Adobe
   page by fetching archived raw HTML, so the fix was in hand and simply was not carried across.

6. **Archive URL normalisation hides an entire capture history.** The Memento timemap returns **0**
   mementos for `https://gptzero.me/pricing` and **66** for `https://gptzero.me/pricing/`. An Arm 2
   check that queries one form can conclude "never archived" about a URL with 66 captures. Query both.

7. **Geo-bound currency is not an access failure, and calling it one hides a real limitation.** For
   Canva and GPTZero the pricing document is fully readable; the price is real, published and
   prominent; it is simply denominated by the reader's IP. No locale path, query parameter, header, or
   archive capture can change that, and for GPTZero an archive capture structurally cannot help
   because the crawler stores the pre-hydration shell. This is a limit on where the study's collection
   host sits, not on what it could reach — and the honest label is an instrument gap, because D-007
   asks a question ("what is a US reader served?") that the protocol gives the coder no way to answer.

**And one mechanism running the other way, worth recording as a success pattern.** Three of this
sweep's strongest retrievals came from **the vendor's own machine-readable payload on the page the
coder was already looking at** — Picsart's country-keyed price table, Phrasly's Paddle catalogue, and
(for a different variable class) Adobe's accordion `textContent`. Where a rendered figure looks
unreachable, the document usually already contains the answer in a form the renderer chose not to
show. That is now four vendors across two sweeps, which makes it a habit rather than a coincidence.

---

## Caveats against my own findings

**First, and most important: fourteen of these twenty-five results are inherited, not re-verified.**
The Sora findings rest on the first sweep's recovery of the Billing FAQ. Archive.org's replay path
returned HTTP 503 on every one of roughly a hundred attempts across this run, so I could not re-read
either capture. What I could check independently — that both slug variants and the parent collection
are genuinely 404 live, and that the timemap returns exactly 31 mementos — matched the first sweep's
account precisely. That is corroboration of its account, not a second reading of the article.

**Second, the Sora article self-scopes to "Sora 1 on Web".** Every finding drawn from it is a finding
about that product state, and the record codes Sora near its 2026-04-26 shutdown. This bites hardest
on `free_plan_exists` and the four cascades that follow it, and on `watermark_removal_tier`.

**Third, only three of the eight records carry independent evidence that today's text is window-era
text.** Jobscan's ToS self-dates "Last updated March 16, 2026", which precedes the window. Picsart's
Pro price (TRY 999/yr = 83.25/mo) is identical to the coded figure. Phrasly's rendered price today
(TRY 526.43) is within 0.4% of the coded TRY 524.43 at a consistent implied FX rate, and GPTZero's
TRY 549 is unchanged. The Adobe Firefly FAQ, the Canva pages and the Wix locale bodies carry **no
last-updated stamp**, and a vendor could have published or restored text between 2026-08-13 and today.
For Firefly specifically, the record's own window-era archive capture would have settled this and was
blocked by the outage — that thread is owed.

**Fourth, the Wix clauses are Turkish and German renderings, not the governing English wording,** and
the English rendering is the defective one. For a contractual variable that is a real evidentiary
limitation, and it should go to adjudication as such rather than be counted as settled.

**Fifth, two of my "addresses" findings are contingent on coding judgments I deliberately did not
take.** The Wix load clause may or may not clear codebook rule 3's conduct/volume line. The four Sora
`free_plan_*` cascades resolve only if an adjudicator accepts documented ineligibility of ChatGPT Free
as "no free plan" for Sora. Either could reasonably move.

**Sixth, the Phrasly USD figures are catalogue objects, not displayed prices.** They establish that the
vendor publishes USD prices for the entry tier on its pricing page. They do not establish which USD
figure a US reader sees, because the annual product carries a base price and three USD overrides and I
could not observe the rendered default state from a US position.

## Threads owed

All three are blocked on the same outage and none is load-bearing for the counts above.

1. **`openai-sora/failed_generation_charge_policy`** — re-read the 2026-02-01 capture and scan for
   `/fail|error|unsuccessful|deduct/i`. This is the only one that could change an outcome.
2. **Adobe Firefly's window-era capture `20260806112138`** — would replace this file's temporal caveat
   on that record with a direct window-era reading of the FAQ.
3. **Arm 2 for canva, gptzero and phrasly** — worth running for completeness, though the geo-bound
   currency analysis above predicts it cannot succeed for gptzero on any capture, and the first sweep
   plus this one both found Canva's archive captures bot-walled.
