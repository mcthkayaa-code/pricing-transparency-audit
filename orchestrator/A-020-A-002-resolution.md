# A-020 and A-002 — when the vendor published it and the rule is the obstacle

**Resolved 2026-08-17 by adjudication. No record edited; corrections are listed for the batch.**

Both items ask one question at two scales: *the vendor published the thing — does our rule let us code
it?* They get opposite answers, and the reason they differ is the whole content of this document.

- **A-020 recodes.** A determinate USD price is obtainable from the vendor's own served pricing-page
  document, and the fact the payload supplies is the *denomination* of a price every reader already
  receives. That is the one thing A-013 made vendor-centric.
- **A-002 does not, because it already did.** The adjudicated record carries the right value; the
  queue row predates the adjudication that answered it. What survives is a defect in the instrument.

---

# A-020 — `phrasly`: `headline_price_usd`, `first_charge_amount_usd`

## 1. The rules that decide it

**The governing rule, from `A-013-A-019-resolution.md`:**

> **A variable asks what a reasonably diligent reader of the vendor's published documents can
> obtain, from any standard reading position, without inspecting page internals.**

Its second clause:

> **"from any standard reading position"** — a plain browser, no account, no developer tools, but not
> tied to one geography, one A/B arm, or one date. If the vendor serves a USD price to readers in the
> United States, that price is obtainable and the study codes it.

Its third clause, and A-019's disposition:

> **"without inspecting page internals"** — a reader reads a page. They do not read its JSON payload,
> its JS bundles, or its DOM attributes. Data present only there is not disclosure.

> **A-019 → not disclosure.** A figure that exists only in unrendered markup fails the third clause.

**The variable, `codebook-v1.md` `headline_price_usd`:**

> **Definition.** The largest, most prominent price figure the vendor publishes for the entry paid
> tier on its pricing page.

> 2. Take the price figure the vendor displays most prominently for that tier, in the page's default
>    state as it loads. Do not switch a billing toggle before reading it.

> | `unknown` | A paid tier exists but no price figure could be located in any official document |

**`first_charge_amount_usd`, rule 2:**

> If the default is annual and the headline is a monthly figure, the first charge is the annual total
> the documents state.

**And the correction that decides the reading of a decision rule, from
`deviations-for-adjudicators.md`:**

> **Read a value's table before its example.** The codebook's illustrations of a value never bound it.

## 2. What I established today, and where the retrieval's account needs correcting

The retrieval was right that the catalogue is in the vendor's own pricing page, and right to flag the
one thing that would have blocked a recode. Both facts now have better evidence than either of us had.

Read from a rendered load of `https://phrasly.ai/pricing`, 2026-08-17, and from a same-origin refetch
of the page's own HTML (no account, no checkout, no interaction with any purchase control):

| Fact | Established how |
|---|---|
| The **served HTML document** for `/pricing` is **260,122 bytes** and contains the complete Paddle price catalogue inline, in the Next.js RSC flight payload | Same-origin `fetch('/pricing')`, unescaped and searched |
| The document contains **no `TRY` at all** — zero occurrences | Same fetch |
| The rendered page contains **zero `$`-figures and zero occurrences of "USD"** | `document.body.innerText` |
| **No currency or country selector exists** — 0 matches on the D-007 selector query | DOM query, reproducing the record's Arm 1 |
| Every request the page makes is **same-origin `phrasly.ai`**; the catalogue arrives from the vendor's own `/api/paddle/pricing` as well as inline | Network log |
| The catalogue's **complete** override key set is `ZA`, `BR`, `[MY,PH]`, `IN`, `ID`, `PH`, `MY` — **there is no `US` key and no `TR` key** | Exhaustive enumeration of every `countryCodes` array in the document |

The Unlimited tier's two price objects, verbatim from the served document:

```
"unitPrice":{"amount":"2000","currencyCode":"USD"},          // monthly, $20.00
"unitPriceOverrides":[{"countryCodes":["BR"],...BRL},{"countryCodes":["MY","PH"],...USD 1299},
 {"countryCodes":["ZA"],...ZAR},{"countryCodes":["IN"],...INR},{"countryCodes":["ID"],...USD 1099}]
"createdAt":"2024-08-06T22:26:05Z","updatedAt":"2026-04-24T20:47:17Z"

"billingCycle":{"interval":"year","frequency":1},
"unitPrice":{"amount":"13188","currencyCode":"USD"},         // yearly, $131.88
"unitPriceOverrides":[{"countryCodes":["BR"],...BRL},{"countryCodes":["PH"],...USD 8599},
 {"countryCodes":["ZA"],...ZAR},{"countryCodes":["IN"],...INR},{"countryCodes":["MY"],...USD 8499},
 {"countryCodes":["ID"],...USD 7299}]
"createdAt":"2024-11-04T20:52:09Z","updatedAt":"2026-04-24T20:45:58Z"
```

**Three things follow that neither the record nor the retrieval had.**

**First, the retrieval's one blocking caveat is dissolved.** It wrote that the catalogue "carries a base
price *plus three USD overrides* for the annual product, so it does not by itself settle which USD
figure a US reader is shown." The three USD overrides are keyed to the **Philippines, Malaysia and
Indonesia**. They are regional discounts. There is no US key, so a US reader falls through to the base
by construction, and the catalogue settles the question completely: **$131.88/yr, $10.99/mo.** Reading
the country keys is not reconstructing the vendor's selection logic — the keys *are* the logic, stated
as data.

**Second, the temporal warrant is now vendor-stamped rather than inferred.** The retrieval rested it on
FX corroboration within 0.4%. The price objects carry their own timestamps: the yearly price was created
**2024-11-04** and last modified **2026-04-24**, the monthly created **2024-08-06** and last modified
**2026-04-24**. Both modifications precede the collection window. The figure I read today is the figure
in force when the record was coded, on the vendor's own dating.

**Third, the record's Arm 2 conclusion is unsafe and should not be carried forward.** It reads: "No
readable price of any kind, in any currency, has ever been archived for this URL." That generalises
from a 34,722-byte capture. The document the vendor actually serves is 260,122 bytes. Whatever that
capture was — Cloudflare-degraded, bot-variant, truncated — it was not this document, and a scan of it
establishes nothing about what the archive could hold. This matters beyond the wording: because the
catalogue is inline in the **served HTML**, an archive capture of the real document *would* contain the
USD figures. Arm 2 is therefore **not structurally impossible for phrasly**, unlike GPTZero, where
retrieval 2 correctly showed the crawler can only ever store a pre-hydration shell with a
server-chosen currency. That thread is live and worth re-running when archive.org's replay path
recovers. (Archive replay returned 503 on every attempt today; CDX and the timemap both worked, and I
confirmed from them that 2026-07-12 20:29:52 is the newest real capture and that the record's
description of the 2026-08-10 204/bot-challenge capture is accurate.)

## 3. Ruling

**Recode.** `headline_price_usd = 10.99`, `first_charge_amount_usd = 131.88`.

**And on the question the queue put: a payment processor's price object shipped to the browser is an
internal layer under the A-019 test, not a published document under the A-013 test.** I hold that
squarely, and it does not decide this record. Both halves need saying.

**Why the catalogue is an internal layer.** A-013's third clause names three things a reader does not
read — "its JSON payload, its JS bundles, or its DOM attributes" — and an RSC flight payload is the
first of those exactly. Nothing renders it. A reader discovers it only by opening a network panel,
which is the developer-tools position the second clause excludes. The format test and the discovery
test both fail, and the stated purpose behind them — "a reader reads a page, they do not read its JSON
payload" — is not satisfied by a payload's being the renderer's *input* rather than inert. The reader
still meets only the renderer's **output**, and here the renderer transformed it: `13188` became
TRY 6,317, divided by twelve, printed as TRY 526.43. On the containment-versus-visibility axis that
A-019 was decided on, this object sits on the containment side, and it must, or A-019 collapses —
humbot's free-tier cap was read out of the same class of object and coded `vendor_silence`.

The one distinction available — that humbot's JSON was inert while phrasly's is live — I decline. The
rule's test is where the data is *present*, not whether something consumes it. Making consumption the
test would let any vendor earn disclosure credit for a fact its own renderer hides, which is the
outcome A-019 exists to prevent. And note the direction that refusal runs in: it is the half of this
ruling that costs the vendor, and I am stating it before the half that helps it.

**Why that does not decide this record.** A-019 bars coding a figure *present only* in the payload.
This figure is not present only there. The price is disclosed to every reader in every position:
TRY 526.43 in Turkey, $10.99 in the United States. Nobody is denied it. What the payload supplies is
not the price but its **unit of account** — and A-013 ruled, as the study's most consequential
interpretive choice, that the currency variables ask a **vendor-centric** question:

> The question is whether a USD price is obtainable from the vendor's documents in some standard
> reading position, not what currency our particular coder was served.

The vendor's denomination is precisely the vendor-centric fact. Recoding does not add a fact the
documents withheld; it restates a fact the record already coded — TRY 524.43 — in the unit the vendor
denominates it in. That is what protocol §6.8 and D-003 call a display variant, and the vendor says so
itself, in rendered prose, in its Terms: "All payments shall be in US dollars", and, of the trial fee,
"$2.00 USD ... or the equivalent amount converted to the user's local currency at the time of
checkout." The vendor states that USD is the price and that a local-currency figure is a conversion of
it. The catalogue confirms it: the document contains no TRY at all, and Turkey has no override, so the
TRY figure is a client-side conversion of a USD base and is not a price this vendor publishes.

So the test I am applying, stated so it can be re-applied or refused:

> A money value is coded where the vendor's **own served document** establishes, from its own data and
> without reconstructing its code, what a standard reader in *some* position is **rendered** — and
> where that reader's figure differs from ours only in denomination. Where the document establishes
> only that *we* were served a figure, the value stays `unknown`.

Phrasly meets it: the document is country-keyed, the US key is absent, the base is USD, and the
renderer's behaviour is proven by arithmetic on our own reading (13188 → TRY 6,317 ÷ 12 = 526.4
against a rendered TRY 526.43, implied 47.9 TRY/USD; and the same rate reproduces the record's own
524.43 four days earlier at 47.7). The only step I have not observed is that a processor returns USD
unchanged to a US reader, which is not a conversion at all.

**The steelman I rejected, and why.** The strongest case for keeping `unknown`: the study has no US
reading position, A-017 established that an archive capture cannot document a script-rendered state,
and so any claim about what a US reader *sees* is inference from internals — making `unknown` plus an
instrument-gap attribution the honest record of an instrument that cannot see what it needs to see.

I reject it on A-013's own terms. A-013 said "serves" and "is obtainable", not "and we read it from
there", and it ratified the D-007 recodes that read USD out of **US-crawled captures** rather than out
of a US-located human reading. Here the vendor's document does something a US-crawled capture could
not: it states the price *and its country-keying*, which removes the residual question a US reading
would have answered. Against that, `unknown` on this variable asserts, in the codebook's own words,
that "no price figure could be located in any official document" — when a figure has been located,
quoted verbatim, timestamped by the vendor to before the window, and corroborated by two independent
live readings four days apart. A-013's own drafting note warns against exactly this outcome:
"Publishing the first draft would have converted a correct, informative value into a false unknown."

**What this ruling does not license.** It is narrow and must stay narrow.

- It admits a payload **only** to establish the denomination and country-keying of a figure the page
  renders to every reader. It does not admit payloads generally. Had phrasly's catalogue carried a
  plan allowance the page never displays, A-019 would bar it, exactly as for humbot.
- It does not reach **Canva or GPTZero**, and the distinction is documentary, not convenient. Retrieval
  2 established that GPTZero's payload carries a **server-supplied** currency: the amount it contains
  is already the localised one, so no USD figure and no country-keying exists in the document to read.
  Canva's price is injected behind a bot wall with nothing country-keyed to read either. Phrasly
  differs because its document ships the whole multi-country table. `unknown` remains right for those
  two, and A-013's `unknown` branch — vendor bills by inferred geography with USD as the base — is
  exactly where they belong.
- It **may** reach one other record. Retrieval 2 records that Picsart's recovery came from "the
  vendor's own machine-readable payload ... Picsart's country-keyed price table". I have not read that
  record and must not. If that table is country-keyed in the sense established here — a USD base with
  no override for the reader's country — the test above applies to it on the same footing. The
  orchestrator should route the test; I assert nothing about that product's values.

## 4. Coded values that change

One record: `records/pass1/phrasly.yaml`. Phrasly is single-coded — there is no pass-2 record and no
adjudicated row — so the correction lands there and nowhere else. Prior passes are not rewritten in
place; the batch applies these as the record's own corrections, with the reasoning carried into
`coder_note`.

**Coder-entered values — 2 change:**

| Variable | Current | New |
|---|---|---|
| `headline_price_usd` | `unknown` | **`10.99`** |
| `first_charge_amount_usd` | `unknown` | **`131.88`** |

**Unchanged, verified rather than assumed:** `entry_tier_name` (Unlimited — and the USD figures
confirm the record's own robustness check: Unlimited $131.88/yr against 3 Day Access $239.88/yr, which
the catalogue states directly as `23988 USD`); `headline_billing_basis` (`per_month_billed_annually`);
`annual_condition_disclosure` (`adjacent`); `mandatory_addon_present` (`no`);
`cost_per_output_computable` (`yes`); `cost_per_output_unit` (`per_seat_month`); every domain 2–10
value.

**Prose and register fields that must be corrected in the same batch:**

| Field | What is now wrong |
|---|---|
| `computation_assumptions` | Denominated in TRY throughout and states "first_charge_amount_usd itself is unknown". Needs rewriting to USD within the 300-char cap: Unlimited, annual default, $10.99/mo billed annually, per_seat_month unit so cost/output = 10.99; first charge = 131.88 read directly from the vendor's annual price object, corroborated by 10.99 × 12. |
| `headline_price_usd` / `first_charge_amount_usd` evidence | Both rest on the premise that "no document anywhere stat[es] a USD number for the Unlimited tier". False. |
| `coder_note` / `conflict_note` | Carry the same premise, plus the unsafe Arm 2 generalisation quoted in §2 above. |
| `register_events` | `[]`, justified as "this record never had a display_variant entry for currency (correctly -- neither state ever showed USD)". That reason no longer holds: the document is served in two display states by inferred geography, which §6.8's preamble names explicitly. **But a conforming §6.6 entry cannot be built** — it requires "both dates and both archive URLs", and no US-served archive URL exists. Record the geographic variance in `coder_note` and in the §7.6 display-variance discussion, and log the unbuildable register entry as a second instance of A-017's gap. |

**Derived variables — every one that touches the money values.** None is coder-entered; all are
computed post-freeze and simply need recomputation for this product.

| Derived variable | Current | New |
|---|---|---|
| `headline_vs_first_charge_gap_ratio` | `not_computable` (both inputs `unknown`) | **12.00** |
| `cost_per_output_value_usd` | not derivable in USD — the record's own arithmetic returns TRY 524.43 for a variable whose name requires USD | **10.99** per seat-month |
| `unknown_count` | includes item **A1** (single-variable, `unknown`) and item **A3** (scores 0 with an `unknown` sub-variable → item-level `unknown` under rule G5) | **−2** |
| `determinability_rate` | A1 and A3 both non-determinate | numerator **+2**; denominator unchanged (no item added or removed) |
| `apti_earned` | A1 `unknown` = **0 of 8**; A3 row `unknown` × column `no` = **0 of 5** | A1 money = **8 of 8**; A3 money × `no` = **5 of 5** → **+13** |
| `apti_available` | 20 on component A | unchanged |
| `apti_component_a` | 7 / 20 = **0.35** (A2 `adjacent` = 7 only) | 20 / 20 = **1.00** |
| `apti_total`, `apti_band`, `apti_equal`, `apti_unknown_excluded` | — | recomputed; +13 earned on a 20-point component moves the band for this product |

So: **two coded values, and every derived quantity downstream of them.**

## 5. Direction

**Stated plainly: this ruling runs toward the vendor on the index, against this study's headline, and
it is not what I wanted the answer to be.**

- **Against the study's headline.** It removes two `unknown`s and hands one product 13 of 13 points it
  currently scores zero on, taking component A from 0.35 to 1.00. The unknown burden is this study's
  central quantity and this shrinks it. If the test reaches Picsart as well, it shrinks it further.
- **Toward the vendor, but not uniformly.** The recode also makes
  `headline_vs_first_charge_gap_ratio` computable at **12.00** — the study can now report that this
  vendor advertises $10.99 and charges $131.88 on the first transaction. Under `unknown` that 12×
  gap was `not_computable` and went unrecorded. Determinacy cuts both ways: A3 scores whether a buyer
  can state the figure, not whether the figure is kind to her.
- **And a further observation against the vendor, verified but not coded.** The Unlimited card's
  struck-through reference price (TRY 1,197.03, $24.99 at the implied rate) **corresponds to no price
  object anywhere in the vendor's catalogue**, and exceeds by 25% the highest price the catalogue
  actually charges for the tier ($20.00/mo). No wave-1 variable captures reference-price integrity, so
  this is an observation for the record's `conflict_note` and a wave-2 candidate, not a coded value.
- **On the honesty of the direction.** The half of this ruling that decides the queue's stated
  question — a processor's price object is an internal layer, not a published document — is the half
  that would have kept the unknowns. I reached it first and it did not settle the record, because the
  record turns on denomination rather than on containment. Had the catalogue carried a `US` override,
  or had the country keys been absent so that the base could not be shown to govern, the value would
  have stayed `unknown` and I would have written that instead.

## 6. What wave 2 must change

1. **Give A-013's rule a fourth clause on denomination.** The three clauses as written cannot resolve
   this record: the second says code what a US reader is served, the third says do not read the
   payload, and here only the payload says what the US reader is served. State that where a document
   publishes a country-keyed price table, the reader's-position question is answered from the table's
   keys, and that this admits the payload for denomination only.
2. **Add the second currency variable A-013 already promised** — "what currency is a reader in the
   study's own jurisdiction served" — so phrasly's TRY 526.43 and its $10.99 are both reported instead
   of one being recorded as the other's absence.
3. **Add a currency field to the cost-per-output pair.** `cost_per_output_computable = yes` combined
   with `headline_price_usd = unknown` produces a `cost_per_output_value_usd` that cannot be expressed
   in USD; this record's own arithmetic returned a TRY figure for a USD-named variable, and nothing in
   the instrument caught it. The recode cures it here and leaves it live for Canva and GPTZero.
4. **Give §6.6 an evidence form for a geographically-varied display state.** The two-archive-URL
   requirement is unsatisfiable for a state our collection host cannot occupy — A-017's gap, met again
   here from the other direction.
5. **Tell coders that a bot-degraded capture cannot ground a negative.** The Arm-2 failure in §2 turned
   on a capture 13% of the served document's size, and no check compared the two sizes.

---

# A-002 — `adobe-express`: `credit_to_output_rate_published`

## 1. The rules that decide it

**`credit_to_output_rate_published`, the value table:**

> | `yes` | Rates are published for the principal output and for the other output types the plan advertises |
> | `partial` | Rates are published for some output types but not the principal one, or only as a range |

**Its decision rule:**

> 1. Identify the principal output, the one the product is sold to produce.
> 4. Rates published for secondary features but not the principal output are `partial`. This is the
>    only variable that applies the principal-output test; `credit_unit_defined` deliberately does not.

**`cost_per_output_unit`, rules 1 and 2:**

> 1. The principal output is what the product is sold to produce, as its own pricing page frames it.
> 2. Where a product sells unmetered access to software rather than a countable artifact, the unit is
>    `per_seat_month`.

**And the binding correction that resolves the collision:**

> **Read a value's table before its example.** The codebook's illustrations of a value never bound it.
> A value was once coded `no` because the vendor's arrangement did not match the illustration, while
> the same variable's value table independently listed the route the vendor had taken.

## 2. Ruling

**The principal-output coding was right. The rule is what needs revisiting. And the queue row is
stale — adjudication has already settled the value at `yes`.**

**The principal-output coding is right on this vendor's own framing.** `cost_per_output_unit` rule 1
asks how the pricing page frames the product, and Adobe's frames a suite: templates, assets, fonts,
storage, brand kits, PDF tools, scheduling, with 250 generative credits a month as one line among
dozens. Rule 2 is met on its face — unmetered access to software, not a countable artifact — and both
passes reached `per_seat_month` independently. Nothing to revisit.

**The rule as written produces the wrong value given that coding, and the defect has a precise name:
rule 4 fires on a vacuously-true antecedent.** The two variables do not mean the same thing by
"principal output". For `cost_per_output_unit`, `per_seat_month` is a **residual** value whose entire
function is to say *this product has no discrete countable output*. For
`credit_to_output_rate_published`, "the principal output" **presupposes** a countable artifact against
which a credit rate could be quoted. Feed the residual into the presupposition and rule 4's
antecedent — "rates published for secondary features but not the principal output" — is satisfied
because there is no principal output to publish a rate for, not because the vendor withheld anything.
The instrument then marks the vendor down for an omission that is logically impossible to commit. This
is the same failure mode A-012 reasoned through as a false antecedent on its rule 3, which makes it a
recognised defect class in this study rather than a novel complaint.

**The value table gives `yes` once the presupposition is dropped.** Its test is "rates published for
the principal output and for the other output types the plan advertises". The first conjunct is vacuous
for a `per_seat_month` product; the second is fully satisfied — a general baseline rate ("Most standard
generative AI features ... use 1 credit per generation"), an itemised table for every premium output
type ("Firefly Image 4 Ultra ... 20 credits per generation", "Generate Video ... 1080p at 24 FPS ...
100 credits per second"), and an explicit list of which Express features consume no credits at all.
Nothing is withheld anywhere inside the credit system's scope. Pass 1 reasoned from rule 4, a
decision-rule step keyed to the codebook's worked example — Vendor K, whose principal output *is* a
creditable artifact lacking a rate. The binding correction quoted above is written for exactly that
move.

**This is a finding about the instrument, and it belongs in wave 2 whether or not a value changes.**
Say it plainly, as the queue asks: **a fully published credit-rate table can code as less than fully
published, because of an interaction between two variables and not because of anything the vendor did
or failed to do.** Every other structurally-forced outcome in this instrument is named and argued
where it occurs — the A3 dagger note, the B1 matrix, B3's impossible pair. This one is not named
anywhere, and it is not a state anyone chose.

**A second instance, found on my own other product and flagged rather than acted on.** Phrasly is also
`cost_per_output_unit = per_seat_month` with `credit_system_present = yes`, and also codes
`credit_to_output_rate_published = partial` — on the reasoning that the credit rate is published for a
secondary feature while "the product's principal output ... is metered in direct word units, not
credits, and no credit rate applies to it." That is the same vacuous firing in different clothes: the
principal output consumes no credits, so there is no credit rate to withhold. Two products in the
small set I am entitled to read makes this a **finding class, not one vendor's edge case** — the
variable penalises any product whose principal output is not credit-metered, whether because it sells
unmetered seat access or because it meters the principal output in some other unit. I am not recoding
phrasly's value: it is outside A-020's scope, which is the money values and their derivations, and it
needs the deliberation A-002 got rather than a hand-applied precedent. **The orchestrator should route
it, and should expect further instances.**

## 3. Coded values that change

**None.**

`records/adjudicated/adobe-express.yaml` already carries `credit_to_output_rate_published = yes`,
resolved in favour of pass 2 and flagged in its own evidence field as "a codebook gap rather than a
coder error on either side". That is the value the published dataset carries, and I reach the same
outcome by a route that overlaps the adjudicator's and sharpens it: the adjudicator argued from the
absence of any dagger note naming this state and from the scope of the variable's definition; the
vacuous-antecedent diagnosis says *why* the omission is impossible to commit, which is what makes the
`yes` compelled rather than merely better-argued.

`records/pass1/adobe-express.yaml` keeps `partial` and `records/pass2/adobe-express.yaml` keeps `yes`.
Neither is rewritten — the disagreement is a reliability observation, and pass 1 flagged it for
adjudication in its own `coder_note`, which is the diligence the design asks for.

**The queue row should be struck through as resolved-by-adjudication, with the date of the adjudicated
record rather than today's date**, so the queue does not imply the item sat open after it was answered.

## 4. Direction

**Toward the vendor, and it was already taken.** `yes` scores item C2 in full where `partial` scores
part; the adjudicated record banked that before this review. My ruling adds no points and removes no
unknowns — it confirms a value and converts the adjudicator's flagged gap into a stated defect.

**Against this study's headline in one respect worth naming:** if the vacuous-antecedent reading is
right, then `partial` values on this variable across the corpus are not all evidence of vendor
non-disclosure, and any count of them overstates opacity by however many `per_seat_month`-and-credits
products it contains. The phrasly instance says that number is at least one beyond adobe-express. That
tells against the study, so it is stated with the same directness as the finding that helps it.

## 5. What wave 2 must change

1. **Split the construct.** `credit_to_output_rate_published` should ask whether rates are published
   for **every output type the credit system meters**, and drop "principal" — or carry an explicit
   `not_applicable`-style route for products whose principal output consumes no credits.
2. **Name the interaction where it occurs**, in the variable's own entry, in the form the A3 and B1
   matrices already use for their unreachable pairs: `cost_per_output_unit = per_seat_month` plus a
   credit system cannot reach `partial` by way of rule 4.
3. **Audit rule antecedents for vacuous satisfaction across the instrument.** Two of this study's
   adjudications — A-012 and this one — turned on a decision rule firing because its antecedent was
   vacuously true. That is a systematic drafting risk, not two coincidences, and wave 2's referee pass
   should test every decision rule against the residual values of the variables it reads.
4. **Carry the codebook's own warning into the coder instructions**, not only into the adjudicator
   corrections: read the value table before the decision rule's worked example, because an example's
   fact pattern is not the value's boundary.

---

## Disclosures

- **I read the vendor's live pricing page and its own same-origin JSON endpoint in a rendered
  browser**, including its inline payload. No account, no login, no trial, no checkout, no purchase
  control touched, no payment detail entered. Reading internals was necessary to answer whether
  internals may be *coded*; the ruling above holds that they may not, except for denomination.
- **I read `orchestrator/post-window-retrieval-2.md` in full around the phrasly section**, which names
  other products. It was assigned reading. The only place it influenced me beyond phrasly is the
  Picsart flag in §3, which asserts no value and is routed to the orchestrator rather than acted on.
- **I did not open another product's record.** The phrasly credit-variable observation in A-002 comes
  from my own assigned product's record. I used `record-template.yaml` and the codebook for field
  shapes.
- **The Memento timemap worked where CDX was intermittent**, and archive replay returned 503 on every
  attempt, so the archive-side checks in §2 rest on CDX and timemap metadata plus the record's own
  logs, not on a fresh reading of any capture. Retrieval 2's "threads owed" item 3 stands, and is now
  worth more than it looked: a real capture of the 260 KB document would carry the USD catalogue from a
  US crawl.
