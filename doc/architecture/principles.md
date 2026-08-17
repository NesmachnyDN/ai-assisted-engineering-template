# Architecture Principles

Tailor these principles to the project. Delete principles that are not applicable and add project-specific invariants.

## P1 — Explicit ownership

Every durable piece of data and behavior has a clear owning module/bounded context. Other contexts interact through defined contracts rather than reaching into internal implementation details.

## P2 — Stable contracts, replaceable internals

Public APIs, events, schemas, and persisted formats are treated as compatibility-sensitive. Internal implementation may evolve without leaking unnecessary coupling.

## P3 — Decisions close to evidence

Architecture decisions must reference the constraints, requirements, or observed problems that justify them. Avoid speculative infrastructure and abstractions.

## P4 — Failure is designed, not hidden

Timeouts, retries, idempotency, partial failure, degraded modes, and observability are considered explicitly where distributed interaction exists. Fallbacks must not silently convert invalid state into apparent success.

## P5 — Security and privacy by boundary

Authentication, authorization, secrets, sensitive data, and trust boundaries are architecture concerns, not late implementation details.

## P6 — Evolution is explicit

Changes to contracts, schemas, data models, and deployment assumptions include an evolution/migration strategy where required.

## P7 — AI agents do not invent architecture

AI may propose alternatives, but material decisions not determined by authoritative project context require an explicit architecture decision before implementation proceeds.

## Project-specific invariants

- `<invariant>`
- `<invariant>`