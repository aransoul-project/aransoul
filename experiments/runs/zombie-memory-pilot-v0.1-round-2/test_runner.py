#!/usr/bin/env python3
"""Offline regression tests for the Round 2 execution runner."""

import importlib.util
import json
import unittest
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("zombie_memory_round2_runner", RUN_DIR / "runner.py")
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class Round2RunnerTests(unittest.TestCase):
    def setUp(self):
        self.config = runner.r1.load_json(runner.CONFIG_PATH)
        self.prompts = runner.r1.load_frozen_prompts(self.config)
        self.row = self.prompts["plain"][0]
        self.ids = runner.r1.record_ids(self.row["prompt"])

    def test_round2_shape(self):
        runner.validate_config(self.config)
        self.assertEqual(40, self.config["requests_per_replication"])
        self.assertEqual(3, len(self.config["replications"]))

    def test_provider_schema_is_compatible(self):
        schema = runner.response_schema(self.row["id"], self.ids)
        self.assertNotIn("uniqueItems", json.dumps(schema))

    def test_local_uniqueness_validation_remains(self):
        duplicate = self.ids[0]
        parsed = {
            "id": self.row["id"],
            "current_answer": "YES",
            "historical_answer": "YES",
            "current_authority_record_ids": [duplicate, duplicate],
        }
        with self.assertRaisesRegex(ValueError, "must be a unique list"):
            runner.validate_parsed(parsed, self.row["id"], self.ids)

    def test_frozen_prompt_hashes(self):
        for condition, relative_path in self.config["prompt_files"].items():
            with self.subTest(condition=condition):
                self.assertEqual(
                    self.config["prompt_sha256"][condition],
                    runner.r1.sha256(runner.REPO_ROOT / relative_path),
                )


if __name__ == "__main__":
    unittest.main()
