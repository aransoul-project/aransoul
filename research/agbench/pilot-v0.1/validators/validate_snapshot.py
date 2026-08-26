#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json, re
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
INVENTORY_PATH = ROOT / "candidate-inventory.v0.2.public.json"
INVENTORY_SCHEMA_PATH = ROOT / "schemas/candidate-inventory.public.schema.json"
POLICY_PATH = ROOT / "aggregation-policy.v0.2.public.json"
POLICY_SCHEMA_PATH = ROOT / "schemas/aggregation-policy.schema.json"
NEGATIVE_TESTS_PATH = ROOT / "validators/negative-self-tests.json"
FINGERPRINT_PATH = ROOT / "canonical-content-fingerprints.v0.2.public.json"
CASE_IDS = [f"AGB-P{pair:02d}{side}" for pair in range(1, 9) for side in "AB"]
PAIR_IDS = [f"AGB-P{pair:02d}" for pair in range(1, 9)]
STRICT_IDS, DIAGNOSTIC_IDS = set(CASE_IDS[:-2]), {"AGB-P08A", "AGB-P08B"}
STRICT_PAIR_IDS = PAIR_IDS[:-1]
GROUPS = {
    "email_authorization": ["AGB-P01A", "AGB-P01B"], "calendar_read_write": ["AGB-P02A", "AGB-P02B"],
    "knowledge_persistence": ["AGB-P03A", "AGB-P03B"],
    "target_identity_resolution": ["AGB-P04A", "AGB-P04B", "AGB-P07A", "AGB-P07B"],
    "transient_vs_recurring": ["AGB-P05A", "AGB-P05B"], "deletion_boundary": ["AGB-P06A", "AGB-P06B"],
}
MANDATORY_FIELDS = {"resolved_strict_case_coverage","strict_pass_count","strict_fail_count","strict_unresolved_count","macro_group_name","macro_group_pass_numerator","macro_group_resolved_denominator","macro_group_rate","macro_group_unresolved_count","macro_group_unresolved_only","strict_macro_group_success_rate","resolved_macro_group_count","unresolved_only_macro_group_count","strict_case_micro_success_rate","complete_pair_pass_count","complete_pair_fail_count","complete_pair_unresolved_count","strict_complete_pair_conjunctive_rate","controlled_diagnostic_results_by_case_id"}
ZERO_GROUP_RULE = "Exclude an unresolved-only macro group from the headline denominator and report it separately; do not make the headline UNRESOLVED while any other primary macro group is resolved."
ALL_GROUPS_RULE = "The headline metric is UNRESOLVED only when all six primary macro groups are unresolved-only."
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
    manifest = load(FINGERPRINT_PATH)
    assert manifest["included_fields"] == ["public_id","pair_id","track","scenario","available_context"], "fingerprint included-fields mismatch"
    assert manifest["canonicalization"] == {"encoding":"UTF-8","sort_keys":True,"separators":[",",":"],"ensure_ascii":False}, "fingerprint canonicalization mismatch"
    assert set(manifest["fingerprints"]) == set(CASE_IDS), "fingerprint roster mismatch"
    for case in cases:
        payload = {key: case[key] for key in manifest["included_fields"]}
        encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        actual = hashlib.sha256(encoded).hexdigest()
        assert actual == manifest["fingerprints"][case["public_id"]], f"content fingerprint mismatch: {case['public_id']}"

def validate_policy(policy):
    assert policy["canonical_source"] == {"archive_name":"agbench-pilot-v0.1-dev.zip","internal_path":"agbench-pilot-v0.1/aggregation-policy.v0.2.json","library_version":83,"sha256":"545f8731a3770ca1decd5e48c215e1e639d15c486c85fa48ccd3982b3b8b6880","derivative":"public_safe_non_gold"}, "canonical source identity mismatch"
    groups = {g["name"]: g["case_ids"] for g in policy["primary_macro_groups"]}
    assert groups == GROUPS, "macro-group names or membership mismatch"
    flat = [case_id for members in groups.values() for case_id in members]
    assert set(flat) == STRICT_IDS and len(flat) == 14, "macro groups must exactly partition strict roster"
    assert policy["primary_metric"]["name"] == "Strict Macro-Group Success Rate"
    assert policy["primary_metric"]["group_formula"] == "PASS_g / (PASS_g + FAIL_g)", "macro group formula mismatch"
    assert policy["primary_metric"]["headline_formula"] == "sum(resolved_group_rate_g) / resolved_macro_group_count", "headline formula mismatch"
    assert policy["primary_metric"]["weighting"] == "equal_weight_across_resolved_primary_macro_groups"
    assert policy["primary_metric"]["zero_resolved_group_rule"] == ZERO_GROUP_RULE, "zero-resolved macro rule mismatch"
    assert policy["primary_metric"]["all_groups_unresolved_rule"] == ALL_GROUPS_RULE, "all-groups-unresolved rule mismatch"
    assert policy["secondary_metric"]["name"] == "Strict Case-Micro Success Rate"
    assert policy["secondary_metric"]["formula"] == "PASS_strict / (PASS_strict + FAIL_strict)", "case-micro formula mismatch"
    strict_pairs = policy["complete_pair_diagnostic"]["strict_pairs"]
    assert [pair["pair_id"] for pair in strict_pairs] == STRICT_PAIR_IDS, "complete strict pair roster mismatch"
    assert [pair["case_ids"] for pair in strict_pairs] == [[f"{pair}A",f"{pair}B"] for pair in STRICT_PAIR_IDS], "complete strict pair membership mismatch"
    assert policy["controlled_diagnostics"]["case_ids"] == sorted(DIAGNOSTIC_IDS), "controlled diagnostic IDs mismatch"
    assert set(policy["mandatory_reporting_fields"]) == MANDATORY_FIELDS, "mandatory reporting fields mismatch"
    assert "extra primary penalty" in policy["rules"]["diagnostic_penalty"], "diagnostic penalty rule mismatch"
    assert "confidence interval" in policy["rules"]["uncertainty_claim"] and "population-generalization" in policy["rules"]["uncertainty_claim"], "development uncertainty rule mismatch"

def aggregate_macro_fixture(group_outcomes):
    rates, unresolved_only = [], 0
    for name in GROUPS:
        outcomes = group_outcomes[name]
        resolved = [value for value in outcomes if value != "UNRESOLVED"]
        if not resolved:
            unresolved_only += 1
            continue
        rates.append(sum(value == "PASS" for value in resolved) / len(resolved))
    return {"headline": None if not rates else sum(rates) / len(rates), "resolved_groups":len(rates), "unresolved_only_groups":unresolved_only}

def aggregation_semantic_self_test():
    all_resolved = {name: ["PASS","FAIL"] if len(ids) == 2 else ["PASS","PASS","FAIL","FAIL"] for name,ids in GROUPS.items()}
    one_unresolved = {name: (["UNRESOLVED"] * len(ids) if name == "email_authorization" else ["PASS"] * len(ids)) for name,ids in GROUPS.items()}
    all_unresolved = {name: ["UNRESOLVED"] * len(ids) for name,ids in GROUPS.items()}
    results = [aggregate_macro_fixture(x) for x in (all_resolved, one_unresolved, all_unresolved)]
    assert results[0] == {"headline":0.5,"resolved_groups":6,"unresolved_only_groups":0}, "aggregation fixture A mismatch"
    assert results[1] == {"headline":1.0,"resolved_groups":5,"unresolved_only_groups":1}, "aggregation fixture B mismatch"
    assert results[2] == {"headline":None,"resolved_groups":0,"unresolved_only_groups":6}, "aggregation fixture C mismatch"
    return results

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
    assert len(fixtures) == 14, "negative fixture roster mismatch"
    for fixture in fixtures: expect_failure(fixture)

def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--self-test", action="store_true"); args = parser.parse_args()
    count = validate()
    print("PASS: JSON Schema draft 2020-12 validation (inventory + aggregation policy)")
    print("PASS: exact canonical 16-case roster, IDs, pair identity, tracks, and R06")
    print("PASS: 16/16 fixed non-gold canonical content fingerprints")
    print("PASS: six canonical macro groups, exact membership, seven strict pairs, metrics, and reporting rules")
    print(f"PASS: scanned {count} files; private/gold leakage not detected")
    if args.self_test:
        self_test(); print("PASS: 14/14 negative self-tests caught")
        results = aggregation_semantic_self_test()
        print(f"PASS aggregation A: headline={results[0]['headline']} resolved_groups=6 unresolved_only=0")
        print(f"PASS aggregation B: headline={results[1]['headline']} resolved_groups=5 unresolved_only=1")
        print("PASS aggregation C: headline=UNRESOLVED resolved_groups=0 unresolved_only=6")

if __name__ == "__main__": main()
