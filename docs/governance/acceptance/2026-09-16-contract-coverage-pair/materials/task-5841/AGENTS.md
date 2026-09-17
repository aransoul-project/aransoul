# Repository agent instructions

## GitHub document completion claims

For tasks that publish or update regular document files in this GitHub repository,
follow [the document completion workflow](docs/governance/document-completion-workflow.md)
before claiming that the specified remote files have been verified.

- Fix the intended repository, destination branch, paths and expected byte hashes
  from reviewed intended content before the verification fetch.
- Run `python3 tools/document-completion/check.py CONTRACT --completion` after
  publication, using the actual full destination commit SHA.
- Require the current invocation's exit code 0, PASS status and matching non-null
  completion receipt before making the scoped remote-file verification claim.
- On FAIL, UNVERIFIED, missing output or unavailable execution, report the actual
  completed actions and the unverified items. Do not reuse an earlier receipt or
  treat a local draft, push response or PR creation as verified main-branch content.
- Verification does not authorize publication or merge. Honor the user's actual
  task authorization; do not request it again when already granted.
- These instructions govern completion reporting, not permission to answer
  questions, review code, save drafts or explain blockers. Do not require a remote
  PASS for tasks that do not claim publication of remote document files.

This is an agent instruction, not a runtime-enforced ChatGPT response filter.
The checker remains a Candidate prototype; EREQ remains Candidate and AGBench
remains paused. Do not infer broader research or capability claims from PASS.
