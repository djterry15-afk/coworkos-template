# CLAUDE.md
*Workstation: Library / Tooling — an EXAMPLE domain that holds projects of MIXED kinds.*
*Read ROOT CLAUDE.md fully before reading this. Read this fully before any project files.*

---

## WHAT THIS WORKSTATION IS FOR

*(Example.)* A domain for the things that support your other work — a knowledge base you retrieve from, and
a tool you're building. Its purpose here is to demonstrate that **a workstation contains projects of
different kinds** (a *kind* is a property of a project, not of a domain), and to show the two project kinds
that A/B/C don't: a **Reference Repo** and a **Build/Workflow**.

---

## PROJECT MAP

**reference-library** — `Reference Repo (own) · Active`. A knowledge base / template library you *consult
and retrieve from* — you do not reason across it toward conclusions (that relationship would make it a
Reasoning Workspace). `CLAUDE.md` doubles as the schema; the body lives in `library/`, indexed.
→ Folder: `reference-library/`

**build-tool** — `Build / Workflow · Active`. A project whose purpose is to **produce running code /
artifacts**. Its project tier is a *reasoning shell* (this standard); its body (`stages/`) is pipeline-ICM.
This is the kind to use when you wrap ICM around an actual codebase.
→ Folder: `build-tool/`

---

## ROUTING TABLE

| Task | Navigate to | Load | Skip |
|---|---|---|---|
| Look something up / retrieve a template | reference-library/ | its CLAUDE.md + `library/index.md` | build-tool |
| Design or build the tool | build-tool/ | its CLAUDE.md + CONTEXT.md → its references/ + stages/ | reference-library |

---

## NAVIGATION SEQUENCE

1. ROOT CLAUDE.md (done) → 2. ROOT CONTEXT.md → 3. this file → 4. Library CONTEXT.md →
5. the relevant project's files → 6. begin work.
