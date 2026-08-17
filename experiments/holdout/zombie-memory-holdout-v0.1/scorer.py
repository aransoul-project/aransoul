from __future__ import annotations

import json
import re
from typing import Any


def _norm_answer(value: Any) -> str:
    if not isinstance(value, str):
        raise ValueError("answer fields must be strings")
    return re.sub(r"\s+", " ", value.strip()).casefold()


def _validate_authority_ids(selected: Any, valid_ids: set[str]) -> list[str]:
    if not isinstance(selected, list) or not all(isinstance(x, str) for x in selected):
        raise ValueError("current_authority_record_ids must be a list of strings")
    if len(selected) != len(set(selected)):
        raise ValueError("duplicate authority record IDs are not allowed")
    unknown = sorted(set(selected) - valid_ids)
    if unknown:
        raise ValueError(f"unknown authority record IDs: {unknown}")
    return selected


def score_case(case: dict[str, Any], submission: dict[str, Any]) -> dict[str, Any]:
    if submission.get("id") != case.get("id"):
        raise ValueError("submission case id does not match gold case id")

    records = case.get("records")
    if not isinstance(records, list) or not records:
        raise ValueError("case records must be a non-empty list")
    valid_ids = {record["id"] for record in records}

    gold = case.get("gold")
    if not isinstance(gold, dict):
        raise ValueError("case gold must be an object")

    selected = _validate_authority_ids(submission.get("current_authority_record_ids"), valid_ids)
    selected_set = set(selected)
    gold_set = set(gold["current_authority_record_ids"])
    stale_set = set(gold.get("stale_record_ids", []))

    return {
        "id": case["id"],
        "current_correct": _norm_answer(submission.get("current_answer")) == _norm_answer(gold["current_answer"]),
        "historical_correct": _norm_answer(submission.get("historical_answer")) == _norm_answer(gold["historical_answer"]),
        "authority_correct": selected_set == gold_set,
        "stale_authority_error": bool(selected_set & stale_set),
        "false_discard": not gold_set.issubset(selected_set),
        "selected_authority_record_ids": sorted(selected_set),
        "gold_authority_record_ids": sorted(gold_set),
    }


def score_cases(cases: list[dict[str, Any]], submissions: list[dict[str, Any]], require_complete: bool = True) -> dict[str, Any]:
    case_by_id = {case["id"]: case for case in cases}
    if len(case_by_id) != len(cases):
        raise ValueError("duplicate gold case IDs")

    sub_by_id: dict[str, dict[str, Any]] = {}
    for sub in submissions:
        case_id = sub.get("id")
        if case_id in sub_by_id:
            raise ValueError(f"duplicate submission case ID: {case_id}")
        if case_id not in case_by_id:
            raise ValueError(f"unknown submission case ID: {case_id}")
        sub_by_id[case_id] = sub

    if require_complete and set(sub_by_id) != set(case_by_id):
        missing = sorted(set(case_by_id) - set(sub_by_id))
        extra = sorted(set(sub_by_id) - set(case_by_id))
        raise ValueError(f"incomplete submission; missing={missing}, extra={extra}")

    per_case = [score_case(case_by_id[case_id], sub_by_id[case_id]) for case_id in sorted(sub_by_id)]
    n = len(per_case)
    if n == 0:
        raise ValueError("no cases scored")

    return {
        "n": n,
        "current_accuracy": sum(row["current_correct"] for row in per_case) / n,
        "historical_accuracy": sum(row["historical_correct"] for row in per_case) / n,
        "authority_exact_set_accuracy": sum(row["authority_correct"] for row in per_case) / n,
        "stale_authority_error_count": sum(row["stale_authority_error"] for row in per_case),
        "false_discard_case_count": sum(row["false_discard"] for row in per_case),
        "per_case": per_case,
    }


def stable_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
