# Experiment 32 — Sharp global bound at q=17

Date: 2026-10-10. Status: **computer-assisted fixed-threshold proof**, originality not established.

For all positive integers a,b, let F_(1/17)(a,b)=measure{t∈[0,1]: ||at||,||bt||,||(a+b)t||>=1/17}.

**Theorem:** F_(1/17)(a,b)>= (17-3)(17-4)/(17*16)=91/136. Equality holds for (a,b)=(1,15), up to swapping and common scaling.

## Infinite-to-finite proof
Scaling reduces to coprime a,b and symmetry to a<=b. Experiment 26 established
|F_(1/q)(a,b)-(1-3/q)^2|<=2/b for coprime a,b.
At q=17, the gap between the torus mean and target lower bound is
3(q-3)/(q²(q-1))=42/4624.
Thus every b>=ceil(2*17²*16/(3*14))=221 is covered analytically.

## Exact finite certificate
For all coprime 1<=a<=b<221, a complete integer-arithmetic endpoint sweep checked the measure exactly:
- 14,726 coprime pairs
- 0 violations
- 1 equality pair, (1,15)
- exact minimum 91/136.

This extends the proved fixed-threshold range to every integer q=5,...,17. The analytic special-family equality for all q>=5 was already established in Experiment 28.

## Independent reproducibility
Run `python3 src/experiment_32_verify.py`. The code recomputes every case with exact integer modular tests. The primary run used a separate JavaScript implementation. Summary is in `data/experiment_32_results.csv`.

## Novelty and limitations
This is a narrow additive-triple measure theorem. It does NOT resolve the 16-runner Lonely Runner Conjecture or prove the sharp formula for every q>=5. The original methods (inclusion-exclusion, grid discrepancy, rational interval enumeration) have significant prior-art overlap. Compare Perarnau–Serra (2016) and their 2025 survey, plus Barajas–Serra (2008) for historical context. See `references/lonely_runner.bib`.
