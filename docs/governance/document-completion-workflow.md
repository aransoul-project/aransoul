# GitHub document completion workflow

Status: Candidate operational integration via repository agent instructions.

## Scope and endpoint

Use this workflow for a claim that specified regular document files were verified
at a GitHub branch snapshot. The existing
[checker](../../tools/document-completion/README.md) performs the readback.
[AGENTS.md](../../AGENTS.md) instructs repository agents to use it.
This adds no model benchmark, automatic CI job, branch protection or universal
ChatGPT enforcement. Agent adherence has not been measured.

## Procedure

1. Review the intended document bytes against the user's request. Fix repository,
   destination branch, required paths and SHA-256 expectations before the checker
   fetches. Include every document covered by the planned completion claim.
   Store the contract outside the files it verifies to avoid self-reference.
2. Perform the authorized publication. Record the actual destination's full
   commit SHA. A PR branch and main are distinct targets. After squash merge,
   carry forward reviewed file hashes and explicitly replace branch/commit with
   the actual merge destination. Never replace hashes with observed values merely
   to make the check pass.
3. From the repository root run:
   `python3 tools/document-completion/check.py CONTRACT --completion`.
   Capture this invocation's JSON and process exit code together. If saving output,
   use a fresh temporary output path; failure to start must not expose an old
   report as current evidence.
4. Require exit 0, status PASS and a non-null receipt. Match its repository,
   branch, commit and complete path set to the intended contract, and its time to
   the current report. Malformed, missing or inconsistent output is unverified.
5. Report the bounded result with the destination commit and source links. Stop
   when the user's agreed deliverable has been verified.

## Reporting decisions

| Observed outcome | Permitted report |
| --- | --- |
| PASS and valid current receipt | Specified file bytes verified at the named branch/commit and check time |
| FAIL | Verification failed; list version, missing/type or content mismatches returned by the checker |
| UNVERIFIED or tool cannot run | State completed actions separately; remote file verification remains unavailable |
| Local draft only | Draft prepared locally; no remote publication verification |
| PR branch PASS, main not checked | PR branch files verified; main completion is not established |

A moved branch fails a strict commit contract even when file contents are unchanged.
Review why it moved before explicitly amending the contract; do not silently retry
with whatever commit happens to be current. Tool failure is a reason to qualify
the report, not a reason to erase completed work or claim a failed publication.

## Evidence limits

A PASS checks snapshot bytes, not content quality, authorship, authorization,
earlier agent actions or continued persistence. A flawed expectation can match a
flawed implementation. Deletions, renames' source removal, non-document side
effects and files outside the contract require separate evidence; this checker
does not establish them.

The CLI suppresses its own completion receipt on failure. Repository instructions
require agents to use that result, but cannot prevent an agent from ignoring the
instructions or inventing a natural-language claim. Testing the CLI is not a test
of agent compliance. Mandatory runtime enforcement would require integration into
a specific host that controls the final response; that is outside this increment.

## Validation

The existing development suite checks success, wrong version/bytes, missing files,
symlinks, local drafts and receipt suppression/reuse. Run it with:
`python3 -m unittest discover -s tools/document-completion -p 'test_*.py' -v`.

For this instruction-only integration, verify relative links and exercise both a
valid remote contract and a deliberately wrong-version contract with the existing
CLI. These checks validate the referenced mechanism, not future agent adherence.
