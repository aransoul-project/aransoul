# External Action Verification

Status: **Operational companion to governance and tool-execution controls**

AranSoul distinguishes **producing an answer** from **completing work in the external world**.

A model can generate correct content while the actual task still fails because a tool call was never sent, the target system rejected it, the change did not persist, or the change landed in the wrong place.

This document explains how to verify completion after an action is authorized. It does not itself grant permission to perform the action; authorization is governed by the canonical authority and process documents.

## Five external completion states

### 1. Generated
The content or intended action has been produced internally.

This does **not** mean any external system has changed.

### 2. Sent
A tool request or write operation has been issued.

This still does not prove the target system accepted or applied it.

### 3. Reached
The external system reports successful receipt or execution.

A successful API response is stronger evidence, but it may still be insufficient when persistence or placement matters.

### 4. Persisted
The resulting content or state can be read back from the external system.

Read-back is especially important for long-running workflows, APIs with eventual consistency, or interfaces where app and web views can disagree temporarily.

### 5. Correctly placed
The result exists in the correct resource, branch, page, section, classification, version, or governance layer.

This is the strongest completion state in the sequence.

## Why this distinction matters

Without explicit verification, an agent may report success at the wrong boundary.

Examples:

- a document was generated but never uploaded;
- a GitHub file was created on the wrong branch;
- a Notion page exists but under the wrong parent;
- an update persisted but was classified as current when it should have been historical;
- an API returned success but the expected field was not actually changed.

## Verification depth should match risk

Not every action needs the same amount of checking.

Low-risk, easily reversible actions may only require confirmation that the target system accepted the request.

Higher-risk actions should add read-back and placement verification, especially when they involve:

- formal governance documents;
- irreversible deletion;
- publication;
- branch or release changes;
- long-running batch edits;
- permission or authorization changes;
- records where duplicate writes are costly.

## Reversibility and rollback

Before meaningful external actions, record or understand:

- what is about to change;
- where the change will land;
- whether it is reversible;
- what prior state would be needed for rollback;
- what evidence will count as successful completion.

For multi-step operations, preserve checkpoints rather than treating the whole process as one opaque success/failure event.

## Avoiding duplicate execution

When an external response is ambiguous, do not immediately repeat the write.

First check whether the original operation may already have succeeded. Blind retry can create duplicate pages, duplicate issues, repeated notifications, or conflicting versions.

A safer sequence is:

1. inspect the target state;
2. determine whether the prior operation persisted;
3. retry only if the required state is still absent.

## Source-of-truth rule

The agent's own prior statement that an action succeeded is not sufficient evidence that the action succeeded.

For externally meaningful work, completion should be grounded in the external system's observable state whenever practical.

> 言成於內，未必事成於外；工經其界，須驗其達、驗其存、驗其位。
