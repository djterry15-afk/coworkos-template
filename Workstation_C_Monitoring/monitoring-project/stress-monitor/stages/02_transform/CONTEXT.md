# 02_transform — Compute Readings + Context (L2 stage contract)
*One job: turn the raw snapshot into current readings + historical context. A deterministic joint.*

---

## What this is

The second mechanical joint. `transform.py` is a **pure function of the snapshot** — no network, no
judgment. It computes derived metrics (spreads), the latest reading, recent change, percentile of
own history, and the GFC / COVID window peaks per the manifest.

---

## Contract

| | |
|---|---|
| **Input** | the latest `01_fetch/snapshots/<date>/` + `_config/manifest.json` (metric defns) |
| **Skip** | FRED · the parent thesis `CONTEXT.md` · rendering |
| **Output** | `02_transform/computed/<date>.json` |

---

## Process

`python stages/02_transform/transform.py`

For the anchor + each component: derive spreads where defined, then compute latest (value, date),
1-week and 1-month change, percentile within own history, and stress-window peaks. A metric with no
data (failed fetch) is marked `available: false`; an uncoverable window peak is `null`.

---

## What NOT to do

- No re-fetch — read the snapshot only (reproducibility).
- No interpretation, no verdict, no alarm thresholds — numbers only.
