#!/usr/bin/env python3
"""Regression tests for deterministic Zombie Memory pilot diagnostics."""

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PILOT_DIR = Path(__file__).resolve().parent
CASES_PATH = PILOT_DIR / "cases.json"
EXAMPLE_PATH = PILOT_DIR / "example-output.json"
SCORER_PATH = PILOT_DIR / "scorer.py"


class FalseDiscardDiagnosticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = json.loads(EXAMPLE_PATH.read_text(encoding="utf-8"))

    def score(self, submission):
        with tempfile.TemporaryDirectory() as tmp_dir:
            submission_path = Path(tmp_dir) / "submission.json"
            submission_path.write_text(json.dumps(submission), encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(SCORER_PATH), str(CASES_PATH), str(submission_path)],
                check=True,
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
        return json.loads(completed.stdout)

    def p05_submission(self, current_answer, selected_ids):
        submission = copy.deepcopy(self.example)
        row = next(row for row in submission if row["id"] == "ZM-P05")
        row["current_answer"] = current_answer
        row["current_authority_record_ids"] = selected_ids
        return submission

    def test_gold_submission_has_no_false_discard(self):
        result = self.score(self.example)
        self.assertEqual(0, result["summary"]["false_discard_case_count"])
        self.assertEqual(1.0, result["summary"]["current_answer_accuracy"])
        self.assertEqual(1.0, result["summary"]["historical_recall_accuracy"])
        self.assertEqual(1.0, result["summary"]["authority_resolution_accuracy"])

    def test_wrong_answer_missing_required_old_record_is_flagged(self):
        result = self.score(self.p05_submission("NO", ["R2"]))
        detail = next(row for row in result["details"] if row["id"] == "ZM-P05")
        self.assertTrue(detail["false_discard_indicator"])
        self.assertEqual(1, result["summary"]["false_discard_case_count"])

    def test_wrong_answer_with_required_old_record_is_not_flagged(self):
        result = self.score(self.p05_submission("NO", ["R1", "R2"]))
        self.assertEqual(0, result["summary"]["false_discard_case_count"])

    def test_correct_answer_need_not_select_noncontrolling_old_record(self):
        result = self.score(self.p05_submission("YES", ["R2"]))
        self.assertEqual(0, result["summary"]["false_discard_case_count"])


if __name__ == "__main__":
    unittest.main()
