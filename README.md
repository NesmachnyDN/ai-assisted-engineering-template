# AI-Assisted Engineering Template

A reusable, architecture-governed project template for AI-assisted software engineering.

This repository is designed for teams and individual engineers who want AI coding agents to work inside explicit architectural, quality, testing, and review guardrails rather than treating prompts as disposable chat instructions.

> The central idea: AI may accelerate engineering, but project truth, architecture boundaries, validation evidence, and merge decisions remain governed engineering artifacts.

## Core workflow

```text
Project context
    ↓
Architecture constraints
    ↓
Roadmap
    ↓
One bounded PR
    ↓
PR-specific implementation prompt
    ↓
AI-assisted implementation
    ↓
Local validation
    ↓
Independent full-diff review
    ↓
Remediation of blockers
    ↓
Merge
    ↓
Roadmap update
```

See [`doc/workflow.md`](doc/workflow.md) for the detailed operating model.

## Principles

- **Authoritative context before implementation.** Agents must read project governance, architecture, roadmap, and applicable local instructions before changing code.
- **Architecture ambiguity is a blocker.** An AI agent must not silently invent a material architecture decision when authoritative context does not determine it.
- **One PR, one bounded objective.** Keep changes reviewable, traceable, and reversible.
- **Prompts are versioned engineering artifacts.** Store PR-specific implementation and remediation prompts with the project when traceability matters.
- **Implementation and review are separate concerns.** Review the actual diff and repository state independently of implementation claims.
- **Tests are evidence, not decoration.** Record exact validation commands and results. Distinguish pre-existing baseline failures from regressions introduced by the change.
- **Roadmap state follows repository reality.** Update planning artifacts only after implementation/review outcomes justify the state transition.
- **Human governance remains explicit.** AI can propose, implement, test, and review; material architecture and merge authority follow project policy.

## Quick start

1. Create a repository from this template.
2. Replace placeholders in `PROJECT_CONTEXT.md`.
3. Tailor root `AGENTS.md` to the project.
4. Define architecture principles and initial decisions under `doc/architecture/`.
5. Create an executable roadmap from `doc/roadmaps/roadmap-template.md`.
6. Use `doc/prompts/next-pr.md` to select exactly one next bounded change.
7. Save the resulting PR-specific prompt under `doc/codex-prompts/<roadmap-or-task>/`.
8. Implement the PR with an AI coding agent.
9. Run the repository's local validation commands.
10. Use `doc/prompts/pr-review.md` for an independent full-diff review.
11. If blockers exist, use `doc/prompts/remediation.md` and re-review the resulting HEAD.
12. Merge only when the applicable acceptance criteria are satisfied, then update roadmap state.

## Minimum adoption checklist

Before the first AI-assisted implementation PR, make sure the project has:

- [ ] project purpose, scope, runtime, and quality gates in `PROJECT_CONTEXT.md`;
- [ ] root AI/contributor governance in `AGENTS.md`;
- [ ] system/module boundaries in `doc/architecture/context.md`;
- [ ] project-specific architecture invariants;
- [ ] at least one active roadmap with bounded PR items;
- [ ] exact local or CI validation commands;
- [ ] a defined policy for architecture blockers;
- [ ] a human merge authority.

Do not fill every template section merely because it exists. Delete irrelevant placeholders and keep the authoritative context compact enough to remain usable.

## Worked example

The fictional [`Document Status Notifier`](examples/document-status-notifier/) demonstrates the artifact chain without requiring a complete application:

```text
PROJECT_CONTEXT
    ↓
Roadmap PR-1.1
    ↓
PR-specific implementation prompt
    ↓
Illustrative independent review
```

Use it to understand the expected level of detail before adapting the template to a real project.

## Repository structure

```text
.
├── AGENTS.md
├── PROJECT_CONTEXT.md
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
├── .gitignore
├── .github/
│   ├── pull_request_template.md
│   └── ISSUE_TEMPLATE/
│       ├── architecture-decision.md
│       └── bounded-change.md
├── doc/
│   ├── workflow.md
│   ├── architecture/
│   │   ├── context.md
│   │   ├── principles.md
│   │   └── decisions/ADR-0000-template.md
│   ├── codex-prompts/
│   │   └── README.md
│   ├── prompts/
│   │   ├── next-pr.md
│   │   ├── implementation.md
│   │   ├── pr-review.md
│   │   └── remediation.md
│   ├── roadmaps/roadmap-template.md
│   └── standards/
│       ├── code-quality.md
│       ├── documentation.md
│       ├── prompt-design.md
│       └── testing.md
├── examples/
│   └── document-status-notifier/
└── templates/
    └── bounded-context-AGENTS.template.md
```

## What each artifact is for

| Artifact | Purpose |
| --- | --- |
| `PROJECT_CONTEXT.md` | Compact project identity, scope, stack, invariants, quality gates, and current roadmap pointer |
| `AGENTS.md` | Repository-wide rules that AI agents and contributors must obey |
| Local `AGENTS.md` | Additional rules for one bounded context/subtree |
| `doc/architecture/*` | System boundaries, principles, and durable decisions |
| `doc/roadmaps/*` | Dependency-aware sequencing into bounded PRs |
| `doc/prompts/*` | Reusable workflow prompts |
| `doc/codex-prompts/*` | Project-specific, versioned execution prompts |
| `doc/standards/prompt-design.md` | Quality gate for PR-specific implementation prompts |
| `.github/pull_request_template.md` | PR traceability and factual validation evidence |
| `.github/ISSUE_TEMPLATE/*` | Structured intake for bounded changes and architecture decisions |

## AGENTS.md hierarchy

The root `AGENTS.md` defines repository-wide rules. Add local `AGENTS.md` files only where a bounded context or subsystem genuinely needs additional constraints. Local rules refine the root rules for their subtree; they should not duplicate the root file.

## Architecture blockers

Stop implementation when a material decision cannot be derived from authoritative context, for example:

- ownership or bounded-context boundaries are unclear;
- two authoritative documents conflict;
- a public contract must change but compatibility policy is unspecified;
- persistence, security, consistency, or deployment semantics require a new architectural decision;
- the requested change would violate an explicit invariant.

Report the decision required, alternatives considered, affected scope, and why implementation cannot safely proceed.

## Review model

Review the **actual PR HEAD**, not the implementation summary. A review should cover scope, roadmap traceability, architecture boundaries, runtime correctness, tests, documentation, duplication/reuse, maintainability, and repository-specific quality gates.

Classify findings as:

- **BLOCKER** — must be fixed before merge.
- **WARNING** — important improvement or risk that does not independently prevent merge.

`APPROVE` is valid only when no mandatory blockers remain.

## CI policy

This template does not assume that hosted CI is available. Projects may rely on local validation. When CI is unavailable by design, its absence is not itself a merge blocker; the PR should record exact local commands and factual results. Projects that do have CI should add their required checks to `AGENTS.md` and `doc/standards/testing.md`.

## Security and confidentiality

Treat AI prompts, logs, test fixtures, and generated documentation as potential disclosure surfaces. Do not put real secrets, production data, personal data, private keys, or confidential internal architecture into the repository or prompts. See [`SECURITY.md`](SECURITY.md).

## What this template is not

This is not a universal prompt collection and it does not replace engineering judgment. The templates establish a repeatable control loop around AI-assisted work. Each project must define its own architecture, invariants, test strategy, security requirements, and acceptance criteria.

## License

Use under the terms of the repository license.