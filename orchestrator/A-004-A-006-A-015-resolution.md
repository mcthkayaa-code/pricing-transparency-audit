# A-004, A-006, A-015 — resolution

**Resolved 2026-08-17.** Three queue items, each a call a coder made deliberately, documented, and
asked to have confirmed. Two are confirmed. One is corrected in part and confirmed in part.

**No record is edited by this document.** Corrections apply later as one batch.

| Item | Variable(s) | Ruling |
|---|---|---|
| A-004 | `cost_per_output_unit` | **CONFIRMED** — `other` (per slide) stands. No value changes. |
| A-006 | product identity | **CONFIRMED** — §10.4 treatment is correct. The dataset prints **Freepik**. No value changes. |
| A-015(a) | `free_plan_duration` + Domain 3 | **CORRECTED** — the Free tier is a 14-day trial, not a free plan. Four values change. |
| A-015(b) | `usage_cap_quantified` | **CONFIRMED on the value, CORRECTED on the basis** — the API clause does not reach the consumer plan; a different, all-users clause does. No value changes. |

**Four coded values change in total, all on one record.**

---

## 0. What this resolution rests on, and what it could not reach

**None of the three records is in the double-coded set.** There is no pass-2 record for decktopus,
freepik or winston-ai, so pass 1 is the only reading each has ever had and the coder's own queue
flag was the only mechanism that would ever have brought a second pair of eyes to these calls. That
is the reason to say plainly, where a call is confirmed, what makes it right.

**Archive.org replay and the CDX index were 503 for this entire run**, exactly as
`orchestrator/post-window-retrieval-2.md` records for earlier the same day: roughly a dozen
attempts across four URLs and both the plain and `id_` replay paths returned the 11,832-byte
"Temporarily Offline" page. The **Memento timemap endpoint stayed up** and was used for enumeration
and for provenance checks. **No archive capture could be read.** Where a coded value needed
verifying, live vendor documents were used and are marked post-window wherever they are relied on.

**Provenance checks performed, since this is the only pass that verifies citations.**

- `pass1/decktopus` cites `web.archive.org/web/20260807033353/.../pricing`. Replay is unreadable,
  but the timemap lists that exact timestamp — `datetime="Fri, 07 Aug 2026 03:33:53 GMT"`. The
  citation is real; it is not a plausibly-dated URL leading nowhere.
- `pass1/winston-ai` has **no archive at all** — every source is `local_copy_only` after the D-012
  archive failures — so none of its quotations had ever been independently verified. Its pricing-page
  quotations were checked against a live read of `gowinston.ai/pricing` and match **verbatim**:
  `2,000 credits / 14 day trial`, `HUMN-1 website certification / 14 day trial`,
  `2,000/14 days | 100,000/month | 200,000/month | 500,000/month`, `Characters Per Scan up to
  200,000` ×3, `Scans Per Hour unlimited` ×3. Every price figure agrees as a number (the live page
  serialises `$ 10.00 / month`, `$ 120.00 / year` where the capture has `$ 10 /month`, `$ 120 /year`;
  a serialisation difference is not a disagreement). Its ToS quotations were checked against the live
  terms and match verbatim.
- `pass1/freepik`'s rebrand observation was checked live: `https://www.freepik.com/pricing` returns
  **HTTP 301, `location: https://www.magnific.com/pricing`**.

**Dating.** The collection window closed **2026-08-13**. The winston ToS carries its own
`Last updated March 18, 2026`, which predates the window close, so the live terms are the
window-era terms; that is what makes A-015(b) decidable on window-era text. The winston help-centre
articles carry no modification date, no sitemap and no capture after 2026-02-21, so their window-era
state cannot be established; they are used only as corroboration, never as the basis of a ruling,
and the counter-signal is disclosed in §3.

**Disclosure.** `deviations-for-adjudicators.md` bars an adjudicator from reading the queue or
another product's record. This assignment is three queue items, so both were read; that is inherent
in a queue-level resolution rather than a breach of the separation's purpose, and it is recorded
here so a reader can weigh it. The three items turn on unrelated constructs — a Domain 6 unit, an
administrative identity field, and Domains 3/4/12 — and no value on one record was used to reason
about another. Nothing outside the three products was opened.

---

## 1. A-004 — decktopus, `cost_per_output_unit`

The coder chose `other` (per slide) over `per_presentation` because the vendor publishes a per-slide
credit rate and states no fixed per-presentation rate.

### 1.1 The rule that decides it

`codebook-v1.md` §7, Domain 6, `cost_per_output_unit`:

> **Definition.** The unit in which this product's principal output is **counted**.
>
> **Decision rule.**
> 1. The principal output is what the product is sold to produce, as its own pricing page frames it.
> …
> 3. Where none of the listed units fits, code `other` and name the unit in `coder_note`.

The variable has two parts and both do work: rule 1 identifies **which output** is principal, and
the definition asks for the **unit that output is counted in**. The enum's own construction shows
the split — a video generator is `per_video_minute`, never "per video"; text is `per_1k_words`,
never "per essay". The listed unit is the metering unit for the principal artifact class.

### 1.2 Ruling: **CONFIRMED**

`per_presentation` is the right value for a vendor that **counts presentations**. Decktopus counts
slides, and nowhere counts presentations.

- The pricing card's own allowance annotation is `750 AI credits / month (~150 slides)`. Verified
  in the record (s1, 2026-08-07) and again on the live page 2026-08-17 as the identical string.
- The comparison grid's only quantified output row is `AI credits included — 750 / mo | 1000 / mo |
  Custom`. The row `Create presentations` is a checkmark, not a count. No plan anywhere carries an
  allowance of N presentations.
- Help article 60, quoted in the record: "how far your credits go depends on how many slides you
  create." The vendor states that a per-presentation figure cannot be fixed, and only the per-slide
  rate (5 credits) is published.
- Post-window corroboration, marked as such: the live pricing page now carries a credit calculator
  whose second input is a **user-supplied assumption** — `Average slides per presentation`, with the
  caption "assumes 10 slides per presentation on average — adjust if yours differ". The vendor asks
  the reader to supply the presentations-to-slides conversion. Whether that widget existed on
  2026-08-07 is unknown and the ruling does not depend on it; it is the clearest available statement
  that the vendor publishes no such conversion.

So `per_presentation` does not fit, the enum has no slide value, and rule 3 returns `other`.
`per_page` was considered and rejected: a slide is not a page, the vendor never calls it one, and
`per_page` is the unit for paginated documents.

**One correction to the coder's reasoning, which does not change the value.** The coder's second
ground — the codebook's Vendor M video example — is not load-bearing and is weaker than the coder
thought. The enum never offered "per video", so that example was forced by the value list rather
than chosen over a whole-deliverable alternative; here the value list *does* offer
`per_presentation`. `deviations-for-adjudicators.md` is explicit that "the codebook's illustrations
of a value never bound it." The value is right on the coder's **first** ground — the vendor's own
metering and its own statement that a per-presentation rate cannot be fixed — read together with
rule 1 and the definition's word "counted".

### 1.3 Coded values that change

**None.** `cost_per_output_unit = other` stands, with `per_slide` named as the record already names
it. `credit_to_output_rate_published = yes`, `cost_per_output_computable = yes` and
`computation_assumptions` ($9.99 ÷ 150 = $0.07/slide) all stand unchanged as consequences of it.

### 1.4 Direction

**Toward the vendor, and the alternative was worse for it.** Had `per_presentation` been coded, the
principal output's rate would have been unpublished and rule 5 would have returned `partial` on
`cost_per_output_computable` — item C3 at 2.5 of 5 instead of 5 (`protocol-v1.md` §8.3.4) — and
probably `partial` on `credit_to_output_rate_published`, item C2 at 3.5 of 7 instead of 7. The
derived `cost_per_output_value_usd` would have become `not_computable` instead of carrying a figure.
So confirming is worth up to 5.5 index points to this vendor, and it is stated because it is worth
that much. It is nonetheless right: the vendor publishes a complete, exact, unqualified rate for the
unit it meters, and a reader can compute a real cost per slide. Marking it down would penalise the
vendor for a gap in **our** value list.

**Neutral on the unknown burden.** No `unknown` is created or removed; `other` is a determinate
value.

### 1.5 For wave 2

1. **Add `per_slide` to the enum**, or restate rule 1 to say outright what it currently only
   implies: the unit follows the vendor's **metering** unit for the principal artifact class, not
   the artifact class's own name.
2. **`other` loses information in the published CSV.** The named unit lives in prose, so a dataset
   row reading `cost_per_output_unit = other` beside a derived `0.07` is uninterpretable without
   reading `coder_note`. Wave 2 needs a companion field — `cost_per_output_unit_other_label` — that
   `validate_records.py` requires whenever `other` is coded.
3. **Post-window observation, no action, disclosed because it was found.** The live pricing page's
   FAQ now reads "Each slide costs 5 credits… The Pro plan includes 750 credits per month, enough
   for roughly 150 AI edits **or 50 new slides**", which contradicts both its own 5-credits-per-slide
   rate and the card's `~150 slides` (750 ÷ 5 = 150). If that text was live on 2026-08-07 it bears on
   `credit_to_output_rate_published`, not on the unit. It cannot be dated — archive replay is down —
   and it is **not** acted on here. Flagged for a dated re-read in wave 2.

---

## 2. A-006 — freepik, product identity across a mid-window rebrand

The vendor rebranded to Magnific mid-window; `freepik.com` 301s to `magnific.com` under the same
legal entity. The coder kept `product_id` and recorded both names.

### 2.1 The rules that decide it

`sampling-rules.md` §10.4, in full:

> 4. A vendor that renames or rebrands a product during the window keeps its `product_id`. Both
>    names are recorded.

`codebook-v1.md` §6, administrative variables:

> | `product_id` | string | Our review slug | **Copied from the frozen frame. Join key across every
> study file.** |
> | `product_name` | string | Product name as the vendor writes it | **Copied from the frozen frame.** |

`codebook-v1.md` §10:

> One row per product per `coder_role`. The published dataset carries the `adjudicated` row where one
> exists and the `primary` row otherwise.

…followed by the column order, which contains **exactly one** name column and ends
`…, conflict_note, coder_note`.

`codebook-v1.md` §11:

> No variable may be added, removed, or redefined after the collection window opens.

### 2.2 Ruling on the treatment: **CONFIRMED**

§10.4 asks for two things and the record does both.

- **`product_id` kept.** The record carries `product_id: freepik`. This is not cosmetic: `freepik`
  is the join key in `frame-frozen-2026-08-04.csv`, `frame-for-pass2.csv`,
  `archive-verification.csv`, `attribution-audit-half2.csv`, `unknown-attribution.csv`, the record
  filename and the sources directory. §10.4 forbids changing it and nothing here invites it.
- **Both names recorded.** `coder_note` carries a dedicated REBRAND paragraph naming both, and
  `register_events` carries a dated entry for it.

The factual predicate was re-verified rather than taken on trust. Live, 2026-08-17:
`https://www.freepik.com/pricing` → **HTTP 301** → `https://www.magnific.com/pricing`; the target's
own `<title>` is **"Pricing plans | Magnific (formerly Freepik)"**; the footer reads "Copyright ©
2010-2026 **Freepik Company S.L.U.**" Two small departures from the record, neither material: the
record says the **root** also 301s, and today `https://www.freepik.com/` returns 403 behind a bot
wall rather than a redirect; and the entity is styled `S.L.U.` (sole-shareholder S.L.) on the live
footer against the record's `Freepik Company, S.L.` Continuity of the legal entity is established
either way, which is what §10.4's "renames or rebrands" turns on — this is a rebrand, not a
successor product, so the frame row survives and the record stays in the wave.

### 2.3 Ruling on the open question: **the dataset prints `Freepik`**

This is the part of the row that was genuinely open, and it has consequences past aesthetics.

**What the dataset prints.** `product_id: freepik`, `product_name: Freepik` — both unchanged. §6
does not leave it to judgment: `product_name` is *copied from the frozen frame*, and the frozen frame
says `Freepik`. The gloss "as the vendor writes it" describes where the frame's value came from at
freeze; it is not a standing instruction to re-derive the field at collection time, and reading it
that way would make an administrative field track the vendor's marketing after the population was
frozen. Printing `Magnific` beside `product_id: freepik` would also desynchronise the dataset row
from the frame row it is drawn from, which is the trip-hazard a replication team meets first.

**Why not a compound string.** `Magnific (formerly Freepik)` — the vendor's own construction — was
considered. It would satisfy "both names are recorded" inside the printed column and answer the
search requirement directly. It is rejected: it is neither the frame's value nor a name the vendor
uses as a name, it breaks any join on `(product_id, product_name)`, and §10.4 asks that both names
be *recorded*, not that both be *printed in one field*.

**What the paper says.** The frame table prints `Freepik`, with a footnote on that row: *rebranded to
Magnific during the collection window; `www.freepik.com/pricing` 301-redirects to
`www.magnific.com/pricing` under the same legal entity (Freepik Company S.L.U.); all coded values
were read from `magnific.com` documents accessed 2026-08-07.* Wherever the paper discusses this
record in prose it uses "Freepik (now Magnific)" on first mention. Dataset and paper then agree, and
the reader is told why a row named Freepik cites magnific.com URLs before she notices it and wonders.

**How the other name stays discoverable — inside the dataset, not only in the paper.** A text search
of the published dataset for `Magnific` returns this row already, four times over, without any new
column: `primary_source_url` and `archive_url` are `magnific.com` URLs, `source_urls` carries six
more, and `coder_note` — which §10 lists as a **published dataset column** — contains the sentence
"banner reads 'Freepik is now Magnific'". A search for `Freepik` returns it via `product_id`,
`product_name` and the same note. Both directions resolve. The requirement the queue names is
therefore already met by the record as coded; what it needs is not an edit but a **guarantee**: the
batch must not compress or drop `coder_note`'s REBRAND paragraph, and the paper's data-availability
note must state that `coder_note` is part of the published dataset and carries former names.

Adding a second name column would be the cleaner answer and is **not available**: §11 freezes the
variable set for wave 1.

### 2.4 Coded values that change

**None.** `product_id`, `product_name`, `category`, `product_status` all stand. Every coded value
stands; the D-007 currency re-code that also lives on this record is A-005's business and is
untouched here.

### 2.5 Direction

**Neutral on both axes.** No index item reads an administrative name field, and no `unknown` is
created or removed. The only thing at stake is whether a reader can find and trust the row, which is
why the ruling is about discoverability rather than about scoring.

### 2.6 For wave 2, and one defect for the batch

1. **Add `product_name_at_collection`** beside `product_name`, with the wave-1 mapping stated:
   wave-1 `product_name` = the frame name = wave-2 `product_name`; wave-2
   `product_name_at_collection` = the name the vendor used on the access date. Then a rebrand needs
   no prose at all, and §10.4's "both names are recorded" becomes a coded fact rather than a
   convention.
2. **`register_events.type` carries an out-of-table value on this record — flagged for the batch,
   and it is not a coded-value change.** `record-template.yaml` fixes the type as
   `vendor_edit|display_variant`; this record's rebrand entry reads `type: rebrand`, and all three
   entries use `date/type/description` keys where the template specifies `type/detail/urls`. This is
   the "values outside a variable's table have reached records and passed every check" failure, and
   it is not harmless: `deviations-for-adjudicators.md` makes a `vendor_edit` entry the *only* thing
   that can support a §7.4 `date_explained` classification, so a rebrand logged as `rebrand` would
   not supply one if this record were ever in a disagreement pass. The batch should re-type it
   `vendor_edit` and keep the rebrand wording in `detail`. Wave 2's register should carry `rebrand`
   as a third type in its own right.

---

## 3. A-015(a) — winston-ai, `free_plan_duration` and the free-plan/trial boundary

The Free tier is described as `2,000 credits / 14 day trial`, while the vendor's own comparison table
notates the same tier `2,000/14 days`, in the rate notation the paid tiers use for `/month`. The
coder read the two as irreconcilable and coded `free_plan_duration = unknown`.

### 3.1 The rules that decide it

`codebook-v1.md` §2.1, the decision tree, applied in order:

> 3. Do two or more official sources state incompatible values? … If they rank equally, code
>    `conflicting` and record both URLs.
> 4. Otherwise, code `unknown`.

`codebook-v1.md` §2, on `conflicting`:

> **Two or more official sources** of equal authority for this variable state incompatible values…

`codebook-v1.md` §7, Domain 3, `free_plan_exists`:

> **Definition.** Whether the vendor documents a plan usable at no cost **and with no time limit
> imposed by a trial**.
>
> **Decision rule.** 1. **A time-limited free trial is not a free plan. It is coded under domain 4.**

`free_plan_duration`'s value table:

> | `not_applicable` | No free plan |

And `orchestrator/A-012-resolution.md` §2, the rule I was directed to apply:

> **`trial_exists` asks whether the vendor documents a time-limited pre-commitment period of access
> to a paid tier. Zero cost is the paradigm case named in the definition, not a condition of the
> construct… The period must end before the plan's first ordinary billing cycle completes.**

### 3.2 Ruling: **CORRECTED**

**First, the coder is right about one thing and it disposes of `conflicting`.** Both readings come
from a single document, so there are not "two or more official sources", and `conflicting` is
unavailable on the technicality that the value's own definition counts sources rather than
statements. The coder said exactly this and was right to refuse it.

**But the two readings are not of equal standing, and once that is seen the ambiguity dissolves.**

1. **The card states a period in words, twice.** `2,000 credits / 14 day trial` and, four lines
   below, `HUMN-1 website certification / 14 day trial`. The recurring reading states nothing: it is
   an *inference* from notational parallelism in one table cell that must express a quantity and a
   window in four characters. The instrument does not let an inference override a stated period —
   it refuses inference repeatedly and by name (`trial_card_required` rule 3; `free_plan_cap_value`'s
   "do not paraphrase an unquantified limit into a number").
2. **The record already reads that phrase the other way, on the same card.** `trial_exists = yes`
   and `trial_length_days = 14` rest on `HUMN-1 website certification / 14 day trial` being a
   14-day time limit on paid-tier functionality. The same four words cannot mean a time limit in
   line 38 of the capture and a recurring cycle in line 33.
   `deviations-for-adjudicators.md`: "A record can contradict itself, and that is evidence… A record
   that codes one value while its own neighbouring values only cohere with the opposite has left the
   evidence for its own correction in place."
3. **The `$0 /year` line is a template slot, not a yearly plan.** The window capture renders the
   Free card `$ 0 /month` + `$ 0 /year` against Essential's `$ 10 /month` + `$ 120 /year`; the live
   page renders three price spans per card (`$ 18 / month`, `$ 10.00 / month`, `$ 120.00 / year` for
   Essential; the same three filled with zeros for Free). Under either rendering the Free card's
   `/year` line is the paid cards' own price slot filled with a zero, emitted for every card by one
   template. No inference about perpetuity survives that.
4. **The Free column is absent from the two rows that describe a standing plan's limits.**
   `Characters Per Scan` and `Scans Per Hour` each carry three values, for Essential/Advanced/Elite.
   The Free tier is given no operating limits at all — consistent with a trial, not with a tier the
   vendor expects anyone to run on indefinitely.
5. **Post-window corroboration, dating caveat and counter-signal disclosed.**
   `help.gowinston.ai/pricing/how-much-does-it-cost` — **already a cited source on this record** —
   states, read 2026-08-17: "You can start with a **free 14-day trial (2,000 credits)** — no credit
   card required. **After the trial you can choose from these plans:**", followed by a table of
   Essential / Essential (Plagiarism) / Advanced / Elite **with no Free row**. That is the sentence
   the record says does not exist ("no FAQ, help article, or homepage text resolves which reading
   governs"), on a page the coder opened but queried with targeted prompts rather than read — the
   "a keyword search is not a reading" failure, in its exact documented form.
   **It cannot be dated into the window**: no capture exists after 2026-02-21, replay and CDX are
   503, the page carries no modification date and the help centre serves no sitemap. Continuity is
   suggested — the coder's 2026-08-13 capture quotes the Elite row of that same table **verbatim**
   ("Everything in Advanced plus HUMN-2 certification, unlimited members, credit top-ups") and
   records that the page gives no price figures and refers readers to `/pricing`, both true today.
   Against that, today's table lists a fifth plan, "Essential (Plagiarism)", that appears on no
   pricing card, and describes Essential as for "teams who don't need plagiarism" while the
   window-era Essential card lists "Advanced plagiarism detection". So the article is **not**
   provably unchanged, and **the ruling does not rest on it.** Points 1–4 are all window-era, all
   from the rank-1 document, all verified verbatim against a live read.

**Now A-012's rule, applied.** A-012 §3 asserted in passing that its rule "has no bearing" on
winston because winston's construct carries no non-zero price. That aside answers the wrong
question. A-012's rule expressly says zero cost is "the paradigm case named in the definition, not a
condition of the construct", so a **zero-cost** 14-day pre-commitment window is not outside the rule
— it is the paradigm inside it. Applying the rule's two tests: is this a time-limited
pre-commitment period of access to paid-tier functionality? Yes — 14 days of HUMN-1 certification
and of a credit allowance, before any commitment, with no card required. Does the period end before
the plan's first ordinary billing cycle completes? Yes — 14 days against a monthly or annual cycle.
It is a trial on A-012's own mechanical test, and the vendor's own word for it is "trial", so the
word-keyed and mechanism-keyed readings agree for once.

`free_plan_exists` rule 1 then routes the construct out of Domain 3 entirely: "A time-limited free
trial is not a free plan. It is coded under domain 4." Domain 4 already holds it.

**On `free_plan_exists = no`, whose value gloss does not literally fit.** The gloss reads "The
pricing page shows paid tiers only, or documents state there is no free plan", and Winston's pricing
page shows a card headed "Free". Neither limb is literally true, and
this is worth naming rather than glossing over. `no` is nonetheless the value: rule 1 is the
operative exclusion, and once the trial leaves Domain 3 no other no-cost, non-trial plan is
documented anywhere, which is what `no` asserts. The gloss describes the paradigm route to `no`, the
same relationship A-012 established between the word "free" in `trial_exists` and that variable's
actual condition. `unknown` was considered and rejected on A-012 §2.3's reasoning: `unknown` is this
study's central quantity and the documents here are not silent — they characterise the construct
twice, in words, on the highest-ranked source.

### 3.3 Coded values that change

Four, all on `pass1/winston-ai`. The first is the queue's variable; the other three are the values it
cannot move without, since `not_applicable` on a Domain 3 variable means "no free plan" and that
statement lives in `free_plan_exists`.

| Variable | Current | New |
|---|---|---|
| `free_plan_duration` | `unknown` | **`not_applicable`** |
| `free_plan_exists` | `yes` | **`no`** |
| `free_plan_cap_documented` | `all_quantified` | **`not_applicable`** |
| `free_plan_cap_value` | `2000 credits per 14 days` | **`not_applicable`** |

**Values that hold, checked rather than assumed.**

- `free_plan_watermark` — `not_applicable` holds, and its **evidence must be restated**: the reason
  is now "no free plan", the first limb of its own value table, not the output-type argument. That
  incidentally puts this record beyond the reach of the A-018 precedent, which contested the
  output-type limb for text-producing products; here the no-free-plan limb applies independently.
- `trial_exists` — `yes` holds, but its **basis broadens** from the narrow HUMN-1 line to the whole
  Free tier, and its evidence should quote `2,000 credits / 14 day trial` as well.
- `trial_length_days` — `14` holds. Stated twice on the card.
- `trial_card_required` — `no` holds, and is now better supported, not worse: "No credit card
  required" is a vendor **statement** paired with the same "Get started free" call to action the
  Free card carries, which is `trial_card_required` rule 2's documented `no`. This is not the
  myperfectresume inference A-012 corrected — nothing is being inferred from a charge.
- `trial_auto_converts` — `unknown` holds. "After the trial you can choose from these plans" plus
  "no credit card required" is the nearest thing to a denial in the documents, but the codebook gives
  `yes` a wording test and no mirror test for `no`, and reading a denial out of a sequence
  description is the inference `trial_card_required` rule 3 bars in the same domain. Descriptive
  variable, no index item, so nothing turns on it.

### 3.4 Direction

**Toward the vendor, and against this study's unknown burden. Both, and neither is marginal.**

- **Unknown burden: −1.** `free_plan_duration` leaves the `unknown` set for `not_applicable`, which
  is removed from the denominator rather than scoring zero. This record's `unknown` count goes 4 → 3.
  §2.2 warns that getting this boundary backwards "would convert the study's central finding into a
  rounding error", so a correction running in this direction has to carry its argument in full, which
  is why §3.2 is as long as it is.
- **Index: B1 unchanged, B2 removed.** `protocol-v1.md` §8.3.3.1 scores `yes + all_quantified` at 5
  and `no + not_applicable` at 5, so **B1 does not move**. B2 currently scores 3 of 5 — one
  determinate sub-variable (`free_plan_watermark`, via rule G4) and one `unknown` — and is
  non-determinate under §8.3.1's item-level definition. After the correction both sub-variables are
  `not_applicable` and, per §8.3.3's B2 row, "the item is `not_applicable`, and removed… which is the
  no-free-plan case." Dropping an item
  the vendor scored 60% on raises its `apti_total` and its `determinability_rate`.
- **I took the less vendor-favourable of the two ways to give effect to the 14-day reading.** The
  alternative — keeping `free_plan_exists = yes` and coding `free_plan_duration = time_limited`, the
  codebook's "free for your first month" route — would score B1 5 **and** B2 5, both sub-variables
  determinate. That is better for the vendor than what I have ordered. It is unavailable because
  `free_plan_exists` rule 1 excludes a trial from Domain 3, and because the same 14 days would then
  be coded twice, as a free plan's expiry and as a trial.

**The finding that goes in the paper beside the score.** Winston presents a 14-day trial as a fourth
plan **column**, headed "Free", carrying `$0 /month` and `$0 /year` price lines in the same
three-span template the paid cards use — while its own help centre says you start with a free 14-day
trial and choose a paid plan afterwards. (The live page additionally badges that card "Most Popular",
inside the card's own `card-head` markup. The window-era capture does not show the badge, so it may
be a post-window addition; the finding does not use it.) The audit's score goes **up** because the
time limit is disclosed on the card, in words; the presentation finding is recorded because a shopper
scanning four columns reads a fourth tier, not a countdown. Those two facts belong in the same
paragraph. Reporting only the first would flatter the vendor; reporting only the second would
misstate our own instrument.

### 3.5 For wave 2

1. **`conflicting` must be reachable for a single self-contradicting document.** Its definition
   counts *sources*, so a vendor that contradicts itself twice on one page is unreachable by the one
   value built for contradiction, and the coder is pushed to `unknown` — which attributes to silence
   a defect that was actually a statement made twice. Wave 2 should define `conflicting` over
   incompatible **statements of equal authority**, whether or not they sit in one document.
2. **The `unknown` kinds register needs a fourth kind.** `unknown-attribution.csv` and its overrides
   file record this value's kind as `vendor_silence`, hand-assigned, reasoning that the vendor
   "though addressing the topic twice, never commits to either". **That attribution is confirmed as
   the least-wrong of the three available kinds** and should not be moved: relabelling it
   `instrument_gap` would shift a vendor-caused defect onto our instrument, which is the
   vendor-favourable direction, on a technicality about which of two true things to record. But
   neither kind is the truth. Wave 2 should carry `vendor_self_contradiction`, and this record is the
   corpus's worked example of it. Under the correction above the row leaves the unknown-attribution
   file entirely, so the fix is for wave 2, not for the batch.
3. **`free_plan_exists = no` needs a value gloss that covers the trial-presented-as-a-tier case**,
   so a coder is not forced to reach the right value through a false antecedent.

---

## 4. A-015(b) — winston-ai, `usage_cap_quantified` and a clause scoped to one access method

"Scans Per Hour: unlimited" is advertised on the Essential (entry) tier. The ToS fair-use/rate-limit
clause sits in a section headed "API Users". The coder coded `some_quantified` rather than treating
the tier's "unlimited" as clean, reasoning that "API access is bundled into the Essential tier, and
the 'unlimited' scans-per-hour claim is not demonstrably clean of this clause".

### 4.1 The rules that decide it

`codebook-v1.md` §7, Domain 12, `usage_cap_quantified`:

> **Decision rule.**
> 1. List every limit the documents attribute to **the entry paid tier**.
> 2. A limit is quantified when it carries a number and the dimension that number counts, plus a
>    period where the limit is a rate…
> 3. **"Unlimited" counts as quantified only where no clause elsewhere qualifies it.** Where a
>    fair-use clause qualifies an unlimited claim, the limit is not quantified, and
>    `unquantified_limit_clause` also records the clause.

And `unquantified_limit_clause` rule 3, which supplies the boundary of what counts as a usage clause
at all:

> 3. A prohibition on illegal or abusive content is not a usage limit and does not trigger `present`.
>    **This variable covers volume and intensity of use, not conduct.**

### 4.2 Ruling: **the value is CONFIRMED; the basis is CORRECTED**

**The queue's question, answered directly: no. A clause scoped to one access method does not qualify
a cap advertised on the consumer plan.** ToS §18 is headed "API Users — Obligations and Disclaimer",
its operative sentence conditions "continued use of **the API**", and the section's neighbouring
obligations are addressed to API users alone ("API users may not resell, sublicense, or
redistribute…"). Rule 1 scopes the exercise to limits "the documents attribute to the entry paid
tier", and nothing in the window-era documents attributes API access to Essential: the Essential
card's extractable feature list has no API line, and the record's own capture marks the comparison
grid's remaining rows "[feature-grid rows below are checkmark/cross icons, not extractable as text]"
— so the coder's premise rests on a grid cell nobody read. Post-window corroboration, marked as such: the vendor's own help
centre states that the API is a separate surface with separate credentials — "Accounts are separate
on purpose: your web-app username and password won't open the developer portal, and an API key won't
sign you in to the app." The coder's stated ground therefore fails, and the phrase "not demonstrably
clean of this clause" inverts rule 3's burden — the rule requires a clause that **does** qualify the
claim, not the absence of proof that none does.

**The value nonetheless stands, on a clause the coder never cited.** Reading the terms end to end —
which `unquantified_limit_clause` rule 1 requires and which is also the only way to answer this
question — the ToS carries an **all-users** clause with an unquantified volume standard. §14, Site
Management:

> We reserve the right, but not the obligation, to: … (3) in our sole discretion and without
> limitation, refuse, **restrict access to, limit the availability of**, or disable … any of your
> Contributions or any portion thereof; (4) in our sole discretion and without limitation, notice, or
> liability, to remove from the Site or otherwise disable all files and content that are **excessive
> in size or are in any way burdensome to our systems**; and (5) otherwise **manage the Site** in a
> manner designed to … facilitate the proper functioning of the Site.

Limb (4) is a volume-and-intensity standard, not a conduct standard, so `unquantified_limit_clause`
rule 3's carve-out does not reach it. And it bites on precisely the dimension left "unlimited": the
vendor has **quantified** the size dimension on the pricing page ("Characters Per Scan up to
200,000") and the throughput dimension is exactly what "in any way burdensome to our systems"
reserves discretion over. An Essential buyer's "unlimited scans per hour" is therefore not clean of
an unquantified clause, and rule 3 returns `some_quantified` — one quantified rate (100,000
credits/month), one quantified standing limit (200,000 characters/scan), one qualified "unlimited".

This clause is **window-era**: the terms carry `Last updated March 18, 2026`, and the record's own
quotations from the refund, auto-renewal, cancellation, prohibited-use, currency and §18 passages all
match the live document verbatim. Nothing here depends on a post-window reading.

**Clauses I declined to rest this on, because the rule would otherwise be vacuous.** §16 ("DENY
ACCESS TO AND USE OF THE SITE … TO ANY PERSON FOR ANY REASON OR FOR NO REASON, IN OUR SOLE
DISCRETION") and §17 ("modify or discontinue all or part of the Site without notice") are
termination-and-availability boilerplate present in nearly every ToS in the frame. If those qualified
an "unlimited" claim, **no vendor could ever earn `all_caps_quantified` on one**, and rule 3 would be
a tax on boilerplate rather than a measurement. The discriminating test used here, and offered to
wave 2: a clause qualifies an advertised allowance only where it **governs the quantity or intensity
of permitted use**. §18 does, for API users only. §14(4) does, for everyone. §16 and §17 do not.

### 4.3 Coded values that change

**None.** `usage_cap_quantified = some_quantified` stands. `unquantified_limit_clause = present`
stands unchanged and needed no scope argument at all: that variable asks "whether official documents
condition use on a standard that carries no number" and is not tier-scoped, so the API clause
supports `present` on its own. This is the F1/F2 split working as `protocol-v1.md` §8.3.10 designed it —
F2 catches the clause wherever it lives, F1 asks only about the entry tier's own limits.

**One evidence correction for the batch, not a value change.** `usage_cap_quantified`'s evidence and
the `USAGE_CAP_QUANTIFIED judgment call` paragraph in `coder_note` should cite ToS §14(4) as the
qualifying clause and record that §18 is scoped to API users and does **not** reach the entry tier.
`unquantified_limit_clause`'s evidence should cite §14(4) alongside §18, since the all-users clause
is the stronger warrant for `present`.

### 4.4 Direction

**Against the vendor, relative to the correction I nearly ordered.** On the coder's stated basis
alone the value would have moved to `all_caps_quantified`, worth **+3 index points** (F1: 6 for
`all_caps_quantified`, 3 for `some_quantified`, `protocol-v1.md` §8.3.7). Reading the terms to the
end found a clause that holds the markdown, so the vendor keeps 3 of 6 rather than gaining 6 of 6.
**Neutral on the unknown burden** — both candidate values are determinate; no `unknown` moves either
way.

### 4.5 The top-up conflict: does it bear on this ruling?

The record logs, and the queue expressly excludes from adjudication, a pricing-page-versus-help-centre
conflict on credit top-up eligibility (all four tiers per the pricing page, Elite-only per two help
articles). **Left as logged, and it does not bear on (b).** Top-up availability is an extension
mechanism, not a limit: Essential's allowance reads "100,000 credits/month" and carries a number
whether or not the buyer may purchase more. Nothing in rule 1's list of limits changes.

It bears on (b) in one indirect way worth recording, because it is the reason the two calls on this
record needed one rule rather than two. Both are the same structural pattern — **the pricing page's
tier cards attribute a capability to Essential that the vendor's other documents scope narrowly**,
to Elite in the top-up case and to API users in the clause case. The coder resolved one by importing
the narrow scope into a coded value (marking Essential down for an API clause) and the other by
logging the divergence and coding nothing. This resolution makes them consistent: **read each
document's own scope, code from it, and log the divergence** — which for top-ups is what the record
already does, and which §6.2 would in any case resolve on the pricing page's side for a pricing
variable, with the disagreement reported as a finding in its own right. `conflict_note` is correctly
populated and the record should be counted in the paper's tally of marketing-versus-documentation
divergences.

### 4.6 For wave 2

1. **Rule 3 needs a scoping test and a burden.** Two defects, both visible on this one record. It
   should say which clauses can qualify an advertised allowance — those governing the **quantity or
   intensity of permitted use**, and applying to the tier being coded — and it should state that a
   coder who has read the terms in full and found no such clause codes `all_caps_quantified`. As
   written, "only where no clause elsewhere qualifies it" asks for a universal negative over a corpus
   of legal documents, which is what pushed a careful coder into a precautionary markdown on an
   unread premise.
2. **The corpus should be swept for the same shape**, by the orchestrator rather than here: any
   record whose `some_quantified` or `none_quantified` rests on a clause scoped to an access method,
   a plan, or a surface the entry tier does not use. I have deliberately not opened another
   product's record to check.

---

## 5. Owner review

The substantive choice is §3 — a four-value correction that reduces this study's headline quantity by
one `unknown` and removes an index item a vendor was scoring 60% on. Its argument is stated at length
because of that direction, and the two window-era facts it stands or falls on are verifiable in
minutes: the Free card says "14 day trial" twice, and the record's own `trial_exists` reads the same
phrase as a 14-day limit. §4's ruling is the mirror image — the coder's reasoning failed and the
value survived anyway — and its §4.2 test for which clauses may qualify an "unlimited" claim is the
part most open to disagreement, since a stricter test would hand this vendor 3 more points and a
looser one would deny the whole frame a clean "unlimited". §§1 and 2 confirm; neither costs the study
anything and both are recorded so that a reader of the paper knows the check happened.
