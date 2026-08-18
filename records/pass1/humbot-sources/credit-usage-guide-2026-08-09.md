# Evidence: Humbot Credit Usage Guide (modal on pricing page)

- URL: https://humbot.ai/pricing (modal opened via the "Learn Credit Usage Rules" button beneath the plan cards; same document/URL, no separate page)
- Accessed: 2026-08-09
- Method: rendered read — clicked the button via `javascript_tool` (`button.click()`), then read the opened modal's `innerText`. Reading a public page's own in-page modal is not a prohibited action under protocol §6.3 (no account, no login, no checkout).

## Full table text (verbatim)

> "Humbot Credit Usage Guide
> Below is a detailed breakdown of how Basic Words and Advanced Words are calculated across our suite of AI tools, helping you maximize your monthly quota.
>
> Feature | Word Type | Credits Required
> **AI Humanizer**
> AI Text Humanizer | Basic Words | 1 word per output word
> **AI Checker**
> GPTZero | Advanced Words | 1 word per input word
> Originality.ai | Advanced Words | 1 word per input word
> ZeroGPT | Advanced Words | 1 word per input word
> Humbot 1.0 | - | free for premium
> AI Image Detector | Advanced Words | Based on token usage
> **AI Study**
> AI Math Solver | Basic Words | Based on token usage
> AI Homework Helper | Basic Words | Based on token usage
> AI Quiz Generator | Basic Words | Based on token usage
> **Content & Writing Tools**
> AI Article Rewriter | Basic Words | 1 word per output word
> AI Summarizer | Basic Words | Text & Files: 1 word per input word; Audio & Video: 1 word per transcribed word; Images: Based on token usage
> AI Reading (Summary) | Basic Words | 1 word per input word
> AI Reading (Mind Map) | Basic Words | 1 word per output word
> AI Reading (Translation) | Basic Words | 1 word per output word
> AI Reading (Chat) | Basic Words | 1 word per output word
> AI Translator | Basic Words | 1 word per output word
> Citation Generator | Basic Words | 1 word per output word
> **Quality & Optimization Tools**
> Plagiarism Checker | Basic Words | 1 word per input word
> Grammar Checker | Basic Words | Input words x 1.6 + Output words x 6.7
> * Note: Image summary credits are calculated based on visual token parsing. Cost varies by image complexity."

## Use in coding

- Product category is "AI humanizer" and the product's own nav/marketing frames "AI Text Humanizer" as the flagship tool, so **AI Text Humanizer is treated as the principal output** (humanized text, metered in words).
- Its rate is exact and numeric: **1 Basic Word credit = 1 output word**. This resolves `credit_unit_defined = yes` and gives the principal-output rate for `credit_to_output_rate_published` and the `cost_per_output_computable` arithmetic.
- Rates ARE published for every other bundled tool too, but several (AI Image Detector, AI Math Solver, AI Homework Helper, AI Quiz Generator, and the image-input path of AI Summarizer) are stated only as "Based on token usage" with no number — not a computable figure, functionally similar to the codebook's "range" carve-out for `partial`. Coded `credit_to_output_rate_published = partial` on that basis even though the principal output's own rate is exact; documented in `conflict_note`/`coder_note` for reviewer visibility since this is a judgment call between two adjacent value-table rows.
- Checked the full page + modal text programmatically for "rollover", "roll over", "expire", "unused", "carry over", "fail", "error", "unsuccessful" — **none appear anywhere**. No rollover or failed-generation policy is stated in any official document found (pricing page, this modal, Terms of Service, Refund Policy). Coded `unknown` on both `credit_rollover_policy` and `failed_generation_charge_policy` accordingly — per the codebook this silence is itself the expected finding, not a search failure.

## Free-plan caveat

No visible UI element on https://humbot.ai/pricing shows a "Free" plan card or names its word/input limits — confirmed no DOM element anywhere on the page contains the bare text "Free" as of this read. The only reader-facing evidence a free plan exists at all is the FAQ line quoted in the main pricing evidence file ("...you can try the Free plan to test out our features before subscribing"), which names the plan but publishes no numbers. The vendor's embedded catalog data (`productslist-2026-08-09.json`) does carry a `Free` SKU (200 words/mo, 100-word input limit) — unlike the Basic/Pro/Unlimited figures, this number was never independently confirmed against a visible rendering (no "Free" card ever appeared across three separate page loads), so it is treated as vendor backend data rather than documented, reader-facing disclosure. `free_plan_exists` is coded `yes` from the FAQ text; `free_plan_cap_documented`, `free_plan_cap_value`, `free_plan_watermark`, and `free_plan_duration` are coded `unknown` since no document visibly states these to a reader. The catalog figures are recorded here for audit transparency only, not used as the coded values.

## Resource hub check

Visited https://humbot.ai/hub: this is an SEO content/blog hub (guides, listicles), not a support or help-center section. No billing FAQ, no help-center article, no acceptable-use policy distinct from the Terms of Service was found. Footer-level legal links are limited to Privacy Policy, Terms of Service, Refund Policy, and Affiliate Program (checked 2026-08-09).
