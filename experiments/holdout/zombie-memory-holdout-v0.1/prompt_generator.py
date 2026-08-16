#!/usr/bin/env python3
"""Deterministically generate model-facing Zombie Memory Holdout v0.1 prompts.

This generator reads only the accepted frozen candidate/render-review artifacts.
It never reads scorer fixtures or gold labels when constructing prompts.
"""

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
GENERATED_DIR = ROOT / "generated"
MANIFEST_PATH = ROOT / "FREEZE-MANIFEST.json"
CONDITIONS = ("plain", "timestamp", "status", "ttea")
CASE_IDS = tuple(f"ZH-{i:02d}" for i in range(1, 25))
HEADER = "Read the records and answer both questions. Also identify the record IDs that currently control the answer."
RETURN_LINE = "Return JSON with id, current_answer, historical_answer, current_authority_record_ids."


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def accepted_base(case_id, version):
    base = ROOT / "candidates" / case_id
    if version == 1:
        return base
    return base / "versions" / f"v{version}"


def format_record(condition, record):
    rid = record["id"]
    if condition == "plain":
        return f"[{rid}] {record['text']}"
    if condition == "timestamp":
        return f"[{rid}]\nTime: {record['time']}\n{record['text']}"
    if condition == "status":
        return f"[{rid}]\nStatus: {record['status']}\n{record['text']}"
    if condition == "ttea":
        return (
            f"[{rid}]\n"
            f"Time: {record['time']}\n"
            f"Status: {record['status']}\n"
            f"Effect: {record['effect']}\n"
            f"Authority: {record['authority']}\n"
            f"Content: {record['content']}"
        )
    raise ValueError(f"unknown condition: {condition}")


def build_prompt(render_review, condition):
    rendered = render_review["renderings"][condition]
    records = "\n\n".join(format_record(condition, r) for r in rendered["records"])
    return (
        f"{HEADER}\n\n"
        f"{records}\n\n"
        f"Current question: {render_review['question']}\n"
        f"Historical question: {render_review['historical_question']}\n"
        f"{RETURN_LINE}"
    )


def build_all():
    manifest = load_json(MANIFEST_PATH)
    versions = manifest["accepted_versions"]
    if tuple(versions) != CASE_IDS:
        raise ValueError("accepted-version manifest does not contain ZH-01..ZH-24 in order")

    outputs = {condition: [] for condition in CONDITIONS}
    for case_id in CASE_IDS:
        version = versions[case_id]
        base = accepted_base(case_id, version)
        candidate_path = base / "candidate.json"
        render_path = base / "rendered" / "render-review.json"
        candidate = load_json(candidate_path)
        review = load_json(render_path)

        if candidate["slot_id"] != case_id or review["slot_id"] != case_id:
            raise ValueError(f"{case_id}: slot-id mismatch")
        if review["candidate_version"] != version:
            raise ValueError(f"{case_id}: accepted version mismatch")
        if review.get("target_model_execution_count") != 0:
            raise ValueError(f"{case_id}: construction artifact shows target-model execution")
        if review["semantic_equivalence_check"]["result"] != "pass":
            raise ValueError(f"{case_id}: semantic-equivalence gate not passed")
        if review["leakage_check"]["result"] != "pass":
            raise ValueError(f"{case_id}: leakage gate not passed")

        for condition in CONDITIONS:
            outputs[condition].append({
                "id": case_id,
                "family": candidate["family"],
                "condition": condition,
                "prompt": build_prompt(review, condition),
            })
    return outputs


def validate_outputs(outputs):
    expected_ids = list(CASE_IDS)
    for condition in CONDITIONS:
        rows = outputs[condition]
        if len(rows) != 24:
            raise ValueError(f"{condition}: expected 24 prompts")
        if [r["id"] for r in rows] != expected_ids:
            raise ValueError(f"{condition}: case order mismatch")
        if any(r["condition"] != condition for r in rows):
            raise ValueError(f"{condition}: embedded condition mismatch")
        for row in rows:
            prompt = row["prompt"]
            forbidden = ("gold_logic", "stale_record_ids", "current_authority_record_ids\":")
            if any(token in prompt for token in forbidden):
                raise ValueError(f"{condition}/{row['id']}: possible gold leakage")
            if "Current question:" not in prompt or "Historical question:" not in prompt:
                raise ValueError(f"{condition}/{row['id']}: missing question")


def render_files(outputs):
    files = {}
    for condition in CONDITIONS:
        files[f"generated/{condition}.json"] = canonical_json_bytes(outputs[condition])
    hashes = {condition: sha256_bytes(files[f"generated/{condition}.json"]) for condition in CONDITIONS}
    hash_doc = {
        "artifact": "Zombie Memory Holdout v0.1 model-facing prompts",
        "algorithm": "sha256",
        "generator": "prompt_generator.py",
        "case_count_per_condition": 24,
        "conditions": list(CONDITIONS),
        "sha256": hashes,
    }
    files["generated/prompt-hashes.json"] = canonical_json_bytes(hash_doc)
    return files, hashes


def write_files(files):
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    for relative, data in files.items():
        path = ROOT / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)


def check_files(files):
    mismatches = []
    for relative, expected in files.items():
        path = ROOT / relative
        if not path.exists():
            mismatches.append(f"missing:{relative}")
        elif path.read_bytes() != expected:
            mismatches.append(f"mismatch:{relative}")
    if mismatches:
        raise SystemExit("deterministic regeneration check failed: " + ", ".join(mismatches))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify existing generated files are byte-identical")
    args = parser.parse_args()
    outputs = build_all()
    validate_outputs(outputs)
    files, hashes = render_files(outputs)
    if args.check:
        check_files(files)
        print(json.dumps({"status": "ok", "sha256": hashes}, indent=2))
    else:
        write_files(files)
        print(json.dumps({"status": "generated", "sha256": hashes}, indent=2))


if __name__ == "__main__":
    main()
