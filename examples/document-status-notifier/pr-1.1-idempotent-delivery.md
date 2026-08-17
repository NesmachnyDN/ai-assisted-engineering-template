# PR-1.1 — Idempotent Delivery

## Objective

Make document-status delivery idempotent so repeated submission of the same logical event cannot create duplicate delivery records or duplicate successful provider sends.

## Why this PR is next

PR-1.0 established durable delivery state. Retry semantics in PR-1.2 depend on deterministic duplicate detection, so idempotency must be established first.

## Dependencies

- PR-1.0 is complete.
- Delivery persistence exists and is owned by the `delivery` module.

## Scope

- Add a stable domain idempotency key derived from the logical incoming event identity.
- Persist the idempotency key with the delivery record.
- Enforce uniqueness at the persistence boundary so concurrent duplicate submissions cannot create duplicate records.
- On duplicate submission, resolve and return/reuse the existing delivery rather than creating another one.
- Ensure duplicate submissions cannot result in a second successful provider send.
- Add focused unit and integration tests.

## Non-goals

- Retry/backoff policy.
- New messaging infrastructure.
- Provider failover.
- Notification preferences.
- General persistence refactoring.
- Provider-contract redesign.

## Architecture boundaries and invariants

- Idempotency belongs to `delivery`; do not implement it only in the HTTP or provider adapter.
- Database uniqueness is the final authority under concurrency; an application-level pre-check alone is insufficient.
- Provider-specific identifiers must not become the domain idempotency key.
- Provider-specific payload types must not leak into the delivery domain model.
- Preserve current behavior for distinct events.

## Implementation guidance

Inspect the existing delivery aggregate/model, repository, service, ingress handler, provider dispatch flow, migrations, and tests before modifying code. Reuse existing transaction/repository patterns.

Do not introduce a new database, queue, distributed lock, or framework. If the existing data model does not contain enough authoritative information to define a stable logical event identity, stop and raise an architecture blocker identifying the missing identity decision rather than inventing a key.

## Acceptance criteria

1. Two sequential submissions of the same logical event produce one persisted delivery.
2. Concurrent duplicate submissions cannot persist two deliveries with the same idempotency key.
3. Duplicate submissions do not produce a second successful provider delivery.
4. Two distinct events continue to produce distinct delivery records and provider sends.
5. Relevant database migration/schema change is included if required.
6. Unit and integration tests demonstrate sequential and concurrent duplicate behavior.

## Validation

Run and report exact results for:

```text
pytest tests/unit -q
pytest tests/integration -q
ruff check .
mypy src
```

If a relevant failure appears to be pre-existing, reproduce it against the base branch before classifying it as baseline.

## Documentation

Update architecture/module documentation only if the idempotency key becomes part of an externally observable contract. Otherwise keep the change implementation-local.

## Stop conditions

Stop and report an architecture blocker if:

- logical event identity cannot be derived from authoritative requirements/context;
- uniqueness requires a cross-module ownership change;
- implementation would require a new infrastructure component;
- current provider semantics make at-most-once successful delivery impossible without a new external contract decision.