#!/usr/bin/env python3
"""Freeze a deterministic exploratory authority-error sample manifest.

This sampling phase reads only frozen family/gold authority metadata and
predicted authority IDs. It does not inspect record contents or free-text
model answers.
"""

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CANDIDATES = ROOT / "candidates"
FREEZE_MANIFEST = ROOT / "FREEZE-MANIFEST.json"
CASE_IDS = [f"ZH-{index:02d}" for index in range(1, 25)]
REPLICATIONS = ["replication-1", "replication-2", "replication-3"]
STRATA = [
    "Temporary rule with expiry/restoration",
    "Scoped exception vs general rule",
    "condition=ttea",
]


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def accepted_metadata():
    versions = load_json(FREEZE_MANIFEST)["accepted_versions"]
    if set(versions) != set(CASE_IDS):
        raise ValueError("accepted versions do not cover exactly ZH-01..ZH-24")
    result = {}
    for case_id in CASE_IDS:
        version = int(versions[case_id])
        path = CANDIDATES / case_id / "candidate.json"
        if version != 1:
            path = CANDIDATES / case_id / "versions" / f"v{version}" / "candidate.json"
        candidate = load_json(path)
        result[case_id] = {
            "family": candidate["family"],
            "gold": set(candidate["gold"]["current_authority_record_ids"]),
        }
    return result


def load_rows(path, replication):
    rows = []
    with Path(path).open("r", encoding="utf-8") as stream:
        for line in stream:
            if line.strip():
                record = json.loads(line)
                if record.get("parse_status") != "parsed":
                    raise ValueError(f"{replication} contains a non-parsed row")
                rows.append(record)
    if len(rows) != 96:
        raise ValueError(f"{replication} expected 96 rows, got {len(rows)}")
    return rows


def stratum_matches(item, stratum):
    if stratum == "condition=ttea":
        return item["condition"] == "ttea"
    return item["family"] == stratum


def deterministic_sample(replication_paths):
    metadata = accepted_metadata()
    failures = []
    for replication in REPLICATIONS:
        for record in load_rows(replication_paths[replication], replication):
            case_id = record["case_id"]
            predicted = set(record["parsed_response"].get("current_authority_record_ids", []))
            gold = metadata[case_id]["gold"]
            missing = gold - predicted
            extra = predicted - gold
            if extra and not missing:
                failures.append({
                    "replication": replication,
                    "case_id": case_id,
                    "condition": record["condition"],
                    "frozen_family": metadata[case_id]["family"],
                    "family": metadata[case_id]["family"],
                })

    failures.sort(key=lambda item: (item["case_id"], item["condition"], item["replication"]))
    selected = []
    used_pairs = set()
    for stratum in STRATA:
        eligible = [item for item in failures if stratum_matches(item, stratum)]
        stratum_selected = []
        for replication in REPLICATIONS:
            match = next(
                (
                    item for item in eligible
                    if item["replication"] == replication
                    and (item["case_id"], item["condition"]) not in used_pairs
                ),
                None,
            )
            if match is not None:
                stratum_selected.append(match)
                used_pairs.add((match["case_id"], match["condition"]))
        for item in eligible:
            if len(stratum_selected) >= 6:
                break
            pair = (item["case_id"], item["condition"])
            if pair not in used_pairs:
                stratum_selected.append(item)
                used_pairs.add(pair)
        selected.extend(stratum_selected)

    return [
        {
            "replication": item["replication"],
            "case_id": item["case_id"],
            "condition": item["condition"],
            "frozen_family": item["frozen_family"],
        }
        for item in selected
    ]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--replication-1", required=True)
    parser.add_argument("--replication-2", required=True)
    parser.add_argument("--replication-3", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    manifest = deterministic_sample({
        "replication-1": args.replication_1,
        "replication-2": args.replication_2,
        "replication-3": args.replication_3,
    })
    Path(args.output).write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({"sampled_unique_failures": len(manifest)}, indent=2))


if __name__ == "__main__":
    main()
