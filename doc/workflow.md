# End-to-End AI-Assisted Engineering Workflow

This guide describes the intended control loop for projects created from this template.

## 1. Establish authoritative context

Before asking an AI agent to implement anything, define the minimum project truth:

- project purpose and constraints in `PROJECT_CONTEXT.md`;
- repository-wide rules in `AGENTS.md`;
- system boundaries in `doc/architecture/context.md`;
- durable principles in `doc/architecture/principles.md`;
- material decisions as ADRs;
- executable sequencing in an active roadmap.

The objective is not to document everything. The objective is to make important constraints explicit enough that an agent cannot plausibly invent them without being detected.

## 2. Select one bounded PR

Use `doc/prompts/next-pr.md` to determine exactly one admissible roadmap item.

A good bounded PR has:

- one observable objective;
- satisfied dependencies;
- explicit scope and non-goals;
- known ownership boundaries;
- no unresolved material architecture decision;
- acceptance criteria that can be validated.

If any of these are missing, resolve them before implementation.

## 3. Freeze the execution contract

Save a PR-specific prompt under `doc/codex-prompts/<roadmap-or-task>/`.

The prompt acts as the execution contract for the coding agent. It should be specific about outcomes and invariants, but avoid prescribing incidental implementation structure unless the architecture requires it.

The prompt should answer:

- What must change?
- What must not change?
- Why is this item next?
- Which boundaries and invariants matter?
- How will success be verified?
- When must the agent stop and ask for an architecture decision?

## 4. Implement on a dedicated branch

Create or reuse the branch associated with the bounded PR. The coding agent must first reconstruct context from the repository rather than relying only on chat history.

During implementation:

- keep the diff inside scope;
- reuse existing abstractions where appropriate;
- do not hide architecture changes inside refactoring;
- add tests for changed behavior;
- stop when a material decision is not authoritative.

## 5. Validate locally

Run validation in increasing scope:

1. targeted test(s) for the changed behavior;
2. subsystem/module regression slice;
3. repository-wide checks required by project policy.

Record exact commands and factual results. If a relevant failure appears pre-existing, reproduce it on the base branch before classifying it as baseline.

## 6. Open or update the PR

The PR body should make the change reviewable without becoming a second architecture document. Include:

- objective and traceability;
- scope/non-goals;
- architecture impact;
- exact validation evidence;
- known baseline defects or risks.

Use `.github/pull_request_template.md` as the default structure.

## 7. Perform an independent review

Use `doc/prompts/pr-review.md` with a fresh reasoning pass. The reviewer should inspect the actual PR HEAD and repository context, not merely the implementation summary.

A full review checks:

- bounded scope and roadmap traceability;
- architecture and ownership boundaries;
- runtime correctness and failure semantics;
- symmetric cases/invariants;
- tests and evidence;
- maintainability and duplication;
- documentation and ADR impact;
- security/privacy/compatibility concerns.

Review output ends with either `APPROVE` or `REQUEST CHANGES`.

## 8. Remediate blockers in place

If blockers exist, use `doc/prompts/remediation.md` against the existing PR branch.

The remediation agent should fix root causes, not just reported lines. It must not create a new PR, jump to the next roadmap item, or expand the scope into opportunistic cleanup.

After remediation, repeat the independent review against the new HEAD.

## 9. Merge by human decision

AI agents may prepare, implement, test, and review. Merge authority remains a project governance decision. This template assumes a human controls merge unless the project explicitly documents another policy.

## 10. Advance roadmap state

After merge:

- update the roadmap item state;
- record evidence (PR/commit/release);
- create/supersede ADRs when implementation resolved a durable decision;
- remove or archive stale active prompts according to project policy;
- select the next bounded PR only from the new authoritative repository state.

## Stop conditions

Stop the implementation loop and raise an architecture/governance blocker when:

- two authoritative sources conflict;
- ownership of data/behavior is unclear;
- a compatibility-breaking contract change is required but policy is absent;
- a new infrastructure/security/persistence decision is required;
- acceptance criteria cannot be made observable;
- the requested change is materially larger than one bounded PR;
- validation evidence cannot distinguish a regression from a relevant baseline defect.

The workflow is intentionally conservative around architecture and deliberately fast around routine implementation.