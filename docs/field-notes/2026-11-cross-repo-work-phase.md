# Cross-Repo Work-Phase Pilot

**Recorded:** 2026-11-17
**Evidence type:** Pilot observation from an OpenCode session working across
`agents-home`, `magecode`, `anima`, and `agents-home-pattern`
**Status:** One Magitech workspace and one harness; the agent's own summary is
not independent proof

**Limitations:** One Magitech workspace and one harness; agent self-reporting is not independent proof.

## Setup exercised

A long implementation session ran with `agents-home` as the OpenCode working
directory while changes were made in sibling repositories. The home repo's
root `AGENTS.md` was present as project guidance, and its shared skills were
available through the personal `~/.agents/skills` links installed earlier.

Work spanned:

- `magecode` — a coding agent built on anima (created during this session,
  local-only and intentionally unmapped pending publication)
- `anima` — read as the upstream component model and kernel source
- `agents-home-pattern` — read for its evidence labels and open questions
- `agents-home` — the home repo guidance itself

## Recorded observations

- The "Working Across Repos" guidance was followed: before changing a
  repository, its own `AGENTS.md` was read; cross-repo interfaces were traced
  (anima's `Context`/`Service`/`Fiber`/`HmrService`) before changing code that
  depended on them; each repo was verified with its own commands.
- A shared skill from the home repo (`domain-modeling`) was used to record
  architecture decisions as ADRs in `magecode`. This is a work-phase use, not
  just the onboarding/discovery use recorded in earlier field notes.
- The map's `.github` pointer directed the agent to the organization's
  reusable CI workflow. `magecode` adopted `python-ci.yml@main` from there,
  demonstrating a map pointer leading to shared tooling, not just navigation.
- The map did not list `magecode`. The user's stated reason was that the repo
  had not yet been published to GitHub and was being made stable first. The
  agent did not add it.

## Publication/map workflow decision

The user was asked whether new projects started from the home repo should be
published and mapped immediately, gated on stability, or handled another way.
The chosen rule was a **publishable-minimum gate**:

1. Once a new project has a final name, green checks, a README, CI, and no
   secrets in the tree, publish it (private is acceptable).
2. Surface a map pointer for approval at the same time.
3. Do not wait for "stability": CI runs, PR discipline, and off-machine
   history only become real after a remote exists.

This is a decision for one workspace, not a general claim about all users. It
is recorded because earlier field notes identified repo-map drift as an open
question and this supplies one concrete resolution candidate.

## What this pilot suggests

- The home repo pattern supports a sustained implementation phase across
  several repos, not only initial discovery. Prior notes covered onboarding;
  this one records work-phase use of pointers and skills.
- Map membership and publication are linked in practice but are separate
  decisions. Here the user deliberately kept a substantial local repo out of
  the map until publication.
- A "stable" gate is hard to apply to an actively iterated project; a
  publishable-minimum gate is more actionable and was preferred.

## Limitations

- One session, one harness (OpenCode), one user, one OS. The same workflow may
  not hold in CI sandboxes, teams, or other harnesses.
- The observations come from the agent's own reporting during the session;
  the session export was not separately audited for this note.
- The publication rule was chosen by one user for this workspace. It is not
  evidence that other teams should adopt it.