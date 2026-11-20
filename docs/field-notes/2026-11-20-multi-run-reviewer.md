# Multi-run reviewer prototype

**Recorded:** 2026-11-20
**Label:** Pilot observation
**Evidence type:** Two full 38-case triage runs plus per-trial raw verdicts in [`data/`](data/).
**Status:** One model, two aggregation rules, one run each.

**Limitations:** Single model version and one run per rule. A targeted 10-run check on one unstable defect is recorded in the raw data but is not a population estimate. The gate remains single-trial.

## Results

| Rule | Detection | False APPROVE | FP | Avg latency | Tokens |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Majority (2/3) | 28/28 | 0 | 1/10 | 9.9 s | 328k / 15k |
| Unanimous (3/3) | 28/28 | 0 | 2/10 | 10.3 s | 328k / 16k |

Both rules preserve the safety metrics. Majority keeps the FP rate at 10%; unanimous doubles it to 20%, still within the bar. Cost is roughly 3x a single review.

## Reproduce

```sh
cd /mnt/storage/projects/magitech/home-swe-home
uv run hsh-review-eval --provider gemini --model gemini-3.8-flash --trials 3 --rule majority --out results.json
```
