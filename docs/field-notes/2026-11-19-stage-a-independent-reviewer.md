# Stage A independent reviewer pilot

**Recorded:** 2026-11-19
**Label:** Pilot observation
**Evidence type:** Live reviewer runs on a synthetic diff and on a real PR, plus PR/CI state observed on GitHub. The reviewer's verdict was not treated as proof of correctness; deterministic gates still ran.
**Status:** One repository (`home-swe-home`), one real PR, one reviewer model.

**Limitations:** One real PR is not a catch-rate measurement. No injected-defect campaign, no cost instrumentation, no reliability sample. The reviewer has no tools and judges from the diff and standards only, so it cannot detect problems invisible in those inputs. Stage B (earn the right to auto-merge) has not started; the human merge gate remains.

## What was built

- `hsh-review` in `home-swe-home`: an information-light reviewer. It receives the diff, the issue's acceptance criteria and local standards; it never receives the author's transcript, reasoning or verification claims, and has no tools.
- It uses a model different from the author by construction. `check_distinct_models` fails closed (exit 2) when the two model ids match.
- Output is a strict JSON verdict (`APPROVE` / `REQUEST_CHANGES`) with evidence-citing findings; malformed output fails closed.
- A PR workflow posts the verdict as a comment and enforces it through the required `Agent review` check. Human merge is preserved.
- The reviewer provider is configurable (`--reviewer-provider`), with the provider registry kept open-ended (D-011).

## Recorded observations

- On a synthetic diff whose `main()` was never called, the reviewer returned `REQUEST_CHANGES` with a blocker citing the exact lines and the missing entry point. On the corrected diff it returned `APPROVE`. This is direct evidence it is judging the material rather than rubber-stamping.
- The same-model guard returned exit 2 with a clear refusal.
- The first reviewer model tried (`mistralai/mistral-large-4-1t-a52b`) timed out repeatedly, once after more than ten minutes in CI. An explicit 180-second timeout, zero retries and a 100k-character diff limit were added so a slow or oversized review fails closed instead of hanging.
- `google/gemma-4-31b-it` reviewed the same real material in about four seconds and produced a well-formed verdict. It is now the default; it is a different model and family from the author's `gemini-4-hydrogen`, served through a different provider.
- On the real PR (#43), the reviewer returned `APPROVE` with a cited summary; `Agent review` and the three OS CI jobs all succeeded before merge.
- Workflow setup required `issues: read` in addition to `pull-requests: write`: without it the trigger issue could not be fetched and the check failed closed. The PR template now requires both `Trigger issue` and `Author model` fields.

## What this does and does not prove

Proves: an independent, information-light reviewer can run on a real PR, produce a cited verdict, enforce it as a required check, and catch a planted defect in a controlled case, while the human merge gate stays intact.

Does not prove: a measured catch rate, reliability across reviewers or task types, cost control, or that removing the human gate is safe. Those are Stage B questions under D-010.

## Relation to the pattern

Concrete instance of the GitHub control-plane loop in `docs/WORKFLOW.md`: an issue is the actionable unit, the worktree scopes execution, deterministic gates and an independent reviewer are required checks, and branch protection preserves human approval. It adds no conformance claim.
