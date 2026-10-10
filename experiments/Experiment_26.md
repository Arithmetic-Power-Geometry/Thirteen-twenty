# Experiment 26 — Variable-threshold additive-triple safe times

**Status:** A valid parameterized torus-average and grid-discrepancy result, but no verified novel breakthrough.

For 0<δ≤1/4, define F_δ(a,b)=μ{t∈[0,1]: ||at||,||bt||,||(a+b)t||≥δ}.

## Theorem
For all positive coprime integers a,b,

|F_δ(a,b)−(1−3δ)²| ≤ 2/max(a,b).

For arbitrary positive a,b, divide a,b by gcd(a,b) first.

**Proof.** Let Aδ={x modulo 1: ||x||≥δ}. The integral of 1_Aδ(x)1_Aδ(y)1_Aδ(x+y) over the two-torus is 1−6δ+9δ²: forbidden singles have area 2δ, pairwise intersections 4δ², and triple overlap 3δ² for δ≤1/4. For coprime a,b, subdivide t=(k+x)/b. For each x, the first coordinate over k=0,…,b−1 is a rotated b-point uniform grid. The allowed first-coordinate set is the intersection of two circle arcs, hence at most two connected arcs. Circular interval grid discrepancy is ≤1/b per connected component. Average over x, then exchange a and b to get the asserted bound.

## Consequences
At δ=1/16, the torus mean is 169/256; the previous sharp inequality F≥13/20 is certified by this discrepancy bound for max(a,b)≥197 and exact finite-case verification for smaller coprime pairs (Experiment 25).

For δ variable, a sharp formula for inf_{a,b} F_δ(a,b) is **not** yet established. In particular, an observed minimizer in a bounded computation must not be stated as universal.

## Novelty audit
- Elementary torus-area and cyclic-grid-discrepancy techniques, not independently verified as original.
- Compare Perarnau–Serra (2016), *Correlation among runners and some results on the Lonely Runner Conjecture*, DOI 10.37236/5123.
- Independently check the exact constant, scope, and closest earlier bounds before preparing a journal paper.

## What is not solved
This does **not** establish the existence of a simultaneous safe time for fifteen arbitrary relative speeds. It does not solve the sixteen-runner Lonely Runner Conjecture, even for the subclass with an additive triple plus twelve arbitrary other speeds.
