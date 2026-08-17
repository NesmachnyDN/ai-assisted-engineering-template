# Project Context — Document Status Notifier

## Identity

- **Project:** Document Status Notifier
- **Purpose:** Receive document-status changes and deliver notifications reliably without duplicate external sends.
- **Primary users/stakeholders:** Internal document platform and operations team.
- **Repository:** `example/document-status-notifier`
- **Default/base branch:** `main`

## Scope

### In scope

- HTTP endpoint for status-change events.
- Durable delivery state.
- Notification dispatch through one external provider adapter.
- Retry-safe idempotent processing.

### Out of scope

- Multi-channel notification preferences.
- User-facing UI.
- Message templating administration.
- High-availability infrastructure design.

## Architecture

- **Architecture style:** Modular service.
- **Primary language/runtime:** Python 3.12.
- **Key frameworks:** FastAPI, SQLAlchemy.
- **Persistence:** PostgreSQL.
- **Messaging/integration:** Synchronous HTTP ingress; provider API egress.
- **Deployment/runtime:** Containerized service.
- **Security model:** Service-to-service authentication at ingress; provider secret stored outside the repository.

## Bounded contexts / modules

| Context / module | Responsibility | Owner / authoritative docs |
| --- | --- | --- |
| `ingress` | Validate incoming status-change requests | architecture context |
| `delivery` | Own delivery state and idempotency | ADR-0001 |
| `provider` | Translate/send outbound notification requests | provider contract |

## Authoritative sources

1. `AGENTS.md`
2. `doc/architecture/principles.md`
3. `examples/document-status-notifier/roadmap.md`
4. PR-specific prompt

## Critical invariants

- One logical document-status event must result in at most one successful provider delivery.
- Provider-specific details must not leak into the `delivery` domain model.
- A retry after an ambiguous transport failure must not create duplicate committed delivery state.

## Quality gates

- **Formatting/lint:** `ruff check .`
- **Unit tests:** `pytest tests/unit -q`
- **Integration tests:** `pytest tests/integration -q`
- **Static/type checks:** `mypy src`
- **Build/package:** `docker build .`

## CI model

Local validation is authoritative for this example. Exact commands/results are recorded in the PR.

## AI-assisted workflow

- Coding agent: AI coding agent
- Human architecture owner: Solution Architect
- Review model: independent AI review + human merge decision
- Merge authority: human maintainer

## Confidentiality and publication constraints

- No real provider credentials or customer/document data in repository artifacts.

## Current roadmap

- Active roadmap: `examples/document-status-notifier/roadmap.md`
- Current phase/item: `PR-1.1`
- Last completed bounded PR: `PR-1.0`