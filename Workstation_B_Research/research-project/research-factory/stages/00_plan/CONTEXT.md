# 00_plan — Plan the Run (L2 stage contract)
*One job: turn a seed into a manifest. NO fetching, NO web, NO wiki, NO angle. Stop at the gate.*

---

## What this is

The seed enters here — from the operator, or from a tier-3 idea-backlog (same slot either way; a seed
is the run's *trigger*, not a fan-in). You frame it into an inspectable manifest. You do not
answer the question here; you set up the run.

---

## Contract

| | |
|---|---|
| **Input** | a seed: one research question (+ optional source pointers + scope hint) |
| **Also load** | `_config/reliability-bar.md` (to state the bar for this run) |
| **Skip** | the wiki · the web · `artifact-format.md` · downstream stages |
| **Output** | `00_plan/manifest-<slug>.md` |

---

## Process

1. Restate the question in one sentence. Derive a kebab-case **slug**.
2. Set **scope**: `external-only` (default) | `+workspace` (only if the operator says so). Record it.
3. List **declared sources** — any pointers that came with the seed (these become *declared
   fan-in* at 01). A seed pointer is a source; the seed itself is not.
4. State the **reliability bar** for this run (default: cite A/B only; C = leads).
5. Write the manifest. Stop.

**Manifest skeleton:** question · slug · date · scope (+ rationale) · declared sources
(title · where · why) · reliability bar (+ any source-state caution) · target = research brief.

---

## GATE (mandatory stop) → 01_source

the operator approves: the question framing · the scope · the declared sources.
**Do not proceed to fetch without sign-off.** Scope is direction-setting; narrowing it yourself
is hidden direction-setting.

---

## What NOT to do

- No web search, no wiki read here — that is 01's job.
- No angle, no verdict. The manifest sets up the search; it does not pre-decide the answer.
