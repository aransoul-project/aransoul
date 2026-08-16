#!/usr/bin/env python3
"""Guarded runner for Zombie Memory Holdout v0.1.

Dry-run is the default. Live execution is impossible until the frozen config
sets execution_authorized=true and the caller also supplies --confirm-live.
The runner reads only frozen model-facing prompt files and never reads gold,
scorer fixtures, candidate files, or construction audits.
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
REPO_ROOT = RUN_DIR.parents[2]
CONFIG_PATH = RUN_DIR / "execution-config.prereg.json"
RESPONSE_FIELDS = {
    "id",
    "current_answer",
    "historical_answer",
    "current_authority_record_ids",
}


def utc_now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_commit():
    completed = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return completed.stdout.strip()


def record_ids(prompt):
    return re.findall(r"^\[([^\]]+)\](?: |\n)", prompt, flags=re.MULTILINE)


def validate_config(config):
    if config["conditions"] != ["plain", "timestamp", "status", "ttea"]:
        raise ValueError("condition order differs from preregistration")
    if config["case_ids"] != [f"ZH-{i:02d}" for i in range(1, 25)]:
        raise ValueError("case-id order differs from preregistration")
    if config["ordering"] != "case-major_then_condition-fixed":
        raise ValueError("request ordering differs from preregistration")
    if config["requests_per_replication"] != 96:
        raise ValueError("holdout replication must contain exactly 96 requests")
    if config["planned_replications"] != 3:
        raise ValueError("holdout requires exactly three planned replications")
    if config["retry_count"] != 0 or config["individual_retry_allowed"] is not False:
        raise ValueError("individual retries must remain disabled")
    if config["seed"] is not None:
        raise ValueError("seed must remain null unless preregistration is amended")


def load_frozen_prompts(config):
    prompts = {}
    for condition in config["conditions"]:
        expected = config["prompt_sha256"][condition]
        if not expected:
            raise ValueError(f"prompt hash not frozen for {condition}")
        path = REPO_ROOT / config["prompt_files"][condition]
        actual = sha256(path)
        if actual != expected:
            raise ValueError(
                f"frozen prompt hash mismatch for {condition}: expected {expected}, found {actual}"
            )
        prompts[condition] = load_json(path)
    return prompts


def validate_prompt_sets(config, prompts):
    reference = None
    pairs = set()
    for condition in config["conditions"]:
        rows = prompts[condition]
        if len(rows) != 24:
            raise ValueError(f"{condition}: expected 24 prompts")
        ids = [row["id"] for row in rows]
        families = [row["family"] for row in rows]
        if ids != config["case_ids"]:
            raise ValueError(f"{condition}: case order mismatch")
        current = list(zip(ids, families))
        if reference is None:
            reference = current
        elif current != reference:
            raise ValueError(f"{condition}: id/family alignment differs from plain")
        for row in rows:
            if row["condition"] != condition:
                raise ValueError(f"{condition}/{row['id']}: embedded condition mismatch")
            ids_in_prompt = record_ids(row["prompt"])
            if not ids_in_prompt or len(ids_in_prompt) != len(set(ids_in_prompt)):
                raise ValueError(f"{condition}/{row['id']}: missing/duplicate record IDs")
            pair = (row["id"], condition)
            if pair in pairs:
                raise ValueError(f"duplicate request pair: {pair}")
            pairs.add(pair)
    if len(pairs) != 96:
        raise ValueError("expected exactly 96 unique case/condition pairs")


def response_schema(case_id, allowed_record_ids):
    return {
        "type": "object",
        "additionalProperties": False,
        "required": sorted(RESPONSE_FIELDS),
        "properties": {
            "id": {"type": "string", "const": case_id},
            "current_answer": {"type": "string"},
            "historical_answer": {"type": "string"},
            "current_authority_record_ids": {
                "type": "array",
                "items": {"type": "string", "enum": allowed_record_ids},
            },
        },
    }


def request_payload(config, row):
    ids = record_ids(row["prompt"])
    return {
        "model": config["model"],
        "input": row["prompt"],
        "temperature": config["temperature"],
        "top_p": config["top_p"],
        "max_output_tokens": config["max_output_tokens"],
        "store": config["store"],
        "text": {
            "format": {
                "type": "json_schema",
                "name": "zombie_memory_holdout_response",
                "strict": True,
                "schema": response_schema(row["id"], ids),
            }
        },
    }


def extract_output_text(response):
    texts = []
    for item in response.get("output", []):
        if item.get("type") != "message":
            continue
        for content in item.get("content", []):
            if content.get("type") == "output_text":
                texts.append(content.get("text", ""))
    return "".join(texts)


def validate_parsed(parsed, case_id, allowed_record_ids):
    if not isinstance(parsed, dict) or set(parsed) != RESPONSE_FIELDS:
        raise ValueError("parsed response must contain exactly the four required fields")
    if parsed["id"] != case_id:
        raise ValueError("response id mismatch")
    if not isinstance(parsed["current_answer"], str) or not parsed["current_answer"].strip():
        raise ValueError("current_answer must be a non-empty string")
    if not isinstance(parsed["historical_answer"], str) or not parsed["historical_answer"].strip():
        raise ValueError("historical_answer must be a non-empty string")
    selected = parsed["current_authority_record_ids"]
    if not isinstance(selected, list) or len(selected) != len(set(selected)):
        raise ValueError("current_authority_record_ids must be a unique list")
    if any(value not in allowed_record_ids for value in selected):
        raise ValueError("current_authority_record_ids contains an unknown record ID")


def parse_response_text(raw_text, case_id, allowed_record_ids):
    try:
        parsed = json.loads(raw_text)
        validate_parsed(parsed, case_id, allowed_record_ids)
        return "parsed", parsed, None
    except (json.JSONDecodeError, TypeError, ValueError) as exc:
        return "parse_failure", None, str(exc)


def call_openai(config, payload, api_key):
    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        "https://api.openai.com/v1/responses",
        data=body,
        method="POST",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=config["request_timeout_seconds"]) as response:
            raw_body = response.read().decode("utf-8", errors="replace")
            return response.status, json.loads(raw_body), None
    except urllib.error.HTTPError as exc:
        raw_body = exc.read().decode("utf-8", errors="replace")
        try:
            raw_response = json.loads(raw_body)
        except json.JSONDecodeError:
            raw_response = {"unparsed_http_body": raw_body}
        return exc.code, raw_response, f"HTTPError: {exc}"
    except Exception as exc:
        return None, None, f"{type(exc).__name__}: {exc}"


def mock_response(row):
    first_id = record_ids(row["prompt"])[0]
    parsed = {
        "id": row["id"],
        "current_answer": "DRY_RUN_CURRENT",
        "historical_answer": "DRY_RUN_HISTORICAL",
        "current_authority_record_ids": [first_id],
    }
    return 200, {"output": [{"type": "message", "content": [{"type": "output_text", "text": json.dumps(parsed)}]}]}, None


def build_record(config, mode, run_id, request_index, row, status, raw, error):
    ids = record_ids(row["prompt"])
    raw_text = extract_output_text(raw or {}) if status == 200 else ""
    if status == 200:
        parse_status, parsed, parse_error = parse_response_text(raw_text, row["id"], ids)
    else:
        parse_status, parsed, parse_error = "request_failure", None, error or f"HTTP status {status}"
    return {
        "experiment_id": config["experiment_id"],
        "mode": mode,
        "run_id": run_id,
        "request_index": request_index,
        "attempt": 1,
        "case_id": row["id"],
        "condition": row["condition"],
        "model": config["model"],
        "http_status": status,
        "parse_status": parse_status,
        "parsed_response": parsed,
        "parse_error": parse_error,
        "raw_response": raw,
    }


def request_sequence(config, prompts):
    for case_id in config["case_ids"]:
        for condition in config["conditions"]:
            row = next(r for r in prompts[condition] if r["id"] == case_id)
            yield row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--replication", choices=("replication-1", "replication-2", "replication-3"), required=True)
    parser.add_argument("--mode", choices=("dry-run", "live"), default="dry-run")
    parser.add_argument("--confirm-live", action="store_true")
    parser.add_argument("--run-id")
    args = parser.parse_args()

    config = load_json(CONFIG_PATH)
    validate_config(config)
    prompts = load_frozen_prompts(config)
    validate_prompt_sets(config, prompts)

    if args.mode == "live":
        if config.get("execution_authorized") is not True:
            raise SystemExit("live execution is not authorized by frozen config")
        if not args.confirm_live:
            raise SystemExit("live mode requires --confirm-live")
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise SystemExit("live mode requires OPENAI_API_KEY")
    else:
        api_key = None

    started_at = utc_now()
    run_id = args.run_id or f"{args.mode}-{started_at.replace(':', '').replace('-', '')}"
    output_dir = RUN_DIR / "outputs" / args.replication / args.mode / run_id
    output_dir.mkdir(parents=True, exist_ok=False)
    manifest_path = output_dir / "manifest.json"
    responses_path = output_dir / "responses.jsonl"
    manifest = {
        "schema_version": 1,
        "experiment_id": config["experiment_id"],
        "replication": args.replication,
        "mode": args.mode,
        "api_called": False,
        "run_id": run_id,
        "status": "running",
        "run_started_at": started_at,
        "run_completed_at": None,
        "repository_commit": git_commit(),
        "construction_payload_commit": config["construction_payload_commit"],
        "model": config["model"],
        "temperature": config["temperature"],
        "top_p": config["top_p"],
        "max_output_tokens": config["max_output_tokens"],
        "retry_count": config["retry_count"],
        "request_count_expected": 96,
        "request_count_recorded": 0,
        "parsed_count": 0,
        "parse_failure_count": 0,
        "request_failure_count": 0,
        "prompt_sha256": config["prompt_sha256"],
        "raw_data_integrity_approved": False,
        "scoring_started": False,
    }
    write_json(manifest_path, manifest)

    with responses_path.open("a", encoding="utf-8", newline="\n") as stream:
        for request_index, row in enumerate(request_sequence(config, prompts), start=1):
            payload = request_payload(config, row)
            if args.mode == "dry-run":
                status, raw, error = mock_response(row)
            else:
                status, raw, error = call_openai(config, payload, api_key)
                manifest["api_called"] = True
            record = build_record(config, args.mode, run_id, request_index, row, status, raw, error)
            stream.write(json.dumps(record, ensure_ascii=False) + "\n")
            stream.flush()
            manifest["request_count_recorded"] += 1
            manifest[f"{record['parse_status']}_count"] += 1
            write_json(manifest_path, manifest)

            if args.mode == "live" and record["parse_status"] == "request_failure":
                manifest["status"] = "technical_invalid_stopped"
                manifest["run_completed_at"] = utc_now()
                write_json(manifest_path, manifest)
                raise SystemExit("transport/provider failure: entire replication is technical-invalid; no selective retry")

    if manifest["request_count_recorded"] != 96:
        raise RuntimeError("replication did not persist exactly 96 records")
    manifest["status"] = "dry_run_validated" if args.mode == "dry-run" else "responses_complete_unreviewed"
    manifest["run_completed_at"] = utc_now()
    write_json(manifest_path, manifest)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
