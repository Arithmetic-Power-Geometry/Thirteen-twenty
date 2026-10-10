# Experiment 95 — Exact event sweep for safe-set topology and grid counts

**Date:** 2026-10-10. **Status:** rigorous all-dimensional algorithm and exact verification. **Unrestricted LRC remains unsolved.**

## Theorem 95.1 — Exact boundary-event decomposition

For any k>=2 distinct positive integer speeds V, let q=k+1, L=lcm(V), M=qL and S={t mod 1: ||vt||>=1/q for all v in V}. Define

B={0,1} union {(qn+1)/(qv), (qn+q-1)/(qv): v in V, 0<=n<v}.

Let 0=e_0<e_1<...<e_m=1 be the sorted distinct members of B, so m<=2 sum(V)+1. Let a_i indicate that e_i is safe, and let c_i indicate that the midpoint (e_i+e_{i+1})/2 is safe, for 0<=i<m. Interpret c_{-1}=c_{m-1}.

Then all the following are **exact**:

1. The entire open interval (e_i,e_{i+1}) is safe if c_i=1, and contains no safe point if c_i=0.
2. The number of safe elementary M-grid cells is
   H=sum_{i:c_i=1} M(e_{i+1}-e_i).
3. The number of connected components, including isolated points, is
   C=sum_{i=0}^{m-1} a_i(1-c_{i-1}).
4. The number of safe M-grid vertices is G=H+C.
5. S is nonempty iff some a_i=1, and the first such e_i is an exact rational witness.

This algorithm uses at most 2 sum(V)+2 rational event values, sorts them, and tests at most twice as many event points and midpoints. It uses O(k sum(V)+sum(V)log(sum(V))) rational comparisons and arithmetic operations, ignoring integer bit-complexity. Its runtime depends on the sum of speeds, not directly on the potentially enormous M=q*lcm(V).

## Proof

For a speed v, the boundary of the forbidden open set {t:||vt||<1/q} consists exactly of the points (qn+1)/(qv) and (qn+q-1)/(qv), 0<=n<v, on [0,1). Every safety indicator is constant on every connected component of [0,1] minus B, proving item 1.

Every event is on the M-grid, since v divides L. A safe event interval contains exactly M(e_{i+1}-e_i) consecutive safe elementary grid cells, giving item 2. Because S is closed and 0 is unsafe, each connected component of S has a unique first safe event vertex after an unsafe preceding event interval. Counting these starts gives item 3; this also counts isolated safe event vertices correctly. The exact cell-complex identity G=H+C was proved in Experiment 90, giving item 4. If S is nonempty, since S is closed and proper, it has a boundary point that belongs to S; every such boundary point is in B. Conversely, a safe event is itself a witness, proving item 5. QED.

## Executed exact audit

The committed program experiments/experiment_95_event_sweep.py was independently run using Python Fraction arithmetic and an integer-only full-grid comparator. It checked all 244 primitive vectors in the ranges (k,N)=(2,12):45, (3,10):109, (4,8):69, (5,7):21. The computed triples (G,H,C) matched exactly in every case.

A larger instance V=(101,103,107,109,113) has M=82,261,868,142 grid vertices but only 1,059 event intervals. The sweep returned G=11,732,278,703; H=11,732,278,616; C=87; witness t=1/606. This large instance was checked internally by exact arithmetic and structural invariants, not by full-grid enumeration (which would require scanning over 82 billion points).

The tight vector V=(1,3,4,7) gave (G,H,C)=(4,0,4) and witness t=1/5, confirming detection of isolated safe points.

## Comparison and novelty limits

This packages the finite boundary principle from the repository's Experiments 74, 84 and 90 into a complete exact algorithm for measure, topology and grid counts. Boundary sweeps and rational interval arrangements are classical. The procedure is **not** a dimension-only finite reduction, does not outperform the general finite-checking bound of Malikiosis–Santos–Schymura (2025), and is not independently established as mathematically novel. The result could support a reproducibility/software methods component but is **not sufficient by itself** for a Q1-level original mathematical paper.

Relevant existing primary literature: Tao (2018), DOI 10.55016/ojs/cdm.v13i2.62728; Malikiosis–Santos–Schymura (2025), DOI 10.1017/fms.2025.10107; Beck–Everett (2026), arXiv:2609.06259. All three were already present in references/lonely_runner.bib; no duplicate entries were appended.

**Verdict:** exact all-dimensional algorithm proved; 244 independent small-grid comparisons passed; unrestricted LRC **NOT SOLVED**; Q1-level independent novelty **NOT ESTABLISHED**.
