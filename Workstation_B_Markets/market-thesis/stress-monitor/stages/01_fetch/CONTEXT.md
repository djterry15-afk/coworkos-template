# 01_fetch — Pull FRED → Snapshot (L2 stage contract)
*One job: fetch the manifest's series from FRED into a dated raw snapshot. A deterministic joint.*

---

## What this is

The first mechanical joint. `fetch.py` reads `_config/manifest.json`, pulls each series via the
FRED API, and writes a verbatim dated snapshot + provenance. It applies no judgment and reads
nothing but the manifest and FRED.

---

## Contract

| | |
|---|---|
| **Input** | `_config/manifest.json` (series list) + `FRED_API_KEY` env var |
| **Also load** | `_config/fetch-rules.md` (key, snapshot, failed-capture discipline) |
| **Skip** | downstream stages · the parent thesis `CONTEXT.md` |
| **Output** | `01_fetch/snapshots/<date>/<SERIES_ID>.csv` (one per series) + `provenance.json` |

---

## Process

`python stages/01_fetch/fetch.py`

It fetches each series from `history_start`, writes one CSV per series + `provenance.json`
(rows, first/last date, fetch timestamp, source URL). Stages read the snapshot, never re-fetch.

---

## What NOT to do

- No transform here — raw values only (02's job).
- A failed series is **reported and excluded**, never faked or carried over (see `fetch-rules.md`).
- Never hardcode the key.
