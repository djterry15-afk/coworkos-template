# CONTEXT.md — 03_adapt (stage contract) — THE HUB
*Job: adapt the core draft into ONE output per **selected** platform. Terminal fan-out hub — it **emits**, it does not feed another stage.*

---

## INPUTS
- `02_draft/output/core-<slug>.md`.
- `references/voice-<platform>.md` for each selected platform.

## THE FORK (on demand, inside this hub)
- Render the platform-neutral core to **any platform in the seed's `platform-intent`** (from the manifest). One voice config per platform:
  - `references/voice-linkedin.md` — **POPULATED** (v1).
  - `references/voice-skool.md` — **RESERVED, not populated** (v1 is LinkedIn only).
- **Add a platform anytime by re-running this stage.** Produce LinkedIn now, then later just "run it through Skool voice" — **no trip back to tier-3, no new seed.** The core is already made; the hub applies the other platform's voice. The posture difference (LinkedIn insight close ↔ Skool learner / open-question close) lives in the **platform voice config**, not the angle.
- Only return to tier-3 to render a platform **outside the seed's `platform-intent`** — whether content fits a platform's posture is a reasoning call.

## PROCESS
1. For each selected platform: re-voice the core per `voice-<platform>.md` (posture + close-form + format). *Same body, platform close.*
2. Write `output/<platform>-<slug>.md` — **publish-ready**.

## OUTPUT
- `output/linkedin-<slug>.md` (v1)

## HARD GATE — PUBLISH
The factory produces the publish-ready file and **STOPS.** No posting, no scheduling, no analytics. Publishing externally is the human's act, outside the factory (writes external permanent state).

## NOT
- Do not populate `voice-skool.md` until Skool is a selected platform (state gates structure).
- Do not post anywhere. Do not auto-select a platform.
