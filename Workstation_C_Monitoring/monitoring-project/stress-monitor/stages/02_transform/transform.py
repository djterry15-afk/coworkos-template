"""02_transform -- compute current readings + historical context from the snapshot.

Pure deterministic function of the latest 01_fetch snapshot. No network, no judgment.
Reads _config/manifest.json for metric definitions; writes 02_transform/computed/<date>.json.
"""
import sys
import json
from pathlib import Path

FACTORY_ROOT = Path(__file__).resolve().parents[2]
MANIFEST = FACTORY_ROOT / "_config" / "manifest.json"


def _latest_snapshot_dir():
    base = FACTORY_ROOT / "stages" / "01_fetch" / "snapshots"
    dirs = sorted([p for p in base.iterdir() if p.is_dir()]) if base.exists() else []
    if not dirs:
        sys.exit("No snapshot found. Run stages/01_fetch/fetch.py first.")
    return dirs[-1]


def main():
    import pandas as pd

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    windows = manifest.get("stress_windows", {})
    snap_dir = _latest_snapshot_dir()
    run_date = snap_dir.name

    def load(sid):
        f = snap_dir / f"{sid}.csv"
        if not f.exists():
            return None
        df = pd.read_csv(f, parse_dates=["date"]).dropna(subset=["value"])
        df = df.sort_values("date").reset_index(drop=True)
        return df if len(df) else None

    def series_for(defn):
        if defn["type"] == "series":
            return load(defn["id"])
        if defn["type"] == "spread":
            a, b = load(defn["minuend"]), load(defn["subtrahend"])
            if a is None or b is None:
                return None
            m = pd.merge(a, b, on="date", suffixes=("_a", "_b"))
            if not len(m):
                return None
            m["value"] = m["value_a"] - m["value_b"]
            return m[["date", "value"]].reset_index(drop=True)
        return None

    def asof(df, target):
        prior = df[df["date"] <= target]
        if not len(prior):
            return None
        r = prior.iloc[-1]
        return round(float(r["value"]), 4)

    def window_peak(df, win):
        if win not in windows:
            return None
        s, e = windows[win]
        m = df[(df["date"] >= pd.Timestamp(s)) & (df["date"] <= pd.Timestamp(e))]
        if not len(m):
            return None
        r = m.loc[m["value"].idxmax()]
        return {"date": str(r["date"].date()), "value": round(float(r["value"]), 4)}

    def compute(defn):
        df = series_for(defn)
        if df is None:
            return {"key": defn["key"], "label": defn["label"], "available": False}
        last = df.iloc[-1]
        last_date = last["date"]
        cur = round(float(last["value"]), 4)
        wk = asof(df, last_date - pd.Timedelta(days=7))
        mo = asof(df, last_date - pd.Timedelta(days=30))
        return {
            "key": defn["key"],
            "label": defn["label"],
            "available": True,
            "units": defn.get("units"),
            "direction": defn.get("direction"),
            "latest": {"date": str(last_date.date()), "value": cur},
            "change_1w": None if wk is None else round(cur - wk, 4),
            "change_1m": None if mo is None else round(cur - mo, 4),
            "percentile": round(100.0 * (df["value"] <= cur).sum() / len(df), 1),
            "history_start": str(df["date"].min().date()),
            "window_peaks": {w: window_peak(df, w) for w in defn.get("stress_windows", [])},
        }

    out = {
        "run_date": run_date,
        "snapshot": str(snap_dir.relative_to(FACTORY_ROOT)).replace("\\", "/"),
        "anchor": compute(manifest["composite_anchor"]),
        "components": [compute(c) for c in manifest["components"]],
    }
    dest_dir = FACTORY_ROOT / "stages" / "02_transform" / "computed"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{run_date}.json"
    dest.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"computed -> {dest.relative_to(FACTORY_ROOT)}")


if __name__ == "__main__":
    main()
