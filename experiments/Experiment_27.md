# Experiment 27 — Candidate exact formula at reciprocal thresholds

**Date:** 2026-10-10. **Status:** 196 exact finite verifications; global identity **CONJECTURAL**, not a solved theorem.

## Question
For integers q≥5, put δ=1/q and use the additive triple of speeds
`(1,q-2,q-1)`. Evaluate
`F_(1/q)(1,q-2)=μ{t∈[0,1]: ||t||,||(q-2)t||,||(q-1)t||≥1/q}`.

## Exact observed identity
For every integer q=5,…,200, an exact integer interval sweep agrees with

`F_(1/q)(1,q-2) = (q-3)(q-4)/(q(q-1))`.

Examples: q=5 gives 1/10; q=8 gives 5/14; q=16 gives 13/20; q=20 gives 68/95; q=32 gives 203/248. These are exact equalities in the tested range. The 196-case data are in `data/experiment_27_q_5_to_200.csv`; reproduce using `python3 src/experiment_27_exact.py 200`.

**Not proved for all q:** this is a candidate formula supported by exact finite testing, not a mathematical theorem for arbitrary q. It also does not establish that this triple minimizes F_(1/q) over all speeds.

## Proven general fact inherited from Experiment 26
For coprime a,b and 0<δ≤1/4:
`|F_δ(a,b)-(1-3δ)^2| ≤ 2/max(a,b)`.
This gives an analytic finite-reduction method but does not imply the proposed exact identity above.

## Next proof target
Derive a symbolic interval-overlap count for the three speeds `1,q-2,q-1` that holds for all q≥5. Then test the **global minimizer** hypothesis against other speed pairs with a complete finite reduction. Neither step is complete.

## Novelty and prior art
Perarnau and Serra, *Correlation among runners and some results on the Lonely Runner Conjecture* (Electronic Journal of Combinatorics 23(1), 2016, DOI 10.37236/5123) studies forbidden-set correlations. Jensen, *Mixed thresholds in the Lonely Runner Conjecture* (arXiv:2605.27941, 2026), includes threshold-function Fourier and integral formulas. Neither was exhaustively checked theorem-by-theorem for the proposed identity. **No originality or priority claim.**

## Answer to 'have we solved it?'
- Sharp fixed-threshold (δ=1/16) additive-triple measure bound: yes, computer-assisted proof recorded in Experiment 25.
- General variable-threshold minimization: no.
- Candidate q-formula for all q: not yet.
- Sixteen-runner Lonely Runner Conjecture: no.
