# Document Status Notifier Roadmap

## Purpose

Introduce reliable, idempotent notification delivery in reviewable bounded changes.

## Invariants

- At most one successful provider delivery per logical document-status event.
- Delivery state is owned by the `delivery` module.
- Provider-specific payloads do not become domain contracts.

## Dependency model

| Item | Depends on | Enables |
| --- | --- | --- |
| PR-1.0 — basic delivery state | — | PR-1.1 |
| PR-1.1 — idempotent delivery | PR-1.0 | PR-1.2 |
| PR-1.2 — retry policy | PR-1.1 | operational hardening |

## Phase 1 — Reliable delivery

### PR-1.0 — Persist basic delivery state

**Status:** `done`

**Goal**

Persist one delivery record for each accepted document-status event.

**Acceptance criteria**

- accepted events receive a durable delivery record;
- provider dispatch can reference that record;
- unit/integration tests cover persistence behavior.

### PR-1.1 — Make delivery idempotent

**Status:** `planned`

**Goal**

Prevent duplicate provider sends when the same logical event is submitted more than once.

**In scope**

- define a stable idempotency key for incoming logical events;
- enforce uniqueness at the delivery persistence boundary;
- return/reuse existing delivery state for duplicate submissions;
- add regression coverage for duplicate submissions.

**Non-goals**

- retry/backoff policy;
- queue introduction;
- provider failover;
- notification preferences;
- schema changes unrelated to idempotency.

**Dependencies**

- PR-1.0 merged and delivery persistence exists.

**Architecture invariants**

- idempotency is owned by `delivery`, not by the provider adapter;
- database uniqueness is authoritative for concurrent duplicate submissions;
- provider-specific identifiers are not used as the domain idempotency key.

**Acceptance criteria**

- two sequential requests with the same logical event create one delivery record;
- concurrent duplicate submissions cannot create two delivery records;
- duplicate requests do not cause a second successful provider send;
- existing non-duplicate delivery behavior remains unchanged.

**Validation**

- `pytest tests/unit -q`
- `pytest tests/integration -q`
- `ruff check .`
- `mypy src`

**Documentation impact**

- update delivery module contract if the idempotency key becomes externally visible.

### PR-1.2 — Add bounded retry policy

**Status:** `blocked-by-PR-1.1`

**Goal**

Retry transient provider failures without violating idempotent-delivery semantics.

## State history

| Date | Item | From | To | Evidence |
| --- | --- | --- | --- | --- |
| 2026-08-17 | PR-1.0 | in-progress | done | example baseline |