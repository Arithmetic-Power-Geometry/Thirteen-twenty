# Experiment 93 — Higher-order generalized-CRT intersection theorem

**Date:** 2026-10-10. **Status:** all-dimensional exact formula proved; 3,211 independently executed integer checks passed. The unrestricted Lonely Runner Conjecture is **not solved**.

## Setup

Fix any full speed vector V of k>=2 distinct positive integers, and write q=k+1, L=lcm(V), M=qL. Select any nonempty subset W of s speeds, 1<=s<=k. Put

- ell=lcm(W), d=gcd(W), r=L/ell;
- for v in W, h_v=ell/v and modulus m_v=q*h_v;
- vertex-forbidden residues R_v={0,...,h_v-1} union {(q-1)h_v+1,...,q*h_v-1};
- open-cell-forbidden residues R_c={0,...,h_v-1} union {(q-1)h_v,...,q*h_v-1}.

Define X_W as the number of tuples (x_v) with x_v in R_v for all v in W that satisfy

    x_u = x_v (mod gcd(m_u,m_v)) for all u,v in W.

Define Y_W analogously with R_c instead of R_v. These are finite generalized-CRT compatibility counts.

## Theorem 93.1 — Exact higher-order forbidden-grid intersection

Let T_W be the number of indices j=0,...,qL-1 such that every v in W is strictly forbidden at j/(qL), i.e., ||v*j/(qL)||<1/q. Then

    T_W = d * [ (r-1)*Y_W + X_W ].

This identity holds for every dimension k and every nonempty W. For s=1 it specializes to the forbidden count 2L-v from Experiment 90; for s=2 it extends the pair formula of Experiment 92.

### Proof

The joint phase pattern of W repeats d times on the unit circle, each with period 1/d. Consider one such period on its natural boundary grid of q*ell/d equal cells. The residue condition for v at the grid vertex j/(q*ell) is j mod m_v in R_v. The corresponding open elementary cell is strictly forbidden throughout precisely when j mod m_v lies in R_c; no boundary of any forbidden set lies in the interior of a natural grid cell.

Since gcd of the speeds in W equals d, lcm(m_v:v in W)=q*ell/d. By the generalized Chinese remainder theorem, a tuple of residues is realized by exactly one index modulo q*ell/d if and only if all pairwise gcd compatibility conditions hold. Hence X_W counts jointly forbidden vertices, and Y_W counts jointly forbidden open cells, in one period.

The jointly forbidden set is open. Within one period, every forbidden vertex is incident to two forbidden cells; the set consists of C=Y_W-X_W open components (including the wraparound case). Refining each original cell by the factor r=L/ell adds r-1 interior grid vertices per jointly forbidden cell, while retaining the X_W originally forbidden vertices. Thus the refined grid contains X_W+(r-1)Y_W jointly forbidden vertices per period. Multiplying by d periods proves the formula. QED.

**Implementation detail:** Generalized CRT can merge compatible residues incrementally. The algorithm enumerates compatible residue states rather than all qL grid points. This is exact but can still be exponential in subset size and is NOT claimed universally faster than grid enumeration.

## Corollary 93.2 — Exact higher-order inclusion–exclusion

Let F_v denote the forbidden vertices for speed v on Z/(qL)Z. Then

    G = qL + sum_{nonempty W subset V} (-1)^|W| * T_W,

where G is the number of safe grid vertices. This is an exact integer formula in every dimension, including configurations with isolated safe times. It does not prove G>0 for arbitrary V.

## Independently executed exact tests

The script experiments/experiment_93_higher_order_crt.py was executed with Python integer arithmetic. For all primitive full speed vectors in (k,N)=(3,10),(4,9),(5,8), every pair, triple and quadruple W was checked against direct modular enumeration on the full qL grid. Results:

- Pair intersections: 1,637 passed.
- Triple intersections: 1,169 passed.
- Quadruple intersections: 405 passed.
- Total: **3,211 passed, zero discrepancies**.

Example full-subset counts: W=(1,2,3), q=4, L=6 gives T_W=3, X_W=3, Y_W=4; W=(1,3,4,7), q=5, L=84 gives T_W=23, X_W=23, Y_W=24.

## Literature, novelty and journal gate

This is an exact higher-order generalization of the repository's Experiment 92. Generalized CRT and inclusion–exclusion are classical; no independent novelty or improved asymptotic bound over existing literature has been demonstrated. Compare Malikiosis, Santos and Schymura (2025), *Forum of Mathematics, Sigma*, DOI 10.1017/fms.2025.10107, and Giri and Kravitz (2026), *Mathematical Proceedings of the Cambridge Philosophical Society*, DOI 10.1017/S0305004125101497. Both verified entries already exist in references/lonely_runner.bib.

**Verdict:** all-dimensional exact theorem proved; unrestricted LRC not solved; Q1-level originality/significance not established. A substantive next step would be an arithmetic lower bound on alternating CRT intersection sums that forces G>=1 independently of the actual speeds.
