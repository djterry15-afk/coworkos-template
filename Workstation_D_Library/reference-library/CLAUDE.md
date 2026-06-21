# CLAUDE.md — reference-library
*Project: reference-library — Library workstation. Kind · State: **Reference Repo (own) · Active.***
*This file doubles as the **schema** (the reference body's rules), per the Reference-Repo pattern.*
*Read ROOT CLAUDE.md → Library CLAUDE.md before reading this.*

---

## WHAT THIS PROJECT IS

A knowledge base / template library you **consult and retrieve from** — prompts, snippets, checklists,
templates. Your relationship to it is *Layer 3*: you internalize or copy an entry, you do **not** reason
across the collection toward conclusions. That relationship is what makes it a **Reference Repo**, not a
Reasoning Workspace (identical-looking folders can be opposite kinds — classify on the relationship, not the
appearance).

There is **no `CONTEXT.md` synthesis** here — a Reference Repo's `CLAUDE.md` carries the map and the schema,
and the control point is the body's `index.md`. (Compare a Reasoning Workspace, whose center *is* its
`CONTEXT.md` synthesis.)

## WHERE THINGS LIVE

- **`library/index.md`** — the control point: a table of contents, one line per entry. Start here.
- **`library/<entry>.md`** — the entries themselves, by topic.

## SCHEMA (the rules entries obey)

- File names: lowercase-with-hyphens, named for the topic (`prompt-patterns.md`).
- Every entry starts with a one-line **what this is** + **when to use it**.
- Keep entries self-contained and retrievable — an entry should be useful pulled on its own.
- **Update `library/index.md`** whenever you add or rename an entry. The index is the retrieval surface.

## HOW TO RETRIEVE

When you (or the agent) need something here: read `library/index.md` first, pull the one or two relevant
entries, use them. Do not load the whole library.
