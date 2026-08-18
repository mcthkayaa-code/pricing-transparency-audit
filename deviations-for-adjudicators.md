# Binding corrections for adjudicators

Read this instead of `orchestrator/deviations-log.md`.

Everything below is a rule the study learned the hard way and is bound by. **No product is named
and no coded value appears**, deliberately: the raw log names 62 of the 76 products and states
coded values for several of them, and an adjudicator who has read another product's values may
resolve a close call toward cross-product consistency instead of toward this vendor's own
documents. The same separation was made for coders under D-014; adjudicators should have had it
from the start and did not.

If you believe a correction is missing here that you need, say so in your report. Do not go and
read the log — the omission is a problem to fix once, not a reason to expose one adjudication.

---

## On evidence and reading

**A keyword search is not a reading.** A coded `absent` or `unknown` resting on "I searched the
terms and found nothing" is the weakest evidence any record can carry. A clause was once coded
absent on a keyword search when it was present under different words, and the value was reversed on
a reading. Vendors write the same obligation a dozen ways — "impose limits", "restrict access",
"unsuccessful generation", "did not complete". Where a disputed value rests on a search, read the
document.

**Two keywords in one document establish nothing.** Where that is the whole basis and the window is
closed so the record cannot be improved, neither answer is honest: coding the vendor silent asserts
more than the record supports, and leaving it open forever is an unpaid debt. Say plainly in your
note that the basis does not support an attribution.

**Verify that a cited capture exists.** A record once cited a dated archive URL for a quoted figure;
the URL redirected to a different date's capture, no capture existed at the cited timestamp, and the
quoted figure appeared nowhere on any date. That is fabricated provenance, not a misreading. You are
the only pass that verifies citations — coders are blind to each other and the mechanical checks
compare timestamps, which cannot see a plausibly-dated URL that leads nowhere. For every disputed
value resting on a quotation, open the capture and find the words in it.

**A record can contradict itself, and that is evidence.** Related variables constrain each other. A
record that codes one value while its own neighbouring values only cohere with the opposite has left
the evidence for its own correction in place.

**Read a value's table before its example.** The codebook's illustrations of a value never bound it.
A value was once coded `no` because the vendor's arrangement did not match the illustration, while
the same variable's value table independently listed the route the vendor had taken.

**A figure present only in UNRENDERED markup is not disclosure — and the caveat decides more cases
than the rule.** A variable asks what a reasonably diligent reader of the vendor's published
documents can obtain, from any standard reading position, without inspecting page internals. A value
existing only in an inert data blob is `unknown`. But **an embedded payload the page RENDERS still
counts**, and so does one carrying a figure the vendor displays to readers that a capture could not
render. An FAQ built from JSON is disclosure if the FAQ appears; the same JSON is not if nothing
displays it. The test is whether a reader sees the figure, not how the datum is stored.

You will meet this as a **disagreement that looks like one coder being careless with page
internals**, and half the time it is the opposite. Both directions have now happened here on the
same rule: one coding read a feature table out of a JS bundle that no page ever displayed and coded
three variables from it, wrongly; another met a working FAQ whose answers a capture had not
expanded, applied the prohibition without the caveat, and coded five properly-disclosed variables
`unknown`. **Deciding it needs one specific finding: does the page display that text to a reader?**
Expand the control in a live browser, or establish that the component renders the payload it holds.
An `aria-expanded="false"` in a capture is a fact about the capture.

Where the answer is that the vendor **changed the page** after the window closed, say so and code the
window. A live page that now server-renders text a window-dated capture lacks is evidence about
today, not about the frame — but it is decisive evidence about the *mechanism*, and the mechanism is
what the caveat turns on.

## On archived and localised pages

**A request-language header is not a currency selector.** Currency localisation is driven by
inferred geography, not by language preference, so a currency read cannot be established that way.

**Archive captures can return pre-hydration HTML** on exactly the script-rendered pages where prices
are hardest to read. A figure absent from a capture is not necessarily absent from the page.

**WebFetch refuses `web.archive.org` outright.** Use `curl` instead. Verifying a cited capture is a
standing duty, so you will hit this; it is a tool limitation, not a sign the capture is missing.

**Prefer window-dated captures for the coded value.** You work after the window closed; if a live
page now differs, say so and code from the capture.

## On `unknown`, `not_applicable` and enums

**`not_applicable` requires positive documentary evidence that the construct cannot exist for this
product.** A vendor saying nothing is `unknown`. This carve-out has been over-extended more than
once, most often on output-related variables such as watermarking, where silence was read as
inapplicability. That boundary is open; resolve by the codebook and say that it is open.

**Every `unknown` you code must name its kind:**
- **vendor silence** — the documents were read and reachable, and the vendor does not publish it.
- **access failure** — a document that would answer it exists, or plausibly exists, and could not be
  retrieved. If the vendor has a page written on exactly this subject and you could not open it, the
  silence is yours, not theirs.
- **instrument gap** — the vendor documents the construct in a form the codebook has no slot for.

An `unknown` without its kind will have to be revisited before the freeze.

**A coded value must be one the codebook's own value table lists.** Values outside a variable's
table have reached records before and passed every check, because nothing was comparing them.

**Numbers compare as numbers.** A difference in how a figure was serialised is not a disagreement.

## On classification under §7.4

`date_explained` requires a `vendor_edit` entry in a change register. A `display_variant` entry never
supplies it. `variant_explained` requires two archive snapshots showing both states.

**Neither may be reached for to improve a statistic.** If the evidence is not there it is an ordinary
disagreement, and an unresolvable one is a finding about the documents rather than a failure of
yours.

## On what you may read

You may read both records for your product, both source sets, the codebook, protocol, sampling
rules, record template, the tools, and the vendor's own live and archived pages.

**Off limits: another product's records, the adjudication queue, `orchestrator/interim-signals.md`,
the raw deviations log, the public site.** The queue and the log both name products alongside the
constructs they are open on, and naming a product as `unknown` on a variable states that product's
value.

**If you need a finished record's format, read `record-template.yaml`.** It carries every field in
order. If it genuinely does not answer your question, report that and format it your best way — an
irregular record is a trivial problem, and one adjudicator's values steering another's is not. An
adjudicator opened another product's record for format and disclosed it; review could rule out
influence on three of its four disputed variables and could not rule it out on the fourth.

## On writing and committing

**Never rewrite an existing record in place.** A script that edited records by line surgery broke
eight of them. Write your own record; leave the prior passes untouched.

**Scope your commit, not just your add.** `git add <your files>` then `git commit -- <your paths>`.
A bare `git commit` takes whatever another agent staged, and has twice shipped one agent's work
inside another's commit. Never `git add -A`, never `git push`.

## On disclosure

If you breach one of these, write it into your own `coder_note` and your report. Every breach so far
has been fixed structurally rather than punished, and the ones that were disclosed cost the study far
less than the ones that had to be discovered.
