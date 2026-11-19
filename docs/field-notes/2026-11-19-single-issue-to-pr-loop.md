# Single issue→PR loop pilot

**Recorded:** 2026-11-19
**Label:** Pilot observation
**Evidence type:** Commands and outputs from one live run in this repository; PR and CI state observed on GitHub. The agent's own report was re-checked independently before it was trusted.
**Status:** One repository, one issue, one doc-only task, one private org.

**Limitations:** A documentation-only change. This proves the loop's mechanics, not that the agent can make correct code changes. No sandbox was used for the model call or tool execution; no autonomous trigger or cron fired the run; the issue→prompt conversion was manual. Cost and token use were not instrumented. One run is not reliability evidence.

## What was run

The narrow loop from `agents-home/docs/research/SOFTWARE_FACTORY_GROUNDING.md` §6: one trigger → one bounded agent session in a worktree → one PR → required checks → human merge.

1. **Trigger** — created the `ready-for-agent` label and issue [#16](https://github.com/magitech-ai/agents-home-pattern/issues/16) with an explicit "Done when" and verify command. No such issue existed in the org before this run.
2. **Isolation** — `git worktree add -b agent/issue-16 ../agents-home-pattern-wt16 main`. The main checkout stayed on `main` and clean.
3. **Home resolution from the worktree** — `hsh -p "reply with exactly: LOOP-WORKTREE-OK"` returned `LOOP-WORKTREE-OK`, confirming the agent resolves the shared home from an arbitrary worktree path.
4. **Bounded session** — `hsh` ran with the issue text, constraints ("edit only `docs/open-questions.md`", "do not use git, do not push") and the verify command in the prompt. It made one `read_file` call, edited the file, reported the diff and its check output.
5. **Independent verification** — `git status --short` showed exactly one modified file; `git diff` matched the agent's report; `python3 scripts/check_evidence.py` exited 0 with `Validated 11 field notes, local links and 9 conformance claims`.
6. **Publish** — committed, pushed `agent/issue-16`, opened [PR #17](https://github.com/magitech-ai/agents-home-pattern/pull/17).
7. **Required checks** — `Validate evidence`, `Analyze (actions)`, `Analyze (python)` and `CodeQL` all `SUCCESS`; `mergeStateStatus: CLEAN`.
8. **Human gate** — PR left **open** for human review and merge. Not merged by the agent.

## Recorded observations

- The end-to-end mechanism works with existing primitives only: `gh`, `git worktree`, `hsh`, the repo's own check script and branch protection. No new orchestrator or CLI was needed, matching the research recommendation not to build a bespoke CLI before repeated friction is documented.
- The agent stayed inside the stated scope: one file changed, no git operations, and its reported verification output matched an independent run.
- Friction encountered, all manual: creating the trigger label; creating the worktree; copying the issue body into the prompt; running the check; writing the commit message, push and PR. None of these is automated yet.
- The trust boundary is mostly host-level, not tool-level: the worktree isolates filesystem scope and branch protection gates the merge, but the session was not sandboxed and had no least-privilege GitHub credential.
- The task was deliberately small and reversible. A code-changing issue would also need a test-first contract, a diff review rule and a rollback path before this loop could be called trustworthy.

## What this does and does not prove

Proves: a `ready-for-agent` issue can drive a bounded agent session in an isolated worktree to a passing PR under a required check, with a human merge gate.

Does not prove: correctness on code changes, reliability across repeated runs, autonomy of the trigger, cost control, sandboxing, or that the output is representative. Those remain open questions.

## Reproduce

```sh
cd /mnt/storage/projects/magitech/agents-home-pattern
git worktree add -b agent/issue-16 ../agents-home-pattern-wt16 main
cd ../agents-home-pattern-wt16
uv run --project ../home-swe-home hsh -p '<issue body plus acceptance criteria>'
python3 scripts/check_evidence.py
```

## Relation to the pattern

This is the first recorded instance in this repository of the GitHub control-plane loop described in `docs/WORKFLOW.md`: an issue is the actionable unit, the worktree scopes execution, the repo's own check is the verification gate, and branch protection preserves human approval. It adds no new conformance claim.
