import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parents[2]
KIT = REPO_ROOT / "docs" / "experiments" / "zombie-memory-replication-kit-v0.1"
VALIDATOR = KIT / "validate_provider_neutral_responses.py"
HASH_VERIFIER = KIT / "verify_frozen_hashes.py"
CONDITIONS = ("plain", "timestamp", "status", "ttea")


def parsed_row(case_id, condition):
    return {
        "case_id": case_id,
        "condition": condition,
        "parse_status": "parsed",
        "parsed_response": {
            "id": case_id,
            "current_answer": "placeholder current",
            "historical_answer": "placeholder historical",
            "current_authority_record_ids": [],
        },
    }


def run_validator(path):
    return subprocess.run([sys.executable, str(VALIDATOR), str(path)], capture_output=True, text=True, cwd=REPO_ROOT)


def test_provider_neutral_validator_accepts_complete_24x4_matrix(tmp_path):
    path = tmp_path / "responses.jsonl"
    rows = [parsed_row(f"ZH-{i:02d}", condition) for i in range(1, 25) for condition in CONDITIONS]
    path.write_text("\n".join(json.dumps(row) for row in rows) + "\n", encoding="utf-8", newline="\n")
    result = run_validator(path)
    assert result.returncode == 0, result.stderr + result.stdout
    payload = json.loads(result.stdout)
    assert payload["status"] == "provider_neutral_integrity_pass"
    assert payload["unique_case_condition_pairs"] == 96


def test_provider_neutral_validator_rejects_96_copies_of_one_pair(tmp_path):
    path = tmp_path / "responses.jsonl"
    row = parsed_row("ZH-01", "plain")
    path.write_text("\n".join(json.dumps(row) for _ in range(96)) + "\n", encoding="utf-8", newline="\n")
    result = run_validator(path)
    assert result.returncode != 0
    assert "each case/condition pair must occur exactly once" in (result.stderr + result.stdout)


def test_provider_neutral_validator_rejects_id_mismatch(tmp_path):
    path = tmp_path / "responses.jsonl"
    rows = [parsed_row(f"ZH-{i:02d}", condition) for i in range(1, 25) for condition in CONDITIONS]
    rows[0]["parsed_response"]["id"] = "ZH-02"
    path.write_text("\n".join(json.dumps(row) for row in rows) + "\n", encoding="utf-8", newline="\n")
    result = run_validator(path)
    assert result.returncode != 0
    assert "parsed_response.id does not match case_id" in (result.stderr + result.stdout)


def test_frozen_prompt_hashes_verify_from_repository_bytes():
    result = subprocess.run([sys.executable, str(HASH_VERIFIER), "--ref", "HEAD"], capture_output=True, text=True, cwd=REPO_ROOT)
    assert result.returncode == 0, result.stderr + result.stdout
    payload = json.loads(result.stdout)
    assert payload["status"] == "pass"
    assert payload["hash_basis"].startswith("git repository bytes")
