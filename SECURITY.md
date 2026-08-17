# Security Policy

This repository is a documentation/template project. Security issues primarily concern unsafe template guidance, accidental secret exposure, or examples that encourage insecure engineering practices.

## Reporting

If you discover a security-sensitive problem, avoid publishing credentials, exploit details against a real system, personal data, or confidential architecture in a public issue. Contact the repository owner through an appropriate private channel when disclosure itself would create risk.

## Template safety expectations

Projects created from this template should explicitly define:

- authentication and authorization boundaries;
- secret storage and rotation expectations;
- sensitive/regulated data handling;
- trust boundaries and external dependencies;
- logging/redaction constraints;
- security validation appropriate to the technology stack.

AI agents must not place real secrets, production data, private keys, access tokens, or confidential organization-specific material in prompts, commits, fixtures, logs, or documentation.

## AI-specific risk

Treat agent output as untrusted engineering work until validated. In particular:

- do not accept security-sensitive architecture decisions inferred from missing context;
- verify dependency and configuration changes;
- inspect generated authorization, cryptography, deserialization, query construction, and secret-handling code carefully;
- never use passing tests as the sole evidence that a security property holds.