# Passive cross-session reminders pilot

**Recorded:** 2026-11-19
**Label:** Pilot observation
**Evidence type:** Commands, test runs, and merged PRs across `agents-home`, `home-swe-home`, and `agents-home-pattern` on this workspace.
**Status:** Two-scope passive reminders implemented (`agents-home/reminders.toml` + gitignored `agents-home/reminders.local.toml`) and exercised locally; one real local reminder seeded (`retire-skills-2026-11-19`).

**Limitations:** Exercised in one workspace on the day of implementation (`2026-11-19`). Multi-day rollover, overdue aging across weeks, and interactive `home-swe-home` REPL sessions with live model turns have not yet been observed over time.

## What was run

1. **Core schema & CLI (`agents-home` PR #45, PR #46):**
   - Implemented `scripts/reminders.py` (stdlib `tomllib`, strict allowlist, atomic writes, `git rev-parse --git-common-dir` resolution for worktree safety, `done_when` `path_absent`/`path_exists` auto-resolution) and `tests/test_reminders.py` (20/20 unit tests passing).
   - Wired `scripts/session_status.py` footer and `scripts/check_all.py` / CI `reminders.py check`.
2. **Native home agent integration (`home-swe-home` PR #59):**
   - Added `RemindersService` (`ctx.reminders`), tail injection into `InstructionsService.build` for interactive REPL mode only (omitted in headless `-p` mode), startup summary line, and read-only `/reminders` command.
   - Passed `Agent review` and `Test & Lint / ci` (Linux, macOS, Windows; 430/430 tests, 100% branch coverage).
3. **Live local seeding:**
   - Seeded `retire-skills-2026-11-19` (`due = 2026-11-26`, `done_when = { path_absent = "~/.agents/skills-retired/2026-11-19" }`) in `agents-home/reminders.local.toml`.
   - Verified `uv run --no-project python scripts/reminders.py check` exited 0 and `uv run --no-project python scripts/session_status.py --all-reminders` displayed the `upcoming` reminder.

## Recorded observations

- Keeping `reminders.local.toml` gitignored inside `agents-home` (rather than `~/.agents/reminders.toml` or `reminders.toml` alone) avoids PR friction for machine-local nudges while keeping `~/.agents/` strictly as the symlink/adapter layer.
- Resolving `reminders.local.toml` via `git rev-parse --path-format=absolute --git-common-dir` is necessary because isolated git worktrees (`/tmp/opencode/...`) do not copy gitignored files from the primary checkout.
- Separating passive session-start reminders (`D-018`) from scheduled unattended automations keeps idle token cost at `$0` and avoids mixing inert data with executable prompts.

## Reproduce

```sh
cd /mnt/storage/projects/magitech/agents-home
uv run --no-project python -m unittest discover -s tests -v
uv run --no-project python scripts/reminders.py check
uv run --no-project python scripts/session_status.py --all-reminders
```

## Relation to the pattern

Records initial implementation and verification evidence for the passive reminders tier described in [open-questions.md](../open-questions.md). Adds no new conformance claim.
