# Pre-freeze checklist — Pricing Transparency Audit, wave 1

Everything that must be true before the dataset is frozen and analysis begins. Written at 73/76
so the close-out is a list to work rather than a set of things to remember. Each item names what
"done" means and where the evidence lives.

Nothing here changes the instrument. These are completion, verification and disclosure steps that
the protocol already requires; the list exists so none of them is skipped quietly.

---

## 1 · Finish pass 1

- [x] **Pass 1 complete 76/76** — **coding ran 2026-08-05 to 2026-08-13**, and that span is NOT the
      protocol's window. **Protocol §104 defines the collection window as opening on the date the
      frame is frozen and closing when the final-day re-check completes: 2026-08-04 to 2026-08-17.**
      Both are true of different things, and the paper correctly prints the pre-registered
      definition. Recorded here in 2026-08-17's figure sweep so that nobody later "corrects" the
      paper to match this line — the same trap the preprint draft caught with the adjudicator count,
      where 24 and 29 are both right about different populations.
- [x] Frame reconciled: 76 rows, no duplicates, no orphan record, 73 active + 3 discontinued.
- **Done means:** 76 of 76 carry `status: complete` and the reconciliation script prints zero
  remaining.

## 2 · Record-completeness gaps found during collection

- [x] ~~**`archive_status` unset on 6 records** — 10web, aiva, aragon-ai, canva, faceless-so,
      ismybrandinai. All are early records, coded before the field was used consistently. The
      validator does not require it because it is administrative, which is why they passed.
      Set each from what that record's sources actually show; do not guess.~~
      **Corrected 2026-08-15 (D-019) — the diagnosis above was wrong for five of the six.**
      `archive_status` was not unset on 10web, aragon-ai, canva, faceless-so and ismybrandinai. It
      was nested inside `variables{}` and populated with `archived`, canva's carrying a full
      evidence paragraph. Read at the top level it looked absent; it never was. Acting on the
      instruction as written would have re-derived a value that already existed and put canva's
      prose at risk. All five are now canonicalised to top level, nested maps left intact. The
      original wording is kept struck through because the misdiagnosis is the useful part: a field
      read in one location and reported as missing is the same error class as D-019 itself.
- [x] ~~**`archive_status` genuinely absent on 1 record — aiva.**~~ DONE 2026-08-17: five fields added, each DERIVED FROM THAT RECORD'S OWN EVIDENCE per the instruction — archive_status from all six sources carrying an archive URL, primary_source_url and archive_url from the pricing-class entry, recheck_date from the latest access date (2026-08-10 vs a 2026-08-06 collection date), and paid_submission from the frozen frame, which is authoritative for it. Provenance recorded in the record. Original text: Also absent there:
      `paid_submission`, `recheck_date`, `primary_source_url`, `archive_url`. These are recorded
      nowhere in the record, so this is the real gap the item above was meant to name. Derive each
      from that record's own `sources[]` by hand; do not guess, and do not infer them from the other
      early records. `entry_tier_name` is NOT in this list — it was nested and has been lifted.
- [x] ~~Re-run the shape survey for `computation_assumptions`~~ DONE: the build reads all three observed shapes and reports zero unrecognised (D-058). Original text: (deviation **D-010**). Records are NOT
      mutated — the dataset build canonicalises across all four observed shapes. Confirm the build
      does that before it produces a CSV, and confirm no record was silently normalised in the
      meantime. At final N the drift is 17 of 76.
- [x] ~~**The dataset build must read every record through a YAML parser.**~~ DONE: `tools/build_dataset.py` parses only, and reports any shape it does not recognise instead of skipping it. Original text: never by text matching.
      Records legitimately differ at the text level in ways a parser erases — `julius-ai` quotes
      `archive_status` where others leave it bare, and both are the same string once parsed. A
      text-matching build would treat them as different values. This is not hypothetical: an
      independent audit's own text-keyed bucketing dropped that exact record and reported the D-012
      split as 45/24/6 = 75 against a corpus of 76, understating the local-only rate by 1.3 points
      (D-010). The study has also been bitten once by text-level record surgery — D-010's normalizer
      produced invalid YAML in eight files before being discarded. Hard requirement, not preference.
- [x] ~~Remove `validate_records.py`'s `TOPLEVEL_OK` exemption~~ **RESOLVED 2026-08-17 AS A KEEP, NOT A REMOVAL (D-062).** The build does now prove it canonicalises across every shape, which is what this item waited on. But **seven records** rely on the exemption, and removing it would fail seven correctly-coded records over a stored-shape difference the build already erases — while the alternative, moving the field inside them, is line surgery on records for a cosmetic reason, which is D-010's exact prohibition and which this orchestrator has already broken three records doing this week. The exemption stays and stops being SILENT instead: `report_toplevel_usage()` names every record relying on it, and wave 2 fixes it in the record template before any data exists. Original text:
      so a future wave cannot drift the same way without failing (D-010 prevention clause, open).
      **Still open, and D-019 did not close it.** D-019 canonicalised ADMINISTRATIVE fields that had
      drifted INTO `variables{}`; `TOPLEVEL_OK` covers a CODED variable that drifted OUT of it. Same
      family, opposite directions, different field classes — and the coded one still carries prose
      the build must merge rather than lift, which is why it waits on the build and this did not.

## 3 · Reliability: pass 2

- [x] **Pre-registered double-coded set: 26 products**, blind — COMPLETE 2026-08-14.
      A pass-2 coder must not read anything under `records/pass1/`.
- [x] ~~**For-cause blind second codings, reported SEPARATELY**~~ **ALL THREE DONE 2026-08-17** —
      promised 2026-08-06/07/12 and performed eleven days late (D-067, D-065, D-066). Agreement,
      reported separately and never pooled with the 26: faceless-so 63.9%/α 0.603, gptzero 75.0%/α
      0.728, squarespace 83.3%/α 0.823; pooled 74.1%/α 0.720 against the corpus's 82.2%/α 0.811. The
      pooled figure is published **with its decomposition** in `methods-who-coded.md`, because bare it
      misleads in both directions: one of the three is above the corpus, and the low one is not noise —
      it decomposes into one underdetermined codebook question, one pass-1 over-read, and one
      orchestrator briefing defect (A-019 pushed to a running coder without A-020's caveat). All three
      raised disagreements that went to adjudication: A-024 faceless-so and A-022 gptzero resolved,
      A-023 squarespace running. Original text: from the pre-registered set so the
      planned statistics stay uncontaminated: faceless-so (**D-001**), gptzero (**D-004**),
      squarespace (**D-011**). All three were blindness breaches self-disclosed by the coder.
- [x] Krippendorff's alpha computed and **three times** corrected (D-020, D-021, and a units fix): **0.811**. The figure read 0.807 here until the freeze sweep on 2026-08-17 caught it disagreeing with `tools/agreement.py` and `limitations-register.md` §3, both of which say 0.811 — a fourth stale hand-typed number, found the same way as the other three, by re-deriving rather than reading. See `reliability-result.md`. Report the pre-registered figure
      and the for-cause records' agreement separately, never pooled.
- **Done means:** 26 blind pass-2 records exist, 3 for-cause records exist, alpha is computed from
  the 26 alone.

## 4 · Adjudication — 15 open items

Settled after pass 2 by a third reading against the same documents. The resolution and its
reasoning enter each record's `coder_note`; nothing is edited silently.

- [x] ~~**Adjudicate the 145 substantive disagreements**~~ COMPLETE 2026-08-17 (D-044): 24 adjudicated records + 2 needing none = 26 covered. Original text: across 26 products (§7.4). Products with
      zero substantive disagreements need no adjudicated row — the codebook publishes the primary
      row where no adjudicated one exists, and two products qualify (D-025), verified rather than
      assumed. **Progress 2026-08-16: 22 of 26 written, 2 need none, 2 remain (copyleaks,
      ismybrandinai).** Both remaining runs were cut off by a session limit before writing.
- [x] ~~**A-012 is a SWEEP.**~~ RESOLVED (D-049): 4 positives of 17 candidates; the token mechanism also has false negatives, so prevalence is a floor. Original text: Pull every record whose `coder_note` carries the literal token `A-012`
      and apply ONE rule across all of them — paid non-zero intro periods must not be settled
      product by product.
- [x] ~~**A-011**~~ RESOLVED with the instrument-gap family (D-055). Original text: now has four records (canva, jobscan, resume-io, teal). Four failures of one enum
      is evidence the value list is incomplete, not that four vendors are unusual. Wave 1 records
      the treatment; wave 2's codebook extends the enum. **Corroborated independently 2026-08-16:**
      `attribute_unknowns.py` classifies these as instrument gaps from the coders' own prose, without
      being told the queue item exists. A second enum gap has since joined it —
      `renewal_notice_commitment` has no value for an event-conditional notice commitment (D-035).
- [x] ~~**A-013**~~ RESOLVED jointly with A-019 (D-052 context): vendor-centric, on obtainability from a standard reading position. Original text: decides whether the currency variables are vendor-centric or reader-centric. Pass 1
      is coded vendor-centrically throughout so the class can be flipped together if adjudication
      chooses otherwise.
- [x] ~~Remaining items: A-001, A-002, A-004, A-006, A-009, A-010, A-014, A-015.~~ ALL RESOLVED 2026-08-17; the queue is closed at 20 items, zero open (D-053, D-054, D-055). (A-003 and A-005
      are resolved by the D-007 sweep; A-007 and A-008 are withdrawn. All four stay listed, struck
      through, so the queue keeps its history.)

## 5 · Mechanical checks, in this order

- [x] ~~`tools/normalize_booleans.py` across all records~~ CLEAN 2026-08-17: zero changes needed across all 131 records, re-run after the aiva addition. Original text: — covers coded values AND the top-level
      admin fields (**D-006 addendum**: `paid_submission` was a YAML boolean in 16 records).
- [x] ~~`tools/validate_records.py`~~ EXIT 0, re-run after every correction batch. Original text: 37/37 coded present on every record, AND the administrative
      guard clean: `coder_role` / `coder_pass` present, top-level, in enum, and not contradicted by
      a nested copy (**D-019**). Read the exit code, not just the OK lines — the guard this replaced
      printed nothing and passed everything for a day.
- [x] ~~**`tools/check_free_text_caps.py`**~~ RUN 2026-08-17, rate published in D-045: 37 of 115 values exceed the 300-character cap, 32%, not truncated. Original text: run and PUBLISH the rate, do not truncate (D-045).**
      37 of 115 `computation_assumptions` values exceed the codebook's 300-character cap, up to
      1,240. They are arithmetic derivations with citations; shortening them would destroy the
      reproducibility the field exists for. Wave 1 discloses the 32% breach, wave 2 reclassifies
      the field as documentation and drops the cap.
- [x] ~~**`tools/check_value_enums.py`**~~ CLEAN 2026-08-17: 131 records, 0 out-of-enum. Original text: zero out-of-enum values across every record** (D-022).
      It parses each variable's allowed values from the codebook. Two variables have no
      parseable table and the tool says so; treat that count as unchecked coverage, not as a pass.
- [x] ~~`tools/check_price_arithmetic.py`~~ RUN CLEAN 2026-08-16 over the PUBLISHING rows after
      D-039 fixed its scope — it had defaulted to pass 1 and never seen an adjudicated row. Six
      items, all previously closed: three A-011 cadence gaps, three D-009 vendor-rounding FLAGs.
      Original wording: every FLAG and PROV either cleared or closed with a
      recorded reason. Four FLAGs are already closed as legitimate vendor rounding or known
      adjudication items (faceless-so, invideo-ai, jobscan, krea-ai); that closure is recorded in
      the D-009 sweep result so they are not re-investigated.
- [x] ~~A YAML parse pass over every record.~~ CLEAN 2026-08-17: 131 records parse. All 76 must load.

## 6 · Archival and provenance (deviation D-012)

- [x] ~~**THE STUDY HAS NO US VANTAGE POINT**~~ **NARROWED AND CARRIED 2026-08-17**: four records at the start, two settled as rendering limits rather than vantage-point ones (the second by D-075's header-level `cf-ray …-IAD` proof of a US-served read), two genuinely vantage-bound and stated as such in `paper-draft.md` limitation 6 with their denominator. Original text: **THE STUDY HAS NO US VANTAGE POINT — now two records, not three (D-056, refined by D-057 and
      again by D-075).** **Sweep 3 settled a second of them, and by header-level proof rather than
      inference:** a Common Crawl capture of that vendor's pricing page carries `cf-ray …-IAD`,
      Cloudflare's Washington-Dulles edge, which establishes the read was SERVED FROM THE US — and
      the document is a pre-hydration shell carrying only `$0` placeholders. So that figure is absent
      from the served document **from any vantage**, not withheld from ours, and the value moved
      `access_failure` → `instrument_gap`. The remaining two have **no Common Crawl record at all**,
      so the arm cannot be run against them and the limitation stands for those two. **Carry into the
      paper as a bounded limitation with its denominator, not as a blanket one** — of the four
      records this began with, two are now settled as rendering limits and two remain genuinely
      vantage-bound. Superseded wording follows:
  *(superseded wording, kept for the record: three records, D-056/D-057)*
      A US-served Common Crawl capture of one of the four was fetched and contains no plan-card
      content at all: that vendor's price is absent from served HTML from any geography, so its
      `unknown` is a rendering limit rather than a vantage-point one, and only a RENDERED US read can
      settle it. Common Crawl holds no capture of the other three pricing pages, and archive.today
      holds two but ten and twenty-two months outside the window. Superseded wording follows:
- [x] ~~**Tighten one record's prose (D-056).**~~ DONE 2026-08-17: the evidence now says the absence is of RENDERED content, names the USD figure that does sit in the vendor's page payload, and states why A-019 leaves the coded value unchanged. Original text: Its evidence says no USD figure is published anywhere
      for its entry tier; a USD annual figure for that tier does exist in the vendor's own page
      payload, unrendered. The coded value is unaffected — A-019 makes unrendered markup non-disclosure
      — but the sentence overstates the absence.


- [x] ~~**Three retrieval threads owed, blocked on the archive.org outage (D-051)**~~ **ALL THREE RUN 2026-08-17 (D-075)**, once the service recovered. The fail/error scan was run on BOTH captures (zero hits for fail/unsuccessful/deduct) and the value it was holding is released. The Firefly capture proved structurally empty — that vendor assembles the page from fragments at runtime — and the fragment origin found instead carries no temporal warrant, so the prior caveat stands. The currency arm was decisive by header-level proof: a Common Crawl capture with `cf-ray …-IAD` establishes a US-served read, and the document is a pre-hydration shell, so the figure is absent from any vantage. Original text: **Three retrieval threads owed, all blocked on the archive.org outage (D-051)**: a fail/error
      scan of the recovered billing article, one vendor's window-era capture 20260806112138, and a
      second retrieval arm for three currency records. One value is deliberately held in
      `access_failure` pending the first of these.
- [x] ~~**A-020**~~ RESOLVED (D-052): recoded to $10.99/$131.88. Original text: adjudicate the recovered USD price (D-051). A-013 and A-019 pull opposite ways on
      whether a payment processor's price object shipped in the page is a published document.
      Recoding would shrink the study's headline, which is the reason to decide it properly.


- [x] ~~**Two archive threads owed from the post-window retrieval (D-050)**~~ **BOTH RUN 2026-08-17 (D-075)** via the Memento timemap, as this item advised. One confirms the study's single genuine access failure and exhausts that route. The other was NOT harmless: the slug was unguessable, and the article links a full credit rate card with expiry terms, which makes D-050's claim that the vendor never published a credit definition half wrong — sweep 1 generalised from one link too early. Original text: **Two archive threads still owed from the post-window retrieval (D-050)** — one vendor's
      captures and another's release notes, blocked because archive.org's replay path and CDX index
      were both intermittently down. Use the Memento timemap endpoint, which the retrieval found
      works when CDX does not.
- [ ] **Add Common Crawl to the collector as a standard route (D-057).** Its index and WARC
      byte-range fetch worked first time, one request each, and its crawler runs on US
      infrastructure — a free second vantage point for a study whose readers all sit in one
      country. It should not have been discovered on the last day.
- [ ] **Add rendered-read and multi-capture rules to the collector for wave 2 (D-050).** Three of
      four under-retrieval mechanisms are procedural: apply D-005's rendered read to help-centre
      articles as well as pricing pages; check MORE THAN ONE archive capture before concluding a
      capture is a shell; and decompress gzipped raw-content responses.
- [x] ~~**Adjudicate the non-English Terms recovery (D-050)**~~ **DONE 2026-08-17 (D-074)**: `records/adjudicated/wix.yaml`. The rule was established rather than assumed — the vendor's own Turkish and German texts each state that the document was authored in English and translated for convenience with English governing, which is the vendor confirming they are parallel translations of one instrument, and the English rendering defect was shown to be five months old rather than window-specific. Three values move; the alternative (a client-side locale artifact, as on a different product here) was specifically tested and ruled out on response headers. Original text: **Adjudicate the non-English Terms recovery (D-050)** — the construct's absence is
      established from a Turkish/German rendering, the governing English wording is not.


- [x] ~~**AUDIT THE PATTERN-CLASSIFIED ATTRIBUTIONS (D-042).**~~ DONE 2026-08-17 (D-048): all 394 audited by two independent reviewers, 87.3% confirmed, 50 corrected, 98% of the errors biased toward vendor_silence. Moved the headline from 88.4% to 79.3%. Original wording: The review slices covered only rows
      marked `NEEDS_HAND_REVIEW`; the ~430 rows the patterns classified were never checked by
      anyone, and a reviewer found five wrong just by reading adjacent rows — four of them on the
      published row of the product A-016 warned would be over-scored, and in the direction that
      inflates our own headline. Sample or sweep the `decided_by: pattern` rows, prioritising
      `vendor_silence` since that is the finding-favourable category.
- [x] ~~**Hand-review the remaining unattributed `unknown` values (D-027)**~~ CLOSED 2026-08-17 (D-043): zero pending, 100 decided by hand with written reasons. Original wording: — 147 at first run, 120
      after 26 hand decisions with written reasons; the two review agents dispatched for the rest
      were cut off by a session limit and need re-running — and re-run
      `tools/attribute_unknowns.py` until the residue is zero or the remainder is published as
      genuinely unattributable. The count goes in the limitations either way.
- [x] ~~**Make `validate_records.py` require evidence prose (D-028)**~~ DONE 2026-08-17 as `check_evidence_prose`, a HARD requirement on publishing rows because D-028's prediction held: zero publishing rows lack it. Pass-2 gaps (18) are reported, never silently passed. NOTE: the first version keyed its targeting on the wrong condition and failed on a clean corpus — caught because a separate query had just returned zero. Original text:, then
      re-run over all records. 25 real coded values currently carry a source but no reasoning;
      confirm the udio and vidnoz adjudicated rows closed the two that reach publishing rows.
- [x] ~~**Close the silent-skip trap in `disagreements.py` and `agreement.py` (D-026).**~~ DONE 2026-08-17: both now report any coded variable absent from either pass to stderr instead of dropping it. Verified inert on this corpus (962 units intact, alpha unchanged at 0.811), so it changes no published figure and stops the next corpus losing units in silence. Original text: Make both
      REPORT a coded variable absent from either record instead of skipping it. Verified inert on
      this corpus (all 26 products carry all 37 in both passes, 962 units intact), so this changes
      no published figure — it stops the next corpus from losing units in silence. Do it when no
      adjudicator is running, then re-run both tools and confirm the counts are unchanged.
- [x] ~~**Re-run the 96 throttled archive citations (D-036)**~~ DONE, three sweeps (D-047): 92 remain unserved, 96% of them on hosts the service serves fine, so request-side rather than capture-side. Reported with the host analysis rather than as a verdict. Original wording: with a longer delay once archive.org
      has forgotten us. They are unassessed, not failed, and must not be reported either way.
- [x] ~~**Trace the 28 unresolvable citations to their coded values (D-036).**~~ DONE (D-037):
      178 values across 10 publishing rows; 159 have a surviving local mirror, 19 on one product
      (`pass1/ismybrandinai`) have neither a resolvable capture nor a local copy. Remaining work
      on this: decide how those 19 are marked in the published dataset.
- [x] ~~**The dataset release MUST include the `-sources/` directories (D-037).**~~ VERIFIED READY 2026-08-17: all **798** source files across the corpus are tracked in git, 82 MB total, so the requirement can be met at release rather than discovered unmeetable. Original text: For 159 published
      values the local capture is the only surviving evidence, because their archive citation
      resolves to a different capture or none. Shipping records alone would look complete and be
      unverifiable.
- [x] ~~**Trace the 28 unresolvable citations**~~ DONE (D-037): 178 values across 10 rows; 159 have a surviving local mirror, 19 on one product have neither. Original text: to their coded values (D-036).** For each of the 14
      pointing at a non-existent capture and the 14 with no capture at all, find whether any coded
      value rests on a quotation from it. Where one does, re-verify or mark it unattributable.
- [x] ~~**Archive-URL existence verification (D-023)**~~ DONE, three sweeps (D-047): 377 exact of 511 cited; 92 unserved, reported with a host analysis. **AMENDED 2026-08-17 (D-069): 13 of the 14 rows called `missing` were HTTP 403 — the archive refusing a whole host — not 404. Genuine archival absence is ONE citation of 511. Re-labelled from the recorded status codes, no re-requests; `verify_archives.py` gained `excluded` and `unclassified` so nothing defaults into `missing`; `check_archive_status.py` now reports 0 failing. Twelve of the thirteen are one vendor the archive refuses entirely, which is a finding about that vendor's archivability rather than a defect in our record.** Original text: LOAD-BEARING, not optional (D-033).** All
      576 cited documents across the 76 pass-1 records carry archive URLs, and 18 records keep no
      local mirror at all, so archive.org IS the provenance of this dataset. One record has
      already been found citing a capture that never existed. Verify every cited capture resolves
      at its cited timestamp rather than redirecting. Note: WebFetch refuses web.archive.org;
      curl is the working fallback.
      A local timestamp-plausibility sweep is already clean but CANNOT see this failure mode: the
      URL that failed carried a perfectly plausible date and simply had no capture behind it. This
      needs the CDX index, so run it alongside the post-window retry below, while nothing else is
      competing for the service.
- [x] ~~**Post-window archival retry**~~ **DONE 2026-08-17 (D-073)**: the 92 citations the service had refused across three sweeps were re-asked once it recovered, and **all 92 came back `ok`**. Provenance moved from 377 of 511 (73.8%) to 482 of 516 (93.4%), with zero unanswered. Original text: run after the window closes when nothing competes for the
      service. Explicitly PARTIAL: a late capture documents the page as it is then, not as it was
      when coded, so the local copy remains the coded evidence and late captures are labelled
      post-window.
- [ ] Query the availability API for captures made by OTHER crawlers near our access dates. Those
      are contemporaneous and are the only kind that genuinely closes the gap.
- [x] ~~**Add an `archive_status` consistency check to the toolset (D-060).**~~ BUILT 2026-08-17: `tools/check_archive_status.py`. Found 14 of 76 records disagreeing with their own status, 12 of them understating our provenance (D-061). A refused capture is reported unverifiable rather than failed, so an outage cannot manufacture failures. Original text: `archived` must require
      at least one capture that resolves; `local_copy_only` must require at least one local file.
      Nothing currently compares the status field against the evidence it describes, and two records
      were found disagreeing with their own status in opposite directions.
- [x] ~~Report the archived / local-only / unset split as a stated limitation~~ DONE in limitations-register.md section 5: 57 archived, 19 local_copy_only, 18 keeping no local mirror. Original text:, naming the mechanism
      **including our own concurrency**, which caused part of the rate-limiting.
- **Done means:** every source in the published dataset carries an archival state a reader can see.

## 7 · Window close and final sweep

- [x] ~~Record the window's close timestamp in `collection-status.md`~~ DONE 2026-08-17: opened 2026-08-05, CLOSED 2026-08-13, with an explicit statement that everything after the close is post-window and labelled. Original text: against the 2026-08-05 open.
      The 7-day target was 2026-08-12; the hard maximum is 2026-08-19.
- [x] ~~Final-day change sweep~~ **DONE 2026-08-17 (D-076)**: 42 of 76 pricing pages have 2+ in-window captures and could be tested at all; of those only 28 span 24h and 4 span a week, and the report leads with that denominator. Four vendor edits found, none leaving a stale coded value — the one that added a quantified cap did so before our read. Two products differ by geography rather than time, typed `display_variant` per §6.8. **No headline price and no tier name changed inside the window on any testable page.** Original text: check whether any coded vendor page changed materially during the
      window, and log any sighting as a register event per protocol section 6.8.
- [x] ~~**Per-record attribution of `unknown` values (D-018).**~~ COMPLETE (D-043/D-048/D-051): 550/550 attributed, 128 by hand with written reasons. Original text: 23 completed records carry
      unknowns alongside access-failure language in their notes — 20 of 76 in pass 1, 3 of 16 so far
      in pass 2. That is co-occurrence, not causation. Read each by hand and attribute every unknown
      to EITHER vendor silence OR our inability to read the document, then report the two separately.
      The study's headline quantity is vendor silence, and any share of it that is actually our
      access must not be counted as the former.
- [x] ~~**Limitations register — add the A/B-test finding**~~ DONE 2026-08-17, into §7 rather than as a new section, since §7 already covers client-side variance. Original text: **Limitations register — add the A/B-test finding.** A pass-2 coder found a pricing page
      running a cookie-consent-gated A/B test (`pricing-ab.js`): declining analytics cookies
      deterministically served the control arm. It then fetched the treatment fragment and
      confirmed both arms carry identical headline price, billing basis and credit allowances, so
      nothing coded is affected. The methodological point survives anyway and belongs in the
      limitations: where a vendor A/B-tests its pricing page, **"the default display state" is not
      a single fact about the vendor** — it is a fact about which arm the reader was assigned.
      Section 6.8 tells a coder to record the state it observed, which is right, but wave 2 should
      check for test machinery explicitly rather than relying on a coder noticing the script.
- [x] ~~**Refresh every computed figure in `limitations-register.md` against the frozen data**~~ DONE 2026-08-17 at freeze: §2's adjudicator count 24→29, §4's whole attribution table (550→581 unknowns, 128→221 by hand, and the publishing-row column added beside the all-records one), §9 given the three for-cause agreement figures, §10's heading 71→76. §3 and §5 verified correct. Every figure re-derived from `agreement.py`, `attribute_unknowns.py`, `build_dataset.py` and the archive ledger, then diffed against the prose. The register's header now states plainly that figures are derived by tools and typed by hand, and that the freeze is what stops them moving. Original text: **Refresh every computed figure in `limitations-register.md` against the frozen data, as the
      first step of the freeze — not from memory.** Added 2026-08-17 because the register was found
      carrying three stale figures at once: §4's attribution table still read 550 unknowns / 463
      vendor silence / 128 by hand when the counts were 564 / 286-on-publishing-rows / 207, §5's
      provenance table still read 377 of 511 before the archive recovered, and §10's heading still
      said fifty-eight deviations at seventy-one. **None was wrong when written.** Every one went
      stale because the data moved underneath a hand-written number, which is the whole argument for
      computing published figures rather than typing them.
      The register's own header promises "every figure here is computed from the frozen records by a
      tool in `tools/`" — that promise is currently kept by hand, and the honest options are to keep
      it by hand at freeze time or to build the checker. **At minimum: re-derive §3, §4, §5, §9 and
      §10 from the tools and diff against the prose before stamping.**
- [x] ~~Freeze the dataset and stamp it~~ **DONE 2026-08-17**: `orchestrator/freeze-stamp.md`, generated by `tools/freeze_stamp.py` so every figure and every SHA-256 is READ from the file it describes rather than typed — the defect this checklist item was written above having just been caught three times. Records frozen: 76 pass-1, 26 pass-2, 29 adjudicated, 3 for-cause, 5 quarantined. 2,812 coded values, 337 unknowns all attributed, 516 cited captures with 482 resolving, 76 deviations. After this point a correction is a published erratum, not an edit.

## 8 · Disclosure — what the paper must carry

- [x] ~~**DISCLOSE WHO THE CODERS WERE**~~ WRITTEN 2026-08-17: `methods-who-coded.md`, with the reliability figure's meaning, the 3.0% third-reading reversal rate, the correlated-error evidence, and a venue note on why no peer review raises the stakes. Original text: — the highest-priority open item, and it is not in the data.**
      The methods documents contain ZERO mention of language models, agents or automation: they say
      "a coder" throughout, which reads as human. So the reliability figure reads as human
      inter-coder reliability, and it is not that — it is agreement between two independent model
      readings, which may be better or worse but is not the same thing, and a reader must be told.
      Needs its own methods section: who coded, under what protocol, what alpha 0.811 does and does
      not establish, and why agreement between model readings is still informative. A reviewer who
      discovers this after publication has grounds to question everything else. The study has strong
      material for it — three adjudicators disclosed their own breaches, a commissioned audit moved
      the headline nine points against us, and independent readers repeatedly caught each other.
- [x] ~~All deviations in the methods section, dated~~ **DONE**: `paper-draft.md` §3.9, as a class table with the log cited rather than 78 entries reproduced. The count is re-derived before publication (see the step below) precisely because this line itself carried 56, then 71, while the log moved to 78. Original text: All **71 deviations** (D-001 … D-072, two numbers unused) in the methods section, dated, with
      what each one changed. **Count updated 2026-08-17 — it read "56 deviations (D-001 … D-056)"
      until then, and had been stale for sixteen entries.** Six were the orchestrator's own defects
      when that sentence was written (D-014, D-015, D-016, D-017, D-020, D-021) and two of those
      retracted a published claim; the closing days added more, including D-063 retracting D-060
      outright, D-065 and D-067 where a rule I delivered mid-task made a coder wrong in opposite
      directions, D-068 where a validator had been examining zero records, D-071 where I scoped two
      adjudications from a report instead of a diff, and **D-070, whose own entry had to be corrected
      the same day for overstating the defect it described.** Several are corrections to our own
      instrument, including two where the orchestrator's own reasoning was wrong (the D-007 drafting
      error, and D-009's inference that earlier records were likely misread — a 25-record check found
      zero changes).
      **Do not re-derive this count by hand at write-up time; run `grep -cE "^## D-" on the log.**
- [x] ~~The blindness record~~ **DONE**: `paper-draft.md` §3.6, with the three for-cause codings reported separately at 63.9% / 75.0% / 83.3% and their decomposition. Original text: The blindness record: **6 breaches, 6 self-disclosures**, and the for-cause set
      (faceless-so, gptzero, squarespace, humanizemy, google-veo). Every breach in this study was
      reported by the agent that committed it, two of them about the orchestrator's own
      instructions. The disclosure rate is reported alongside the breach count, because a study
      that only counted breaches would look worse the more honest its coders were.
- [x] ~~The **tooling failure modes**, as a methods note other researchers can use~~ WRITTEN 2026-08-17: `methods-tooling-failure-modes.md` — 34 numbered modes in four groups, each having actually happened here and dated in the log, plus a closing section on what actually caught them (a total exceeding a known denominator; two readings of one file disagreeing; an agent reporting against its own interest; a blunt question from someone who had looked). Original text: formatted-price
      misreads that no plausibility check catches, and outright **fabrication** by summarising
      fetches — two instances, where invented structure contradicted the verbatim DOM.
- [x] ~~The frame's two stale statuses~~ **DONE**: `paper-draft.md` §4.8 — "Two products the frame called active had already been discontinued, and how they were found matters." Original text: The frame's two stale statuses (openai-sora, lovo-ai), how they were found, and the honest
      verdict that the freeze-time check was blind to vendors that collapse without announcing it.
- [x] ~~The independent audits~~ **DONE**: `paper-draft.md` §6.4, which also carries what replaces peer review for a self-published study. Original text: The **independent audits**: a second session, run by the owner on the same task, checked the
      D-014 remedy and then the pass-2 briefs and then the log's numeric claims. It found a missed
      contaminated record, a false positive on the exposed list, an overstated control group, and
      two inaccurate claims in D-013. It also disclosed that its own first measurement of the D-012
      rate used a wider surface than the claim and returned 64% before being re-measured against the
      claim's own definition at 32% — the same failure mode it had just found in my work, caught
      because the failure mode had been named. The reliability section reports the audits AND that
      near-miss. An auditor described as clean is less credible than one that says where it slipped.
- [x] ~~**Re-derive the deviation count in `paper-draft.md` immediately before publication.**~~
      **AUTOMATED 2026-08-18 — `tools/check_published_figures.py`.** The manual version of this item
      failed on the day it mattered. Publishing moved the count to 79 and a hand-run grep, phrased
      too narrowly, reported the paper clean while five statements of "78 dated deviations" survived
      — two in the paper, three on the site including the summary that renders on the listing page.
      A promise to remember is not a control. The checker computes each figure from the data, finds
      every phrasing the study actually uses across paper, site copy, freeze stamp, register,
      analysis and press kit, and **fails when a concept matches nothing at all**, so a rewording
      cannot quietly blind it. 39 stated figures across 7 surfaces currently agree with the data.
- [x] ~~Owner sign-off on the frozen dataset before anything is published.~~ **SIGNED 2026-08-18 by Mucahit Kaya**, founder and editor, the named human in the study's AI-assistance framing. He set the research question before any data existed, approved the protocol, sampling rules and codebook, ratified the frozen frame, intervened on substance during the work — **two of the largest corrections in the study came from those interventions rather than from any automated step** (D-050, D-056/D-057) — and reviewed the frozen dataset, the paper and the open release before signing. Nothing here is published on automated authority.

## 9 · Then, and only then

Analysis → figures from real data → preprint (ResearchGate/Zenodo, DOI) → open dataset (CC BY 4.0)
→ the site's Research page moves from "In build" to "Live" → companion Analysis piece → corrections
to any of our own published reviews the data contradicts.
