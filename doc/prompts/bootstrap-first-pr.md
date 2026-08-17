# Prompt: Bootstrap the First Bounded PR

Use this once after cloning/adopting the template and completing `BOOTSTRAP.md` through Gate 4.

```text
Repository: <owner/repo>
Base branch: <branch>

This repository was created from the AI-assisted engineering template. Bootstrap it into the normal bounded-PR workflow. Do not implement product functionality in this step.

Use only current authoritative repository context. Do not ask me to restate information already recorded in the repository and do not invent missing architecture decisions.

First, read:
- BOOTSTRAP.md;
- root AGENTS.md;
- PROJECT_CONTEXT.md;
- doc/bootstrap/project-context-checklist.md;
- doc/bootstrap/adoption-checklist.md;
- architecture principles and applicable ADRs;
- the active roadmap referenced by PROJECT_CONTEXT.md;
- applicable engineering and prompt-design standards.

Then inspect repository state sufficiently to validate the context rather than trusting roadmap text alone.

Perform these gates in order:

1. Context readiness
Verify that PROJECT_CONTEXT.md contains enough project-specific information to determine scope, architecture boundaries, authoritative sources, invariants, validation, CI policy, confidentiality constraints, and the active roadmap.

2. Adoption readiness
Verify the adoption checklist. Identify unresolved template placeholders, contradictory authoritative sources, missing validation contracts, missing ownership boundaries, and material architecture decisions.

3. First bounded PR selection
If Gates 1 and 2 pass, determine exactly one next admissible bounded PR from the active roadmap. Verify that its dependencies are actually satisfied in the repository.

4. Architecture decision gate
Resolve a decision only when authoritative repository context determines the answer. If a material decision affecting scope, architecture, security, compatibility, data semantics, or acceptance cannot be determined, STOP and report BOOTSTRAP BLOCKER. Do not create an implementation prompt.

5. Prompt creation
If no blocker remains, create exactly one PR-specific implementation prompt at:

doc/codex-prompts/<roadmap-or-task>/pr-<id>-<short-name>.md

The prompt must contain:
- objective and rationale;
- dependency evidence;
- exact scope;
- explicit non-goals;
- affected ownership/architecture boundaries;
- invariants to preserve;
- expected behavior;
- acceptance criteria;
- exact/project-appropriate local validation requirements;
- handling of pre-existing baseline failures;
- documentation and roadmap obligations;
- prohibited scope expansion;
- required PR/commit validation evidence.

Do not prescribe incidental implementation structure unless architecture or repository rules require it.
Do not implement the PR.
Do not generate multiple candidate PRs.
Do not treat unavailable or non-required hosted CI as a blocker when PROJECT_CONTEXT.md defines local validation as authoritative.

Return only:
1. bootstrap readiness: READY or BLOCKED;
2. blockers, if any;
3. selected first bounded PR and why it is next, if READY;
4. scope and dependency evidence;
5. created prompt path;
6. architecture decisions resolved from authoritative context.
```