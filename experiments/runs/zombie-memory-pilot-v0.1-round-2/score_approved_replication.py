#!/usr/bin/env python3
"""Run the frozen scorer on approved Round 2 condition submissions."""

import argparse
import json
import subprocess
import sys
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
REPO_ROOT = RUN_DIR.parents[2]
SCORER = REPO_ROOT / "benchmarks/zombie-memory/pilot-v0.1/scorer.py"
CASES = REPO_ROOT / "benchmarks/zombie-memory/pilot-v0.1/cases.json"
CONDITIONS = ("plain", "timestamp", "status", "ttea")


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--raw-integrity-approved", action="store_true")
    args = parser.parse_args()
    if not args.raw_integrity_approved:
        raise SystemExit("frozen scoring requires --raw-integrity-approved")
    manifest = load_json(args.run_dir / "manifest.json")
    if manifest.get("raw_data_integrity_approved") is not True:
        raise ValueError("run manifest is not raw-data-integrity approved")

    submissions_dir = args.run_dir / "scoring/submissions"
    results_dir = args.run_dir / "scoring/results"
    results_dir.mkdir(parents=True, exist_ok=False)
    summary = {
        "run_id": manifest["run_id"],
        "replication": manifest["replication"],
        "scorer": str(SCORER.relative_to(REPO_ROOT)).replace("\\", "/"),
        "raw_data_integrity_approved": True,
        "conditions": {},
    }
    for condition in CONDITIONS:
        submission_path = submissions_dir / f"{condition}-submission.json"
        submission = load_json(submission_path)
        if len(submission) != 10:
            raise ValueError(f"{condition}: expected exactly 10 submission rows")
        completed = subprocess.run(
            [sys.executable, str(SCORER), str(CASES), str(submission_path)],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        output = json.loads(completed.stdout)
        write_json(results_dir / f"{condition}-scorer-output.json", output)
        summary["conditions"][condition] = output["summary"]
    write_json(results_dir / "summary.json", summary)


if __name__ == "__main__":
    main()
