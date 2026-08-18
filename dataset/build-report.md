# Dataset build report

- **76 publishing rows** — 29 adjudicated, 47 primary. Pass 2 never publishes; it is the blind second reading behind the reliability figure.
- **2812 coded values** = 76 x 37.
- **337 unknowns**, of which **0 carry no attribution kind**.

## Storage shapes encountered

Reported because four separate times in this study a tool read one shape and produced a
confident wrong number (D-020, D-033, D-037, and once inside D-047).

- `variables/dict` — 2808
- `variables/str` — 2
- `toplevel/str` — 2

## Anything the build could not handle

- unrecognised shapes: **0**
- coded variables absent from a publishing row: **0**

## Per-output costs computed on a non-USD basis

Not contradictions. **A-021** established that `cost_per_output_computable` is
currency-neutral by the instrument's pre-registered design — protocol 8.3.10 and
section 9 limitation 12 apply the USD-centric deduction to items A1 and A3 only,
never to C3 — so a cost computed in the vendor's own currency is computable.

Listed because a reader is entitled to know that a **full-credit disclosure score**
can sit beside a **derived figure that is not dollar-comparable**. That asymmetry is
the honest cost of a currency-neutral construct, and A-021 names it too.

- aiva: per-output cost computable, basis is 'non_usd' — the derived figure is not dollar-comparable
- canva: per-output cost computable, basis is 'unknown' — the derived figure is not dollar-comparable
- gptzero: per-output cost computable, basis is 'unknown' — the derived figure is not dollar-comparable
- ismybrandinai: per-output cost computable, basis is 'not_applicable' — the derived figure is not dollar-comparable
- picsart: per-output cost computable, basis is 'unknown' — the derived figure is not dollar-comparable

## What ships with this dataset

The `records/*/*-sources/` directories must be published alongside these CSVs. For 159
coded values the local capture is the only surviving evidence, because their archive
citation resolves to a different capture or to none (D-037). A release of the CSVs alone
would look complete and be unverifiable.

