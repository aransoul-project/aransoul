import json
from pathlib import Path

from semantic_grader import ALLOWED_LABELS, grade


ROOT = Path(__file__).resolve().parent
DATASET = ROOT / "semantic-scoring-synthetic-v0.1.json"


def test_frozen_synthetic_labels():
    cases = json.loads(DATASET.read_text(encoding="utf-8"))
    assert len(cases) == 18
    results = {
        case["id"]: grade(case["question"], case["gold"], case["candidate"])
        for case in cases
    }
    assert all(label in ALLOWED_LABELS for label in results.values())
    failures = {
        case["id"]: {"expected": case["expected"], "actual": results[case["id"]]}
        for case in cases
        if results[case["id"]] != case["expected"]
    }
    assert failures == {}
