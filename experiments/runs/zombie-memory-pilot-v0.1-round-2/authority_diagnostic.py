#!/usr/bin/env python3
"""Preregistered Round 2 Authority secondary diagnostic.

Execution is gated on explicit raw-data integrity approval and completed frozen
scoring. The diagnostic never replaces or modifies frozen scorer results.
"""

import argparse
import hashlib
import json
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
REPO_ROOT = RUN_DIR.parents[2]
CASES_PATH = REPO_ROOT / "benchmarks/zombie-memory/pilot-v0.1/cases.json"
CONDITIONS = ("plain", "timestamp", "status", "ttea")
NON_AUTHORITATIVE_PHRASES = (
    "non-authoritative",
    "no authority to amend",
    "does not independently set",
)


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def explicitly_non_authoritative(case):
    result = {}
    for record in case["records"]:
        authority = record.get("authority", "")
        if any(phrase in authority.lower() for phrase in NON_AUTHORITATIVE_PHRASES):
            result[record["id"]] = authority
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--raw-integrity-approved", action="store_true")
    parser.add_argument("--scoring-complete", action="store_true")
    args = parser.parse_args()
    if not args.raw_integrity_approved:
        raise SystemExit("Authority diagnostic requires --raw-integrity-approved")
    if not args.scoring_complete:
        raise SystemExit("Authority diagnostic requires --scoring-complete")

    submissions_dir = args.run_dir / "scoring/submissions"
    results_dir = args.run_dir / "scoring/results"
    output_dir = args.run_dir / "scoring/authority-secondary"
    output_dir.mkdir(parents=True, exist_ok=False)
    cases = load_json(CASES_PATH)
    cases_by_id = {case["id"]: case for case in cases}
    analysis_rows = []
    summary_rows = []
    submission_paths = {
        condition: submissions_dir / f"{condition}-submission.json"
        for condition in CONDITIONS
    }

    for condition in CONDITIONS:
        submission = load_json(submission_paths[condition])
        scored = load_json(results_dir / f"{condition}-scorer-output.json")
        details = {row["id"]: row for row in scored["details"]}
        if len(submission) != 10 or len(details) != 10:
            raise ValueError(f"{condition}: expected exactly 10 submission/scorer rows")
        condition_rows = []
        for submitted in submission:
            case = cases_by_id[submitted["id"]]
            gold = set(case["gold"]["current_authority_record_ids"])
            selected = set(submitted.get("current_authority_record_ids", []))
            missing = sorted(gold - selected)
            extra = sorted(selected - gold)
            exact_match = gold == selected
            non_authoritative = explicitly_non_authoritative(case)
            stale_selected = sorted(selected.intersection(case["gold"].get("stale_record_ids", [])))
            non_authoritative_selected = sorted(selected.intersection(non_authoritative))
            row = {
                "condition": condition,
                "case_id": case["id"],
                "family": case["family"],
                "gold_controlling_record_ids": sorted(gold),
                "model_selected_record_ids": sorted(selected),
                "exact_set_scorer_result": details[case["id"]]["authority_correct"],
                "missing_gold_record_ids": missing,
                "extra_selected_record_ids": extra,
                "over_selection": not exact_match and gold.issubset(selected) and bool(extra),
                "omission": bool(missing),
                "wrong_source": bool(missing) and bool(extra),
                "stale_or_non_authoritative_selection": bool(
                    stale_selected or non_authoritative_selected
                ),
                "selected_stale_record_ids": stale_selected,
                "selected_explicitly_non_authoritative_record_ids": non_authoritative_selected,
                "explicitly_non_authoritative_evidence": {
                    rid: non_authoritative[rid] for rid in non_authoritative_selected
                },
            }
            if row["exact_set_scorer_result"] != exact_match:
                raise ValueError(f"{condition}/{case['id']}: exact-set result mismatch")
            condition_rows.append(row)
            analysis_rows.append(row)
        summary_rows.append({
            "condition": condition,
            "cases": 10,
            "exact_set_match_count": sum(row["exact_set_scorer_result"] for row in condition_rows),
            "exact_set_mismatch_count": sum(not row["exact_set_scorer_result"] for row in condition_rows),
            "over_selection_count": sum(row["over_selection"] for row in condition_rows),
            "omission_count": sum(row["omission"] for row in condition_rows),
            "wrong_source_count": sum(row["wrong_source"] for row in condition_rows),
            "stale_or_non_authoritative_selection_count": sum(
                row["stale_or_non_authoritative_selection"] for row in condition_rows
            ),
        })

    status = load_json(submission_paths["status"])
    ttea = load_json(submission_paths["ttea"])
    status_by_id = {row["id"]: row for row in status}
    ttea_by_id = {row["id"]: row for row in ttea}
    common = {
        "analysis_status": "preregistered_secondary_diagnostic",
        "raw_data_integrity_approved": True,
        "frozen_scoring_complete": True,
        "scoring_changed": False,
    }
    write_json(output_dir / "authority-error-summary.json", {
        **common,
        "condition_by_error_type": summary_rows,
        "status_ttea_comparison": {
            "byte_identical": submission_paths["status"].read_bytes() == submission_paths["ttea"].read_bytes(),
            "structurally_identical": status == ttea,
            "differing_case_ids": [
                case_id for case_id in status_by_id
                if status_by_id[case_id] != ttea_by_id.get(case_id)
            ],
            "status_submission_sha256": sha256(submission_paths["status"]),
            "ttea_submission_sha256": sha256(submission_paths["ttea"]),
        },
    })
    write_json(output_dir / "authority-error-cases.json", {**common, "cases": analysis_rows})


if __name__ == "__main__":
    main()
