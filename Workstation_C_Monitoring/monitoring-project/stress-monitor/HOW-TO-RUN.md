# HOW TO RUN ONE DASHBOARD
*Operator onboarding. Provisional — refine after the first real run.*

---

The scripts do the work; **you gate lightly.** One run = one date → one dashboard. The factory
*monitors* the metrics; it does **not** make the thesis call (that stays in the parent research project `CONTEXT.md`).

**One-time setup**
- `pip install -r requirements.txt` (fredapi + pandas).
- Set your FRED key in the environment: `export FRED_API_KEY=...` (bash) / `$env:FRED_API_KEY="..."`
  (PowerShell). Never commit the key. See `_config/fetch-rules.md`.

**A run**
1. **00_plan — confirm the manifest.** Open `_config/manifest.md`. If the metrics are unchanged,
   the gate is "go." If you want to add/change/drop a metric, edit `_config/manifest.json` (the
   authoritative list) — that edit *is* the configure-the-factory act, and it is the one place real
   judgment lives. Approve before fetch.
2. **01_fetch — pull the data.** `python stages/01_fetch/fetch.py` → writes
   `01_fetch/snapshots/<today>/` (one CSV per series + `provenance.json`).
3. **02_transform — compute.** `python stages/02_transform/transform.py` → writes
   `02_transform/computed/<today>.json` (latest reading, recent change, historical context per
   metric). Pure function of the snapshot; no network.
4. **03_render — render.** `python stages/03_render/render.py` → writes
   `03_render/output/<today>/dashboard.md`. Also write the run's `load-log.md` here.
5. **Glance.** Read the dashboard. That's the light review gate. If a reading is alarming, that is
   *input to your reasoning* — take it to the parent research project `CONTEXT.md`; the dashboard never concludes.

**Steady state:** once the manifest is settled, a run is steps 2→3→4 in sequence (the three scripts)
plus a glance. That collapse to "run the scripts" is the deterministic archetype working as designed.

**If a series fails to fetch** (network error / bad ID): the run stops and reports it — a missing
series is excluded, never faked. Fix the ID in the manifest or note the gap; do not paraphrase a
value from elsewhere into the dashboard.
