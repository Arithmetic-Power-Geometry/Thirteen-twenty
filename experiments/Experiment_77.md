# Experiment 77 — Universal normalized-pair obstruction for tight configurations

Date: 2026-10-10
Status: complete theorem in all dimensions, plus exact finite census. Independent novelty NOT established; general LRC UNSOLVED.

## Theorem 77.1
Let k>=2, q=k+1 and V=(v_1,...,v_k) be distinct positive integer speeds. If L(V)=max_t min_i ||v_i*t|| equals 1/q, then there are distinct indices i,j such that q divides (v_i+v_j)/gcd(v_i,v_j).

## Proof
Write F(t)=min_i ||v_i*t||. The function F is continuous and piecewise affine on the circle. On any open subinterval avoiding the finitely many cusps and pairwise crossings of its constituent distance functions, F equals one of the affine branches, each with slope +v_i or -v_i, hence nonzero. Therefore F cannot be identically equal to 1/q on any nonempty open interval.

Assume L(V)=1/q. The safe set S={t:F(t)>=1/q} is exactly the set of global maximizers {t:F(t)=1/q}. Because F is piecewise affine with finitely many breakpoints and has no flat positive-length segment, S is finite, so every safe time is isolated.

At an isolated safe time t*, at least one active constraint is on the boundary v_i*t*=n+1/q and another distinct active constraint is on the opposite boundary v_j*t*=m-1/q: otherwise a small one-sided displacement would preserve safety. Put g=gcd(v_i,v_j), A=v_i/g, B=v_j/g. Eliminating t* gives B*n-A*m=-(A+B)/q. The left side is an integer, so q divides A+B. QED.

## Corollary 77.2 (rigorous exclusion of tightness)
If q does not divide (v_i+v_j)/gcd(v_i,v_j) for every pair i<j, then L(V) is NOT equal to 1/q. More precisely, either L(V)<1/q (a counterexample) or L(V)>1/q (strictly safe). One must not infer strict safety without a separate proof of existence.

## Exact arithmetic census
Script: experiments/experiment_77_pair_obstruction.py
The script enumerates all primitive ordered-increasing k-speed sets from 1,...,N, and counts those with no normalized complementary pair:
k=3, N=15: 409 primitive, 215 excluded from tightness.
k=4, N=12: 479 primitive, 141 excluded.
k=5, N=12: 786 primitive, 354 excluded.
These counts were independently computed with Python's exact integer gcd and combinations; no floating-point operations.

## Relation to previous experiments
Experiments 67 and 68 characterized an isolated witness. The new step is proving that EVERY safe time of a tight configuration must be isolated. The resulting necessary condition now applies to all tight configurations. This does not rule out counterexamples and therefore is not a universal LRC proof.

## Literature and priority
Tight instances and critical-time arithmetic are well developed. Relevant verified references already in references/lonely_runner.bib:
- Goddyn, Luis and Wong, Erick B. (2006), Tight instances of the lonely runner, Integers 6, A38.
- Fan, Ho Tin and Sun, Alec (2026), Amending the Lonely Runner Spectrum Conjecture, Electronic Journal of Combinatorics 33(1), P1.38, DOI 10.37236/13840.
- Zhang, Yuhan (2026), Tight instances of the Lonely Runner Conjecture: complete classification of one-entry modifications, a new infinite family, and the growth bound, arXiv:2608.13599v2.
These records have been checked against the primary publisher/arXiv or author records. The theorem-level originality of this gcd-normalized condition has NOT been independently established, and no first-discovery claim is made.

## Next research requirement
A successful universal proof must exclude the possibility L(V)<1/q as well as characterize equality. A necessary condition for equality alone does not settle the conjecture.
