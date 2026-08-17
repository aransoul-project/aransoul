#!/usr/bin/env python3
"""Fail-closed integrity gate for provider-neutral Zombie Memory responses.jsonl.

This validator checks only structural/integrity properties needed before the
archived Holdout scorer is invoked. It does not inspect gold labels or score
answer quality.
"""

import argparse
import json
from collections import Counter
from pathlib import Path

CONDITIONS = ("plain", "timestamp", "status", "ttea")
CASE_IDS = tuple(f"ZH-{i:02d}" for i in range(1, 25))
EXPECTED_PAIRS = {(case_id, condition) for case_id in CASE_IDS for condition in CONDITIONS}
REQUIRED_PARSED_FIELDS = {
    "id",
    "current_answer",
    "historical_answer",
    "current_authority_record_ids",
}


def fail(message: str):
    raise SystemExit(message)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("responses", type=Path)
    args = parser.parse_args()

    rows = []
    with args.responses.open("r", encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                fail(f"line {line_number}: invalid JSON: {exc}")

            case_id = record.get("case_id")
            condition = record.get("condition")
            parse_status = record.get("parse_status")
            parsed = record.get("parsed_response")

            if case_id not in CASE_IDS:
                fail(f"line {line_number}: unexpected case_id {case_id!r}")
            if condition not in CONDITIONS:
                fail(f"line {line_number}: unexpected condition {condition!r}")
            if parse_status != "parsed":
                fail(f"line {line_number}: parse_status must be 'parsed' before scoring")
            if not isinstance(parsed, dict):
                fail(f"line {line_number}: parsed_response must be an object")
            if set(parsed) != REQUIRED_PARSED_FIELDS:
                fail(f"line {line_number}: parsed_response must contain exactly {sorted(REQUIRED_PARSED_FIELDS)}")
            if parsed.get("id") != case_id:
                fail(f"line {line_number}: parsed_response.id does not match case_id")
            if not isinstance(parsed.get("current_answer"), str) or not parsed["current_answer"].strip():
                fail(f"line {line_number}: current_answer must be a non-empty string")
            if not isinstance(parsed.get("historical_answer"), str) or not parsed["historical_answer"].strip():
                fail(f"line {line_number}: historical_answer must be a non-empty string")
            authority_ids = parsed.get("current_authority_record_ids")
            if not isinstance(authority_ids, list):
                fail(f"line {line_number}: current_authority_record_ids must be a list")
            if len(authority_ids) != len(set(authority_ids)):
                fail(f"line {line_number}: duplicate authority IDs in parsed response")
            if any(not isinstance(value, str) or not value.strip() for value in authority_ids):
                fail(f"line {line_number}: authority IDs must be non-empty strings")

            rows.append((case_id, condition))

    if len(rows) != 96:
        fail(f"expected exactly 96 parsed response rows, found {len(rows)}")

    pair_counts = Counter(rows)
    duplicates = sorted(pair for pair, count in pair_counts.items() if count != 1)
    if duplicates:
        fail(f"each case/condition pair must occur exactly once; invalid pairs: {duplicates[:10]}")

    seen_pairs = set(rows)
    missing = sorted(EXPECTED_PAIRS - seen_pairs)
    unexpected = sorted(seen_pairs - EXPECTED_PAIRS)
    if missing or unexpected:
        fail(f"pair coverage mismatch: missing={missing[:10]} unexpected={unexpected[:10]}")

    by_condition = Counter(condition for _, condition in rows)
    if any(by_condition[condition] != 24 for condition in CONDITIONS):
        fail(f"each condition must contain exactly 24 rows; found {dict(by_condition)}")

    by_case = Counter(case_id for case_id, _ in rows)
    if any(by_case[case_id] != 4 for case_id in CASE_IDS):
        fail("each case must contain exactly four condition rows")

    result = {
        "status": "provider_neutral_integrity_pass",
        "rows": 96,
        "unique_case_condition_pairs": 96,
        "cases": 24,
        "conditions": {condition: by_condition[condition] for condition in CONDITIONS},
        "answers_scored": False,
        "gold_inspected": False,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
