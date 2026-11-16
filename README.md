# Agent Home Pattern

**Status: incubation. This repository is exploratory and non-normative.**

This project records and tests an emerging way to organize shared agent
guidance and skills across repositories and harnesses. It is inspired by Matt
Pocock's [Home Repo Pattern](https://www.aihero.dev/the-home-repo-pattern), but
is not an official standard, certification program, or replacement for
established formats such as Agent Skills, `AGENTS.md`, or MCP.

## Current working hypothesis

Keep shared guidance and skills in one version-controlled repository, use it
as the human-edited canonical source, and connect it to other repositories and
harnesses through explicit pointers or discovery adapters. Keep
harness-specific discovery behavior separate from the portable format of the
content itself.

This is a hypothesis drawn from one active setup, not a requirement for other
users. We expect to revise it as we test other harnesses, environments, and
collaboration models.

## Evidence labels

- **Pilot observation** — behavior exercised in the Magitech workspace.
- **Documented behavior** — a harness or standard's own documentation states
  the behavior; this does not by itself prove it works in every version or
  surface.
- **Hypothesis** — a proposed generalization that still needs testing.
- **Open question** — an unresolved design or interoperability issue.

See the [initial pilot notes](docs/field-notes/2026-11-initial-pilot.md),
[fresh OpenCode onboarding pilot](docs/field-notes/2026-11-fresh-opencode-onboarding.md),
[sources](docs/sources.md), and [open questions](docs/open-questions.md).
Terms used in this repository are defined in the [glossary](GLOSSARY.md).

## What this repository is not

- Not a protocol or conformance target.
- Not a claim that one directory name or layout is universally discoverable.
- Not a substitute for each harness's documentation or established standards.
- Not the canonical store for the Magitech skills themselves; those live in
  [`magitech-ai/agents-home`](https://github.com/magitech-ai/agents-home).

## Contributing evidence

When adding an observation, say whether it was personally tested or found in
documentation, identify the harness/version and environment where possible,
and link the source. Keep confirmed facts, interpretations, and questions
distinct. Record contrary evidence as readily as supporting evidence.
