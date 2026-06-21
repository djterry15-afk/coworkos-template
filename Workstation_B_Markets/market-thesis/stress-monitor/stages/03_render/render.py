"""03_render -- render the dashboard markdown from the computed readings.

Deterministic formatter. Reads the latest 02_transform/computed/<date>.json (the numbers)
and _config/manifest.json (presentation: descriptions, groups); writes
03_render/output/<date>/dashboard.md. No network, no judgment, no numbers of its own.

Output = a grouped plain-language explanation section (legible to a non-quant) ABOVE a
compact table (visual reference). Positioning is described relative to each metric's OWN
history -- never an absolute signal or verdict.
"""
import sys
import json
from pathlib import Path

FACTORY_ROOT = Path(__file__).resolve().parents[2]
MANIFEST = FACTORY_ROOT / "_config" / "manifest.json"


def _latest_computed():
    base = FACTORY_ROOT / "stages" / "02_transform" / "computed"
    files = sorted(base.glob("*.json")) if base.exists() else []
    if not files:
        sys.exit("No computed file found. Run stages/02_transform/transform.py first.")
    return files[-1]


def num(v):
    return "—" if v is None else f"{v:.2f}"


def delta(v):
    return "—" if v is None else f"{v:+.2f}"


def peak(p):
    return "—" if not p else f"{p['value']:.2f} ({p['date']})"


def position_phrase(pct):
    """Verbalize where the latest reading sits within the metric's own history."""
    if pct is None:
        return "position unknown in"
    if pct < 10:
        return "near the LOW of"
    if pct < 40:
        return "below the middle of"
    if pct <= 60:
        return "around the middle of"
    if pct < 90:
        return "above the middle of"
    return "near the HIGH end of"


def main():
    data = json.loads(_latest_computed().read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    pres = {manifest["composite_anchor"]["key"]: manifest["composite_anchor"]}
    for c in manifest["components"]:
        pres[c["key"]] = c

    run_date = data["run_date"]
    a = data["anchor"]
    notes = []

    L = [
        f"# Market-Stress Monitor — {run_date}",
        "",
        f"*Readings + context, **not** a signal. Snapshot: `{data['snapshot']}`. "
        f"The thesis call stays in the parent market-thesis project `CONTEXT.md`.*",
        "",
        "## Overall conditions",
        "",
    ]
    apres = pres.get(a["key"], {})
    if a.get("available"):
        L += [
            f"**{a['label']}** — **{num(a['latest']['value'])}** ({a['latest']['date']})",
            f"- *{apres.get('description', '')}*",
            f"- Sits **{position_phrase(a['percentile'])} its history** "
            f"(since {a['history_start']}; {a['percentile']}%ile). "
            f"GFC peak {peak(a['window_peaks'].get('GFC'))}, "
            f"COVID peak {peak(a['window_peaks'].get('COVID'))}.",
            f"- Change: {delta(a['change_1w'])} (1w) · {delta(a['change_1m'])} (1m)",
            "",
        ]
    else:
        L += [f"**{a['label']}** — unavailable this run (fetch failed).", ""]
        notes.append(f"- Anchor `{a['label']}` excluded (fetch failed).")

    # --- grouped plain-language explanations (primary layer) ---
    L += ["## What the metrics say", ""]
    comps_by_key = {c["key"]: c for c in data["components"]}
    seen_groups = []
    for mc in manifest["components"]:
        grp = mc.get("group", "Other")
        if grp not in seen_groups:
            seen_groups.append(grp)
            L += [f"### {grp}", ""]
        c = comps_by_key.get(mc["key"])
        if not c or not c.get("available"):
            L += [f"- **{mc['label']}** — unavailable this run.", ""]
            notes.append(f"- `{mc['label']}` excluded (fetch failed).")
            continue
        L += [
            f"- **{mc['label']}** — **{num(c['latest']['value'])} {c.get('units', '')}** "
            f"({c['latest']['date']})",
            f"    - *{mc.get('description', '')}*",
            f"    - Sits **{position_phrase(c['percentile'])} its history** "
            f"(since {c['history_start']}; {c['percentile']}%ile). "
            f"Change {delta(c['change_1w'])} (1w) · {delta(c['change_1m'])} (1m).",
            f"    - Stress reference — GFC {peak(c['window_peaks'].get('GFC'))}, "
            f"COVID {peak(c['window_peaks'].get('COVID'))}.",
            "",
        ]
        for w in ("GFC", "COVID"):
            if w in c.get("window_peaks", {}) and c["window_peaks"][w] is None:
                notes.append(
                    f"- `{mc['label']}` has no {w} context (history starts {c['history_start']})."
                )

    # --- compact table (visual reference) ---
    L += [
        "## Table (visual reference)",
        "",
        "| Metric | Latest (date) | 1w Δ | 1m Δ | %ile | GFC peak | COVID peak | dir |",
        "|---|---|---|---|---|---|---|---|",
    ]
    def mlabel(key, fallback):
        return pres.get(key, {}).get("label", fallback)

    if a.get("available"):
        lt = f"{num(a['latest']['value'])} ({a['latest']['date']})"
        L.append(
            f"| {mlabel(a['key'], a['label'])} | {lt} | {delta(a['change_1w'])} "
            f"| {delta(a['change_1m'])} | {a['percentile']}% | {peak(a['window_peaks'].get('GFC'))} "
            f"| {peak(a['window_peaks'].get('COVID'))} | anchor |"
        )
    for c in data["components"]:
        label = mlabel(c["key"], c["label"])
        if not c.get("available"):
            L.append(f"| {label} | unavailable | — | — | — | — | — | — |")
            continue
        lt = f"{num(c['latest']['value'])} ({c['latest']['date']})"
        L.append(
            f"| {label} | {lt} | {delta(c['change_1w'])} | {delta(c['change_1m'])} "
            f"| {c['percentile']}% | {peak(c['window_peaks'].get('GFC'))} "
            f"| {peak(c['window_peaks'].get('COVID'))} | {c.get('direction', '')} |"
        )
    L += [""]

    # --- notes ---
    L += ["## Notes", ""]
    L += sorted(set(notes)) if notes else ["- All metrics available; all context windows covered."]
    L += [
        "",
        "*pp = percentage points · % = percent · index per series. "
        "Position = where the latest reading sits within the metric's OWN history — "
        "not an absolute signal or verdict.*",
    ]

    out_dir = FACTORY_ROOT / "stages" / "03_render" / "output" / run_date
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "dashboard.md"
    dest.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"dashboard -> {dest.relative_to(FACTORY_ROOT)}")


if __name__ == "__main__":
    main()
