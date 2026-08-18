# Tooling failure modes: a methods note for anyone coding web documents at scale

**Written 2026-08-17 from this study's own deviations log. Every item below actually happened here, was
caught, and is dated in `orchestrator/deviations-log.md`.**

This is the part of the study most likely to be useful to someone whose subject is not pricing. A
documents-only audit of live web pages fails in specific, repeatable ways, and almost none of them look
like errors while they are happening — they look like findings. The list is ordered by how much damage
each did before it was caught.

A single sentence carries the whole note: **a tool that reads less than it claims produces a number
nobody can distinguish from a result.**

---

## A. Reading the page

**1. A rendered figure is not the figure in the markup.** Prices are commonly injected at runtime. A
static fetch of a pricing page returns a pre-hydration shell with no price in it, and a coder who reads
that shell records "no price published" about a vendor whose price every browser displays. This study
had three products coded that way before the mechanism was identified, and the fix — a rendered read —
had to be applied retroactively.

**2. `innerText` returns nothing for a hidden element; `textContent` returns the real text.** An entire
eleven-answer FAQ was recorded as unreadable because a coder clicked the accordion triggers and read
rendered text. The answers were in the DOM at load, populated, hidden. Reading `textContent` of each
`aria-controls` target retrieved all eleven **without interacting with the page at all**. The same
record had already solved this problem on a different page of the same vendor and did not reapply it.

**3. Two collapsed FAQs on the same site can be two different kinds of evidence, and nothing on screen
says which.** One vendor here answers questions in a native `<details>` element on its pricing page —
the answer text sits in the DOM whether the disclosure is open or shut, so a capture holds it — and in
a JavaScript-driven accordion on its home page, where the answers are **absent from the collapsed DOM
entirely**: not in the markup, not in any script payload, retrieved only from a separately-fetched
bundle when a reader clicks. Same furniture, same visual idiom, same site. A coder who learns "FAQ
answers are in the DOM" from one page carries a false generalisation to the other, and a capture of the
second one shows `aria-expanded="false"` and nothing else.

**The consequence is not that the accordion's contents are unusable — it is that a capture cannot tell
you whether the vendor discloses them.** A reader clicking that control sees the answer, so the vendor
does disclose it; the capture merely failed to expand. This study coded five variables `unknown` on one
product for exactly that reason, and the values were properly disclosed. Deciding it takes one live
finding: **does the page display that text to a reader?** Expand the control, or establish that the
component renders the payload it holds.

**4. A saved auxiliary file can make absent evidence look present.** Beside that capture sat a
hand-saved fragment holding the accordion's answers in unquoted-key object-literal form. It is a slice
of the bundle, not a render — but it is a plain text file in the record's own source directory, and it
reads exactly like retrieved evidence. **The most dangerous file in a capture set is the one a coder
saved themselves**, because provenance is what a capture carries and a fragment carries none.

**5. A bundle can hold several generations of pricing.** One chunk in this corpus carries multiple sets
of pricing-config objects for differently-named plans at unrelated price points — an archaeology of the
vendor's past tiers, live in the shipped JavaScript. A figure taken from the first regex match can be
years out of date and perfectly well-formed. Check every plan name against what the page displays.

**6. A 403 to a static fetcher is often a 200 to a browser.** Three vendors' help-centre articles refuse
`curl` and render normally in an ordinary browser. The study already had a rule authorising a rendered
read and had applied it to pricing pages but not to help articles, where it applied equally.

**7. A superscript-cents layout can render `$6.75` as `$675`.** Found by one coder and then swept for
across the corpus. Price text extracted from markup needs a second representation — a DOM attribute, an
embedded JSON payload, a `data-price` — before it is trusted.

**8. A summarising fetch will invent structure.** Asking a tool to summarise a pricing page returns
plausible tiers that are not on the page. Two instances in this study. The rule that followed: quote,
never summarise, and quote from a saved artifact rather than from a response.

**9. A vendor can re-implement a page between your window and your writing-up.** The accordion in
mode 3 now server-renders its answers into plain markup; eleven days earlier it did not. Nothing about the
policy changed. **A live page is evidence about the mechanism and not about the frame** — which is
precisely what makes it worth loading, because the mechanism is what decides whether a capture's
silence means anything.

## B. Reading the archive

**10. Check more than one capture.** A billing FAQ had **31 captures**. The coder checked the newest,
correctly found a bot-wall shell, and concluded the document was unrecoverable. Two earlier captures
carried the full article. One capture is not the archive.

**11. Raw-content archive responses are compressed, and gzip is not the only codec.** A capture read
without decompression looks like an empty shell — that much was known here early, and it probably
accounts for at least one other "empty capture" conclusion never revisited.

**What was not known is that the same endpoint also serves zstd and brotli, and that the failure mode
inverts.** A zstd capture decoded as gzip-or-nothing does not come back empty; it comes back as **noise**,
and a price regex run over that noise **mined a `$5` out of it** — presenting as a total price change 112
seconds after the previous capture, on a page whose two captures are byte-identical once properly
decoded. A missing decompressor cost this corpus a fabricated finding, not a missing one.

**Never let a decoder fail silently into "empty" or into raw bytes.** Return an explicit `undecodable`
and stop, because a pattern-matcher downstream cannot tell noise from content and will find something
plausible in it. That is the same lesson as the summarising fetch in mode 8, arriving from the opposite
direction: invented structure is not caught by any magnitude or arithmetic screen.

**12. A trailing slash can change a timemap from 0 captures to 66.** `…/pricing` returned nothing;
`…/pricing/` returned sixty-six mementos. Any negative archive result should be re-run against URL
variants before it is recorded.

**13. An archive cannot capture a client-side variant.** The crawler does not execute the experiment
script, so a page under live A/B assignment is archived in one arm only — and no number of captures
will document the other. A protocol rule that admits only archive evidence for display variance is
**unsatisfiable** for the commonest kind of variance on modern pricing pages.

**14. An inexact archive citation is not a citation.** The service resolves a timestamp it has no
capture for to whatever is nearest **at request time**. This study watched one such citation resolve to
a capture dated 13 August and, two days later, to one dated 16 August. Verify that a cited capture
exists **at the cited timestamp**; a plausible-looking date proves nothing.

**15. A save request that returns an error may have succeeded.** This study's `archive_status` field
recorded what each save request appeared to return. Verified against the capture index afterwards, **12
of 76 records understated their own archival coverage**, and on five of them a capture dated the
collection day resolves today — so the failure note was wrong when written, not merely stale.

**16. Distinguish "we could not ask", "we are not allowed to read it", and "it is not there."** Three
different facts, and this study merged them **three separate times in one function.** A sweep logged 110
citations as missing captures on the strength of empty responses; re-tested slowly they returned 503,
and the service was throttling. Later, 13 of the 14 rows that same tool still called `missing` turned
out to be **403 — the archive refusing an entire host** — with the tool's own `detail` column recording
`HTTP 403` beside a verdict of "no capture exists", across three sweeps, unread. A third instance sat
beside it: a local request timeout also returned `missing`, so a request that never reached the service
was recorded as evidence about a document.

Corrected, the study's genuine archival absence was **one citation out of 511** rather than fourteen.

**And the nastiest shape of all: a 200 with an empty body.** A degraded Memento timemap endpoint answers
**HTTP 200 and returns zero bytes**, which a naive enumerator reads as "this URL has no captures". It hit
five URLs in one batch here; retried, the same URLs returned **12, 66 and 66 mementos**. Had that batch
been trusted, the sweep would have reported four documents as never archived and been wrong about three
of them. The status code is the success code, the request completed, nothing anywhere says failure —
**only the arithmetic of an empty result against a plausible expectation catches it.** The same
discipline applies one service over: on Common Crawl a **404 means no record and a 502 or 504 means no
answer**, and merging them repeats the whole error in a new place.

**The transferable fix is not a longer status list — it is the default, plus one assertion.** Every one
of these came from a fall-through that asserted absence. Make the unrecognised case `unclassified` and
let it be loud; a bucket that means "there is nothing there" must be reachable only by a response that
says so. And **treat a zero-length success as a failure to answer**, because no service legitimately
returns nothing with a 200.

**And check whether the refusal is itself your finding.** A 403 on every URL form for one domain, while
four peer domains return 200 in the same run and the domain's own `robots.txt` invites crawlers, is not
a fact about your tooling. It means **that vendor's documents cannot be independently re-examined at
any past date by anyone** — which, for an audit of what vendors disclose, is a stronger result than the
provenance failure it was masquerading as.

**17. There is more than one archive, and one of them may sit in a different country.** Common Crawl's
index is separate infrastructure and its crawler runs from the US, which makes it a **second
geographic vantage point** for free. This study discovered that on its last day, after months of
treating a geography-bound value as an unavoidable limitation.

## C. Reading your own data

**18. Read every storage shape — and every storage LOCATION.** The single most expensive class here,
**six separate times.** A field stored as a dict inside one map, a bare string inside the same map, and
a string at the top level is one field with three shapes, and a tool that reads one of them produces a
confident number: five reliability units silently dropped; sixteen publishing rows reported as having no
provenance when the real figure was zero; a text-keyed bucketing that dropped one record and reported a
76-product corpus as 75.

The last two were **directories rather than fields**, which is the same defect one level up and harder
to see. A product's saved captures live under `records/pass1/`, under `records/pass2/`, or at the study
root — four tools globbed the first alone, and one of them went on to report a publishing row as having
no re-examinable evidence at all, naming seven files as missing that all existed. And the structural
validator globbed `records/pass1/` when live records sit in four folders, so even when its path
resolved it was checking 76 of 129.

**The direction of the error is not random and the reassuring direction is more dangerous, because
nothing prompts a second look.** Three of these ran alarming — a provenance crisis, an archival
coverage failure, a row with no evidence — and each was investigated immediately because it looked
bad. The reassuring ones sat: dropped reliability units make a corpus look tidier, and a validator
that examines nothing reports success.

**19. Compare numbers as numbers.** `10.0` against `10.00` counted as coder disagreement in nineteen
instances and pushed a headline reliability figure below its threshold. The published claim built on it
had to be withdrawn.

**20. A bare `no` is a YAML boolean.** So is `yes`, `true`, `off`. A coded value written unquoted comes
back as `False` and fails an enum check that would otherwise pass — or worse, passes a check that
coerces it.

**21. Never edit a record by line surgery.** A normalising script produced invalid YAML in eight
records. Two years of care and one regex. This orchestrator then did it three more times in two days,
each caught only because a parse check ran **before** the commit rather than after.

**22. Read negation.** A classifier matched the phrase `instrument gap` inside the sentence *"not
instrument gap"* and assigned that very category. Coders and adjudicators routinely rule categories out
**by name**, so a matcher blind to negation reads their exclusions as assertions. And the obvious fix
overcorrects: suppressing any match near a negator moved fifteen records wrongly, because evidence
describing an absence is written in negatives throughout.

**And read the spelling your own output uses.** The same classifier's category pattern allowed a space
or a hyphen — `vendor silence`, `vendor-silence` — and therefore could not match `vendor_silence`, which
is the canonical form: the spelling in the codebook, in every record, and in this tool's own output
column. A coder writing `unknown_kind=vendor_silence` in their evidence was invisible to the classifier
that exists to read evidence for exactly that. **Test a matcher against the vocabulary your own
artifacts are written in**, and when you widen it, measure the net change before believing the fix — the
widening here moved zero rows, which is the only reason it could be accepted without a re-audit.

**23. Audit what the machine classified, not only what it flagged.** 394 attributions were set by
pattern and never checked; two independent reviewers found **50 wrong, and 49 of the 50 ran toward the
study's own conclusion**. The rows a design treats as finished are the rows most worth checking, and a
classifier's errors are not randomly distributed — they follow the shape of the categories it was
built to favour.

**24. A check nobody runs is not a check, and a check that quietly covers less than it claims is
worse.** One tool defaulted to a glob that excluded every published row in the dataset while printing
"checked 76 records". Ask what a tool globbed before believing its output.

**25. The terminal case of that, and the one to guard against by construction: a checker that examines
ZERO rows and exits 0.** This study's structural validator defaulted to a path relative to the
repository root while every instruction told agents to run it from the study directory. From there the
glob matched nothing, the loop never entered, and the tool printed **nothing** and returned success.
Agents reported "validated OK" on the strength of that silence for days.

Two properties made it invisible. **Silence is indistinguishable from a pass** — there is no output to
disbelieve. And the corpus happened to be clean, so nothing downstream ever contradicted it; a vacuous
check aimed at clean data leaves no trace anywhere. Re-running it properly found 129 records and zero
failures, which means no record was ever wrong and **nobody had established that.**

The same file had a second, related defect: its `__main__` block did not call the functions holding
its real logic. Two checks existed, were correct, were covered by tests of a sort — and had never run
except by hand. **An entry point that reimplements what the module already does is dead code that
looks live.**

The guard is one line and it generalises: **a check that finds nothing to check must fail.** A
denominator of zero is arithmetic that cannot be true, which this note's closing section already names
as the cheapest detector available — used here against absence rather than excess.

## D. Working with concurrent agents

**26. Scope the commit, not only the add.** `git commit -- <directory>` takes everything beneath that
directory, including a file another agent wrote seconds earlier. Two commits here carry another agent's
work under a message about something else. Name files.

**27. Merge, do not append.** A resumable checker appended a second row per item on its second run,
producing 603 rows for 511 items, and every summary computed from the file double-counted until a total
exceeded a known denominator.

**28. An instruction delivered at spawn reaches only what spawns after it.** A token coders were told to
write lived in the dispatch prompt rather than in the persistent required reading, so the 44 records
collected before it was written could not carry it — and a prevalence computed from that token is a
floor, not an estimate. Anything that must bind a whole corpus belongs in the document, not the
dispatch.

**29. A rule computed against a mutable file is a manifest with extra steps.** Replacing a missing
manifest with "read the ledger and take the 17th slice onward" removed one dependency and created
another: the ledger regenerated mid-run, two new rows appeared ahead of the slice, and the boundary
moved. Freeze the slice at dispatch and hand over an immutable list.

**30. A prohibition without a permitted alternative invites a narrow breach.** Told never to read
another product's record, two independent adjudicators each opened one for **formatting reference**,
because nothing said where else to look. Both disclosed it. The fix was a route, not a firmer rule.

**31. A rule pushed to a running agent arrives abridged, and the abridgement becomes the rule.** Mode 28's sibling, and it cost this study more. A coder was found applying a rule too loosely, so the rule
was sent to the two agents then running. One of them was mid-task, holding the full statement in its
required reading, and applied the **pushed prohibition over the caveat the prohibition was written
alongside** — coding five properly-disclosed variables `unknown`. The first error was too permissive
and the correction was too strict, and **both came from the same cause: a rule that reached a coder as
a message rather than as the document it lives in.**

A message is an instruction; a document is a rule. A pushed instruction is shorter than the rule by
construction — nobody pastes four paragraphs into a dispatch — and the half that gets dropped is the
half that constrains the prohibition. If a rule needs a caveat to be correct, it cannot be delivered
without one; send the pointer, or send both halves and say which cases the caveat owns.

**32. Check that the role whose job is deciding has the rule that decides.** The same rule was
present in the coders' brief and **absent from the adjudicators' brief entirely** — so the only pass
whose function is resolving disputes lacked the text governing the dispute in front of it. Role-scoped
briefs drift apart silently, because each one reads complete on its own.

**33. Scope a task from the diff, not from the report.** Two adjudications here were briefed from what
each earlier coder had described as notable in its own write-up. Diffing the two records afterwards
showed **9 disagreements where 5 had been briefed, and 6 where 3 had been briefed** — a third to a half
of the real work missing from both briefs, on the same day, from the same habit.

A report is a summary written to be read, and a summary drops what its author found uncontroversial —
which is exactly where a second reader's silent divergence hides. The diff drops nothing. **Use the
mechanical comparison to set the scope and the human account to supply the argument, never the reverse.**

The cost was smaller than it should have been, and only because the agent overrode the brief: it diffed
all 37 variables itself, found the four nobody had assigned it, resolved them, and **labelled each one
as outside its remit** instead of presenting them as adjudicated. **An under-scoped brief is caught by
an agent that checks its own scope, which is not something you can rely on.** Give it the diff.

---

## What actually caught these

Almost none were caught by the check designed to catch them. The recurring mechanisms were:

**A total that exceeded a known denominator.** 182 unserved captures against 511 citations; 100 records
in a 76-product corpus. Arithmetic that cannot be true is the cheapest detector there is, and it costs
one `assert`.

**Two independent readings of the same file disagreeing.** A report path that deduplicated by key and an
ad-hoc script that did not gave different counts, and the difference was the bug. Where a number
matters, compute it twice by different routes.

**An agent reporting something against its own interest.** Three adjudicators disclosed breaches nobody
would have detected. A reviewer reversed its own initial flags after calibrating against existing
decisions. A retrieval sweep marked one of its own conclusions conditional and said to hold it. **None
of that is enforceable, and all of it depended on breaches being fixed structurally rather than
punished.**

**Being asked a blunt question by someone who had looked.** The owner said a figure was on a vendor's
own page and that we had said otherwise. Going to look produced a real correction, a retracted framing,
and a new archive route — and the answer turned out narrower than either party had claimed.
