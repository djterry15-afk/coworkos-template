# CONTEXT.md — 00_plan (stage contract)
*Job: take a **seed** (one post idea) and **plan the run** — scope what to pull/search into a manifest. Production planning, NOT angle-setting; the angle is discovered later, at the `01` gate.*

---

## WHERE THE SEED COMES FROM
A **seed** is one post idea — a *topic*, not an angle. It arrives at run start: stated in the entry prompt, picked from a tier-3 idea-backlog (if you keep one), or drawn from a (rare) campaign batch. **No campaign or tier-3 plan is required** — the common path is a single idea you want to explore.

## INPUTS
- The seed (entry prompt, or a named tier-3 backlog item).
- `manifest-schema.md` (the shape to fill).

## PROCESS
1. **Capture the seed:** topic (one line) + `platform-intent` (which platforms it might suit — a light call, refined later) + slug. If the seed names a tier-3 backlog item, **pull that one settled file** → snapshot, provenance (six guards) — do *not* pull tier-3 synthesis.
2. **Scope the sources — two kinds:**
   - **Declared** — sources you already know (named files); tag `grade` + `location`.
   - **Exploratory** — name the *scope* to search (which folders/projects) and *what you're looking for*. Discovery happens in `01`, not here.
3. **Write `output/manifest-<slug>.md`.** No angle — the manifest scopes the run, it does not decide the argument.

## OUTPUT
- `output/manifest-<slug>.md`

## GATE — STOP for scope approval before 01 runs (mandatory)
A real stop, not a notification. Get human approval of the **seed/topic**, the **search scope**, and any **declared sources** — *before* `01` fetches anything. **Do not self-fast-path on "collection is read-only / reversible"** — choosing and *narrowing* the scope is direction-setting (it shapes which angles can surface). The agent may *propose* a narrowing; the human approves it. Only then `01_collect` runs.
*(With exploratory fan-in, specific files are discovered in `01`, not here — so this gate approves the **scope**; the discovered source set is reviewed at the `01` gate.)*

## NOT
- Do **not** decide the angle or what the post argues — that's discovered at the `01` gate from the pulled material. `00_plan` scopes; it does not reason the post.
- Do **not** require a tier-3 brief/plan — a bare seed (a topic) is a complete input.
- Do **not** pull a tier-3 *synthesis* to "understand" the topic — fetch only the seed/declared settled files (self-containment; guard 6).
