#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

CONDITIONS = ("plain", "timestamp", "status", "ttea")
STATUS_LABELS = {"current", "superseded", "partial", "candidate", "historical", "revoked"}


def load_cases(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def render_record(record, condition):
    lines = [f"[{record['id']}] {record['text']}"]
    if condition in ("timestamp", "ttea"):
        lines.append(f"Time: {record['time']}")
    if condition == "status":
        if record["effect"] not in STATUS_LABELS:
            raise ValueError(f"unsupported effect-only status: {record['effect']}")
        lines.append(f"Status: {record['effect'].upper()}")
    if condition == "ttea":
        lines.extend([
            f"Truth: {record['truth']}",
            f"Effect: {record['effect']}",
            f"Authority: {record['authority']}",
        ])
    return "\n".join(lines)


def render_case(case, condition):
    records = "\n\n".join(render_record(r, condition) for r in case["records"])
    return {
        "id": case["id"],
        "family": case["family"],
        "condition": condition,
        "prompt": (
            "Read the records and answer both questions. Also identify the record IDs that currently control the answer.\n\n"
            + records
            + "\n\nCurrent question: " + case["current_question"]
            + "\nHistorical question: " + case["historical_question"]
            + "\nReturn JSON with id, current_answer, historical_answer, current_authority_record_ids."
        ),
    }


def assert_no_leakage(case, rendered):
    """Reject benchmark-only annotations in a model-facing prompt."""
    prompt = rendered["prompt"]
    gold = case["gold"]
    forbidden_labels = (
        "gold",
        "stale_record_ids",
        "stale record ids",
        "still_valid_older_record_ids",
        "still valid older record ids",
        "historical_record_ids",
        "historical record ids",
    )
    lowered = prompt.lower()
    leaked_labels = [label for label in forbidden_labels if label in lowered]
    if leaked_labels:
        raise ValueError(f"{case['id']}: forbidden annotation label(s): {', '.join(leaked_labels)}")

    answer_patterns = (
        rf"current[_ ]answer\s*[:=]\s*[\"']?{re.escape(str(gold['current_answer']))}\b",
        rf"historical[_ ]answer\s*[:=]\s*[\"']?{re.escape(str(gold['historical_answer']))}\b",
    )
    if any(re.search(pattern, prompt, flags=re.IGNORECASE) for pattern in answer_patterns):
        raise ValueError(f"{case['id']}: gold answer leaked into prompt")

    controlling_pattern = r"current[_ ](?:authority|controlling(?:[-_ ]source)?)[-_ ]record[_ ]ids?\s*[:=]"
    if re.search(controlling_pattern, prompt, flags=re.IGNORECASE):
        raise ValueError(f"{case['id']}: current controlling-source gold labels leaked into prompt")

    # Canonical record IDs must occur in their record headers, but nowhere else.
    for record in case["records"]:
        record_id = record["id"]
        if len(re.findall(rf"(?<!\w){re.escape(record_id)}(?!\w)", prompt)) != 1:
            raise ValueError(f"{case['id']}: record ID {record_id} appears outside its canonical header")


def assert_equivalent(cases, rendered_by_condition):
    """Verify required canonical identity fields across all four views."""
    expected_ids = [case["id"] for case in cases]
    if len(cases) != 10 or len(set(expected_ids)) != 10:
        raise ValueError("pilot-v0.1 requires exactly 10 cases with unique IDs")

    for condition in CONDITIONS:
        rendered = rendered_by_condition[condition]
        if len(rendered) != 10:
            raise ValueError(f"{condition}: expected 10 rendered cases, found {len(rendered)}")
        if [row["id"] for row in rendered] != expected_ids:
            raise ValueError(f"{condition}: case IDs differ from canonical cases.json")

        for case, row in zip(cases, rendered):
            if row["family"] != case["family"]:
                raise ValueError(f"{condition}/{case['id']}: family differs from canonical cases.json")
            prompt = row["prompt"]
            rendered_record_ids = re.findall(r"^\[([^\]]+)\] ", prompt, flags=re.MULTILINE)
            canonical_record_ids = [record["id"] for record in case["records"]]
            if rendered_record_ids != canonical_record_ids:
                raise ValueError(f"{condition}/{case['id']}: record IDs differ from canonical cases.json")
            if f"Current question: {case['current_question']}" not in prompt:
                raise ValueError(f"{condition}/{case['id']}: current question differs from canonical cases.json")
            if f"Historical question: {case['historical_question']}" not in prompt:
                raise ValueError(f"{condition}/{case['id']}: historical question differs from canonical cases.json")
            assert_no_leakage(case, row)


def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python renderer.py cases.json output_dir")
    cases = load_cases(sys.argv[1])
    out = Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    rendered_by_condition = {}
    for condition in CONDITIONS:
        rendered_by_condition[condition] = [render_case(c, condition) for c in cases]

    assert_equivalent(cases, rendered_by_condition)

    for condition, rendered in rendered_by_condition.items():
        (out / f"{condition}.json").write_text(json.dumps(rendered, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
