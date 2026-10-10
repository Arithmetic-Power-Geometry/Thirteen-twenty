# Experiment 64 — Why short-relation exclusion cannot solve LRC

Date: 2026-10-10
Status: rigorous all-dimensional no-go result for an overstrong proof strategy. Classical mathematics, not an original solution.

## Theorem 64.1 (tight configurations with short relations in every dimension)
For every integer k>=2, let V_k=(1,2,...,k), and define LR(V_k)=max_{t mod 1} min_{1<=j<=k} ||jt||. Then LR(V_k)=1/(k+1). At the same time, V_k has the nonzero short relation 2*v_1-v_2=0 of coefficient l1-norm 3, which is less than or equal to 2k+3.

## Proof
At t=1/(k+1), the residues j/(k+1), j=1,...,k, all have nearest-integer distance at least 1/(k+1), giving LR(V_k)>=1/(k+1).

For the reverse bound, consider the k+1 fractional parts {0,t,2t,...,kt} in the unit circle. If any two coincide, some nonzero difference j*t is an integer, and the desired upper bound holds. Otherwise order them around the circle. The k+1 circular gaps have total length one, so one gap has length at most 1/(k+1). The two points bounding that gap correspond to indices a,b with 0<=a<b<=k after relabeling; their difference gives 1<=j=|a-b|<=k with ||jt||<=1/(k+1). Thus min_j ||jt||<=1/(k+1) for every t, and equality follows. The relation 2*1-2=0 has norm 3. QED.

## Corollary 64.2 (no-go for relation elimination)
Any proposed proof of unrestricted LRC that requires every valid speed vector to be free of integer relations of norm <=2k+3 is false in every dimension k>=2. Moreover, scaling V_k by any positive integer preserves both its tightness and the relation, producing infinitely many such examples. These are not counterexamples to LRC.

## Consequence for Experiment 63
Beck and Everett's theorem supplies a necessary condition for counterexamples OR tight instances. The presence of a short relation cannot distinguish those two cases. Experiment 63's relation-free certificate remains correct, but the unresolved relation-bearing stratum is essential and cannot simply be excluded.

## Research decision
Do not continue trying to prove that short relations never occur. A valid next theorem must establish safety WITH relations, ideally by exploiting the sign pattern or additive structure of the relation. Do not label a relation as an obstruction to safety without a separate argument.

## Literature and provenance
Beck, Matthias and Everett, Samuel (2026), Lonely Runner Relations, arXiv:2609.06259, https://arxiv.org/abs/2609.06259 (primary source checked 2026-10-10).
Malikiosis, Romanos Diogenes; Santos, Francisco; Schymura, Matthias (2025), Linearly exponential checking is enough for the lonely runner conjecture and some of its variants, Forum of Mathematics, Sigma 13, e164, DOI 10.1017/fms.2025.10107 (publisher record checked 2026-10-10).
Both sources are already in references/lonely_runner.bib; avoid duplicates. The elementary tight example is classical and is not claimed as original.

## Verdict
Proved a dimension-uniform limitation of the prior strategy. Unrestricted LRC remains unsolved; independent Q1-level novelty: none.
