# Antigravity Onboarding Evaluations

**Recorded:** 2026-11-15
**Evidence type:** Two user-directed, read-only Antigravity desktop-app sessions
**Status:** One-machine pilot; app version was not recorded

**Limitations:** One-machine pilot; app version not recorded.

## Test setup

Both sessions used `/mnt/storage/projects/magitech/agents-home` as the
workspace. The first evaluated the onboarding guidance before the recent
OpenCode-driven edits. The second used the updated evaluation prompt after
those edits.

The local Antigravity app stored each conversation in a separate SQLite
database under
`~/.gemini/antigravity/conversations/<conversation-id>.db`; its
`conversation_summaries.db` contains an index with titles, workspace paths,
and searchable conversation text. The linked
[Antigravity overview](https://antigravity.google/docs/overview), checked on
2026-11-15, does not document this local storage path or a portable transcript
export format. Treat the observed path and format as local implementation
details, not a documented contract.

The archived `.db` files below are unmodified SQLite backup snapshots of the
individual conversation databases. They passed SQLite's `integrity_check`.
They use an app-internal schema and may not be conveniently readable outside
Antigravity. They contain local paths and session contents, so retain them
only in this private evidence repository.

## Sessions

### Initial evaluation

- Conversation: `25202278-b775-4995-a5f0-8799346a110d`
- Title: “Agent Onboarding and Repository Evaluation”
- Last user input: 2026-11-16 02:13 UTC
- Archived snapshot: [`2026-11-15-initial-onboarding-evaluation.db`](../../evidence/antigravity/2026-11-15-initial-onboarding-evaluation.db)
- The agent reported it could not verify OpenCode behavior from Antigravity,
  noted that several linked skills were absent from its advertised list, and
  proposed adding an explicit preflight and fallback guidance.

### Updated evaluation

- Conversation: `973d7dcc-b5cc-4907-b99e-b58790d58d34`
- Title: “Agents-Home Repository Onboarding Evaluation”
- Last user input: 2026-11-16 03:22 UTC
- Harness/model as reported by the agent: Antigravity, Claude Opus 5.5
- Archived snapshot: [`2026-11-15-updated-onboarding-evaluation.db`](../../evidence/antigravity/2026-11-15-updated-onboarding-evaluation.db)
- The agent ran the documented skill-link `check`, reported 30 links valid
  across one effective target, and saw 13 skills advertised versus 17 marked
  `disable-model-invocation: true`.
- It could read an advertised skill's `SKILL.md`, but reported no Antigravity
  agent-side tool for invoking a skill by name. It could not verify whether
  users can explicitly invoke hidden skills.
- It found the preflight explanation clearer than before, while noting that
  “Run the installer” could misleadingly imply that the `check` command
  installs anything. It also questioned whether “can still be invoked
  explicitly by skill name” applies to every harness.

## Interpretation and limitations

These are agent-reported observations, not proof of behavior in other
Antigravity versions, machines, or harness surfaces. In particular, a local
database snapshot establishes where these two sessions were stored on this
machine; it does not establish a supported export workflow.

The local search index's text for the updated session begins with the
unexplained phrase “Need the truncated middle.” The raw conversation database
was preserved without editing; consult the Antigravity app if the exact
user-visible response matters.