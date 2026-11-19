# Stage B: injected-defect evaluation of the reviewer

**Recorded:** 2026-11-19
**Label:** Pilot observation
**Evidence type:** A fixed 16-case suite run against two reviewer models with real API calls. Raw verdicts, timings and token counts are preserved in [`data/`](data/); the case suite itself is versioned in `home-swe-home/src/home_swe_home/review_cases.json`.
**Status:** One suite, two models, one run each.

**Limitations:** 16 small synthetic cases are not proof of production reliability, and two models are not the whole model space. The suite was corrected twice before the final run (see below), so these numbers describe the corrected suite only. No adversarial/prompt-injection cases, no long or multi-file real PRs. The human merge gate remains; this evidence does not by itself justify Stage C.

## Bar, fixed before measurement

`agents-home/docs/DECISIONS.md` D-012: ≥15 cases with ≥3 clean controls and ≥3 contract-fidelity defects; zero false APPROVEs on any defect case; ≥95% blocker detection; ≤20% false positives on clean controls; two reviewer models with latency and token cost recorded.

## Results

| Model | Provider | Cases | Detection | False APPROVE | False positives | Avg latency | Prompt / completion tokens |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `google/gemma-4-31b-it` | nvidia | 16 | 12/12 (100%) | 0 | 0/4 (0%) | 8.61 s | 9,538 / 1,856 |
| `gemini-3.1-flash-lite` | gemini | 16 | 12/12 (100%) | 0 | 0/4 (0%) | 1.11 s | 8,850 / 1,485 |

Both models satisfy every D-012 condition. `gemini-3.1-flash-lite` is ~8x faster with slightly lower token use, but shares a vendor with the author model (`gemini-4-hydrogen`); `gemma-4-31b-it` is a different model family served through a different provider. The Stage-A default remains Gemma for that independence reason.

## Fixture corrections (transparency)

The first run produced 3 false positives on cases labelled clean. Inspection showed the reviewer was **correct**: those diffs changed behaviour without adding tests, which violates our own review standard. The controls were fixed to include matching tests. A second run still produced 2 false positives because the synthetic diffs were internally inconsistent (a dict called as a function; a class missing `__init__`/`push`). Those were fixed too. No bar condition was changed, and no defect case was weakened. The final run used the corrected suite and is the one reported above.

This is itself evidence that the reviewer is applying the standard rather than approving indiscriminately.

## What this does and does not prove

Proves: on a fixed suite of small, known defects and clean controls, two different reviewer models hit 100% blocker detection with zero false APPROVEs and zero false positives, with recorded latency and token cost.

Does not prove: reliability on large or multi-file real PRs, resistance to prompt injection in issue text, stability across model version changes, or that a human per-PR gate is now unnecessary. Stage C remains a separate decision under D-010.

## Relation to the pattern

Adds measured evidence to the review step of `docs/WORKFLOW.md` and the Stage-A field note. It makes no new conformance claim for the portable pattern.
