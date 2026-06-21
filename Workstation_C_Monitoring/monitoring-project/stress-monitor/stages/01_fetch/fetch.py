"""01_fetch -- pull the manifest's FRED series into a dated raw snapshot.

Deterministic mechanical joint: reads _config/manifest.json, fetches via fredapi,
writes one verbatim CSV per series + provenance.json. Reads nothing but the manifest
and FRED; writes only into 01_fetch/snapshots/<date>/.
"""
import os
import sys
import json
from datetime import date, datetime, timezone
from pathlib import Path

FACTORY_ROOT = Path(__file__).resolve().parents[2]
MANIFEST = FACTORY_ROOT / "_config" / "manifest.json"


def main():
    # Self-contained key handling: load FACTORY_ROOT/.env if present (gitignored),
    # then fall back to a pre-set FRED_API_KEY in the environment.
    try:
        from dotenv import load_dotenv
        load_dotenv(FACTORY_ROOT / ".env")
    except ImportError:
        pass
    api_key = os.environ.get("FRED_API_KEY")
    if not api_key:
        sys.exit("FRED_API_KEY not set. Put it in stress-monitor/.env (see .env.example) "
                 "or the environment. See _config/fetch-rules.md.")
    try:
        from fredapi import Fred
    except ImportError:
        sys.exit("fredapi not installed. Run: pip install -r requirements.txt")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    start = manifest.get("history_start", "2007-01-01")
    run_date = date.today().isoformat()
    snap_dir = FACTORY_ROOT / "stages" / "01_fetch" / "snapshots" / run_date
    snap_dir.mkdir(parents=True, exist_ok=True)

    fred = Fred(api_key=api_key)
    provenance = {
        "run_date": run_date,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "history_start": start,
        "source": "FRED (api.stlouisfed.org)",
        "series": [],
        "failures": [],
    }

    for item in manifest["series"]:
        sid = item["id"]
        try:
            s = fred.get_series(sid, observation_start=start)
            df = s.rename("value").rename_axis("date").reset_index()
            df.to_csv(snap_dir / f"{sid}.csv", index=False)
            provenance["series"].append({
                "id": sid,
                "label": item.get("label", sid),
                "rows": int(len(df)),
                "first": str(df["date"].min().date()) if len(df) else None,
                "last": str(df["date"].max().date()) if len(df) else None,
                "url": f"https://fred.stlouisfed.org/series/{sid}",
            })
            print(f"fetched {sid}: {len(df)} rows")
        except Exception as exc:  # failed capture -> exclude, never fake
            provenance["failures"].append({"id": sid, "error": str(exc)})
            print(f"FAILED {sid}: {exc}")

    (snap_dir / "provenance.json").write_text(
        json.dumps(provenance, indent=2), encoding="utf-8"
    )
    print(f"snapshot -> {snap_dir.relative_to(FACTORY_ROOT)}")
    if provenance["failures"]:
        print(f"NOTE: {len(provenance['failures'])} series failed and are excluded.")


if __name__ == "__main__":
    main()
