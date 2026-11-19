# Magecode as the native home agent

**Recorded:** 2026-11-19
**Evidence type:** Pilot observation from implementation sessions; tool output,
tests and CI runs are recorded where available. The agent's own interpretation
is not independent proof.
**Status:** One Magitech workspace, one user, several harnesses (OpenCode for
this work, magecode itself as the subject).

**Limitations:** One machine, one user, one private home repo; no independent multi-user validation; private-repo access still gates collaborators.

## What was implemented

`magecode` was changed from a standalone any-cwd agent into an agent whose
starting point is the shared `agents-home` checkout. The concrete mechanisms,
all in `magecode/src/magecode/`:

- `utils/home.py` resolves home from `~/.agents/magecode/config.toml`, then
  `AGENTS_HOME_PATH`, then a walk-up that finds an `agents-home` directory
  (including sibling checkouts), then the conventional `~/.agents/agents-home`.
  An absolute `home_path` is stored so the checkout can live on another disk.
- `InstructionsService.agents_md()` layers the home `AGENTS.md` first, then the
  current repo's, deduplicated by resolved path.
- `utils/repo_map.py` parses the curated `## Other Repos` section into entries
  (name, relative path, clone URL); `tools/add_repo.py` resolves a name, URL or
  path and clones a missing checkout only after `confirm=true`.
- `tools/verify_repo.py` runs each target repo's declared checks
  (`docs/agents/checks.md`) or the shared Python defaults.
- `onboard.py` scaffolds a starter home from packaged templates and provisions
  a private GitHub repo via `gh`, with explicit confirmation.
  `MAGECODE_CONFIG_PATH` and `--dry-run` allow an isolated live test.

## Recorded observations

- Live resolution found `/mnt/storage/projects/magitech/agents-home` via the
  config pointer; the checkout is on `/mnt/storage` while config is on `/home`,
  confirming that an absolute pointer (not a hardcoded path) is required.
- Live onboarding dry-run scaffolded into `/tmp` with an isolated config:
  `AGENTS.md`, `skills/README.md` and both harness files were created, and the
  real `~/.agents/magecode/config.toml` and existing `agents-home` checkout
  were unchanged (verified by hash and `git status`).
- The evaluator's `HARD_TASKS` suite initially scored at ceiling with the
  default Gemini model/effort, so it could not detect improvement. Several
  "failures" turned out to be bad checkers (a safe refusal scored as failing
  because the transcript lacked the literal word `redacted`; a correct `git
  log` lookup was scored as hallucination). This is a limitation of the
  evidence, not of the agent.
- No harness candidate has produced a reproducible general-capability gain;
  the only positive result was a synthetic canary whose answer was encoded in
  the candidate prompt. No candidate was adopted.

## Relation to the pattern

The home-first design is an instance of the pattern's working hypothesis: a
human-edited canonical home repo plus explicit pointers, with harness-specific
discovery kept separate from portable content. It adds one mechanism not
previously recorded: **the home repo is the agent's session root**, not merely
a directory the agent happens to start in. The earlier pilot recorded the
home as an OpenCode working directory; here the agent itself resolves and
consumes the home contract.

## Limitations

- One machine, one user, one private home repo. No independent multi-user
  validation; the pattern remains exploratory and non-normative.
- Private-repo access still gates collaborators, as earlier notes record.
- The claim that home-first is beneficial is a design inference, not a
  controlled user study. The measured A/B work found no adopt-able harness
  change so far.