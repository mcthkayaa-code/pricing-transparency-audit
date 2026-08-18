# A-018 — the watermark carve-out, and what it does not cover

**Resolved 2026-08-17. Third reading of `humbot`, plus a value-driven enumeration of every
`not_applicable` on the two watermark variables across the corpus.**

The queue raised A-018 as a consistency question and deliberately left it open: two adjudicators had
read the `not_applicable` carve-out narrowly on products they examined, one further record carried the
reading they rejected, and applying their conclusion by hand to a record neither had opened would
have made a precedent into an administrative act. This is the reading that record never got.

Nothing below edits a record. Corrections are applied later as one batch under one rule.

---

## 1. Ruling on `humbot.watermark_removal_tier`

> **`not_applicable` → `unknown`.** The carve-out does not reach this vendor's output. Confirmed
> independently, not adopted from the precedent.

The clause at issue is codebook Domain 11, `watermark_removal_tier`, decision rule 3:

> `not_applicable` where the principal output is not a media artifact a watermark could mark, for
> example a detection score or an analysis table.

The record's coder read "media artifact" as excluding text and reasoned by analogy to the two
examples: principal output is "plain rewritten text (AI Text Humanizer), not a visual/audio media
artifact... text rewriting is analogous". Five grounds defeat that, in descending order of weight.

**(a) A vendor in the same category, with the same output type, publishes a position on it.**
`phrasly` is an AI humanizer — humbot's own category, the same rewritten-text output — and its
pricing page carries the FAQ *"Will my texts be watermarked in the future? No."*, with both plan
cards listing "Watermark and future proof" as an included feature. This study codes that
`watermark_removal_tier = no_watermark` and `free_plan_watermark = no`: two determinate values.
`undetectable-ai`'s plan cards carry the identical "Watermark and future proof" phrase. Rule 3 asks
whether the output is the kind of thing a watermark could mark. A construct that a direct competitor's
documents affirmatively resolve, in standard category vocabulary, is not a construct incapable of
existing for the output type. Humanized text passes rule 3's test on documentary evidence from inside
this corpus. This ground alone settles the item, and it is independent of both prior rulings.

**(b) The protocol states the same test without the qualifier the coding leaned on.** Protocol §8.3,
item E2:

> `not_applicable`, where the principal output is not **an artifact** a watermark could mark: item
> removed.

The codebook says "media artifact"; the protocol says "an artifact". Rewritten text is an artifact.
The single word "media" is the whole of what the `not_applicable` coding rests on, and the scoring
surface that decides E2's index membership does not carry it.

**(c) The two worked examples cannot bear the weight put on them.** A detection score and an analysis
table are both text-shaped. Were rule 3's test "output is text", the examples would be superfluous —
the drafter would have written "where the principal output is text" — and this study's humanizer,
detector, resume-builder and writing categories would all have left item E2 silently, without the
codebook saying so. What actually unites the two examples is that neither is a deliverable the buyer
takes away: each is a read-out *about* an artifact the buyer already had, so there is nothing leaving
the vendor's system whose provenance a mark could assert. Humbot's humanized text is the opposite —
it is the entirety of what the buyer pays for and carries away.

**(d) The record contradicts itself between its two watermark variables.**
`free_plan_watermark`'s `not_applicable` row carries the same output-type limb: *"No free plan, or
the output type cannot carry a watermark."* Humbot's coder had that limb available, declined it, and
coded `unknown` with the evidence "Not addressed anywhere in the documents read." Same product, same
output, same construct, same silence, two opposite answers. One is wrong, and it is not the one §2.2
endorses.

**(e) §2.2 settles any residue.** The record's own evidence field concedes the silence: "Confirmed
silent in every document read (pricing page, feature-comparison table, ToS, refund policy) — the word
'watermark' appears nowhere." I re-swept all four of this record's local captures
(`records/pass1/humbot-sources/`) for the construct's synonyms beyond the literal keyword —
brand/branding, logo, "powered by", attribution, white-label — and found nothing bearing on output
marking; the only hits are the pricing page's "83% OFF" promotional badge and the coder's own prose.
That is a completed read returning genuine vendor silence, not a failed search. §2.2 makes silence
`unknown`, and names the exact cost of getting it backwards: `unknown` scores zero in the index while
`not_applicable` leaves the denominator.

### The argument I checked and then discarded

Humbot codes `commercial_use_lowest_tier = not_granted` (ToS: "you will not use the Website and/or
Services for a commercial activity") and `output_ownership_statement = unknown`. Both presuppose an
output that rights attach to, which looks like it should settle E2 by internal consistency. It does
not. E2's carve-out is scoped to whether the **principal output** is a markable artifact; E1's and
E3's are scoped to whether **any** rights-bearing output exists at all — a distinction the codebook
draws explicitly (E3: "the same test `commercial_use_lowest_tier` applies") and one that `aiclicks`'
pass-2 coder identified unprompted. Two records in this corpus, `brandcited` and `copyleaks`,
legitimately hold E2 `not_applicable` alongside fully determinate E1 and E3. The inconsistency is
corroborative at most. Recorded because a resolution resting on an argument its own corpus refutes
would be worse than none.

### A humbot-specific fact that makes the carve-out a poor fit here

Humbot bundles both kinds of output: an AI Checker and an AI Image Detector, which *would* fit rule 3,
alongside the AI Text Humanizer, which does not. Rule 3 is principal-output-scoped, and this record's
own coding fixes the principal output as the Humanizer — `cost_per_output_unit = per_1k_words`, keyed
throughout to "AI Text Humanizer, the product's namesake function". The one output that could have
supported the carve-out is precisely the one rule 3 directs the coder away from.

### A counter-signal the queue did not report

The queue describes the precedent as two adjudicators. Checking it found a third ruling on the same
clause the same day, pointing the other way, and the picture is more mixed than the queue implies.

- **`anomaly-ai` (adjudicated 2026-08-16)** characterises corpus practice as: *"not_applicable in this
  dataset is reserved for a bare score/report/**plain-text-rewrite** output (sapling, originality,
  copyleaks, gowinston, humanizemy's detector, ismybrandinai)."* That sentence would put humbot's
  value in the legitimate bucket. It does not survive checking. None of the six products it cites is a
  text-rewrite product — all six are detectors or auditors, so the phrase has no referent in its own
  citation list. The list is illustrative rather than a sweep: it omits four other `not_applicable`
  records (`aiclicks`, `apify-robots-checker`, `brandcited`, `gptzero`) and humbot itself, so that
  adjudicator did not have this record in view. And the ruling it supports concerns dashboards, PDF
  and Slides exports, where the phrase does no work. It is dictum, and it is wrong — but a later
  reader should know it is there.
- **`undetectable-ai` is a weaker precedent than the queue implies.** Its `watermark_removal_tier` was
  never `not_applicable`: both passes agreed `unknown` on an ambiguous vendor phrase. What its
  adjudicator moved was `free_plan_watermark`, and that `not_applicable` rested on a mistaken
  "no free plan" premise rather than on the text/media carve-out. Its operative sentence — "no
  document states whether free/Basic-tier output carries vendor branding or a watermark. Silence, not
  documented absence" — does treat text output as watermark-capable, so it corroborates. It is not a
  reasoned ruling on rule 3.

`humanizemy` is therefore the only squarely reasoned precedent on this clause. That makes this third
reading more load-bearing than the queue assumed, not less, which is the argument for having done it.

---

## 2. Every `not_applicable` on the two watermark variables

Enumerated across all **76 effective products** (adjudicated record governs where one exists, pass 1
otherwise; 76 × 37 coded variables = 2,812 coded values). All 76 carry a value on both variables — no
gaps — so this is exhaustive rather than merely broad. **29 `not_applicable` values** in total.

### `free_plan_watermark` — 18 values, all legitimate

The variable's own row licenses two routes: *"No free plan, **or** the output type cannot carry a
watermark."*

**Route 1, no free plan (11).** Each carries `free_plan_exists = no`, mechanically checkable:
`aiclicks`, `copyleaks`, `d-id`, `hostinger`, `hyperleap`, `midjourney`, `plus-ai`, `revid-ai`,
`shortsfaceless`, `squarespace`, `xseek`.

**Route 2, output is a read-out; a free plan does exist (7).** All are detectors or crawler /
brand-visibility auditors whose principal output is a probability score or an audit table:
`apify-robots-checker`, `brandcited`, `gptzero`, `humanizemy-ai-detector`, `ismybrandinai`, `sapling`,
`winston-ai`.

### `watermark_removal_tier` — 11 values, 10 legitimate and 1 over-extended

This variable has **no free-plan limb at all**. Rule 3's output-type test is its only route to
`not_applicable`.

| Product | Category | Principal output | Verdict |
|---|---|---|---|
| `aiclicks` | AI bot checker | visibility / citation-tracking analytics | legitimate — see note |
| `apify-robots-checker` | AI bot checker | structured robots.txt audit rows | legitimate |
| `brandcited` | AI bot checker | AI Search Health score + audit report | legitimate — see note |
| `copyleaks` | AI detector | detection / assessment report (ToS §7.1) | legitimate |
| `gptzero` | AI detector | AI-probability score + highlighted-text analysis | legitimate |
| `humanizemy-ai-detector` | AI detector | percentage score + per-pattern table | legitimate |
| **`humbot`** | **AI humanizer** | **rewritten text (AI Text Humanizer)** | **over-extended** |
| `ismybrandinai` | AI bot checker | crawler-by-crawler allow/block table | legitimate |
| `originality-ai` | AI detector | detection score / report | legitimate |
| `sapling` | AI detector | probability score + per-sentence breakdown | legitimate |
| `winston-ai` | AI detector | detection score / PDF report | legitimate |

I checked the two nearest the line rather than passing the set on category:

- **`aiclicks`** — its own pass-2 coder flagged that the product also generates "AI-optimized
  articles", a genuine text deliverable, and wrote that a reader weighing articles as principal
  "would reach `watermark_removal_tier = unknown`". The value holds because rule 3 is
  principal-output-scoped and this record fixes the principal output elsewhere as the tracking
  analytics — "brand tracked per month" is what the price scales on. Both passes agreed independently,
  which is why no adjudicated record exists. It stands on the principal-output rule alone: if wave 2
  revisits which output is principal here, this value moves with it.
- **`brandcited`** — its output roster includes a "shareable score report", which reads like a
  deliverable. It is not. `cost_per_output_unit` is "brand tracked per month", with the record
  expressly ruling out every artifact unit, and ToS §8 reserves vendor ownership of "any reports or
  outputs generated by our system" granting only an internal-use licence. A vendor-owned monitoring
  read-out licensed for internal use is the paradigm rule-3 case, not its edge.

The other eight meet rule 3's worked example on its own terms. One framing dependency worth recording:
`sapling` ships a writing assistant as well as a detector, and its `not_applicable` holds because this
study frames the product as the detector and codes the principal output accordingly.

### Corpus practice confirms the work-product / read-out line, not a text / media line

Every one of the ten legitimate values is a detector or an auditor. Not one is a product that hands
the buyer a text deliverable. Products whose principal output is text a buyer keeps are coded
`unknown` on documented silence throughout — all six AI resume builders, and four of the six AI
humanizers, including two adjudicated ones. Were "text is exempt" the operative reading, those ten
records would all be `not_applicable` and `phrasly`'s two determinate values would be unreachable.
Humbot is the sole exception in its own category.

---

## 3. Did the queue's coverage claim hold?

**Split verdict: the conclusion held, the stated reason did not.**

**The conclusion held.** All 28 non-humbot values are the legitimate case. Exactly one record is
over-extended and it is the one the queue named. No record that nobody had looked at turned out to be
wrong. Tested by enumerating all 76 products' values on both variables directly, not by re-reading
the sweep.

**The stated reason failed.** The queue gave one: *"Every other `not_applicable` on these variables
across the corpus is the legitimate case: no free plan exists, so the variable does not apply."* That
accounts for **11 of the 28**. The other **17** rest on the second limb — the output-type carve-out —
which the queue's sentence does not mention. For `watermark_removal_tier` the stated reason is not
merely incomplete but structurally impossible: that variable has no free-plan clause, so none of its
ten legitimate values could ever have rested on the absence of a free plan. Two of them (`aiclicks`,
`copyleaks`) happen to have no free plan, which is irrelevant to this variable.

This matters beyond bookkeeping, because the description is what a later reader would re-run the check
against. A re-verification driven by the queue's wording would look for missing free plans and would
pass over the seventeen values that actually turn on the harder question. Relatedly, the sweep is
described as covering "every media-output product": read literally that scope could not have reached
humbot, a text product, nor the seven read-out products. The enumeration above was category-blind and
value-driven, which is the scope the claim needs.

---

## 4. Net effect on the study's numbers

**One value changes.**

| Record | Variable | From | To |
|---|---|---|---|
| `records/pass1/humbot.yaml` | `watermark_removal_tier` | `not_applicable` | `unknown` |

Nothing else. The evidence field must be rewritten to record the silence rather than the carve-out,
and the ruling appended to `coder_note`, but those are documentation of the one value change, not
further changes. Humbot's `free_plan_watermark` is already `unknown` and stays — the queue was right
about that. Humbot is not double-coded, so pass 1 is the published row and there is no adjudicated
record to reconcile.

**Corpus distributions, n = 76.** `watermark_removal_tier`: `unknown` 38 → **39**, `not_applicable`
11 → **10**; `lowest_paid` 21, `never_removed` 2, `mid_tier` 2, `no_watermark` 2 all unchanged.
`free_plan_watermark`: unchanged at `unknown` 38, `yes` 19, `not_applicable` 18, `no` 1.

**Direction: against the vendor, on all three headline quantities.** For humbot, item E2 stops being
an inapplicable item and becomes an applicable item that scores zero.

- `unknown_count` **+1**. E2 becomes an applicable item whose item-level value is `unknown`.
- `determinability_rate` **falls**. `not_applicable` is determinate under rule G0, but an item removed
  under G2 "enters neither side of this ratio"; the recoded item enters the denominator as
  non-determinate. `determinate_items` unchanged, `applicable_items` +1.
- `apti_available` **+3**, `apti_earned` **+0** — E2's maximum is 3 and `unknown` scores 0 — so
  `apti_total` falls.
- Corpus-wide, item E2 moves from 65 products' index into 66.

Item B2 is untouched: it scores from `free_plan_watermark` and `free_plan_duration`, both already
`unknown` on this record.

**Magnitude, stated plainly.** One value in 2,812. It will not move any corpus-level aggregate to a
visible decimal, and it lowers exactly one product's score. It is worth doing because the study's
claim to measure the unknown burden honestly rests on `not_applicable` never being a place to park an
unanswered question — and because the direction is the one that costs the vendor, which is the
direction a study of this kind is most tempted to leave alone.

---

## 5. Note for wave 2: the carve-out needs a test, not an example

Rule 3 states its condition once and then illustrates it, and the illustration is doing work the
condition should be doing. "Not a media artifact a watermark could mark" invites the media/text
reading, and it was taken: three independent coders reached `not_applicable` on a genuine work-product
output through this clause — `humbot` pass 1 and `humanizemy` pass 1 on rewritten text, `anomaly-ai`
pass 2 on dashboards, PDF and Slides exports — and a fourth reader, `anomaly-ai`'s adjudicator,
endorsed the loose reading in passing. Two adjudicators caught it. A clause that four of this study's
readers took the wrong way is a reliability defect in the instrument, not a run of coder error, and
the defect is diagnosable: the protocol's own E2 scoring row states the same condition without the
word "media", and both of the codebook's worked examples are themselves text-shaped, so a coder who
reads the examples closely reaches one answer while a coder who reads the condition's adjective
reaches the other. Wave 2 should drop the adjective and promote the examples into a test the coder
applies to the vendor rather than to the output's file type — on the order of: `not_applicable` only
where the principal output does not leave the vendor's system as an artifact the buyer keeps and
reuses, so no vendor mark could travel with it; and where any vendor in the same category publishes a
watermark or branding position on the same output type, that fact alone establishes the construct
exists and the value is `unknown` at worst. The second clause is the one that would have caught humbot
mechanically, since `phrasly`'s FAQ answers the watermark question for humanized text in the same
category. The instrument is frozen for wave 1 under codebook §11, so none of this changes wave 1's
rules; it changes one wave-1 value that the rules as written already required.
