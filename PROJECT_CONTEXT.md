# Project Context

> Replace all `<...>` placeholders before using this repository for a real project.

## Identity

- **Project:** `<name>`
- **Purpose:** `<one-paragraph business/engineering purpose>`
- **Primary users/stakeholders:** `<who>`
- **Repository:** `<owner/repository>`
- **Default/base branch:** `<main|develop|other>`

## Scope

### In scope

- `<capability>`

### Out of scope

- `<explicit non-goal>`

## Architecture

- **Architecture style:** `<modular monolith|microservices|library|CLI|other>`
- **Primary language/runtime:** `<...>`
- **Key frameworks:** `<...>`
- **Persistence:** `<...>`
- **Messaging/integration:** `<...>`
- **Deployment/runtime:** `<...>`
- **Security model:** `<...>`

## Bounded contexts / modules

| Context / module | Responsibility | Owner / authoritative docs |
| --- | --- | --- |
| `<name>` | `<responsibility>` | `<path/team>` |

## Authoritative sources

List sources in precedence order.

1. `<architecture specification / ADR set>`
2. `<active roadmap>`
3. `<domain contract>`
4. `<other>`

## Critical invariants

- `<invariant that must never be violated>`
- `<compatibility or data invariant>`

## Quality gates

- **Formatting/lint:** `<commands>`
- **Unit tests:** `<commands>`
- **Integration tests:** `<commands>`
- **Static/type checks:** `<commands>`
- **Build/package:** `<commands>`
- **Other:** `<commands>`

## CI model

`<Hosted CI required | local validation is authoritative | hybrid>`

Describe which checks are mandatory and how evidence is recorded.

## Documentation model

- Architecture: `doc/architecture/`
- Roadmaps: `doc/roadmaps/`
- PR-specific prompts: `doc/codex-prompts/`
- Standards: `doc/standards/`

Adjust paths if the project uses another structure.

## AI-assisted workflow

- Coding agent(s): `<Codex / other>`
- Human architecture owner: `<role>`
- Review model: `<independent AI review + human decision / other>`
- Merge authority: `<human role>`

## Confidentiality and publication constraints

- `<what must not enter prompts, commits, logs, screenshots, or public artifacts>`

## Current roadmap

- Active roadmap: `<doc/roadmaps/...>`
- Current phase/item: `<...>`
- Last completed bounded PR: `<...>`