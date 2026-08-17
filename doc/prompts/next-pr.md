# Prompt: Select the Next Bounded PR

Use this prompt with a reasoning-capable assistant before asking a coding agent to implement the next roadmap item.

```text
Repository: <owner/repo>
Base branch: <branch>
Active roadmap: <path>

Use only current authoritative repository context.

From the current base branch, determine exactly one next admissible bounded PR from the active roadmap. Do not implement functionality.

Before selecting the PR:
1. Read the root AGENTS.md and applicable governance/quality documents.
2. Read project context, architecture principles, applicable ADRs, the active roadmap, and roadmap state/history.
3. Inspect the current repository state sufficiently to verify that dependencies and predecessor work are actually complete.
4. Resolve required architecture decisions only when authoritative context determines them.
5. If a material decision cannot be determined from current authoritative context, stop and report an architecture blocker instead of creating an implementation prompt.

For the selected PR, produce a PR-specific implementation prompt containing:
- objective and rationale;
- dependencies and evidence they are satisfied;
- exact scope;
- explicit non-goals;
- affected ownership/architecture boundaries;
- invariants that must be preserved;
- expected implementation behavior without over-prescribing incidental code structure;
- acceptance criteria;
- exact or project-appropriate validation requirements;
- documentation/roadmap obligations;
- prohibited scope expansion.

Save only the current PR-specific prompt under:
doc/codex-prompts/<roadmap-or-task>/pr-<id>-<short-name>.md

Remove a stale prompt for an already merged predecessor from that active prompt directory when repository policy requires one active prompt.

Return:
1. selected PR and why it is next;
2. scope and dependencies;
3. path of the created prompt;
4. any resolved architecture decisions;
5. architecture blocker instead of a prompt if implementation is not ready.
```