# Experiment 37 — Exact finite-grid equivalence in every dimension

Date: 2026-10-10. **Proved exact all-dimensional reduction; not a solution of the unrestricted Lonely Runner Conjecture.**

## Theorem 37.1 (finite-grid equivalence)

Let q>=2 be an integer and V=(v_1,...,v_k) a nonempty vector of positive integer speeds. Set L=lcm(v_1,...,v_k) and M=2qL. Then the following are equivalent:

1. There exists a real t with ||v_i t||>=1/q for every i.
2. There exists an integer j in {0,1,...,M} with ||v_i j/M||>=1/q for every i.
3. There exists an integer j in {0,1,...,M} such that, for all i,
   q*min((v_i*j) mod M, M-((v_i*j) mod M))>=M.

**Proof.** Reduce time modulo 1. For each speed v_i, the boundary of the forbidden set ||v_i t||<1/q occurs at t=(qm±1)/(qv_i) modulo 1. Since v_i divides L, each boundary belongs to the grid (1/(qL))Z/Z. Thus the truth value of each safe predicate is constant on every open grid cell (r/(qL),(r+1)/(qL)). If a simultaneous witness lies on a grid boundary, it belongs to the candidate set with even index j=2r. If it lies inside a grid cell, its midpoint (2r+1)/(2qL) has the same truth values and belongs to the candidate set with odd index j=2r+1. Conversely any listed grid point is a real time. The modular integer criterion is exactly the circle-distance inequality after multiplication by M. QED.

**Important:** Boundary points are included, so this equivalence also captures witnesses of zero safe-time measure. Merely checking interval midpoints would be insufficient for the closed inequality in the LRC.

## Computational check

Executed `python /tmp/experiment37.py` with exact modular arithmetic and fractions:
- q=4, speeds (1,2,3), L=6: witness 1/4.
- q=5, speeds (1,2,3), L=6: witness 1/5.
- q=16, speeds (1,14,15), L=210: witness 1/16.
- q=6, speeds (1,2,3,4,5), L=60: witness 1/6.

Reproducible file: `src/experiment_37_grid.py`. The theorem itself is established analytically; the examples test implementation only.

## Arbitrary dimension and limitation

For k relative speeds the LRC threshold is q=k+1. This gives an exact finite criterion even for k=15 (sixteen runners). It does **not** show that a candidate j necessarily exists. The grid has 2(k+1)lcm(v_i)+1 points and may be impractically large. Unlike the additive-triple estimates, it yields no uniform positive lower bound on the safe-time measure.

## Literature audit and originality

Tao (2018), *Some remarks on the lonely runner conjecture*, explicitly proves a finite **speed bound** sufficient for the conjecture. Malikiosis–Santos–Schymura (2025), *Linearly exponential checking is enough for the lonely runner conjecture and some of its variants*, greatly improves this speed reduction. Their results are different from the elementary finite **time grid for a fixed speed vector** proved here. Both are already in `references/lonely_runner.bib`; do not duplicate entries. This grid lemma is elementary and **not claimed to be historically novel**.

## Open problem

Prove that the finite modular feasibility system in condition 3 always has a solution at q=k+1 for distinct positive speeds, or identify a rigorous counterexample. No such result follows from Experiment 37.
