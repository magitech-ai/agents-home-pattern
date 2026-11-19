# Code-changing issue→PR loop pilot

**Recorded:** 2026-11-19
**Label:** Pilot observation
**Evidence type:** Commands and outputs from one live run in `anima`; PR and CI state observed on GitHub. The agent's change was re-verified independently before publication.
**Status:** One repository, one issue, one small code change with tests, one private org.

**Limitations:** One small bug fix is not evidence of reliability on larger changes. No sandbox, no autonomous trigger, no least-privilege credential, no cost instrumentation. The issue→prompt conversion and all publishing steps were manual. One run cannot establish a pass rate.

## What was run

A second execution of the loop recorded in
[the single issue→PR pilot](2026-11-19-single-issue-to-pr-loop.md), this time on a code-changing issue with strict gates.

1. **Trigger** — [anima#81](https://github.com/magitech-ai/anima/issues/81), a bounded defect split from the broader #27. Verified against local `main` `5c3261d`: `DisposableList.push()`/`unshift()` return a disposer that pops `_map` but never `_weak`, so every push/dispose cycle leaks a `_weak` entry.
2. **Isolation** — `git worktree add -b agent/issue-81 ../anima-wt81 main`; main checkout stayed clean on `main`.
3. **Home resolution** — `hsh` from the worktree returned `CODE-LOOP-OK`.
4. **Bounded session** — `hsh` ran with the issue body, a "change only these two files" constraint, a "do not use git/push/PR" constraint and four pass/fail commands. It edited `src/anima/events.py` and added `tests/unit/test_events_disposable_list_weak.py`.
5. **Independent verification** — `git status` showed exactly the two intended files; the diff introduced a small `_make_disposer` helper guarded by `_weak.get(value) == sn` so a stale disposer cannot remove a newer registration of the same value. Locally: `uv run pytest -q` → 1299 passed, 100% statement and branch coverage; `ruff check`, `ruff format --check`, `mypy` all clean; shared `check_all.py --fast` → ALL GREEN.
6. **Publish** — [anima PR #82](https://github.com/magitech-ai/anima/pull/82) opened.
7. **Required checks** — `Test & Lint` on ubuntu, macos and windows, plus Actions/Python analyze and CodeQL: all `SUCCESS`, `mergeStateStatus: CLEAN`.
8. **Human gate** — PR left open for review and merge.

## Recorded observations

- The agent handled a real code change, not just prose: it chose a helper method, covered the stale-disposer edge case with targeted tests, and maintained 100% branch coverage under `anima`'s strict settings.
- Independent verification matched the agent's reported results exactly. This is the second consecutive run where the agent's self-report was accurate.
- The change is scoped and reversible: two files, no git operations by the agent, no writes outside the worktree.
- **New friction:** the shared pre-commit hook infers "current repo" from the working directory. Run from a worktree, its repo-map check reported ten false drift findings (it believed every mapped repo's origin was `anima`'s) and an unmapped local checkout. Findings are informational and the gate stayed green, but the noise is misleading. The same gate run from `agents-home` was clean.
- **Repo hygiene finding, not caused by this run:** `anima` has many open issues already fixed on `main` (for example #28 was resolved by PR #72, #23 by PR #70). Picking a genuinely open task required checking recent commit history, not just the issue list.
- All orchestration steps remain manual: label creation, issue creation/splitting, worktree setup, prompt assembly, verification, commit, push and PR.

## What this does and does not prove

Proves: a `ready-for-agent` issue can drive a bounded agent session in an isolated worktree to a correct, tested code change that passes strict local gates and six required CI checks across three operating systems, with a human merge gate.

Does not prove: reliability across repeated runs, behaviour on larger or architectural changes, autonomy of the trigger, sandboxing, credential least privilege, or cost control.

## Reproduce

```sh
cd /mnt/storage/projects/magitech/anima
git worktree add -b agent/issue-81 ../anima-wt81 main
cd ../anima-wt81
uv run --project ../home-swe-home hsh -p '<issue body plus acceptance criteria>'
uv run pytest -q && uv run ruff check src tests && uv run mypy src
```

## Relation to the pattern

Second instance of the `docs/WORKFLOW.md` control-plane loop, now with a code change and a real verification gate. It adds one recorded friction (CWD-dependent hook) and one hygiene observation (stale issues), neither of which changes any conformance claim.
