# Source: https://sapling.ai/ai-content-detector
# Accessed: 2026-08-12
# Method: rendered browser read; verbatim strings pulled via document.body.innerText (JS) to avoid
#         WebFetch markdown-summarization error (WebFetch's small-model pass on this page fabricated a
#         false "Pro=50,000 / Enterprise=100,000" distinction; the verbatim DOM text below corrects it).

## Verbatim (innerText, exact quote, this is the authoritative reading):
"My text is getting cut off. How can I run the AI detector on longer texts?
The free version is currently truncated to 2000 characters (roughly 400 to 500 tokens). Pro and
Enterprise Sapling subscribers can paste texts of up to 100,000 characters (roughly 20,000 to
25,000 tokens). For texts longer than that, please break up the text into multiple sections, or
consider using our API. If you plan to process more than 5 million characters/month, contact us
to see how we can better support your use case."

=> Free tier cap: 2000 characters per query (standing, per-request limit; quantified).
=> Pro AND Enterprise share the SAME cap: 100,000 characters per query (quantified). No separate
   50,000-character Pro tier exists -- that figure was a WebFetch misread, corrected here.
=> "5 million characters/month" is phrased as a contact-us threshold ("if you plan to process more
   than X, contact us"), not as a stated entitlement/cap of the Pro plan itself. Not coded as a
   quantified Pro-tier cap for that reason -- it is not presented as part of what Pro includes.

## Negative findings (keyword search across full page innerText, 9427 chars, via JS):
No occurrence anywhere on this page of: "unlimited", "per day", "account", "sign in", "watermark",
"commercial". I.e. the vendor does not state a check-frequency limit (daily/monthly count) for the
free checker in either direction (no number, no "unlimited" claim either)(page is silent), does not
mention any account/sign-in requirement to use the free checker, and does not address watermarking
or commercial use of detection results anywhere on this page.

## Interactive tool observed in default state
Live demo box pre-loaded with a sample: "Fake: 73.6%" with a colour gradient meter, and
"Share Certificate (Expires after 3 Days)" + Copy button. "Show Sentence Perplexity Scores" toggle
button also present. (Context only -- not a coded pricing variable; the certificate-expiry detail
has no codebook variable to attach to.)
