#!/usr/bin/env python3
"""Deterministic scorer for Zombie Memory Benchmark pilot v0.1.

Usage:
    python scorer.py cases.json submission.json

The scorer intentionally evaluates only fields with explicit gold labels.
It does not use an LLM judge.
"""

import json
import sys
from pathlib import Path


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def norm_answer(value):
    return str(value).strip().upper()


def norm_ids(values):
    return sorted(str(v).strip() for v in (values or []))


def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python scorer.py cases.json submission.json")

    cases = load(sys.argv[1])
    submission = load(sys.argv[2])
    submitted = {row["id"]: row for row in submission}

    totals = {
        "cases": len(cases),
        "current_correct": 0,
        "historical_correct": 0,
        "authority_correct": 0,
        "stale_authority_errors": 0,
        "false_discard_cases": 0,
    }
    details = []

    for case in cases:
        cid = case["id"]
        gold = case["gold"]
        row = submitted.get(cid, {})

        current_ok = norm_answer(row.get("current_answer", "")) == norm_answer(gold["current_answer"])
        historical_ok = norm_answer(row.get("historical_answer", "")) == norm_answer(gold["historical_answer"])
        selected = norm_ids(row.get("current_authority_record_ids", []))
        expected = norm_ids(gold["current_authority_record_ids"])
        authority_ok = selected == expected

        if current_ok:
            totals["current_correct"] += 1
        if historical_ok:
            totals["historical_correct"] += 1
        if authority_ok:
            totals["authority_correct"] += 1

        stale = set(norm_ids(gold.get("stale_record_ids", [])))
        stale_error = (not current_ok) and bool(stale.intersection(selected))
        if stale_error:
            totals["stale_authority_errors"] += 1

        required_old = set(norm_ids(gold.get("still_valid_older_record_ids", [])))
        false_discard = bool(required_old) and not required_old.issubset(set(selected))
        if false_discard:
            totals["false_discard_cases"] += 1

        details.append({
            "id": cid,
            "current_correct": current_ok,
            "historical_correct": historical_ok,
            "authority_correct": authority_ok,
            "stale_authority_error": stale_error,
            "false_discard_indicator": false_discard,
        })

    n = totals["cases"] or 1
    result = {
        "summary": {
            "cases": totals["cases"],
            "current_answer_accuracy": totals["current_correct"] / n,
            "historical_recall_accuracy": totals["historical_correct"] / n,
            "authority_resolution_accuracy": totals["authority_correct"] / n,
            "stale_authority_error_count": totals["stale_authority_errors"],
            "false_discard_case_count": totals["false_discard_cases"],
        },
        "details": details,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
