from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("holdout_scorer", ROOT / "scorer.py")
assert SPEC and SPEC.loader
scorer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(scorer)


def zh01_case():
    return {
        "id": "ZH-01",
        "records": [{"id": "R1"}, {"id": "R2"}],
        "gold": {
            "current_answer": "45 seconds",
            "historical_answer": "30 seconds",
            "current_authority_record_ids": ["R2"],
            "stale_record_ids": ["R1"],
        },
    }


def zh02_case():
    return {
        "id": "ZH-02",
        "records": [{"id": "R1"}, {"id": "R2"}, {"id": "R3"}],
        "gold": {
            "current_answer": "East Gate",
            "historical_answer": "South Gate",
            "current_authority_record_ids": ["R2"],
            "stale_record_ids": ["R1", "R3"],
        },
    }


def test_zh01_correct():
    row = scorer.score_case(zh01_case(), {
        "id":"ZH-01", "current_answer":"45 seconds", "historical_answer":"30 seconds",
        "current_authority_record_ids":["R2"]
    })
    assert row["current_correct"] is True
    assert row["historical_correct"] is True
    assert row["authority_correct"] is True
    assert row["stale_authority_error"] is False
    assert row["false_discard"] is False


def test_zh01_stale_wrong_source():
    row = scorer.score_case(zh01_case(), {
        "id":"ZH-01", "current_answer":"45 seconds", "historical_answer":"30 seconds",
        "current_authority_record_ids":["R1"]
    })
    assert row["authority_correct"] is False
    assert row["stale_authority_error"] is True
    assert row["false_discard"] is True


def test_zh02_overselection_is_exact_set_failure():
    row = scorer.score_case(zh02_case(), {
        "id":"ZH-02", "current_answer":"East Gate", "historical_answer":"South Gate",
        "current_authority_record_ids":["R2", "R3"]
    })
    assert row["authority_correct"] is False
    assert row["stale_authority_error"] is True
    assert row["false_discard"] is False


def test_zh02_correct():
    row = scorer.score_case(zh02_case(), {
        "id":"ZH-02", "current_answer":"East Gate", "historical_answer":"South Gate",
        "current_authority_record_ids":["R2"]
    })
    assert row["authority_correct"] is True
    assert row["stale_authority_error"] is False
    assert row["false_discard"] is False


def test_duplicate_authority_ids_rejected():
    try:
        scorer.score_case(zh02_case(), {
            "id":"ZH-02", "current_answer":"East Gate", "historical_answer":"South Gate",
            "current_authority_record_ids":["R2", "R2"]
        })
    except ValueError as exc:
        assert "duplicate authority" in str(exc)
    else:
        raise AssertionError("duplicate authority IDs should fail")


def test_deterministic_output():
    cases = [zh01_case(), zh02_case()]
    submissions = [
        {"id":"ZH-01","current_answer":"45 seconds","historical_answer":"30 seconds","current_authority_record_ids":["R2"]},
        {"id":"ZH-02","current_answer":"East Gate","historical_answer":"South Gate","current_authority_record_ids":["R2"]},
    ]
    first = scorer.stable_json(scorer.score_cases(cases, submissions))
    second = scorer.stable_json(scorer.score_cases(cases, submissions))
    assert first == second
