import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


gen = load_module("holdout_prompt_generator", "prompt_generator.py")
runner = load_module("holdout_runner", "runner.py")


def test_generated_prompt_set_matches_runner_contract():
    outputs = gen.build_all()
    config = runner.load_json(runner.CONFIG_PATH)
    runner.validate_config(config)
    runner.validate_prompt_sets(config, outputs)
    sequence = list(runner.request_sequence(config, outputs))
    assert len(sequence) == 96
    assert [(r["id"], r["condition"]) for r in sequence[:4]] == [
        ("ZH-01", "plain"),
        ("ZH-01", "timestamp"),
        ("ZH-01", "status"),
        ("ZH-01", "ttea"),
    ]
    assert sequence[-1]["id"] == "ZH-24"
    assert sequence[-1]["condition"] == "ttea"


def test_record_id_parser_supports_all_four_formats():
    outputs = gen.build_all()
    for condition in gen.CONDITIONS:
        for row in outputs[condition]:
            ids = runner.record_ids(row["prompt"])
            assert ids
            assert len(ids) == len(set(ids))


def test_response_schema_avoids_provider_rejected_uniqueitems_keyword():
    schema = runner.response_schema("ZH-01", ["R1", "R2"])
    authority = schema["properties"]["current_authority_record_ids"]
    assert "uniqueItems" not in authority
    assert authority["items"]["enum"] == ["R1", "R2"]


def test_parsed_validation_enforces_uniqueness_in_application_code():
    good = {
        "id": "ZH-01",
        "current_answer": "45 seconds",
        "historical_answer": "30 seconds",
        "current_authority_record_ids": ["R2"],
    }
    runner.validate_parsed(good, "ZH-01", ["R1", "R2"])

    bad = dict(good)
    bad["current_authority_record_ids"] = ["R2", "R2"]
    try:
        runner.validate_parsed(bad, "ZH-01", ["R1", "R2"])
    except ValueError:
        pass
    else:
        raise AssertionError("duplicate authority IDs should fail application validation")


def test_live_execution_starts_disabled():
    config = runner.load_json(runner.CONFIG_PATH)
    assert config["execution_authorized"] is False
    assert all(config["prompt_sha256"][c] is None for c in config["conditions"])
