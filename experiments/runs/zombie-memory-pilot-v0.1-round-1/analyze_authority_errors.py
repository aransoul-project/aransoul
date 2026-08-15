#!/usr/bin/env python3
"""Post-hoc authority-selection diagnostics for a scored live run."""

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
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def explicitly_non_authoritative(case):
    result = {}
    for record in case["records"]:
        authority = record.get("authority", "")
        lowered = authority.lower()
        if any(phrase in lowered for phrase in NON_AUTHORITATIVE_PHRASES):
            result[record["id"]] = authority
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("run_id")
    parser.add_argument("--scoring-id", default="first-scoring")
    args = parser.parse_args()

    scoring_dir = RUN_DIR / "outputs/live" / args.run_id / "scoring" / args.scoring_id
    cases = load_json(CASES_PATH)
    cases_by_id = {case["id"]: case for case in cases}
    analysis_rows = []
    summary_rows = []

    submissions = {
        condition: scoring_dir / f"{condition}-submission.json"
        for condition in CONDITIONS
    }
    status_submission = load_json(submissions["status"])
    ttea_submission = load_json(submissions["ttea"])
    status_by_id = {row["id"]: row for row in status_submission}
    ttea_by_id = {row["id"]: row for row in ttea_submission}
    differing_case_ids = [
        case_id
        for case_id in status_by_id
        if status_by_id[case_id] != ttea_by_id.get(case_id)
    ]

    for condition in CONDITIONS:
        submission = load_json(submissions[condition])
        scorer_output = load_json(scoring_dir / f"{condition}-scorer-output.json")
        scorer_details = {row["id"]: row for row in scorer_output["details"]}
        if len(submission) != 10 or len(scorer_details) != 10:
            raise ValueError(f"{condition}: expected 10 submission and scorer rows")

        condition_rows = []
        for submitted in submission:
            case_id = submitted["id"]
            case = cases_by_id[case_id]
            gold = set(case["gold"]["current_authority_record_ids"])
            selected = set(submitted["current_authority_record_ids"])
            missing = sorted(gold - selected)
            extra = sorted(selected - gold)
            exact_match = gold == selected
            over_selection = not exact_match and gold.issubset(selected) and bool(extra)
            omission = bool(missing)
            wrong_source = omission and bool(extra)
            stale_selected = sorted(
                selected.intersection(case["gold"].get("stale_record_ids", []))
            )
            non_authoritative = explicitly_non_authoritative(case)
            non_authoritative_selected = sorted(selected.intersection(non_authoritative))
            stale_or_non_authoritative = bool(
                stale_selected or non_authoritative_selected
            )
            error_types = []
            if over_selection:
                error_types.append("over_selection")
            if omission:
                error_types.append("omission")
            if wrong_source:
                error_types.append("wrong_source")

            exact_set_scorer_result = scorer_details[case_id]["authority_correct"]
            if exact_set_scorer_result != exact_match:
                raise ValueError(
                    f"{condition}/{case_id}: diagnostic exact-set result differs "
                    "from frozen scorer output"
                )
            row = {
                "condition": condition,
                "case_id": case_id,
                "family": case["family"],
                "gold_controlling_record_ids": sorted(gold),
                "model_selected_record_ids": sorted(selected),
                "exact_set_scorer_result": exact_set_scorer_result,
                "missing_gold_record_ids": missing,
                "extra_selected_record_ids": extra,
                "error_types": error_types,
                "over_selection": over_selection,
                "omission": omission,
                "wrong_source": wrong_source,
                "stale_or_non_authoritative_selection": stale_or_non_authoritative,
                "selected_stale_record_ids": stale_selected,
                "selected_explicitly_non_authoritative_record_ids": (
                    non_authoritative_selected
                ),
                "explicitly_non_authoritative_evidence": {
                    record_id: non_authoritative[record_id]
                    for record_id in non_authoritative_selected
                },
            }
            analysis_rows.append(row)
            condition_rows.append(row)

        summary_rows.append({
            "condition": condition,
            "cases": len(condition_rows),
            "exact_set_match_count": sum(
                row["exact_set_scorer_result"] for row in condition_rows
            ),
            "exact_set_mismatch_count": sum(
                not row["exact_set_scorer_result"] for row in condition_rows
            ),
            "over_selection_count": sum(row["over_selection"] for row in condition_rows),
            "omission_count": sum(row["omission"] for row in condition_rows),
            "wrong_source_count": sum(row["wrong_source"] for row in condition_rows),
            "stale_or_non_authoritative_selection_count": sum(
                row["stale_or_non_authoritative_selection"]
                for row in condition_rows
            ),
        })

    metadata = {
        "run_id": args.run_id,
        "scoring_id": args.scoring_id,
        "analysis_status": "post_hoc_diagnostic_not_preregistered",
        "scoring_changed": False,
        "classification_note": (
            "Error flags follow the requested set definitions and are non-exclusive: "
            "wrong_source also implies omission because at least one gold record is missing."
        ),
        "explicit_non_authoritative_detection": {
            "source": "canonical record authority prose",
            "case_insensitive_phrases": list(NON_AUTHORITATIVE_PHRASES),
        },
    }
    comparison = {
        "status_and_ttea_submissions_byte_identical": (
            submissions["status"].read_bytes() == submissions["ttea"].read_bytes()
        ),
        "status_and_ttea_submissions_structurally_identical": (
            status_submission == ttea_submission
        ),
        "differing_case_ids": differing_case_ids,
        "status_submission_sha256": sha256(submissions["status"]),
        "ttea_submission_sha256": sha256(submissions["ttea"]),
    }
    write_json(scoring_dir / "authority-error-summary.json", {
        **metadata,
        "condition_by_error_type": summary_rows,
        "status_ttea_comparison": comparison,
    })
    write_json(scoring_dir / "authority-error-cases.json", {
        **metadata,
        "cases": analysis_rows,
    })
    print(json.dumps({
        "condition_by_error_type": summary_rows,
        "status_ttea_comparison": comparison,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
