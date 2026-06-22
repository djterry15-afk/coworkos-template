# recipe.md — the build's recipe (L3, configure-the-factory input)
*The settled constraints/conventions the code obeys, handed down from the reasoning shell to the body.*
*(Example — a markdown link-checker CLI. Replace with your build's real spec.)*

---

- **What it builds:** `linkcheck`, a small command-line tool that scans a folder of markdown and reports
  relative links — `[text](path)` — whose target file does not exist. Exits non-zero when any link is
  broken, so it can run in CI.
- **Conventions the code obeys:** Python 3, **standard library only** (no third-party deps); one core module
  + a thin CLI entrypoint; the link extraction/resolution core is **pure functions** (text + base path in,
  results out) so it is unit-testable without the filesystem; every public function typed.
- **Hard constraints:** **read-only** — it never edits the files it scans (reports, never fixes). Resolves
  each link relative to its *own file's* directory — the exact bug class it exists to catch. Output is
  deterministic (sorted), so a CI diff is stable.
- **Out of scope (v1):** external `http(s)://` URLs, `[[wikilinks]]`, and anchor fragments (`#section`).
  Listed here so the boundary is explicit, not forgotten — a later version may earn them.

*This is the "configure once" intelligence: decided here in reasoning mode, then obeyed by the body during
production. Keep it to settled rules; unsettled exploration stays in `CONTEXT.md`.*
