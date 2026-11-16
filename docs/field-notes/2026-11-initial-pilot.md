# Initial Magitech Pilot

**Recorded:** 2026-11-15
**Evidence type:** Pilot observations plus linked vendor documentation
**Status:** Snapshot of one user's setup; not a compatibility guarantee

## Setup exercised

The Magitech workspace uses a private shared repository, now named
[`agents-home`](https://github.com/magitech-ai/agents-home), alongside several
separate code repositories. The shared repository began as `home` and was
renamed after distinguishing the repository's role from a machine's home
directory.

In this setup:

- Shared skills are maintained in `agents-home/skills/`, with each skill as a
  direct child directory containing `SKILL.md`. A catalog records source and
  license provenance.
- Shared guidance lives in `agents-home/AGENTS.md`; sibling repositories keep
  their own instructions and point to shared guidance and skills where useful.
- The personal `~/.agents/skills/` directory exposes each canonical skill
  through a symlink. At the time of this snapshot, 30 shared skills were
  linked, while 33 unrelated user skill directories remained in place.
- On this machine, `~/.gemini/config/skills` is itself a symlink to
  `~/.agents/skills`. The two configured paths therefore resolve to one
  effective directory here; this is a property of this machine's setup, not a
  claim about Antigravity defaults.
- `agents-home/scripts/sync_skills.py` provides `install`, `check`, and
  `uninstall` actions. It leaves unrelated skills alone, fails on conflicting
  names before creating links, and is idempotent for links it manages.
- The script was tested for conflict handling, repeat installation, checking,
  and selective uninstall in temporary directories. The current symlinks were
  also checked after installation.
- The repository rename required updating relative paths in the sibling
  repositories. That work was merged through pull requests.

## What this pilot suggests

1. **Separate authoring from discovery.** Keeping the maintained copy in
   `agents-home` avoids treating a harness-specific directory as the source of
   truth.
2. **Use real discovery paths as adapters.** In this setup, `~/.agents/skills`
   reaches multiple harnesses according to their documentation; a symlink
   exposes the canonical skill folders there without maintaining copies.
3. **Keep repository-specific guidance local.** A shared home can orient an
   agent across projects without replacing each project's own `AGENTS.md`.
4. **Preserve unrelated configuration.** A distribution mechanism should
   avoid claiming or deleting skills it did not install.

These are early design signals from one user's machine and organization. They
are not yet demonstrated across multiple independent users, operating systems,
or all product surfaces.

## Documented discovery behavior checked for this snapshot

The following is evidence from product documentation, not a runtime matrix:

| Harness / standard | Documented or observed location | Evidence and limitation |
| --- | --- | --- |
| OpenCode | Global `~/.agents/skills`; project `.agents/skills` | Listed as compatibility locations in [OpenCode's skill documentation](../sources.md#harness-discovery-documentation). |
| GitHub Copilot CLI | Personal `~/.agents/skills`; project `.agents/skills` | Explicitly listed in [GitHub's CLI guide](../sources.md#harness-discovery-documentation); other Copilot surfaces can differ. |
| Antigravity App | Global `~/.gemini/config/skills`; workspace `.agents/skills` and parent directories | Explicitly listed in [Antigravity's skill documentation](../sources.md#harness-discovery-documentation). The local symlink makes its global path resolve to `~/.agents/skills` on this machine. |
| Codex | Repository `.agents/skills` in the working-directory ancestry; other scopes also exist | Described in [Codex's skills documentation](../sources.md#harness-discovery-documentation); this pilot did not test Codex loading the personal collection. |
| DeepSeek Harness | The project repository itself contains skills under `.agents/skills` | A repository-tree observation only. The exact user-level and runtime discovery contract needs a revision-specific primary-document citation and direct test. |

The broader `.agents` directory convention is distinct from the standardized
Agent Skills bundle format. Support for `.agents/skills` does not mean these
harnesses implement the full draft `.agents` Protocol.

## Known limitations and failure modes

- The installer creates absolute symlinks. Moving the canonical checkout can
  leave broken links until they are reinstalled.
- Symlink behavior and permissions can differ across operating systems,
  filesystems, containers, and remote development environments.
- Harness reload behavior and same-name conflict/precedence rules have not
  been tested consistently across the user's four target harnesses.
- A skill being present at a documented path does not prove a specific
  harness version will load it, or that its instructions behave as intended.
- A private canonical repository cannot be assumed accessible to collaborators
  or machines that do not have its checkout.

## Next validation steps

- Record exact versions and directly test discovery and invocation in OpenCode,
  Antigravity, Copilot, and DeepSeek Harness.
- Repeat the install flow on another machine and at least one environment
  without symlink support.
- Ask another person to reproduce the pattern independently, noting which
  decisions they make differently.
- Use the [open questions](../open-questions.md) to decide what evidence would
  justify keeping, revising, or dropping each part of the hypothesis.
