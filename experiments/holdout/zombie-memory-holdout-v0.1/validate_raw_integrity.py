#!/usr/bin/env python3
"""Metadata-only integrity validator for Zombie Memory Holdout v0.1 live runs.

This script deliberately does not inspect parsed answers, authority selections,
or raw provider payload content. It validates only request metadata and manifest
consistency before scoring is permitted.
"""

import argparse
import json
from pathlib import Path


CONDITIONS = ("plain", "timestamp", "status", "ttea")
CASE_IDS = tuple(f"ZH-{i:02d}" for i in range(1, 25))
EXPECTED_SEQUENCE = tuple((case_id, condition) for case_id in CASE_IDS for condition in CONDITIONS)


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir", type=Path)
    args = parser.parse_args()

    manifest_path = args.run_dir / "manifest.json"
    responses_path = args.run_dir / "responses.jsonl"
    manifest = load_json(manifest_path)

    required_manifest = {
        "mode": "live",
        "api_called": True,
        "status": "responses_complete_unreviewed",
        "request_count_expected": 96,
        "request_count_recorded": 96,
        "parsed_count": 96,
        "parse_failure_count": 0,
        "request_failure_count": 0,
        "retry_count": 0,
        "scoring_started": False,
    }
    for key, expected in required_manifest.items():
        actual = manifest.get(key)
        if actual != expected:
            raise SystemExit(f"manifest mismatch: {key} expected {expected!r}, found {actual!r}")

    seen = []
    indices = []
    with responses_path.open("r", encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            record = json.loads(line)
            # Intentionally read only non-answer metadata fields.
            if record.get("mode") != "live":
                raise SystemExit(f"line {line_number}: mode is not live")
            if record.get("attempt") != 1:
                raise SystemExit(f"line {line_number}: attempt is not 1")
            if record.get("parse_status") != "parsed":
                raise SystemExit(f"line {line_number}: parse_status is not parsed")
            if record.get("model") != manifest.get("model"):
                raise SystemExit(f"line {line_number}: model mismatch")
            seen.append((record.get("case_id"), record.get("condition")))
            indices.append(record.get("request_index"))

    if len(seen) != 96:
        raise SystemExit(f"expected 96 response rows, found {len(seen)}")
    if tuple(seen) != EXPECTED_SEQUENCE:
        raise SystemExit("case/condition sequence differs from frozen case-major order")
    if len(set(seen)) != 96:
        raise SystemExit("duplicate case/condition pair detected")
    if indices != list(range(1, 97)):
        raise SystemExit("request_index is not exactly 1..96 in order")

    result = {
        "status": "raw_data_integrity_pass",
        "rows": 96,
        "unique_case_condition_pairs": 96,
        "ordering": "case-major_then_condition-fixed",
        "attempts": "all_1",
        "request_indices": "1..96",
        "mode": "live",
        "api_called": True,
        "answers_inspected": False,
        "scoring_started": False,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
