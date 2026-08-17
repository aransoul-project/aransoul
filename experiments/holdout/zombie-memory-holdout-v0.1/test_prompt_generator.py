import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("holdout_prompt_generator", ROOT / "prompt_generator.py")
gen = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gen)


def test_builds_exactly_24_by_4_without_gold_leakage():
    outputs = gen.build_all()
    gen.validate_outputs(outputs)
    assert set(outputs) == set(gen.CONDITIONS)
    for condition in gen.CONDITIONS:
        assert len(outputs[condition]) == 24
        assert [row["id"] for row in outputs[condition]] == list(gen.CASE_IDS)
        for row in outputs[condition]:
            assert "gold_logic" not in row["prompt"]
            assert "stale_record_ids" not in row["prompt"]
            assert "Current question:" in row["prompt"]
            assert "Historical question:" in row["prompt"]


def test_generation_is_byte_deterministic():
    first_outputs = gen.build_all()
    second_outputs = gen.build_all()
    first_files, first_hashes = gen.render_files(first_outputs)
    second_files, second_hashes = gen.render_files(second_outputs)
    assert first_hashes == second_hashes
    assert first_files == second_files


def test_condition_files_are_semantically_aligned_by_id_and_family():
    outputs = gen.build_all()
    reference = [(row["id"], row["family"]) for row in outputs["plain"]]
    for condition in gen.CONDITIONS:
        assert [(row["id"], row["family"]) for row in outputs[condition]] == reference


def test_accepted_version_routing_is_frozen():
    manifest = gen.load_json(gen.MANIFEST_PATH)
    assert manifest["accepted_versions"]["ZH-02"] == 3
    assert manifest["accepted_versions"]["ZH-03"] == 2
    assert sum(1 for v in manifest["accepted_versions"].values() if v != 1) == 2
