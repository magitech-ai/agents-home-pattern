# Harness evidence matrix

Scope: the three harnesses already piloted in this workspace — OpenCode,
Antigravity and Magecode. A cell holds the strongest recorded claim, not a
capability estimate. "Open question" means no field note recorded the
behaviour; it is not a claim that the harness cannot do it.

| Capability | OpenCode | Antigravity | home-swe-home |
| --- | --- | --- | --- |
| Discovery of home guidance | Pilot observation — fresh session read root `AGENTS.md`, README and skill catalog ([note](field-notes/2026-11-fresh-opencode-onboarding.md), 2026-11-15) | Pilot observation — two read-only sessions read the home repository ([note](field-notes/2026-11-antigravity-onboarding-evaluations.md), 2026-11-15) | Pilot observation — home resolved from config, then walk-up, then conventional path ([note](field-notes/2026-11-19-magecode-native-home-agent.md), 2026-11-19) |
| Pointer resolution / clone-on-demand | Pilot observation — read-only repo-map drift check reported differences without editing ([note](field-notes/2026-11-repo-map-drift-check.md), 2026-11-17) | Open question — [not recorded](open-questions.md) | Pilot observation — `Other Repos` parsed; missing clone only after `confirm=true` ([note](field-notes/2026-11-19-magecode-native-home-agent.md), 2026-11-19) |
| Skill loading, including hidden skills | Pilot observation — explicit invocation reached a skill excluded from model selection ([note](field-notes/2026-11-fresh-opencode-onboarding.md), 2026-11-15) | Pilot observation — `SKILL.md` readable; no agent-side invoke-by-name tool reported, so explicit invocation unverified ([note](field-notes/2026-11-antigravity-onboarding-evaluations.md), 2026-11-15) | Open question — [not recorded](open-questions.md) |
| Cross-repo work from one session | Pilot observation — work-phase pilot swept changes across repos from one session ([note](field-notes/2026-11-cross-repo-work-phase.md), 2026-11-17) | Open question — [not recorded](open-questions.md) | Pilot observation — `verify_repo` runs each target repo's declared checks from the home session ([note](field-notes/2026-11-19-magecode-native-home-agent.md), 2026-11-19) |

## Reading the matrix

- Every filled cell links to a field note that names the harness, environment
  and limitations. No cell generalises beyond the note's recorded scope.
- An open question is a gap in evidence, not a negative result. Promote it to
  an issue via the [evidence workflow](WORKFLOW.md) when it is worth a
  pilot.
- Do not add a fourth harness row without a field note. The repository's claim
  set stays scoped to the three harnesses actually exercised.

## Unresolved questions: none.
