# Reviewer false-positive remediation

**Recorded:** 2026-11-20
**Label:** Pilot observation
**Evidence type:** Six live 38-case evaluations before and after the fix; three final runs preserved in [`data/`](data/).
**Status:** One model, one suite, three final trials.

**Limitations:** A single model version. The remaining false positive is `clean-contract`, where the reviewer substitutes a remembered API shape for an explicitly stated field type. Ten percent meets the D-013 bar but is not zero.

## What changed

- The review standard forbids invented requirements and states that explicit criteria take precedence over remembered API shapes.
- Clean-control specs name in-scope files and exact field types.
- An experimental API-facts section did not help and was removed.

No bar, verdict rule, or model was changed.

## Results

| Run | Detection | False APPROVE | Clean controls rejected | FP rate |
| :--- | :--- | :--- | :--- | :--- |
| Before (3 runs) | 28/28 | 0 | 3/10 | 30% |
| Final 1 | 28/28 | 0 | 1/10 | 10% |
| Final 2 | 28/28 | 0 | 1/10 | 10% |
| Final 3 | 28/28 | 0 | 1/10 | 10% |

## Reproduce

```sh
cd /mnt/storage/projects/magitech/home-swe-home
uv run hsh-review-eval --provider gemini --model gemini-3.8-flash --out results.json
```
