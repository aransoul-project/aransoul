#!/usr/bin/env python3
"""Create condition submissions and run the frozen scorer for one live run."""

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
SUBMISSION_FIELDS = (
    "id",
    "current_answer",
    "historical_answer",
    "current_authority_record_ids",
)


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, value):
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("run_id")
    parser.add_argument("--scoring-id", default="first-scoring")
    args = parser.parse_args()

    live_dir = RUN_DIR / "outputs/live" / args.run_id
    responses_path = live_dir / "responses.jsonl"
    records = [
        json.loads(line)
        for line in responses_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if len(records) != 40:
        raise ValueError(f"expected exactly 40 response records, found {len(records)}")

    output_dir = live_dir / "scoring" / args.scoring_id
    output_dir.mkdir(parents=True, exist_ok=False)
    summary = {
        "run_id": args.run_id,
        "scoring_id": args.scoring_id,
        "scorer": str(SCORER.relative_to(REPO_ROOT)).replace("\\", "/"),
        "conditions": {},
    }

    for condition in CONDITIONS:
        condition_records = [row for row in records if row["condition"] == condition]
        if len(condition_records) != 10:
            raise ValueError(
                f"{condition}: expected exactly 10 response records, "
                f"found {len(condition_records)}"
            )
        if any(row["parse_status"] != "parsed" for row in condition_records):
            raise ValueError(f"{condition}: contains a non-parsed response")

        submission = [
            {field: row["parsed_response"][field] for field in SUBMISSION_FIELDS}
            for row in condition_records
        ]
        submission_path = output_dir / f"{condition}-submission.json"
        scorer_path = output_dir / f"{condition}-scorer-output.json"
        write_json(submission_path, submission)

        completed = subprocess.run(
            [sys.executable, str(SCORER), str(CASES), str(submission_path)],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        scorer_output = json.loads(completed.stdout)
        write_json(scorer_path, scorer_output)
        summary["conditions"][condition] = scorer_output["summary"]

    write_json(output_dir / "summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
