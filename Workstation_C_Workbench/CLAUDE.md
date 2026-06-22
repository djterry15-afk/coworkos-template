# CLAUDE.md
*Workstation: Workbench — an EXAMPLE domain (a subject-area) that holds projects of MIXED kinds.*
*Read ROOT CLAUDE.md fully before reading this. Read this fully before any project files.*

---

## WHAT THIS WORKSTATION IS FOR

*(Example.)* A domain for the things that support your other work — references you consult, references you
study, and a tool you're building. Its purpose here is to demonstrate that **a workstation contains projects
of different kinds** (a *kind* is a property of a project, not of a domain). It shows the kinds A/B don't — a
**Reference Repo** and a **Build/Workflow** — and sets a **flat Reference Repo** (`reference-library`,
consult-from) beside a **Reasoning Workspace that synthesizes across reference material** (`reference-study`),
so the *consult* vs *synthesize-across* relationship to the same kind of material is visible in one domain.
(`reference-study` is the live `Reference_Repos` pattern.) It also carries a **Dead** project (`retired-tool`)
to put the second classification axis — **STATE** — on display beside KIND: *state gates structure*, so a
Dead project keeps only a map + one record. *(The matching `Forming`/stub end of the lifecycle is shown by
`Workstation_A_Writing/forming-idea/`.)*

---

## PROJECT MAP

**reference-library** — `Reference Repo (own) · Active`. A knowledge base / template library you *consult
and retrieve from* — you do not reason across it toward conclusions (that relationship would make it a
Reasoning Workspace — see `reference-study` beside it for exactly that contrast). `CLAUDE.md` doubles as the
schema; the body lives in `library/`, indexed.
→ Folder: `reference-library/`

**reference-study** — `Reasoning Workspace (study container) · Active`. A set of reference *sub-projects* you
**synthesize across** — each member a consult-from reference with its own `CLAUDE.md` + `CONTEXT.md`; the
cross-member synthesis is compiled in this project's `CONTEXT.md`. Reasoning *across* the members is what makes
it a Reasoning Workspace, not a Reference Repo — same kind of material as `reference-library`, opposite
relationship. The live `Reference_Repos` pattern. *(Skeleton — members plug in here.)*
→ Folder: `reference-study/`

**build-tool** — `Build / Workflow · Active`. A project whose purpose is to **produce running code /
artifacts**. Its project tier is a *reasoning shell* (this standard); its body (`stages/`) is pipeline-ICM.
This is the kind to use when you wrap ICM around an actual codebase.
→ Folder: `build-tool/`

**retired-tool** — `Reference Repo (own) · Dead`. A finished, retired utility kept only as a static reference
record — the **Dead / own-reference** case. Here to show the *other* axis, **STATE**: a Dead project sheds
`CONTEXT.md`, `references/`, and `_reasoning-log/`, keeping only a map + one record (*state gates structure*).
Contrast `reference-library` (own-reference, **Active**) and `build-tool` (Build/Workflow, **Active**) — same
families, opposite end of the lifecycle.
→ Folder: `retired-tool/`

---

## ROUTING TABLE

| Task | Navigate to | Load | Skip |
|---|---|---|---|
| Look something up / retrieve one entry | reference-library/ | its CLAUDE.md + `library/index.md` | the others |
| Study or synthesize across reference materials | reference-study/ | its CLAUDE.md + CONTEXT.md → the member(s) | the others |
| Design or build the tool | build-tool/ | its CLAUDE.md + CONTEXT.md → its references/ + stages/ | the others |
| Look up what a retired tool did | retired-tool/ | its CLAUDE.md + build-record.md | the others |

---

## NAVIGATION SEQUENCE

1. ROOT CLAUDE.md (done) → 2. ROOT CONTEXT.md → 3. this file → 4. Workbench CONTEXT.md →
5. the relevant project's files → 6. begin work.
