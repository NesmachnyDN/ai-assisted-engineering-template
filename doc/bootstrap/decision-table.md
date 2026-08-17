# Bootstrap Decision Table

Use this table when the adoption flow reaches an ambiguity.

| Situation | Action | Continue to implementation? |
| --- | --- | --- |
| Placeholder or missing required section in `PROJECT_CONTEXT.md` | Fill the missing project fact | No |
| `TBD — BLOCKER` affects first roadmap item | Resolve the decision; add ADR when durable/material | No |
| Active roadmap path does not exist | Create/fix the roadmap reference | No |
| Hosted CI is unavailable but local validation is authoritative | Record exact local commands/results | Yes |
| A relevant test already fails on the base branch | Record baseline evidence and verify PR does not worsen it | Yes, if outside scope and policy permits |
| Architecture boundary/ownership is unclear | Resolve ownership/contract explicitly | No |
| Implementation detail has several equivalent local choices | Let implementation agent choose within standards | Yes |
| First roadmap item depends on unmerged predecessor | Finish predecessor first | No |
| Candidate PR contains multiple unrelated objectives | Split roadmap item into bounded PRs | No |
| Review finds a blocker inside PR scope | Remediate on the same PR and re-review | No, until blocker is cleared |
| Review finds a warning only | Record/accept according to project policy | Usually yes |
| Required change exposes secret/confidential production data | Redesign fixtures/examples/process | No |

The governing distinction is simple: an AI agent may choose implementation details inside established constraints, but it may not silently choose project truth, architecture boundaries, compatibility semantics, or acceptance policy.