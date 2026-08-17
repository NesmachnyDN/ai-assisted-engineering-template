# PR-Specific Prompt Design Standard

A PR-specific prompt is an execution contract between project governance and an AI coding agent. It should reduce ambiguity without hard-coding incidental implementation details.

## Required sections

Every implementation prompt should state:

1. **Objective** — one bounded outcome.
2. **Why this change is next** — roadmap/dependency rationale.
3. **Authoritative context** — files/areas the agent must inspect.
4. **Dependencies** — predecessor work/decisions that must already exist.
5. **Scope** — behavior/files/areas that may change.
6. **Non-goals** — adjacent work that must not be pulled in.
7. **Architecture boundaries and invariants** — what must remain true.
8. **Acceptance criteria** — observable completion conditions.
9. **Validation** — tests/checks/evidence required.
10. **Documentation obligations** — roadmap/ADR/contracts if affected.
11. **Stop conditions** — architecture ambiguity or scope-growth triggers.

## Prompt quality rules

- Prefer outcomes and invariants over line-by-line implementation instructions.
- Do not repeat entire repository governance inside every prompt; reference authoritative files.
- Include repository paths when they prevent ambiguity.
- Use exact commands only when the project actually defines them.
- Do not ask the agent to invent pass counts, CI results, performance metrics, or completion evidence.
- Do not state architecture assumptions as facts when they are unresolved.
- Avoid mixing implementation and independent-review roles in the same execution step.
- Keep the prompt specific to one bounded PR.

## Bad prompt signals

A prompt should be redesigned when it:

- contains several independent features;
- says "refactor as needed" without boundaries;
- asks for "best architecture" without authoritative constraints;
- mandates a new framework/library without a project decision;
- includes future-roadmap work "while you are there";
- defines acceptance only as "tests pass";
- relies on conversation history instead of repository context;
- cannot state meaningful non-goals.

## Acceptance criteria quality

Good acceptance criteria are observable and behavior-oriented:

- `Concurrent duplicate requests cannot persist duplicate delivery records.`
- `Legacy API consumers continue to receive the existing response schema.`

Weak criteria are implementation claims:

- `Use a clean architecture.`
- `Code should be high quality.`
- `Add necessary classes.`

## Stop condition pattern

Use explicit language such as:

> If authoritative context does not determine `<material decision>`, stop and report an architecture blocker containing the missing decision, affected scope, and viable alternatives. Do not silently choose an option.

## Traceability

When PR-specific prompts are versioned in the repository, the PR should link to the exact prompt path and the roadmap item it implements. If the prompt is updated during remediation, preserve enough history in Git to explain why the execution contract changed.