# Experiment 85 — Constructive nested-interval theorem for lacunary speeds

Date: 2026-10-10. Status: complete direct theorem in every dimension k>=2, with exact constructive witness and positive-measure safe interval. Unrestricted LRC remains open.

## Theorem 85.1 (nested safe intervals)
Let k>=2, q=k+1, delta=1/q, and 0<v_1<...<v_k be positive integers. Suppose for every 1<=i<k,
v_(i+1)/v_i >= 2k/(k-1) = 2(1-delta)/(1-2delta).
Then there exists a CLOSED interval I of length (k-1)/[(k+1)*v_k] on which every speed is safe:
||v_i*t||>=1/(k+1) for all i and all t in I.
In particular, the safe set has positive measure at least (k-1)/[(k+1)*v_k], and the LRC condition holds STRICTLY in the sense that its maximum loneliness is greater than 1/(k+1).

## Proof
For speed v, each closed allowed interval
J_(v,n)=[(n+delta)/v,(n+1-delta)/v], n integer,
has length (1-2delta)/v, and every t in it satisfies ||v*t||>=delta.

Initialize I_1=J_(v_1,0). Suppose I_i=[L,R] is a full allowed interval for speed v_i and lies in all earlier safe sets. Its length is (1-2delta)/v_i. The growth assumption implies
v_(i+1)*(R-L) >= 2(1-delta).
Let v=v_(i+1), and set n=ceil(v*L-delta). Then n+delta >= v*L. Since n < v*L-delta+1 (or <=), we have
n+1-delta <= v*L+2(1-delta) <= v*R.
Consequently J_(v,n) is contained in I_i. Define I_(i+1)=J_(v,n), and repeat. The final interval I_k has length (1-2delta)/v_k=(k-1)/[(k+1)*v_k] and is contained in every runner's safe set.

To see strict loneliness, take an interior point of I_k away from the finitely many boundaries ||v_i*t||=delta. All inequalities are then strict, so max_t min_i ||v_i*t|| >delta. QED.

## Explicit examples
- k=2: threshold ratio 4; (1,4) qualifies.
- k=3: threshold ratio 3; (1,3,9) qualifies.
- k=4: threshold 8/3; (1,3,9,27) qualifies.
- k=5: threshold 5/2; (1,3,9,27,81) qualifies.
- For every k>=3, the entire infinite family (a,3a,9a,...,3^(k-1)a), a positive integer, qualifies. More generally all successive ratios >=2k/(k-1) qualify, without requiring geometric progression.

## Why this is different from Experiments 79–84
This is a direct geometric proof producing a positive-length common safe interval. It neither computes forbidden intersections nor uses a finite boundary search, and does not depend on Beck–Everett's relation theorem. It proves an all-dimensional sufficient condition with an explicit rational witness and a quantitative safe-measure bound.

## Verification
experiments/experiment_85_nested_intervals.py implements the construction with exact Fraction arithmetic, checks containment at every stage and validates the final midpoint and endpoints. It tests k=2,...,30 and multiple families with ratios at least the theorem threshold. The analytical proof applies to arbitrary dimension, independently of those tests.

## Literature, novelty, and limits
Beck–Everett (2026), Lonely Runner Relations, arXiv:2609.06259, proves short-relation constraints for tight/counterexample configurations, yielding other lacunarity corollaries. Beck–Hosten–Schymura (2016), Lonely Runner Polyhedra, arXiv:1606.01783, treats geometric sufficient families. The nested-interval argument is elementary and may be known; no first-discovery or Q1 novelty is claimed without direct comparison. Existing Beck–Everett entry in references/lonely_runner.bib; the 2016 paper's BibTeX status must be checked and, if missing, a primary-source-verified entry appended.

## Verdict
Proved an infinite class for every dimension with a positive-measure interval. Did NOT prove unrestricted LRC; vectors without the growth condition remain unresolved.
