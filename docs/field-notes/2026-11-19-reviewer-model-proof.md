# Reviewer model: burden-of-proof investigation

**Recorded:** 2026-11-19
**Label:** Pilot observation
**Evidence type:** Official model documentation, a reasoning-effort prototype, a saturated 28-case suite and an 8-case hard-mode suite with reason-matching. Hard-mode cases and raw results are in [`data/`](data/).
**Status:** One investigation, three models compared at different stages.

**Limitations:** The hard-mode suite has 8 cases; its reason-matching heuristic checks that the finding text contains a known defect token, not that the reasoning is sound. One clean control was itself ambiguous and rejected by both models. No statistically significant sample.

## Question and outcome

The user asked that flash-lite be proven better if I advocated it, with the burden of proof on me. It was not met. The full analysis is in `agents-home/docs/research/REVIEWER_MODEL_DECISION.md`.

- Google positions 3.8 Flash for long-horizon software engineering and verification, and 3.1 Flash-Lite for simple high-volume processing. The only deprecation was the Flash-Lite *preview*, not GA.
- On the saturated 28-case suite all models scored 100% detection with zero false APPROVEs and zero injection approvals. Flash-Lite had 0 false positives, 3.8 Flash 1 (within the bar).
- On the discriminating hard suite, both detected 7/7 defects; 3.8 Flash identified the actual reason in 7/7 versus 6/7 for Flash-Lite.
- The audit branch showed 2 live timeouts from Gemma, which was retired. No timeouts were observed for either Gemini model.

## Outcome applied

3.8 Flash remains the default. The investigation found a free improvement: `reasoning_effort="low"` gives identical suite metrics at 2.7x the speed (4.46s vs 11.86s). It is now sent to the Gemini provider only; `minimal` is rejected by the API.

## Relation to the pattern

Evidence for a control-plane choice, not a conformance claim.
