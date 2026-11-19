# Pilot conformance claims

These are **descriptive** statements about one workspace, not requirements for
other users. A label records how a claim was evidenced; it does not recommend
that anyone adopt the behaviour. Nothing here is a protocol or certification.
The claim set is versioned with this repository and checked by
`scripts/check_evidence.py`.

| ID | Claim | Evidence | Proof |
| --- | --- | --- | --- |
| C1 | One home repository held the shared skill collection; each child repo kept its own guidance and issue tracker. | Pilot observation | [Initial pilot](docs/field-notes/2026-11-initial-pilot.md) |
| C2 | Home-repo pointers resolved to local checkouts or cloneable remotes; drift was reported read-only rather than silently repaired. | Pilot observation | [Repo map drift check](docs/field-notes/2026-11-repo-map-drift-check.md) |
| C3 | Harness-specific discovery was handled by adapters and installers, separate from portable content. | Pilot observation | [OpenCode onboarding](docs/field-notes/2026-11-fresh-opencode-onboarding.md), [Antigravity evaluations](docs/field-notes/2026-11-antigravity-onboarding-evaluations.md) |
| C4 | Agent-facing setup exposed plan-before-mutate and explicit replacement semantics. | Pilot observation | [Onboarding UX](docs/field-notes/2026-11-19-onboarding-ux-for-agents.md) |
| C5 | A self-improvement loop can be fully instrumented and still yield nothing adoptable; the loop refused adoption. | Pilot observation | [Measured self-improvement](docs/field-notes/2026-11-19-measured-self-improvement.md) |
| C6 | A native home agent was implemented and exercised in one workspace; the result is a pilot, not a portability proof. | Pilot observation | [Native home agent](docs/field-notes/2026-11-19-magecode-native-home-agent.md) |
| C7 | Evidence notes carry a recorded date, controlled label, status and limitations; local links resolve; every claim has a resolvable proof. | Pilot observation | `check: scripts/check_evidence.py` |
| C8 | Claims were made checkable without asserting universal discovery behaviour: each claim is a past-tense workspace statement with a label and a proof that resolves. | Pilot observation | [Conformance claims decision](docs/field-notes/2026-11-20-conformance-claims.md) |
| C9 | Cross-harness claims were scoped to OpenCode, Antigravity and Magecode; untested cells are explicit open questions. | Pilot observation | [Harness evidence matrix](docs/harness-matrix.md) |

## Adding a claim

Add a row with an ID (`C<n>`), a descriptive claim, one label from the README
vocabulary, and a proof target — either a relative Markdown link or a
`check: <path>` to a local script. Run `python3 scripts/check_evidence.py`
before opening a PR; CI runs the same check. Claims may only describe observed
or documented behaviour; a proposed generalisation stays a *Hypothesis* until
a field note records the pilot that tests it.
