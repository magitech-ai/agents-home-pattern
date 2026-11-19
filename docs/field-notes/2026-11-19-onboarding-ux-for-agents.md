# Onboarding UX for humans and agents

**Recorded:** 2026-11-19
**Evidence type:** Implementation and live CLI runs in `magecode`
**Status:** One workspace; the agent-friendliness is interface-level, not a
user study.

**Limitations:** One machine and one CLI implementation; no other harness tested; --force is blunt migration.

## Observation

An onboarding wizard initially used a single interactive `input()` prompt. That
works for a human at a terminal but is awkward for an autonomous agent, which
must shell out with piped input and cannot see what will be created before
confirming. Three additions resolved this:

- `--plan --json` prints the exact files and provisioning commands without
  writing anything, so an agent can inspect the side effects first.
- `--yes` confirms non-interactively.
- A guard refuses to replace an existing home checkout unless `--force` is
  passed, because agents operating from a repo can otherwise overwrite the
  canonical pointer during an experiment.

`MAGECODE_CONFIG_PATH` isolates the config location, which made a live test
possible without touching the real `~/.agents/magecode/config.toml`.

## Recorded evidence

- Live agent plan: JSON with 4 files and 8 commands, no writes.
- Live agent scaffold: `--yes --dry-run --json --force` into `/tmp` returned
  `{"accepted": true, ...}`; the real config hash and the existing
  `agents-home` `git status` were unchanged.
- The guard blocked the same command without `--force`, proving that an agent
  cannot silently replace the home.

## Implication

A home-repo pattern used by both humans and agents needs **inspection before
mutation** and **explicit replacement semantics**. Interactive-only wizards are
a hidden coupling to one kind of operator. This is a small but concrete
extension of the pattern's "explicit pointers" idea to agent-facing tooling.

## Limitations

- One machine and one CLI implementation; no other harness tested.
- `--force` is a blunt instrument; finer-grained migration was not explored.