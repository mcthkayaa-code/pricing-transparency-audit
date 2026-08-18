# Doctrine: an event-conditional notice commitment is an instrument gap, not vendor silence

**Resolved 2026-08-17 by the orchestrator. This document reverses its own first ruling, written two
hours earlier, and the reversal is left visible because the reason for it is the substance.**

## The shape

A vendor's terms commit to advance notice before a **price or plan change** — "we will provide advance
notice of any price increase via email before your next renewal date" — and say nothing about notice
before an **ordinary renewal charge at the existing price**.

`renewal_notice_commitment` asks whether the vendor commits to notifying in advance of a renewal
charge. So: is the narrow clause a partial answer the value list cannot express (`instrument_gap`), or
is the vendor silent on the construct while having addressed a neighbour (`vendor_silence`)?

## The inconsistency this resolves, which is mine

Both readings were live in **hand** decisions, not machine ones — the same construct on the same
products classified both ways in one file:

- `pass1/colossyan`, `pass1/jobscan` → hand-decided `vendor_silence`
- `adjudicated/colossyan`, `adjudicated/jobscan`, `pass1/picsart` → hand-decided `instrument_gap`

## The ruling: `instrument_gap`, on a test the hand set had already articulated

> **Where the vendor publishes a notice commitment scoped to a different trigger, the construct is
> documented in a form the value list cannot hold → `instrument_gap`. Where there is no adjacent notice
> clause at all, the vendor is silent → `vendor_silence`.**

That test is not new. It is stated verbatim in an existing hand basis on `plus-ai`: silence applies
where there is *"not even an adjacent clause about price or plan changes — unlike sibling records where
an adjacent, differently-triggered notice clause exists."* The audit applied it consistently and
confirmed the rows on the far side of it: one vendor whose adjacent clause **disclaims** notice, another
whose clause puts the deadline on the user. Those are determinate positions, not gaps.

## Why I reversed

My first ruling was `vendor_silence`, argued from the construct: a price-change commitment is a
commitment about a different event, so on notice-before-renewal the vendor is silent. That reasoning is
coherent. It is also inconsistent with a rule this study had already written down.

**The attribution tool's own documented precedence says a format signal beats a silence signal, "for the
same conservative reason: an instrument gap is a limitation of ours, and claiming ours is the safer
error than claiming theirs."** I wrote that into the tool. My first ruling contradicted it — it resolved
an ambiguous case toward the category that credits the study's own finding.

Two further things I had weighed wrongly:

**I misread the authority I leaned on.** I cited an adjudicator that "named and rejected `instrument_gap`
with reasons". Re-reading it, its reasoning is about the **coded value** — choosing `unknown` over
`no_notice_stated`, by analogy to a refund variable whose negative value requires an affirmative vendor
statement. That analogy settles the value, not the kind. It does state `vendor_silence` for the kind,
but as an assertion rather than the conclusion of the argument it makes.

**The flattening cost runs the other way from how I described it.** I wrote that `instrument_gap` would
discard the distinction between a vendor who says nothing and one who scoped a clause narrowly. It is
the opposite: `vendor_silence` flattens them into one category, and `instrument_gap` is what preserves
the difference.

## What this costs

**It moves values out of the study's headline.** Twelve audit corrections plus two stale hand decisions
move from "the vendor did not publish this" to "the vendor published something our instrument cannot
hold". The unknown burden attributable to vendors gets smaller and the burden attributable to us gets
larger. **That is the direction that makes this study's central claim weaker, which is the main reason to
trust the ruling** — but a reader should also see that it means one more variable's `unknown`s are partly
our own construct's failure.

**It concedes a real design fault.** A binary `advance_notice_stated` / `no_notice_stated` list cannot
express the commonest thing vendors actually do here, which is to promise notice for changes and stay
quiet about renewals. That is a gap in wave 1's instrument, and calling it one is more honest than
recording it as vendor opacity.

## Corrections that follow

- The audit's twelve `vendor_silence → instrument_gap` corrections on this shape are **accepted**.
- My hand decisions of `instrument_gap` on `adjudicated/colossyan`, `adjudicated/jobscan` and
  `pass1/picsart` were **right** and stand.
- My hand decisions of `vendor_silence` on `pass1/colossyan` and `pass1/jobscan` are **wrong under the
  later convention** and are corrected to `instrument_gap`. The audit flagged these as stale even though
  they sat outside its slice.
- Rows where the adjacent clause is determinate — disclaiming notice, or placing the deadline on the
  user — stay as coded. They are not gaps.

## For wave 2

Widen `renewal_notice_commitment` to record the trigger, not just the presence, of a notice commitment:
at minimum a value for "notice committed for price or plan changes only". That is the change that makes
this a measurement instead of a gap. Do **not** absorb it into the existing binary, which would make one
variable measure two constructs — the error A-013 and A-019 were resolved to avoid.

## Why the reversal is left in the document

Deleting the first ruling and publishing only the second would hide that this study's orchestrator, on
this question, first resolved an ambiguous case toward its own finding and had to be argued out of it by
an audit it commissioned. That is worth more to a reader than a clean-looking decision.
