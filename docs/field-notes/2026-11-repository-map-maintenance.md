# Repository Map Maintenance Pilot

**Recorded:** 2026-11-16
**Evidence type:** Pilot observations from a Copilot SDK in VS Code session
**Status:** One Magitech workspace and organization; not a general workflow

## Setup exercised

The shared `agents-home` repository documents sibling projects in its root
`AGENTS.md`. The Magitech workspace contained multiple local repositories
whose ownership had recently moved to `magitech-ai`, plus a `voice_io`
project directory that was not yet a Git checkout or an organization
repository.

The agent compared the committed repo map, the local uncommitted map, local
Git remotes, and the active repositories listed by GitHub. It then helped
publish `voice_io` and update the map in separate pull requests:

- [`magitech-ai/voice_io#1`](https://github.com/magitech-ai/voice_io/pull/1)
  published the project source-only; the separately licensed non-commercial
  TTS weights were excluded.
- [`magitech-ai/agents-home#12`](https://github.com/magitech-ai/agents-home/pull/12)
  updated the map after the `voice_io` repository existed and corrected the
  transferred repositories' URLs.

Both pull requests were merged after their configured checks passed.

## Recorded observations

- The committed `agents-home` map did not list `Pymordial`,
  `PymordialBlue`, `PymordialDroid`, or `typesafe-sdk-godot`, although local
  checkouts existed and GitHub listed them as active `magitech-ai`
  repositories.
- The local map draft did list those projects but still used the former
  owner's URLs. Local checkouts' `origin` URLs and GitHub's organization
  listing provided evidence for the current URLs.
- A `voice_io` directory existed locally but had no Git metadata and was not
  present in the active organization repository listing. It became a map
  entry only after the user chose to publish it and its source repository
  existed.
- Editing the local map did not update `main`. The local change was initially
  uncommitted; it became live only after a feature branch, pull request,
  successful checks, and merge.

## What this pilot suggests

A repo map is a curated navigation aid, but its entries can drift from both
the current workspace and the organization's published repositories.
Workspace presence, Git remotes, and organization membership answer different
questions; none alone established which projects belonged in this map.
Publication and repository-map maintenance were also separate changes with
separate review and validation.

This pilot does not establish that the map should be generated
automatically, that every organization repository belongs in it, or that a
specific hosting arrangement is right for other teams.

## Candidate approaches

These are options to test, not recommendations or decisions:

1. **Curated map with a maintenance checklist.** Keep entries human-authored;
   check them when repositories are added, transferred, renamed, or retired.
   This preserves editorial scope and descriptions, but depends on someone
   remembering to update the map.
2. **Read-only drift report.** Periodically compare the curated entries with
   a chosen source such as the organization repository list and local Git
   remotes. Report missing entries, stale URLs, and local-only repositories
   without changing the map. This can surface drift while retaining human
   selection, but needs an explicit definition of which differences matter
   and access to the data sources.
3. **Generated inventory with curated annotations.** Generate repository
   names and canonical URLs from an explicitly selected source, while keeping
   descriptions, relevance, and local-checkout notes human-maintained. This
   could reduce URL drift, but may list irrelevant or inaccessible
   repositories and adds generation/update machinery.

Useful comparison criteria include missed changes, noisy or irrelevant
reports, review burden, source accessibility, and whether a human can
understand why an entry is included. The next pilot could apply a read-only
comparison to a small, explicitly selected repo set before choosing whether
any ongoing process is worthwhile.

## Follow-up question

See the open question on keeping a curated repo map accurate as repositories
are added, transferred, renamed, unpublished, or present only as local
checkouts.
