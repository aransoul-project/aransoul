#!/usr/bin/env python3
"""Round 2 runner for the frozen Zombie Memory Pilot v0.1 prompts.

This runner never reads cases.json, gold labels, or scorer.py. Live execution
requires an explicit replication, OPENAI_API_KEY, and --confirm-live.
"""

import argparse
import importlib.util
import json
import os
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
REPO_ROOT = RUN_DIR.parents[2]
CONFIG_PATH = RUN_DIR / "config.json"
ROUND1_RUNNER_PATH = RUN_DIR.parent / "zombie-memory-pilot-v0.1-round-1/runner.py"


def load_round1_runner():
    spec = importlib.util.spec_from_file_location("zombie_memory_round1_runner", ROUND1_RUNNER_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


r1 = load_round1_runner()
response_schema = r1.response_schema
validate_parsed = r1.validate_parsed


def validate_config(config):
    expected_replications = {"replication-1", "replication-2", "replication-3"}
    if set(config["replications"]) != expected_replications:
        raise ValueError("Round 2 requires exactly replication-1/2/3")
    if config["requests_per_replication"] != 40:
        raise ValueError("Round 2 requires exactly 40 requests per replication")
    if config["retry_count"] != 0:
        raise ValueError("Round 2 retries must remain zero")


def validate_output_record(record, replication):
    if record["replication"] != replication:
        raise ValueError("response replication mismatch")
    if record["attempt"] != 1:
        raise ValueError("retry attempts are not allowed")
    if record["parse_status"] == "parsed" and record["parsed_response"] is None:
        raise ValueError("parsed record is missing parsed_response")
    if record["parse_status"] != "parsed" and record["parse_error"] is None:
        raise ValueError("failure record is missing parse_error")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--replication", required=True)
    parser.add_argument("--mode", choices=("dry-run", "live"), default="dry-run")
    parser.add_argument("--confirm-live", action="store_true")
    parser.add_argument("--run-id")
    args = parser.parse_args()

    config = r1.load_json(CONFIG_PATH)
    validate_config(config)
    if args.replication not in config["replications"]:
        raise SystemExit(f"unknown replication: {args.replication}")

    prompts = r1.load_frozen_prompts(config)
    r1.validate_prompt_sets(config, prompts)
    if args.mode == "live" and not args.confirm_live:
        raise SystemExit("live mode requires --confirm-live")
    api_key = None
    if args.mode == "live":
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise SystemExit("live mode requires OPENAI_API_KEY")

    started_at = r1.utc_now()
    run_id = args.run_id or f"{args.mode}-{started_at.replace(':', '').replace('-', '')}"
    output_root = RUN_DIR / config["replications"][args.replication]
    output_dir = output_root / args.mode / run_id
    output_dir.mkdir(parents=True, exist_ok=False)
    manifest_path = output_dir / "manifest.json"
    responses_path = output_dir / "responses.jsonl"
    manifest = {
        "schema_version": 1,
        "experiment_id": config["experiment_id"],
        "preregistration_commit": config["preregistration_commit"],
        "replication": args.replication,
        "mode": args.mode,
        "api_called": False,
        "run_id": run_id,
        "status": "running",
        "run_started_at": started_at,
        "run_completed_at": None,
        "repository_commit": r1.git_commit(),
        "provider": config["provider"],
        "api": config["api"],
        "model": config["model"],
        "temperature": config["temperature"],
        "top_p": config["top_p"],
        "max_output_tokens": config["max_output_tokens"],
        "retry_count": config["retry_count"],
        "request_count_expected": config["requests_per_replication"],
        "request_count_recorded": 0,
        "parsed_count": 0,
        "parse_failure_count": 0,
        "request_failure_count": 0,
        "prompt_sha256": config["prompt_sha256"],
        "cost_estimate": r1.estimate_cost(config, prompts),
        "raw_data_integrity_approved": False,
        "scoring_started": False,
        "authority_diagnostic_started": False
    }
    r1.write_json(manifest_path, manifest)

    request_index = 0
    with responses_path.open("a", encoding="utf-8", newline="\n") as stream:
        for condition in config["conditions"]:
            for row in prompts[condition]:
                request_index += 1
                request_started_at = r1.utc_now()
                payload = r1.request_payload(config, row)
                if args.mode == "dry-run":
                    status, raw, error = r1.mock_response(row)
                else:
                    status, raw, error = r1.call_openai(config, payload, api_key)
                    manifest["api_called"] = True
                record = r1.build_record(
                    config, args.mode, run_id, request_index, row,
                    request_started_at, status, raw, error,
                )
                record["replication"] = args.replication
                validate_output_record(record, args.replication)
                stream.write(json.dumps(record, ensure_ascii=False) + "\n")
                stream.flush()
                manifest["request_count_recorded"] += 1
                manifest[f"{record['parse_status']}_count"] += 1
                r1.write_json(manifest_path, manifest)

    if manifest["request_count_recorded"] != config["requests_per_replication"]:
        raise RuntimeError("replication did not persist exactly 40 records")
    manifest["status"] = (
        "dry_run_validated" if args.mode == "dry-run" else "responses_complete_unreviewed"
    )
    manifest["run_completed_at"] = r1.utc_now()
    r1.write_json(manifest_path, manifest)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
