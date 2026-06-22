---
name: web-capture
description: Deterministic capture of paginated / gated web content into raw markdown + JSON for later LLM triage. No LLM in the capture loop.
trigger: A corpus of web content (post history, article archive, gated community content) needs to get into files for analysis. Invoke when capture volume makes manual paste tedious and agent-browsing too token-heavy.
tier: ROOT
location: 00_Resources/references/skills/web-capture.SKILL.md
---

# Web Capture
*(Example skill.) The deterministic procedure for getting a web corpus into files. The durable asset is the
procedure; any script written from it is disposable — it rots when the site's frontend changes, and that's
fine. Used by the research-factory's `01_source` stage as the capture tool for gated / JS-heavy sources.*

## Principle

Spend intelligence designing, run determinism forever. The LLM's job is to
discover the site's structure once and freeze it into a disposable script.
The script does the repetition at zero tokens. The LLM re-enters only for
judgment (triage, distillation). Never leave an LLM in a loop a script could run.

## The Procedure

1. **Connect to a real browser, don't fight auth.** Launch Chrome with
   `--remote-debugging-port=9222 --user-data-dir=<dedicated dir>` and connect
   via Playwright `connect_over_cdp`. Chrome 136+ blocks debugging on the
   default profile — a dedicated profile dir is required; log in once there if
   the content needs it. The script inherits the session; no credentials in code.

2. **Check for `__NEXT_DATA__` before parsing DOM.** Next.js sites (and many
   others) embed the full structured data as JSON in
   `<script id="__NEXT_DATA__">`. The JSON usually has MORE than the rendered
   page (full text behind "See more" folds, timestamps).
   If present, the JSON is the source of truth; rendered text is the fallback.
   **Verify what the payload actually contains before assuming scope** — a
   common gotcha: comment threads are often NOT in `__NEXT_DATA__` (some
   platforms ship only comment *counts* in the payload and load the threads via
   a separate API call), so capturing them means intercepting that call or
   expanding threads in-page — a different script. Likewise, authenticated file
   attachments are usually not script-capturable — manual browser download is
   the step, by design.

3. **Dump raw first, parse separately.** The capture script saves everything
   (raw JSON per page + rendered text) and parses nothing. A second script
   parses the dumps into clean markdown. When parsing reveals a problem
   (truncation, missing fields), you re-run the parser — not the capture.

4. **Make capture observable and survivable.** Save a manifest of every URL
   with status. Stop pagination when a page yields nothing new (handles
   unknown page counts and wrong pagination params visibly). Retry navigation
   per page; skip and log on failure — one bad page must not kill the run.
   Avoid `networkidle` waits (modern sites never go idle); wait for
   DOM-ready + the data payload selector.

5. **Be polite, stay one-time.** 1.5s+ between navigations. The script is
   disposable — the durable asset is this procedure, not any script.

## Output Convention

`_capture/` folder in the relevant project: scripts + `raw_dump/` (listing
pages, `posts/` rendered, `posts_full/` parsed, `manifest.json`). Raw dumps are
reasoning history, never treated as distilled state. Delete `_capture/` once
distillation is complete, or keep `raw_dump/` if the corpus has reference value.

## Boundaries

- Per-site work is rediscovered each time: pagination scheme, link filter,
  JSON paths. The recipe transfers; the selectors don't.
- Gated/membership content: capturing your own paid-for reading for personal
  analysis is low-risk but technically gray against most platforms' ToS —
  name it, keep it personal-use, don't redistribute dumps.
- This skill covers CAPTURE only. Triage and distillation are judgment work —
  a separate step with separate criteria, LLM-appropriate.
