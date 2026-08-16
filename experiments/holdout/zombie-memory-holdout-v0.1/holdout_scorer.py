#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CANDIDATES = ROOT / "candidates"
CONDITIONS = ["plain", "timestamp", "status", "ttea"]
CASE_IDS = [f"ZH-{i:02d}" for i in range(1, 25)]


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def norm_answer(value):
    return str(value).strip().upper()


def norm_ids(values):
    return sorted(str(v).strip() for v in (values or []))


def score_one(gold, row):
    selected = norm_ids(row.get("current_authority_record_ids", []))
    expected = norm_ids(gold.get("current_authority_record_ids", []))
    stale = set(norm_ids(gold.get("stale_record_ids", [])))
    selected_set = set(selected)
    expected_set = set(expected)
    return {
        "current_correct": norm_answer(row.get("current_answer", "")) == norm_answer(gold.get("current_answer", "")),
        "historical_correct": norm_answer(row.get("historical_answer", "")) == norm_answer(gold.get("historical_answer", "")),
        "authority_correct": selected == expected,
        "stale_authority_error": bool(stale.intersection(selected_set)),
        "false_discard": not expected_set.issubset(selected_set),
    }


def fixture_paths():
    for cid in CASE_IDS:
        path = CANDIDATES / cid / "scorer-fixture.json"
        if not path.exists():
            raise SystemExit(f"missing fixture: {path}")
        yield cid, path


def self_test():
    checks = 0
    for cid, path in fixture_paths():
        fixture = load_json(path)
        gold = fixture["case"]["gold"]
        correct = score_one(gold, fixture["correct_submission"])
        for key in ("current_correct", "historical_correct", "authority_correct"):
            if not correct[key]:
                raise AssertionError(f"{cid} correct submission failed {key}")
        if correct["stale_authority_error"]:
            raise AssertionError(f"{cid} correct submission selected stale authority")
        if correct["false_discard"]:
            raise AssertionError(f"{cid} correct submission false-discarded authority")
        checks += 1
        for negative in fixture.get("negative_checks", []):
            actual = score_one(gold, negative["submission"])
            for key, expected in negative.get("expect", {}).items():
                if key not in actual:
                    continue
                if actual[key] != expected:
                    raise AssertionError(
                        f"{cid}/{negative['name']} {key}: expected {expected}, got {actual[key]}"
                    )
                checks += 1
    return {"status": "fixture_self_test_pass", "cases": 24, "assertions_checked": checks}


def load_gold():
    result = {}
    families = {}
    for cid in CASE_IDS:
        candidate = load_json(CANDIDATES / cid / "candidate.json")
        result[cid] = candidate["gold"]
        families[cid] = candidate["family"]
    return result, families


def load_responses(path):
    rows = []
    with Path(path).open("r", encoding="utf-8") as stream:
        for line in stream:
            if line.strip():
                record = json.loads(line)
                if record.get("parse_status") != "parsed":
                    raise ValueError("all scored rows must be parsed")
                rows.append(record)
    if len(rows) != 96:
        raise ValueError(f"expected 96 rows, got {len(rows)}")
    return rows


def empty_bucket():
    return {"n": 0, "current": 0, "historical": 0, "authority": 0, "stale": 0, "false_discard": 0}


def add(bucket, scored):
    bucket["n"] += 1
    bucket["current"] += int(scored["current_correct"])
    bucket["historical"] += int(scored["historical_correct"])
    bucket["authority"] += int(scored["authority_correct"])
    bucket["stale"] += int(scored["stale_authority_error"])
    bucket["false_discard"] += int(scored["false_discard"])


def summarize(bucket):
    n = bucket["n"] or 1
    return {
        "responses": bucket["n"],
        "current_answer_accuracy": bucket["current"] / n,
        "historical_answer_accuracy": bucket["historical"] / n,
        "authority_exact_set_accuracy": bucket["authority"] / n,
        "stale_authority_error_count": bucket["stale"],
        "stale_authority_error_rate": bucket["stale"] / n,
        "false_discard_count": bucket["false_discard"],
        "false_discard_rate": bucket["false_discard"] / n,
    }


def aggregate_score(responses_path):
    self_test_result = self_test()
    gold, _ = load_gold()
    rows = load_responses(responses_path)
    overall = empty_bucket()
    by_condition = {condition: empty_bucket() for condition in CONDITIONS}
    for record in rows:
        cid = record["case_id"]
        condition = record["condition"]
        if cid not in gold or condition not in by_condition:
            raise ValueError("unexpected case or condition")
        scored = score_one(gold[cid], record["parsed_response"])
        add(overall, scored)
        add(by_condition[condition], scored)
    return {
        "status": "aggregate_scoring_complete",
        "fixture_self_test": self_test_result,
        "inspection_level": "aggregate_only_no_individual_details",
        "overall": summarize(overall),
        "by_condition": {key: summarize(value) for key, value in by_condition.items()},
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--responses")
    parser.add_argument("--output")
    args = parser.parse_args()
    if args.self_test:
        print(json.dumps(self_test(), ensure_ascii=False, indent=2))
        return
    if not args.responses or not args.output:
        raise SystemExit("use --self-test or provide --responses and --output")
    result = aggregate_score(args.responses)
    Path(args.output).write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
