# Changelog

All notable template changes are documented here.

## Unreleased

The project is in stable/dogfooding mode. Further feature automation is intentionally deferred until justified by repeated real-world adoption feedback.

## 0.2.0 — 2026-08-17

### Added

- guided bootstrap/adoption workflow for new projects;
- machine-checkable bootstrap readiness validator;
- regression tests for validator behavior;
- bootstrap documentation index and validator contract;
- five-minute quickstart, decision table, ownership guidance, FAQ, reviewer checklist, and manual smoke test;
- explicit prompt-design quality guidance and first-PR bootstrap gate.

### Changed

- made bootstrap the primary entry path for new users;
- separated machine-verifiable readiness checks from qualitative architecture/reviewer decisions;
- clarified that hosted CI is optional when project policy defines local validation as authoritative;
- established `v0.2.0` as the stable baseline for real-project dogfooding.

## 0.1.0

### Added

- root `AGENTS.md` governance model;
- `PROJECT_CONTEXT.md` project contract;
- architecture, roadmap, ADR, testing, documentation, and prompt-design templates;
- bounded PR implementation, review, and remediation prompts;
- worked example and repository contribution/security guidance.