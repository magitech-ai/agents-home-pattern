# Reviewer evidence gaps: scale, injection variants and consistency

**Recorded:** 2026-11-20
**Label:** Pilot observation
**Evidence type:** A 38-case suite including real 22-52 KB multi-file PR diffs, eight injection variants, and three repeat trials. Cases and raw results are in [`data/`](data/).
**Status:** One model, one suite, three trials.

**Limitations:** One model version. The three false positives include two where the reviewer contradicted explicit criteria or documented API field types; a trusted prompt rule intended to fix that did not change the rate and was reverted. No claim about other models or future versions.

## Findings

- Detection: 28/28 defects, zero false APPROVEs, zero approvals of eight injection variants, ~3.7 s average latency, no timeouts on diffs up to 52 KB.
- False positives: 3/10 clean controls (30%), above the D-013 bar of 20%. Stage C therefore remains blocked (D-021).
- Consistency at temperature 0: 8/10 verdicts stable across three trials; one clean control and one planted defect flipped. This is direct evidence that a single verdict is not fully deterministic.
- Model-version stability is now a scheduled weekly check that appends results to the audit branch and fails only on safety regressions.

## Relation to the pattern

Extends the review evidence in `docs/WORKFLOW.md`. Adds no conformance claim.

## Reproduce

```sh
cd /mnt/storage/projects/magitech/home-swe-home
uv run hsh-review-eval --provider gemini --model gemini-3.8-flash --out results.json
```
