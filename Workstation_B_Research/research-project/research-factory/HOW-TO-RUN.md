# HOW TO RUN ONE RESEARCH BRIEF
*Operator onboarding. Read this if you've never driven this factory.*

---

You drive; the agent fetches and drafts; **you decide at every gate.**
One run = one question → one brief. The factory *structures* the reliability judgment; it does **not**
make it for you. (Worked once, end-to-end, cold — four gates, four artifacts, no fabrication.)

1. **Bring a seed.** One research question. Optionally: source pointers you already know, and a scope
   hint (`external only` is the default; say `also check Work_Build` to allow workspace fan-in). Embedded
   empirical claims in the seed are *claims to verify*, not sources — the agent will log them as such.
   *Example seed (generic):* "When a fast-growing SaaS company switches from seat-based to usage-based
   pricing, does net revenue retention typically rise or fall in the first year, and what drives it?"

2. **00_plan — frame it.** The agent turns the seed into a manifest (question · slug · scope · declared
   sources · reliability bar). **You approve seed + scope before it fetches.** Mandatory stop. (Scope is
   direction-setting — don't let the agent narrow it silently.)

3. **01_source — find & grade (the heavy gate).** The agent Queries the wiki first (what we already
   hold), then searches externally and **proposes a candidate ledger** — discovered sources + grades +
   the angle the evidence points to. **You approve the candidate set + grades + angle.** Reject weak
   sources; flag any AI-authored ones. **Only after you approve** does it commit full snapshots of the
   approved sources. (This ordering is the v2 fix — no snapshotting sunk cost before you've signed off.)

4. **02_extract — pull the evidence.** The agent curates the raw snapshots into an evidence file
   (verbatim + provenance, tagged for/against). You check it matches the snapshots.

5. **03_synthesize — write the brief.** Evidence for / against / mixed · contradictions · source
   ledger — **no verdict.** You review.

6. **After the run.** The brief is yours to reason over → update the parent research project `CONTEXT.md` (the verdict
   is *your* call). Optionally hand the snapshots to the wiki to ingest. Then archive working files →
   `_archive/<slug>/`.

---

**If you're unsure whether a source is good enough** — that's exactly what gate 01 is for. The factory
makes the reliability call explicit and auditable; you make it. **If a source can't be captured
(403 / paywall)** — it's dropped, never paraphrased from a search summary. No snapshot → not evidence.
