# Binding rules from the deviations log — coder-safe digest

**Read this instead of `deviations-log.md`.** The full log is the study's audit trail and it names
products and quotes their coded values, which would tell a second coder what the first one found.
This digest carries every rule the log created and none of the evidence it created them from.

Nothing here is new. If a rule below and the full log ever disagree, the log governs and this file
is wrong and should be fixed.

---

## Reading a page

**A rendered read IS a documentary read.** Loading a public page and letting its own scripts run is
reading a document. The prohibitions are on account creation, login, checkout, card entry, trial
activation, product use and vendor contact — never on rendering. So:

- If a static fetch shows no price, you must attempt a rendered read before coding anything
  `unknown`. "Our fetcher could not see it" is not a finding; "a visitor cannot find it" is.
- Check the page's **embedded JSON payload** as well as its rendered text. Prices and plan data
  routinely live in a payload that never becomes visible text.
- Feature grids drawn with check/cross **icons** need DOM inspection, not text extraction.

**A figure present only in UNRENDERED markup is not disclosure.** A variable asks what a reasonably
diligent reader of the vendor's published documents can obtain, from any standard reading position,
without inspecting page internals. A reader reads a page; they do not read its JSON payload, its JS
bundles or its DOM attributes. A value existing only in an embedded feature table, an inert data blob or
an unrendered FAQ payload is `unknown`, not a documented value.

The caveat matters as much as the rule: **an embedded payload the page RENDERS still counts**, and so
does a payload that carries a figure the page displays to readers but a capture could not render. The
test is whether a reader sees the figure, not how the datum is stored. An FAQ built from JSON is
disclosure if the FAQ appears; the same JSON is not if nothing displays it. A price a vendor plainly
shows, read out of structured data because the archive stored a pre-hydration shell, IS disclosure — the
payload supplied the reach, not the fact.

Decided in adjudication (A-019, A-020) and added here late: a second coding read a feature table out of a
JS chunk and coded three variables from it, and its values were wrong where the first coder's were right.

**Read any money value in a second representation before coding it.** Formatted price markup lies
to text extractors: a superscript-cents layout can read as whole dollars, an order-of-magnitude
error that no plausibility check catches because the wrong number looks ordinary. Confirm each
figure in embedded JSON, raw HTML, or a screenshot, and sanity-check its magnitude against the tier
name and billing basis. Record which representation you confirmed against.

Some pages are worse than misleading — they are unreadable to extraction by construction. Prices
rendered by an animated digit-roller inside a shadow DOM return nothing at all to plain text
scraping, and a coder who trusts the empty result codes `unknown` for a figure any visitor can see.
Where the text is empty but the page plainly shows a price, reach for the page's own structured
data (`ld+json` Offer blocks, embedded commerce payloads) or a screenshot. An empty extraction is a
fact about your tool, never about the vendor.

**Beware fabrication, not just misreading.** Summarising fetches have been caught inventing
structure the verbatim DOM contradicts — a cap split across tiers that is actually identical for
all of them, a rights grant that the terms deny. Invented structure cannot be caught by any
arithmetic or magnitude screen. Confirm every structured claim against raw DOM text.

**A coder-tooling misread is never a `display_variant`.** The vendor served one state and our
reader mangled it. Document it in `coder_note` and code the true value.

**Establish a toggle's DEFAULT state from the DOM** — which control carries `checked` or
`aria-selected`, what the plan grid's own classes say — not from which number an extractor printed
first. Also check whether a toggle changes the SET of tiers rather than only their prices.

## Currency

`non_usd` is a claim ABOUT THE VENDOR and needs positive evidence. Work down this list, stop at the
first arm that returns readable prices:

1. **The vendor's own currency disclosure** — a currency or country selector, an explicit currency
   statement in billing/help documentation or the terms, or a vendor-supported currency parameter.
   If the vendor offers USD, the USD figure is the published price; log the locally served currency
   as a `display_variant` register event.
2. **A US-crawled archive capture that actually contains price figures.** A capture returning
   pre-hydration markup with no prices has NOT answered the question.
3. Only then may you code `non_usd`, and only where the evidence shows the vendor publishes a
   non-USD price **to a US reader** — not merely that it serves one to us. A vendor whose stated
   policy is to bill in the buyer's local currency is serving a US reader USD by that same policy.

**Where no arm returns readable prices, code `unknown`, not `non_usd`** — "we could not look" is a
statement about our evidence. An `Accept-Language: en-US` header is NOT a US-locale test: it states
a language preference, while currency localisation is driven by IP geolocation.

## First charge

Multiply a monthly figure by 12 **only where a document states the plan is charged once for twelve
months**, and record the arithmetic in `computation_assumptions`. Where no document states the
billing frequency, code `unknown` — do not assume twelve months. A first charge you computed and a
total the vendor published are indistinguishable in the value alone, which is why the note is
required rather than optional.

## Record hygiene

**Quote yes/no values** — `value: "yes"`, not bare `yes`. Unquoted, YAML parses them as booleans and
the same coded value ends up stored two ways across records. This applies to top-level
administrative fields too, not only to coded values.

**`computation_assumptions` belongs inside `variables:`** as a `{value, source, evidence}` map, like
every other coded variable. Not as a top-level field.

## Sources and archival

**An official source you could not read is not evidence.** Log it in `conflict_note` and code from
what you could read. If a page requires login, do not open it — say so instead.

**Archive.org rate-limits us.** Cap at two save attempts, then record `local_copy_only` with a
dated verbatim local capture and move on. That is an expected outcome, not a failure on your part.

**If a governing document returns a page whose BODY does not render**, verify that in a full browser
render and say so explicitly. A document that exists as a URL but not as readable text is a finding,
not a fetch failure.

## Product status

If the vendor's own pages show the product is no longer offered — a shutdown notice, a sunset date,
a "no longer available" page, a redirect to an unrelated successor — say so prominently in
`coder_note`. A slow page, a bot wall, a 403 or a geo-block is NOT evidence of shutdown; a rebrand
where the product still sells is not either.

## Blindness

Do not open another product's record, in any pass — not for its values, and **not for its
formatting, its YAML shape, or an example of how a tool is run.** The template is for that. If a
second coder has seen the first coder's values, the reliability estimate the whole study rests on
is not measuring what it claims to.

If you breach this anyway, say so plainly in `coder_note`. Every coder who has disclosed a breach
kept their record usable under a for-cause second reading, which is far better than a quiet breach.

**Blindness is about how you search, not only what you open.** A coder ran a grep across `*.md` in
the study directory and swept in an orchestrator file it was not meant to see. Do not glob across
the study directory: open files by exact path, and when you are hunting for a rule, search THIS
file. The `orchestrator/` subdirectory is not yours at all — it holds the deviations log, the
adjudication queue, the collection tracker and the sampling selection, every one of which names
products and quotes their coded values.

**Git: you commit, you never read history.** You need exactly `git add <your own files>` and
`git commit`.

**Scope the commit, not only the add.** Use `git commit -- <your own paths>`, never a bare `git commit`. A bare commit takes whatever is in the shared index, and a concurrent collector may have staged its own files a second earlier — one coder's first commit swept in five files belonging to another product exactly that way. Scoping costs nothing and makes the race harmless.
 Never run `git log`, `git show`, `git diff` or `git blame`. If you need to confirm your own commit landed, `git commit` already told you, and `git status --porcelain -- <your own paths>` will confirm a clean tree without showing you a single commit message. The orchestrator's commit
messages describe findings in detail, by product name and with figures — every product in the
reliability sample is named in them with a coded value — so reading history would tell you what
another coder found as surely as opening their record would. This one cannot be solved by moving a
file, because the history belongs to the repository you have to commit into. It rests on you.

**Your attestation carries both clauses:** that you opened no other product's record, and that you
did not read repository history.

## Known open questions

Where a vendor sells a cheap **non-zero** time-limited intro period that auto-converts to a higher
recurring rate, the instrument does not cleanly cover it and the question is open in adjudication.
Code the trial variables as your own reading of the frozen codebook supports, and describe the
intro period plainly in `coder_note` — its price, its length, and the rate it converts to, with
sources. Note that `trial_card_required` has its own rule barring inference: vendor silence there
is `unknown`, and the existence of a charge is not a statement that a card is required.

Where a published billing cadence matches none of the codebook's allowed values, code `unknown`,
state exactly what the vendor publishes in `coder_note`, and move on. The instrument is frozen for
this wave; do not invent a value.
