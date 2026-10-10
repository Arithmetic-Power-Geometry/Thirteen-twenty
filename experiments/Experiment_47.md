# Experiment 47 — Exact global loneliness optimum from a finite critical-time set

Date: 2026-10-10. Status: proved and independently checked exact optimization theorem, not an unrestricted LRC proof.

## Theorem 47.1 — Critical-time exact maximum in every finite integer dimension

For positive integer speeds V=(v_1,...,v_k), define

f_V(t)=min_i ||v_i t||, t∈[0,1].

Let C(V) contain 0, 1, all single-speed corner times j/(2v_i)∈[0,1], and all pairwise crossing times j/(v_i+v_l) and j/|v_i−v_l| in [0,1] (the latter only for unequal speeds). Then

max_{t∈[0,1]} f_V(t) = max_{t∈C(V)} f_V(t).

This computes the **exact optimum**, not just existence at the conjectured threshold. The result applies to every finite number of positive integer relative speeds.

### Proof

Each individual g_i(t)=||v_i t|| is continuous, piecewise affine, with all corners at t=j/(2v_i). On an open interval containing no single-speed corner, all g_i are affine, each with slope +v_i or −v_i. The pointwise minimum f_V is also piecewise affine. Any interior change in its active affine branch must occur at equality g_i(t)=g_l(t). Writing each affine branch as ±v_i t+n_i with n_i integer, equality implies (v_i±v_l)t is an integer. Thus every breakpoint of f_V belongs to C(V). Between consecutive points of C(V), f_V is affine, hence attains its maximum on that closed cell at an endpoint. Taking the maximum over all cells proves the identity. QED.

An upper bound on candidate count before deduplication is 2+Σ_i(2v_i+1)+Σ_{i<l}[(v_i+v_l+1)+(|v_i−v_l|+1)] = O(k² max_i v_i). Thus the algorithm is pseudopolynomial, not polynomial in binary input length.

### Why this is different from Experiment 43

Experiment 43 only tests safety at a fixed threshold 1/(k+1), and Experiment 46 classifies the measure of the threshold-safe set. Experiment 47 computes the **maximum achievable minimum separation exactly**, enabling a rational certificate of whether an instance is strict, tight, or a counterexample, including the margin above/below 1/(k+1).

### Independent validation

The executable uses exact Python fractions and cross-checks against a second algorithm that partitions at all single-runner corners and solves every pairwise affine crossing inside each cell. Every subset of {1,...,8} with k=2,3,4 was tested (28+56+70=154 cases), with zero discrepancies.

Examples:
- (1,3,4,7): optimum 1/5, tight, witness 4/5.
- (1,3,4,5,9): optimum 1/6, tight, witness 5/6.
- (1,2,4,8): optimum 1/3, strictly above 1/5, witness 2/3.

The example tight configurations are known in the literature and are not new discoveries.

## Literature and novelty

The critical-time principle is classical/folklore: Lemma 11 of *Amending the Lonely Runner Spectrum Conjecture*, Electronic Journal of Combinatorics 33(1) (2026), P1.38, states a sharper local-maximizer characterization involving j/(v_i+v_l). Thus no originality is claimed for the critical-point idea. The cited 2026 paper is verified through the journal's primary published PDF; it is newly added to the BibTeX library after checking the author metadata.

Related one-entry tight-instance classifications are given by Yuhan Zhang, *Tight instances of the Lonely Runner Conjecture: complete classification of one-entry modifications, a new infinite family, and the growth bound*, arXiv:2608.13599v2 (2026). This preprint was already in the existing library under Zhang2026 and is not duplicated.

## What remains unsolved

The theorem is an exact optimization algorithm for any fixed integer-speed vector, but does not establish max_t f_V(t)>=1/(k+1) for **all** V. The universal LRC is not solved. A successful next step must derive a structural lower bound for the critical-time maximum uniform over all V, not just enumerate C(V).
