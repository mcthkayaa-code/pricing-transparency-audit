# Deviations log — Pricing Transparency Audit

Recorded per protocol discipline: every process deviation is logged, dated, and carried into
the paper's methods section.

## D-001 · 2026-08-06 · faceless-so pass-1 blindness breach (disclosed by coder)

- What happened: the pass-1 coder read another product's completed pass-1 record
  (aragon-ai.yaml) to confirm YAML structure, violating the blindness rule. Self-disclosed
  prominently in the record's coder_note.
- Assessment: all coded values trace to faceless.so's own documents; exposure risk is
  presentational/judgment-style anchoring, not product-fact contamination. No same-product
  pass-1/pass-2 exposure occurred.
- Decision (orchestrator, ratified for owner review): record RETAINED; a FOR-CAUSE blind
  second coding of faceless-so is added. Its agreement result is reported separately from
  the pre-registered double-coded set so the planned statistics stay uncontaminated.
- Prevention: collector instructions amended — the record schema is fully specified in the
  assignment; opening any other record is never necessary and the completeness check now
  includes an explicit no-other-records attestation.

## D-002 · 2026-08-07 · Four frame rows carried a schema.org type URI as `vendor_home_url`

- What happened: the freeze script derived `vendor_home_url` from each review's `entitySameAs`
  list, taking the first non-encyclopedia entry. For colossyan, fotor, freepik and pixlr that
  entry was `https://schema.org/SoftwareApplication`, a type URI rather than a vendor site.
- Detection: the fotor pass-1 coder reported the bad URL, located the official domain, and
  documented the correction. An audit of all 76 rows then found exactly four affected.
- Assessment: no coded value is affected. The frame's identity keys (`product_id`, product name,
  category, status) were always correct, and coders are instructed to locate and document the
  official domain when the frame URL fails. The colossyan and fotor records were both coded from
  the correct official domains.
- Decision: the four `vendor_home_url` cells are repaired in place, each with a dated
  `frame_note`. This is a convenience-field repair, not a frame change: no product enters or
  leaves the frame, and no identity key moves. Sampling rules section 3's never-edit rule binds
  the frame's membership and identity; a demonstrably wrong lookup URL is corrected in the open
  rather than left to mislead a later coder or a dataset reader.
- Prevention: wave 2's freeze script must filter type URIs (`schema.org/*`) and encyclopedia
  entries when deriving a vendor home URL, and flag any row it cannot resolve.

## D-003 · 2026-08-07 · Geo-localized pricing pages can produce false `non_usd` codings

- What happened: the framer pass-1 coder found the vendor's pricing page rendering entirely in
  Turkish Lira and coded `headline_price_usd = non_usd`. The collection environment egresses
  from Turkey, so the page state reflects the collector's location, not the vendor's disclosure
  practice. A vendor that publishes USD to a US reader would be recorded as publishing no USD
  price, which measures our network rather than the product.
- Scope: two records carry `non_usd`. Verification with an en-US request found aiva genuinely
  EUR-only (a real vendor characteristic, correctly coded). framer is affected and goes to
  adjudication for its currency-dependent A-domain variables.
- Rule addendum, binding for the rest of the window and consistent with protocol section 6.8:
  before coding any currency variable `non_usd`, the coder performs one independent US-locale
  check (an `Accept-Language: en-US` request, or the page's most recent Wayback capture, which
  is crawled from the US). Where that check shows a published USD figure, the USD figure is
  coded and the locally observed currency is logged as a `display_variant` register event.
  Where both states show no USD, `non_usd` stands and the check is recorded as evidence.
- Prevention and disclosure: the limitations register gains an entry stating that collection
  ran from a single network location, that geo-localized pricing was detected during the
  window, and how it was handled. The instrument is unchanged; this is a collection-procedure
  clarification recorded before analysis, not a variable redefinition.

## D-004 · 2026-08-07 · gptzero pass-1 blindness breach (disclosed by coder), and the real fix

- What happened: the pass-1 coder opened `records/pass1/copyleaks.yaml` to see the record
  schema, the same failure mode as D-001. The coder disclosed it in `coder_note` and in a
  top-level `blindness` field rather than attesting falsely, and confirmed every GPTZero value
  traces to GPTZero's own sources.
- Assessment: values are document-sourced; the exposure is presentational. No same-product
  pass-1/pass-2 contact occurred.
- Decision: record RETAINED; a FOR-CAUSE blind second coding of gptzero is added, reported
  separately from the pre-registered double-coded set, as with faceless-so under D-001.
- Root cause and real prevention: after D-001 the instruction set required an attestation. An
  attestation makes a breach visible; it does not remove the reason for it. Coders opened
  another record because they needed the record SHAPE and had no other place to see it.
  `record-template.yaml` now ships an empty, fully-commented skeleton in the study directory,
  and the collector brief points at it. The need is gone, so the rule can hold.

## D-005 · 2026-08-07 · Static-fetch coding produced false `unknown` prices (owner-detected, MATERIAL)

- What happened: three records (canva, gamma, gptzero) coded `headline_price_usd = unknown`
  because no price appeared in the served HTML, the archive captures, or the embedded page
  payload. The owner opened one of those pricing pages in an ordinary browser and read the
  prices plainly. Orchestrator verification confirmed it: gptzero.me/pricing renders
  TRY 549/month and TRY 1,049/month once the page's own scripts run.
- Why this is material, not cosmetic: the study asks whether a consumer can determine a
  product's cost before paying. A consumer uses a browser. Coding `unknown` for a figure that
  any visitor can read measures our fetch tooling, not the vendor's disclosure. Published as
  it stood, the finding would have been indefensible on first inspection by any reader with a
  browser, and it would have inflated the study's central quantity, the unknown burden.
- Rule clarification, binding for the rest of the window: loading a public page and letting
  that page's own scripts render is READING A DOCUMENT, and is inside the documents-only
  method. Protocol section 6.3 prohibits account creation, login, checkout, card entry, trial
  activation, product use, and vendor contact; it never prohibited rendering. A coder may code
  `unknown` for a price only after a rendered read of the pricing page also shows none. Where
  the rendered read supplies the figure, its state is recorded per section 6.8 and the D-003
  currency check applies to it as to any other read.
- Remedy: canva, gamma and gptzero are re-collected as fresh pass-1 records under the corrected
  rule. Their superseded records remain in version history and the substitution is dated here.
  Any other record whose A-domain was coded `unknown` for the same reason is re-collected the
  same way; the validator run at analysis time lists them.
- Withdrawn: adjudication items A-007 and A-008 proposed naming "price rendered but never
  documented" as a finding class. That framing was the orchestrator's, and it was wrong. It is
  withdrawn rather than argued down, and the queue records the withdrawal.
- Credit: detected by the owner during routine review, not by the instrument. Recorded because
  the paper's reliability section should say plainly which checks caught which errors.

### D-005 remediation closed · 2026-08-08

All three affected records were re-collected under the corrected rule, and the correction
changed substantive findings rather than merely filling blanks:

- **gptzero** — the rendered read exposed a cheaper plan invisible to static fetching, so the
  entry tier moved from Professional to Premium, the headline price resolved, and
  cost-per-output became computable from an official overage rate.
- **canva** — the entry tier resolved to Pro on a real annual-equivalent comparison against
  Business, four A-domain variables moved off `unknown`, and a defect carried from the
  superseded record was fixed (`refund_policy_location` held a value belonging to a different
  variable's list).
- **gamma** — six blocked variables resolved on a live rendered read, and the currency check
  showed prices already in USD with only the interface localized, which is why D-003's check
  is run mechanically rather than assumed either way.

Superseded records remain in version history. The re-collections are dated in
`collection-status.md` and each record's `coder_note` carries its own changed-versus-superseded
diff.

## D-006 · 2026-08-08 · YAML boolean coercion silently split coded values in two

- What happened: records are written as YAML, where an unquoted `yes` or `no` parses as a
  boolean rather than a string. Nine of thirty-six pass-1 records carried 71 coded values in
  boolean form, so the same value — `yes` on `free_plan_exists`, say — was stored as `yes` in
  some records and as `True` in others.
- Why it matters: nothing on screen looks wrong, and every record validated. The damage would
  have appeared at dataset build, where the published CSV would carry two spellings of one
  value across eleven variables, and any tally grouping by value would split its own counts.
  It was found while sampling the cost-per-output distribution mid-window, not by a check
  designed to catch it.
- Remedy: `tools/normalize_booleans.py` quotes every boolean-parsed value inside the
  `variables:` block, canonicalizing to the codebook's `yes` / `no` and leaving prose,
  evidence text and every other field untouched. It is idempotent, it ran across all pass-1
  records (71 values in 9 files), and a re-audit found zero remaining. No coded MEANING
  changed: `True` and `yes` were always the same coded value, stored differently.
- Prevention: the normalizer runs over every record before the dataset is frozen, and again
  after pass 2 and adjudication. The record template shows quoted values so new records are
  written correctly from the start.

### D-006 addendum · 2026-08-12 · the boolean fix was scoped too narrowly and missed `paid_submission`

- Found by the sapling coder, which noticed that the RECORD TEMPLATE'S OWN `paid_submission: no`
  was parsing as the boolean `False`, and fixed it in its own record.
- Scope of the miss: D-006's normalizer quoted boolean-parsed values INSIDE the `variables:` block
  and nowhere else, so top-level administrative fields were never covered. **Sixteen records
  carried `paid_submission: False` instead of `"no"`**, seeded by the template itself.
- Why it matters rather than being cosmetic: the study reports index results both with and without
  paid-submission products, so that field decides which rows enter the "excluding paid submissions"
  figures. Two spellings of one value would have split those counts — the exact harm D-006 named,
  in the one field where it would have hit a headline number.
- Remedy: `normalize_booleans.py` now also fixes the named top-level admin fields; it ran across
  all records (16 values), every record still parses, and a re-audit finds zero YAML booleans
  anywhere. The template is corrected and now says explicitly to quote the value and why.
- The lesson is the same one D-010 taught hours earlier: a fix aimed at where a defect was first
  seen, rather than at everywhere the defect can occur, leaves the rest of the surface untouched
  and passing every check. Both were caught by a coder or a screen, not by the original fix.

## D-007 · 2026-08-10 · The D-003 currency check could not do what it claimed, and `non_usd` rested on it

- What happened: the phrasly coder ran the D-003 check honestly and both of its arms failed for
  technical reasons — the `Accept-Language` request was refused by the vendor's bot wall, and
  the most recent Wayback capture returned pre-hydration markup carrying no prices. Under
  D-003's closing clause ("where both states show no USD, `non_usd` stands") the coder recorded
  `non_usd`. Reviewing that record, the orchestrator found the rule itself was unsound.
- Why the check was unsound: an `Accept-Language: en-US` header states a language preference.
  Vendors that localize currency overwhelmingly do it by **IP geolocation**, which that header
  does not change, so the first arm was never a US-locale test — it was the same Turkish-egress
  read with a different header, and any agreement it produced was not evidence. The second arm
  is sound in principle, because the Wayback crawler does read from US IPs, but it returns
  pre-hydration HTML on JavaScript-rendered pricing pages, which is precisely the population
  where the question arises. D-005 already established that these pages render their prices
  client-side.
- Why it matters: `non_usd` is a substantive claim about the vendor — that it publishes its
  price in some currency other than USD. D-003's closing clause let that claim rest on a test
  that had not run. Two different situations, "this vendor genuinely publishes no USD price"
  and "we were unable to look", were being written into the dataset as the same value on a
  headline variable, and every derived A-domain figure inherits it.
- Scope: six of forty-eight pass-1 records carry `non_usd` — aiva, canva, framer, freepik,
  gptzero, phrasly. aiva was independently verified EUR-only under D-003 and is expected to
  stand. framer and freepik already sit in the adjudication queue (A-003, A-005) for this same
  reason, which in hindsight was the first signal that the rule, not the records, was at fault.
- Rule amendment, binding for the rest of the window: documentary evidence of the vendor's own
  currency practice now leads, and the geo test is demoted to a fallback.
  1. Read the vendor's own currency disclosure: a currency selector on the pricing page, an
     explicit currency statement in billing or help documentation or in the terms, or a
     vendor-supported currency parameter. These are documentary reads under protocol section
     6.3 and outrank any inference drawn from which state our network was served.
  2. Failing that, a US-crawled archive capture that actually contains price figures.
  3. `non_usd` requires POSITIVE evidence — that the vendor publishes only a non-USD price, or
     that a US reader is served one. Where no arm returns readable evidence, the variable is
     coded `unknown` with the attempted checks recorded, because "we could not look" is a
     statement about our evidence and `unknown` is the value for it. The `Accept-Language`
     request is no longer sufficient on its own and is not recorded as a US-locale check.
- Remediation, run inside the window: all six `non_usd` records are re-checked under the
  amended rule before the window closes. This is deliberate — protocol section 6.8 fixes
  observation to the collection window, so a re-check performed after the window would be
  reading pages the study does not cover. Whatever the sweep changes is recorded per record.
- Standing: the instrument is untouched. No variable is redefined and no value is added or
  removed; what changed is which evidence supports which existing value. Like D-003 and D-005
  this is a collection-procedure correction recorded before analysis.
- Disclosure: the limitations register entry created under D-003 is extended to state that the
  original check was inadequate, when that was found, how many records were affected, and what
  the re-check changed. The paper reports the corrected figures, not the first ones.

### D-007 sweep result · 2026-08-10 · five of six records changed, and the rule's own wording needed fixing

- Outcome across the six `non_usd` records. **aiva** confirmed EUR-only, now on positive evidence
  (a content-bearing US-crawled capture showing EUR and no `$`) instead of an absence-only check.
  **framer** became `10.00` / `120.00` USD and **freepik** became `14.50` / `174.00` USD — in both
  cases the USD figures were already sitting in an archive capture the record had collected and
  never opened, because the superseded rule could not credit an archive over a live same-network
  read. **gptzero** and **phrasly** became `unknown`: each vendor's terms state unconditionally
  that payments are in US dollars, which directly contradicts a clean `non_usd`, but no document
  states the USD figure for the tier. **canva** is being re-examined, below.
- So the superseded rule produced a value that was wrong or unsupported in four of the six records
  it governed. Two asserted that a vendor publishes no USD price when the study's own evidence
  showed otherwise. That is the cost of letting a substantive claim rest on a test that had not run.
- Both money variables moved together in every record — never a mixed outcome — and where a value
  became a real figure the dependent cost-per-output computation was recomputed in USD with the
  superseded arithmetic kept rather than deleted.
- **A drafting error in D-007 itself, found by applying it.** The amended rule was written into two
  places with two different tests. The agent definition asked for evidence that the vendor publishes
  a non-USD price "to the reader"; this log asked for evidence that "a US reader is served one".
  The sweep agent applied the agent-definition wording faithfully and, on that test, kept canva at
  `non_usd`: Canva's help centre states local-currency billing by default with USD as the fallback
  where the local currency is unsupported, and TRY is actively served to us. Read against a US
  reader, that same policy means Canva bills a US reader in USD. The agent-definition wording has
  been corrected to match this log, which is the authoritative record and the one consistent with
  D-003's founding purpose — that a page rendered in local currency may be measuring us rather than
  the vendor. canva returned to the sweep agent for re-examination under the corrected test, with an
  explicit invitation to disagree on the record rather than change a value to match an instruction.
  It re-derived the question independently before writing anything, and agreed. Canva's "USD only if
  your local currency is unavailable" flips outcome depending on whose local currency the policy is
  read against: for our Turkey-based reader TRY is available so the fallback never triggers, which
  is what supported the original `non_usd`; for a US reader USD *is* the available local currency,
  so the same policy puts them in the ordinary case, meaning the vendor does not publish only a
  non-USD price and a US reader is not served one. Arm 2 still returns no readable capture, so no
  figure exists to code as money. **canva is `unknown` on both money variables**, the TRY state is
  logged as a `display_variant` register event, and the record now matches the structural pattern
  already applied to gptzero and phrasly — a real currency fact with no matching figure. The
  original pass reasoning is preserved in `coder_note` rather than overwritten, and the sweep report
  carries its own section naming the drafting error.
- Final tally: **five of six records changed.** Two became real USD money values, three became
  `unknown`, one was confirmed.
- The deeper question that error exposed is now **A-013**: whether the currency variables are
  vendor-centric or reader-centric where a vendor's stated practice is genuine local-currency
  billing. Both readings are defensible and they score differently. Pass 1 codes vendor-centrically
  so the class stays internally consistent and adjudication can flip all of it together.
- Adjudication items **A-003** (framer) and **A-005** (freepik) were opened for exactly this
  currency problem and are resolved by the sweep: both now carry real USD figures from official
  archived vendor pages. They are marked resolved rather than deleted, so the queue keeps its
  history.

## D-008 · 2026-08-10 · The frame's status re-check missed a product that had already shut down

- What happened: the openai-sora pass-1 coder found the vendor's own page reading "Sora is no
  longer available", and OpenAI's help centre dating the shutdown of the web and app
  experiences to **2026-04-26**, with the API sunsetting 2026-09-24. The frozen frame carries
  `product_status = active` for that row.
- Why it is a freeze defect and not a mid-window event: sampling-rules section 10.4 already
  covers a product that shuts down DURING the window (it moves to `discontinued`, dated and
  reported). This shutdown predates the 2026-08-04 freeze by more than three months, so the
  frame was wrong at the moment it was frozen. Sampling-rules line 122 states that status is
  re-checked for every product at freeze precisely so a shutdown since review publication is
  caught; for this row that re-check did not happen or did not register. The same class of
  defect as D-002, which found four rows carrying a schema.org type URI as `vendor_home_url`.
- What it would have cost if it had gone unnoticed: 24 of that record's 37 coded variables are
  `unknown`, because the product's pricing surfaces are gone and its Billing and Credits FAQ
  now 404s beyond archive recovery. Scored as an active product, that record would have entered
  the index as a near-total transparency failure and dragged the aggregate down — measuring a
  dead product's missing pages rather than any vendor's disclosure practice. The instrument
  already protects against this: protocol D8 and sampling-rules section 6.2 exclude
  discontinued products from every aggregate and from the index and report them in a separate
  table. The defect was in the frame's status field, not in the analysis.
- Correction: the row moves to `discontinued` with the vendor-documented shutdown date, annotated
  in place with a dated `frame_notes` entry exactly as D-002's repairs were. The record itself
  stands as coded — a discontinued product coded from archived materials is what section 6.2
  asks for — and joins playht in the discontinued stratum. Active-product counts drop by one.
- Systemic remediation: one row failing a freeze-time check means the check cannot be assumed to
  have run on the other 75. A status verification sweep now runs across the frame while the
  window is open. It covers every product not yet collected, plus the collected records whose
  coders met hard failures that a dead product would also produce — lovo-ai, whose entire domain
  returned HTTP 402; midjourney, whose own /pricing and /plans returned 404; and freepik, which
  rebranded to Magnific mid-window (A-006). Products already coded from a live pricing page that
  sells plans are evidenced as active by that coding and are not re-checked.
- Standing: the instrument is untouched. `product_status` is an administrative frame field, its
  two values and their consequences are unchanged, and no coded variable is redefined. What is
  corrected is a factual error in the frame.
- Disclosure: the paper reports that the frame carried one stale status at freeze, how it was
  found, that a sweep followed, and whatever the sweep changed. The discontinued table names
  every product in it with its shutdown date and how the date was documented.

### D-008 sweep result · 2026-08-10 · one further correction, and a failure mode the check was never built for

- Coverage: 31 rows checked — the 28 products with no completed pass-1 record, plus lovo-ai,
  midjourney and freepik, whose coders met failures a dead product would also produce. Products
  already coded from a live pricing page that sells plans were treated as evidenced active by
  that coding and not re-checked. Full table in `d008-status-sweep.md`.
- Result: 30 rows confirmed, 1 changed, 0 inconclusive. playht's existing `discontinued` was
  confirmed. midjourney is active — its 404s on /pricing and /plans are a homepage redesign, and
  the plan table in its documentation still carries the prices the pass-1 record cites. freepik
  is active under the Magnific rebrand, matching the A-006 treatment.
- The change — **lovo-ai moves to `discontinued`.** LOVO, Inc. filed **Chapter 7** liquidation on
  **2026-05-27** (S.D.N.Y. case 26-11249), reported consistently by MLex, Law360 and Bloomberg
  Law and listed by a public docket aggregator; the district court stayed the voice-actors class
  action on the bankruptcy notice. The entire vendor domain returns HTTP 402 with
  `x-vercel-error: DEPLOYMENT_DISABLED` on every path, observed on three separate days by two
  independent checkers. The filing predates the 2026-08-04 freeze by over two months, so this is
  the same class as the openai-sora finding: the frame was wrong when it was frozen.
- On the evidence standard, stated plainly because a referee will ask: the sweep agent flagged
  this row rather than changing it, correctly, because there is no statement in LOVO's own words
  — the 402 page is generic hosting text, not vendor prose. The orchestrator changed it anyway,
  on two grounds. First, protocol section 6.2's "official vendor sources only" rule governs
  **coded variables**, which are claims about what a vendor discloses; `product_status` is an
  administrative frame field, a claim about the world, and it takes the best available evidence.
  Second, a Chapter 7 petition is not third-party commentary — it is a primary document filed by
  the vendor itself, and what the legal press reported is its docket entry. Sampling-rules 6.2
  defines `discontinued` as the vendor having stopped offering the product, announced a shutdown,
  **or ceased operating**; a liquidation filing plus a dead storefront is the third of those.
- What the sweep says about the freeze-time check, without softening it: against the failure mode
  it was designed for — a vendor that announces a shutdown on its own site — the check looks
  broadly sound, since all 30 other rows confirmed cleanly. Against a different failure mode it
  was never built for — a vendor that collapses and simply stops paying its hosting bill, posting
  no announcement anywhere — it failed. Both rows it missed, openai-sora and lovo-ai, are of that
  second kind. A future wave's freeze procedure should test liveness directly rather than look
  only for announcements.
- Sampling consequences: the frame now reads 73 active and 3 discontinued (lovo-ai, openai-sora,
  playht). **The reliability sample is untouched** — none of the three is in the double-coded set,
  so no re-selection is needed and no blindness question arises. The double-coded share of active
  products moves from 26/75 (34.7%) to 26/73 (35.6%), still at or above the pre-registered target.
- The lovo-ai record stands exactly as coded. It was collected from archived materials because the
  domain was already down, which is what section 6.2 asks of a discontinued product; only its
  `product_status` line changes, annotated in place.

## D-019 · 2026-08-15 · The administrative-enum guard was blind to eight records, and the drift under it was wider than the field it checked

- What happened: the D-015 addendum's guard, once running live, reported zero enum violations across
  the corpus. That was true and misleading. It read `record["coder_role"]` at the top level only, so
  it could not see the two ways a record can fail without holding a wrong value: **five pass-1
  records stored `coder_role` INSIDE `variables{}`** in `{value: primary}` wrapper form (10web,
  aragon-ai, canva, faceless-so, ismybrandinai), and **three had no `coder_role` key at all** (aiva,
  d-id, fotor). The guard's `role is not None` test permitted absence by construction. Eight of 76
  passed trivially.
- Why that is the same harm, not a lesser one: D-015 recorded that a build selecting rows by role
  would silently miss eleven pass-2 records. A build reading top-level `coder_role` would today miss
  these eight pass-1 records. Different cause — misplacement and absence rather than a misspelling —
  identical consequence, and the guard written to prevent the consequence could not see either.
- **The drift was wider than the field that surfaced it.** Checking the five nested records for one
  administrative field showed that **ten of the thirteen export columns** were nested there, 50 field
  instances in all: `product_name`, `category`, `product_status`, `paid_submission`,
  `entry_tier_name`, `coder_role`, `recheck_date`, `primary_source_url`, `archive_url`,
  `archive_status`. Repairing `coder_role` alone would have converted "row silently dropped by the
  role filter" into "row present with nine blank export columns" — the quieter failure of the two,
  and a worse one to leave for a reader to notice.
- A second administrative field was drifting unchecked beside it. `coder_pass` is defined by the
  template as `1|2`; across pass 1 it was stored **62× as `1`, 12× as `'primary'` — a ROLE value in
  the PASS slot — and twice not at all** (apify-robots-checker, heygen). That is very likely the
  mechanism behind the three absent roles: all three of aiva, d-id and fotor carried
  `coder_pass: primary` and no `coder_role`, the two fields collapsed into one. Nothing checked
  `coder_pass`, so it had drifted three ways in silence.
- **A correction to this study's own checklist, found on the way.** The pre-freeze checklist recorded
  `archive_status` as UNSET on six records and instructed a coder to "set each from what that
  record's sources actually show; do not guess." For five of the six the value was not unset — it was
  nested and populated with `archived`, canva's carrying a full evidence paragraph on why its price
  content is local-only. Following the checklist as written would have sent someone to re-derive a
  value that already existed, and put canva's prose at risk of being overwritten. Only **aiva** is a
  genuine gap. The checklist item is corrected in place, with the original wording struck through so
  the misdiagnosis stays visible.
- Decision: **the records are repaired, and the contrast with D-010 is deliberate.** D-010 declined
  to touch `julius-ai` because the difference was parser-INVISIBLE — quoted versus bare, the identical
  string once parsed — and because `computation_assumptions` carries coder prose that line surgery
  endangers. Neither reason reaches here. This defect is parser-VISIBLE in the worst direction: a
  parser reading the documented location returns `None`. And the values were never in doubt — every
  record under `records/pass1/` is pass 1 by construction, the five nested ones already said
  `primary`, and the three absent ones carried `primary` in the pass slot. Recovering a determined
  value is not the same act as rewriting a coder's prose.
- **Method, chosen against D-010's failure rather than around it.** D-010's normalizer moved nested
  blocks by line surgery, matched more records than intended, and produced invalid YAML in eight
  files. So the nested maps were **not moved and nothing was deleted**: top-level scalars were added
  beside them and the `{value, source, evidence}` maps left exactly as they stood. Appending a scalar
  cannot break the nesting it sits above, so that failure mode is structurally unavailable. The
  duplication is deliberate and disclosed — D-010 already accepts dual-shape records — and it costs
  nothing that a build reading the top level will notice. Every edit was made by exact-match hand
  edit, proved on 10web first, and parse-checked after each file.
- What changed, 19 records in total: 5 records gained 10 top-level administrative scalars each;
  aiva gained `entry_tier_name` (lifted from its nested map) and an in-file note naming the five
  fields it still genuinely lacks; 3 records gained `coder_role: primary`; 12 records had
  `coder_pass: primary` corrected to `1`; 2 gained a missing `coder_pass: 1`. **No coded variable
  was touched, no nested map was altered or removed, and no value was invented.** Post-state: all 76
  pass-1 records carry `coder_pass: 1` and `coder_role: primary`; all 12 export columns now read at
  the top level on every record but aiva, whose five remaining gaps are recorded rather than filled.
- Standing: the instrument is untouched. No variable is redefined and no coded meaning is affected —
  this is a storage-placement defect, as D-010 was, not a measurement one.
- Prevention: `check_admin_enums` now checks **placement as well as membership**. A field nested in
  `variables{}` fails even when its value is valid; an absent `coder_role` or `coder_pass` fails; a
  top-level value that disagrees with a nested one fails; and `coder_pass` is checked against `1|2`
  on the same footing as `coder_role`. Verified the way the original guard was not: the pre-fix
  records were restored from git and run through it, and it rejects all four defect classes while
  passing a conforming control. D-015's original `secondary` case is kept as a regression check.
- The lesson, which is D-015's own lesson turned on its author: that entry closed the gap where a
  field held a WRONG value and left open the gaps where a field was in the wrong PLACE or absent
  entirely. A guard that reads one location certifies that location, not the field. Both times the
  guard passed everything and both times the defect was still there — the first found by a coder,
  this one found by running the guard and asking what it could not see. **Zero violations is a claim
  about a check's reach before it is a claim about the data.**

## D-012 · 2026-08-12 · A third of records have no independent archive capture, and our own concurrency is part of why

- What happened: the teal coder reported that every one of its five sources fell back to
  `local_copy_only` — the Wayback save endpoint returned "Job failed", the availability API
  returned 429, and static fetches to the vendor were 403. A sweep across the completed records
  found the pattern is not isolated: **20 of 64 (31%) carry `local_copy_only` or an archive
  failure, 38 are archived, and 6 leave `archive_status` unset entirely.**
- Why it matters: the study's evidentiary claim is that specific documents said specific things on
  specific dates. A third-party archive capture is what lets a reader verify that WITHOUT taking
  our word for it. A local copy is our own word, timestamped by us. Both are honest, but they are
  not equally checkable, and a paper that does not distinguish them is overstating its provenance.
- Mechanism, including our share of the blame: some failures are vendor-side (Cloudflare and bot
  walls return 403 to the archiver as readily as to us, and archive.org's crawler is served
  interstitials by several of these vendors — canva's captures are all its "Unsupported client"
  page). But the 429s are ours: running several collectors concurrently, each submitting save
  requests, rate-limits us against a shared service. Concurrency bought throughput and cost
  archival coverage, and that trade was made without being noticed until now.
- Remedy, and its limit: a post-collection archival retry is planned for the 20 affected records,
  run after the window closes when nothing else is competing for the service. It is explicitly a
  PARTIAL remedy and its captures will be labelled post-window, because a capture made later
  documents the page as it is then, not as it was when coded — protocol section 6.8 fixes
  observation to the window and a late capture cannot be substituted for the coded read. The local
  copy stays the coded evidence in every case. The retry should also query the availability API for
  captures made by OTHER crawlers near our access dates: those are contemporaneous and are the only
  kind that genuinely closes the gap.
- The 6 records with `archive_status` unset are a record-completeness gap rather than an archival
  one, and go on the pre-freeze checklist: the field is administrative and the validator does not
  require it, which is why they passed.
- Disclosure: the paper reports the archived / local-only / unset split as a stated limitation,
  names the mechanism including our own concurrency, and the published dataset marks each source's
  archival state per record so a reader can see exactly which claims they can independently check.
  This is not a defect to bury — the honest number is the interesting one.
- **Re-measured at final N (2026-08-14), prompted by an independent audit.** At N=76: **45 archived,
  25 local-only or failed, 6 unset — 33%**, against 31% measured at N=64. Twelve further records
  moved the rate by two points, so this is a stable property of collecting from live vendor pages
  under these conditions, not an artifact of when the snapshot was taken. The paper reports it as a
  RATE with its denominator rather than as a one-off count, which is the stronger and more reusable
  claim. The six `unset` records are a record-completeness gap tracked on the pre-freeze checklist,
  not an archival failure.

## D-081 · 2026-08-18 · The paper claimed a DOI it does not have, and the owner has decided it does not need one

- What happened: the data-availability section read "Published under CC BY 4.0 with a DOI minted at
  publication." **No DOI was minted.** The sentence had been carried forward from the protocol, where
  it was a plan stated before collection began, into the paper, where it reads as a fact about a
  finished release. It went live and stayed live.
- Why it is the worst kind of error for this study specifically: it is an unverifiable claim about
  provenance in a paper whose entire subject is unverifiable claims. A reader who went looking for
  the identifier would have found nothing, in the one document that tells them to go and check.
- Why nothing caught it: every check built today compares a **number** in prose against the data.
  This was a claim with no number in it. `check_published_figures.py` is blind to it by construction,
  and so was every earlier sweep.
- What was done: the sentence now says no DOI has been minted, names what does identify the release
  (the repository and the freeze stamp's per-file checksums), and commits to naming one if that
  changes. The protocol and dossier are left as written — they stated an intention at the time and
  are frozen; the paper is where the claim had to be true.
- Owner decision, same day: **no DOI for now** ("gerekirse sonra"). Recorded here so the absence is
  a decision rather than an oversight.
- The class of defect, for wave 2: a promise made in a pre-registration is not automatically true in
  the report. Anything the protocol says the study *will* do needs checking against what it *did*
  before that sentence is repeated as fact.

## D-080 · 2026-08-18 · The freeze stamp invited readers to verify its hashes, and one of its own hashes was already wrong

- What happened: the stamp records SHA-256 for 16 artifacts so a reader can confirm the copy they
  downloaded is the copy that was frozen. Checking it against disk for the first time today,
  `methods-tooling-failure-modes.md` did not match. It had moved twice since the stamp was
  generated — once on freeze day, when the deploy that reported success while serving a stale
  artifact was written up, and once this evening, when the search-submission step was found to have
  published the section index without the paper.
- Scope, checked rather than assumed: **the other 15 match exactly** — `coded-values.csv`,
  `coded-long.csv`, `apti-scores.csv`, the protocol, the codebook, the sampling rules, the
  limitations register and the analysis. The freeze held for everything it was meant to hold. No
  coded value, attribution or index score moved.
- Why it matters anyway: the stamp does not merely record hashes, it *invites* a reader to check
  them, and a reader who accepted that invitation would have found a mismatch with no explanation
  attached. Unexplained drift in a document that exists to prove nothing drifted reads as tampering,
  which is worse than the drift.
- Why no check caught it: none existed. The stamp was a claim about the repository that nothing
  in the repository ever read back — the same defect this study has now logged in a dozen costumes,
  which is a tool, or in this case a document, asserting something nobody re-derived.
- What was done: the stamp now separates **frozen bytes** from **hashed but living** documents and
  states which mismatch is a defect and which is growth. The tooling register is a running account
  of how this study's own instruments failed and is meant to keep growing; freezing it would either
  stop it learning or falsify the stamp every time it did. It feeds no figure in the paper.
  `tools/verify_freeze.py` now checks the stamp against disk and exits non-zero on any frozen
  mismatch, so the invitation is tested rather than trusted.
- What it does not do: this does not reopen the freeze. It narrows a claim that was too wide, and
  the narrowing is disclosed here rather than absorbed into a regenerated file.

## D-079 · 2026-08-17 · The preprint draft audited every figure against the frozen data and found six more disagreements, two of them mine

`paper-draft.md` written. The brief told it that where two documents disagree on a figure it must
**stop and report rather than pick**, because that situation had already arisen five times here and each
was a real finding. It found six more, verified each against the frozen data, and carried them into the
paper as a methods subsection rather than reconciling them quietly.

| figure | conflict | frozen data |
|---|---|---|
| deviations logged | **77** in the freeze stamp's own table vs **76** in the stamp's own prose and the register heading; `methods-who-coded.md` still said **57** | 77 (D-001→D-078, D-024 vacated) |
| `instrument_gap` unknowns | 48 in the stamp and the register table vs 46 in the register prose and the findings note | **48**, of which one product carries 20 |
| paid submissions | the findings note said **four**; `apti-report.md` said **one** | **1 of 76** |
| primary IQR | 69.9–86.5 vs 70.0–86.4 | neither wrong — exclusive vs inclusive quartiles, ~0.2 pt apart. Both printed |
| raw two-pass agreement | 788 of 962 (81.9%) on `reliability-result.md`'s standalone headline vs 791 of 962 (82.2%) in its own tables | **791 of 962** — D-078's correction had missed that one line |
| pattern-set attributions | 393 in the failure-modes note vs 394 in D-048 | **394** (344 + 50) |

**And it correctly identified two apparent conflicts that are not conflicts**, recording them so nobody
"fixes" them: two documents compute two items over 72 scored products and 73 active ones respectively,
which is why one prints an exact 50/50 split and the other does not; and **24 and 29 adjudicators are
both true** — 24 from the pre-registered double-coded set, plus 3 for-cause and 2 late ones, giving the
29 adjudicated rows. Distinguishing a real disagreement from a denominator difference is the harder
half of that task and it did it.

### The two that are mine, and the worse one is a conflicts disclosure

**The freeze stamp typed a number it also computes.** Its table printed 77 from a direct count while its
prose said "Seventy-six deviations say otherwise" three paragraphs above — **inside the one document
whose entire purpose is to be right about its own contents**, written by me hours earlier in an entry
about typed figures going stale. The tool now interpolates that count instead of carrying it as prose,
and says so.

**And `analysis-first-findings.md` claimed "the four products that paid a listing fee do not sit
differently in the distribution."** There is **one**, and it scores 83.8, above the median. The count was
taken from a summary rather than read from `apti-scores.csv`.

That sentence was wrong twice over. The count is wrong, and **a group of one supports no claim at all
about how paid submissions sit in a distribution** — rule D3 bars a percentage below n=5 for exactly
this reason. It is now reported as a raw count with the product's score, and the correction is printed
beside it.

**Of everywhere in this study for an unverified number to appear, a conflict-of-interest disclosure is
the worst**, and it is the seventh instance of one defect in a single day: a figure derived by a tool,
typed into prose, and never re-derived.

### What that makes the day's tally

**Seven stale or unverified hand-typed figures, across six documents, in one day. Every one found by
re-deriving rather than by reading, and the last two by an agent instructed to check every figure it was
handed.** None reached publication. That is not evidence of care — it is evidence that the only reliable
detector for this class is mechanical re-derivation, and the study now says so in the register's header,
in the freeze stamp, and in the paper.

**The wave-2 item is unchanged and is now the highest-value one on the list**: a checker that diffs the
prose figures in the published documents against what the tools compute. Seven occurrences in one day
is the argument.

### On the draft itself

11,686 words against a 6,000–9,000 target, cut from 14,800 across three passes. It **stopped and flagged
the overrun rather than cutting mandated content**, and named the two sections it would cut first if the
call goes the other way. That is the right instinct and the decision is the owner's, not an agent's.

### D-079 amended · 2026-08-17 · a seventh instance, and it was in the fix for the other six

Found by the Turkish translation pass, which re-derived every figure in its slice from the English rather
than trusting it.

**Two places in §3.9 survived D-079's own correction sweep.** Its body still read "carries **77** numbered
entries" directly under a heading printing *Seventy-eight*, and its class table stopped at D-078 — no row
covered **D-079 itself**, the figure audit that §3.10 describes at length. Both fixed: the body count, and
the table's freeze-day-drift row now spans D-078 and D-079.

**This is the defect appearing inside its own remedy**, which is the sharpest form it has taken. Recorded
as an amendment rather than as D-080, deliberately: opening a new entry would move the count again and
re-trigger the exact problem, and this is the same audit finding the same class of error one pass later,
not a new event.

**And a second pass caught two substantive defects in the paper's §4.6**, both flagged as "the English
was ambiguous enough that I had to pick a reading" rather than quietly resolved:

- **"Four independent judgments" followed by a list of three.** The fourth was genuinely missing — the
  classification question the variable's own value list does not cover, which the adjudication settled
  from the protocol's source hierarchy and which matched neither coder.
- **A paragraph about product A that recomputed product B.** The translator noticed the arithmetic
  (27/36 → 27/33 = 81.8%) only works for B, and said so rather than making the sentence agree with
  itself. It had run two different rule errors together.

**Disentangling them produced a better finding than the muddle contained.** The same rule failed on both
products, in opposite directions, for opposite reasons: on A it arrived mid-task without its caveat and
made the coder too strict, reversing five properly-disclosed variables to `unknown`; on B it never
arrived at all and the coder read three values out of markup no page displays. Both failures are the
orchestrator's. The paper now says that, and the Turkish slice is being re-translated against it.

The translation pass also caught a **meaning change** in the earlier Turkish draft — "two of the largest
corrections" rendered as "the two largest" — which no figure check would have found, because no figure was
involved. **A careful reader of every sentence catches a class of error that no mechanical check reaches**,
and that is the argument for a translation pass being a review step rather than an afterthought.

## D-078 · 2026-08-17 · FREEZE. And the freeze sweep found the study quoting two different values for its own headline reliability figure

**The dataset is frozen.** `orchestrator/freeze-stamp.md`, generated by `tools/freeze_stamp.py` so that
every count and every SHA-256 is **read from the file it describes rather than typed** — which is the
defect this same sweep caught five times in one day. After this stamp a correction is a published
erratum, not an edit.

### What the pre-freeze figure refresh found

My own checklist item said to re-derive the register's figures from the tools before stamping rather
than trusting the prose. It found four stale numbers and then a fifth that mattered far more:

- §2's adjudicator count, 24 → **29**
- §4's whole attribution table: 550 → **581** unknowns, 128 → **221** decided by hand, and a
  publishing-row column added beside the all-records one, because the publishing rows are what a
  reader's figures come from
- §9 given the three for-cause agreement figures, which existed by then
- §10's heading, 71 → **76** deviations — a number I had myself corrected from 58 hours earlier
- the checklist's own α, **0.807 → 0.811**

### The fifth one, which is a finding rather than housekeeping

`orchestrator/reliability-result.md` said, under the sentence **"The pre-registered figure of 0.807 is
what the abstract carries"**, a figure its own history table three sections higher already recorded as
**0.811** after D-022's out-of-enum corrections. **One document, two values for the study's headline
reliability figure, and the stale one sitting under the sentence that tells the paper what to print.**

**Established before correcting, not assumed**, because 0.811 is the higher number and picking it
unexamined would be picking the flattering one:

1. **The data did not move it.** Nine pass-1 records changed since that file was written, but only one
   — `aiva` — is in the 26-product reliability sample, and **none of its coded values changed**; the
   edit added administrative fields, which α does not read.
2. **The tool did not move it.** `agreement.py`'s only change since was an inert reporting guard
   (D-026), and **the version of the tool as it stood when that file was written returns 0.811 against
   today's records.** Both tool versions, both data states, one answer.
3. So the prose was simply never updated when the history table was. **0.807 is not reproducible from
   anything in this repository.**

Corrected: the sensitivity table (0.807 → 0.811, 0.795 → 0.798), the raw-agreement row (81.9% →
**82.2%**, since 791 of 962 agree), the abstract-carries sentence, and the blindness-exposure argument
at §53, which had been comparing tier C's 0.823 against the stale pooled figure. **The argument survives
the correction** — 0.823 still sits above both — and it is re-based rather than left standing on numbers
that no longer hold.

The `excluding the prose field` column is **left as written and explicitly not re-verified**, because
`agreement.py` does not compute it. Flagged in the document rather than silently carried forward.

### The pattern, stated once because it is the day's real lesson

**Five hand-typed figures went stale in a single day, in four different documents, and every one was
found by re-deriving rather than by reading.** None was wrong when written. Each went stale because data
moved underneath a number that had been derived by a tool and then typed into prose.

The register's own header promises its figures are "computed from the frozen records by a tool". That
promise is now stated honestly: they are **derived** by tools and **typed** by hand, the freeze is what
stops them moving, and **a checker that diffs the prose against the tools is a wave-2 item** — the
single highest-value one on the list, because it is the only defect class here that recurred five times
in one day.

### What is frozen

76 pass-1 records, 26 blind pass-2, 29 adjudicated, 3 for-cause, 5 quarantined and never published.
**2,812 coded values. 337 unknowns on publishing rows, every one attributed** — 283 vendor silence,
48 instrument gap, 4 access failure, 2 unattributable. **516 cited captures, 482 resolving, none
unanswered.** 72 products scored, median **80.25**. **77 deviations logged** — and this sentence said 78 until the stamp, which counts them, disagreed with it. Sixth in a day, inside the entry about the other five.

### What the freeze does NOT cover

**Owner sign-off**, which the checklist requires before anything is published and which is a separate
decision from stopping the data moving.

**One provenance defect, reported and deliberately unfixed** (D-076): a record pairing an access date
with an archive URL stamped five days earlier, across a demonstrated edit. Its coded values survive in
both captures. **No record was edited by this orchestrator on freeze day**, and that invariant was kept
in preference to the correction.

## D-077 · 2026-08-17 · The withdrawn-documents question is ruled, a prior finding reverses on the vendor's own scope disclaimer, and the declared-vs-derived check catches its first contradiction

`openai-sora` adjudicated. Nine values move from `unknown` to determinate; publishing-row
`access_failure` falls from 11 to **4**.

### The withdrawal rule

For a **discontinued-stratum** product, a value determinable from a dated, official, pre-shutdown
archived document is coded determinate on the same terms as any other document. **Withdrawal before the
window does not downgrade it to `unknown`.**

The adjudicator grounded that in the study's existing rules rather than inventing it: `sampling-rules`
§6.2 and protocol §4 provide for discontinued products to be "coded from archived materials" with no
live-at-window-open restriction; this record's pass 1 had already coded values that way without
objection; and the opposite rule would make **every discontinued product `unknown` by construction**,
voiding the stratum.

**The argument it rejected is the one I would have made**: a window-era reader genuinely could not have
read these documents, so crediting them overstates window-era determinability. Its answer is that the
concern is already absorbed — **discontinued products are excluded from every aggregate and from the
index under rule D8** — so a second penalty on top of exclusion is double-counting.

**I verified that exclusion holds before accepting the reasoning**, because the whole argument rests on
it: `openai-sora` carries `apti_total: excluded_discontinued`, alongside two other products. **None of
the nine newly-determinate values touches the APTI median, the IQR, or any published index figure.**
That is what makes the ruling low-risk, and it is stated here rather than left implicit.

Recommendation for wave 2, made rather than acted on: a fourth attribution kind — `withdrawn_pre_window`
— for the case where a value must stay `unknown` **because** the one document that would settle it was
withdrawn and nothing else reaches it. No value on this record is an example, and inventing the category
inside a frozen instrument would be the wrong order.

### A prior finding reverses on the vendor's own words

Sweep 2 had coded `free_plan_exists = no` from the Billing FAQ. That document, and one other both sweeps
leaned on, opens: **"the following experience only applies to Sora 1 on Web. It does not apply to the
Sora app or Sora 2 on web."**

**The vendor's own scope disclaimer excludes exactly the product this record measures** — its
`primary_source_url` redirects to the Sora app. I confirmed the sentence verbatim in two saved captures
rather than taking it on report. Three undisclaimed documents govern instead, and under them
`free_plan_exists` returns to `unknown`: they establish invite gating and credit-purchase eligibility
"for all users" but never state a no-cost ongoing allowance.

**Two sweeps built on a document the vendor had marked as not applying to this product.** The saved
captures are now filename-tagged `INSCOPE` / `OUTOFSCOPE`, which is the cheapest possible guard against a
third repetition.

### The declared-vs-derived check earns its keep

Built this morning (D-070 corrected), it found its **first contradiction**: `headline_price_usd` declared
`vendor_silence`, derived `instrument_gap`.

Ruled a **classifier false positive.** The evidence says "no determinate value stated anywhere" and the
GAP pattern list carries `no determinate` — but the coder means *the vendor* states no value, which is
silence language. The gap sense is our value list having no slot, and this variable has slots for a
figure, for `non_usd` and for `no_public_price`. All ten recovered documents were reachable, read in
full, and contain zero `$` characters. **`vendor_silence` stands.**

**Not fixed by editing the pattern.** "No determinate" is genuine gap language in other sentences, and
tuning a classifier until it stops disagreeing with you is precisely what the overrides file exists to
prevent — its own docstring says so. A hand decision with a written reason is auditable; a pattern edited
to make a disagreement vanish is not.

### The genre problem, third occurrence, and I caused this one

Ten further values needed hand closure because the adjudicator wrote verdict-style evidence
(`unknown_kind=vendor_silence`) rather than the descriptive prose the classifier reads. **I warned this
specific agent about it in its brief — "write the reasoning, not just the label" — and it happened
anyway on ten values.** A warning in a dispatch is not a fix; the classifier needs the adjudicator genre
in its patterns, or the record template needs the field.

Those ten are closed on a **shared basis, and the sharing is disclosed rather than hidden**: the
adjudicator documents reading all ten recovered documents in full, I verified the record's load-bearing
fact independently, three sweeps have read the same document set, and **the product is excluded from the
index so no published figure depends on them.** That last clause is the honest reason a shared basis is
acceptable here and would not be on a scoring row.

### And my own error in the same operation

My first attempt at those overrides parsed the tool's output with `[1:-1]`, which stripped the closing
bracket **and the last character of every variable name** — `trial_exists` became `trial_exist` — so ten
override rows were written that matched nothing. Caught immediately because the review count did not
move, removed, and redone with an anchored regex. **The fourth measurement-shell error I have made
today**, and the fourth caught by checking the result against an expectation rather than by reading the
code.

### Where the corpus now stands

**581 unknowns, 0 needing a human, 140 decided by hand with written reasons.** On the 76 publishing rows:
**337 unknowns — 283 vendor silence (84.0%), 48 instrument gap (14.2%), 4 access failure (1.2%), 2
unattributable (0.6%).**

**Access failure began today at 16 corpus-wide and 14 on publishing rows. It ends at 4.** Not because
anything was reclassified to flatter the study — every one of the reductions came from a document being
retrieved and read, and the reclassifications ran through `instrument_gap` and `vendor_silence` on
stated evidence. The paper reports the path, not just the endpoint.

## D-076 · 2026-08-17 · The final-day change sweep: the frozen frame holds where it could be tested, and a missing decompressor nearly manufactured a price change

Report: `orchestrator/final-day-change-sweep.md`. The last validity check the design owed itself — did a
vendor materially change a coded page **inside** the collection window, which would make two products
coded on different days incomparable.

### The honest denominator, reported before the result

**42 of 76 pricing pages have two or more in-window captures** and can be tested at all. Of the other 34:
22 have exactly one capture, 11 have none, and one is a host the archive refuses outright (D-069).

And 42 overstates it. **40** yielded two readable non-shell bodies; only **28** span 24 hours or more;
**16** span three days; **4** span a week. Twelve of the 42 have every capture inside a single day — one
pair 33 seconds apart, another 13 minutes. **A page tested across 33 seconds has not been tested for
change over a seven-day window**, and the report says so rather than counting it as covered.

Every negative was re-run against four URL variants in CDX **and** independently against the Memento
timemap, and the two indexes agreed in all 34 cases.

### Four vendor edits, none of them stale in our data

**No headline price and no tier name changed inside the window on any testable page.** That is the result
the frozen-frame assumption needed.

- One vendor **added a quantified monthly cap to all three tiers**, bounded to a 26-hour span, monotone
  across ten captures with identical prices and locale markers, so an edit and not a display variant.
  **Our read came after it and the record already codes the new cap.**
- One cut its pricing FAQ from 34 answers to 11. The operative refund answer and the compare-table caps
  survive in both captures, in HTML and in JSON-LD, so no coded value moves.
- Two are cosmetic — a promotional label, a rewritten paragraph adding "Cancel anytime." — with prices
  and tiers identical, and the coded values resting on text present throughout.

Two products differ across captures **by geography rather than time** and are typed `display_variant`
per §6.8 rather than counted as edits. And both of the study's known A/B-testing vendors fall outside the
tested set entirely — one has a single capture, the other none. **For every product here, "unchanged"
covers the arm the crawler was assigned and nothing else.**

### The finding worth keeping: a decompressor that fails into noise

Archive `id_` responses are **zstd and brotli as well as gzip.** A zstd capture decoded as
gzip-or-nothing came back not empty but as **noise — and a price regex mined a `$5` out of it**,
presenting as a total price change 112 seconds after the previous capture. Properly decoded the two
captures are identical.

**A missing decompressor cost this sweep a fabricated finding, not a missing one**, and that inverts what
this study had recorded about compression. The sweep now returns an explicit `undecodable` rather than an
empty string, which is the general rule: a decoder must never fail silently into "empty" or into raw
bytes, because a pattern-matcher downstream cannot tell noise from content and **will find something
plausible in it.** Carried into failure mode 11.

### A provenance defect on a publishing row, reported and deliberately not fixed

One record's pricing source pairs `access_date: 2026-08-12` with an archive URL stamped **20260807** —
five days earlier, and **on the far side of the FAQ edit the sweep had just demonstrated on that same
page.** A matching 2026-08-12 capture exists. Its coded values survive in both captures, so this is a
provenance defect and not a value defect — but a reader following that citation gets HTTP 200 and a
materially different document, with nothing to signal it.

That is worse in one respect than D-073's case, where the cited timestamp had no capture at all and the
redirect itself was the signal. Here everything looks fine.

**Not fixed, deliberately.** No record has been edited by this orchestrator today and that invariant is
worth more than the correction; it goes into the freeze package as an owner decision.

Turned from one sighting into a check: `tools/check_citation_recency.py`. **407 sources carry both an
access date and a timestamped capture; 54 are two or more days adrift, and all 54 cite a capture from
BEFORE the read** — the risky direction, since the page can change in between.

**That 54 is a review list and not a defect count, and the tool's own docstring says so at length.** It
measures the gap, not whether the gap is wrong, and most of the large ones are records citing the newest
capture that exists — one product's documentation cites a 2022 capture because the archive holds nothing
newer, and a discontinued vendor has nothing recent to cite at all. One flagged row is **today's wix
adjudication deliberately bracketing the window** with captures either side of it, argued in its own
record. The tool flags that as drift; it is the opposite of a defect.

**The discriminating question — was a nearer capture available and not cited — needs one archive query
per source and belongs in the collector for wave 2**, so a coder cites the nearest capture at collection
time instead of having it audited afterwards.

Incidental, and already covered by the `local_copy_only` notes in `check_archive_status.py`: one record
marks its pricing sources `local_copy_only` while the archive holds ten in-window captures, two of them
on that record's own access dates. The D-061 pattern, understating our own provenance again.

## D-075 · 2026-08-17 · Retrieval sweep 3 closes all five owed threads, retrieves 12 of 13, and corrects an earlier sweep's own claim

Run once the archive recovered (D-073). Report: `orchestrator/post-window-retrieval-3.md`.

### The five owed threads, all closed

- **The fail/error scan D-051 held a value for** — run on **both** Billing FAQ captures. Zero hits for
  `fail`, `unsuccessful` and `deduct`; the only `error` hits are an account-deletion FAQ. **The condition
  the hold was waiting on is met and the hold is released.** It is also the first independent
  re-verification of sweep 1's recovery, which sweep 2 had named as its own central caveat.
- **The Firefly capture** — read. It does not contain the FAQ: that vendor assembles the page from
  fragments at runtime, so the archive stored a skeleton. The sweep found the published fragment origin,
  which reproduces the eleven answers as a static document — **an independent second route with no
  temporal warrant.** Sweep 2's caveat stands and the route is structurally empty, not re-runnable.
- **The currency arm** — **decisive for one record and by header-level proof rather than inference.** A
  Common Crawl capture carries `cf-ray …-IAD`, Cloudflare's Washington-Dulles edge: **the read was served
  from the US**, the vantage point this study has always lacked. And the document is a pre-hydration
  shell with only `$0` placeholders. So the figure is absent from the served document **from any
  vantage**, not withheld from ours. Reclassified `access_failure` → `instrument_gap`. Two other records
  have no Common Crawl record at all and the arm cannot be run against them.
- **The Hailuo captures** — both in-window captures read in full, 149 and 146 characters of visible text,
  "From /mo", no toggle, no `aria-selected`. **This confirms the study's one genuine access failure** and
  the route is now exhausted.
- **The release-notes thread — and it was not harmless.** The slug was not guessable. The article links a
  full credit rate card with expiry terms. **D-050's claim that the vendor never published a credit
  definition is half wrong**: sweep 1 enumerated a document collection and generalised from one link too
  early. The material was stripped from that article before the window opened.

### The 13 access-failure values: 12 retrieved, 1 stands

**`hailuo-ai / annual_default_toggle` is the only one left**, and it is window-dated, read in full, and
genuinely unreachable. Across three sweeps the corpus's access-failure story is now: **47 of 47 in the
first two, and 12 of 13 here — 59 of 60 such values proved retrievable.** `access_failure` has described
our reading of a document far more often than our reach to one, and the paper should say so with that
denominator.

Three settled today by attribution override, each with the basis re-read rather than taken on the
sweep's word — the currency record above, plus the two whose documents were reached and found to say
nothing. **Publishing-row `access_failure` falls 14 → 11.**

Two stand as `access_failure` after retrieval, and both are honest:

- One record's captures **can never be window-dated** — all twelve are "update your browser" shells, no
  Common Crawl record, no date stamp. Retrieved, addresses the construct, undatable.
- One is **the cleanest instrument miss in the corpus**: a capture dated 2025-09-17, comfortably
  pre-window, already carries "credits (if used) will be returned to your account". The document was
  reachable throughout and our procedure did not reach it. That is what `access_failure` means, and
  calling it anything softer would be flattering ourselves.

### Two questions the sweep refused to answer, correctly

Both referred to adjudication rather than decided by a retrieval agent or by this orchestrator:

1. **Published, then withdrawn before the window.** Six values hang on it. Every recovered document for
   that product was delisted before the window opened. "The vendor published this" and "a reader could
   have obtained it in the window" are different claims and only the first is established — and **the
   three-kind attribution vocabulary has no slot for the difference.**
2. **A free-tier premise is contested, not merely soft.** Three of the vendor's own documents disagree
   about whether the free tier was eligible, and the one that says "for all users" belongs to the product
   era the record codes.

`openai-sora` is now in adjudication on both, with the six held values, and asked to say whether wave 2
needs a fourth attribution kind rather than to invent one.

### The method finding, which belongs in the tooling

**A degraded Memento timemap returns HTTP 200 with a zero-byte body**, and a naive enumerator reads that
as "no captures". It hit five URLs in one batch; on retry the same URLs returned **12, 66 and 66**
mementos. **Had the sweep trusted that batch it would have declared four documents never archived and
been wrong about three of them.** The success code is present, the request completed, and nothing
reports failure — only an empty result measured against a plausible expectation catches it.

This is the **fourth shape** of the defect D-012, D-047 and D-069 already recorded: a service's failure
read as a document's absence. 503 was the first, 403 the second, a local timeout the third, and a
**200 with no body** is the worst of them, because every other shape at least announces itself. Carried
into the failure-modes note with the accompanying rule: **treat a zero-length success as a failure to
answer.**

Also recorded from the same run: on Common Crawl **404 means no record and 502/504 mean no answer**, and
the CDX index was still 503 on a third consecutive day while replay worked but flapped — success arriving
on attempts one through thirteen for the same URLs.

## D-074 · 2026-08-17 · wix adjudicated from its non-English Terms, and the index's treatment of `instrument_gap` turned out to be a promise the instrument never made

**Three things landed together and the third is the one that matters.**

### The wix adjudication

Not a coder disagreement — a post-window retrieval had recovered a document pass 1 could not read, and
the sweep **declined to code the result and referred it here**, which is the right instinct.

The adjudicator established the non-English rule rather than assuming it, and tested the alternative it
was warned about. The vendor's **English** Terms have a rendering defect that hides Sections 2–19; a
Wayback capture from **2026-03-20** shows the identical broken banner, so the defect is five months old
and not window-specific. The Turkish and German locales serve the complete instrument from the vendor's
own first-party infrastructure — verified on response headers, not assumed — both self-dated
**2025-10-30**, and **both state in their own language that the document was authored in English and
translated for convenience, with English governing conflicts.** That is the vendor confirming they are
parallel translations of one instrument, which is exactly what the Termly case elsewhere in this study
disproved for a different vendor, where the endpoint's own metadata showed English was the only locale
ever authored. Same shape, opposite answer, and the difference was established rather than guessed.

Three values change: `unquantified_limit_clause` unknown → `present`, `output_ownership_statement`
unknown → `user_owns`, `auto_renewal_disclosure_location` `help_center_only` → `multiple`. Window
warrant is a Turkish capture dated 2026-08-05 and a German one dated 2026-05-18, bracketing the window.
It also corrected a citation error in the retrieval sweep's own report (§6.2 for the renewal-notice
clause; it is §6.3).

**`output_ownership_statement` was one of the 14 `access_failure` values**, so that count drops to 13
before the retrieval sweep has even reported.

### A fourth source-directory location, flagged rather than worked around

The adjudicator had nowhere canonical to save its captures: no adjudicated record had a sources
directory and `source_paths.py`'s `CANDIDATES` had no entry for one. It saved to the study root — a
location the module already knows, so nothing was lost — and **said so in its report instead of
silently inventing a path.** `records/adjudicated/{slug}-sources` is now in `CANDIDATES`.

Worth stating plainly: **the first five occurrences of this defect were all found by a tool producing a
confident wrong number.** This one was found by an agent reporting a gap it had routed around. That is
the cheaper detector and it is not enforceable.

### The finding: the register promised something the index does not do

`limitations-register.md` §4 has said, since it was written, that **"the index must not score an
`instrument_gap` unknown as non-disclosure."** Checking the scorer against it: **it does not read
`unknown_kind` at all**, and **protocol §8.3 never mentions attribution kinds.** The protocol scores an
`unknown` item as zero, full stop.

**The scorer is right and the register was wrong.** Attribution kinds were assigned *after* collection,
partly by a classifier the orchestrator wrote — and re-weighting a frozen, pre-registered index using
post-hoc attributions is precisely what pre-registration exists to prevent. Implementing the register's
sentence would have let this study adjust its own headline after seeing the data.

What honours the concern is **S2**, pre-registered in §8.4 as "the most favorable reading available to
any vendor": remove `unknown` items from numerator and denominator alike.

| | median | min |
|---|---|---|
| primary | 80.2 | 26.9 |
| **S2** | **88.2** | **67.4** |

**Eight points of median is what this study's stance on `unknown` costs a vendor, now published rather
than asserted.**

### And the case the protocol foresaw, which lands on the worst-affected product

**`google-veo` carries 20 of the corpus's 46 `instrument_gap` unknowns** — one record holding 43% of
them. It scores **26.9: the minimum, the sole occupant of the lowest band, and the setter of the
observed range**, with 13 of 20 items `unknown` and a determinability rate of 0.32.

Its S2 value is **`suppressed`**. Rule S2.2, written before collection, says removing `unknown` items
shrinks `available` and the §8.3.8 guard is re-applied to the shrunken figure; 13 removed items drop it
to 25.0, under the threshold of 50. So **the one product whose score is most distorted by our treatment
of `unknown` is the one product for which the analysis designed to expose that distortion cannot be
computed.**

That is not a protocol defect — the guard exists so a score computed over a quarter of the instrument is
not published as comparable — but it fixes what may be said. **26.9 is not this study finding a vendor
opaque.** The gap to the next product is 23.6 points, and the minimum, the range, and the lowest band's
sole occupancy are all one product meeting an instrument that could not describe it. Register §4 is
corrected, and `analysis-first-findings.md` §3a states the constraint.

### Attribution, after all three

566 unknowns, **0 needing a human**; 346 on publishing rows, **0 unattributed** — 285 vendor silence,
46 instrument gap, 13 access failure, 2 unattributable. 16 declare a kind in their own prose, the
pattern independently derived 13 of them, and **0 contradicted their own declaration.**

**All three of today's hand overrides came from adjudicators**, and the reason is a genre difference
worth recording: an adjudicator's evidence reads as a verdict — "unchanged value,
`unknown_kind=vendor_silence`" — where the classifier's silence patterns were built from coders'
descriptive prose, "no document states", "is silent". The classifier is not wrong; it is reading a genre
it was not built for. A fourth role in wave 2 would need the same widening.

## D-073 · 2026-08-17 · The archive came back, all 92 unanswered citations answered, and provenance goes from 74% to 93%

D-047 left 92 citations recorded as `throttled` — asked three times, refused three times, and reported
as **unverified rather than failed**, on the rule that an unanswered request is not evidence a capture is
absent. That rule was doing real work: it kept the study from publishing a provenance crisis built out of
an outage.

While checking hostinger's captures for D-069 it became clear the service had recovered — `archive.org`,
CDX for four other vendors' domains, and unrelated captures all returned 200 in the same run. So the
tool's own `--redo-throttled` mode was run at a five-second spacing.

**Every one of the 92 answered, and all 92 came back `ok`. None was missing.**

| | before | after |
|---|---|---|
| exact cited capture served | 377 | **469** |
| nearest capture, same day | 13 | 13 |
| cited capture does not exist | 15 | **20** |
| archive withholds the host (403) | 13 | 13 |
| no capture at all (404) | 1 | 1 |
| **service would not answer** | **92** | **0** |
| **resolving** | **390/511 = 76.3%** | **482/516 = 93.4%** |

The denominator moved 511 → 516 because the three closing-day adjudications cite five further captures.
State the figure over 516; the old 511 is not the same population.

**The published 73.8% was never wrong — it was a measurement of an outage, labelled as one.** What the
re-sweep establishes is that the caveat attached to it was correct in the direction it guessed: the note
said 96% of the unanswered sat on hosts the service was serving fine in the same run, so a patient reader
would probably retrieve most of them. A patient reader retrieved **all** of them.

**The 5 new redirects are the cost, and they were traced rather than counted.** A citation the service
answers by serving a *different* timestamp is not reproducible provenance (D-023, and failure mode 14).
Traced through every variable's `source` and `evidence` across all three record folders: **19 of the 20
sit on records that do not publish. One touches a publishing row** — `aiva`, on `headline_price_usd` and
`free_plan_cap_value`, citing a timestamp four days *after* the window with no capture behind it.

**Both values verified against the capture the service actually serves, which is dated inside the
window.** The free-plan allowance is there verbatim — "3 downloads per month Track durations up to 3
minutes" — and `non_usd` is right, because that capture prices in EUR ("Free, Forever €0") with no dollar
figure anywhere in its rendered text. So the defect is the **cited timestamp**, not the value and not its
evidence.

Deliberately not fixed by editing the record: D-010 bars line surgery, and the verification ledger
already carries the truth in a column a reader can follow (`status: redirect`, `served: 20260810075025`).
The register states it in prose as well, because a reader should not have to diff a CSV to learn that one
citation points four days past its capture.

**Closing position on provenance: no publishing-row value in this dataset rests on a capture a reader
cannot open.**

## D-072 · 2026-08-17 · A-023 closes the queue, and pass 1 had priced a page it never saved — while silently dropping a column from the vendor's own table

**A-023 resolved. The adjudication queue is empty**, 24 items opened and 24 closed.

Entry tier confirmed as **Basic** — both passes already agreed on the tier's *name*, so §7.2 never had to
break a tie. The dispute was entirely about its price, and the price moves to the second coding's figures:
**$19.00/mo, $228.00 first charge**, not pass 1's $12.00/$144.00. Five values change on the publishing row.

**Two findings about pass 1 that go well beyond a price disagreement.**

1. **It priced a page it never saved and never archived.** `squarespace-sources/` contains no capture of
   the pricing page, and pass 1's own `archive_results.txt` logs **no save attempt for that URL at all**.
   The archive citation it does carry resolves to a pre-hydration shell with **zero `$` characters
   anywhere** — verified by the adjudicator against that capture and two further window-dated ones, plus
   a live re-fetch.
2. **It read a four-column comparison table as three.** The table is genuinely server-rendered, not
   hydration-gated, and it is the table pass 1 cites as its source for several other variables. It has
   four plan columns; pass 1 describes three, dropping "Plus" from every row it quoted. Its own
   `credit_system_present` evidence quotes the AI-credits row as `10 one-time [Basic] / 20 per month
   [Core] / 120 per month [Advanced]` — the vendor's row reads `10 / 20 / 40 / 120`.

The second one did **not** reach the published dataset: the adjudication rewrote the affected evidence
fields, and `credit_system_present` now rests on a different, cleaner quotation from the vendor's help
documentation. But a coded value being right does not make its evidence right, and **this record shipped
a factually wrong quotation of a vendor table on a publishing row until today.**

**Two rulings match neither coder's evidence**, and one of them matches neither coder's reasoning while
happening to land on pass 1's value:

- `credit_rollover_policy` → `unknown`, `instrument_gap`. The second coding's determinate value is not
  barred on rendering grounds — the help page plainly displays the text — but on antecedent-tracking it
  describes the *other three plans'* recurring pool, not the entry tier's one-time grant. Reading it
  otherwise makes the vendor's FAQ contradict itself within two consecutive sentences. **A one-time
  non-recurring grant is a form none of the three codebook values was built to describe**, all three
  presupposing a recurring allowance. Our gap, not the vendor's silence — the vendor documents the
  arrangement at length.
- `commercial_use_lowest_tier` → `lowest_paid`, on **neither record's evidence**. Pass 1 cited the wrong
  construct entirely (e-commerce features rather than AI-output rights); the second coding correctly
  rejected that but then never connected **its own citation** of the vendor's AI Terms §1.1.2 — an
  unrestricted, untiered grant of ownership in generated output — to the variable it answers.

**The pattern I flagged before dispatching is real, and the mechanism is worse than I guessed.** I had
warned this adjudicator that `commercial_use_lowest_tier` disagreed on two of the three for-cause
products with the identical shape (pass 1 determinate, re-coding `unknown`), and that on the other
product the cause was a terms clause the re-coding never engaged. Here the re-coding **did** read the
governing clause, quoted it, and failed to apply it to the variable. So across the three for-cause
codings the failure is not "did not find the rights clause" — it is **not connecting rights language to
the rights variable**, which is a codebook-navigation weakness rather than a retrieval one. Worth a
wave-2 instrument note: the variable's definition should name the document class that governs it.

**Directional bias: none.** The adjudicator reports errors in both directions for both coders — pass 1
over-credited on `trial_auto_converts` and under-credited on `mandatory_addon_present`; the second coding
over-credited on `credit_rollover_policy` and under-credited on `commercial_use_lowest_tier`. Each tracks
a construct-specific misreading rather than a lean.

**Method notes disclosed by the adjudicator rather than left implicit:** the annual-billing toggle state
*is* establishable — `aria-checked="true"` is server-rendered and identical across three window captures
— but **the price figures exist in no rendered form in any capture, live fetch or archive**; that is the
page's architecture, not one capture's failure. It therefore leaned on the vendor's own `ld+json`, which
A-020's caveat admits, and only because the independently-rendered comparison table corroborates the same
four-plan structure — cross-document confirmation rather than a single payload taken on trust. **Common
Crawl held no capture of the URL**, checked and reported rather than dropped. And one WebSearch was run
*after* the figures had been derived three times from vendor documents, purely as a plausibility check,
determining no coded value, disclosed in `coder_note`.

## D-071 · 2026-08-17 · A-022 ruled against pass 1 in the direction that flatters us — and I had scoped both remaining queue items from a report instead of a diff

**A-022 resolved.** `credit_system_present` moves **yes → no** and its four dependents to
`not_applicable`. The for-cause coding is upheld and pass 1 reversed. Six values change on the
publishing row; the corpus now carries 26 adjudicated rows and 50 primary.

The codebook's domain-5 **rule 1** decides it: a plan allowance stated directly in output units is not a
credit system, and the entry tier's own rendered card states "Up to 300,000 words per month" with a
published $0.00046/word overage. The single occurrence of the word "credit" anywhere relevant is an
unquantified "Shared team credits" bullet on the sales-gated Enterprise tier, which is out of scope for
an entry-tier variable and carries no balance, rate or purchase mechanism anywhere, including in the
bundle.

**The check I asked for was actually made, and it mattered.** I warned this adjudicator that the
for-cause coding of *this* product has a recorded error of its own (D-065): its coder read a feature
table out of a JS chunk and coded three variables from unrendered markup. So its metering argument had
to be tested for the same defect before being accepted. The adjudicator established that the word-count
figures **are rendered**, three independent ways: the saved capture is literally `document.body.innerText`
after full load; the pre-hydration HTML carries only `$0` placeholders where those figures belong, so
hydration supplies them rather than nothing displaying them; and a fresh live fetch reproduces the same
split. Different failure mode, same product — and the D-065 defect **does** still taint three other
variables, which it confirmed separately.

**Pass 1 left the evidence for its own correction in place.** Its `coder_note` called the `yes` "a closer
call toward no", and its own answers to `cost_per_output_computable` and `usage_cap_quantified` rely on
the identical word-count figures as solid fact. A record whose neighbouring values only cohere with the
opposite reading is the adjudicators' brief's own signal, and it fired here.

**Direction, stated because it runs our way.** Coding `no` removes one `unknown` and three
determinate-but-empty values, so it slightly shrinks this study's unknown burden — the flattering
direction. The brief said so explicitly and told the adjudicator to rule on the codebook regardless. It
did, and the reasoning stands on rule 1 rather than on the count.

### The orchestrator defect: a queue item scoped from a report under-scopes

**I built both remaining queue items from what each for-cause coder reported as notable, instead of
mechanically diffing the two records.** Measured after the fact:

| product | real disagreements | I briefed | outside the brief |
|---|---|---|---|
| gptzero (A-022) | **9** | 5 | **4** |
| squarespace (A-023) | **6** | 3 | **3** |

A coder's report is a summary written to be read, and a summary omits what the writer thought
uncontroversial. The diff omits nothing. **Scope an adjudication from the diff and use the report for
the argument, never the reverse.**

Corrected for A-023 mid-task: the three extra variables were sent to the running adjudicator so it could
rule on them in scope, with a warning on each about where the determinate value comes from.

For A-022 it was too late, and the adjudicator handled it better than the brief deserved: it diffed all
37 itself, found the four, resolved them, and **labelled each resolution `OUT-OF-SCOPE FINDING, NOT
ADJUDICATED UNDER A-022`** rather than passing them off as adjudicated — then recommended they get their
own pass. Reporting against its own interest again, which remains the mechanism that catches most of
what gets caught here.

Reviewed, and no further pass is being run on those four, for stated reasons:

- **Three are the D-065 trio** (`free_plan_cap_documented`, `free_plan_cap_value`,
  `usage_cap_quantified`). Pass 1's values stand, and this is now the **second independent
  confirmation** — D-065 was my finding, and an adjudicator that re-read the rendered capture reached it
  without being told the conclusion.
- **One is new: `commercial_use_lowest_tier`.** Pass 1 `not_granted`, for-cause `unknown`. Not defaulted
  to pass 1 — the adjudicator re-fetched pass 1's cited ToS capture today, confirmed it genuine (HTTP
  200, matching `memento-datetime`, no redirect reason) and found §8 "PROHIBITED ACTIVITIES" containing
  the governing clause verbatim. The second coding never engaged a clause sitting in a document it
  should have read, so `unknown` is wrong on the document rather than on a judgment.

**A pattern across the for-cause codings worth flagging before freeze:** `commercial_use_lowest_tier` is
a disagreement on **two of the three** for-cause products, and in both the shape is identical — pass 1
determinate, the re-coding `unknown`. On gptzero the established cause was a ToS clause the re-coding
did not engage. The running A-023 adjudicator has been told to read the terms itself on that variable
rather than choose between records. If the same cause holds there, it is a systematic weakness in how
these three re-codings handled rights language, not three coincidences.

## D-070 · 2026-08-17 · The unknown-attribution classifier could not read the canonical spelling of its own three categories

Found while closing out the faceless-so adjudication, whose record left five `unknown` values with no
attribution kind and so took the dataset's unattributed count from 0 to 5.

The adjudicator had in fact declared every one of them — as `unknown_kind=vendor_silence`, written
inside its evidence prose, which is the designed route: attribution lives in a sidecar and
`attribute_unknowns.py` reads evidence rather than mutating records. But its category pattern was

    \b(?:instrument[- ]gap|access[- ]failure|vendor[- ]silence)\b

**A space or a hyphen, never an underscore.** So `vendor_silence`, `instrument_gap` and
`access_failure` — the canonical spelling, the one used in the codebook, in every record's enum, and in
this tool's own output column — matched nothing. A classifier whose whole job is reading evidence for a
declared category could not read that category written the way the study writes it.

**Bounded, and in the safe direction.** Only 9 unknowns anywhere in the corpus declare a kind
explicitly; coders overwhelmingly write reasoning rather than category names, which is why the blindness
cost so little. Of the 9, **8 were assigned the declared kind anyway** by prose inference, and the
ninth was left `NEEDS_HAND_REVIEW` rather than guessed at. Nothing was mis-assigned; one row was
under-assigned.

Widened to `[-_ ]`, and then measured before being believed, which is D-042's lesson: **zero rows
moved.** The negation guard is untouched and still applies — widening what counts as a category *name*
does not widen what counts as an assertion of one.

The ninth row stayed `NEEDS_HAND_REVIEW` after the fix, correctly: **the classifier never auto-assigns
`vendor_silence`**, because that is the category which flatters this study's headline finding. So it was
closed the designed way, as override 207 of 554, with the basis re-read from the vendor's documents
rather than taken from the adjudicator's declaration — the developer docs state when credits are charged
and separately that a generation can fail, and never state whether a failed generation's credits are
kept or returned.

**Result: 554 unknowns, 0 needing a human. 348 on the 76 publishing rows, 0 unattributed** — 286 vendor
silence (82.2%), 47 instrument gap (13.5%), 13 access failure (3.7%), 2 unattributable (0.6%).

### D-070 corrected · 2026-08-17 · this entry overstated what the defect was, and the fix is narrower than it claims

Found hours later, when a second adjudicated record declared `unknown_kind=instrument_gap` in its
evidence and the classifier **still** reported "no signal matched" — after the widening above was
supposed to have made exactly that readable.

Reading the classifier properly: **`CATEGORY_NAMES` never assigns a category.** It appears in one place,
inside the signal matcher, as half of the negation guard — it suppresses a keyword hit when a category
name appears next to a negator. Assignment is done by `classify()` from three separate keyword lists
over the coder's *reasoning*, and it **deliberately ignores any `unknown_kind=` label a coder writes.**

So two claims above are wrong and are corrected here rather than edited away:

- "A classifier whose whole job is reading evidence for a declared category could not read that category
  written the way the study writes it" — **it never read declarations for assignment at all**, by
  design, and still does not.
- The widening's real scope is the **negation guard**: a coder writing "not vendor_silence" with an
  underscore would not have been suppressed and now is. **Zero rows moved because no coder wrote that** —
  which means the fix was inert on this corpus, not that it was safely absorbed. Both readings are
  consistent with the measurement; only one is true, and I published the wrong one.

**The design being ignored here is right, and stays.** A label is cheap and reasoning is checkable;
a classifier that took a coder's `unknown_kind=` at face value would be recording an assertion rather
than testing one. But it means **an explicit declaration is silently unused, so a coder declaring one
kind while their own prose supports another would surface nowhere.** Nothing compared the two.

That check now exists, and it is pointed at the **pattern's** verdict rather than the final one — the
first version compared against the post-override kind, so a hand override that matched a declaration
made the row agree with itself and inflated the pass rate from 12 to 14. Corrected before use.

**14 of 564 unknowns state a kind in their own prose. The pattern independently derived the declared
kind on 12. Two declared a kind the reasoning did not signal and were left for a human — both closed
today by hand with a written basis read from the vendor's documents rather than from the label. Zero
contradicted their own declaration.**

That last figure is the one worth keeping: **no coder in this study ever labelled an unknown as one kind
while writing reasoning that supports another.**

### D-067 amended · 2026-08-17 · the faceless-so adjudication landed, and it upheld NEITHER coding on two variables

Ruled on all 13 disputed variables: **8 to the for-cause coding, 3 to pass 1, and 2 to neither.** Ten
substantive values change in the published dataset, plus one free-text field; the corpus now carries 25
adjudicated rows and 51 primary.

**It found a better basis than either coder or this orchestrator had.** On the free-plan question I had
reasoned from the developer docs that a subscription-less team receives no credit allowance, which is
true but indirect. The adjudicator read the vendor's own front-end configuration and found the
free-plan object **suppressed by an explicit `hideFreePlan=true` flag** — never rendered under any
state. So pass 1 had coded a free plan from a data object the vendor deliberately hides. That is a
cleaner application of A-019 than either the "no ongoing allowance" argument or the "it is in the
bundle" one.

**And it verified the FAQ mechanism properly.** My own check had loaded the live page, which the vendor
had re-implemented since the window — decisive about the mechanism but a generation removed from the
evidence. The adjudicator read the component's render logic in the window-era bundle, confirmed the
answer is inserted on click, and upheld pass 1's refund and cancellation values on that basis. Better
evidence for the same conclusion.

**Two rulings match neither coding**, which is what an adjudication is for:

- `auto_renewal_disclosure_location` → **`absent`**, not pass 1's `pricing_page` and not for-cause's
  `unknown`. All four location classes were read and none states a renewal position, which is the
  variable's own definition of `absent` — a determinate finding, where `unknown` would have claimed
  documents were unreachable.
- `refund_policy_location` → **`help_center`**, on protocol §6.2 folding billing and help articles into
  that authority class. Pass 1's `pricing_page` would have contradicted how the same record uses that
  value elsewhere, where it means the literal `/pricing` URL, on which no refund text appears.

**The direction of error was not uniform, and the paper should say so.** Pass 1 over-credited disclosure
on 9 variables; the for-cause coding under-credited it on 4. A single-direction story — "the later
reading was stricter" or "the first reading was sloppier" — would be false in both directions.

Provenance improved as a side effect: the adjudicator verified every cited capture itself and corrected
three JS-chunk citations that resolved to a real but different timestamp, plus one incorrect
`archive_failed` flag on the vendor's privacy page.

**One honest open item, flagged by the adjudicator rather than smoothed over.** `refund_policy_location`
has four values, and the protocol's own source hierarchy names a class of official vendor page that none
of the four covers — the statement here sits on the home page. `help_center` is the closest defensible
fit and is coded as such, with the instrument gap recorded in the variable's evidence and in the
`coder_note` instead of being presented as clean. **A codebook fix for wave 2, not a late patch to a
frozen instrument.**

## D-069 · 2026-08-17 · 13 of 14 "missing" captures are WITHHELD, not absent — and one vendor's whole domain is refused by the archive

Found by running every offline checker in `tools/` end to end, on the reasoning that if one validator
had been vacuous (D-068) others might be. Seven were fine. `check_archive_status.py` reported **one
failure**, and the failure was real in the sense that something was wrong — but not the thing it said.

`hostinger` claims `archive_status: archived` and cites 12 captures, **none of which resolves**. Twelve
sequential save-request timestamps on 2026-08-07 between 11:50:45 and 11:58:48, the signature of a
coder working through a batch.

**The verifier had recorded the reason and then thrown it away.** Its classifier read:

    if code == "404":                              return "missing"
    if code in ("429","503","502","504",""):       return "throttled"
    return "missing", served, f"HTTP {code}"       # <- 403 lands here

So a **403 fell through into `missing`**, a verdict whose own documented meaning is "404 — archive.org
answered, and there is no capture." And the `detail` column had been carrying `HTTP 403` beside every
one of those rows since the first sweep. The evidence was in the tool's own output, unread, for three
sweeps.

| verdict | before | after |
|---|---|---|
| archive withholds the host (403) | — | **13** |
| no capture at all (404) | 14 | **1** |

**The study's genuine archival absence is one citation out of 511.** Re-labelled from the recorded
status codes — nothing was re-requested, and the CSV rows say so — so this correction does not depend
on the service being reachable today.

**This is the third time this study has conflated a service's refusal with a document's absence.**
D-012 and D-047 were 503 (110 rows). This is 403 (13 rows), in the same function, one branch down. A
fourth was sitting beside it and is fixed in the same commit: a local `subprocess` timeout also returned
`missing`, so a request that never reached archive.org at all was recorded as evidence about a capture.
The verifier now carries `excluded` for 401/403 and **`unclassified` for anything else, because the
lesson of three repetitions is that the default bucket must not be one that asserts something.**

**The vendor finding, which is worth more than the correction.** Controlled, in one run, same user
agent, same delay:

| CDX query | result |
|---|---|
| `hostinger.com` · `www.hostinger.com` · a specific path | **403 on all three forms** |
| `squarespace.com` · `wix.com` · `canva.com` · `gptzero.me` | 200 |
| `example.com` | 503 (rate limit — a different fact) |
| `archive.org` front page, an unrelated capture | 200 |

So the archive is up, it serves other vendors in the frame, and it refuses this one. **And the vendor's
own `robots.txt` does not ask archivers to stay out** — its only `Disallow` rules are query-parameter
patterns, and it sets `Content-Signal: search=yes, ai-input=yes, ai-train=yes`, which is permissive. So
the exclusion is not robots-derived; it is an exclusion held at the archive.

**A vendor whose pricing documents the public archive will not serve is a vendor whose past pricing
claims no third party can check.** For a study about pricing transparency that is a substantive finding,
and it was sitting inside our data labelled as our own provenance failure. It is now reported as what it
is: `check_archive_status.py` returns **0 failing, 13 noted**, and hostinger's note says the archive
will not serve this vendor to anyone and that 8 local mirror files stand in.

Deliberately NOT done: hostinger's `archive_status` field was not rewritten. `archived` may well have
been true when the coder wrote it — the captures were requested and may exist — and what changed is
readability, not existence. Editing the record would assert a fact we do not have, over a field the
dataset already publishes three computed columns beside. D-010's prohibition on line surgery holds.

Open for wave 2, recorded here so it is not lost: **the index does not score archivability.** It
measures what a vendor discloses, not whether anyone may keep a copy — and a disclosure nobody can
re-examine later is weaker than one they can. Adding it would need a codebook variable, a pre-registered
decision rule, and a frame-wide 403 sweep, so it belongs in a next wave rather than as a late addition
to this one.

## D-068 · 2026-08-17 · The structural validator examined ZERO records and exited 0, and had been doing so in every agent's hands

Found while checking whether the three `records/for-cause/` records were covered by any standing
check. They are — but the check that matters most was not covering anything at all.

`tools/validate_records.py` has two code paths. The functions carry the real logic and glob
absolute, `HERE`-relative paths correctly. The `__main__` block does not call them. It has its own
loop, and its default glob was a **repo-root-relative literal**:

    "Data/seo/research/pricing-transparency/records/pass1/*.yaml"

Every agent brief in this study says to run `python3 tools/validate_records.py` **from the study
directory**. From there that path does not exist, the glob returns an empty list, the loop body never
executes, and the tool prints nothing and exits 0.

**A validator that examines zero records and reports success is worse than one nobody runs**, because
its silence is indistinguishable from a pass. Three for-cause coders and an unknown number of earlier
agents reported "validated OK" on the strength of that silence.

Two functions were also unreachable as a script and had never run except when called by hand:
`check_evidence_prose()` — the hard requirement that every coded value on a publishing row carry
reasoning, not just a URL — and `report_toplevel_usage()`.

**What the corpus actually looks like, now that the check runs:** 129 records across `pass1`,
`adjudicated`, `for-cause` and `pass2`, **0 failing**, 0 out-of-enum, 7 records relying on the
`TOPLEVEL_OK` exemption as expected, and the evidence-prose requirement met on every publishing row.

So **no record was wrong. Nobody had established that.** This is the reassuring direction of the
defect described in the failure-modes note, and it is the more dangerous one: a vacuous check aimed
at a clean corpus leaves no trace anywhere. Had a record been broken, the same silence would have
shipped it.

Fixed: the default is absolute and spans every folder holding live records (`pass2-contaminated` is
deliberately excluded — those five are withdrawn, and publishing them would be the error); a run that
matches nothing now **fails with exit 2 and names what it searched**; both orphaned functions are
called. `check_evidence_prose` also carried an unused `paths` parameter that a caller would
reasonably read as scoping the check — removed, because a signature that lies about coverage is the
same defect one level up.

Corrected mid-task to the adjudicator then running on faceless-so, whose brief had told it to run the
vacuous command.

Not a widening of scope: `check_value_enums.py` was already globbing `records/*/` and had been
covering all 134 records correctly the whole time, which is why the enum figure quoted elsewhere in
this log stands. Two tools, two coverage stories, and the survey I did first — grepping each tool for
path literals instead of asking the tool what it globbed — got this one backwards before running it
got it right. The note's own instruction is *ask what a tool globbed*; I asked grep.

## D-067 · 2026-08-17 · The for-cause set closes at three of three, and the last one inverts what the number means

D-001 promised faceless-so a for-cause blind second coding on 2026-08-06, reported **separately** from
the pre-registered 26 so the planned statistic stayed uncontaminated. Carried out today, eleven days
late, closing the set opened by D-065 and D-066.

| | raw | α |
|---|---|---|
| faceless-so (D-001) | 23/36 = **63.9%** | **0.603** |
| gptzero (D-004) | 27/36 = 75.0% | 0.728 |
| squarespace (D-011) | 30/36 = 83.3% | 0.823 |
| **all three pooled** | **80/108 = 74.1%** | **0.720** |
| the 26 pre-registered products | 82.2% | 0.811 |

**Reported separately, as promised, and the pooled figure is 8.1 points below the corpus.** Publishing
that comparison without its decomposition would be the error, in both directions: it invites a reader
to conclude that records collected after a blindness breach are worse, and it also hides that one of
the three disagreements is a real correction to a publishing row.

**faceless-so's 13 disagreements are 3 independent judgments.**

- **7 values ride on one upstream question** — does a free signup that grants no credits constitute a
  documented free plan? `free_plan_exists` plus four dependents, plus `commercial_use_lowest_tier` and
  `watermark_removal_tier`, which both change meaning depending on whether a free tier exists to be
  the lowest one. One judgment, seven cells.
- **2 values are an independent dispute**, and here pass 1 looks wrong: it coded
  `auto_renewal_default = on` and `auto_renewal_disclosure_location = pricing_page` while its own
  evidence field records that the terms of service are "completely silent: zero occurrences of
  'renew', 'subscription', 'billing', or 'cancel'". What the pricing page discloses is *cancellation*
  — "you can cancel your subscription at any time" — and reading a renewal default out of a
  cancellation permission is an inference, not a disclosure. That credits the vendor with a
  transparency disclosure it did not make, on a variable the index scores.
- **4 values are my defect, not a coder's.** See below.

**The mid-task rule delivery, in the opposite direction from D-065.** D-065 recorded that gptzero's
re-coder was never told A-019, and coded three variables out of an unrendered JS feature table — too
permissive. I sent A-019 to both running agents to prevent a repeat. faceless-so's coder received it
mid-task, was reasoning toward determinate refund and cancellation values, and reversed all five to
`unknown` on the strength of it. **That was too strict, and the rule as written says so:** A-020's
caveat is explicit that *an embedded payload the page RENDERS still counts*, and that *an FAQ built
from JSON is disclosure if the FAQ appears*.

The vendor's home page renders a working FAQ accordion. Its four buttons carry exactly the four
questions held in the bundle's `FAQAccordion` array of `{question, answer}` pairs. A reader who
clicked "What is the refund policy?" saw the answer. What the coder was actually looking at was a
**capture** in which `aria-expanded="false"` and the answers were absent from the served document
entirely — not in markup, not in any script payload. That is a fact about the capture.

Established by live inspection today, and it settles the mechanism rather than the content: a static
fetch of the same page **now** returns those answers in ordinary non-script markup, and on the live
page the text sits in `innerText` while the control still reads `aria-expanded="false"`. **The vendor
re-implemented the component after the window closed.** So the window-dated capture and today's page
disagree for a reason that has nothing to do with the refund policy changing.

Three faces of one orchestrator defect, all mine:

1. A rule pushed to a running agent as a message arrives **abridged**, and the abridgement becomes the
   rule. The full statement was in the coder's required reading; the pushed prohibition outweighed the
   caveat it was written alongside.
2. Two agents received the same push and applied it differently, which is what a rule delivered
   outside the document is for.
3. **A-019 and A-020 were absent from `deviations-for-adjudicators.md` entirely** — the rule that
   decides this class of case was missing from the brief of the only role whose job is deciding cases.
   Added today, with both directions stated and the specific finding an adjudicator needs: *does the
   page display that text to a reader?*

**faceless-so is now in adjudication**, on all 13, with both source sets and the mechanism finding
handed over as evidence rather than as a verdict. It was not in the pre-registered 26 and had no
adjudicated record; it will have one, and `build_dataset.py` prefers adjudicated over pass 1, so the
outcome reaches the published dataset. Whatever the adjudicator rules, this entry stands: the raw
63.9% is measuring one codebook question, one pass-1 over-read, and one orchestrator briefing defect
— not coder noise.

**A fourth reading of the access-failure story.** The five `access_failure` attributions this coding
produced were the refund and cancellation family. They were never retrieval failures: the evidence was
in hand and the rule was misapplied to it. Two earlier retrieval sweeps found 46 of 47 `access_failure`
values retrievable; these five were not even that — they were retrievable and already retrieved.
`access_failure` continues to describe our reading of a document far more often than our reach to one.

**The capture-set traps this coding found, all real and all reusable** — carried into the
failure-modes note:

- The home page's FAQ is a **JS-driven accordion whose answers are absent from the collapsed DOM**.
  The pricing page's FAQ on the same site is a **native `<details>` element that keeps its answer text
  in the DOM regardless of open state**. Same vendor, same page furniture, two completely different
  evidentiary situations, and nothing on screen distinguishes them.
- A saved auxiliary file, `faq_home_raw_segment.txt`, holds those answers in unquoted-key
  object-literal form. It is a fragment of the bundle, not a render — and it **made evidence the
  capture never displayed look present**.
- `chunks/584c5016af948b8b.js` carries several sets of **stale or historical pricing-config objects**
  for differently-named plans at unrelated price points. A figure taken from the first regex match
  there can be years out of date.

Attestations: the coder confirmed it opened neither pass 1's record, nor any sibling for-cause record,
nor `orchestrator/`, nor the public site, and read no git history. It independently verified 10
window-dated captures through the public CDX index. `/billing` is categorically unreachable — 307 to
login, CDX empty, no public snapshot on any date — which is a genuine `unknown` under §6.3 and coded
as one.

## D-066 · 2026-08-17 · Second for-cause coding: agreement ABOVE the corpus, and it found a capture-set gap nobody had noticed

D-011's promised for-cause blind second coding, also never performed until today.

**37 of 37 settled, 4 `unknown` all vendor silence, zero access failures, zero instrument gaps.**

| | raw | α |
|---|---|---|
| **this for-cause pair** | **30/36 = 83.3%** | **0.823** |
| the 26 pre-registered products | 82.2% | 0.811 |

**Above the corpus figure.** Two for-cause codings are now done and neither shows the blindness breach
degrading its record: one matched the corpus once its own rule error was removed, this one exceeds it
without correction.

### It closed a gap in the evidence base by its own initiative

**Pass 1's saved captures do not include the pricing page** — the document the whole A-domain rests on —
even though every captured page links to it in navigation and a captured help article refers to "the
amount listed on the pricing page." Without it the re-coder would have sent most of Domains 1–4 to
`unknown`. Instead it queried the capture index, found four window-dated snapshots, and read the one
closest to the other captures' timestamps.

The archived page stored a **client-side loading placeholder** with no price in visible text, so it took
the figures from the page's own `ld+json`, parsed with a real JSON parser rather than text-scraped. Under
A-020 that is legitimate: the vendor plainly displays these prices and the payload supplied our reach, not
the fact. It is the opposite situation from D-065's error, where a feature table and FAQ were never
rendered to anyone.

### The disagreement that matters is an entry-tier disagreement

Pass 1: **$12.00/mo, $144.00 first charge, mandatory add-on present.** Re-coding: **$19.00/mo, $228.00, no
add-on**, selecting Basic after comparing four plans on annual-equivalent cost. Both cannot be the entry
tier, and the add-on disagreement is probably the same question — a cheaper headline that requires a paid
add-on is not cheaper.

Opened as **A-023**. It is harder than a normal tier dispute because the pricing page is absent from the
capture set and the archived version renders nothing, so **which plan was DEFAULT is a display-state
question structured data cannot answer.**

### Two more things the re-coding recorded rather than smoothed

The vendor's own `ld+json` gives three plans about **54 region-specific offers each and the fourth only
two** — an internal inconsistency in its own structured data, logged as a `display_variant` rather than
resolved silently.

And a document-hierarchy tension: the terms frame refunds as fully discretionary while a dedicated help
page states a concrete 14-day annual policy with no discretion language. Recorded in `conflict_note` and
coded from the specific policy.

### The briefing fix landed where it belongs

`deviations-for-coders.md` now carries A-019 **and** A-020's caveat — that an embedded payload the page
renders still counts, and so does one carrying a figure the vendor displays but a capture could not render.
Both for-cause coders were also messaged mid-task. D-065's error came from that rule living only in an
adjudication ruling; it now lives in the file every coder is bound by.

## D-065 · 2026-08-17 · The first for-cause second coding lands, and the breach did not degrade the record — but the re-coding made an error of its own, from a rule I left out of its brief

D-004 promised a for-cause blind second coding of the product whose pass-1 coder disclosed a blindness
breach, reported **separately** from the pre-registered 26 so the planned statistic stays clean. Promised
2026-08-07, never done, found on 2026-08-17, now done.

**It settled 37 of 37 from window-dated captures alone** — 23 determinate, 7 `unknown` all attributed to
vendor silence, 7 `not_applicable`. Nothing required treating a variable as inaccessible.

### The result, with the confound named

| | raw | α |
|---|---|---|
| as recorded | 27/36 = 75.0% | 0.728 |
| **excluding the re-coder's own rule error** | **27/33 = 81.8%** | **0.800** |
| the 26 pre-registered products, for context | 82.2% | 0.811 |

**So the breach did not detectably degrade the record.** Once the re-coding's own error is removed,
agreement sits at the corpus figure. That is the answer the exercise existed to produce, and it is
reported with both numbers rather than only the flattering one.

### Nine raw disagreements are three real ones

- **3 are the re-coder's error.** It coded the free-plan cap and the usage cap from an **embedded JS
  feature table and an unrendered FAQ payload**. A-019 bars exactly that: a figure present only in
  unrendered markup is not disclosure. Pass 1 was right. I confirmed the sources are unrendered — a
  browser read of that pricing page shows neither an FAQ nor a comparison table.
- **5 cascade from one judgment** about whether the product has a credit system at all. The re-coder's
  argument is strong and specific, and it is now **A-022** for adjudication.
- **1 is an ordinary judgment difference** on commercial-use rights.

### The re-coder's error is my briefing defect

**I briefed it on the three kinds of `unknown` and never mentioned A-019** — the rule this vendor's
evidence turns on, decided by me the same day. The coder applied the codebook faithfully and read a
payload the codebook does not exclude, because the exclusion lives in an adjudication ruling it was not
given.

The two for-cause codings still running have been sent the rule mid-task, with the caveat that an
embedded payload the page RENDERS still counts — the test is whether a reader sees the result, not how
the datum is stored. The message to one of them also sharpens it for that vendor specifically: its
structured data advertises a tier the pricing page no longer shows, and under A-019 that tier is markup,
not a disclosed plan.

**This is D-049's shape again**: an instruction that must bind reaches only what is briefed after it
exists. The durable fix is the same — `deviations-for-coders.md` should carry A-019, not just the
dispatch.

### And a finding the re-coding produced on its own

The vendor's own embedded feature table names an **"Essential" tier at 150,000 words/month that was never
rendered as a purchasable plan card** in the captured state, and the page's JS references a live
experiment with a **`no-essential-no-quarterly`** variant plus code filtering that tier out. So the entry
tier this study selected may have been chosen against one arm of a live pricing experiment. Under A-019
the unrendered tier is not a disclosed plan and the coded values stand — **but this is the sharpest
concrete instance of A-017's limitation**, that the study can demonstrate an experiment and cannot
classify what it does. It goes to the limitations register beside A-017.

## D-064 · 2026-08-17 · Owner framing adopted, and the statistic renamed rather than the framing bent

The study's dossier, owner-approved on 2026-08-03, standing instruction: *"internal agent tooling is
described only at the /ai-transparency level — AI-assisted under named human editorial control."* The
methods section written earlier today described the coding step in detail and conflicted with it.

**Owner decision, 2026-08-17: use the AI-assisted framing.** Reason given: the owner reviews and
approves before anything is published, so the description is accurate.

**Adopted, and the framing is accurate for what it describes.** It is also more substantive than a
formula: the editor fixed the question and design before data existed, approved the instrument, ratified
the frame, signs off the freeze — and **two of the largest corrections in this study came from editorial
intervention rather than from any automated step**: the challenge that a figure sat on a vendor's own
page (D-056, D-057) and the challenge to filing gaps as limitations before chasing them, which turned 21
claimed access failures into one (D-050). Both are in the section by name.

### The one thing that could not be published under it, and what was done instead

Editorial control governs **what is published**; it does not change **what a statistic measures**.
Approving a value after the fact does not make the two readings behind an agreement figure human, and
does not decorrelate their errors. So a reader meeting **α = 0.811** under an "AI-assisted" heading
would read it as agreement between two people who used AI help — a different quantity, because human
coders' errors are largely uncorrelated and two automated readings of one input can fail identically,
agree, and raise the statistic without raising accuracy.

**The fix was to rename the statistic, not to bend the framing.** It is now reported as **instrument
consistency under independent double reading** rather than as inter-coder reliability. That is the
narrower and true claim: an instrument two independent readings apply differently is broken whoever
applies it, and consistency is worth measuring on its own terms. **No human-coder claim is made
anywhere, so the owner's framing misleads nobody**, and the number keeps its meaning.

Propagated to the limitations register and the published data dictionary in the same pass, so the three
documents cannot disagree about what the figure is.

### Why this is recorded rather than settled quietly

Because the alternative was available and would have been easy: publish α under the conventional label,
inside a section that says AI-assisted, and let a reader supply the wrong assumption. **Nothing would
have looked wrong.** Using the conventional name for a number that does not meet its convention is the
cheapest kind of false impression to create and the hardest to be caught at, and this study has spent
two weeks refusing cheaper versions of exactly that.

## D-063 · 2026-08-17 · RETRACTION. D-060's headline finding was my own path bug, and the export tool found it.

**D-060 reported that one publishing row had no re-examinable evidence at all** — that its
`archive_status` claimed a local copy, that it named seven local files, and that **none of the seven
existed.** It called this "the single worst provenance case in the study."

**All seven files exist.** They are in `originality-ai-sources/` **at the study root**, not under
`records/pass1/`. My check globbed one path.

### The layout, which nobody had surveyed

    records/pass1/<slug>-sources/     59 products
    records/pass2/<slug>-sources/     26 products
    <slug>-sources/                   14 products, at the study root

**Four tools globbed the first path alone** and were wrong about the thirteen products that keep
theirs at the root: the provenance trace (D-037), the `archive_status` consistency check (D-061), the
dataset build's `local_source_files` column, and the quotation check.

### Every affected figure, corrected

| | as reported | true |
|---|---|---|
| publishing rows with **no re-examinable evidence** | 1 | **0** |
| records keeping no local mirror | 18 | **4** |
| `archive_status` consistency failures | 3 | **1** |

The remaining single failure is real and is the one D-061 named: a record claiming `archived` whose
twelve cited captures do not resolve, while it does hold local files — a status that **overstates**.
The four with no local mirror are genuine: three have no source directory anywhere and one has an
empty directory.

Fixed properly rather than patched four times: `tools/source_paths.py` is now the one place that
knows where a product's captures live, and the four tools delegate to it.

### This is the fifth time, and the pattern is now exact

D-020: a field stored in three shapes, read in one. D-033: a provenance check reading one field,
nearly publishing a false crisis. D-037: a citation trace keyed on one failure mode, blind to records
citing nothing. D-061: a status field trusted rather than verified. **And this: a directory that lives
in three places, globbed in one.**

Every one produced a confidently wrong number. **Three ran alarming and two ran reassuring, and this
one was alarming** — it accused the study's own record-keeping of a failure that had not happened,
which is its own kind of harm: an unearned confession is as false as an unearned defence, and it
would have gone into a published limitations register.

### What caught it, which is the part worth keeping

**Not one of the four checks.** The public-export tool refused to copy files it had no rule for and
printed them — and the printed paths had no `records/pass1/` prefix. A tool built to fail loudly on
anything unclassified found what four tools globbing a single path had missed, on a day when I had
already written the finding up twice.

`methods-tooling-failure-modes.md` §14 says to read every storage shape and names four occurrences.
It is now five, and the note says so.

## D-062 · 2026-08-17 · A checklist item resolved as a KEEP, because removing the exemption would cost more than the drift it hides

The pre-freeze checklist wanted `validate_records.py`'s `TOPLEVEL_OK` exemption **removed** once the
dataset build proved it canonicalises across storage shapes, so a future wave could not drift the same
way without failing. The build does now prove exactly that (D-058, zero unrecognised shapes).

**The exemption stays, and the reasoning is the point.**

**Seven records rely on it** — I checked before deciding, and my earlier survey had said two, because
that count was over publishing rows where the build resolves adjudicated files. Removing the exemption
would fail seven records that are **correctly coded** and merely store one field in a different place.

The alternative is moving the field inside those seven, and that is line surgery on records for a
cosmetic reason. **D-010 exists because a script doing exactly that broke eight records, and this
orchestrator has broken three more doing it in the last two days** (D-053, D-054, and one during the
A-010 batch). A stored-shape difference the build already erases is not worth risking a record over.

So the item is closed as a keep, with the exemption **counted instead of silent**:
`report_toplevel_usage()` names every record relying on it, the comment above it explains why it
survives, and **wave 2 fixes it where it belongs — in the record template, before any data exists.**

That is the same move this study has made a dozen times now: where a rule and the records disagree and
the records are right, the answer is to make the exemption visible rather than to force the records or
to hide the rule.

### Two smaller closures in the same pass

**One record's prose was overstating an absence** (D-056). Its evidence said no USD figure is published
anywhere for its entry tier; the vendor's own page payload carries one, as unrendered educator-program
copy. The sentence now says the absence is of **rendered** content, names the figure, and states why
A-019 leaves the coded value unchanged. **The value was never wrong; the sentence was.**

**The dataset release requirement is verified as meetable, not assumed.** All **798** source files across
the corpus are tracked in git, 82 MB. For 159 coded values the local capture is the only surviving
evidence (D-037), so a release of the CSVs alone would look complete and be unverifiable — and it is
better to learn now that the files are there than at release.

## D-061 · 2026-08-17 · `archive_status` is wrong on 14 of 76 records, and almost always in the direction that undersells us

Built `tools/check_archive_status.py` after D-060 found two records disagreeing with their own status.
It compares the field against what the record actually holds: `archived` requires a cited capture that
**resolves**, `local_copy_only` requires a **local file**.

| coded `archive_status` | verified | rows |
|---|---|---|
| archived | archived | 56 |
| **local_copy_only** | **archived** | **12** |
| local_copy_only | local_copy_only | 6 |
| **archived** | **local_copy_only** | **1** |
| **local_copy_only** | **no re-examinable evidence** | **1** |

**14 of 76 disagree, and 12 of the 14 understate the study's own provenance.** Exactly one record
overstates it, and one has no evidence at all (D-060).

### I tested the obvious excuse and it does not hold

The charitable reading is that the field was true when written and went stale — a save that failed
during collection succeeding later. **Checked on eight of the twelve: five have a capture dated the
COLLECTION DAY that resolves today.** So the coder recorded "archive attempt failed" while a capture
from that very day existed. The observation was wrong when it was written, not merely out of date.

The mechanism is almost certainly that Wayback's save endpoint returned an error or timed out **while
the save completed anyway**, and the coder recorded what the request appeared to return. So the field
means *"what my save request seemed to say"* rather than *"whether a capture exists"* — and its name
does not say so.

### The fix preserves the observation instead of overwriting it

The coded field stays exactly as the coder wrote it. The dataset gains three **computed** columns —
`archive_status_verified`, `resolving_captures`, `local_source_files` — so a reader gets what is true
without the record losing what was observed. Same principle as the unknown-attribution sidecar: a
build canonicalises and computes, it never rewrites a coded value.

### Why this one is worth the space

**It runs in the study's favour, and that is the reason to be careful with it.** Twelve records have
better archival coverage than the dataset claimed, so the honest correction improves our numbers. A
study that chases corrections against itself and takes the favourable ones on trust has only moved its
bias. So this one was verified per-record against the capture index rather than asserted, the one
record that overstates is named alongside the twelve that understate, and the raw coded field is still
in the CSV for anyone who wants to check the computation.

## D-060 · 2026-08-17 · ~~One publishing row has no re-examinable evidence at all~~ **RETRACTED — see D-063**

> **RETRACTED 2026-08-17, hours after it was written.** The record's seven named source files all
> exist, at the study root rather than under `records/pass1/`. My check globbed one of three
> possible locations. The corpus-wide claim below — one publishing row with no re-examinable
> evidence — is **false**; the true figure is zero. The entry is kept in full because the reasoning
> it contains about *why D-037's check could not have found such a record* is still correct and
> transferable, and because deleting a retracted finding is how a log stops being evidence.

Compiling the limitations register turned up the worst provenance case in the study, and it was invisible
to the check that was supposed to catch exactly this.

**`originality-ai` cites no archive captures and has no local source files.** Its `archive_status` and
all eight of its `sources` entries read `local_copy_only`, and each entry's note names a specific local
file — `pricing-page.txt`, `terms-and-conditions.txt`, and five more. **None of the seven named files
exists.** The `-sources/` directory was never created; only the record YAML is in the repository. And
because the status is `local_copy_only`, the record cites **zero** archive URLs, so there is nothing to
resolve either.

**All 37 of that record's coded values rest on evidence a reader cannot open.** It is a publishing row.

### Why D-037 missed it, which is the transferable part

D-037 traced the 28 citations that **fail to resolve** back to the values resting on them, and found 178
values across 10 rows with 159 recoverable from local mirrors and 19 with neither. **This record cites
nothing, so it was never in that population.** A check keyed on broken citations cannot see a record with
no citations — the failure mode is absence, and absence does not appear in a list of failures.

Asking the question the other way round settles it corpus-wide: **for each publishing row, does ANY
re-examinable evidence exist — a capture that resolves, or a local file?**

| | rows |
|---|---|
| resolving archive **and** local files | 51 |
| resolving archive only | 17 |
| local files only | 7 |
| **neither** | **1** |

So the scope is one complete record, not a scattering. That is worth stating precisely in both
directions: it is the single worst case in the study, and it is one row of 76.

### The mirror-image case, found in the same pass

**`shortsfaceless` is marked `local_copy_only` while carrying three archive captures that all verify
`ok`.** Its provenance is better than its own status claims. Recorded because the pair is instructive:
one record's status asserts more than the record can support, the other asserts less, and **nothing in
the toolset was comparing a status field against the evidence it describes.** Both were found by hand
while writing a limitations section.

### What follows

- Both go in the limitations register, §5a and §5b, by name and with the counts.
- A mechanical check belongs in the toolset: **`archive_status` must be consistent with what the record
  actually holds** — `archived` requires a resolving capture, `local_copy_only` requires a local file.
  Added to the checklist.
- The `originality-ai` values are **not** withdrawn. They were coded from documents the coder read, its
  evidence fields quote them, and the vendor's pages remain live. What is gone is the ability to
  re-examine what was read at the time. **That is a provenance failure, not a data-fabrication finding**,
  and conflating the two would be its own error.

## D-059 · 2026-08-17 · A-021's answer was already in the pre-registered protocol, and my build was wrong three times looking for a problem that was not there

**A-021: `cost_per_output_computable` is currency-neutral, and this is not a construct decision made
today.** `protocol-v1.md` §8.3.10 and §9 limitation 12 — **both written before any of the six disputed
records were collected** — apply the USD-centric deduction to index items A1 and A3 only and never to
C3. The instrument always permitted a cost computed in the vendor's own currency. The adjudicator found
the answer in the pre-registration rather than reasoning to a preference, which is the strongest ground
a ruling in this study can have.

**Zero of the ten values I flagged were contradictions.** Six were never even candidates:
`cost_per_output_unit` names WHAT a product sells — video-minutes, words, seats — and carries no price
and no currency, so a non-USD headline cannot contradict it. **My build conflated a unit label with a
price claim.** The other four rest on complete published calculations in EUR, TRY, TRY, and a
currency-invariant zero, and stand as coded.

**One value changes, and the adjudicator found it outside my list by applying the ruling consistently:**
`picsart/cost_per_output_computable` `unknown` → `yes`, on a published ₺83.25 per seat-month. Its coder
gated the variable on the headline's CURRENCY, which the variable never asks about — and two other
records with the identical fact pattern were read correctly by their own coders the same day, which is
what makes it a slip rather than an ambiguity.

**Direction: toward determinacy, away from `unknown`** — the direction the queue item itself flagged as
convenient for us, and the correction pushes further that way. It survives because **the decisive
protocol text predates every affected record**, and the adjudicator named the counterweight rather than
leaving it: the dollar-comparable `cost_per_output_value_usd` stays `not_computable` for the three
non-zero foreign-currency records, so those score full credit on the disclosure item while their
reported figure is not dollar-comparable. Generous on the scored dimension, limited on the reported one,
and both halves published.

### Three heuristics, three failures, and the right conclusion

My build tried three times to flag this as a defect:

1. **Blank any derived figure where a money value is `unknown` or `non_usd`.** Fired on ten; five had a
   perfectly good USD headline and an `unknown` FIRST CHARGE for unrelated reasons. Removed (D-058).
2. **Flag where the headline is not a USD number.** Could not distinguish a published euro price from no
   price at all — equally non-numeric.
3. **Key it on the attribution sidecar.** Still misfired, because `vendor_silence` on
   `headline_price_usd` correctly means *no USD price published* and says nothing about whether a price
   exists in another currency.

**The right conclusion was that there was nothing to flag.** A-021 read all six records and found zero
contradictions. A fourth heuristic would have been a fourth wrong answer to a question the
pre-registration had already settled.

So the build now reports the **fact** instead of asserting a defect: five rows compute a per-output cost
on a non-USD basis, listed because a reader is entitled to know a full-credit disclosure score can sit
beside a figure that is not dollar-comparable. **A tool that cannot find a real defect should report what
it can see, not keep refining until something looks wrong.**

## D-058 · 2026-08-17 · The dataset build runs clean, and it found ten contradictions by refusing to fix one

`tools/build_dataset.py` emits the publishable dataset: **76 publishing rows x 37 variables = 2,812
coded values**, plus a long-form file carrying each value's source, the coder's evidence and its
unknown-attribution kind, plus a build report stating every count a reader would otherwise take on
trust.

**It runs clean on the four hard requirements**, each of which exists because something cost the study
something: parses rather than text-matches (D-010); reads every storage shape and found three, reporting
**zero unrecognised** (D-020/D-033/D-037); never coerces `yes`/`no` through YAML's boolean rules (D-006);
and joins the attribution sidecar, confirming **351 unknowns on publishing rows with zero unattributed**.

### The part worth recording is a rule I wrote, tested, and removed

The first version applied D-053's reasoning as a build rule: blank any derived per-output figure to
`not_computable` wherever a money value was `unknown` or `non_usd`, since a USD figure cannot come from a
non-USD one. It fired on ten values. **I checked which ten before trusting it, and half were wrong.**

Five of the records it caught have a perfectly good USD headline price and an `unknown` **first charge**
for reasons with nothing to do with currency — a pay-per-event product with no determinate first
transaction, an unstated billing cadence, a discontinued product. Blanking their derived figures would
have been a fabrication produced by my own build.

**And the deeper problem is that the rule existed at all.** A build that rewrites a coded value is the
orchestrator making a coding decision at build time, which this study forbids everywhere else.
Canonicalising a storage shape is not the same act as changing a value. The build now **reports and
changes nothing.**

### What reporting instead of fixing turned up

Ten contradictions across six records, none previously noticed: each carries a determinate per-output
value while its own headline price is not a USD number. **They are not all errors, which is why a build
rule would have been the wrong instrument.** Where the headline is `non_usd`, the cost per output is
genuinely computable and simply denominated in the vendor's currency. Where it is `not_applicable`
because the product is free, a per-output cost of zero is computable too. Only where no price is
obtainable at all is the pair truly incoherent.

So the question is what `cost_per_output_computable` means — computable **in USD**, or computable **at
all** — which the codebook never says. Opened as **A-021**, to be answered consistently with A-013, whose
parallel reading would keep ten determinate values rather than convert them to `unknown`. **That
direction shrinks this study's headline, so it must not be adopted for being convenient.**

## D-057 · 2026-08-17 · Archive retried across three services. One of them answered a question we had been treating as unanswerable.

The owner asked me to try the archive again. I tried three, and the round was not empty.

**archive.org is in a full outage, not throttling us.** Homepage 503, CDX 503, availability API 502,
replay 503, Memento aggregator no connection at all. That distinction matters for D-047: the 92
unserved citations were logged while 377 others served fine in the same run, so that reading — a
request-side limit rather than missing captures — still holds for that window. Today's failure is a
different and larger event.

**Common Crawl is up, and it is the vantage point this study lacks.** Its crawler runs on US
infrastructure, so a Common Crawl capture is a US-served read — exactly what D-007's unexecutable
"US reader" test was reaching for and what our own geography cannot produce. Nobody had tried it.

It holds a **June 2026 capture of the record the owner named.** Fetched it properly: index lookup,
WARC byte-range request (HTTP 206, 316,708 bytes), decompressed to 476,589 characters.

**The capture contains none of the plan-card content.** Zero occurrences of `PREMIUM`, `MOST POPULAR`,
`billed annually`, `words per month` or `Choose Plan`. The single `TRY` hit was base64 noise, not a
currency. It is a pre-hydration shell: Common Crawl does not execute the page's scripts either.

### What that establishes, and it is stronger than the assumption it replaces

**For that record the `unknown` is not a geography problem at all.** The price is absent from the
vendor's served HTML **from a US vantage point too**. It exists only in a runtime-rendered state that
no static fetcher and no archive crawler can capture, from anywhere. So D-056's framing — that this
value turns on our lacking a US position — is **too generous to our own instrument and is corrected
here**: a US-served archive read was available all along, it was fetched, and it does not contain the
price.

This extends A-017. That item established that an archive cannot document a client-side A/B variant
because it does not execute the experiment script. The same mechanism applies to client-side price
rendering generally, and it produces a **class of vendor whose price is unarchivable in principle** —
determinable only by a rendered read, never by any capture. That belongs in the limitations as a
finding about the method's reach, not as a gap in this study's diligence.

**The practical consequence: the fix for that record is a rendered read from a US position, not an
archive capture.** The checklist item said archive-or-owner; for this record it is owner-only, because
the archive route is now known to be structurally empty rather than merely blocked.

### The other three records are where they were

Common Crawl holds **no capture** of the other three pricing pages — only the vendors' homepages.
`archive.today` is up and holds two of them, but both are far outside the window (ten months and
twenty-two months before it), too old to bear on a window-dated value, and it rate-limited us (429)
after two lookups. So for those three the owed archive thread is still owed, and archive.org's outage
is the blocker.

**Method note worth keeping:** the Common Crawl index and byte-range fetch worked first time and cost
one request each. It should be a standard route in the collector, not something discovered on the last
day — a US-infrastructure crawler is a free second vantage point for any study whose readers sit in
one country.

## D-056 · 2026-08-17 · The owner said a price was on the vendor's own page. I went and looked. Six routes, and the answer is narrower than either of us said.

The owner objected that the study cannot file a gap as its own limitation when the figure is on the
vendor's own pages, and named a specific record: they had looked, and I had said it was not there.

**I did not defend the classification. I opened the page.**

### What I found, in order, including the part where I was wrong

**A real USD figure for that record's entry tier exists in the vendor's own page payload.** The
pricing page ships, in its data payload, the string *"GPTZero premium for life (valued at
$288/year)"* — and Premium is the record's coded entry tier. So the record's phrase "no USD figure is
published anywhere for it on the live page" is **looser than the evidence supports** and its prose
should be tightened.

**But it is not rendered.** Checked on the pricing page and on the educators page: the string appears
in neither as visible text. It is copy for an educator-program section that neither page displays.

**Then I made a mistake and caught it.** A fetch-and-parse pass reported that the FAQ page "renders
$21 and $26". It does not. Parsing a detached document made script content read as text. With scripts
stripped, the rendered FAQ contains **zero dollar figures and zero local-currency figures**. I had
briefly written a finding that was an artifact of my own method — the fifth time in three days that a
striking result turned out to be the instrument.

**Six routes, all exhausted from here:**

| route | result |
|---|---|
| pricing page, rendered | **TRY only** — 549 / 1,049 / 2,098, no USD anywhere visible |
| currency or locale control in the DOM | **none exists** |
| price API endpoints (five probed) | **all 404** |
| currency codes anywhere in the payload | **zero** — no `USD`, no `TRY` key |
| payment-processor catalogue (the route that produced A-020's recode) | **absent** — this vendor ships none |
| US-crawled archive capture | **archive.org 503** — homepage, CDX and the Memento aggregator all down |

### The ruling, and it does not change the value

`unknown` stands and `instrument_gap` is the correct attribution. Under **A-019**, a figure present only
in unrendered markup is not disclosure — and applying that rule against my own interest here is the
same discipline the A-020 adjudicator showed when it reached A-019 first and then found a *different*
clause decided its record. There is no equivalent second clause here: A-013 rescued A-020 because that
vendor **displays** a price and only its denomination lived in the payload. This vendor displays a price
too, but nothing anywhere gives its USD denomination.

### Where the owner is right, and it is the part that matters

**The study has no US vantage point, and four records turn on exactly that.** Currency is IP-bound,
there is no locale path or header that overrides it, and every coder and agent in this study reads from
one country. That is not a property of the vendors and it should never have been written as though it
were. It is a **fixable instrument gap**, and the fix is a US-served read:

- a US-crawled archive capture — **owed, and blocked today by an archive.org outage with a date on it**,
  not by anything about the vendor;
- or a dated reading from a reader position the instrument does not have.

**The owner can supply the second one.** If a USD figure is visible from their position, that is
evidence this instrument structurally cannot produce, and it would settle four records rather than one.
That is not work being handed back — it is the single vantage point the study lacks, and saying so is
more honest than recording four `unknown`s and calling them ours.

**On the checklist as its own item**: the four affected records, the owed archive thread, and a wave-2
requirement that the protocol name an executable route for a US-denominated read instead of a test with
no route.

## D-055 · 2026-08-17 · The adjudication queue is closed. 20 items, and the largest correction runs against our own headline.

`orchestrator/A-009-A-011-A-016-A-017-resolution.md` closes the last four as one family, because they are
one question: **when a vendor publishes something the instrument cannot express, what does wave 1 do?**

**Zero coded values change.** What changes is what the dataset records and what the paper may say.

The treatment, in four parts: the value stays `unknown` and the attribution is `instrument_gap`; the
vendor's actual figure is carried in the record's own prose, so **nothing is lost, it is only uncounted**;
the index must not score an `instrument_gap` unknown as non-disclosure, since a vendor that published a
quarterly price and got `unknown` because our list lacks the word "quarterly" disclosed fully and scoring
it as opaque measures us; and the APTI guard must use the **corrected** dependency count of six, not the
nineteen A-016 states, which would credit one vendor with dependent-unknown relief its record does not
support.

**A-017 needed one thing the others did not.** The other three are gaps in a value list; that one is a gap
in an evidentiary rule, and it produces a sentence the paper has to carry: this study can demonstrate that
a vendor's price was under live experiment — both arms sit in the page's own markup — and simultaneously
cannot classify the resulting disagreement as display variance under its own protocol, because §7.4.2
admits only archive evidence and **no archive can record a client-side variant.** The bar was correctly
held: the adjudicator that met it fetched both passes' archives through the raw endpoint, took a fresh
third capture, found all three identical, and resolved the disagreement as an ordinary one rather than
lowering the bar for a tidier statistic.

### The queue is closed: 20 items

Every one produced either a correction, a confirmation with its reasoning replaced, or a finding. **Nine
coded values changed across the whole queue** — three under A-010, four under A-015, two under A-020 — plus
one under A-018. Of those ten, **six ran toward the vendors and four against them**, which is roughly what
a set of rulings decided on rules rather than on preference should look like.

### The number I would put in front of a reviewer

**67 of 550 unknowns — 12.2% — are this instrument's inability to express something a vendor published.**
That is larger than the 2.9% attributable to documents we could not reach, and it is the **largest single
correction this study makes against its own headline**. The instrument, not vendor opacity, is the
second-biggest source of unknowns in this dataset. Wave 1's contribution is to have measured that rather
than to have fixed it.

## D-054 · 2026-08-17 · The confirm cluster resolved; two rulings kept a value and replaced its reasoning; and my commits have been scoped to a directory, which is not scoping

`orchestrator/A-004-A-006-A-015-resolution.md`. **Four coded values change, all on one record.**

**A-004 — CONFIRMED**, and the reviewer separated the coder's two grounds: the first carries the ruling,
the second is not load-bearing and is weaker than the coder thought, because the enum it appealed to never
offered the value it reasoned from. Confirming a value while retiring half its justification is the useful
kind of confirmation.

**A-006 — CONFIRMED**, verified live: the old domain 301s to the new one, the title reads "formerly", and
the footer still names the original legal entity. **The dataset prints the frozen-frame name**, because §6
copies `product_name` from the frame and printing the new name beside the old `product_id` would
desynchronise the row from the frame it was drawn from. Discoverability is satisfied *inside* the dataset
without a new column — §11 bars adding one — because a search for the new name hits the row through the
source URLs and a `coder_note` sentence, and §10 publishes `coder_note` as a column. The paper prints the
frame name with a footnote carrying the new name, the redirect and the entity.

**A-015(a) — CORRECTED.** The Free tier is a 14-day trial, not a perpetual free plan. Decided on window-era
pricing-page text **plus the record's own self-contradiction**: it already reads the identical phrase, four
lines below on the same card, as a 14-day limit in order to code the trial variables. Four values recoded;
the trial variables hold unchanged. **The reviewer took the less vendor-favourable of the two available ways
to give the reading effect** and said so.

It also **corrects a passing aside in the A-012 resolution**: zero cost is that rule's paradigm case, not a
condition of it. A resolution written yesterday, corrected today by the next reader of it.

**A-015(b) — value CONFIRMED, basis REPLACED.** The queue's question is answered **no**: the clause the
coder relied on is scoped to API users on a separate surface with separate credentials, and no document
attributes that access to the entry tier, so **the coder's stated ground fails.** The value survives on a
clause the coder never cited — an all-users provision about content excessive in size or burdensome to the
vendor's systems — window-dated by the terms' own last-updated line. Right value, wrong reason, and the
reviewer found the right one instead of accepting the value on the wrong one. **Confirming it denied the
vendor three index points.**

### Two evidence problems it surfaced

**A coder queried a page instead of reading it.** The help article the record cites contains the sentence
the record says does not exist — "you can start with a free 14-day trial… after the trial you can choose
from these plans". The coder had put targeted prompts to that page rather than reading it through. The
reviewer could not date the page into the window, so **the ruling deliberately does not rest on it**; it
rests on the pricing page and the record's own contradiction.

**One record had no archive at all** — every source `local_copy_only` after D-012 — so none of its
quotations had ever been verified against anything. The reviewer checked them against live reads and found
them verbatim. That is luck, not method, and it is the same exposure D-037 measured on other records.

Also flagged for the batch: the rebranded record's change register uses an **out-of-table event type**,
which would fail to supply the `vendor_edit` entry a §7.4 `date_explained` classification requires.

### And a defect in my own git practice, found because an agent reported being swept up

The reviewer disclosed that my D-053 commit absorbed its resolution document mid-write. **Checked: true.**
That commit carries 622 lines of its work under a message about something else. Two of my twenty-nine
commits today did this.

**The cause is exact and it is mine.** I have been writing `git commit -- <study>/orchestrator/` — a
**directory** path. A directory takes everything beneath it, including a file another agent wrote there
seconds earlier. The rule I put into the agent definitions reads *"scope the commit, not only the add"*, and
**scoping to a directory is not scoping.** Nothing was lost and content parity was verified, but the git
record now attributes an agent's document to a commit about a different subject, and for a study that
publishes its own process that is a real if modest cost. From here: name files.

### Two YAML mistakes applying this batch, both caught before commit

The first inserted a note containing a double quote into a flow-mapping field and produced invalid YAML
(D-053). The second wrote a bare `no`, which **YAML parses as boolean False** — deviation D-006, the exact
reason `normalize_booleans.py` exists. Both were caught by running the validator, the enum check and a
type assertion *before* committing, and both were restored from git and redone. **Three record-surgery
failures in two days says the method is wrong, not that I was unlucky**: these edits should be made by a
YAML-aware writer, and that goes to wave 2's tooling list.

## D-053 · 2026-08-17 · The entry-tier family resolved, a cascade figure I had been repeating is wrong, and I broke a record doing it

`orchestrator/A-001-A-010-A-014-resolution.md`. **Zero entry-tier selections change. Three coded values
change, all on one record.**

- **A-001** — the item's premise did not survive its own record. §7.2's price basis is **currency-agnostic**
  ("lowest annual-equivalent cost… in the pricing page's default display state"), and §6.5 governs how a
  money *variable* is coded rather than the comparison that picks a plan. The re-collection reads the two
  candidates in local currency and post-window sweep 2 independently confirms the same ordering on a
  different locale path — so **the selection is reproducible even where the denomination is not.** One
  variable class defeated by D-007's unexecutable US-reader test, ten intact.
- **A-010** — the entry tier is forced: §7.2 carries no exclusivity requirement and §7.3 needs no paid
  tier at all AND a vendor statement saying so. Three values recoded; the coder's vocabulary-based split
  is **sound evidence applied to the wrong variable** — it belongs to the numerator of one variable, not
  to the tier-scoping of another.
- **A-014** — the pricing-page anchor holds. Three independent checks all favour it, and the sharpest is
  that **selecting the cheaper off-page plan would make the study score that vendor's price LESS
  determinable**, since the price variable is definitionally a pricing-page figure. It would also convert
  a determinate billing basis into an A-011 unknown.

**Net direction: favours the vendors, against our headline.** All three rulings decline an available route
to more unknowns — one alone would have taken five further cascade values to `unknown`.

### A number I had been repeating is wrong, and it runs against the vendors

I have said several times, including to the owner, that an entry-tier decision cascades to "roughly twenty"
variables. **Codebook §5.2 enumerates six**, ten counting the price group. The platform-embedded product's
22 unknowns therefore include **six** cascade values, not nineteen — the other sixteen share a *different*
antecedent, which vendor surface the product is sold on. **A-016 states the inflated figure and the APTI
guard must not inherit it**, or that vendor will be credited with far more dependent-unknown relief than
its record supports. Correcting it makes that vendor look *more* opaque, not less.

### A derived-variable defect with no rule, found by enumerating the cascade properly

Four records would feed a **non-USD figure into a USD-denominated derived variable**, and §6.5's `non_usd`
exclusion misses all four because their money values are coded `unknown` rather than `non_usd`. The
recommendation is a computation instruction rather than a codebook change: `not_computable` wherever the
arithmetic would be non-USD. This is for the analysis build, and it must not be discovered there.

### The shopper-versus-seller divergence is a finding class with three arms

A-014 asked whether one vendor's off-page cheaper plan was a quirk. It is not. Three arms: one priced
off-page; one naming **a fourth billing period in its ToS with no price published anywhere reachable
without an account** — the worse failure, presenting as the milder one; and one where the vendor
affirmatively withdrew the plans, checked deliberately so the class is not built from silence alone. Plus
two adjacent mechanisms, a slider default and a stale structured-data tier. **Report it whether or not any
value changes.**

### And I broke a record applying this, which is D-010 exactly

My first edit inserted a note containing a double quote into a flow-mapping evidence field and **produced
invalid YAML** — the validator failed immediately, the file was restored from git, and the edit was redone
with no quote characters and a parse check between each change. D-010 is the deviation that says records
are never rewritten by line surgery; I did it anyway, one record, caught in seconds because the check runs
before the commit rather than after. **The lesson is not that I made the mistake but where the guard sat**:
had I committed first and validated later, a broken record would be on origin.

## D-052 · 2026-08-17 · A-020 recoded on a distinction I had not drawn; A-002 is a rule defect with a second instance

**A-020: two coded values recoded.** `phrasly` `headline_price_usd` `unknown` → **10.99**,
`first_charge_amount_usd` `unknown` → **131.88**. First money recodes since the window closed.

**The reasoning matters more than the values, because it corrects my own ruling by refining it.** The
queue's stated question was whether a payment processor's price object shipped inside a page is a
published document. The adjudicator answered that question **A-019's way: it is an internal layer, not a
document.** It explicitly refused the escape available to it — that this payload is *live* where the one
that set the A-019 precedent was *inert* — on the ground that the rule tests where data is **present**,
not whether something consumes it, because making consumption the test would let any vendor earn credit
for a fact its renderer hides. That is a better statement of the rule than the one I wrote.

**And then it found that the question does not decide the record.** A-019 bars a figure present *only* in
the payload. This price **is displayed to every reader** — a local-currency figure here, a USD figure in
the US. What the payload supplies is not the price but its **denomination**, which is the exact thing
A-013 made vendor-centric. So recoding restates a fact the record already carried, in the vendor's own
unit of account. My two rulings did not conflict; I had failed to notice that they operate on different
objects — one on the figure, one on the currency it is expressed in.

**Three findings made it determinate rather than a judgment call:**
- **Every** `countryCodes` key in the catalogue was enumerated: six countries, and **no US key and no
  local key.** The retrieval's one blocking caveat — "a base price plus three USD overrides" — dissolves,
  because those three are other countries entirely. A US reader falls through to the base **by
  construction**, so exactly one USD figure is reachable rather than several.
- The price objects carry **vendor timestamps**, created and last-modified both **pre-window**, which
  replaces a 0.4% FX corroboration with vendor-stamped temporal warrant.
- The record's own conclusion that no readable price "has ever been archived" generalises from a
  34,722-byte capture, where the served document is **260,122 bytes** and carries the catalogue inline.
  That thread is alive, not structurally dead.

**Direction, stated plainly: toward the vendor and against this study's headline.** Two unknowns removed
and APTI component A from 0.35 to 1.00. Not uniformly favourable, though — it makes the gap between the
advertised monthly figure and the actual first charge **computable at 12.0× for the first time**. And an
incidental observation the adjudicator recorded without coding: the card's struck-through reference price
corresponds to **no price object in the vendor's catalogue at all** and exceeds the highest price it
actually charges for that tier by 25%. No wave-1 variable captures reference-price integrity. It should.

**I checked the routing item rather than assuming it.** The adjudicator flagged that another vendor also
recovered from a "country-keyed price table" and said it asserted nothing about that record. Checked: the
retrieval enumerated that table in full — 348 price rows across ten products — and found **no US/USD row
for the entry tier while carrying one for the tier above.** Same test, opposite answer, because the facts
differ: one vendor's US reader falls through to a base price, the other's has no row to fall through to.
**No recode there**, and the difference is worth stating because it shows the test discriminates rather
than sweeping.

**A-002: no change to the value, and the rule is the defect.** The principal-output coding is right on
that vendor's own framing, and the published row already carries the value the queue was worried about.
But the diagnosis has a **second instance on the A-020 vendor** — same shape, a principal output that
consumes no credits, so there is no rate to withhold. Two instances in what one reviewer could read makes
it a finding class rather than one vendor's quirk, and it goes to wave 2.

### A git risk found in the same report and worth its own line

The adjudicator disclosed that the worktree was **already on a detached HEAD** before it committed, so its
commit sat on no branch. Checked immediately: HEAD was one commit ahead of `origin/main` with no
divergence, that commit was the resolution, and it is now pushed. **No work was lost.** But a detached
HEAD with several agents committing into it is a state where a single reset would take work with it, and
it is only safe because every agent's commit gets pushed promptly. Left as-is while the conveyor runs, for
the D-026 reason — the fix is not urgent and breaking a worktree three agents are committing into is.

## D-051 · 2026-08-17 · Second sweep: 25 of 25 retrievable. Across both sweeps, 46 attempted and ONE genuine access failure.

The D-048 audit moved 25 values into `access_failure` after the first retrieval sweep had already
finished, so the study was asserting a limitation on 25 values nobody had tried. Found by counting the
inventory from the file rather than from memory when the owner asked what was still missing.

**Second sweep result: 10 retrieved and addressing the construct, 15 retrieved and the construct absent,
ZERO still unreachable.**

**Across both sweeps: 46 values attempted, and exactly one is a genuine permanent access failure** — a
plan interface behind an authenticated session the protocol forbids opening. The study began this week
claiming twenty-one.

### Three more under-retrieval mechanisms, and one is embarrassing

1. **Collapsed accordion answers live in `textContent` and are empty in `innerText`.** That is how an
   entire eleven-answer FAQ was recorded as unreadable. **The same record had already solved this exact
   problem on a different page of the same vendor**, via archived raw HTML — so the technique was in the
   record and was not reapplied.
2. **A trailing slash moves a Memento timemap from 0 captures to 66.** `…/pricing` returns nothing;
   `…/pricing/` returns sixty-six mementos.
3. **Geo-bound currency is an instrument gap, not an access failure.** Two vendors plainly publish
   prices; what fails is D-007's "US reader" test, and **the protocol provides no executable route to
   satisfy it** — currency is IP-bound and no locale path, URL parameter or request header overrides it.
   Three values reclassified to `instrument_gap` accordingly, which is consistent with the A-013 ruling's
   test of obtainability from a standard reading position.

### One value deliberately NOT reclassified

The sweep flagged `openai-sora/failed_generation_charge_policy` as **the one value its evidence does not
reach** — the first sweep never scanned the recovered document for `fail` or `error`, so "absent" would
rest on inference. It said to hold the value in `access_failure` if the scan is wanted first. **Held.**
Sweeping in a reclassification an agent marked conditional would defeat the point of asking it to mark
conditions.

### Caveats the sweep recorded against itself, which is why its numbers are usable

**archive.org's replay path returned 503 for the entire run — roughly a hundred attempts, CDX down a
second day.** So the fourteen values on the discontinued product are **inherited from sweep 1, not
independently re-verified**, and the sweep says so rather than presenting them as fresh. What it could
check matched exactly: both slugs 404 live, and the timemap returns precisely 31 mementos.

It also recorded that the recovered document self-scopes to one surface of that product, which bites
hardest on five specific values; that one vendor's recovered clause is Turkish and German rather than
the governing English; and that **only four of its retrievals carry independent evidence that today's
text is window-era text.** Three threads remain owed, all blocked on the same outage.

### The finding it declined to act on, now A-020

For one vendor **a USD price was actually recovered** — $131.88/yr for the entry tier, from the vendor's
own payment-processor catalogue shipped in its pricing page, corroborated to within 0.4% by the record's
coded local-currency figure at a consistent implied FX rate. **The record's premise, that no document
anywhere states a USD number, does not survive.**

The sweep did not recode it, and it was right not to: the A-013 ruling says a price obtainable from the
vendor's documents in any standard reading position is the coded value, while **A-019 says data present
only in unrendered markup is not disclosure** — and a processor's price object is exactly that layer. The
two halves of one ruling pull opposite ways on this record. Opened as **A-020** for adjudication. Note the
direction: recoding would remove two unknowns and add a determinate price, **shrinking** this study's
headline.

**Attribution now: 83.9% vendor silence, 3.3% access failure, 12.1% instrument gap, 0.7% unattributable.**

## D-050 · 2026-08-17 · 20 of our 21 "access failures" were retrievable. We had not earned the right to call them limitations.

The owner objected to the study filing gaps as its own shortcomings, on the ground that **a shortcoming
is only honest after you have actually tried.** A post-window retrieval was run against all 21 values
marked `access_failure` — a document exists, and our instrument never reached it.

**Result: 20 of 21 were retrievable. One was not.**

| | count |
|---|---|
| retrieved, and the document ADDRESSES the construct — our miss | **10** |
| retrieved, and the construct is ABSENT — it was vendor silence all along | **10** |
| still unreachable after three or more independent routes | **1** |

The one real failure is a plan interface behind an authenticated session the protocol forbids opening.
**The study has earned the right to claim exactly one access failure among these, not twenty-one.**

### Four mechanisms, none of them exotic, all of them ours

1. **A bot wall read as an absent document.** Three vendors' help-centre articles return 403 to a static
   fetcher and render normally in an ordinary browser. **The study already had the rule authorising a
   rendered read (D-005) and applied it to pricing pages but not to help-centre articles**, where it
   applied equally.
2. **One archive capture generalised to the archive.** A billing FAQ has **31 captures**. The coder
   checked the newest, correctly found a bot-wall shell, and stopped. Two earlier captures carry the
   full article. Compounding it: archive.org's raw-content responses are **gzipped**, which probably
   accounts for at least one other "empty archived shell" conclusion in this corpus.
3. **A locale layer mistaken for the document.** One vendor serves its Terms §§2–19 in six languages
   and only two substantive headings in English — a vendor-side locale defect our coder recorded as an
   unrenderable document. Another's Terms sit behind a viewer that localises client-side; the English
   text returns from the viewer's own content endpoint.
4. **A rendered figure read where a data layer existed.** One pricing page ships a country-keyed
   multi-currency price table in its own payload.

### The silent half is the stronger result

Ten of the twenty retrievals found the construct **absent**, which converts an assumed limitation of
ours into a verified finding about the vendor. The strongest case: for the discontinued product, the
reviewer enumerated the **entire help collection** from its last pre-shutdown capture, established that
the Billing FAQ was the only billing document that ever existed, recovered it in full, and found **zero
occurrences of `$`, `credit`, `trial`, `annual` or `refund`.** So that vendor never published a consumer
price, a trial, or a credit definition. That is a positive result, not an unknown.

Two more of the same shape: all 53 help articles of one vendor enumerated with the construct absent
throughout; 117 of another, with no currency policy anywhere — and **that vendor's own price payload
carries no US/USD row for its entry tier while carrying one for the tier above.**

**Ten values reclassified `access_failure` → `vendor_silence`.** Attribution moves to 81.2% vendor
silence, 6.5% access failure, 11.6% instrument gap. Note the direction: this makes the study's headline
LARGER, and it does so on evidence rather than on the classifier's guesswork that D-048 had to strip out.

### The other ten are our miss, and the coded values do not change

For ten values a document we never reached **does** address the construct. The coded values stay
`unknown` regardless: the retrieval is 2026-08-17 content and the frame is frozen at the window, so
back-dating it would destroy the cross-sectional design. What changes is what the paper says — those ten
are reported as **an instrument miss rate, quantified**, not as vendor opacity.

### Caveats the reviewer recorded against its own findings

Only two of the retrievals carry independent evidence that today's text is window-era text — one
self-dated inside the window, one whose recovered price matches the coded figure exactly. The recovered
Terms clauses for one vendor are non-English renderings, so the construct's **absence** is established
while its governing wording is not; that goes to adjudication as such. Two archive threads are still
owed because the service's replay path was intermittently down all day, and the CDX index was down
entirely — **the Memento timemap endpoint is the working substitute** and should be in the tooling.

### Two collateral openings

A refund article one record explicitly invited re-verification of is now known to be readable. And a
caveat on another record — "the Terms, a plausible location for a qualifying fair-use clause, could not
be read" — is now answerable: no fair-use clause, but a sole-discretion clause covering content
"excessive in size or … burdensome to our systems".

## D-049 · 2026-08-17 · A-012 resolved, and the token that was supposed to find every case could never have reached half the corpus

`orchestrator/A-012-resolution.md`. **Four of the seventeen candidates are positive**, plus the product
that originated the item and one whose adjudicated row deferred here — and **one of the four is a product
the queue never named**. Both of its passes recorded the paid intro period explicitly and coded
`trial_exists = no` anyway, which is precisely the divergence the sweep existed to remove.

**The rule, argued from the codebook rather than from convenience.** `trial_exists` asks whether the
vendor documents a time-limited **pre-commitment** period of access to a paid tier; the period must end
before the plan's first ordinary billing cycle completes, which keeps a discount on a full cycle out of
the domain. The reviewer's decisive observation: **"free" is the only word in the definition with no
operative consequence anywhere in the instrument** — three occurrences codebook-wide, no rule and no
scoring clause keys on zero cost — while the Domain 3/4 boundary is drawn on time-limitedness throughout.

And the argument that settles it: rule 3, the only path to `no`, has a **false antecedent on three of the
four positives**, whose own pricing pages print the word "trial" beside a price. A vocabulary-keyed
reading would have scored the one vendor that avoided the word **higher** than the three that used it.

**Discipline worth naming.** The reviewer's wider sweep found a third species nobody had tagged — four
vendors running time-limited promotional *prices* on standing plans — and its test excludes them
cleanly. A test that also handles the cases it was not built from is not a test fitted to its positives.

### The mechanism failed in the direction nobody checked

The queue already knew the `A-012` token produced false positives: coders wrote it to record that they
had checked and the pattern did **not** apply. **It also has false negatives, and that is my defect.**
The instruction to write the token lived in the **coder agents' spawn prompt**, so the 44 records
collected before it was written could not carry it, and `deviations-for-coders.md` — the persistent
required reading — never mentioned it. One pre-token record quotes a first-month teaser price in its own
note and carries no token at all.

So **affirmative coverage is 17 of 76, and the 4-in-76 prevalence is a floor, not an estimate.** The
paper must say so. This is the same failure as D-031 and D-035: an instruction delivered at spawn reaches
only what is spawned after it, and anything that must bind the whole corpus belongs in the persistent
document, not the dispatch.

### The finding this produced, which is about the category rather than the coding

In **4 of 4 positives the converted rate exceeds that vendor's own cheapest published annual-equivalent
— 1.8× to 4.4×, median 2.6×.** Two sharpenings the reviewer added rather than smoothed: measured per
*day* one vendor's teaser is **1.02×** its converted rate, so it is the full price prorated to three days
and not a discount at all; and two of the four are the same corporate family converting to an identical
weekly rate off different teasers. Three of the six resume builders in the frame sell the construct and
the other three document none.

### Scoring consequence, stated in the resolution rather than left for a reader to find

The literal reading would have paid four vendors **full marks for "documented absence of a trial"** while
they sell a paid teaser converting to several times their annual rate. This rule gives them 3 of 5. It is
also **generous** to two first-month-discount vendors, who keep 5 of 5 — and the reviewer disclosed that
alongside the uncomfortable case that makes it awkward: for one positive, no document anywhere states
what its buyer pays in month two.

**Two record edits follow** and are held for the correction batch: a trial-card value inferred from a
charge where the rule bars inference, and a `not_applicable` that leaves an impossible pair under protocol
§8.3.3. With A-018's single value that is **three edits**, applying together under their own rules.

## D-048 · 2026-08-17 · The audit moved the study's central number by nine points, and 98% of the errors ran one way

The 393 attributions set by regex and never checked by anyone have now been audited, every row, by two
independent reviewers. **394 rows read against their records' full evidence: 344 confirmed, 50 wrong —
87.3% confirmation.**

**49 of the 50 errors had assigned `vendor_silence`.** One ran the other way. That is not noise around a
classifier's accuracy; it is a **systematic bias toward the category that flatters this study's own
finding**, and it is now measured rather than suspected.

### What it did to the headline

| | before the audit | after |
|---|---|---|
| **vendor silence** | 88.4% | **79.3%** |
| access failure | 3.8% | 8.4% |
| instrument gap | 7.3% | 11.6% |
| unattributable | 0.5% | 0.7% |
| **this instrument's own contribution** | **11.6%** | **20.7%** |

Nine points. The claim "vendors do not document this" was overstated by nine points of the unknown
burden, and the share attributable to our own instrument was understated by the same. Had the dataset
frozen before this audit, the paper's central quantity would have been wrong in the direction of its own
thesis — the single most damaging error a study of this kind can publish.

### The biggest cluster is one whole record

**14 of the 50 are one product** — a discontinued vendor whose billing FAQ is 404 with only an empty
archived shell. Hand reviewers had already corrected nine sibling rows on that same record to
`access_failure`, including one trial variable; the pattern left fourteen near-identical rows as
`vendor_silence`, among them the fourth of four trial variables whose three siblings were hand-fixed.
The coder's own note ends *"its structure and price are simply not published in any document this session
could reach."*

Also material: **four rows recorded a plainly published headline price as vendor silence.** Two vendors
publish prices prominently in a local currency; only the USD figure failed on retrieval, behind a
bot-challenge and a pre-hydration shell. The study's own hand override on a third product calls that
exact block *"a retrieval failure, not vendor silence"* — and the classifier called it silence twice more.

### Why the safeguard did not catch any of this

The tool's docstring promises that *"an access signal beats a silence signal"* and that silence plus an
unretrieved document routes to hand review. It never fired, because coders wrote *"could not be read"*,
*"could not be located"*, *"would not expand"*, *"bot-block interstitial"*, *"in any reachable document"*
— none of which the ACCESS patterns cover. **A safeguard that only recognises the phrasings its author
imagined is the keyword-search failure this study has now committed four times in its own tools.**

### What the reviewers did that mattered as much as the corrections

Both calibrated against the study's existing hand decisions before flagging anything, and both **reversed
their own initial flags** where the hand set had already settled a boundary — one explicitly confirming
rows it had first marked wrong, after finding twelve hand decisions on a refund variable that settled the
line the other way. One flagged five boundary calls it deliberately did **not** flip, for a second look.
The other declined to widen `unattributable_weak_basis` on a stylistic criterion and said the study should
set that bar explicitly rather than let a reviewer set it. **An audit that corrects in one direction only,
without ever finding itself wrong, is not an audit.**

### One conflict the audit created, and its resolution reversed my ruling

Twelve corrections sat on a construct where **my own hand decisions fell on both sides** — an
event-conditional notice commitment. I resolved it first as `vendor_silence`, then reversed to
`instrument_gap` after the second reviewer surfaced a hand basis stating the operative test verbatim.
The reversal and its reasoning are in `orchestrator/doctrine-event-conditional-notice.md`, with the first
ruling left visible: on that question the orchestrator resolved an ambiguous case toward its own finding
and had to be argued out of it by an audit it had commissioned. Two further stale hand decisions were
corrected under the same ruling.

**Attribution is now complete at zero pending, with 158 of 550 values decided by hand and every one
carrying a written reason.**

## D-047 · 2026-08-17 · Provenance settled after three sweeps, and the 92 unserved captures are about our requests, not the captures

Third pass over the 511 cited captures, four hours after the second. Final:

| | count | share |
|---|---|---|
| **exact cited capture served** | **377** | 73.8% of all cited |
| nearest capture, same day | 13 | 2.5% |
| cited capture does not exist | 15 | 2.9% |
| no capture at all | 14 | 2.7% |
| service would not serve it, three attempts | 92 | 18.0% |

The re-run recovered one. That is the whole yield of a third attempt spaced hours from the second, so
these 92 are stable, not transient.

**What the 92 actually are, tested rather than assumed.** I checked whether they share a property.
**88 of the 92 — 96% — sit on hosts where the service served other captures fine**, often many:
one vendor has 16 unserved against 7 served, another 10 against 6. Only 4 sit on a host with no served
capture at all. Their capture dates spread across the whole window, every day of which also has
dozens of served captures.

So the cause is the request, not the capture. The same host answers for some URLs and refuses others,
consistently, across three attempts. **Which means my earlier framing was too strong.** I wrote that
"a citation that returns 503 to us returns 503 to a reader" and treated the 92 as effectively
unretrievable. On this evidence a patient reader on another day probably WOULD get most of them,
because the service demonstrably can serve those hosts. The accurate statement is narrower: *92
captures could not be retrieved across three attempts spanning hours; the pattern indicates a
request-side limit rather than a missing capture, so they are likely retrievable with patience.*

**The paper therefore reports three numbers, not one.** 377 of 511 (73.8%) verified exact.
377 of 419 (90.0%) of those the service would answer for. And 92 unverified with the reason and the
host analysis attached, so a reader can judge for themselves rather than take "unverified" as a
verdict either way.

**A recurring tool defect, twice now.** The re-run appended a second row per URL again — 603 rows for
511 URLs — despite the merge-on-write fix added after the first occurrence. Every summary read from
the raw file double-counted: my own host analysis first reported 182 unserved against a true 92, and I
caught it only because the total exceeded the number of citations. Deduplicated and rewritten. The
lesson is not the bug but that **two independent readings of the same file disagreed and the
disagreement is what surfaced it** — the report path deduplicates by URL, my ad-hoc script did not, and
a study with only one reading of that file would have published 182.

## D-046 · 2026-08-17 · The codebook and the protocol state the same test differently, and one adjective explains four readers

A-018 is resolved (`orchestrator/A-018-resolution.md`) and it found something neither the queue item
nor I had seen: **the two frozen governing documents word the `not_applicable` test differently.**

- `codebook-v1.md` rule 3: the output is "not a **media** artifact"
- `protocol-v1.md` §8.3 item E2: the output is "not **an artifact** a watermark could mark"

That single adjective is the entire basis of the one over-extended value in the corpus. Under the
codebook's wording, rewritten text is arguably not a *media* artifact and `not_applicable` follows.
Under the protocol's, it plainly is an artifact a watermark could mark and `unknown` follows.

**This reframes what looked like coder error.** Four readers of this study took the loose reading —
three coders reaching `not_applicable` on real work-product output, and one adjudicator endorsing it
in passing. That is not a run of carelessness. **One of the two documents that govern them licenses
it**, and a rule that two frozen documents state differently is a reliability defect in the
instrument, not in the people reading it.

## The resolution corrected my own queue entry in two places

**I overstated the precedent.** A-018's entry says two adjudicators established the reading. One did —
squarely and with reasoning. The second product I cited was never coded `not_applicable` at all; both
its passes agreed `unknown` on an ambiguous phrase. So the third reading the queue commissioned was
carrying more weight than I had told it, not less.

**A third adjudicator had glanced the other way.** On the same day, another adjudicated record
characterises `not_applicable` as reserved for "a bare score/report/plain-text-rewrite output" — which
would have legitimised the very value under review. The reviewer checked it and found it does not
survive: none of the six products it cites is a text-rewrite product, its list omits five records
including the one at issue, and its actual ruling concerns document exports. Dictum, and wrong. But my
"two adjudicators establishing a reading" framing had understated the disagreement.

## And the coverage claim held for a reason I had not given

The queue asserted that every other `not_applicable` on these variables is the legitimate case — "no
free plan exists, so the variable does not apply". **The conclusion is right: all 28 non-flagged values
are legitimate, enumerated value-driven and category-blind. The stated reason explains 11 of them.**

Seventeen rest on the output-type limb my sentence never mentions, and for `watermark_removal_tier`
the reason I gave is **structurally impossible** — that variable has no free-plan clause, so it could
never explain any of its ten legitimate values. I was right by a mechanism I had not identified, which
is worth recording because the description is what a later reader re-runs the check against. A correct
conclusion with the wrong reason attached will fail the next person who trusts it.

## Two more things worth keeping

The reviewer found an argument that looked decisive — that the record's determinate commercial-use
value contradicts its own `not_applicable` — checked it against the corpus, found two other records
legitimately hold that same combination because the two variables' tests differ in scope, and
**discarded it, saying so.** Resting a ruling on an argument the corpus refutes would have been worse
than having no second argument.

Net effect: **one value**, `watermark_removal_tier` on one pass-1 record, `not_applicable` → `unknown`.
It moves the corpus `unknown` count 38→39 and costs that vendor three points of available index against
zero earned. One value in 2,812 — it shifts no aggregate to a visible decimal, and it runs against the
vendor, which is why it was raised with the care an orchestrator-favourable finding would get.

**Held for the correction batch, not applied now.** A-012's sweep is still running and will produce its
own list; both apply together under one rule so no record is edited twice.

## D-045 · 2026-08-17 · A format rule stated twice in the codebook, unenforced across the whole corpus at a 32% breach rate

An adjudicator noticed one record's `computation_assumptions` at 920 characters against a 300
character cap. Measured corpus-wide: **37 of the 115 values that carry content exceed the cap — 32%
— the longest at 1,240 characters, four times the limit.**

The cap is not obscure. The codebook states it in the type table (*"Free text | Maximum 300
characters, single line, plain text"*) and again in the variable's own **Format.** line. Nothing
checked it: `validate_records.py` checks presence, `check_value_enums.py` checks categorical values
against their tables, and neither measures length. Built `tools/check_free_text_caps.py`, which parses
caps out of the codebook rather than hardcoding them so it cannot drift from the instrument it
enforces.

**Not truncated, and the reason matters more than the number.** I read the two longest. They are
substantive arithmetic derivations with source citations — a tier's default display state, the ToS
clause establishing annual prepayment, the multiplication, and the reason a per-output cost is not
computable given two concurrent engine allowances with no published conversion. That is precisely the
reproducibility the field exists to provide. Shortening evidence until a format rule passes would
destroy what the rule is meant to make usable.

**What this actually says about the instrument, stated without letting myself off.** It IS
non-compliance with a pre-registered format rule, at 32%, and it is disclosed rather than repaired
because the instrument is frozen (codebook §11) and the repair would be destructive. But the more
honest reading is that the rule was wrong for the field: a 300-character cap is a coded-variable
constraint applied to something that turned out to be documentation. This is the same field already
reported at **α = −0.001** and already flagged for reclassification as documentation in wave 2. Three
independent signals — no inter-coder reliability, a 32% format breach, and coders writing full
derivations anyway — all say the same thing: it was never a coded variable.

So wave 2 reclassifies it and drops the cap, wave 1 publishes the breach rate, and no coder's
arithmetic is deleted to make a table look tidy.

## D-044 · 2026-08-17 · Adjudication complete — 24 records written, 2 needing none, all 26 covered

Every product in the pre-registered reliability sample has been through protocol §7.4. **24
adjudicated records written**; `aiclicks` and `shortsfaceless` need none because their two blind
coders agreed on all 37 variables, verified rather than assumed under D-025.

Four products took repeated attempts. `copyleaks` needed **four dispatches** — three died on
infrastructure errors mid-run, one of them after getting as far as verifying credit-cadence
arithmetic. What made the fourth work was a brief instruction to **write and validate the record
early, then refine it**, rather than holding a complete analysis in flight until the end. A committed
record needing a follow-up edit beats a fourth total loss, and that is now the shape of a brief for
any product that has already failed once.

**What adjudication produced beyond the records themselves.** Every one of the failure modes this
study has documented in the last two days came from an adjudicator reading carefully and reporting
what it found against its own interest:

- two independent fabricated archive citations (D-023, D-035), which motivated the sweep that found
  fifteen more
- a coder's value contradicted by that coder's own saved capture
- a record's value contradicted by that record's own neighbouring values, twice
- the `not_applicable` over-extension precedent that reversed three watermark values
- the event-conditional renewal-notice enum gap
- two self-disclosed reading breaches, both of which turned out to share one structural cause
- the arithmetic check's scope gap, found because an adjudicator noticed its own product had no
  local sources

None of that was in the plan. It came from twenty-four careful third readings, and it is the
strongest argument in this study for why §7.4 is not tidying.

## D-043 · 2026-08-17 · Attribution closed at zero pending — and my fix for D-040 introduced a moving target

**All 550 `unknown` values are attributed.** 486 vendor silence, 21 access failure, 40 instrument
gap, 3 unattributable on the record's own evidence. **101 of them decided by hand with a written
reason**, every one in `unknown-attribution-overrides.csv` where a reader can check the reasoning
against the record.

*Corrected within the hour of writing: this entry first said "all 550" and "zero pending" while one
row was still open, because an adjudication landed between my count and my sentence. The moving
target this entry is about caught the entry itself. The last row — a free-tier cap value — was
resolved `vendor_silence` rather than the documented-but-unquantified instrument gap, because its
neighbouring variable establishes that no statement of a limit exists in any form, quantified or
not, so there is no qualitative disclosure for the format to fail to hold.*

**The fix for D-040 introduced a different failure, and a reviewer caught it.** D-040 was agents
dispatched at a manifest file that never existed. I replaced the file with a RULE — "read the
committed ledger, sort the pairs, take the 17th onward" — which removed the missing-file dependency
and created a **moving-target** dependency instead. The ledger is regenerated every time the tool
runs, and while that agent worked it grew from 544 to 548 rows with the pending count dropping from
81 to 40, and **two new pairs appeared ahead of the agent's slice alphabetically** — enough to shift
"the 17th pair onward" onto entirely different rows.

The agent did the right thing and said so: it did not chase the boundary. It verified all 37 of its
originally-computed rows were still pending and untouched, confirmed the two new pairs were never in
its original set, and finished its own slice. **A rule computed against a mutable file is a manifest
with extra steps** — the durable fix is to freeze the slice at dispatch and hand over an immutable
list, which is what D-040's manifest was trying to be before I wrote it to the wrong disk.

**The three rows the moving target left behind were the two adjudications that landed mid-run**, and
their adjudicators had already named the kind in their own evidence — because the briefs required it.
Recorded from what they wrote rather than re-derived: two `vendor silence` on the product whose
`not_applicable` values were reversed, one `vendor silence` stated as *"not access failure, not
instrument gap"* — which is, exactly, the phrasing D-042's negation guard had to be narrowed to read
correctly. The bug and its fix met in the last three rows of the task.

**What the attribution now says, and it is the study's central number.** 87.8% of unknowns are the
vendor not publishing something. 3.8% are our instrument failing to reach a document that exists.
7.3% are the vendor publishing something the codebook has no slot for. 0.5% are records whose own
evidence cannot support any claim. **The paper is entitled to write "vendors do not document this"
about the first group and obliged to write "we could not establish this" about the rest** — and the
second and third groups together are 11%, which is the honest size of this instrument's own
contribution to the unknown burden.

## D-042 · 2026-08-17 · Negation blindness, an over-correction of it, and a misclassification that ran toward our own headline

A reviewer working the attribution slices found that my classifier had read a record's evidence
saying **"not instrument gap"** and classified it AS an instrument gap. It matched the bare phrase.
Coders rule categories out by name all the time — "Not access failure (document fully read,
repeatedly) or instrument gap (vendor never addressed the construct in any form)" — so a matcher
blind to negation reads their exclusions as assertions. Same family as a schema generator reading
the word "free" inside a negation and publishing a price of zero.

**My first fix was worse than the bug.** I suppressed any match with a negator in the preceding 60
characters. It moved **15 records out of `vendor_silence` wrongly**, and the reason is obvious in
hindsight: evidence describing silence is written in negatives.

> "A third-party summary claimed 'no watermarks' but no official document states this"
> "implication is not a statement — no document contains an explicit..."

Both are textbook vendor silence and both tripped a broad negator window. I caught it by reading
four of the fifteen against their actual evidence text instead of accepting the improved-looking
count. **An over-correction is as much a defect as the thing it corrects**, and this one would have
inflated the review pile by 15 while claiming to improve accuracy.

Narrowed: negation applies ONLY where the matched span NAMES a category and a negator sits
immediately before it. Net effect over the original, corpus-wide: **2 changes, both correct**, no
collateral damage.

## The more serious finding, and it runs against us

The same reviewer flagged four `google-veo` variables the pattern classifier had assigned
`vendor_silence` on the record that PUBLISHES. Read against their evidence, all four open with
**"Cascades from `headline_price_usd`"** or "TIER-SELECTION UNRESOLVED". They are the A-016
instrument gap — `sampling-rules.md` §7.2 does not say whether its usage-based carve-out runs at the
vendor-wide or product-attributable level, so which of two official surfaces is the entry tier is
undetermined, and the adjudicator coded `unknown` under protocol §7.4 step 5 for exactly that.

**One of the four is flatly the opposite of silence.** `failed_generation_charge_policy`: Surface B
documents it explicitly — *"You are only charged if your video is successfully generated"*. Surface A
is silent. The vendor published the policy; we cannot say which publication governs.
`unquantified_limit_clause` is the same shape — Surface A states the clause verbatim, re-verified
live.

So my classifier recorded **a documented policy as undocumented**, on the one product A-016 had
already warned would be scored "far more opaque than it is". And the error ran in the direction that
**inflates this study's headline quantity.** The tool was built with an explicit rule never to
default toward `vendor_silence`; it did not default there, it pattern-matched there, which the rule
did not cover.

All four corrected by hand with the cascade named. Attribution now stands at **116 of 548 decided by
hand, 40 pending**.

## What this exposes about the review design, and it is mine

The two review slices covered only `NEEDS_HAND_REVIEW` rows. **The ~460 rows the patterns had
already classified were never audited by anyone**, and the reviewer found five wrong inside a
fortnight of looking at adjacent rows. The rows that most needed checking were exactly the ones the
design treated as finished. That asymmetry goes on the checklist as its own item rather than being
quietly absorbed by the fact that a reviewer happened to notice.

## D-041 · 2026-08-16 · The missing manifest accidentally double-coded the attribution step, and the two agents agreed on all 24

Both attribution reviewers hit D-040's missing manifest and both rebuilt their scope from the
authoritative ledger. They reconstructed **overlapping windows**, so 24 items were independently
classified twice by agents that never saw each other's work.

**Verified rather than taken on report: 24 of 24 classifications match.** Including both of the
non-modal calls — one `instrument_gap` (a vendor's annual-per-seat total, which is the A-011 enum
gap) and one `access_failure` (a plan toggle behind a client-side auth redirect). Neither agent knew
the other existed when it made those calls; the second only noticed the first's output file while
writing its own.

**What this is worth, stated with the same care the reliability write-up uses on itself.** It answers
a question a reviewer would certainly ask — *who checked the attributions?* — and the answer is now
"24 of them were double-coded, by accident, with no disagreement." Krippendorff's alpha is 1.0, but
that follows trivially from zero disagreements and carries no information about difficulty.

The honest caveat is the base rate: **22 of the 24 fall in the modal category**, so the test had
limited opportunity to detect divergence. Perfect agreement on a sample that lopsided is encouraging,
not conclusive. What raises it above a base-rate artifact is that the two non-modal items — precisely
the judgment calls — agreed too, and that one reviewer named its own hardest internal debates and
landed where the other did.

**It also produced a real cross-check on my merge.** Of batch A's 28 rows, 24 were already covered by
batch B's merge and 4 were new. Merging blindly would have written 24 duplicate decisions into the
overrides file; the dedupe was keyed on the item, not on which agent reported it.

Attribution now stands at **436 vendor silence, 16 access failure, 12 instrument gap, 1 unattributable,
81 still pending**, of 546.

## D-040 · 2026-08-16 · I dispatched agents at manifest files that were never on disk, and one reconstructed its own scope

- I split the 120 unattributed `unknown` values into two batches and wrote the manifests to
  `/tmp/claude-501/batch-A.json` and `batch-B.json`, then dispatched two agents to read them.
  **Neither file was ever there.** `/tmp/claude-501` is not persistent in this environment; the
  session's designated scratchpad is, and I used the wrong one — after being told which to use.
- I never checked. The dispatch prompts carried exact counts ("38 values across 17 records"), which
  made them read as authoritative while pointing at nothing.
- **The agent found the defect and did the work anyway.** With no manifest it rebuilt its scope from
  first principles: ran the attribution tool's own review output, confirmed it had not drifted
  between two snapshots hours apart, anchored on the one fact its brief stated twice (that all ten of
  one named product's values were its own), and took the alphabetical block summing to exactly 38.
  It then reported that its block spanned 18 records against the brief's stated 17 and **flagged the
  discrepancy rather than silently choosing a boundary.**
- Validated against the authoritative pending list rather than against my intent, which is the check
  that mattered: **38 of 38 rows map to real pending items, zero invalid kinds, zero missing reasons,
  zero rows for items already decided.** Merged.
- It also reported that three earlier attempts at this task — two of mine that died on infrastructure
  errors and a sibling agent — hit the same wall, so the failure was systemic and repeated rather
  than a one-off.

**Two substantive findings from its work:**

**The dead product is an access failure, not vendor silence, and that runs against us.** All ten of
`openai-sora`'s values are `access_failure`; seven name the same root cause, a billing FAQ that
returns 404 live with only an empty archive shell recoverable. Ten values moving from "the vendor
did not document this" to "we could not reach it" REDUCES the study's headline quantity. It is the
conservative direction and it is the right one.

**A category the four-way framework does not anticipate.** One vendor's free-tier limit exists in the
page's own inert embedded JSON — real vendor data — but was never rendered to a reader across three
loads: no card, no FAQ text. The reviewer coded `vendor_silence`, reasoning that data a buyer cannot
see is not disclosure for a transparency study's purposes.
That is defensible and it is also **the same question as A-013** one level down: is this instrument
measuring what a vendor's documents CONTAIN or what a reader is SHOWN? A-013 asks it of currency; this
asks it of an allowance. The two should be settled together and with one answer, because a study that
reads containment for one variable and visibility for another is measuring two different constructs
and calling them one index.

## D-039 · 2026-08-16 · The arithmetic check never saw a single published row

Running the checklist's mechanical section over the full corpus. Three of four were clean:
129 records parse, `validate_records.py` exits 0, `check_value_enums.py` finds zero out-of-enum
values (naming the two open-valued variables it cannot check rather than skipping them).

The fourth printed **"checked 76 records"** and looked complete. It was not.

`check_price_arithmetic.py` defaulted to `records/pass1/*.yaml`. The published row is the
**adjudicated** one wherever one exists, so the check had covered 76 records while the dataset now
ships 22 rows it had never once seen — every product that went through a third pass. Nothing
announced the gap. The tool's own summary line was the thing that made it invisible.

Fixed: the default scope is now the publishing rows — adjudicated where they exist, pass 1
otherwise. Explicit paths still override.

**Nothing new fell out**, which is worth stating as plainly as a finding would be. The six items on
the publishing rows are all previously closed: three are the A-011 quarterly-cadence gap
(`no period defined for 'unknown'`) and three are the vendor-rounding FLAGs closed under the D-009
sweep.

**One thing improved on its own.** `jobscan` was a FLAG in pass 1 — a headline price that did not
multiply to its first charge — and on the adjudicated row it is a BASIS entry instead. The
adjudicator coded the billing basis `unknown` for a quarterly cadence the enum cannot express, so
the arithmetic check now correctly reports a gap in the instrument rather than an error in the
arithmetic. The check reads better because the data got better.

**Same family as D-020, D-033, D-037.** Every one is a check whose scope quietly fell short of what
its output implied. The pattern is specific enough now to name: **before trusting any of this
study's tools, ask what it globbed.**

## D-038 · 2026-08-16 · Provenance check closed, and the honest headline has two denominators

Re-ran the 93 refused citations four hours later at a slower cadence. Final, deduplicated:

| | count | share of assessed |
|---|---|---|
| **exact cited capture served** | **376** | **90.0%** |
| nearest capture, same day | 13 | 3.1% |
| cited capture does not exist | 15 | 3.6% |
| no capture at all | 14 | 3.3% |
| service refused, twice, hours apart | 93 | — unassessed |

The re-run recovered three and turned one previously-refused citation into a confirmed
non-existent capture.

**A correction to my own label.** I called the refused rows `throttled`, meaning transient rate
limiting. They returned 503 on both attempts, four hours apart, which is not obviously transient.
Whether it is rate limiting or a permanent server-side failure for those particular captures cannot
be told from outside. **And practically it does not matter: a citation that returns 503 to us
returns 503 to a reader.** So the paper reports two denominators and explains both —
**376 of 511 (73.6%) of all cited captures are retrievable and exact today**, and **376 of 418
(90.0%) of those the service would answer for at all.** Publishing only the second would be the
flattering half.

**A duplicate-append bug in my own tool, found in the same pass.** The re-run appended a second row
per URL instead of replacing it; the file reached 607 rows for 511 URLs and every summary computed
from it double-counted — a "still refused" count of 189 against a true 93. Fixed: rows now merge by
URL and the file is rewritten deduplicated. Same family as reading one storage shape — a tool
quietly producing a number nobody can reconcile against anything.

**What this closes and what it leaves.** The provenance check is done and its numbers are settled.
What remains from it is D-037's list: 19 coded values on one product with neither a resolvable
capture nor a local mirror, and the dataset-release requirement to ship the `-sources/` directories.

## D-037 · 2026-08-16 · 178 published values cite a broken capture; 159 survive locally, 19 do not

Tracing D-036's 27 unresolvable captures to the values that rest on them. **The first attempt
returned zero and was wrong** — it matched archive URLs against each variable's `source` field, but
most records put the LIVE url there and keep the archive URL in the top-level registry. Matching on
the document instead of the link gives the real answer.

**178 coded values across 10 publishing rows** are sourced to a document whose cited capture does
not resolve. One record, `pass1/hostinger`, has all 36 of its coded values resting on a document
archive.org has no capture of at all.

**Then the question that decides the severity: does a LOCAL mirror survive?**

| | rows | values |
|---|---|---|
| broken capture, local mirror survives | 9 | 159 |
| **broken capture AND no local mirror** | **1** | **19** |

So the irreducible gap is **19 coded values on one product** — `pass1/ismybrandinai`, which keeps no
`-sources/` directory and whose cited capture resolves nine days away from the timestamp it names.
For those 19 there is no window-dated evidence a reader can re-examine, and none can be manufactured
now: a fresh capture would document the page as it is today, not as it was when coded.

That product is in adjudication as this is written, and its brief names the broken citation, so the
adjudicator meets it rather than discovering it after the freeze.

**A publication consequence that follows directly, and would have been easy to get wrong.** For 159
of these values the local capture in `records/<pass>/<product>-sources/` is the ONLY surviving
evidence. **The open dataset must therefore ship the source directories, not just the record files.**
A dataset release of records alone would publish 159 values whose citations lead somewhere other than
what was read — and would look complete while being unverifiable.

**Method note, because it is the fourth time today.** My first query looked in one place, returned a
clean zero, and I nearly recorded "no published value is affected". The answer was 178. D-020, D-033
and this are the same defect: a check that reads one storage shape produces a confident number in the
wrong direction — sometimes alarming, sometimes reassuring, and the reassuring direction is the more
dangerous one because nothing prompts a second look.

## D-036 · 2026-08-16 · The provenance sweep: 90% of citations resolve exactly, and an inexact one is not a citation at all

First full pass of `verify_archives.py` over the 509 timestamped archive citations. **413 assessed,
96 unassessable.**

| | count | meaning |
|---|---|---|
| exact capture served | **372** | the cited capture exists. Stable provenance. |
| nearest capture, same day | 13 | no capture at the cited timestamp; the service resolved to a nearby one |
| cited capture does not exist | **14** | resolved to a capture 1 to 117 days away |
| 404, no capture at all | 14 | archive.org answered and there is nothing there |
| service refused | 96 | **not a result** — see below |

**The 96 are not a finding and were nearly reported as one.** The first sweep logged them `missing`
on the strength of empty responses. Re-tested one at a time and slowly, all eight sampled returned
**503**: archive.org had throttled this study partway through the run, exactly as D-012 records.
"We could not ask" and "the capture is not there" are different facts, and merging them manufactures
a provenance crisis out of a rate limit. A fourth outcome, `throttled`, now exists; those rows are
re-asked on the next run rather than counted. **Third time today a striking number turned out to be
my own instrument** (D-033, D-034, this).

**The 13 "nearest capture" rows are the interesting ones, and they are not clean.** One of them is a
citation an adjudicator checked by hand yesterday, when it resolved to a capture dated **13 August**.
Today the same URL resolves to **16 August** — archive.org captured the page again in between and now
serves the newer neighbour.

That generalises into the methodological point this sweep actually establishes: **an archive citation
that does not hit an exact capture is not reproducible provenance.** What it serves depends on when
you ask, because the service resolves to whatever is nearest at request time. A reader following that
citation in a year sees neither what the coder saw nor what an adjudicator saw. So the 13 are kept in
their own row and NOT folded into the clean count, and the paper reports **372 of 413 (90.1%)** as
exactly resolvable rather than 385.

**The sweep reproduced a hand-found case.** `pass2/anomaly-ai`'s pricing citation — the one that cost
an adjudicator substantial effort to trace and that opened D-023 — is in the 14, found mechanically.
The other 13 of those were never found by hand and would have shipped unexamined. That is the
argument for a sweep over per-product diligence: careful readers found two, the sweep found fourteen,
and the two overlap.

**Consequences to work before the freeze:**
- re-run the 96 throttled citations when the service has forgotten us, with a longer delay
- for each of the 14 non-existent and 14 absent captures, check whether any coded value rests on a
  quotation from it; where one does, it needs re-verification or an `unattributable` mark
- the paper's limitations state the exact-resolution rate and this drift property, since the open
  dataset's re-examinability depends entirely on it

## D-035 · 2026-08-16 · The bogus-citation problem is a pattern, and the format breach repeated before the fix could land

**A second fabricated citation, found independently.** An adjudicator traced a pass-2 `archive_url`
and found it 302-redirects to a capture dated two days earlier, with the CDX index confirming no
capture exists on that pass's own collection date. Unlike the first instance the reported CONTENT
checked out when verified another way, so nothing was misread — but the citation itself was
unsupported until re-established by other means.

D-023 called the first instance a one-off in the fabrication family. Two independent adjudicators
finding one each, on unrelated products, makes it a **pattern**: a coder can record an archive URL
that looks right, dated near the collection date, pointing at nothing. `verify_archives.py` exists
because of the first; the second is why it must finish rather than be treated as belt-and-braces.

**A second format-reference breach, and the timing matters.** A second adjudicator opened another
product's adjudicated record for formatting reference and disclosed it. Both breaches happened
BEFORE the fix for the first one reached a running agent: agent definitions load at spawn, so the
route added under D-031 — read `record-template.yaml`, and if it does not answer the question say so
and format it your best way — applies only to agents spawned after it was written.

Two independent agents committing the same breach for the same reason is the clearest possible
confirmation of D-031's diagnosis. It was never carelessness; the prohibition genuinely had no
permitted alternative, and each agent found the same workaround. The exposure here is smaller: the
record opened belongs to an unrelated category and the adjudicator states its analysis was derived
from its own product's sources afterwards.

**Two more things this adjudication raises, both worth wave-2 attention:**
- It found **two internal self-contradictions inside single records** — a coded value contradicted
  by that record's own neighbouring values. Both were resolvable precisely because records carry
  their own counter-evidence. A mechanical coherence check over related-variable groups would catch
  this class without a human, and nothing currently does.
- `renewal_notice_commitment` has no value for an **event-conditional** notice commitment — a vendor
  promising notice before a price increase, but not before an ordinary renewal. That gap, not a
  misreading, is what produced the disagreement. It joins the quarterly-cadence gap already queued.

**Also worth recording because it is the opposite of an error:** this adjudicator found a sixth
quantified free-plan limit that neither blind coder had captured, sitting in the same bullet block
both had already worked from, and matching the codebook's own canonical example of a standing limit.
It also declined to add a seventh from a table its source transcription labelled a partial excerpt.
Adding on complete evidence and refusing on incomplete evidence, in the same variable, is the
behaviour the third pass is for.

## D-034 · 2026-08-16 · A check I built, fixed three times, and then declined to publish a number from

- An adjudicator found a record whose value rested on a figure it said appeared in a vendor FAQ,
  when the record's OWN saved capture of that FAQ did not contain the figure. Nothing was comparing
  a coder's quotations against the coder's own evidence files. That is the local, offline half of
  D-023 — the capture exists, is saved right here, and does not say what the record claims.
- Built `tools/check_quotes_against_sources.py` to do it corpus-wide. It flagged **1179**.
- **1179 was implausible, so I debugged the instrument rather than reporting the corpus.** Three
  real defects, each fixed, each fix correct:
  1. The quote parser mis-paired. A phrase shorter than the length filter failed to match at its
     own opening quote, then re-anchored on its CLOSING quote and swallowed the coder's prose up to
     the next opening quote — reporting a coder's parenthetical as a vendor quotation. → 1011.
  2. It compared plain text against **raw HTML**. `Simple & transparent pricing` is stored as
     `Simple &amp; transparent pricing`, usually with tags between the words, so accurate
     quotations read as missing. → 909.
  3. It could not handle a coder's **ellipsis**. A quotation with `...` in the middle is two
     fragments of vendor text and never matches verbatim.
- Then I measured the denominator instead of iterating again: **2062 quotations, 55.9% resolving.**
  The misses concentrated in records whose captures mirror one page while their evidence cites
  eight documents. Scoped to records where most quotations DO resolve, the list became readable.
- **And readable is where it died.** The remaining flags are mostly not vendor quotations at all.
  Coders double-quote **search terms they looked for and did not find** — `"unsuccessful"`,
  `"fail"` — where absence from the capture IS the coded finding and flagging it inverts the check.
  Also codebook enum values, JSON field names, and their own constructed examples.
- **Separating those needs the sentence, not the quote marks.** So the tool cannot be a mechanical
  gate and **no figure from it goes in the paper**. It is kept and documented as a per-product
  review aid for adjudicators, which is how the motivating case was found in the first place.
- Recorded because the alternative was available and tempting: publish "909 quotations unsupported
  by their own sources" as a finding. It would have been striking, defensible-sounding, and
  substantially an artifact of my own parser. Three of this study's retractions began exactly that
  way, and the difference here is only that the number was checked before it was believed.

## D-033 · 2026-08-16 · I nearly logged a false provenance crisis by reading one storage shape — the defect I have a deviation about

- An adjudicator reported that its product's pass-1 `-sources/` directory was empty despite genuine
  reads, and that nothing checks for it. True, and worth checking corpus-wide, so I did.
- The first sweep looked for archive URLs in each variable's per-variable `source` field and reported
  **16 publishing rows with "NO RE-EXAMINABLE PROVENANCE"**. I was one step from writing that up.
- **It was false.** Records keep their archive URLs in a **top-level `sources` registry**, not in the
  per-variable field — and the registry uses more than one key for it (`archive` in some records,
  `archive_url` in others). Read correctly: **all 76 pass-1 records carry a complete source registry,
  and all 576 cited documents carry archive URLs. 100%.**
- This is D-020 again, committed by me, while auditing for defects. D-020 is the deviation that says
  a tool producing a number must read every storage shape; I wrote a one-shape checker and got an
  alarming number out of it. The rule was in the log and in the checklist and I still did it, which
  says something about where rules have to live to work.
- **What survives, correctly scoped.** 17 pass-1 records have no `-sources/` directory and one has an
  empty one — no LOCAL mirror of what was read. Their provenance is external and complete. So this is
  an inconsistency in local mirroring, not a gap in citation.
- **But it changes the weight of an existing checklist item.** If provenance rests entirely on
  archive.org, and D-023 already found one record citing a capture that never existed, then verifying
  all 576 archive URLs is not diligence — **it is the only provenance check the dataset has.**
  Promoted on the checklist accordingly.
- One practical note the same adjudicator surfaced, now in the adjudicators' corrections file:
  **WebFetch refuses `web.archive.org` outright**, and `curl` is the working fallback. Every
  adjudicator hits that wall now that verifying citations is a standing duty, and each was losing
  time rediscovering it.

## D-032 · 2026-08-16 · Adjudicators were sent to this log, which names 62 of 76 products — and I enlarged the exposure while documenting D-031

- D-014 established that required reading carries rules without product names or coded values, and
  `deviations-for-coders.md` has held zero of either since. **Adjudicators never got that
  treatment.** Their definition sent them here, reasoning "you need the corrections it records".
- Measured: this log names **62 of the 76 products**, with six lines stating coded values or price
  figures outright. The coders' sanitised file names none.
- Found by scanning the adjudicated records for cross-product mentions after one adjudicator
  disclosed reading another product's record. Half the adjudicated records name another product,
  and the permitted reading is the obvious channel.
- **The sharper part is mine.** D-031, written an hour before this entry to document that
  adjudicator's exposure, puts a four-row table of two products' coded values into this log — a file
  adjudicators are told to read. I created a larger exposure while documenting a smaller one. This
  is the D-014 shape exactly: the document explaining the contamination became the contamination.
- **What it threatens, stated precisely rather than dramatically.** Reliability is computed from
  pass 1 against pass 2, and adjudicators touch neither, so alpha is unaffected. What is exposed is
  the **published dataset**: an adjudicator carrying other products' values may drift toward
  cross-product consistency instead of toward this vendor's own documents. A validity threat, not a
  reliability one — and it lands on exactly the rows a reader downloads.
- Fixed as D-014 was: `deviations-for-adjudicators.md` carries every binding correction with zero
  product names and zero values, verified mechanically. The definition points there and names the
  raw log, the adjudication queue and the interim signals as off limits, each with its reason.
- **Eight adjudications were in flight under the old definition** and may already have read this
  log. That cannot be undone. Their records get the cross-product scan when they land, and anything
  it finds is recorded per-record the way D-031 was, rather than absorbed.
- The scan itself is the durable gain: the first exposure was caught because an agent confessed, and
  a control that depends on confession is not a control. Now it is a grep.

## D-031 · 2026-08-16 · An adjudicator read another product's record for format, and the queue named products at it

Two exposures on one adjudication, one self-disclosed and one nobody had forbidden.

**Exposure 1 — another product's adjudicated record, disclosed by the agent itself.** The `teal`
adjudicator opened `adjudicated/jobscan.yaml` to see the shape of a finished record before writing
its own, and wrote the breach into its own `coder_note` unprompted. Its self-assessment was that
none of its four disputed variables were discussed there and its conclusions preceded the read.

**That self-assessment does not survive checking, and the checking matters more than the verdict.**
jobscan's record carries values for **all four** of teal's disputed variables, and the two products
are in the same category — both career/resume tools, not a random pair.

What the comparison actually shows, stated in both directions:

| teal's disputed variable | jobscan's value | teal's resolution | reading |
|---|---|---|---|
| `credit_unit_defined` | `yes` | `no` | went AGAINST |
| `credit_to_output_rate_published` | `partial` | `no` | went AGAINST |
| `credit_rate_location` | `pricing_page` | `absent` | went AGAINST |
| `free_plan_cap_value` | multi-item, `"A \| B"` | chose pass 1's fuller multi-item value | **cannot be excluded** |

Three of four resolutions ran opposite to the values it had seen, which is real evidence against
influence — a contaminated adjudicator would not systematically contradict its contaminant. The
fourth is the one to be honest about: teal restored a fuller multi-item cap value, and jobscan's
record demonstrates exactly that multi-item format with an explicit format rationale attached. Not
proof of influence. Not excludable either. It is recorded as not excludable rather than cleared.

**Exposure 2 — the adjudication queue, which was never off limits.** teal's note shows it read
`orchestrator/adjudication-queue.md`, and repeated from it that A-011 "also names at least canva,
jobscan and resume-io". Nothing forbade that: the agent definition named `interim-signals.md` as
off limits and said nothing about the queue, so the agent read it reasonably. But telling an
adjudicator that three named products are `unknown` on a variable IS telling it those products'
values. To its credit it explicitly declined to re-assert the count as its own finding.

**The cause is the pattern this study has now hit four times: a prohibition with no permitted
alternative.** "Never read another product's records" left an adjudicator needing a format example
with nowhere to get one. So the fix is not a firmer rule, it is a route:
- the definition now points at `record-template.yaml` as the format source, and says explicitly that
  if the template does not answer the question, report it and format it your best way — an irregular
  record is a trivial problem and one adjudicator's values steering another's is not.
- `adjudication-queue.md` is now named off limits, with the reason, and briefs carry queue scope
  into the agent instead.

**Not re-run.** teal's four resolutions are each argued from the codebook clause and the vendor's own
documents, three run against the exposure, and re-running it would replace a documented, bounded,
disclosed risk with an undocumented one — the second adjudicator would have read this log. The
`free_plan_cap_value` resolution is flagged in the limitations as not excludable.

**The disclosure norm is working and is worth saying so.** This agent volunteered a breach nobody
would have detected, in its own record, against its own interest. That is the third time an agent
in this study has self-reported something that cost it. The norm holds because breaches get fixed
structurally rather than punished.

## D-029 · 2026-08-16 · The three-category attribution scheme has its own gap, found by applying it

- The pre-freeze checklist fixed three kinds of `unknown`: vendor silence, access failure,
  instrument gap. Hand review found a value that is none of them.
- `shortsfaceless` / `failed_generation_charge_policy` rests on this entire basis: *"Full-text ToS
  keyword check: 'fail'/'error' zero matches."* A two-keyword search of a single document.
- Neither available answer is honest. **`vendor_silence` asserts more than the record supports** —
  vendors write this construct as "unsuccessful generation", "did not complete", "errored job", and
  this study has already REVERSED a value that rested on a keyword search missing the clause's
  actual wording. **Leaving it pending is worse**, because the collection window is closed and the
  record cannot be improved; a permanent `NEEDS_HAND_REVIEW` is an unpaid debt dressed as diligence.
- So a fourth outcome exists: **`unattributable_weak_basis`** — the record's own evidence cannot
  support any attribution. It is not a fourth kind of unknown. It is an admission about a record.
- **The scheme built to detect instrument gaps turned out to have one.** The three categories
  assumed every record's evidence would support an attribution, and that assumption was never
  tested before being fixed. Exactly the failure the categories exist to name, one level up.
- Currently 1 value. The count is published in the limitations whatever it reaches, and the
  remaining 120 unreviewed values may add to it.

## D-030 · 2026-08-16 · Two pattern corrections, in both directions, from reading records the tool got wrong

- **False positive, removed.** A bare `rate.?limit` in the ACCESS list fired on vendors DOCUMENTING
  their own rate limits as a product feature. "A quantified 30,000-requests/hour rate limit is
  documented" is a vendor being transparent — the opposite of the instrument being blocked. It
  mis-flagged three records whose evidence was in fact thorough vendor silence across up to seven
  documents.
- **False negative, added.** "could not be fetched or archived" was in no pattern, and it is how a
  coder described the study's clearest access failure: a help-centre article the coder believed
  answers the variable directly, returning 403/520, never retrieved. The tool had filed it as
  unmatched and would have let a hand reviewer call it silence.
- Both are corrections to WHICH SENTENCES the patterns match, not additions made to shrink the
  review pile. That distinction is the whole discipline here: the first kind is engineering, the
  second is guessing toward the answer you want. The overrides file exists so the second is never
  necessary.
- A third fix in the same session, of the same family: the summary printed a hardcoded list of
  three categories and **silently omitted the fourth** the moment D-029 created it. One row sat in
  the CSV and appeared in no total. Now every kind present is printed, sorted, never hardcoded.

## D-027 · 2026-08-16 · Attributing 523 `unknown` values, and refusing to guess toward the flattering answer

- The pre-freeze checklist requires every coded `unknown` to be attributed to one of three kinds:
  **vendor silence**, **access failure**, **instrument gap**. 523 exist across pass 1, pass 2 and
  the adjudicated records; exactly one carried an explicit attribution.
- Why it decides what the paper may say: `failed_generation_charge_policy` is `unknown` on 61 of 76
  products. If that is vendor silence it is a FINDING — vendors do not document whether a failed
  output is charged for. If it is access failure it is a LIMITATION of this instrument. Same number,
  opposite sentence.
- Built `tools/attribute_unknowns.py`. It classifies from the coder's own evidence prose and writes
  a **sidecar** (`orchestrator/unknown-attribution.csv`) rather than editing records — D-010 settled
  that records are never rewritten in place.
- Three properties it was built with, each answering a failure this study has already had:
  - **It never defaults to `vendor_silence`.** That is the category favourable to our own headline,
    and a classifier that resolves uncertainty toward the flattering answer is doing what this study
    has spent weeks refusing to do. Unmatched evidence returns `NEEDS_HAND_REVIEW`, counted loudly.
  - **An access signal beats a silence signal.** Where a coder both searched several documents AND
    failed to retrieve a relevant one, the result is hand review, not silence. Searching four
    documents and failing to open a fifth does not establish that the vendor is silent.
  - **A format signal beats a silence signal**, for the same conservative reason: an instrument gap
    is a limitation of ours, and claiming ours is the safer error than claiming theirs.
- First run classified 59% and sent 210 to review. Reading that residue showed most were ordinary
  silence phrased in ways I had not imagined — the same keyword-search failure this study already
  caught in a coder, committed by me in a pattern list. Extended, re-run: **70.4% vendor silence,
  7 instrument gaps, 1 access failure, 147 still needing a human.**
- The 147 are not a backlog to be waved through. They go to hand or agent review before the freeze,
  and the count is published in the limitations either way.
- Among the 7 instrument gaps the tool now catches independently: the quarterly-billing family
  already sitting in the queue as A-011, where two blind coders each met a vendor billing every
  three months and each found the variable's closed value list has no such category. The tool
  reaching the coders' own conclusion from their prose is corroboration, not novelty, but it does
  confirm A-011 is a real instrument gap rather than two coders' shared confusion.

## D-028 · 2026-08-16 · 25 coded values carry a source but no evidence prose, and 2 of them publish

- Found while attributing unknowns. Across 4329 coded values, 67 carry no evidence prose. **42 of
  those are `computation_assumptions`**, the free-prose arithmetic note — an empty one means the
  coder had no arithmetic to record, which is benign and concerns the field already reported at
  alpha -0.001 and flagged for reclassification as documentation in wave 2.
- That leaves **25 real coded variables with no evidence prose**, concentrated in two records:
  `pass2/shortsfaceless` (18) and `pass1/undetectable-ai` (6).
- **Scoped accurately rather than alarmingly.** Every one of the 25 still cites a **source URL** —
  there are zero values with neither evidence nor source — and both records carry substantial coder
  notes (3176 and 6633 characters). This is "no per-variable justification prose", not "no
  documentation". A reader can follow the source; what they cannot see inline is the coder's reasoning.
- **Effect on the published dataset: two rows.** The publishing rule is the adjudicated row where
  one exists and the primary row otherwise. `undetectable-ai` has an adjudicated row that supersedes
  its pass-1 record; `shortsfaceless` publishes its pass-1 row per D-025, which is fully evidenced.
  Of the 76 publishing rows, exactly **2** carry a real coded variable without evidence prose —
  `udio` and `vidnoz`, one each — and both are in adjudication as this is written, so their
  adjudicated rows will supersede the gap. Re-check after they land.
- **Effect on reliability: none.** Agreement measures whether two coders wrote the same value, and
  the values are unchanged. It is disclosed anyway, because a reader assessing the reliability
  sample is entitled to know that one of its 26 records justified 18 of its values by source alone.
- Why the validator missed it: `validate_records.py` checks that all 37 variables are PRESENT, never
  that each carries the evidence the record template requires. Queued on the pre-freeze checklist
  rather than changed now, for the D-026 reason — adjudicators are mid-run and the validator is on
  their critical path.

## D-025 · 2026-08-16 · Two products need no adjudicated record, and the reason is stated rather than assumed

- `aiclicks` and `shortsfaceless` return **zero substantive disagreements**: their two blind coders
  wrote the same value for all 37 coded variables. Protocol §7.4 sends disagreements to a third
  pass, so there is nothing here for a third pass to do, and no adjudicated row is written.
- **Verified rather than trusted.** `disagreements.py` skips any variable that is absent on either
  side, so a report of "0 disagreements" could in principle mean "the variable was missing", not
  "the coders agreed". Checked directly: all 26 double-coded products carry all 37 coded variables
  in both passes, the intersection is complete, and 26 x 37 = 962 matches the reliability n exactly.
  These two zeros are real agreement.
- **What publishes for them.** The primary (pass 1) record, per the codebook's rule that the
  adjudicated row publishes where it exists and the primary row otherwise. Both records are
  identical on every coded variable, so the choice is immaterial for the data.
- One thing it is NOT immaterial for: both products disagree on `computation_assumptions`, the free
  prose field where a coder writes out their own arithmetic. Publishing the pass-1 record publishes
  the pass-1 coder's note. That is correct treatment for documentation rather than measurement — the
  field is already reported at alpha -0.001 and flagged for reclassification in wave 2 — but the
  dataset should say plainly that this field carries one coder's working, not a reconciled value.

## D-026 · 2026-08-16 · A latent trap in two tools, found while checking something else, fixed later on purpose

- `disagreements.py` skips a variable that is `None` on either side; `agreement.py` intersects the
  two records' key sets. Neither would report a variable that went missing from a record — the
  adjudication work-list would simply be shorter and the reliability n simply smaller, both silently.
  This is the same shape as D-020, where a tool read one storage format and dropped five units
  without saying so.
- **Inert on this corpus**, verified above: nothing is missing, so nothing is being dropped. No
  published figure is affected and none is being restated.
- **Not fixed at the moment of discovery, deliberately.** Three adjudicators were mid-run and both
  tools are on their critical path; breaking a tool three running agents depend on, to close a hole
  that is verified empty, is a bad trade. Queued on the pre-freeze checklist to be done when the
  conveyor is idle, where it can be verified against the whole corpus in one pass.
- Recorded because "we found it and chose when to fix it" and "we did not find it" look identical in
  a repository six months from now, and only one of them is true.

## D-023 · 2026-08-16 · A record cited an archive capture that never existed

- Found by the anomaly-ai adjudicator. A pass-2 record coded a free-tier allowance from a quoted
  figure and cited a dated Wayback URL for it. The adjudicator followed the URL: it **302-redirects
  to the other pass's earlier capture** (`x-archive-redirect-reason: found capture at 20260806…`),
  and the CDX index shows no distinct capture on the cited date ever existed. It then re-verified
  with a fresh capture and a live read: the quoted figure appears nowhere, on any date this study
  covers.
- Class: this is the fabrication family, not the misreading family. A misread takes a real page and
  gets it wrong. Here a citation pointed at a capture that does not exist and carried a figure the
  vendor never published. Two earlier instances in this study were summarising fetches inventing
  structure; this one invented provenance.
- Corrected in adjudication: the value resolved to the other pass's `none_quantified`, verified
  independently against the vendor's own embedded JSON on three dates.
- **Scope check run, and what it does NOT cover.** A local sweep compared every archive timestamp
  cited in every record against that record's own `collection_date`. One record cites a capture
  dated two days after its collection — rezi, which was coded in resume mode across two days, so
  archiving later is expected rather than suspect. No other record cites a future-dated capture.
  **But that check cannot see the anomaly-ai failure at all.** The cited URL there had a perfectly
  plausible date; what was wrong is that no capture existed at it. Detecting that requires querying
  the CDX index per URL, which is a network operation against the service D-012 records as
  rate-limiting us.
- So no clean bill is claimed. The corpus is clean on the one failure mode a local check can see,
  and unverified on the mode that actually occurred. **Archive-URL existence verification goes on
  the pre-freeze checklist** as a real pass, run when the window is closed and nothing competes for
  the service: for every record, confirm each cited capture resolves to a capture at the cited
  timestamp rather than redirecting to another.
- The 26 double-coded products get this scrutiny anyway through adjudication, which is how this one
  surfaced. The 50 products with only a pass-1 record do not, and that asymmetry is worth stating in
  the limitations: single-coded records in this study have had their sources read once, by the coder
  who chose them.

## D-022 · 2026-08-16 · Nothing checked a coded value against its own variable's allowed values

- Found by the adobe-firefly adjudicator, which noticed that `auto_renewal_default` carried `"yes"`
  — a value that variable's own table does not contain. Its enum is `on`, `off`,
  `no_recurring_billing`, `unknown`, `conflicting`.
- **Nothing in this study checked that.** `validate_records.py` verifies all 37 variables are
  PRESENT and enforces the two administrative enums added under D-015. No check ever compared a
  coded value against the codebook's allowed values for that variable, so a coder could write any
  token and every gate would pass.
- Scope, measured with a new tool that parses each variable's value table out of the codebook:
  **8 of 76 pass-1 records** carried `auto_renewal_default: "yes"`. No other variable in any pass
  had an out-of-enum value; 116 records checked.
- Substance: none. Every one of the eight records' evidence quotes the vendor saying the
  subscription "will automatically renew" — the coders read the vendor correctly and wrote the
  wrong token. Corrected `yes` → `on`, which is the D-015-addendum treatment (a value simply wrong
  against a frozen enum is repaired) rather than the D-010 treatment (a parser-invisible formatting
  difference is left alone and canonicalised at build).
- Effect on the reliability figures, reported because the correction moved them: alpha 0.807 →
  **0.811**, median per-variable 0.754 → **0.770**, variables reaching 0.800 16 → **17**. Small,
  and in the same direction as D-020 and D-021 — three separate defects, all of which had been
  recording vocabulary noise as coder disagreement.
- **`tools/check_value_enums.py`** now performs this check across every record. Two variables have
  no parseable value table (`computation_assumptions`, `free_plan_cap_value`); the tool REPORTS them
  as unchecked rather than skipping them silently, because a check that quietly covers less than it
  claims is the exact failure this study keeps finding in itself.
- The check is on the pre-freeze checklist as a required run and named in the adjudicator brief.
  D-020's dead guard is the reason that matters: a check nobody runs is worth the same as a check
  that does not exist.

## D-021 · 2026-08-15 · The comparison counted `10.0` against `10.00` as disagreement, and a headline claim came down with it

- Found while adjudicating aiva, whose single "disagreement" turned out to be one coder writing
  "3 minutes maximum" and the other "3 minutes max" — the same fact from the same sentence. That
  prompted a check of how the comparison treats non-categorical variables.
- The codebook types 31 of 37 variables as categorical, where exact string match is the right
  comparison, and 6 as money, integer or free text, where it is not. **Nineteen recorded
  disagreements across ten products were pure decimal formatting** — `10.0` against `10.00`,
  `96.00` against `96.0` — both coders having read the same figure while YAML serialised the float
  differently.
- Like D-020's shape defect, this is not an analytic choice. Two identical numbers are identical;
  counting them as disagreement was a bug in the comparison. `agreement.py` now canonicalises the
  four money and integer variables numerically before comparing, and leaves status values like
  `unknown` and `non_usd` as strings.
- Effect: raw 79.9% → **81.9%**, alpha 0.786 → **0.807**, median per-variable 0.710 → 0.754,
  variables reaching 0.800 14 → 16. The headline crosses the conventional threshold, so the write-up
  now prints the whole progression — 0.790 first published, 0.786 after the shape fix, 0.807 after
  this one — because a reader is entitled to see that the movement came from fixing comparisons and
  not from choosing a friendlier method.
- **A claim withdrawn, and it was mine and prominent.** The previous write-up reported
  `headline_price_usd` at α = 0.568 and `first_charge_amount_usd` at 0.492 and built on them: "a
  price two trained readers cannot reliably agree on IS the finding." Compared as numbers those
  variables are among the study's strongest — **0.920 (raw 24/26)** and **0.881 (raw 23/26)**. The
  claim is withdrawn rather than softened.
- What replaces it is sharper and survives the correction. The genuinely low-agreement variables are
  `unquantified_limit_clause` (0.249), `free_plan_cap_value` (0.285), `cost_per_output_computable`
  (0.309) and `usage_cap_quantified` (0.493). **What two careful readers cannot agree on is not what
  a product costs, but what you get for it** — whether a cap is quantified, what the free tier's
  limit really is, whether cost per output is computable at all, whether a discretionary fair-use
  clause qualifies an advertised allowance. Vendors are largely legible about price and largely
  illegible about entitlement.
- Standing: no coded value changed. This is a defect in how two records were compared, not in either
  record, and no adjudication decision made before the fix rests on it.
- Note for the adjudication phase: the work-list shrinks by 19 items, and `disagreements.py` should
  adopt the same canonicalisation so adjudicators are not sent to reconcile a trailing zero.
- **The retracted claim was still in circulation, and it was shaping the work.** The adjudicator
  agent definition, written before this deviation, told adjudicators that "two careful readers
  disagreed about a vendor's own published price roughly half the time". Three adjudications ran
  under that framing. It is now corrected to what the data supports: the passes agree about price
  far more often than not, and what they disagree about is what a buyer actually gets.
- Retracting a claim in the write-up is not the same as retracting it from the instructions the work
  runs on. A withdrawn finding that survives in a brief keeps steering the study toward the
  conclusion it was withdrawn for — quietly, and by people who have no way to know it was
  withdrawn. Checked every orchestrator file and the agent definitions afterwards; no other instance
  survives.

## D-020 · 2026-08-15 · The reliability tool broke the rule the pre-freeze checklist exists to enforce, and two commits carry another session's work

Two unrelated defects, both found by a parallel session auditing this session's output, both
verified here before being accepted.

### The tool read one storage shape

- `tools/agreement.py`'s `coded()` read `computation_assumptions` from `variables{}` only. Five
  records store it at top level (D-010: adobe-express, aiva, anomaly-ai, colossyan, copyleaks), so
  five units never entered the comparison and were dropped in silence.
- **This is the defect the pre-freeze checklist names as a hard requirement in my own words** —
  "the dataset build must read every record through a YAML parser, never by text matching", written
  after D-010 and reinforced with a worked example. I then wrote the tool that produces this study's
  headline reliability number and had it read one shape.
- Effect on the published figures: 957 units → **962**; raw 80.4% → **79.9%**; alpha 0.790 →
  **0.786**; tiers 0.790/0.773/0.788 → **0.786/0.770/0.788**.
- **One sentence in `reliability-result.md` became false**, not merely imprecise: it said "the
  never-exposed group is not the highest". With the dropped units restored, tier C at 0.788 IS the
  highest of the three. Corrected in place with the superseded claim shown, because the conclusion
  it supported — exposure did not detectably inflate reliability — survives and is now better
  supported, and deleting a wrong sentence that happened to argue against my own interests would be
  the worst possible edit.
- Fixed: `coded()` now falls back to the top level for any name in the validator's canonical `CODED`
  list, importing that list rather than restating it so the two tools cannot drift apart. A no-op
  placeholder loop left in the first version was also removed — harmless, but it sat in a tool that
  produces a published number.

### The pooled alpha flatters, and the per-variable table is better evidence

- Pooling 37 heterogeneous variables into one coincidence matrix raises expected disagreement
  (0.938 pooled against ~0.620 mean per-variable) and, since α = 1 − Do/De, pushes alpha up. The
  formula was verified correct by independent recomputation; the population was the problem.
- **Median per-variable alpha is 0.710, and only 14 of 37 variables reach 0.800.**
- This is now reported beside the pooled figure because it strengthens the study rather than
  weakening it: `headline_price_usd` at α = 0.568 supports "a price two trained readers cannot
  reliably agree on is the finding" far better than a pooled 0.786 does.

### Two commits carry another session's work

- `2a49d0e` ("PASS 2 COMPLETE — 26/26") also contains 19 pass-1 record edits, `validate_records.py`
  +57, `deviations-log.md` +72 (the whole D-019 entry) and `pre-freeze-checklist.md` +26.
  `d7483de` ("Pass 2: undetectable-ai complete") also contains the validator's dead-code repair.
- Cause: a parallel session was repairing administrative fields in the same worktree while this
  session committed, and `git add -A` on the study directory took everything staged — **the exact
  failure this session had diagnosed for its own coders days earlier and fixed by requiring scoped
  commits. The rule was written for the agents and not applied to the orchestrator.**
- `2a49d0e`'s message asserts both passes are closed while the commit carries 19 pass-1 data
  corrections, which is self-contradictory on its face. D-017 established that this repository's
  history is part of the audit trail, so a reader tracing when those records changed will find them
  inside a pass-2 completion commit.
- **Recorded as an erratum rather than repaired by rewriting history.** Published history is not
  rewritten without the owner, and a labelled inaccuracy in an audit trail is worth more than a
  tidy one that has been edited. What `2a49d0e` and `d7483de` actually contain is stated here, and
  D-019 in this same log describes the administrative work itself.
- Prevention: the orchestrator's own commits are scoped from here, the same rule the coders follow.

### D-020 addendum · 2026-08-16 · an adjudication brief quoted a stale count from memory

- The aragon-ai adjudicator reported that its brief said eleven substantive disagreements while
  `disagreements.py` and an independent 37-field diff both find nine. It was right. I wrote
  "eleven" from a `--counts` run taken BEFORE D-021's numeric canonicalisation, which removed
  nineteen formatting artifacts across the corpus and changed several per-product counts.
- Two of the variables I had counted — `refund_policy_exists` and `cancellation_self_serve` — are
  `conflicting` on that product but AGREED between the passes. A value can be `conflicting` because
  the vendor's own sources clash and still be a perfect agreement between coders; those are not
  disputes and never belonged in an adjudication count.
- Same class as D-015: a figure typed from memory instead of derived from the instrument, in a brief
  the recipient then has to reconcile. Harmless here because the adjudicator checked rather than
  trusted — which is the second time a brief error in this study has been caught by its recipient
  rather than by me.
- Practice from here: every adjudication brief reads its count from `tools/disagreements.py` at the
  moment of writing. Nothing about a product's dispute set is quoted from an earlier run.

### D-020 second instance · 2026-08-16 · I repeated the bare-commit defect after documenting it

- The undetectable-ai adjudicator reported that my commit `f59e918`, titled "Adjudication:
  elevenlabs done", contains its 535-line record. Verified: it does.
- Cause, and it is not a new one. I ran `git add <scoped path> && git commit`. The ADD was scoped;
  the COMMIT was bare, and a bare commit takes the whole index including whatever a concurrent agent
  staged a second earlier. D-020 diagnosed exactly this, and the fix I wrote then — `git commit --
  <your own paths>` — went into the agent definition and the coder digest and into every brief since.
  It did not go into my own hands.
- **That is the failure worth recording, more than the commit itself.** This is the second time in
  this study that I have written a rule for the agents and not applied it to the orchestrator, and
  the first time was this same rule. A control that its author is exempt from is not a control.
- Both records verified intact afterwards: 37/37 coded, validator clean on each, working tree clean.
  The damage is again a provenance smudge — one commit's message names a product whose file it did
  not intend to carry — and again it is recorded rather than repaired, because published history is
  not rewritten to look tidier than it was.
- Practice, this time actually applied: every orchestrator commit uses `git commit -- <paths>`. The
  next occurrence of this entry will mean the practice failed again, and that is the point of
  writing the sentence.

## D-018 · 2026-08-14 · Some `unknown` values may record our access rather than the vendor's silence

- What happened: the jobscan pass-2 coder could not read the vendor's general Terms of Service in
  English. The document rendered in Turkish throughout the session and five independent methods —
  WebFetch, two browser navigations, a web.archive.org capture and an archive.ph attempt — all
  failed to produce an English text. Four contractual variables are `unknown` as a result, with a
  full written account of every attempt kept in the record's sources directory.
- Why this is a validity problem and not just an inconvenience: `unknown` in this instrument means
  **no official document states it**. That is a claim about the vendor. D-005 settled the principle
  in the opposite direction — "our fetcher could not see it" is not a finding, "a visitor cannot
  find it" is — and here the document exists, says something, and we could not read it. Coded as
  `unknown`, those four variables will read in the published dataset as vendor silence.
- **What was measured, stated as measured.** A scan of all completed records for unknowns
  co-occurring with access-failure language in the coder's own notes returns **23 records — 20 of
  76 in pass 1, 3 of 16 so far in pass 2**. That is co-occurrence, NOT causation: most of those
  notes document a barrier on one source while the unknowns come from genuine silence elsewhere.
  The number that says "this unknown exists because we could not read the document" is not knowable
  from a keyword scan and I am not going to imply otherwise. What the scan establishes is the size
  of the population that needs reading, not the size of the problem.
- Access barriers seen across those records, for the paper's methods section: Cloudflare
  interstitials served to fetchers and to archive.org's crawler alike, blanket 403s to automated
  requests, help centres that render nothing to extraction, prices drawn as unextractable glyphs,
  and now a contract served in the reader's inferred language with no reachable English version.
- **Three categories, not two — corrected 2026-08-16 by an adjudicator.** This entry framed the
  attribution as a binary: an `unknown` is either vendor silence or our access failure. The jobscan
  adjudicator found a third that belongs to neither. Two of that record's unknowns are the quarterly
  billing-cadence gap (A-011 family): the vendor publishes its cadence in full, we could read it
  perfectly, and the codebook's enum has no value for it. That is an INSTRUMENT gap, and folding it
  into "vendor silence" would blame a vendor for our own value list. The per-record attribution now
  sorts every `unknown` into vendor silence, access failure, or instrument gap, and the paper
  reports all three separately.
- Also worth recording: adjudication can CLOSE an access barrier. That same record's four
  access-limited unknowns were resolved when the adjudicator read the English document the other
  pass had obtained — three turned out to be genuine vendor silence, confirmed by a completed read,
  and one resolved off `unknown` entirely. An access-limited `unknown` is provisional in a way a
  silence-based one is not.
- Treatment, given the instrument is frozen: the value stays `unknown` — inventing a distinct code
  mid-wave would breach the freeze — and the DETERMINATION goes on the pre-freeze checklist as a
  per-record read. Every record whose notes document an access barrier is read by hand at
  adjudication, each unknown attributed to either vendor silence or our access, and the two are
  reported separately. Wave 2's codebook needs a distinct value for "document exists and could not
  be read", because conflating it with silence understates vendors that publish and overstates the
  study's central quantity.
- This is the same root as D-003, D-007 and interim signal S-3, reaching a third surface. Our
  network location has already been shown to change the currency a page shows and the product
  lineup it offers; here it changes the LANGUAGE of a governing contract. The limitations register's
  sentence about collection running from a single network location is doing far more work than it
  looks like, and the paper should say what it actually covers.

## D-017 · 2026-08-14 · The repository's own history exposes every product in the reliability sample

- What happened: the ismybrandinai pass-2 coder mentioned, in passing, that it had observed a
  sibling commit in the shared repository log while working. What it saw was a process fact — a
  note about an enum bug — not a coded value. But it prompted the obvious question, and the
  measurement is worse than the incident: **all 26 of the pre-registered double-coded products are
  named in commit messages together with a coded value. 26 of 26.**
- The commit messages are detailed by design. Each one explains what a record found and why it
  matters, with prices, conflict shapes and named products, because that is how this study's
  reasoning has been kept auditable. Every one of those messages sits in the history of the
  repository that pass-2 coders must commit their own work into.
- **This is D-014 and D-016 a third time, and unlike those two it cannot be fixed structurally.**
  The required-reading list could be replaced with a safe digest. The orchestrator's files could be
  moved into their own directory. History cannot be moved out of the repository a coder has to
  commit to, and stripping the audit trail from commit messages to protect blindness would trade a
  real asset for a partial defence.
- What is actually done about it:
  1. The agent definition now states the narrow truth: a coder needs `git add` and `git commit` and
     nothing else, and must never run `git log`, `git show`, `git diff` or `git blame`. It says
     plainly that this one rests on the coder rather than on structure.
  2. The blindness attestation gains a second clause — **"I did not read repository history"** —
     alongside the existing statement about other products' records.
  3. Orchestrator commit messages from here on describe findings by reference (record path,
     deviation id) rather than quoting figures for double-coded products. That limits future
     exposure without gutting the trail; it does nothing for the 26 already written.
- **What cannot be claimed, stated plainly.** The fifteen pass-2 records coded before this rule
  existed carry attestations about records, not about history. I cannot retroactively establish that
  none of those coders read a commit message, and I will not assert it. One of them disclosed that
  it did read one. The paper says exactly this: for pass-2 records coded before 2026-08-14, blindness
  from the repository's history is not evidenced, only unobserved.
- Consequence for the reliability estimate, which is the uncomfortable part: D-014 already narrowed
  the "never exposed" control group to five products. This deviation makes even that group's
  cleanliness conditional on coders not having read history. **The paper reports Krippendorff's
  alpha with that stated, and does not present any subgroup as a clean control.** An alpha computed
  under a blindness regime this study cannot fully evidence is still worth reporting — reliability
  estimates are routinely imperfect — but it must be reported for what it is.

### D-017 first test · 2026-08-14 · the rule was breached, disclosed, and was missing an alternative

- The google-veo pass-2 coder — the first to work under this rule — ran a narrow `git log --oneline`
  and disclosed it in its attestation, stating it saw its own commit subjects and no other product's
  content, rather than signing a clean attestation it could not honestly sign.
- Treated as precedent requires: the record is RETAINED and joins the for-cause set, its agreement
  reported separately from the pre-registered sample. Fifth blindness disclosure in this study,
  fifth voluntary one.
- **But the rule was at fault as well as the coder.** I mandated self-committing after every
  variable group and index.lock retries, which gives a coder a genuine reason to want confirmation
  that its commits landed — and then forbade every command that would confirm it, offering nothing
  in its place. A prohibition with no permitted alternative for a legitimate need is a prohibition
  that invites careful people to breach it narrowly. That is the D-004 lesson again: an attestation
  makes a breach visible, it does not remove the reason for it.
- Fix, in both the agent definition and the coder digest: the same sentence now names what to do
  instead — `git commit` already reports success, and `git status --porcelain -- <your own paths>`
  confirms a clean tree without displaying a single commit message. The need is met, so the rule can
  hold.

**Second test, 2026-08-14, and a deliberate non-escalation.** The sapling pass-2 coder disclosed a
single accidental `git diff --stat --cached`, run while diagnosing a "nothing to commit" race with
a concurrent collector. **Its output was empty** — nothing was staged at that moment — so no history
and no other record's content was displayed. Zero information transferred, provably.

That record is NOT added to the for-cause set, and the reasoning is recorded rather than assumed
because a decision not to escalate should be as auditable as a decision to escalate. The for-cause
set exists to mark records whose independence may have been compromised. Adding one where the
compromise is provably empty would be ritual, and it would dilute the set's meaning for the records
that actually need it — google-veo, whose coder did see commit subjects, belongs there; this one
does not. The contact is recorded here and in the record's own `coder_note` either way, so a reader
who disagrees with my line can draw it differently.

Worth separating from the blindness question: the "nothing to commit" race is real, and it is a
consequence of running several collectors in one worktree. It is an operational cost of the
concurrency choice, alongside the archive rate-limiting in D-012, and belongs in the methods
section as such.

**Third instance, and this one my instruction's fault outright.** The recraft pass-2 coder disclosed
that its first commit swept in five files belonging to a different product's pass-2 record — staged
by a concurrent collector in the same worktree a moment before it ran `git commit`. It saw only
filenames in its own commit output, never content, and scoped every later commit itself.

I told coders "never `git add -A`" and stopped there. A bare `git commit` takes whatever is in the
shared index regardless of who staged it, so the instruction forbade the obvious way to hit the
problem and left the non-obvious one open. Both rule files now require `git commit -- <your own
paths>`, and the checkpoint example is scoped too.

Both affected records were verified intact afterwards — 37/37 coded, `status: complete`, validator
clean on each. The only damage is a provenance smudge in the history: one commit's message names a
product whose files it did not intend to carry. Recorded rather than rewritten, because rewriting
history to tidy an audit trail is a worse trade than living with a labelled smudge.

That makes three documented operational costs of running collectors concurrently in one worktree:
archive rate-limiting (D-012), the nothing-to-commit race, and cross-product commit capture. The
concurrency bought throughput and the methods section should price it honestly.

## D-016 · 2026-08-14 · A coder's own grep reached the orchestrator's files, so the files moved

- What happened: the humanizemy pass-2 coder searched the study directory's `*.md` files for
  guidance on how to handle a bundled product. The glob swept in `adjudication-queue.md`, whose
  entry A-010 concerns this exact product and quotes pass-1 entry-tier figures for it, plus one
  line of `interim-signals.md`. The coder disclosed it in full, in detail, and re-derived every
  value independently from its own rendered read of the live site.
- **D-014's shape, one layer down.** That deviation fixed the case where required reading handed
  over the answer. This is the case where forbidden reading sat in the same folder and an ordinary
  search found it. The rule said "do not open these files"; nothing stopped a glob from opening them
  anyway. A prohibition that depends on a coder never using a wildcard is not a control.
- Scope, measured across the study directory before the fix: six files exposed coded values to
  anything globbing `*.md` — `collection-status.md` (26 double-coded products named, 12 with
  values), `deviations-log.md`, `interim-signals.md`, and the three sweep reports. Two more named
  products without values. `double-coded-selection.csv` additionally revealed reliability-sample
  membership, and the frozen frame still carried `review_url`.
- Structural fix, replacing the rule rather than restating it: every orchestrator-only artifact moved
  into **`orchestrator/`** — the deviations log, adjudication queue, collection tracker, the three
  sweep reports, the pre-freeze checklist, the sampling selection and the frozen frame. What remains
  in the study directory is exactly a coder's instrument: dossier, protocol, sampling rules,
  codebook, `deviations-for-coders.md`, the record template, `frame-for-pass2.csv`, `tools/`, and
  the records. A glob over the study directory now cannot reach anything it should not.
- The agent definition now also names the search behaviour itself, because the file move handles the
  directory but not the habit: do not glob across the study directory, open files by exact path, and
  if you are hunting for a rule it is in `deviations-for-coders.md` — search that file.
- Remedy for this record: humanizemy's pass-2 record is RETAINED and joins the for-cause set, its
  agreement reported separately from the pre-registered sample, as with every prior breach.
- **Fourth blindness disclosure, fourth voluntary one.** Every breach in this study has been reported
  by the agent that committed it, including two where the fault was the orchestrator's. That rate is
  reported alongside the breach count, because a study that only counted breaches would look worse
  the more honest its coders were.

## D-015 · 2026-08-14 · Three pass-2 assignments named the wrong vendor, product or category (orchestrator defect)

- What happened: the aiclicks pass-2 coder reported that its assignment's `vendor_home_url` did not
  resolve and that its `product_name` and `category` disagreed with the frame. It coded from the
  frame instead and flagged the correction. An audit of all ten pass-2 assignments issued to that
  point found **three of ten disagreed with the frozen frame**:
  - `aiclicks` — wrong on all three: name, URL (`aiclicks.app` against the frame's `aiclicks.io`)
    and category (`AI SEO` against `AI bot checker`).
  - `anomaly-ai` — wrong URL: I wrote `anomaly.io`, the frame says `findanomaly.ai`. **Those are
    different companies.** A coder working from my URL would have coded an entirely different
    product into this study's dataset under Anomaly AI's `product_id`.
  - `aragon-ai` — category wording (`AI headshot generator` against `AI headshot`). Cosmetic, but
    it is the study's stratification value and the record must match the frame exactly to join it.
- Cause, and it is not subtle: I typed the assignment fields from memory instead of reading them
  out of the frame. Ten assignments, thirty fields, four wrong.
- Why it did not become a contaminated record: the briefs also instruct coders to use
  `frame-for-pass2.csv` and to locate the official domain themselves if the given URL fails. The
  aiclicks coder did exactly that. **That is luck dressed as a control** — the instruction was
  written to handle vendor-side link rot, not to catch the orchestrator's typing, and it only
  worked because that particular URL failed loudly. `anomaly.io` resolves fine; it just belongs to
  someone else, and nothing in the brief would have alerted a coder to that.
- Immediate action: both running coders were messaged. anomaly-ai was told to stop, discard anything
  read from the wrong domain, re-target from the frame, and record the defect in `coder_note`.
  aragon-ai was given the category correction. Neither correction carries any pass-1 information, so
  the blinding is intact.
- Real fix, aimed at the cause rather than the instance: **`tools/brief_fields.py`** generates the
  assignment block directly from `frame-for-pass2.csv` and never invents a value.
  `--all-pending` emits blocks for every outstanding product in alphabetical order. Assignment
  fields are no longer typed.
- Disclosure: the paper reports that three of ten early pass-2 assignments carried a wrong
  administrative field, that one named a different company, how it was caught, and that assignment
  generation was mechanised afterwards. It also reports the uncomfortable part — the catch depended
  on a coder checking the frame against its own brief, which no rule required it to do.

### D-015 addendum · 2026-08-14 · a fourth typed field was wrong in every brief, and nothing checked it

- The autoshorts-ai pass-2 coder reported that its assignment said `coder_role: secondary` while the
  codebook's enum is `primary | second | adjudicated`. It coded `second` and logged the mismatch.
- I had written `secondary` into every pass-2 brief. **Eleven of sixteen pass-2 records carried the
  invalid value**; the five that did not were coded by agents that checked the template rather than
  trusting the brief. The validator did not check the field at all.
- Why this is worse than a typo: the codebook selects the published dataset BY this field — "the
  published dataset carries the `adjudicated` row where one exists and the `primary` row otherwise",
  one row per product per role. A build filtering for `second` would have silently missed eleven of
  the sixteen second codings. Same harm class as D-006: one value, two spellings, a count that
  splits without warning.
- **Corrected in the records, and the contrast with `julius-ai` is deliberate.** Under D-010 I
  declined to repair a record whose `archive_status` was merely QUOTED where others were bare,
  because under a parser both are the identical string and no coded meaning was at risk. Here the
  value is simply wrong against a frozen enum — `secondary` is not `second` to any consumer, parser
  or otherwise. Repairing an unambiguous wrong value in a single administrative scalar is not the
  same act as rewriting a record's prose for a parser-invisible difference, and treating them alike
  would be consistency for its own sake.
- Prevention, both halves: `brief_fields.py` now emits `coder_role: second` with the enum spelled
  out beside it, and `validate_records.py` gained an administrative-enum guard so an out-of-enum
  role fails validation rather than passing silently.
- That is four wrong fields across the pass-2 assignments — vendor URL, product name, category, and
  now role — every one of them because I typed what the record needed instead of deriving it from
  the instrument. Every one was caught by a coder rather than by a check. The generator exists so
  the next wave does not rely on that.

## D-014 · 2026-08-14 · The required reading told pass-2 coders what pass 1 found (orchestrator defect, MATERIAL)

- What happened: the krea-ai pass-2 coder disclosed, unprompted, that `deviations-log.md` — which
  the agent definition listed as required reading — names its assigned product and quotes a pass-1
  coded value. It re-derived the figure independently from a fresh session and documented the whole
  chain, but the exposure is real and it is structural, not a slip.
- **This is my defect, not a coder's.** I wrote the log to name products and quote their values,
  which is exactly what an audit trail should do, and then I put that audit trail on the reading
  list for the coders whose independence the study's reliability estimate depends on. Every previous
  blindness deviation (D-001, D-004, D-011) was a coder reaching for something it should not have.
  This one was the instructions handing it over.
- Scope, measured rather than estimated: **13 of the 26 pre-registered double-coded products are
  named in the required reading alongside a coded value or status** — 10web, aiva, colossyan,
  copyleaks, elevenlabs, humanizemy, jobscan, krea-ai, nicepage, pika, sapling, teal,
  undetectable-ai. Half the reliability sample was exposed by design. The other 13 are clean:
  adobe-express, adobe-firefly, aiclicks, anomaly-ai, aragon-ai, autoshorts-ai, beautiful-ai,
  google-veo, ismybrandinai, recraft, shortsfaceless, udio, vidnoz.
- Why it matters more than the earlier breaches: a coder who has seen a sibling record's FORMATTING
  can still reach its values independently. A coder who has been shown the value itself cannot.
  Agreement produced that way is not evidence of a reliable instrument; it is evidence that we told
  someone the answer. Left uncorrected it would have inflated Krippendorff's alpha on half the
  sample, and alpha is the number that licenses every other claim in the paper.
- Remedy:
  1. **`deviations-for-coders.md`** now carries every binding rule the log created and none of the
     evidence — no product names, no coded values. The agent definition points at it, and carries an
     explicit instruction never to open the full log.
  2. The four pass-2 records already produced under the old reading list — 10web, elevenlabs,
     copyleaks, krea-ai, all four of them on the exposed list — are moved to
     `records/pass2-contaminated/` rather than deleted. They are retained, named, and reported.
  3. All four are **re-coded from scratch by fresh coders** under the corrected reading list. The
     pre-registered set stays at 26 rather than being quietly reduced or substituted.
  4. The nine exposed products not yet pass-2 coded simply get the corrected list.
- What is NOT claimed: that the re-coded records are perfectly clean. A fresh agent instance has no
  memory of the contaminated run, and the corrected reading list contains no values, so the exposure
  route is closed — but the paper reports which 13 products were exposed, which 4 were re-coded, and
  that alpha can be computed both on all 26 and on the 13 never-exposed products as a robustness
  check. If those two figures diverge, that is a finding about this study's own method and it gets
  published as one.
- Credit where it belongs: found by a coder that read its instructions, noticed they contradicted
  the blindness rule it had also been given, and said so instead of quietly proceeding. Three of the
  four blindness deviations in this study were self-disclosed by agents; this one was disclosed by
  an agent about the orchestrator.

### D-014 amended · 2026-08-14 · a second session audited the fix and found three things wrong with it

A second Claude session, started by the owner on the same task and working read-only, audited this
remedy. Its findings hold up under my own re-scan and are adopted.

- **A FIFTH record was contaminated and I had missed it.** adobe-express's pass-2 run was spawned at
  18:24 and my corrected agent definition landed at 18:53; agent instructions load at spawn, so it
  ran its entire assignment under the old reading list. Its own checkpoints straddle the fix — 18:50
  before, 18:57 after — which is how it was caught. Its blindness attestation reads clean and could
  not have caught this, which was the krea-ai coder's original point: `deviations-log.md` is not
  "pass-1 material" under the literal wording, so a coder can attest truthfully having read it.
  Quarantined with the other four and re-coded. **Five records, not four.**
- **My exposure scan was wrong in both directions.** It searched `interim-signals.md` as well as the
  deviations log, but interim-signals is orchestrator-only and appears in no coder's reading list —
  so `undetectable-ai`, whose only hit was there, was never exposed at all. And its context regex was
  loose enough to count almost any nearby word as a disclosure. The corrected scan excises D-014's
  own text, which postdates every pass-2 launch and names all products by design, and tests for
  actual figures.
- **The criterion has to be stated, and the answer is three tiers rather than two.** "Named alongside
  a coded value or status" is too vague to survive a referee, and under it 10web and elevenlabs sat
  on the exposed list while adobe-express sat on the clean one for an identical class of mention.
  Restated:
  - **Tier A — a coded value, or a stated relationship between coded values, is disclosed (7):**
    aiva, colossyan, copyleaks, jobscan, krea-ai, nicepage, pika. colossyan and copyleaks are here
    because D-009's provenance list states their first charge is "exactly twelve times the headline",
    which is a value relationship even though no figure is printed. The auditing session placed those
    two in this tier; my first scan had them lower, and it was wrong.
  - **Tier B — named, but only pass-1 status or process (14):** 10web, adobe-express, adobe-firefly,
    aiclicks, anomaly-ai, aragon-ai, autoshorts-ai, beautiful-ai, elevenlabs, google-veo, humanizemy,
    ismybrandinai, sapling, teal. Being listed as re-read-and-confirmed, or as storing a field in a
    particular shape, tells a coder the product was examined; it does not tell them any value.
  - **Tier C — never named in anything a coder reads (5):** recraft, shortsfaceless, udio,
    undetectable-ai, vidnoz.
- **The robustness check must be described honestly rather than flattered.** I had implied alpha
  could be computed on 13 never-exposed products as a clean control. There are five. Five products
  cannot carry a robustness claim on their own, and the paper will say exactly that rather than
  presenting a tidy-looking figure. Alpha is reported three ways — all 26, the 19 outside tier A,
  and tier C with its n printed beside it — and the reader is told which is load-bearing.
- **The same defect had a second instance I had not looked for.** `frame-frozen-2026-08-04.csv` is
  required reading and carries `review_url`, a direct link to our own published review of the
  product, plus an `in_double_coded_set` flag. Protocol §7.3 says a second coder must not see our
  review; the rule forbade opening it while the required reading handed over the pointer — the exact
  shape of D-014 itself. **`frame-for-pass2.csv`** now ships identity and administrative columns
  only, and the agent definition directs pass-2 coders to it.
- On remedy scope: the five quarantined records span tiers A and B, and all five are re-coded rather
  than only the tier-A one. Tier-B exposure is weak, but one agent run is cheap insurance against an
  argument I would rather not have to make in a methods section.
- Recorded because it belongs in the paper: this fix was audited by an independent session, and the
  audit found a missed record, a false positive, and an overstated control group. The reliability
  section reports that too. A remedy that has itself been checked is worth more than one that has
  not, and the checking is part of the method rather than an embarrassment to it.

## D-013 · 2026-08-13 · The orchestrator is not blind, and pass-2 briefs had to be written around that

- The situation, stated plainly because a referee will ask it: the same orchestrator that processed
  every pass-1 record also writes the pass-2 assignments. The coders are blind to each other; the
  person handing out the work is not. There is no way around this in a one-human operation, so the
  question is how it was controlled.
- What was done: pass-2 briefs carry **no product knowledge at all**. Protocol §7.3 allows the
  second coder the product name and the vendor's home URL, and that is exactly what the briefs
  contain, plus two administrative fields (`paid_submission`, `product_status`) that come from the
  frozen frame rather than from any pass-1 finding. Every pass-1 brief's category guidance — which
  variables tend to be thin here, what a sibling product turned out to do, which vendor pattern to
  watch for — is absent. Those hints raised pass-1 quality; in pass 2 they would raise AGREEMENT,
  which is the one thing this pass is supposed to measure rather than manufacture.
- The pass-1 `-sources/` directories are off limits to pass-2 coders for the same reason. A sources
  folder is the first coder's document selection; handing it over would make the passes agree
  because they read the same pages, and would also void §7.3's second purpose — testing whether the
  documents are findable at all.
- **No per-product agreement is computed until all 26 pass-2 records are complete.** Comparing as
  they land would let a low early agreement figure influence how later briefs are written, which is
  precisely the contamination route that matters when one party sees both sides. Protocol §7.4 step
  1 already requires comparison "after both passes close"; this records why that ordering is not
  merely administrative.
- What remains uncontrolled, and is therefore disclosed rather than claimed away: the orchestrator
  wrote the briefs' shared instrument-operation section knowing what pass 1 had struggled with.
  That section carries no product-specific content, but it is not nothing, and the paper says so.

### D-013 corrected · 2026-08-14 · two claims in this entry were inaccurate, both found by an independent audit

The same second session audited the pass-2 briefs themselves — the one surface the orchestrator
cannot check, since it wrote them. Its substantive finding confirms this entry's central claim:
**no pass-2 brief carries pass-1 product knowledge.** Zero money figures, zero mentions of any
product other than the brief's own target, and every line unique to a single brief is either a
generic instrument rule or a statement about our own run failures ("a previous run was killed"),
never about anything pass 1 found. The `first_charge_amount_usd` rule appears in every brief
including the earliest, so it is not a hint aimed at the products where that pattern turned up.

Two claims made above were nevertheless wrong, and both are corrected here rather than left to be
discovered by a referee diffing an appendix.

- **"Identical across all pass-2 assignments" is literally false.** With product tokens masked, the
  briefs vary in wording: the rule set was progressively compressed as it settled, and **two
  operational rules were genuinely added mid-pass** — an explicit login prohibition ("if a page
  requires login, do NOT open it, §6.3"), added after a coder met a login redirect and disclosed it,
  and a per-product survivability line. Later coders therefore operated a slightly better-specified
  instrument than earlier ones. That is not contamination, but it is real, and the accurate claim is
  narrower: the briefs are **materially identical in substance** — the same rule set, progressively
  compressed, with two operational rules added mid-pass and named here — and contain no
  product-specific content.
  - It happens that the asymmetry falls entirely on records being discarded anyway: the five coders
    who worked before the login rule existed are the five quarantined under D-014, and their
    re-codes read `deviations-for-coders.md`, which carries it. Stated because it is true, not as a
    defence — the claim was still wrong when it was made.
  - Structural fix so the drift cannot recur: pass-2 briefs now carry the six frame fields and a
    pointer to `deviations-for-coders.md`, rather than restating instrument rules inline. One
    canonical text, versioned in the repository, instead of a rule set retyped thirteen times.
- **The enumeration of what a brief contains was under-inclusive by two.** This entry said the
  briefs carry the product name and vendor home URL "plus two administrative fields
  (`paid_submission`, `product_status`)". They also carry **`product_id`** and **`category`** — four
  administrative fields, not two, all four frame-sourced and none of them a coded variable
  (`category` is a top-level frame field in the record template, and is the study's stratification
  variable). Worth saying plainly rather than only correcting the count: **protocol §7.3's literal
  permission is two things, the product name and the home URL, and the briefs give four.** The two
  extra are administrative and disclose nothing pass 1 found, but `category` in particular could in
  principle prime a coder toward category-typical reasoning — a coder told "AI detector" may reach
  more readily for the score-is-not-an-artifact treatment. It is supplied because the record's
  category must match the frame for the dataset to join, not because it helps the coder, and the
  paper states the four fields and this reservation rather than the two.
- **Amended the same day, because one of the two uncontrolled factors did not have to stay that
  way.** The first four pass-2 launches — 10web, elevenlabs, copyleaks, krea-ai — were ordered by
  the orchestrator's judgment. From the fifth onward the remaining products are processed in strict
  ALPHABETICAL order, a rule fixed here in advance that removes the orchestrator's discretion from
  the sequence entirely. Batch order is unlikely to matter much, but "unlikely to matter" is a
  worse answer to a referee than "determined by a published rule", and the fix cost nothing. The
  four hand-ordered products are named here so a reader can see exactly which ones predate the rule.

## D-011 · 2026-08-12 · A third blindness breach, for the same innocent reason as the first two

- What happened: the squarespace pass-1 coder disclosed in `coder_note` that it briefly opened
  `nicepage.yaml` for tooling context before beginning to code. Self-disclosed, unprompted, exactly
  as D-001's and D-004's coders did.
- Remedy, unchanged from precedent: the record is RETAINED and squarespace joins faceless-so and
  gptzero in the for-cause blind pass-2 set, reported separately from the pre-registered
  double-coded sample so the reliability estimate is not contaminated by a re-read chosen because
  something went wrong.
- **The pattern is the finding.** All three breaches were the same act for the same reason: a coder
  wanting to see what a finished record looks like. D-004's fix — `record-template.yaml`, so no
  coder needs a sibling record for the schema — was correct but incomplete, because this coder was
  not after the schema. It wanted to see the shape of a real, filled-in one, and the prohibition
  did not say that was covered.
- Real fix, again aimed at the reason rather than the rule: the agent definition now lists the
  files a collector MAY read — the instrument documents, the frame, the template, `tools/`, and its
  own record and sources — and states explicitly that another record is off limits for its
  formatting and for an example of running a tool, not only for its values. It also tells coders
  what to do instead: write the uncertainty into `coder_note` and code what the rules support,
  because an imperfectly formatted field is cosmetic and the orchestrator can fix it, while a coder
  who has seen a sibling's values cannot un-see them.
- The disclosures themselves are working and are worth saying so plainly: three for three, every
  coder who breached told us. A quiet breach would have left a contaminated record indistinguishable
  from a clean one. The paper reports the breach count, the disclosure rate, and the for-cause set.

## D-010 · 2026-08-12 · One variable is stored in three different shapes, and the validator was told to accept the drift

- What happened: `computation_assumptions` is defined by the record template as a coded variable —
  a `{value, source, evidence}` map inside `variables:`. Across the 55 completed pass-1 records it
  is actually stored four different ways: 39 conform; 8 carry the map AND a second top-level prose
  string (10web, aragon-ai, d-id, elevenlabs, faceless-so, gamma, invideo-ai, ismybrandinai); 6
  carry only a top-level string (adobe-express, aiva, anomaly-ai, brandcited, colossyan, copyleaks);
  and 2 put a bare string inside `variables:` instead of a map (aiclicks, humbot). Sixteen of 55
  records deviate.
- How it stayed invisible: `tools/validate_records.py` carries the line
  `TOPLEVEL_OK = {"computation_assumptions"}  # template drift: accepted at top level`. The drift
  was noticed at some point and the validator was widened to accept it rather than the records
  being brought into line — so every record passed validation and nothing surfaced. Same family as
  D-006, where a boolean coercion split one value into two spellings and every record still
  validated.
- Why it matters: a dataset build that reads `variables.computation_assumptions` — the shape the
  template defines and the shape 39 records use — silently drops the field for the 6 top-level-only
  records and mis-reads the 2 bare-string ones. It also loses the extra prose in the 8 that carry
  both. The field is the record's account of its own arithmetic, which is precisely what a reader
  checking a computed first charge needs. It was found while extending the price screen: four
  records flagged as "no computation recorded" turned out to have recorded it somewhere the tool
  could not see.
- **A failed repair, recorded because it happened.** The first attempt was a normalizer that moved
  the top-level block into `variables:` by line surgery. It matched more records than intended and
  produced invalid YAML in eight of them. The damage was caught immediately by a parse check, the
  records were restored from git, and all 57 parse cleanly — but the attempt should not have been
  run across the corpus before being proved on one file. The script was deleted rather than fixed.
- Decision: **the records are not mutated.** They are the primary artifact and they carry coder
  prose, evidence quotes and comments that line surgery puts at risk for no analytical gain. The
  canonicalisation belongs in the dataset build, which is a script whose output is derived and
  reproducible: it reads the field from every shape, writes one canonical column, and appends any
  second prose string to the record's notes column rather than discarding it. `check_price_arithmetic.py`
  already reads all shapes and its four false "missing provenance" flags cleared once it did.
- Standing: the instrument is untouched. No variable is redefined, no value changes, and no coded
  meaning is affected — this is a storage-shape defect, not a measurement one.
- Prevention: the validator's `TOPLEVEL_OK` exemption is to be removed once the build's
  canonicalisation is written and proved, so a future wave's records cannot drift the same way
  without failing. Until then it stays, with this entry naming it as a known exemption rather than
  an accepted convention.
- Disclosure: the published dataset's codebook states which shape the CSV column came from for each
  record, so a reader reconciling the CSV against the raw YAML is not surprised.
- **Re-counted at final N (2026-08-14), prompted by an independent audit.** The figures above were
  scoped to the 55 records complete when this entry was written, so they were true then and stale
  now. At N=76: 59 conform; 8 carry the map AND a top-level prose string; 7 carry only a top-level
  string; 2 put a bare string inside `variables:`. **17 of 76 deviate.**
- That is the more interesting number, because of what it is not. The count rose by one while the
  corpus grew by twenty-one — **29% (16/55) down to 22% (17/76)** — so only one record added after
  this deviation was opened repeated the defect. Correcting the template and the agent definition
  worked on new records; it just could not reach the ones already written. The paper reports both
  figures and that trajectory, since "the fix held for everything coded after it" is evidence about
  the remedy and not merely bookkeeping.
- Still open, and named again so it is not lost: the `TOPLEVEL_OK` exemption in
  `validate_records.py` comes out once the dataset build's canonicalisation is written and proved.
- One further text-level inconsistency, found by the same audit and deliberately NOT repaired:
  `julius-ai` stores `archive_status` quoted where 24 other records store it bare. Under a YAML
  parser both are the identical string — `local_copy_only` is not a special token the way `yes` is,
  so unlike D-006 no coded meaning is at risk. Repairing it would mean mutating a completed record
  for a difference that only a text-matching tool can see, which is exactly what this entry decided
  against. The durable answer is the guard rather than the edit: **the dataset build must read every
  record through a YAML parser and never by text matching**, and that requirement is now on the
  pre-freeze checklist.
- **And that guard has a worked example, produced accidentally inside this study's own audit trail
  within hours of the field being flagged.** The auditing session reported the D-012 split as
  45 / 24 / 6 = 75 against a corpus of 76. I corrected the arithmetic; the auditor then found the
  real cause, which was not arithmetic at all. Its bucketing matched `archive_status` as TEXT, so
  the quoted `julius-ai` value landed in a fourth bucket of its own and was silently dropped from
  the summary line. Reproduced here both ways:
  - through a YAML parser — `archived: 45, local_copy_only: 25, unset: 6` = 76, rate **32.9%**
  - through naive text matching — `archived: 45, local_copy_only: 24, "local_copy_only": 1,
    unset: 6`; a bucket keyed on the bare spelling reports **31.6%**
  The defect the auditor had just identified split the auditor's own count, in the same message, on
  the one field where it had said the harm was confined to text-matching tools. Nothing in the study
  turned on it — one record, 1.3 points, and the substantive claim is unaffected — but it converts
  the parser requirement from a precaution against a hypothetical into a rule with a demonstrated
  failure behind it. That is the strongest form the requirement could take, and it was free.
- Both directions of this failure mode are now on record and belong together in the reliability
  section: the auditor's first D-012 measurement scanned a WIDER surface than the claim and returned
  64%, and its bucketing then read a NARROWER set than the corpus and returned 31.6%. Same root —
  a measurement whose scope is not the claim's scope — approached from opposite sides.

## D-009 · 2026-08-10 · The two-representation price rule caught three misreads in four records, so the records coded before it need re-reading

- What happened: the "read a price twice, in two representations" rule was added this morning
  after the nicepage coder found a superscript-cents layout rendering `$6.75` as `$675` in both
  WebFetch output and `innerText`. In the four records coded since, it caught a misread in three:
  nicepage (a 100x magnitude error), pixlr (an annual figure read from a page whose default state
  is monthly — `$1.99` annual instead of `$2.49` monthly), and pika (a summarised fetch that
  reported the entry tier at `$28` with a duplicated tier row, where the true grid is free `$0`,
  Standard `$8`, Pro `$28`, Fancy `$76` — the entry tier was out by 3.5x).
- Why it forces a sweep: three catches in four records is not a comfortable rate, and every other
  completed record was coded WITHOUT a mandatory second read. We cannot tell from a record which
  coders happened to cross-check anyway. `headline_price_usd` is the study's headline variable and
  the A-domain items derive from it, so an uncorrected misread propagates into every figure the
  paper prints.
- Why the existing checks would not catch these: the magnitude screen run after nicepage looks for
  implausible values, and all three of these misreads were individually plausible — `$28` is a
  perfectly ordinary price for a video generator, and `$1.99` for an image editor. A wrong value
  that looks right is invisible to any check that only tests plausibility.
- New screen, added now: `tools/check_price_arithmetic.py` cross-checks `headline_price_usd` times
  the period implied by `headline_billing_basis` against `first_charge_amount_usd`. A misread
  usually breaks that relation even when each value looks sensible alone. Run across the pass it
  flags four records — faceless-so, invideo-ai, krea-ai, and jobscan. jobscan's flag is the
  already-queued A-011 quarterly-billing case and its ratio comes out at exactly 3.00, which is
  the screen independently reproducing a known finding rather than a new one. The screen decides
  nothing: vendors do legitimately advertise a round annual total beside a rounded monthly
  equivalent, so a flag is a place to look.
- Remediation: a verification sweep re-reads the A-domain money variables — `entry_tier_name`,
  `headline_price_usd`, `headline_billing_basis`, `first_charge_amount_usd` — in a second
  representation for the 42 completed records not otherwise in hand. It is a targeted re-read, not
  a re-code: no other variable is touched. The three arithmetic-flagged records are read first.
  The six records the D-007 currency sweep is editing are excluded and follow after it finishes,
  and the records already coded under the rule are not re-read.
- Timing: this runs inside the open window for the same reason as D-007 and D-008 — protocol
  section 6.8 fixes observation to the collection window.
- Standing: the instrument is untouched. No variable is redefined and no value list changes. What
  changes is the evidentiary standard for reading a number off a page, and which records have met
  it. Corrections are recorded per record with both the old and the new value.
- Disclosure: the paper reports the rule, the rate at which it caught errors on new records, that
  a sweep followed for the earlier ones, and what the sweep changed. Reporting the rate matters
  more than the individual corrections — it is a measurement of how unreliable single-representation
  reading of modern pricing pages is, which is itself a result other researchers should have.

### D-009 sweep result · 2026-08-12 · twenty-five records re-read, nothing changed, and the alarm that started it was misread

- Result so far: **25 of the 42 records in scope were re-read in a second representation and every
  one confirmed. Not a single coded value changed.** The re-read set spans the categories and the
  price range — 10web, adobe-express, adobe-firefly, aiclicks, anomaly-ai, elevenlabs, faceless-so,
  fotor, gamma, godaddy, google-veo, hailuo-ai, invideo-ai, ismybrandinai, jobscan, julius-ai,
  kling-ai, krea-ai, leonardo-ai, midjourney, mubert, murf-ai, myperfectresume, openai-sora,
  originality-ai. Seventeen remain and are listed below.
- **The inference that launched this sweep was wrong, and the sweep is what showed it.** D-009
  reasoned from "three misreads in four records" that the earlier records, coded without a
  mandatory second read, were likely to carry the same errors. The observed rate in those earlier
  records is 0 of 25. The two rates were never measuring the same thing: the three catches were
  errors in a coder's FIRST READ, which the rule forced that same coder to find and fix before
  anything was written down. They were never errors that reached a record. What the rule does is
  prevent a misread from being committed; it does not imply that coders working before it were
  getting numbers wrong, and the evidence now says they were not.
- That correction is worth more than the sweep's zero corrections, and the paper should carry it
  rather than the alarming figure that prompted the work. Publishing "single-representation reads
  are wrong three times in four" on the strength of four records, when a 25-record check of the
  same population found nothing, would have been a real error in the other direction.
- The arithmetic screen's flags are also resolved, and none was a misread. **krea-ai** — which the
  orchestrator specifically flagged as looking like a genuine error, because the record's own
  `computation_assumptions` note reads "$63/yr=$5.25/mo per page" against a coded `5.00` — was
  re-read twice and `headline_price_usd = 5.00` confirmed. The orchestrator's reading of that note
  was wrong. **faceless-so** ($24.00 card price against a $290 annual total) and **invideo-ai**
  ($17/mo against $200/yr) are vendors rounding a displayed monthly figure off a round annual
  total, confirmed from the pages. **jobscan** is the already-queued A-011 quarterly-prepay case.
  All four still print from the screen because the screen tests a relation, not a defect list; they
  are closed, and the closure is recorded here so they are not re-investigated.
- Remaining scope, now lower priority on the evidence: apify-robots-checker, aragon-ai,
  autoshorts-ai, beautiful-ai, brandcited, colossyan, copyleaks, d-id, decktopus, heygen, hostinger,
  humanizemy, humanizemy-ai-detector, humbot, hyperleap, ideogram, lovo-ai. Five of these carry the
  genuinely open question — colossyan, copyleaks, hostinger, humanizemy-ai-detector and humbot show
  a first charge exactly twelve times the headline with no computation recorded, so it cannot be
  told from the record whether the vendor published the total or the coder multiplied. Those five
  are done next as a provenance check; the rest follow as budget allows and are not blocking.
- Operational note: this sweep and four collectors were killed mid-run by an account weekly limit
  and the worktree was cleared. Nothing was lost beyond a few minutes of work, because every agent
  self-commits after each variable group and the branch had been pushed — the survivability design
  introduced after the earlier session-limit failures did its job under a harder failure than it
  was built for.

