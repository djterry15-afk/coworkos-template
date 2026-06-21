# Fetch Rules — _config (L3, stable across runs)
*The discipline the deterministic joints obey. Mirrors the research factory's provenance rules,
adapted for a single structured-data source (FRED).*

---

## Key handling
- The FRED API key lives in **`stress-monitor/.env`** (gitignored) as `FRED_API_KEY=...`, loaded by
  `fetch.py`; a pre-set `FRED_API_KEY` environment variable also works. See `.env.example`.
- **Never** hardcode it in a script, the manifest, or any committed file, and never commit `.env`.
  If the key is missing, the fetch stops with a clear message — it does not prompt or guess.

## Snapshot + provenance
- Every run writes a **dated raw snapshot** (`01_fetch/snapshots/<date>/`): one CSV per series,
  verbatim from FRED, plus `provenance.json` (series id, label, rows, first/last date, fetch
  timestamp, source URL).
- Downstream stages read **only the snapshot**, never re-fetch live. A run is reproducible from its
  snapshot.

## Failed capture → exclude, never fake
- If a series fails to fetch (network error, bad/renamed id, empty result), the run **reports the
  failure and excludes that series** from the dashboard. A missing metric is shown as "unavailable
  this run," **never** paraphrased or carried over silently from a prior run. (Same rule as the
  research factory's failed-capture→exclude.)

## Single source, by design
- FRED only. Metrics not on FRED (MOVE, cross-currency basis, Treasury market depth) are
  out of scope until the widen phase — they need a second source class.
