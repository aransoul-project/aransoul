#!/usr/bin/env python3
"""EXPLORATORY — NOT PREREGISTERED CONFIRMATORY ANALYSIS.

Aggregate structural set-difference taxonomy for authority selections only.
No free-text answer fields are read or used.
"""

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CANDIDATES = ROOT / "candidates"
FREEZE_MANIFEST = ROOT / "FREEZE-MANIFEST.json"
CONDITIONS = ["plain", "timestamp", "status", "ttea"]
CASE_IDS = [f"ZH-{index:02d}" for index in range(1, 25)]
REPLICATIONS = ["replication-1", "replication-2", "replication-3"]
TAXONOMY = ["under_selection", "over_selection", "mixed_selection", "empty_prediction", "other"]


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def accepted_metadata():
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
            "family": candidate["family"],
            "gold_authority": set(candidate["gold"]["current_authority_record_ids"]),
        }
    return result


def load_replication(path, replication):
    rows = []
    with Path(path).open("r", encoding="utf-8") as stream:
        for line in stream:
            if line.strip():
                record = json.loads(line)
                if record.get("parse_status") != "parsed":
                    raise ValueError(f"{replication} contains a non-parsed response")
                rows.append(record)
    if len(rows) != 96:
        raise ValueError(f"{replication} expected 96 rows, got {len(rows)}")
    pairs = {(row.get("case_id"), row.get("condition")) for row in rows}
    expected = {(case_id, condition) for case_id in CASE_IDS for condition in CONDITIONS}
    if pairs != expected:
        raise ValueError(f"{replication} does not contain exactly one row per case-condition")
    return rows


def classify(predicted, gold):
    missing = gold - predicted
    extra = predicted - gold
    if not missing and not extra:
        return "exact_match"
    if not predicted and gold:
        return "empty_prediction"
    if missing and not extra:
        return "under_selection"
    if extra and not missing:
        return "over_selection"
    if missing and extra:
        return "mixed_selection"
    return "other"


def empty_bucket():
    return {
        "total_responses": 0,
        "exact_matches": 0,
        "failures": 0,
        "taxonomy_counts": {label: 0 for label in TAXONOMY},
    }


def add(bucket, label):
    bucket["total_responses"] += 1
    if label == "exact_match":
        bucket["exact_matches"] += 1
    else:
        bucket["failures"] += 1
        bucket["taxonomy_counts"][label] += 1


def summarize(bucket):
    total = bucket["total_responses"]
    failures = bucket["failures"]
    if not total:
        raise ValueError("cannot summarize an empty bucket")
    return {
        "total_responses": total,
        "total_exact_matches": bucket["exact_matches"],
        "exact_match_rate": bucket["exact_matches"] / total,
        "total_failures": failures,
        "failure_rate": failures / total,
        "error_taxonomy": {
            label: {
                "count": bucket["taxonomy_counts"][label],
                "rate_of_failures": bucket["taxonomy_counts"][label] / failures if failures else 0.0,
                "rate_of_total": bucket["taxonomy_counts"][label] / total,
            }
            for label in TAXONOMY
        },
    }


def analyze(replication_paths):
    metadata = accepted_metadata()
    overall = empty_bucket()
    by_condition = {condition: empty_bucket() for condition in CONDITIONS}
    by_replication = {replication: empty_bucket() for replication in REPLICATIONS}
    families = sorted({entry["family"] for entry in metadata.values()})
    by_family = {family: empty_bucket() for family in families}

    for replication in REPLICATIONS:
        rows = load_replication(replication_paths[replication], replication)
        for record in rows:
            case_id = record["case_id"]
            condition = record["condition"]
            gold = metadata[case_id]["gold_authority"]
            predicted = set(record["parsed_response"].get("current_authority_record_ids", []))
            label = classify(predicted, gold)
            add(overall, label)
            add(by_condition[condition], label)
            add(by_replication[replication], label)
            add(by_family[metadata[case_id]["family"]], label)

    return {
        "analysis_title": "EXPLORATORY — NOT PREREGISTERED CONFIRMATORY ANALYSIS",
        "analysis_status": "exploratory",
        "taxonomy_method": "set-difference structural taxonomy",
        "semantic_causal_interpretation_performed": False,
        "overall": summarize(overall),
        "taxonomy_by_condition": {key: summarize(value) for key, value in by_condition.items()},
        "taxonomy_by_replication": {key: summarize(value) for key, value in by_replication.items()},
        "taxonomy_by_family": {key: summarize(value) for key, value in by_family.items()},
        "exact_match_by_condition": {
            key: {
                "count": value["exact_matches"],
                "rate": value["exact_matches"] / value["total_responses"],
            }
            for key, value in by_condition.items()
        },
        "exact_match_by_replication": {
            key: {
                "count": value["exact_matches"],
                "rate": value["exact_matches"] / value["total_responses"],
            }
            for key, value in by_replication.items()
        },
        "exact_match_by_family": {
            key: {
                "count": value["exact_matches"],
                "rate": value["exact_matches"] / value["total_responses"],
            }
            for key, value in by_family.items()
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--replication-1", required=True)
    parser.add_argument("--replication-2", required=True)
    parser.add_argument("--replication-3", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    result = analyze({
        "replication-1": args.replication_1,
        "replication-2": args.replication_2,
        "replication-3": args.replication_3,
    })
    Path(args.output).write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
