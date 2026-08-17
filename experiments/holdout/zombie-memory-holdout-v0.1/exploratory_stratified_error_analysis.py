#!/usr/bin/env python3
"""EXPLORATORY — NOT PREREGISTERED CONFIRMATORY ANALYSIS.

Classify extra authority records in the already-frozen stratified sample using
only structural metadata in accepted candidate artifacts.
"""

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CANDIDATES = ROOT / "candidates"
FREEZE_MANIFEST = ROOT / "FREEZE-MANIFEST.json"
ROLES = [
    "expired_temporary_rule",
    "restored_general_rule",
    "general_rule_outside_scope",
    "scoped_exception",
    "superseded_record",
    "current_non_authoritative_material",
    "supporting_or_context_record",
    "other_structural_role",
    "unclassified",
]
STRATA = [
    "Temporary rule with expiry/restoration",
    "Scoped exception vs general rule",
    "condition=ttea over-selection failures",
]


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def candidate_path(case_id, versions):
    version = int(versions[case_id])
    if version == 1:
        return CANDIDATES / case_id / "candidate.json"
    return CANDIDATES / case_id / "versions" / f"v{version}" / "candidate.json"


def structural_text(record):
    return " ".join(
        str(record.get(field, "")).casefold()
        for field in ("status", "effect", "authority", "content")
    )


def classify_record(record):
    if not record:
        return "unclassified"
    text = structural_text(record)
    status_effect = " ".join(
        str(record.get(field, "")).casefold() for field in ("status", "effect")
    )
    if any(marker in text for marker in (
        "non-authoritative", "not an independent source", "not independently",
        "administrative confirmation", "descriptive note only",
    )):
        return "current_non_authoritative_material"
    if ("temporary" in status_effect or "extension" in status_effect) and any(
        marker in status_effect for marker in ("expired", "ended", "no longer in effect")
    ):
        return "expired_temporary_rule"
    if "general" in text and any(marker in text for marker in ("restored", "again in effect", "resumes")):
        return "restored_general_rule"
    if "general" in text and any(marker in text for marker in ("narrower", "except where", "exception applies")):
        return "general_rule_outside_scope"
    if any(marker in text for marker in ("scoped exception", "narrower exception", "exception to")):
        return "scoped_exception"
    if any(marker in text for marker in ("superseded", "displaced", "replaced by", "former rule")):
        return "superseded_record"
    if any(marker in text for marker in (
        "separate from", "only for", "only;", "only.", "does not set",
        "does not establish", "does not modify", "does not create",
        "does not independently", "timing only", "documentation only",
        "transferability only", "submission method only",
    )):
        return "supporting_or_context_record"
    if any(str(record.get(field, "")).strip() for field in ("status", "effect", "authority")):
        return "other_structural_role"
    return "unclassified"


def response_lookup(path):
    result = {}
    with Path(path).open("r", encoding="utf-8") as stream:
        for line in stream:
            if line.strip():
                row = json.loads(line)
                result[(row["case_id"], row["condition"])] = row
    if len(result) != 96:
        raise ValueError(f"expected 96 unique response pairs in {path}")
    return result


def empty_role_counts():
    return {role: 0 for role in ROLES}


def add_role(grouped, key, role):
    if key not in grouped:
        grouped[key] = empty_role_counts()
    grouped[key][role] += 1


def stratum_for_index(index):
    if index < 6:
        return STRATA[0]
    if index < 12:
        return STRATA[1]
    return STRATA[2]


def analyze(manifest_path, replication_paths):
    manifest = load_json(manifest_path)
    if len(manifest) != 18:
        raise ValueError("frozen sample manifest must contain exactly 18 unique failures")
    pairs = {(item["case_id"], item["condition"]) for item in manifest}
    if len(pairs) != len(manifest):
        raise ValueError("sample manifest repeats a case-condition pair")

    versions = load_json(FREEZE_MANIFEST)["accepted_versions"]
    responses = {key: response_lookup(path) for key, path in replication_paths.items()}
    candidate_cache = {}
    samples = []
    overall_roles = empty_role_counts()
    by_family = {}
    by_condition = {}
    by_replication = {}
    by_stratum = {}
    sampled_by_stratum = {stratum: 0 for stratum in STRATA}

    for index, item in enumerate(manifest):
        replication = item["replication"]
        case_id = item["case_id"]
        condition = item["condition"]
        stratum = stratum_for_index(index)
        sampled_by_stratum[stratum] += 1
        if case_id not in candidate_cache:
            candidate_cache[case_id] = load_json(candidate_path(case_id, versions))
        candidate = candidate_cache[case_id]
        if candidate["family"] != item["frozen_family"]:
            raise ValueError("manifest family differs from accepted candidate family")
        row = responses[replication][(case_id, condition)]
        gold = set(candidate["gold"]["current_authority_record_ids"])
        predicted = set(row["parsed_response"].get("current_authority_record_ids", []))
        extra = sorted(predicted - gold)
        missing = gold - predicted
        if not extra or missing:
            raise ValueError("sample contains a non-over-selection response")

        records = {record["id"]: record for record in candidate["records"]}
        labels = []
        for record_id in extra:
            role = classify_record(records.get(record_id))
            labels.append({"record_id": record_id, "structural_role": role})
            overall_roles[role] += 1
            add_role(by_family, item["frozen_family"], role)
            add_role(by_condition, condition, role)
            add_role(by_replication, replication, role)
            add_role(by_stratum, stratum, role)

        samples.append({
            "replication": replication,
            "case_id": case_id,
            "condition": condition,
            "family": item["frozen_family"],
            "gold_authority_ids": sorted(gold),
            "predicted_authority_ids": sorted(predicted),
            "extra_ids": extra,
            "extra_record_structural_labels": labels,
        })

    return {
        "analysis_title": "EXPLORATORY — NOT PREREGISTERED CONFIRMATORY ANALYSIS",
        "analysis_status": "exploratory",
        "sample_manifest_frozen_before_content_inspection": True,
        "sampling_deterministic": True,
        "semantic_free_text_answers_inspected": False,
        "causal_interpretation_performed": False,
        "new_live_api_calls": 0,
        "sampled_cases_count": len(samples),
        "sampled_failures_by_stratum": sampled_by_stratum,
        "extra_record_count": sum(overall_roles.values()),
        "extra_record_structural_role_counts": overall_roles,
        "structural_role_by_stratum": by_stratum,
        "structural_role_by_family": by_family,
        "structural_role_by_condition": by_condition,
        "structural_role_by_replication": by_replication,
        "samples": samples,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--replication-1", required=True)
    parser.add_argument("--replication-2", required=True)
    parser.add_argument("--replication-3", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    result = analyze(args.manifest, {
        "replication-1": args.replication_1,
        "replication-2": args.replication_2,
        "replication-3": args.replication_3,
    })
    Path(args.output).write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    aggregate = {key: value for key, value in result.items() if key != "samples"}
    print(json.dumps(aggregate, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
