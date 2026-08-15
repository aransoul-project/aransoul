#!/usr/bin/env python3
"""Create scorer-compatible submissions after raw-data integrity approval.

This adapter never reads cases.json or gold and never invokes scorer.py.
"""

import argparse
import json
from pathlib import Path


CONDITIONS = ("plain", "timestamp", "status", "ttea")
FIELDS = ("id", "current_answer", "historical_answer", "current_authority_record_ids")


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--raw-integrity-approved", action="store_true")
    args = parser.parse_args()
    if not args.raw_integrity_approved:
        raise SystemExit("submission creation requires --raw-integrity-approved")

    records = [
        json.loads(line)
        for line in (args.run_dir / "responses.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if len(records) != 40 or any(row["attempt"] != 1 for row in records):
        raise ValueError("expected exactly 40 single-attempt response records")
    output_dir = args.run_dir / "scoring/submissions"
    output_dir.mkdir(parents=True, exist_ok=False)
    for condition in CONDITIONS:
        condition_rows = [row for row in records if row["condition"] == condition]
        if len(condition_rows) != 10:
            raise ValueError(f"{condition}: expected exactly 10 records")
        submission = []
        for row in condition_rows:
            if row["parse_status"] == "parsed":
                submission.append({field: row["parsed_response"][field] for field in FIELDS})
            else:
                submission.append({"id": row["case_id"]})
        write_json(output_dir / f"{condition}-submission.json", submission)


if __name__ == "__main__":
    main()
