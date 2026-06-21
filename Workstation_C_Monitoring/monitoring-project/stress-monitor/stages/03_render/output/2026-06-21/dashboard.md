# Market-Stress Monitor — 2026-06-21

*Readings + context, **not** a signal. Snapshot: `stages/01_fetch/snapshots/2026-06-21`. The thesis call stays in the parent research project `CONTEXT.md`.*

## Overall conditions

**Chicago Fed NFCI (overall financial conditions)** — **-0.51** (2026-06-12)
- *Composite of ~105 indicators of US financial conditions. 0 = average; positive = tighter (more stress) than average, negative = looser.*
- Sits **around the middle of its history** (since 2007-01-05; 43.4%ile). GFC peak 3.07 (2008-11-28), COVID peak 0.31 (2020-04-03).
- Change: +0.00 (1w) · -0.01 (1m)

## What the metrics say

### Funding plumbing (these move first)

- **10Y Term Premium** — **0.77 %** (2026-06-12)
    - *Extra yield investors demand to hold a 10-year bond rather than roll short-term debt — compensation for duration/rate risk.*
    - Sits **above the middle of its history** (since 2007-01-02; 88.0%ile). Change -0.03 (1w) · +0.02 (1m).
    - Stress reference — GFC 1.25 (2009-06-10), COVID -0.29 (2020-03-19).

- **SOFR - EFFR (funding spread)** — **0.00 pp** (2026-06-17)
    - *Gap between secured (repo, SOFR) and unsecured (fed funds, EFFR) overnight borrowing. Spikes signal funding/plumbing stress.*
    - Sits **above the middle of its history** (since 2018-04-03; 69.0%ile). Change +0.03 (1w) · +0.10 (1m).
    - Stress reference — GFC —, COVID 0.29 (2020-03-17).

### Credit spreads (these confirm, and lag)

- **HY credit OAS** — **2.63 pp** (2026-06-17)
    - *Extra yield on US high-yield (junk) bonds over Treasuries. Widens when risk appetite drops.*
    - Sits **near the LOW of its history** (since 2023-06-19; 1.8%ile). Change -0.17 (1w) · -0.20 (1m).
    - Stress reference — GFC —, COVID —.

- **IG credit OAS** — **0.74 pp** (2026-06-17)
    - *Extra yield on US investment-grade corporate bonds over Treasuries.*
    - Sits **near the LOW of its history** (since 2023-06-19; 3.6%ile). Change -0.01 (1w) · -0.01 (1m).
    - Stress reference — GFC —, COVID —.

## Table (visual reference)

| Metric | Latest (date) | 1w Δ | 1m Δ | %ile | GFC peak | COVID peak | dir |
|---|---|---|---|---|---|---|---|
| Chicago Fed NFCI (overall financial conditions) | -0.51 (2026-06-12) | +0.00 | -0.01 | 43.4% | 3.07 (2008-11-28) | 0.31 (2020-04-03) | anchor |
| 10Y Term Premium | 0.77 (2026-06-12) | -0.03 | +0.02 | 88.0% | 1.25 (2009-06-10) | -0.29 (2020-03-19) | context |
| SOFR - EFFR (funding spread) | 0.00 (2026-06-17) | +0.03 | +0.10 | 69.0% | — | 0.29 (2020-03-17) | higher = more stress |
| HY credit OAS | 2.63 (2026-06-17) | -0.17 | -0.20 | 1.8% | — | — | higher = more stress |
| IG credit OAS | 0.74 (2026-06-17) | -0.01 | -0.01 | 3.6% | — | — | higher = more stress |

## Notes

- `HY credit OAS` has no COVID context (history starts 2023-06-19).
- `HY credit OAS` has no GFC context (history starts 2023-06-19).
- `IG credit OAS` has no COVID context (history starts 2023-06-19).
- `IG credit OAS` has no GFC context (history starts 2023-06-19).

*pp = percentage points · % = percent · index per series. Position = where the latest reading sits within the metric's OWN history — not an absolute signal or verdict.*
