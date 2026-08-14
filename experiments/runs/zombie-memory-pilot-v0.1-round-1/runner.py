#!/usr/bin/env python3
"""Independent empirical runner for frozen Zombie Memory Pilot v0.1 prompts.

Dry-run is the default. Live mode requires both OPENAI_API_KEY and
--confirm-live. The runner never reads cases.json, gold labels, or scorer.py.
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
REPO_ROOT = RUN_DIR.parents[2]
CONFIG_PATH = RUN_DIR / "config.json"
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
    return re.findall(r"^\[([^\]]+)\] ", prompt, flags=re.MULTILINE)


def load_frozen_prompts(config):
    prompts = {}
    for condition in config["conditions"]:
        path = REPO_ROOT / config["prompt_files"][condition]
        actual_hash = sha256(path)
        expected_hash = config["prompt_sha256"][condition]
        if actual_hash != expected_hash:
            raise ValueError(
                f"frozen prompt hash mismatch for {condition}: "
                f"expected {expected_hash}, found {actual_hash}"
            )
        prompts[condition] = load_json(path)
    return prompts


def validate_prompt_sets(config, prompts):
    expected_count = config["cases_per_condition"]
    reference_ids = None
    reference_families = None
    seen_pairs = set()

    for condition in config["conditions"]:
        rows = prompts[condition]
        if len(rows) != expected_count:
            raise ValueError(f"{condition}: expected {expected_count} prompts, found {len(rows)}")
        ids = [row["id"] for row in rows]
        families = [row["family"] for row in rows]
        if len(set(ids)) != expected_count:
            raise ValueError(f"{condition}: duplicate case IDs")
        if reference_ids is None:
            reference_ids = ids
            reference_families = families
        elif ids != reference_ids or families != reference_families:
            raise ValueError(f"{condition}: case ID order or family differs from Plain")

        for row in rows:
            if row["condition"] != condition:
                raise ValueError(f"{condition}/{row['id']}: embedded condition mismatch")
            if not isinstance(row["prompt"], str) or not row["prompt"].strip():
                raise ValueError(f"{condition}/{row['id']}: empty prompt")
            if not record_ids(row["prompt"]):
                raise ValueError(f"{condition}/{row['id']}: no record IDs in prompt")
            pair = (condition, row["id"])
            if pair in seen_pairs:
                raise ValueError(f"duplicate request pair: {pair}")
            seen_pairs.add(pair)

    expected_total = len(config["conditions"]) * expected_count
    if len(seen_pairs) != expected_total:
        raise ValueError(f"expected {expected_total} request pairs, found {len(seen_pairs)}")


def response_schema(case_id, allowed_record_ids):
    return {
        "type": "object",
        "additionalProperties": False,
        "required": sorted(RESPONSE_FIELDS),
        "properties": {
            "id": {"type": "string", "const": case_id},
            "current_answer": {"type": "string", "enum": ["YES", "NO"]},
            "historical_answer": {"type": "string", "enum": ["YES", "NO"]},
            "current_authority_record_ids": {
                "type": "array",
                "items": {"type": "string", "enum": allowed_record_ids},
                "uniqueItems": True,
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
                "name": "zombie_memory_pilot_response",
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
        raise ValueError(f"response id {parsed['id']!r} does not match {case_id!r}")
    for field in ("current_answer", "historical_answer"):
        if parsed[field] not in ("YES", "NO"):
            raise ValueError(f"{field} must be YES or NO")
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
        config["endpoint"],
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
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
    except Exception as exc:  # Preserve transport failures; deliberately no retry.
        return None, None, f"{type(exc).__name__}: {exc}"


def mock_response(row):
    first_id = record_ids(row["prompt"])[0]
    parsed = {
        "id": row["id"],
        "current_answer": "YES",
        "historical_answer": "YES",
        "current_authority_record_ids": [first_id],
    }
    raw_text = json.dumps(parsed, separators=(",", ":"))
    raw_response = {
        "id": f"dry-run-{row['condition']}-{row['id']}",
        "object": "response.dry_run",
        "model": "dry-run-no-api-call",
        "output": [
            {
                "type": "message",
                "content": [{"type": "output_text", "text": raw_text}],
            }
        ],
        "usage": {"input_tokens": 0, "output_tokens": 0, "total_tokens": 0},
    }
    return 200, raw_response, None


def build_record(config, mode, run_id, request_index, row, started_at, status, raw, error):
    received_at = utc_now()
    raw_text = extract_output_text(raw or {})
    allowed_ids = record_ids(row["prompt"])
    if error:
        parse_status, parsed, parse_error = "request_failure", None, error
    else:
        parse_status, parsed, parse_error = parse_response_text(
            raw_text, row["id"], allowed_ids
        )
    return {
        "schema_version": 1,
        "mode": mode,
        "api_called": mode == "live",
        "run_id": run_id,
        "provider": config["provider"],
        "api": config["api"],
        "endpoint": config["endpoint"],
        "model_requested": config["model"],
        "model_returned": (raw or {}).get("model"),
        "temperature": config["temperature"],
        "top_p": config["top_p"],
        "max_output_tokens": config["max_output_tokens"],
        "request_index": request_index,
        "attempt": 1,
        "condition": row["condition"],
        "case_id": row["id"],
        "family": row["family"],
        "request_started_at": started_at,
        "response_received_at": received_at,
        "http_status": status,
        "raw_response": raw,
        "raw_text": raw_text,
        "parse_status": parse_status,
        "parsed_response": parsed,
        "parse_error": parse_error,
        "usage": (raw or {}).get("usage"),
    }


def validate_output_record(record):
    required = {
        "schema_version", "mode", "api_called", "run_id", "provider", "api",
        "endpoint", "model_requested", "model_returned", "temperature", "top_p",
        "max_output_tokens", "request_index", "attempt", "condition", "case_id",
        "family", "request_started_at", "response_received_at", "http_status",
        "raw_response", "raw_text", "parse_status", "parsed_response",
        "parse_error", "usage",
    }
    if set(record) != required:
        raise ValueError("output record fields do not match schema version 1")
    if record["attempt"] != 1:
        raise ValueError("retry attempts are not allowed in round 1")
    if record["parse_status"] == "parsed" and record["parsed_response"] is None:
        raise ValueError("parsed record is missing parsed_response")
    if record["parse_status"] != "parsed" and record["parse_error"] is None:
        raise ValueError("failure record is missing parse_error")


def estimate_cost(config, prompts):
    prompt_chars = sum(len(row["prompt"]) for rows in prompts.values() for row in rows)
    schema_chars = sum(
        len(json.dumps(response_schema(row["id"], record_ids(row["prompt"]))))
        for rows in prompts.values()
        for row in rows
    )
    estimated_input_tokens = (prompt_chars + schema_chars + 3) // 4
    count = len(config["conditions"]) * config["cases_per_condition"]
    expected_output_tokens = count * config["expected_output_tokens_per_response"]
    max_output_tokens = count * config["max_output_tokens"]
    prices = config["pricing_usd_per_million_tokens"]
    input_cost = estimated_input_tokens * prices["input"] / 1_000_000
    expected_cost = input_cost + expected_output_tokens * prices["output"] / 1_000_000
    max_configured_cost = input_cost + max_output_tokens * prices["output"] / 1_000_000
    return {
        "method": "character_count_divided_by_4_including_per-request JSON schema",
        "prompt_characters": prompt_chars,
        "schema_characters": schema_chars,
        "estimated_input_tokens": estimated_input_tokens,
        "expected_output_tokens": expected_output_tokens,
        "max_configured_output_tokens": max_output_tokens,
        "estimated_cost_usd": round(expected_cost, 6),
        "max_configured_cost_usd": round(max_configured_cost, 6),
    }


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("dry-run", "live"), default="dry-run")
    parser.add_argument("--confirm-live", action="store_true")
    parser.add_argument("--run-id")
    args = parser.parse_args()

    config = load_json(CONFIG_PATH)
    prompts = load_frozen_prompts(config)
    validate_prompt_sets(config, prompts)

    if args.mode == "live" and not args.confirm_live:
        raise SystemExit("live mode requires --confirm-live")
    api_key = None
    if args.mode == "live":
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise SystemExit("live mode requires OPENAI_API_KEY")

    run_started_at = utc_now()
    run_id = args.run_id or f"{args.mode}-{run_started_at.replace(':', '').replace('-', '')}"
    output_dir = RUN_DIR / "outputs" / args.mode / run_id
    output_dir.mkdir(parents=True, exist_ok=False)
    responses_path = output_dir / "responses.jsonl"
    manifest_path = output_dir / "manifest.json"

    manifest = {
        "schema_version": 1,
        "experiment_id": config["experiment_id"],
        "mode": args.mode,
        "api_called": False,
        "run_id": run_id,
        "status": "running",
        "run_started_at": run_started_at,
        "run_completed_at": None,
        "repository_commit": git_commit(),
        "provider": config["provider"],
        "api": config["api"],
        "model": config["model"],
        "temperature": config["temperature"],
        "top_p": config["top_p"],
        "max_output_tokens": config["max_output_tokens"],
        "retry_count": config["retry_count"],
        "request_count_expected": 40,
        "request_count_recorded": 0,
        "parsed_count": 0,
        "parse_failure_count": 0,
        "request_failure_count": 0,
        "prompt_sha256": config["prompt_sha256"],
        "cost_estimate": estimate_cost(config, prompts),
        "scoring_started": False,
    }
    write_json(manifest_path, manifest)

    request_index = 0
    with responses_path.open("a", encoding="utf-8", newline="\n") as stream:
        for condition in config["conditions"]:
            for row in prompts[condition]:
                request_index += 1
                started_at = utc_now()
                payload = request_payload(config, row)
                if args.mode == "dry-run":
                    status, raw, error = mock_response(row)
                else:
                    status, raw, error = call_openai(config, payload, api_key)
                    manifest["api_called"] = True
                record = build_record(
                    config, args.mode, run_id, request_index, row, started_at,
                    status, raw, error,
                )
                validate_output_record(record)
                stream.write(json.dumps(record, ensure_ascii=False) + "\n")
                stream.flush()
                manifest["request_count_recorded"] += 1
                key = f"{record['parse_status']}_count"
                manifest[key] += 1
                write_json(manifest_path, manifest)

    if manifest["request_count_recorded"] != manifest["request_count_expected"]:
        raise RuntimeError("run ended without exactly 40 persisted response records")
    manifest["status"] = "dry_run_validated" if args.mode == "dry-run" else "responses_complete_unscored"
    manifest["run_completed_at"] = utc_now()
    write_json(manifest_path, manifest)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
