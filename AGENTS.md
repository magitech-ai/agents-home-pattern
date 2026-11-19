# Agent Home Pattern Incubation

This repository records evidence and explores the Agent Home Pattern. It is
not a standard or conformance target.

## Evidence discipline

- Label statements as pilot observations, documented behavior, hypotheses, or
  open questions.
- For observations, identify the harness, version, operating environment, and
  steps when known. Do not generalize one setup's behavior to all users.
- Prefer primary product and standards documentation; link the source and note
  when it was checked.
- Record conflicting evidence and limitations alongside supporting evidence.
- Keep the working hypothesis explicitly revisable. Do not introduce
  normative requirements or claim conformance without a separate, deliberate
  decision.
- Update `GLOSSARY.md` when this project settles on domain terminology.

## Claims

Descriptive [pilot conformance claims](CONFORMANCE.md) live in one table. They
are observations about this workspace, never requirements. Validate notes,
links and claims with `python3 scripts/check_evidence.py` before a PR. Work
flows through GitHub issues to proof PRs per [docs/WORKFLOW.md](docs/WORKFLOW.md).

## Scope

The Magitech skill collection itself is maintained in the separate
[`agents-home`](https://github.com/magitech-ai/agents-home) repository. This
repository tracks what can be learned from that and other pilots.
