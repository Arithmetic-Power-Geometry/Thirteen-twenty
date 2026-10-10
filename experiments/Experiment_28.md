# Experiment 28 — Exact reciprocal-threshold formula (PROVED)

**Date:** 2026-10-10

## Theorem
For every integer q>=5, set δ=1/q and relative speeds (1,q-2,q-1). With ||x|| denoting distance to the nearest integer, define

F_q = measure{t in [0,1]: ||t||,||(q-2)t||,||(q-1)t|| >= 1/q}.

Then **F_q = (q-3)(q-4)/(q(q-1))**.

This is an analytic proof for all q>=5; it is not extrapolated from finite numerical checks.

## Proof
The speed-1 safe interval is I=[1/q,1-1/q]. Put n=q-1 and m=q-2. The forbidden intervals for speed n inside I are centered at j/n (1<=j<=n-1=q-2) with radius 1/(qn). They are all contained in I, possibly touching its endpoints, and have combined length 2(q-2)/(q(q-1)). Likewise, speed m contributes m-1=q-3 intervals centered at k/m (1<=k<=m-1=q-3), radius 1/(qm), combined length 2(q-3)/(q(q-2)).

A speed-n forbidden interval centered at j/n intersects a speed-m forbidden interval centered at k/m only if
|jm-kn|/(nm) < (n+m)/(qnm),
i.e. |j(q-2)-k(q-1)| < (2q-3)/q = 2-3/q < 2.

The left-hand side is a nonnegative integer and cannot vanish: gcd(m,n)=1 and 1<=j<=n-1, 1<=k<=m-1. Thus it must be 1. Since jm-kn = (j-k)m-k, the only possible pairs in these ranges are (j,k)=(1,1) and (j,k)=(n-1,m-1). (One can also solve the Bezout equation modulo m and n.) The overlap length for each pair is
1/(qn)+1/(qm)-1/(nm)=(q-3)/(qnm).
There are exactly two overlaps, and the same-speed forbidden intervals are mutually disjoint.

By inclusion–exclusion inside I:
F_q = 1-2/q - 2(q-2)/(q(q-1)) - 2(q-3)/(q(q-2)) + 2(q-3)/(q(q-1)(q-2))
= (q-3)(q-4)/(q(q-1)).
This completes the proof.

## Checks and connection to earlier experiments
- q=5: 1/10
- q=8: 5/14
- q=16: 13/20, corresponding to relative speeds (1,14,15)
- q=20: 68/95
- q=32: 203/248
- Experiment 27 had 196 exact finite checks for q=5..200; the present proof removes that finite-range limitation.
- Experiment 25 established the sharp **global additive-triple lower bound at the fixed threshold 1/16**, using analytic discrepancy plus exact finite verification. The present result gives a direct symbolic equality witness.

## Scope and novelty
**Solved:** the exact safe-time measure of this particular one-parameter family for every integer q>=5.

**NOT solved:** the sharp minimum over arbitrary additive triples at variable δ; the case of fifteen arbitrary relative speeds; the general 16-runner Lonely Runner Conjecture.

**Originality unverified:** this is an elementary rational-interval overlap calculation and may be implicit in earlier work. Prior art to inspect includes Perarnau–Serra (2016), DOI 10.37236/5123, and general work on runner correlations and safe-time measures. Do not claim a historical breakthrough or journal novelty without a full theorem-level comparison.

## Next experiment
Determine whether (1,q-2,q-1) globally minimizes F_(1/q)(a,b) over all positive a,b, or find a counterexample. The exact formula alone does not prove minimization.
