# Project Status

## Current state

**Version:** `0.2.0`  
**Lifecycle:** Stable / dogfooding  
**Core workflow:** Functionally complete

The project has reached its intended current scope: a reusable, architecture-governed workflow for adopting AI coding agents into a bounded, traceable software engineering process.

## Stable baseline

The current baseline includes:

- repository-wide and local `AGENTS.md` governance;
- compact authoritative `PROJECT_CONTEXT.md`;
- architecture principles and ADR model;
- roadmap-driven bounded PR decomposition;
- reusable prompts for first/next PR selection, implementation, independent review, and remediation;
- explicit local validation and baseline-failure handling;
- guided bootstrap/adoption workflow;
- machine-checkable bootstrap readiness validator and regression tests;
- worked example and reviewer/adoption guidance.

## What happens next

The project is intentionally not entering continuous feature development. The next phase is real-project adoption and observation.

Acceptable changes during dogfooding:

- correctness fixes;
- security fixes;
- broken-link or contradictory-documentation fixes;
- clearer examples and wording based on observed confusion;
- compatibility updates required by actual coding-agent/tool changes;
- workflow changes backed by repeated adoption evidence.

Changes that should normally wait:

- interactive bootstrap CLI/wizard;
- automatic prompt generation engines;
- agent orchestration frameworks;
- hosted services or dashboards;
- technology-specific application scaffolding;
- speculative abstractions without demonstrated adoption pain.

## Evidence threshold for v0.3

A new feature-oriented minor version should be considered only when at least one of these conditions is met:

1. the template has been used on multiple real projects and the same adoption failure/friction repeats;
2. a current workflow step is demonstrably error-prone despite documentation and validation;
3. an upstream coding-agent/platform change invalidates an important workflow assumption;
4. a security or governance requirement cannot be addressed as a maintenance-level change.

The purpose of this threshold is to keep the repository a focused engineering template rather than allowing it to grow into an unrelated agent platform.

## Feedback to capture during dogfooding

For each real adoption, record only actionable observations:

- which bootstrap step required clarification;
- which project fact was difficult to encode in `PROJECT_CONTEXT.md`;
- whether bounded PR selection was consistently small enough;
- where agents still guessed despite governance;
- which validation evidence reviewers lacked;
- which manual step was repeated often enough to justify automation.

Use this evidence, rather than feature speculation, to shape any future `v0.3` roadmap.