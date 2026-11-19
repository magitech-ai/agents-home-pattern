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

Every field note declares one label explicitly as a `**Label:**` header, using
the controlled vocabulary below. Notes recorded from 2026-11-20 onward must
also include a `**Reproduce:**` block naming the command and the artifact that
backs the observation. `python3 scripts/check_evidence.py` enforces both rules
and runs in CI.

- **Pilot observation** — behavior exercised in the Magitech workspace.
- **Documented behavior** — a harness or standard's own documentation states
  the behavior; this does not by itself prove it works in every version or
  surface.
- **Hypothesis** — a proposed generalization that still needs testing.
- **Open question** — an unresolved design or interoperability issue.

Descriptive [pilot conformance claims](CONFORMANCE.md) are collected in one
table and checked by the same script. They are statements about this workspace,
not requirements for other users.

See the [initial pilot notes](docs/field-notes/2026-11-initial-pilot.md),
[fresh OpenCode onboarding pilot](docs/field-notes/2026-11-fresh-opencode-onboarding.md),
[Antigravity onboarding evaluations](docs/field-notes/2026-11-antigravity-onboarding-evaluations.md),
[repository map maintenance pilot](docs/field-notes/2026-11-repository-map-maintenance.md),
[repo map drift check pilot](docs/field-notes/2026-11-repo-map-drift-check.md),
[cross-repo work-phase pilot](docs/field-notes/2026-11-cross-repo-work-phase.md),
[home-swe-home as the native home agent](docs/field-notes/2026-11-19-magecode-native-home-agent.md),
[measured self-improvement](docs/field-notes/2026-11-19-measured-self-improvement.md),
[onboarding UX for agents](docs/field-notes/2026-11-19-onboarding-ux-for-agents.md),
[component-creation gap](docs/field-notes/2026-11-19-component-creation-gap.md),
[single issue→PR loop pilot](docs/field-notes/2026-11-19-single-issue-to-pr-loop.md),
[code-changing loop pilot](docs/field-notes/2026-11-19-code-changing-loop-pilot.md),
[Stage A independent reviewer pilot](docs/field-notes/2026-11-19-stage-a-independent-reviewer.md),
[Stage B reviewer evaluation](docs/field-notes/2026-11-19-stage-b-reviewer-eval.md),
[Stage B2 real/injection evaluation](docs/field-notes/2026-11-19-stage-b2-real-and-injection-eval.md),
[reviewer model proof](docs/field-notes/2026-11-19-reviewer-model-proof.md),
[checkable conformance claims](docs/field-notes/2026-11-20-conformance-claims.md),
[harness evidence matrix](docs/harness-matrix.md),
[workflow](docs/WORKFLOW.md), [sources](docs/sources.md), and
[open questions](docs/open-questions.md).
Terms used in this repository are defined in the [glossary](GLOSSARY.md).

## What this repository is not

- Not a protocol or conformance target.
- Not a claim that one directory name or layout is universally discoverable.
- Not a substitute for each harness's documentation or established standards.
- Not the canonical store for the Magitech skills themselves; those live in
  [`magitech-ai/agents-home`](https://github.com/magitech-ai/agents-home).

## Contributing evidence

The [evidence workflow](docs/WORKFLOW.md) runs from an issue, through a proof
PR, to a CI gate and a proof comment on close. Issue templates, the controlled
label vocabulary and a PR template live in `.github/`. When adding an
observation, say whether it was personally tested or found in documentation,
identify the harness/version and environment where possible, and link the
source. Keep confirmed facts, interpretations, and questions distinct. Record
contrary evidence as readily as supporting evidence.
