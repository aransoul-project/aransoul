#!/usr/bin/env python3
from pathlib import Path
import argparse, json, re
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
INVENTORY_PATH = ROOT / "candidate-inventory.v0.2.public.json"
INVENTORY_SCHEMA_PATH = ROOT / "schemas/candidate-inventory.public.schema.json"
POLICY_PATH = ROOT / "aggregation-policy.v0.2.public.json"
POLICY_SCHEMA_PATH = ROOT / "schemas/aggregation-policy.schema.json"
NEGATIVE_TESTS_PATH = ROOT / "validators/negative-self-tests.json"
CASE_IDS = [f"AGB-P{pair:02d}{side}" for pair in range(1, 9) for side in "AB"]
PAIR_IDS = [f"AGB-P{pair:02d}" for pair in range(1, 9)]
STRICT_IDS, DIAGNOSTIC_IDS = set(CASE_IDS[:-2]), {"AGB-P08A", "AGB-P08B"}
STRICT_PAIR_IDS = PAIR_IDS[:-1]
GROUPS = {
    "email": ["AGB-P01A", "AGB-P01B"], "calendar": ["AGB-P02A", "AGB-P02B"],
    "knowledge_persistence": ["AGB-P03A", "AGB-P03B"],
    "target_identity_resolution": ["AGB-P04A", "AGB-P04B", "AGB-P07A", "AGB-P07B"],
    "transient_vs_recurring": ["AGB-P05A", "AGB-P05B"], "deletion": ["AGB-P06A", "AGB-P06B"],
}
MANDATORY_FIELDS = {"strict_macro_group_success_rate","strict_case_micro_success_rate","strict_complete_pair_conjunctive_rate","strict_pass_count","strict_fail_count","strict_unresolved_count","strict_unresolved_reasons","macro_group_name","macro_group_pass_numerator","macro_group_resolved_denominator","macro_group_rate","macro_group_unresolved_count","complete_pair_pass_count","complete_pair_fail_count","complete_pair_unresolved_count","controlled_diagnostic_results_by_case_id"}
FORBIDDEN_FILENAMES = [re.compile(x, re.I) for x in (r"answer[-_ ]?key",r"blind[-_ ]?(id[-_ ]?)?map",r"reviewer[-_ ]?(only|packet|response|submission)",r"adjudicator[-_ ]?(submission|packet|response)",r"sealed")]
FORBIDDEN_JSON_KEYS = {"expected_label","gold_label","answer_key","private_map","blind_id","required_behavior_atoms","forbidden_behavior_atoms","best_action_mode","best_observable_behavior","observable_pass","observable_fail","candidate_expected_outcome","first_adjudicator_label","second_adjudicator_label","selected_label","review_metadata","adjudication"}
SUSPICIOUS_BLIND_ID = re.compile(r'"blind_id"\s*:\s*"[A-Z]+[0-9]{2,}"', re.I)

def load(path): return json.loads(path.read_text(encoding="utf-8"))

def schema_validate(instance, schema, label):
    Draft202012Validator.check_schema(schema)
    errors = sorted(Draft202012Validator(schema).iter_errors(instance), key=lambda e: list(e.path))
    assert not errors, f"{label} schema: " + "; ".join(e.message for e in errors)

def walk_json(value, path="$"):
    if isinstance(value, dict):
        for key, child in value.items():
            assert key not in FORBIDDEN_JSON_KEYS, f"forbidden JSON key {key!r} at {path}"
            walk_json(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value): walk_json(child, f"{path}[{index}]")

def validate_leakage():
    files = [path for path in ROOT.rglob("*") if path.is_file() and "__pycache__" not in path.parts]
    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        assert not any(rx.search(relative) for rx in FORBIDDEN_FILENAMES), f"forbidden filename: {relative}"
        if path.suffix.lower() in {".json", ".md", ".py", ".txt"}:
            text = path.read_text(encoding="utf-8")
            if path.name != "validate_snapshot.py": assert not SUSPICIOUS_BLIND_ID.search(text), f"suspicious blind-id payload in {relative}"
            if path.suffix == ".json": walk_json(json.loads(text))
    return len(files)

def validate_inventory(inv):
    cases = inv["cases"]
    assert [case["public_id"] for case in cases] == CASE_IDS, "canonical case roster/order mismatch"
    by_id = {case["public_id"]: case for case in cases}
    assert len(by_id) == 16, "case IDs are not unique"
    for case_id, case in by_id.items(): assert case["pair_id"] == case_id[:-1], f"pair identity mismatch: {case_id}"
    assert {i for i,c in by_id.items() if c["track"] == "strict_primary"} == STRICT_IDS, "exact strict roster mismatch"
    assert {i for i,c in by_id.items() if c["track"] == "controlled_scope_diagnostic"} == DIAGNOSTIC_IDS, "exact diagnostic roster mismatch"
    assert "（使用者目前時區）" in by_id["AGB-P02A"]["scenario"], "P02A R06 timezone scenario repair missing"
    assert by_id["AGB-P02A"]["available_context"].get("time_zone_resolved") is True, "P02A R06 time_zone_resolved repair missing"
    assert all(by_id[x]["track"] == "strict_primary" for x in ("AGB-P05A","AGB-P05B")), "P05 pair must be strict"
    assert all(by_id[x]["track"] == "controlled_scope_diagnostic" for x in ("AGB-P08A","AGB-P08B")), "P08 pair must be controlled diagnostic"
    assert inv["inventory_summary"] == {"synthetic_cases":16,"strict_primary":14,"controlled_scope_diagnostics":2,"primary_macro_groups":6,"complete_strict_contrast_pairs":7,"recorded_repairs":6}, "inventory summary mismatch"

def validate_policy(policy):
    groups = {g["name"]: g["case_ids"] for g in policy["primary_macro_groups"]}
    assert groups == GROUPS, "macro-group names or membership mismatch"
    flat = [case_id for members in groups.values() for case_id in members]
    assert set(flat) == STRICT_IDS and len(flat) == 14, "macro groups must exactly partition strict roster"
    assert policy["primary_metric"]["name"] == "Strict Macro-Group Success Rate"
    assert policy["primary_metric"]["weighting"] == "six_macro_groups_equal_weight"
    assert policy["secondary_metric"]["name"] == "Strict Case-Micro Success Rate"
    assert policy["complete_pair_diagnostic"]["strict_pair_ids"] == STRICT_PAIR_IDS, "complete strict pair roster mismatch"
    assert policy["controlled_diagnostics"]["case_ids"] == sorted(DIAGNOSTIC_IDS), "controlled diagnostic IDs mismatch"
    assert set(policy["mandatory_reporting_fields"]) == MANDATORY_FIELDS, "mandatory reporting fields mismatch"
    for section in (policy["primary_metric"],policy["secondary_metric"],policy["complete_pair_diagnostic"]):
        assert "UNRESOLVED" in section["unresolved_rule"], "UNRESOLVED reporting rule missing"

def validate(inv=None, policy=None, scan=True):
    inv, policy = (load(INVENTORY_PATH) if inv is None else inv), (load(POLICY_PATH) if policy is None else policy)
    walk_json(inv); walk_json(policy)
    validate_inventory(inv); validate_policy(policy)
    schema_validate(inv, load(INVENTORY_SCHEMA_PATH), "inventory")
    schema_validate(policy, load(POLICY_SCHEMA_PATH), "aggregation policy")
    return validate_leakage() if scan else None

def mutate_fixture(document, fixture):
    parent = document
    for component in fixture["path"][:-1]: parent = parent[component]
    leaf = fixture["path"][-1]
    if fixture["operation"] == "set": parent[leaf] = fixture["value"]
    elif fixture["operation"] == "delete": del parent[leaf]
    elif fixture["operation"] == "remove_value": parent[leaf].remove(fixture["value"])
    else: raise AssertionError(f"unknown negative-fixture operation: {fixture['operation']}")

def expect_failure(fixture):
    inv, policy = load(INVENTORY_PATH), load(POLICY_PATH)
    mutate_fixture(inv if fixture["target"] == "inventory" else policy, fixture)
    try: validate(inv, policy, scan=False)
    except (AssertionError, KeyError) as error:
        assert fixture["expected_error"] in str(error), f"negative {fixture['name']!r} failed for wrong reason: {error}"
        print(f"PASS negative: {fixture['name']} -> {fixture['expected_error']}")
        return
    raise AssertionError(f"negative self-test was not caught: {fixture['name']}")

def self_test():
    fixtures = load(NEGATIVE_TESTS_PATH)
    assert len(fixtures) == 9, "negative fixture roster mismatch"
    for fixture in fixtures: expect_failure(fixture)

def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--self-test", action="store_true"); args = parser.parse_args()
    count = validate()
    print("PASS: JSON Schema draft 2020-12 validation (inventory + aggregation policy)")
    print("PASS: exact canonical 16-case roster, IDs, pair identity, tracks, and R06")
    print("PASS: six macro groups, exact membership, seven strict pairs, metrics, and reporting rules")
    print(f"PASS: scanned {count} files; private/gold leakage not detected")
    if args.self_test: self_test(); print("PASS: 9/9 negative self-tests caught")

if __name__ == "__main__": main()
