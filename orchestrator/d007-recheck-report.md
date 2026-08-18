# D-007 currency re-check sweep — report

Ran 2026-08-10, inside the open collection window, per deviations-log.md D-007 and the
amended "Currency check" rule in `.claude/agents/research-data-collector.md`. Scope: the
six pass-1 records that carried `non_usd` on at least one currency variable —
`aiva`, `canva`, `framer`, `freepik`, `gptzero`, `phrasly`. Each was re-checked arm by arm
(vendor's own currency disclosure, then a US-crawled archive capture), never re-derived
from scratch, and every original coder judgment was preserved in place rather than
overwritten.

## Results

| product_id | value before | value after | which arm settled it | evidence file |
|---|---|---|---|---|
| aiva | `non_usd` (EUR 11/mo) | `non_usd` (confirmed) | Arm 2 — US-crawled web.archive.org capture, content-bearing, shows EUR only, zero "$" | `records/pass1/aiva-sources/d007-currency-recheck-2026-08-10.txt` |
| canva | `non_usd` (TRY 1,920/yr) | **`unknown`** (was briefly re-confirmed `non_usd` the same day, then corrected — see "canva re-examination under corrected wording" below) | Arm 1 — same help article, re-read against the wording D-007 actually specifies ("a US reader"), not the reader this study's network happens to be; Arm 2 still returns nothing readable | `records/pass1/canva-sources/d007-currency-recheck-2026-08-10.txt` |
| framer | `non_usd` (TRY 231/mo) | **`10.00`** USD/mo (first charge `120.00`) | Arm 2 — this record's own previously-uncoded archive capture, content-rich, shows $10 Basic at the identical DOM position/credit-tier/toggle state as the TRY reading, 23.10x ratio holds across three tiers, confirmed in raw HTML | `records/pass1/framer-sources/d007-currency-recheck-2026-08-10.txt` |
| freepik | `non_usd` (TRY 450/mo) | **`14.50`** USD/mo (first charge `174.00`) | Arm 2 — this record's own already-archived capture (never previously opened) shows $14.50 Premium, same tier/description/credit-allowance as the TRY reading, corroborated across three tiers | `records/pass1/freepik-sources/d007-currency-recheck-2026-08-10.txt` |
| gptzero | `non_usd` (TRY 549/mo) | **`unknown`** | Arm 1 returned a real but incomplete signal — ToS: "All payments shall be in U.S. dollars" (a currency, not a figure); Arm 2 re-confirmed no readable price exists anywhere | `records/pass1/gptzero-sources/d007-currency-recheck-2026-08-10.txt` |
| phrasly | `non_usd` (TRY 524.43/mo) | **`unknown`** | Same pattern as gptzero — ToS: "All payments shall be in US dollars" (no figure for the Unlimited tier); Arm 2 re-confirmed on the original capture and on a same-day capture newer than the original check had | `records/pass1/phrasly-sources/d007-currency-recheck-2026-08-10.txt` |

`headline_price_usd` and `first_charge_amount_usd` moved together in every record (both
stayed `non_usd`, both became a money value, or both became `unknown` — never a mixed
outcome). Where a value changed to a real USD figure (framer, freepik), the dependent
cost-per-output computation was recomputed in USD and the superseded TRY arithmetic is
kept in the record's history, not deleted. Where a value changed to `unknown` (gptzero,
phrasly), the cost-per-output computation was left exactly as it was — that variable's
own decision rule never gated on the currency variable's value, so nothing there needed
recomputing, only a stale cross-reference correcting.

## What the sweep changed, honestly

One of six records was already correct and stayed that way, but on materially better
evidence than before: aiva's `non_usd` call now rests on a positive documentary finding
(a content-bearing, US-crawled archive capture showing EUR only) instead of an
absence-only check. Canva looked like a second case of this — see the correction below.

Two records were substantively wrong under the superseded rule and are now real money
values: framer and freepik were both coded `non_usd` despite each vendor's own,
previously-collected archive evidence already sitting in the record's own `sources[]` —
in framer's case, explicitly noted by the original coder as showing USD figures and then
set aside because the old rule couldn't credit an archive over a live same-network read.
The amended rule inverts that precedence, and simply reading the capture the study had
already found supplied a real headline price and a real first-charge figure for both
products, each corroborated across multiple tiers and confirmed in a second
representation (raw HTML) against the risk of a text-extraction misread.

Two records — gptzero and phrasly, the pair whose D-003 failures are what exposed the
old rule as unsound in the first place — resolved to `unknown` rather than to a money
value or to `non_usd`. Both vendors' own terms of service contain an unconditional
statement that payments are in US dollars, which is real documentary evidence and directly
contradicts a clean `non_usd` reading, but neither vendor's terms, help documentation, or
archived pages state what the USD figure actually is for the tier in question. This is
not an evidence gap this sweep failed to close; it is what the amended rule is for.
Coding either product `non_usd` would have asserted a vendor behavior ("publishes only a
non-USD price") the vendor's own contract denies, and coding a money value would have
invented a number no document states. `unknown` is the honest value for a genuine
documentary contradiction between a displayed local price and a contractual USD promise,
with no way to reconcile the two from public materials — which is itself a finding about
determinability, the thing this study measures. Canva joined this group on the same day,
after a correction — see the section immediately below.

Net effect on the dataset: 2 of 76 pass-1 records (framer, freepik) move from `non_usd`
to a determinate money value on both A-domain currency variables (a positive movement for
the determinability figures those records contribute), and 3 (gptzero, phrasly, canva)
move from `non_usd` to `unknown` (i.e., they now correctly count toward the study's
undeterminable-burden finding rather than being credited as a clean non-USD disclosure
they hadn't actually earned). aiva stands exactly where it started, now on firmer
evidence. No variable was redefined and no record outside this scoped six was touched.

## Canva re-examination under corrected wording

**The drafting error.** This sweep's two authoritative texts disagreed without either
coder or coordinator noticing until after canva's first pass closed. The agent
definition's "Currency check" section required evidence that the vendor publishes a
non-USD price "to the reader" — wording that does not say which reader, and this coder
read it as the reader this study's own network happens to produce (Turkey-egressing,
served TRY). The deviations-log D-007 entry — the authoritative record of the rule
amendment, and the text the agent definition was supposed to restate — requires evidence
"that the vendor publishes only a non-USD price, or that **a US reader** is served one."
That is a materially different test, and it is the one D-003 was written to answer in the
first place: D-003 exists precisely because a page rendered in local currency "may be
measuring us rather than the vendor," i.e. the question was never what our own network
sees, but what a US buyer would see. The agent definition has since been corrected by the
study coordinator to match the deviations log.

**What changed.** Canva's own help article
(`https://www.canva.com/help/pay-credit-debit-card/`) states the vendor bills in local
currency by default, with USD used only where the reader's local currency is
unavailable. Under the first (miswritten) reading, this coder evaluated that clause
against the collection network's own reader, for whom TRY is confirmed available, and
concluded `non_usd` — TRY is genuinely this reader's served, available local currency,
so the "unavailable" fallback clause does not even apply to them. Under the corrected
reading, the same clause is evaluated against a US reader, whose local currency is USD —
plainly available to them, since Canva is well known to serve USD pricing to US
customers. That puts a US reader in the ORDINARY case under Canva's own policy (billed in
their own available local currency, USD), not the fallback case. Neither condition
`non_usd` requires is then met: the vendor does not publish only a non-USD price (it
publishes USD to US readers), and a US reader is not served a non-USD price (TRY is what
a Turkey-based reader sees, not a US-based one). Arm 2 (a US-crawled archive capture that
actually contains price figures) still returns nothing — both attempted capture URLs
redirect to Canva's own bot-block interstitial — so no actual USD figure is available to
code as a money value. `headline_price_usd` and `first_charge_amount_usd` both move to
`unknown`, and the TRY figure this study observed is logged as a `display_variant`
register event rather than treated as the vendor's general publication practice.

**Why this is not a value changed to order.** The requesting message invited disagreement
if the corrected test still supported `non_usd` on re-reading. It does not: re-deriving
the conclusion independently, before writing anything, produced the same result the
coordinator proposed, for the reasons above, using evidence this sweep had already
collected (no new browsing was needed — Arm 1's and Arm 2's underlying facts are
unchanged from the first pass; only which reader the facts are evaluated against changed).
This also resolves a visible inconsistency the first pass carried without flagging it:
canva was the only one of the six records where a real documentary currency policy
existed without a matching figure, yet it landed on `non_usd` while gptzero and phrasly —
carrying the structurally identical pattern (a currency statement, no figure) — correctly
landed on `unknown`. All three now share the same resolution for the same reason.

**Standing question, not resolved here.** Whether currency variables should be read
vendor-centrically (does the vendor publish a USD price to anyone, anywhere) or
reader-centrically (what does a US buyer specifically see) when a vendor's stated policy
is genuine local-currency billing is opened as adjudication item A-013 by the study
coordinator. That question sits above a coding decision and is deliberately left there;
canva's `unknown` coding keeps the record consistent with gptzero and phrasly so that
adjudication can move the whole class together if it resolves A-013 the other way,
instead of one record having quietly pre-empted the answer.
