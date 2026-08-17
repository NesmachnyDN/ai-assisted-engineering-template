# Architecture Context

Describe the system context that an engineer or AI agent must understand before making implementation decisions.

## System purpose

`<What problem does the system solve?>`

## Context diagram

`<Link to diagram or describe external actors/systems and trust boundaries.>`

## Major components

| Component | Responsibility | Owns | Must not own |
| --- | --- | --- | --- |
| `<component>` | `<responsibility>` | `<data/behavior>` | `<explicit boundary>` |

## External dependencies

| Dependency | Purpose | Contract | Failure/availability assumptions |
| --- | --- | --- | --- |
| `<dependency>` | `<purpose>` | `<API/event/etc.>` | `<assumptions>` |

## Data and consistency

`<Ownership, transaction boundaries, consistency model, migrations, retention.>`

## Security and privacy

`<Authentication, authorization, secrets, sensitive data, trust boundaries.>`

## Deployment and operations

`<Runtime topology, environments, observability, operational constraints.>`

## Known constraints

- `<constraint>`

## Open architecture questions

- `<question; convert durable decisions to ADRs>`