#!/usr/bin/env python3
"""Regression tests for the experiment-side Zombie Memory runner."""

import importlib.util
import json
import unittest
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("zombie_memory_runner", RUN_DIR / "runner.py")
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class RunnerSchemaCompatibilityTests(unittest.TestCase):
    def setUp(self):
        self.config = runner.load_json(runner.CONFIG_PATH)
        self.prompts = runner.load_frozen_prompts(self.config)
        self.row = self.prompts[self.config["conditions"][0]][0]
        self.allowed_ids = runner.record_ids(self.row["prompt"])

    def test_provider_schema_omits_unique_items(self):
        schema = runner.response_schema(self.row["id"], self.allowed_ids)
        self.assertNotIn(
            "uniqueItems",
            schema["properties"]["current_authority_record_ids"],
        )
        self.assertNotIn("uniqueItems", json.dumps(schema))

    def test_local_validator_rejects_duplicate_authority_ids(self):
        duplicate_id = self.allowed_ids[0]
        parsed = {
            "id": self.row["id"],
            "current_answer": "YES",
            "historical_answer": "YES",
            "current_authority_record_ids": [duplicate_id, duplicate_id],
        }
        with self.assertRaisesRegex(ValueError, "must be a unique list"):
            runner.validate_parsed(parsed, self.row["id"], self.allowed_ids)

    def test_frozen_prompt_hashes_match_config(self):
        for condition, relative_path in self.config["prompt_files"].items():
            with self.subTest(condition=condition):
                self.assertEqual(
                    self.config["prompt_sha256"][condition],
                    runner.sha256(runner.REPO_ROOT / relative_path),
                )


if __name__ == "__main__":
    unittest.main()
