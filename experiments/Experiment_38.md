# Experiment 38 — A dimension-independent modular certificate and exact residue density

Date: 2026-10-10.

## Theorem 38.1 (explicit all-dimensional witness)

Let q>=2 be an integer and let v_1,...,v_k be positive integer speeds, for arbitrary finite k. If **q does not divide any v_i**, then t=1/q satisfies

||v_i t|| >= 1/q for every i.

**Proof.** The residue r_i=v_i mod q belongs to {1,...,q-1}. Hence ||v_i/q||=min(r_i,q-r_i)/q >=1/q. QED.

In the Lonely Runner Conjecture with k relative speeds, set q=k+1. Thus every speed vector having no speed divisible by k+1 is an explicit solved subclass, in **every dimension**, including k=15 (sixteen total runners).

## Corollary 38.2 (exact density of the certificate class)

Among the q^k residue vectors in (Z/qZ)^k, exactly (q-1)^k satisfy the sufficient condition. Thus the proportion is ((q-1)/q)^k. For q=k+1, this tends to e^(-1) as k→infinity.

This is an exact **residue-vector counting** statement. It is NOT a density theorem about all distinct primitive integer speed vectors under arbitrary arithmetic distributions, and is NOT the fraction of LRC cases that have a witness (other cases may also have witnesses).

## Verification

The standalone exact rational script `src/experiment_38_residue.py` was executed in Python 3. It independently enumerated all q^k residue vectors for k=1,...,5 and checked the formula, then evaluated the formula for k=6,7,8. Two fifteen-speed examples at q=16 were checked with exact fractions:
- V=(1,2,...,15), witness t=1/16.
- V=(1,3,...,29), witness t=1/16.

A vector containing a multiple of 16 is **outside this sufficient-condition theorem**, not a counterexample to the Lonely Runner Conjecture. The program returns None for that certificate without declaring the instance unsolvable.

## Exact output

k,q,certified_residue_vectors,total_residue_vectors,density
1,2,1,2,1/2
2,3,4,9,4/9
3,4,27,64,27/64
4,5,256,625,256/625
5,6,3125,7776,3125/7776
6,7,46656,117649,46656/117649
7,8,823543,2097152,823543/2097152
8,9,16777216,43046721,16777216/43046721

## Relationship to Experiment 37 and open obstruction

Experiment 37 gives an exact finite-grid equivalence for every integer speed vector. The present theorem supplies a closed-form feasible grid point for a large explicit subclass. It does not establish a witness when any speed is divisible by q, nor does it solve general LRC. The condition is elementary, likely known implicitly, and no historical originality is asserted.

## Literature, verified primary publisher metadata

Beck and Schymura, *Deep Lattice Points in Zonotopes, Lonely Runners, and Lonely Rabbits*, International Mathematics Research Notices 2024(8), 6553–6578, DOI 10.1093/imrn/rnad232, discusses a proved discrete analogue and geometric reformulation of LRC. Metadata checked against Oxford Academic and appended to `references/lonely_runner.bib`. Tao (2018), Malikiosis–Santos–Schymura (2025), and Giri–Kravitz remain directly relevant and are already in the bibliography.

## Next challenge

Find a modular witness with a different denominator when some v_i are multiples of k+1; prove an all-vector existence theorem without assuming favorable residues. The current result proves a proper subclass only.
