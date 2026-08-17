#!/usr/bin/env python3
"""Aggregate-only semantic scoring for Zombie Memory Holdout v0.1."""

import argparse
import hashlib
import json
from pathlib import Path

from semantic_grader import ALLOWED_LABELS, grade


ROOT = Path(__file__).resolve().parent
CANDIDATES = ROOT / "candidates"
FREEZE_MANIFEST = ROOT / "FREEZE-MANIFEST.json"
GRADER_PATH = ROOT / "semantic_grader.py"
FROZEN_GRADER_COMMIT = "52450aca7988ec0377ca889a6d0db4f7c03c77fa"
FROZEN_GRADER_SHA256 = "ae850a560c2072b658a0aaa5dff344e4ab8c321d542d70058a567aefcf60a108"
CONDITIONS = ["plain", "timestamp", "status", "ttea"]
CASE_IDS = [f"ZH-{index:02d}" for index in range(1, 25)]
LABELS = ["equivalent", "not_equivalent", "indeterminate"]


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def verify_frozen_grader():
    actual = hashlib.sha256(GRADER_PATH.read_bytes()).hexdigest()
    if actual != FROZEN_GRADER_SHA256:
        raise ValueError("semantic_grader.py does not match frozen grader commit")


def accepted_gold():
    manifest = load_json(FREEZE_MANIFEST)
    versions = manifest.get("accepted_versions", {})
    if set(versions) != set(CASE_IDS):
        raise ValueError("accepted versions do not cover exactly ZH-01..ZH-24")
    result = {}
    for case_id in CASE_IDS:
        version = int(versions[case_id])
        if version == 1:
            path = CANDIDATES / case_id / "candidate.json"
        else:
            path = CANDIDATES / case_id / "versions" / f"v{version}" / "candidate.json"
        candidate = load_json(path)
        result[case_id] = {
            "current_question": candidate["question"],
            "historical_question": candidate["historical_question"],
            "current_answer": candidate["gold"]["current_answer"],
            "historical_answer": candidate["gold"]["historical_answer"],
        }
    return result


def load_responses(path):
    rows = []
    with Path(path).open("r", encoding="utf-8") as stream:
        for line in stream:
            if line.strip():
                record = json.loads(line)
                if record.get("parse_status") != "parsed":
                    raise ValueError("all semantic-scored rows must be parsed")
                rows.append(record)
    if len(rows) != 96:
        raise ValueError(f"expected 96 responses, got {len(rows)}")
    pairs = {(row.get("case_id"), row.get("condition")) for row in rows}
    expected_pairs = {(case_id, condition) for case_id in CASE_IDS for condition in CONDITIONS}
    if pairs != expected_pairs:
        raise ValueError("responses do not contain exactly one row per case-condition pair")
    return rows


def empty_field_bucket():
    return {label: 0 for label in LABELS}


def empty_bucket():
    return {"responses": 0, "current": empty_field_bucket(), "historical": empty_field_bucket()}


def add(bucket, current_label, historical_label):
    if current_label not in ALLOWED_LABELS or historical_label not in ALLOWED_LABELS:
        raise ValueError("semantic grader returned an invalid label")
    bucket["responses"] += 1
    bucket["current"][current_label] += 1
    bucket["historical"][historical_label] += 1


def summarize_field(counts, total):
    return {
        label: {"count": counts[label], "rate": counts[label] / total}
        for label in LABELS
    }


def summarize(bucket):
    total = bucket["responses"]
    if not total:
        raise ValueError("cannot summarize an empty bucket")
    return {
        "responses": total,
        "current": summarize_field(bucket["current"], total),
        "historical": summarize_field(bucket["historical"], total),
    }


def aggregate_score(responses_path):
    verify_frozen_grader()
    gold = accepted_gold()
    rows = load_responses(responses_path)
    overall = empty_bucket()
    by_condition = {condition: empty_bucket() for condition in CONDITIONS}

    for record in rows:
        case_id = record["case_id"]
        condition = record["condition"]
        parsed = record["parsed_response"]
        canonical = gold[case_id]
        current_label = grade(
            canonical["current_question"],
            canonical["current_answer"],
            parsed.get("current_answer", ""),
        )
        historical_label = grade(
            canonical["historical_question"],
            canonical["historical_answer"],
            parsed.get("historical_answer", ""),
        )
        add(overall, current_label, historical_label)
        add(by_condition[condition], current_label, historical_label)

    if any(bucket["responses"] != 24 for bucket in by_condition.values()):
        raise ValueError("each condition must contain exactly 24 responses")
    return {
        "status": "semantic_aggregate_scoring_complete",
        "measurement": "post-freeze semantic scoring amendment",
        "grader": {
            "frozen_commit": FROZEN_GRADER_COMMIT,
            "sha256": FROZEN_GRADER_SHA256,
        },
        "inspection_level": "aggregate_only_no_individual_details",
        "overall": summarize(overall),
        "by_condition": {condition: summarize(by_condition[condition]) for condition in CONDITIONS},
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--responses", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    result = aggregate_score(args.responses)
    Path(args.output).write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
