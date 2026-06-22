# CONTEXT.md
*Project: build-tool — the reasoning shell's synthesis (build-state + architecture decisions).*

> **STOP:** read this project's `CLAUDE.md` before this file.

---

## CURRENT STATE

*(Example build-state — replace with your own.)* Building `linkcheck` (spec in `references/recipe.md`). The
pipeline below carries it from plan to release.
- **Done:** recipe settled; `00_plan` gate passed.
- **In progress:** `01_build` — implementing the link resolver.
- **Blocked:** none.

## ARCHITECTURE DECISIONS

*(Example.)* The load-bearing choices and why — kept here so the build doesn't drift from its design.
- **Standard library only.** A link-checker isn't worth a dependency tree; stdlib keeps it portable and fast
  to audit. Revisit only if `[[wikilinks]]` support later forces a real markdown parser.
- **Pure core, thin CLI.** Link extraction/resolution are pure functions (text + base path → results); the
  CLI is a shell around them. This is what makes `02_test` possible without touching the filesystem.
- **Report, never fix.** Auto-fixing a link writes to human-authored content — out of scope under the
  bounded-autonomy rule. The tool surfaces problems; the human edits.

## THE BODY

`stages/` holds the build pipeline (`00_plan → 01_build → 02_test → 03_release`). In a real project the
actual code lives at the build stage — e.g. `stages/01_build/repo_vault/linkcheck/`. The reasoning happens
here at the project tier; the code is built there. At build time this shell's context is distilled into the
stage contracts once, and a run scopes context per stage.
