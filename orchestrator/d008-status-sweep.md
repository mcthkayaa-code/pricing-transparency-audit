# D-008 status verification sweep

Frame-integrity check, run while the collection window is open, per deviations-log D-008's
systemic remediation clause. Not a coding pass: no study variable is touched here.

Scope derived from the frame and the records directory on 2026-08-10 (not from memory):
`frame-frozen-2026-08-04.csv` lists 76 products; `records/pass1/*.yaml` shows 48 with
`status: complete` (picsart is `status: in_progress` and does not count). The 28-product
difference is scope (a). Scope (b) adds lovo-ai, midjourney and freepik (already `complete`,
flagged for cause); playht is already inside scope (a), so the assignment's four named products
add three new IDs, for **31 products checked** in total.

---

## Rows that should change

**One row: `lovo-ai`.** Frame carries `active`. Evidence below is strong but does not meet this
sweep's own bar for a clean confirmation (a vendor-authored statement on the vendor's own page),
so this is flagged rather than asserted as settled — the orchestrator should make the final call,
possibly after checking the SDNY docket directly.

- `lovo.ai` and `lovo.ai/pricing` return **HTTP 402, "This deployment is temporarily paused"**
  on every check across two independent days (pass-1 coding 2026-08-09; this sweep 2026-08-10) —
  the whole apex domain, not one page. On its own this is exactly the kind of infrastructure
  failure method step 3 says is NOT evidence of shutdown, and I am treating it that way.
- Independently, **Lovo Inc. filed Chapter 7 bankruptcy on 2026-05-27** in the U.S. District
  Court, Southern District of New York, case **#26-11249**, three weeks ahead of scheduled
  motion-to-dismiss arguments in a voice-actor class action (Lehrman v. Lovo) alleging
  non-consensual voice cloning. Reported consistently, with matching case-specific detail (case
  number, judge, asset/liability figures), by **Law360**, **Bloomberg Law**, and **MLex** —
  specialist legal trade press, not the SEO-affiliate/content-mill sites that dominate the rest
  of the search results for this query and that I am treating with active suspicion given this
  study's own subject matter. Chapter 7 is liquidation, not reorganization.
- The bankruptcy filing predates the 2026-08-04 freeze by over two months. If the product is in
  fact gone, this is the **same defect class as D-008's openai-sora finding** — a pre-freeze
  fact the freeze-time re-check should have caught and did not — not a mid-window event under
  sampling-rules 10.4/section 10.
- What stops me from just writing `discontinued`: I found no statement in LOVO's own words. The
  "temporarily paused" text is generic Vercel hosting boilerplate, not vendor prose, and
  `help.lovo.ai` returned 403 (Cloudflare challenge — per method step 3, not evidence either
  way, not pursued further). A Chapter 7 filing is a legal act taken by the vendor itself, but
  it is not "the vendor's own page," which is the standard this sweep otherwise holds to. I am
  reporting the full strength of the evidence rather than rounding it down, and leaving the
  classification call to the orchestrator.

No other row in this sweep produced evidence pointing away from its frame status.

---

## Table

| product_id | frame status | verified status | evidence (URL + what it says) | date checked |
|---|---|---|---|---|
| lovo-ai | active | **inconclusive by this sweep's own rule; strong non-vendor-page evidence points to discontinued** | `https://lovo.ai`, `https://lovo.ai/pricing` — HTTP 402, "This deployment is temporarily paused" (Vercel infra message, both checked 2026-08-09 and 2026-08-10). `help.lovo.ai` — HTTP 403 (Cloudflare challenge, not evidentiary). Corroborating, not determinative: Law360/Bloomberg Law/MLex report Lovo Inc. Chapter 7 bankruptcy, SDNY case #26-11249, filed 2026-05-27, amid Lehrman v. Lovo voice-cloning suit. See flagged section above. | 2026-08-10 |
| midjourney | active | active (confirmed) | `https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans` (rendered) — live plan table, Basic $10/Standard $30/Pro $60/Mega $120/mo, identical to the pass-1 record's figures. `https://www.midjourney.com` (rendered) — live homepage, Sign Up/Log In active, "For billing support email us at: billing@midjourney.com". The 404s on /pricing and /plans (already logged in the pass-1 record) reflect a homepage redesign to "research lab" branding, not a product shutdown — prices simply moved to the help-center article. | 2026-08-10 |
| freepik | active | active (confirmed; rebrand under sampling-rules 10.4) | `https://www.freepik.com` redirects to `https://www.magnific.com` (rendered) — title "Magnific (formerly Freepik) \| The AI Creative Platform", "Trusted by 1M+ subscribers", live pricing/signup. Matches the pass-1 record (2026-08-07) exactly; rebrand keeps `product_id`, both names already recorded there. | 2026-08-10 |
| playht | discontinued | discontinued (confirmed) | `play.ht` — WebFetch: DNS resolution failure (ENOTFOUND). Direct DNS-over-HTTPS query: NOERROR but **no A record**; authoritative nameservers are `a.ns.facebook.com` / `dns.facebook.com` (Meta's own DNS) — verified against a working control query (elevenlabs.io resolved fine via the same method), so this is a fact about the domain, not a sandbox network issue. Browser navigation to play.ht denied/failed (dead domain), consistent. Corroborating: multiple independent sources (community.kore.ai, infrabase.ai, and others) converge on "Meta acquired PlayHT [as PlayAI] July 2025; service shut down December 31, 2025," matching the date already in the frame's own `frame_note`. **Limitation**: this environment blocks both WebFetch and browser reads of web.archive.org, so I could not pull PlayHT's own historical shutdown notice directly the way D-008 did for openai-sora; the DNS finding is the strongest first-party-adjacent evidence available to me. | 2026-08-10 |
| originality-ai | active | active | `https://originality.ai` — live homepage, "Signup / Login" to app, `/pricing` link, "3 Free AI Scans Per Day", current-model references (GPT-5.6, Claude Fable 5, Gemini 3). | 2026-08-10 |
| picsart | active | active | `https://www.picsart.com` — live homepage, "Start creating" CTA, `/pricing/` nav link, "Seedance 2.5" marked New, "100M+ creators". | 2026-08-10 |
| pika | active | active | `https://pika.art` — live homepage, sign-up + `/pricing` + API (`dev.pika.art`) links, "The new Pika API Club is here", "© 2026 Pika. All rights reserved." | 2026-08-10 |
| pixlr | active | active | `https://pixlr.com` — live homepage, "Plans start at just $1.99/month", `/pricing/` link, active AI tool set. | 2026-08-10 |
| plus-ai | active | active | `https://plusai.com` — live homepage, "Try Plus AI" / "Get started for free" CTAs, `/pricing` link, "© Plus Docs, Inc 2026". | 2026-08-10 |
| quillbot | active | active | `https://quillbot.com` — live homepage, "Upgrade to Premium", "Sign up now. It's free!", "35+ million writers". | 2026-08-10 |
| recraft | active | active | `https://www.recraft.ai` — live homepage, "Meet Recraft V4.1: Our most advanced model", Pricing/Enterprise links. | 2026-08-10 |
| resume-io | active | active | `https://resume.io` — live homepage, "Create my resume" CTA, live Trustpilot widget (4.2/5, 55,944 reviews), testimonials dated days before check. | 2026-08-10 |
| revid-ai | active | active | `https://www.revid.ai` — live homepage, "Our most popular plan starts at just $39/month", "240,909+ videos created", "14,258+ creators". | 2026-08-10 |
| rezi | active | active | `https://www.rezi.ai` — live homepage, Free/$29 Pro/$149 Lifetime plans listed, "4,510,834 Total Users". | 2026-08-10 |
| runway | active | active | `https://runwayml.com` — 308 redirect to `https://runway.com`, which is live: "Try Runway for free" CTAs, active "until August 14th" promo, pricing link. | 2026-08-10 |
| sapling | active | active | `https://sapling.ai` — live homepage, "Ready to try Sapling for free?", `/pricing` link, active enterprise integrations listed. | 2026-08-10 |
| shortsfaceless | active | active | `https://www.shortsfaceless.com` — live homepage, Essential $19/mo and Professional $29/mo tiers, "Copyright © 2026", recent build hash shown. | 2026-08-10 |
| speechify | active | active | `https://speechify.com` — live homepage, `/pricing/` link, blog content dated as recently as 2026-07-10. | 2026-08-10 |
| squarespace | active | active | `https://www.squarespace.com` — live homepage, "subscriptions start at $19/mo", active "20% off" promo, "Start a Free Trial". | 2026-08-10 |
| stable-audio | active | active | `https://stableaudio.com` (rendered; static fetch returned an empty shell) — live working demo, "Create music with AI" / "Try now". | 2026-08-10 |
| suno | active | active | `https://suno.com` — live homepage, Monthly/Yearly ("save 20%") plans, "Join Suno for free", "© 2026 Suno, Inc." | 2026-08-10 |
| synthesia | active | active | `https://www.synthesia.io` — live homepage, "Get started"/"Create free AI video" CTAs to `/pricing`, "New release" feature notice. | 2026-08-10 |
| teal | active | active | `https://www.tealhq.com` (rendered; static fetch 403) — live homepage, "Sign up! It's 100% Free!", active resume/job-tracker tools. | 2026-08-10 |
| udio | active | active | `https://www.udio.com` (rendered; static fetch returned an empty shell) — live homepage, Sign In/Sign Up/Create; banner notes "currently experiencing slow generation speeds" (a performance notice, not a shutdown one). | 2026-08-10 |
| undetectable-ai | active | active | `https://undetectable.ai` — live homepage, "Subscribe Now", "Start FREE Trial", "24M+ users • 29,473 new users this week". | 2026-08-10 |
| vidnoz | active | active | `https://vidnoz.com` — live homepage, "Create Free Video Now", "60 Free Credits Every Day", active model integrations (Veo, Kling, Sora). | 2026-08-10 |
| winston-ai | active | active | `https://gowinston.ai` — live homepage, `/pricing/` link, "Trusted by 10M+ users", blog dated July 2026. | 2026-08-10 |
| wix | active | active | `https://www.wix.com` (rendered; static fetch truncated before body) — live homepage, "300M+ sites built on Wix", "Get Started" CTA. | 2026-08-10 |
| writehuman | active | active | `https://writehuman.ai` — live homepage, Basic $12 / Pro $18 / Ultra $36 plans, update note dated "August 3", "7.5M+ documents humanized". | 2026-08-10 |
| xseek | active | active | `https://www.xseek.io` — live homepage, Starter/Growth/Scale plans, "Book a call" / "Test my visibility" CTAs. | 2026-08-10 |
| zety | active | active | `https://www.zety.com` (rendered; static fetch timed out) — live homepage, career-advice article dated 2026-07-24. | 2026-08-10 |

---

## Summary

31 products checked: the 28 in scope (a) with no completed pass-1 record, plus lovo-ai,
midjourney and freepik under scope (b) (playht, the fourth named product, was already inside
scope (a)). Zero rows are being asserted as changed outright. One row, lovo-ai, is flagged as a
likely-but-unconfirmed status change — the strongest finding this sweep produced, and one nobody
in the pipeline had connected before now: the pass-1 coder saw the same HTTP 402 outage on
2026-08-09 and coded around it as a hosting incident, without connecting it to the vendor's own
Chapter 7 filing three months earlier. Zero rows are coded inconclusive in the strict "could not
determine" sense; every row reached a reportable finding, though lovo-ai's finding carries an
explicit evidentiary caveat rather than a clean confirmation.

Whether the freeze-time check was broadly sound: mostly yes, with one real crack. The 28
never-before-checked products and the two rendering/URL-structure edge cases (midjourney,
freepik) all confirm cleanly — every one is a live, operating commercial product, several with
same-week content or matching pass-1 figures. That is what a sound freeze-time check should
produce on rows with nothing wrong. But lovo-ai shows the freeze-time check's method has a real
blind spot, not just the one instance D-008 already found: a plain page-load check (which is
what a freeze-time status re-check realistically is) will not surface a bankruptcy filing on a
domain that still technically resolves and only degrades into an outage later. openai-sora was
catchable by reading the vendor's own words. lovo-ai, if it truly is gone, is only catchable by
knowing to look outside the vendor's site entirely — a materially higher bar than what section
6.2's re-check appears to have been designed to do. I'd call this sweep evidence that the
freeze-time check is sound against the failure mode it was built for (missed vendor
announcements) and not sound against a different one (vendor collapse with no announcement at
all), which is a narrower and more honest claim than either "the check worked" or "the check
failed."
