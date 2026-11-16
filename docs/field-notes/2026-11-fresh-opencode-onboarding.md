# Fresh OpenCode Onboarding Pilot

**Recorded:** 2026-11-15
**Evidence type:** User-directed fresh-session test with exported transcript
**Status:** One-machine pilot; limited to OpenCode v2.3.0

## Test setup

- Repository: private
  [`magitech-ai/agents-home`](https://github.com/magitech-ai/agents-home),
  launched as the OpenCode working directory.
- Harness: OpenCode v2.3.0.
- Prompt: inspect the repository guidance and relevant pattern notes without
  changing files or installing anything; verify skill discovery and report
  onboarding gaps.
- Session export:
  [`2026-11-15-fresh-agent-onboarding.json`](../../evidence/opencode/2026-11-15-fresh-agent-onboarding.json).

## Recorded outcome

The session transcript records that the agent:

- Read the root `AGENTS.md`, `README.md`, and skill catalog, then inspected
  the pattern notes and skill installer.
- Checked the local skill links and found 30 canonical skills linked to
  `agents-home`; it also observed three unrelated symlinks and 33 unrelated
  skill directories in the user's global directory.
- Invoked `writing-for-agents` and explicitly loaded the normally hidden
  `ask-matt` skill. It reported 13 skills advertised for model selection and
  17 with `disable-model-invocation: true`.
- Ran the four installer unit tests successfully and made no file changes.
- Identified that the global skill installation is a precondition on a new
  machine, and that the then-current README's “not smoke-tested” statement had
  become stale.

The transcript includes tool invocations and results for the checks and skill
loads. Interpretations and recommendations in the agent's final answer remain
the agent's analysis, not independent proof.

## What this pilot supports

- A fresh OpenCode session in this checkout could use the root guidance and
  installed global skills without prior conversation context.
- Explicit invocation provides a route to skills excluded from automatic
  model selection.
- The repository explains the canonical source and installer, but did not
  yet make preflight checking or intentional non-invocation prominent enough.

This does not show that an unconfigured clone has the shared skills available:
the test machine already had the global symlink installation. It also does not
validate another OpenCode version, harness, user account, operating system, or
all skill behavior.

## Follow-up

The onboarding guidance in `agents-home` was updated to:

1. Run the installer `check` action before relying on shared skills, and run
   `install` if links are missing.
2. Explain that `disable-model-invocation: true` prevents automatic selection
   but does not prevent explicit skill invocation.
3. Replace the stale “not smoke-tested” statement with a scoped record of this
   single OpenCode pilot.

See the subsequent changes in the
[`agents-home` repository](https://github.com/magitech-ai/agents-home).
