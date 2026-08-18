# A-021 — does `cost_per_output_computable` mean computable in USD, or computable at all

**Resolved 2026-08-17 by an adjudicator working across six records under delegated authority.**
Companion to `orchestrator/A-013-A-019-resolution.md`, which this item extends one level down: A-013
made the money variables vendor-centric on obtainability; this item asks whether the same reading
applies to the variable that reports whether a cost *per output* can be worked out from what the
vendor publishes.

**One-line answer: `cost_per_output_computable` is currency-neutral by the instrument's own design —
it asks whether the arithmetic is possible from published figures, not whether the answer comes out
in dollars — and that reading is not a construct choice I am making today. It is already written into
`protocol-v1.md`, pre-registered, before any of these six products were collected.**

## Summary

| # | Record | Variable | Situation | Current | New | Changed? |
|---|---|---|---|---|---|---|
| 1 | aiva | `cost_per_output_unit` | not a price claim | `other` | `other` | No |
| 2 | aiva | `cost_per_output_computable` | 1 (non_usd, single currency) | `yes` | `yes` | No |
| 3 | canva | `cost_per_output_unit` | not a price claim | `per_seat_month` | `per_seat_month` | No |
| 4 | canva | `cost_per_output_computable` | 3a (real price, US-reader test only) | `yes` | `yes` | No |
| 5 | gptzero | `cost_per_output_unit` | not a price claim | `per_1k_words` | `per_1k_words` | No |
| 6 | gptzero | `cost_per_output_computable` | 3a (real price, US-reader test only) | `yes` | `yes` | No |
| 7 | ismybrandinai | `cost_per_output_unit` | not a price claim | `other` | `other` | No |
| 8 | ismybrandinai | `cost_per_output_computable` | 2 (no paid tier, $0) | `yes` | `yes` | No |
| 9 | openai-sora | `cost_per_output_unit` | not a price claim | `per_video_minute` | `per_video_minute` | No |
| 10 | picsart | `cost_per_output_unit` | not a price claim | `per_seat_month` | `per_seat_month` | No |
| — | **picsart** | **`cost_per_output_computable`** | **3a, mis-gated on currency** | **`unknown`** | **`yes` (₺83.25/seat-month)** | **YES — outside the ten, entailed by the same ruling** |

**Zero of the ten flagged values change. One value outside the ten — found while applying the same
ruling consistently across the six records — should change, from `unknown` to a determinate `yes`.**
Full reasoning for every row below.

---

## 1. The construct ruling

### 1.1 What the disputed variable's own text says

`codebook-v1.md`, `cost_per_output_computable`:

> **Definition.** Whether a reader can calculate a cost per unit of principal output using only
> published figures and arithmetic.
>
> 1. **The price input is fixed.** It is the **entry paid tier's price**, as selected under
> `sampling-rules.md` section 7.2 and read **in the pricing page's default display state**. Not the
> cheapest plan on the page, not the plan whose allowance divides most neatly, and not a figure found
> by switching the billing toggle. Two coders computing the same product must start from the same
> number.

No currency word appears anywhere in the definition or the nine-step rule. It sources its numerator
from `sampling-rules.md` section 7.2, which is itself currency-agnostic on its face:

> **Price basis.** Among the eligible candidates, the **entry paid tier** is the one with the
> **lowest annual-equivalent cost of a single seat, computed in the pricing page's default display
> state**.
>
> 1. **Read the page as it loads.** … 2. **Annualize whatever that state shows.** …

"Lowest annual-equivalent cost," not "lowest USD cost." A comparison between two figures in one
currency, on one period, for one seat needs no exchange rate, and §7.2 never asks for one. (This is
also what a different adjudicator concluded, independently, resolving A-001 on this same day — see
the disclosure section below for exactly how I used that document and what I verified myself rather
than took from it.)

### 1.2 The decisive evidence: the protocol already answers this, pre-registered

This is the piece that settles it rather than merely supports it. `protocol-v1.md` §8.3.10 argues
the instrument's one deliberate currency deduction, and names which items carry it:

> **`non_usd` is deducted rather than treated as neutral.** **Items A1 and A3** dock a product that
> publishes no USD figure. The reason is a determinability claim about a specific reader: this index
> reports in USD, and a buyer reading in USD cannot state what she will pay without an exchange rate
> we refuse to invent under section 6.5. … This makes the index USD-centric, the limitation is
> recorded as item 12 of section 9…

And the limitations register restates the same scope, by the same two item names:

> **12. The index is USD-centric.** **Items A1 and A3** deduct points where a vendor publishes no
> USD figure, because the index reports in USD and section 6.5 forbids inventing an exchange rate.
> For a buyer reading in the vendor's own currency those terms may be perfectly determinable, and the
> deduction does not describe her.

A1 is `headline_price_usd`. A3 is `first_charge_amount_usd` and `mandatory_addon_present` together.
**Item C3 — `cost_per_output_computable` — is not named in either sentence**, in a document that
names its two USD-docked items explicitly, twice, in two different sections, specifically so a reader
does not have to guess which items carry the limitation. The scoring table confirms it structurally:
A1's own row prints a `non_usd` value at half credit (`Numeric USD price… 8. non_usd: 4.`); C3's row
carries no such value or deduction at all —

> C3 Cost per output computable | 5 | `yes`: 5. `partial`: 2.5. `no`: 0. `unknown`: 0. `conflicting`:
> 1.7. Never `not_applicable`…

`cost_per_output_computable`'s own value list has no `non_usd` option to begin with — only money
variables carry that value. This was written before the window opened (§12.1: "Versions 1.1 and 1.2…
issued before the window opens and before any data exists"), months before any of these six products
were read. It cannot have been shaped to produce a favourable outcome for this adjudication, because
it existed before the disagreement it now resolves did.

### 1.3 Corroborating structural evidence

**The naming convention is consistent and load-bearing.** Every variable that is actually a
dollar-denominated value carries the `_usd` suffix and a `non_usd` escape hatch: `headline_price_usd`,
`first_charge_amount_usd`, and the *derived* `cost_per_output_value_usd`. `cost_per_output_unit` and
`cost_per_output_computable` carry neither. The codebook is careful about this elsewhere (§2.3's
exception register is itself an exercise in stating exactly which variables carry which status
values); the omission is a signal, not an accident.

**The alternative reading has no home in the variable's own value table — a reductio, checked against
every row.** Suppose "computable" meant "computable in USD." A vendor that publishes every figure
needed, completely, only in euros or lira, is not `no` (`no` requires "at least one required figure is
not published" — none is missing, they are all published, just not in dollars). Not `partial` (that
value's two cases are a secondary-output shortfall or a range; neither applies to a complete,
single-figure, foreign-currency calculation). Not `unknown` (`unknown` requires "the documents needed
could not be located"; they were located and read). There is no cell in this variable's own table for
"fully disclosed, just not in dollars." A reading that produces a case the instrument cannot express is
not the instrument's own reading.

**Direct parity with A-013.** That ruling held that a vendor which positively, singularly publishes a
price in one non-USD currency and nothing else is `non_usd` rather than `unknown`, because that is
"a positive, informative finding about the vendor, not an absence of one." The same principle bars
treating a vendor's complete foreign-currency cost-per-output disclosure as if it were silence merely
because the number is denominated in euros rather than dollars.

### 1.4 Which way this cuts, and why the direction does not decide it

**Reading `cost_per_output_computable` as currency-neutral keeps ten determinate values rather than
converting them to `unknown` or `no` — the convenient direction, and I want that named before applying
it rather than after.** But every piece of evidence above is a textual or structural fact about the
instrument, established independent of outcome: §7.2's own wording, §8.3.10's and §9.12's pre-registered
item list (written before collection began), the value table's own vocabulary, the naming convention.
None of these were selected because they produce a favourable count; they are where "what does this
variable mean" is actually answered in this instrument, and they agree. Stress-tested the other way: had
§8.3.10 named C3 alongside A1 and A3, or had the value table included a `non_usd` row for C3, I would
have ruled the other way on the same method, and said so. It does not, and I did not have to choose.

**What this construct ruling does *not* do: it does not make the derived dollar figure appear.**
`cost_per_output_value_usd` is a separate, downstream, `_usd`-named variable, computed after freeze,
and protocol §6.5's "we do not invent an exchange rate" governs it exactly as it governs `headline_price_usd`.
A vendor's foreign-currency cost-per-output disclosure earns full credit on the *disclosure-sufficiency*
item (C3, scored in the index) while its *comparable dollar figure* (the derived reporting field, not
scored, used for cross-vendor tables) stays unavailable. Both are true at once, and §4 below states which
records are in each state and what the study loses by it.

---

## 2. Per record

Live-verified today (2026-08-17) wherever the figure a record rests on could be reached without a
rendered-browser tool; see Disclosures for exactly what was and was not re-checked and why.

### `cost_per_output_unit` — one finding that covers all six instances

Before the per-record situations: **none of the six `cost_per_output_unit` entries was ever actually in
tension with a non-USD or unresolved `headline_price_usd`, and none needs the construct ruling above at
all.** Its definition is "the unit in which this product's principal output is counted," and its rule
asks only "what the product is sold to produce, as its own pricing page frames it" — a categorical fact
about the *kind* of thing sold (video minutes, words, seats, a robots.txt check), never a number, a
price, or a currency. `openai-sora` demonstrates this cleanly: its coder assigned `per_video_minute`
from the marketing page's "turn your ideas into videos" copy, with *zero* price information located
anywhere for this product. A categorization needs no numerator to categorize. The build script's
contradiction check flagged all six as if a determinate `cost_per_output_unit` implied a computed-cost
claim; it never does. **All six stay exactly as coded, and the reason is that they were never
contradictory with anything, not that the currency question resolves in their favour.** I recommend
`tools/build_dataset.py`'s flagging heuristic stop matching this variable (§5, tooling note).

### aiva — Situation 1 (headline `non_usd`, single currency affirmatively established)

Adjudicated record (`records/adjudicated/aiva.yaml`), both prior passes agreed, DOM-scanned: "No USD
figure or currency/country selector exists anywhere on the page." Live-reconfirmed today: `www.aiva.ai`
still shows "€11 / month" (Standard, the entry tier), "€33 / month" (Pro), "€0" (Free), "15 downloads
per month" for Standard — no `$`, no currency selector, byte-identical to the three prior reads spanning
2026-08-06 to 2026-08-15.

- `cost_per_output_unit = other` ("per track download") — a categorization, per the general finding
  above. **Unchanged.**
- `cost_per_output_computable = yes`, €11 ÷ 15 = €0.73/download, both figures on the same (monthly)
  period, no assumption needed. Every figure published, fully in one currency, no gap. **Unchanged**
  under §1's ruling — this is the paradigm case the ruling is written for.
- Downstream (not a coded value on this record; a post-freeze computation): the derived
  `cost_per_output_value_usd` should be `not_computable`, currency and figure preserved in
  `computation_assumptions` (already there, verbatim: "11 / 15 = EUR 0.73 per download").

### canva — Situation 3a (a real price *was* read; `unknown` is a US-reader-test artifact, not absence)

`records/pass1/canva.yaml`. This is the record whose own coder already worked through exactly this
question and answered it the same way I do here, independently, on 2026-08-10 — worth stating because
it is corroboration, not the basis for my ruling.

The critical fact the task's own three-situation framing risks flattening: **`headline_price_usd = unknown`
here does not mean no price was found.** A real, DOM-confirmed, twice-corroborated figure was read from
this study's own actual reading position — Pro, "1.920 TRY," captioned "annual price for one person,"
rendered, archived locally, and independently re-found via a second locale path in a later sweep. The
field reads `unknown` rather than `non_usd` or a money value **only** because A-013's specific test for
*that* variable asks whether a USD figure is obtainable from *some* standard reading position (because
the variable is literally named `_usd`), and Canva's own help article makes the served currency
geography-dependent with USD as a named fallback — so neither "a USD figure was obtained" nor
"definitively, only this one currency exists" can be said. That is a fact about the money-specific test,
not a fact about whether any price exists. The record's own words: "headline_price_usd is unknown… no
USD figure exists in any document to substitute, and this variable's rule does not gate on
headline_price_usd's specific value, so the TRY-denominated computation itself is unaffected."

- `cost_per_output_unit = per_seat_month` — categorization ("Pro card is scoped 'For one person'…
  core design features carry no usage ceiling"). **Unchanged.**
- `cost_per_output_computable = yes`, 1,920 TRY/yr ÷ 12 = 160.00 TRY/month; per-seat-month means the
  monthly-equivalent price directly *is* the output cost, no separate allowance to convert. **Unchanged**
  under §1 — the same reasoning as aiva, with the "unknown" label correctly not read as blocking it.
- Downstream: derived `cost_per_output_value_usd → not_computable` (already the study's own
  recommendation from the same-day A-001 resolution, which I affirm and extend to the other two
  records below); figure preserved as ₺160.00/seat-month in `computation_assumptions` (already there).

### gptzero — Situation 3a, same pattern as canva, reached independently

`records/pass1/gptzero.yaml`, a different coder, same construct question, same answer, same day. Premium:
"TRY 549/ month, billed annually," "Up to 300,000 words per month," both on the same card, same period.
`headline_price_usd` moved `non_usd → unknown` under the D-007 re-check for the identical reason as
canva — GPTZero's own ToS states "All payments shall be in U.S. dollars," which is evidence *against* a
clean single-currency finding, while no document states the actual dollar figure, so the field reads
`unknown` rather than `non_usd`. The coder's own words: "This variable's value list has no `non_usd`
option and nothing in its decision rule gates on currency, so headline_price_usd = non_usd does not
block this."

Static curl today confirms the live page is still a pre-hydration JS shell to a non-rendering fetch (no
"549," no "TRY," consistent with the record's own documented D-005 finding that this page requires a
rendered read) — so I did not attempt to independently re-render it; see Disclosures for why I judge
this proportionate rather than a gap.

- `cost_per_output_unit = per_1k_words` — categorization, from the published per-word overage rate
  ("$0.00046 per word" beyond allowance, confirming words as the metered dimension). **Unchanged.**
- `cost_per_output_computable = yes`, 549 ÷ 300,000 = 0.00183 TRY/word (TRY 1.83/1,000 words), both
  figures on the same card, same period. **Unchanged.**
- Downstream: derived `cost_per_output_value_usd → not_computable`; TRY 1.83/1,000 words preserved.

### ismybrandinai — Situation 2 (no paid tier at all; zero is the strongest case, not the weakest)

`records/adjudicated/ismybrandinai.yaml`. Five independent official documents (ToS, About, Tools
listing, the AI Bot Checker page, and the absence of any `/pricing` route in the site's own
`sitemap.xml`) affirmatively establish no paid tier exists anywhere. Live-reconfirmed today: the tool
page still reads "Free AI Bot Checker," "this free checker," unchanged.

This is not merely "arguably computable," as the task's framing puts it — it is the single most
determinate case in the whole set, and its currency-neutrality is stronger than the other three, not
weaker. A wholly free product's cost per output is $0.00, for any unit, forever, guaranteed by the
vendor's own affirmative statement, with no arithmetic even required beyond recognizing that zero
divided by anything is zero. Every alternative value fails the same reductio run in §1.3: `no` needs a
missing figure (none is missing — "free" is stated five separate times); `unknown` needs an unreachable
document (all five were read); `not_applicable` is categorically barred by the codebook's own exception
register ("every product has a principal output unit, so item C3 applies to every product"), which was
written for exactly this purpose — to force a real answer for the free-product case rather than let it
opt out.

- `cost_per_output_unit = other` ("per domain / robots.txt check") — categorization. **Unchanged.**
- `cost_per_output_computable = yes`, $0.00. **Unchanged**, and on stronger footing than §1's general
  ruling needs: zero requires no currency at all, so this record does not even depend on the
  vendor-currency reading — it would be `yes` under either construct reading of C3.
- Downstream: **this is the one record where the derived `cost_per_output_value_usd` does *not* need
  `not_computable`.** $0.00 is already a USD figure with no exchange rate to invent — zero in any
  currency equals zero dollars. `cost_per_output_value_usd = 0.00` is a straightforward application of
  the existing derived-variable rule, no extension needed. This distinguishes ismybrandinai cleanly
  from the three non-zero foreign-currency records above.

### openai-sora — Situation 3b (genuinely no price, in any currency, from any reading position)

`records/pass1/openai-sora.yaml`. This is the one record in the set of six where the task's "really does
look incoherent" concern would bite — *if* the pairing existed. It does not: `cost_per_output_computable`
here is already `unknown`, not a determinate value, so the build script never flagged it as one of the
ten (only `cost_per_output_unit` was flagged, and that variable was never a price claim — see above).

The record documents a genuine, thorough, three-surface search (`sora.com`, `openai.com/sora/`, the
archived `chatgpt.com/pricing`) plus a fourth attempt at the one document that would have stated the
credit-to-output rate (the Sora Billing & Credits FAQ, HTTP 404 live, empty archived shell) — none
recovered a price in any currency, and the entry tier itself could not be identified. A second,
independent re-read on 2026-08-10 (labelled D-009 in the record) reproduced the same finding. Under the
value-table test in §1.3, `unknown` — not `no` — is exactly right: the document that would answer the
question exists and could not be reached, which is `unknown`'s own definition ("the documents needed
could not be located"), distinct from `no`'s ("read and found silent").

- `cost_per_output_unit = per_video_minute` — categorization, from marketing copy alone, needing no
  price information. **Unchanged.**
- `cost_per_output_computable = unknown` — already correct, already consistent with §1's ruling
  (no figure exists in *any* currency to compute from). **Unchanged.**
- **This record is not incoherent.** Nothing here required a construct ruling to resolve; it was
  already right.

### picsart — Situation 3a, same pattern as canva and gptzero, but the coder answered it the other way

`records/pass1/picsart.yaml`. This is the one place the corpus disagrees with itself on the exact
question A-021 asks — not between two coding passes (picsart has no pass 2; it was not in the
double-coded subsample), but between this record's own reasoning and canva's/gptzero's, on an
identical fact pattern, reached by different coders on different days.

Live-reconfirmed today: `picsart.com/pricing/` still returns real, substantial rendered content to a
plain fetch (unlike the record's `default_display_state` note, which describes an earlier "static
fetch/curl returns empty JS-shell" state — the page evidently now serves enough server-rendered markup
for a static read to work). Its own embedded payload reads, verbatim: `₺ | 83.25 | /mo | Billed yearly`
for Pro — the exact figure the record cites, unchanged since collection (2026-08-10).

The record's own `headline_price_usd = unknown` rests on the same D-007 two-arm test as canva and
gptzero — no currency selector, no readable USD figure in the most recent US-crawled archive capture —
and the same underlying fact: a real TRY price (₺83.25/mo) *was* read, from the actual default display
state, and is sitting in the record. `cost_per_output_unit = per_seat_month` is settled and uncontested
(Ultra explicitly bills "per seat"; the bulk of the feature list is unmetered software access). Given
that unit, the record's own words for what the "output" price would be: "**the 'output' price is the
headline seat-month price itself**" — the identical structure as canva's "the monthly-equivalent price
IS the cost per output unit," no separate allowance to convert, no range, no secondary-output problem.

The record then declines to compute it: `cost_per_output_computable = unknown`, on the stated ground
that this figure "is unknown in USD… the currency block, not a missing figure, is what prevents
computation." That is precisely the reading §1 rules against — it gates a currency-neutral variable
on `headline_price_usd`'s specific coded value, which rule 1 never asks for, and it is the same fact
pattern canva's and gptzero's own coders read correctly on the same day.

**This is a genuine error, not a defensible alternative reading, for the same reason §1.3's reductio
applies here without qualification: nothing is missing.** The price is published (₺83.25/mo), the
period already matches (no conversion needed — it is not even an annual-total case like canva's), and
the unit needs no allowance. Every input required by rule 1 through rule 4 is present. `unknown` fails
`unknown`'s own test ("the documents needed could not be located" — they were located and are quoted in
the record itself).

**Recommended correction, outside the ten formally flagged values, entailed by the same ruling that
leaves the ten alone:**

| Field | Current | Recommended |
|---|---|---|
| `cost_per_output_computable` | `unknown` | `yes` |
| `computation_assumptions` | `not_applicable` | `"Pro tier, ₺83.25/mo billed annually per default display state (rendered read, 2026-08-10; reconfirmed live 2026-08-17 unchanged: '₺ \| 83.25 \| /mo \| Billed yearly' in the page's own payload). per_seat_month output = monthly price directly; no separate allowance to convert. Cost per output = ₺83.25/seat-month. Figure in TRY; no USD figure is published anywhere for Picsart's Pro plan (headline_price_usd=unknown, D-007: both arms failed to find a currency selector or a readable US-crawled capture); this variable's rule does not gate on headline_price_usd's coded value, so the TRY-denominated computation stands (protocol-v1.md 6.5: no rate invented)."` |

Downstream: derived `cost_per_output_value_usd → not_computable`, ₺83.25/seat-month preserved, same
treatment as canva and gptzero.

**Why I am recommending this rather than silently leaving it, even though it is not one of the ten I was
assigned.** Leaving it uncorrected while ruling the other four records `yes` on the identical construct
would mean the same fact pattern gets two different answers depending on which record happened to be
flagged by a mechanical build check — exactly the "same construct, different outcome by accident of
which record got audited" problem `deviations-for-adjudicators.md` and the wider study design exist to
prevent. It is reported here for the correction batch, not applied to any record.

---

## 3. Is any record genuinely incoherent

**No.** Checked individually, not assumed:

- Six of the ten flagged values (`cost_per_output_unit` on all six records) were never in tension with
  anything — the variable makes no price or currency claim, so a non-USD or unresolved
  `headline_price_usd` cannot contradict it. This is a build-heuristic false positive, not a finding
  about any vendor or any coder.
- Four of the ten (`cost_per_output_computable = yes` on aiva, canva, gptzero, ismybrandinai) each rest
  on a complete, published calculation in a real currency (or, for ismybrandinai, a currency-invariant
  zero). None needs an unpublished figure, a secondary-output substitution, or a use-pattern assumption.
  All four are correct as coded.
- The one record where `headline_price_usd = unknown` could have meant "no price anywhere, in any
  currency" (openai-sora) already carries `cost_per_output_computable = unknown` — correctly, and
  without needing this adjudication to say so.
- The one place the corpus actually disagrees with itself (picsart) is not an incoherent record; it is
  a single miscoded value, corrected in §2 above by the same rule applied consistently to canva and
  gptzero.

**The task's framing anticipates a "situation 3, really does look incoherent" case. It does not
materialize in this set of six once the underlying evidence is read.** Every `headline_price_usd =
unknown` instance here turns out, on inspection, to be the 3a pattern (a real price was read; the money
field's US-reader-specific test is what returns `unknown`, not price opacity) rather than the 3b pattern
(no price anywhere). That distinction is not visible from the coded values alone — `unknown` looks the
same regardless of which of the two produced it — which is exactly why this adjudication had to open
the underlying evidence rather than reason from the labels, per `deviations-for-adjudicators.md`'s
standing instruction that a record's neighbouring values, and here its own prose, constrain the reading.

---

## 4. Direction and count

**Ten flagged values: zero change.** All ten are confirmed correct as coded, for the reasons in §2, not
merely left alone by default.

**One value outside the ten changes: picsart's `cost_per_output_computable`, `unknown → yes`.**

**Net direction: toward more determinate values, away from `unknown` — the same direction the queue
item's own framing anticipated for the ten, and the picsart correction pushes further in that direction
than the ten-value preservation alone would have.** Stated plainly because the task requires it stated
plainly: this ruling reduces the study's unknown count by one beyond what "change nothing" would have
done, and it does so by finding an *additional* error the build script's mechanical check could not see
(because picsart's `cost_per_output_computable` was already `unknown`, not a determinate value in
tension with anything — it never tripped the flag).

**The counterweight, stated with the same care.** Reading C3 as currency-neutral is generous on the
*scored, indexed* dimension and simultaneously produces nothing on the *reported, comparable* dimension
for three of the five `yes` records. Once this ruling and its picsart extension are applied: aiva,
canva, gptzero, and picsart each score full credit on item C3 (5 of 5, `yes`) while their derived
`cost_per_output_value_usd` — the field a reader would actually consult to compare "typical cost per
output" across vendors in one table — is `not_computable` for all four. Only ismybrandinai's is a
genuine, populated $0.00. A reader comparing vendors on the derived dollar figure alone would see four
blanks where the coded record shows full marks on disclosure. Both facts are true at once, and both
belong in the paper, not just the favourable one.

**Why the convenient direction does not disqualify the ruling.** §1.4 already argues this from the
evidence; restated here because the task asks for it explicitly at this point too. The load-bearing
fact — protocol §8.3.10 and §9 limitation 12 naming only A1 and A3 — is pre-registered text that
predates the collection of every one of these six records. It was not written to settle this dispute
favourably; it settles it because it already existed and already said this, and I read it rather than
inferred it.

---

## 5. What wave 2 must add

1. **State the currency-neutrality of `cost_per_output_computable` in the codebook entry itself, not
   only inferable from an absence in the protocol's scoring tables.** Right now a coder reading only
   `codebook-v1.md`'s domain-6 section has no way to learn that protocol §8.3.10/§9.12 name only A1 and
   A3 as USD-docked — they would have to notice the *omission* of C3 from a different document's
   argument section and draw the inference themselves. Picsart's coder did not, and produced exactly
   the miscoding this resolution corrects. Add one sentence to the variable's own decision rule: "This
   variable does not require the entry tier's price to be in USD; a calculation complete in the vendor's
   own currency is computable. The dollar-comparable figure is reported separately, in
   `cost_per_output_value_usd`, and is unavailable where the underlying price is not USD." State a test,
   not only the example the codebook already carries — the pattern this study repeatedly finds is a
   coder generalizing correctly from the codebook's one worked illustration and missing that a
   differently-shaped case is governed by the same rule.

2. **Give `cost_per_output_value_usd` an explicit rule for the non-USD-arithmetic case**, confirming and
   generalizing the recommendation `orchestrator/A-001-A-010-A-014-resolution.md` made for canva alone:
   `not_computable` wherever the only available arithmetic is denominated in a currency other than USD,
   *except* where the computed figure is exactly zero, which needs no exchange rate and stands as a
   genuine USD value. This is an instruction for the post-freeze derived-variable computation under
   codebook §8, not a change to any coded value, and does not touch the §11 freeze.

3. **Yes — a derived money variable needs its own currency field**, and the reason is concrete rather
   than principled-in-the-abstract: right now a reader of the published, structured dataset sees
   `cost_per_output_value_usd = not_computable` for aiva, canva, gptzero, and (under the correction
   above) picsart, and has no way to discover from the structured data alone that a complete, correct
   figure exists for each of them — €0.73/download, ₺160.00/seat-month, TRY 1.83/1,000 words,
   ₺83.25/seat-month — without opening the source record's free-text `computation_assumptions` prose.
   Add a paired field (`cost_per_output_value_native` and `cost_per_output_currency`, or equivalent)
   that carries the real number and its currency code whenever `cost_per_output_computable` is `yes` or
   `partial` but the price is not USD. This is the exact parallel of what A-013's own resolution already
   recommends for `headline_price_usd` ("add the currency question… as a second, separate variable, so
   the reproducible measure and the buyer-relevant measure can both be reported instead of one being
   sacrificed to the other") — Domain 6 needs the same fix, for the same reason, and currently lacks it.

4. **Extend rule 1's text to cover the wholly-free, no-paid-tier case explicitly.** The rule as written
   says "the entry **paid** tier's price," which has no antecedent where §7.3 establishes no paid tier
   exists at all. ismybrandinai's coders reached the right answer ($0.00, currency-invariant, the
   strongest possible case) by reasoning from the codebook's exception register ("every product has a
   principal output unit, so item C3 applies to every product") rather than from rule 1's own text,
   which does not name this case. State it directly: a product with no paid tier at all computes at
   $0.00 per output, and that figure requires no currency designation.

5. **Tooling note, not a codebook change.** `tools/build_dataset.py`'s contradiction-detection heuristic
   should stop flagging `cost_per_output_unit` against `headline_price_usd` — the variable makes no
   claim the currency question could contradict, and all six of this item's ten flagged values that
   involve it were false positives for that reason. The heuristic should test only
   `cost_per_output_computable`, and, once (1)-(2) above land in the codebook, should stop flagging that
   too for `non_usd`/`unknown` headlines specifically, reserving the check for genuinely unresolvable
   pairings (a determinate `cost_per_output_computable` alongside a headline that is `unknown` *for the
   3b reason* — no price in any currency — which this build-report sweep did not actually find an
   instance of, but which the heuristic should still be able to catch if a future collection wave
   produces one).

---

## Disclosures

**What I read.** `orchestrator/adjudication-queue.md` (row A-021, and — because the Read tool returns
the whole file and the task directed me to this file — the rest of the queue; I did not act on, and am
not aware of relying on, anything from another row). `deviations-for-adjudicators.md` in full.
`orchestrator/A-013-A-019-resolution.md` in full, as directed. `dataset/build-report.md`'s contradiction
section, then reproduced it myself by running `python3 tools/build_dataset.py`, which returned the
identical ten values. `codebook-v1.md` sections 1-9 (definitions, decision rules, §2's status-value
register, §5.2's entry-tier variable enumeration, §8's derived-variable table). `protocol-v1.md` §6.4-6.7
(archival, currency, mid-window, execution sequence), §7.4-7.6 (adjudication and reliability, for
completeness, though this item is a construct ruling rather than a per-value pass1/pass2 reconciliation
and did not need §7.4.1/§7.4.2's classification machinery), §8.3.2-8.3.10 (the full APTI scoring
apparatus for components A and C), §9 (limitations), §12 (versioning). `sampling-rules.md` §7
(unit of analysis and plan selection) in full. `record-template.yaml` was not needed — this task
produces an orchestrator resolution document, not a record. All six products' own records and source
directories: `records/adjudicated/aiva.yaml`, `records/adjudicated/ismybrandinai.yaml`,
`records/pass1/canva.yaml`, `records/pass1/gptzero.yaml`, `records/pass1/openai-sora.yaml`,
`records/pass1/picsart.yaml` (none of these six has a pass 2 outside the two adjudicated ones, confirmed
by directory listing before reading — canva, gptzero, openai-sora and picsart were single-pass products,
not in the double-coded subsample, so this is each record's first adjudicative review on any variable).

**I read `orchestrator/A-001-A-010-A-014-resolution.md`, which is not one of the files this task
directed me to, and I disclose exactly how and why.** It covers three products, one of which — canva —
is one of my six; the other two — humanizemy-ai-detector and rezi — are not, and I did not open either
of *their* own pass1/pass2/adjudicated records, and nothing in this resolution rests on anything said
about them. I opened this document because its "cascade set" section states, and works through, exactly
the sampling-rules §7.2 currency-agnosticism question this item turns on, for canva specifically, and
because it contains a specific recommendation about `cost_per_output_value_usd`'s non-USD treatment that
is directly on point. **What I verified independently rather than took on that document's authority:**
every quotation from `sampling-rules.md` §7.2 and every quotation from `protocol-v1.md` §8.3.10/§9.12
above was re-read by me from the primary document itself, not copied from that resolution's
characterization — and the §8.3.10/§9.12 evidence, which is the decisive piece of my ruling, is not
discussed in that document at all; I found it independently. **One place that document's characterization
did not match the record it described, which I caught only because I opened picsart's own record rather
than trusting the aside:** it lists "pass1/picsart (₺83.25/mo)" alongside canva and gptzero as if the
arithmetic had already been computed there; picsart's own record shows the coder explicitly declined to
compute anything (`cost_per_output_computable = unknown`, `computation_assumptions = not_applicable`).
That discrepancy is what led me to picsart's `coder_note` and to the correction in §2. A reader should
discount my picsart finding accordingly for exposure, though I believe the finding itself is
independently sound on picsart's own text, checked on its own terms above.

**Not opened:** `orchestrator/interim-signals.md`, `orchestrator/deviations-log.md` (the raw log),
`aitoolspolice.com`, `site/content/reviews/`, any other product's pass1/pass2/adjudicated record, and no
other orchestrator resolution document besides the two named above.

**Live verification performed today, 2026-08-17**, because the task's standing duty is to verify a
cited figure rather than trust the record's account of it:

| Check | Result |
|---|---|
| `aiva.ai/` — €11/€33/€0, "15 downloads per month" | Confirmed live, byte-consistent with all three prior reads (2026-08-06, 2026-08-14, 2026-08-15) |
| `ismybrandinai.com/tools/ai-bot-checker` — "free" | Confirmed live |
| `picsart.com/pricing/` — `₺ \| 83.25 \| /mo \| Billed yearly` (Pro) | Confirmed live, found in the page's own embedded payload; this is the figure my one correction rests on |
| `canva.com/pricing/` via curl | HTTP 403 (bot-walled), consistent with the record's own documented finding; not re-rendered — I am not changing canva's price, and the record's existing evidence already rests on a rendered capture plus a DOM scan and a second locale-path cross-check the record itself performed |
| `gptzero.me/pricing` via curl | HTTP 200 but pre-hydration shell (no "549," no "TRY"), consistent with the record's own documented D-005 finding that this page needs a rendered read; not re-rendered, for the same reason as canva — no value on this record is changing |
| `web.archive.org/` homepage and CDX endpoint | HTTP 200, both — **the brief stated archive.org was in a full outage today; my own checks found it responding normally.** I did not rely on archive.org for any conclusion in this resolution (the load-bearing evidence is codebook/protocol/sampling-rules text and fresh live-vendor reads), so this discrepancy does not affect anything above, but I record it because the brief's premise did not hold when I checked it. |
| One specific memento cited in picsart's own record (`20260810104607`) | 302-redirects to `20260810104533`, 34 seconds earlier, same date — a normal Wayback timestamp-rounding artifact (`x-archive-redirect-reason: found capture at 20260810104533`), confirmed to resolve HTTP 200. This is not the phantom-citation pattern the study has previously caught (a citation redirecting to a capture days off, or to none at all); the target is genuine and adjacent. |

**Nothing in this document has been applied to any record.** The picsart correction in §2 is a
recommendation for the correction batch, stated exactly, not an edit. `git add` and `git commit` below
touch only this file.
