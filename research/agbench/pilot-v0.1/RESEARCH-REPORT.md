# AGBench Pilot v0.1 — Development Research Report

## Purpose

AGBench Pilot v0.1 is a small synthetic research program for evaluating observable agent-governance boundaries: when an agent should answer, inspect, preview, clarify, commit an external action, or avoid an unauthorized effect.

The present repository snapshot captures the design after static measurement-design consolidation. The work is paused at this boundary so that later implementation or live execution cannot be mistaken for a continuation already authorized by the static review.

## Current design state

The consolidated inventory contains 16 synthetic cases: 14 strict-primary cases and 2 controlled-scope diagnostics. The primary material is organized into six macro groups and seven complete strict contrast pairs. Six repairs are recorded in the development provenance.

Offline validation for P0, P1, inventory structure, aggregation logic, and final consolidation was reported as passing before this snapshot was prepared.

## Measurement principle

The target is observable behavior and externally inspectable effects, not hidden reasoning labels. A case is useful only when its pass/fail boundary can be grounded in channels such as response text, tool calls, or post-state.

The public inventory therefore includes canonical case/pair identity, measurement track, scenario text, and supplied observable context, and is not direct model input. Expected behavior and adjudication belong to a separate private evaluation layer and are intentionally absent here.

## Scope limits

This snapshot makes no model-performance claim. It contains no live responses and authorizes no provider execution. It is not frozen, preregistered, released, or suitable to cite as a completed benchmark result.

## Provenance note

The public-safe snapshot is a curated derivative of a larger private development package. Selection is intentionally lossy: public preservation is favored over exhaustive archival when exhaustive archival would expose reviewer-only or gold-bearing material.

The current public-safe snapshot does not assert that every historical development artifact has been reproduced here. The authoritative claim is narrower: the included files document the static design state without intentionally carrying evaluation answers or blind mappings.
