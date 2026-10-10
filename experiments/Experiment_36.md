# Experiment 36 — All-dimensional Fourier reduction and resonance obstruction

Date: 2026-10-10. **Rigorous all-dimensional identity, not a proof of the Lonely Runner Conjecture.**

## General setup

For an integer speed vector V=(v_1,...,v_k) with each v_i nonzero, and 0<δ<1/2, define

S_δ(V)=∫_0^1 ∏_{i=1}^k 1_{||v_i t||≥δ} dt.

A positive S_δ(V) gives a witness time with all k relative speeds at distance at least δ, except for the technical distinction of boundary-only witnesses. The general LRC at k relative speeds seeks existence at δ=1/(k+1), not a uniform positive-measure lower bound.

## Theorem 36.1: exact all-dimensional Fourier resonance identity

Let f_δ(x)=1_{||x||≥δ} on the circle. Its Fourier coefficients are

c_0=1-2δ,
c_n=-sin(2πnδ)/(πn) for nonzero integer n.

Let σ_N f_δ be the Fejér mean, i.e. the convolution with the Fejér kernel. Then

S_δ(V)
=lim_{N→∞} ∑_{n∈Z^k, |n_i|≤N, Σ_i n_i v_i=0}
  ∏_{i=1}^k (1-|n_i|/(N+1)) c_{n_i}.

**Proof:** Each Fejér mean is a finite trigonometric polynomial, bounded between 0 and 1, and converges pointwise to f_δ except at the two boundary points ±δ modulo 1. Since every v_i is nonzero, their finitely many boundary preimages have measure zero in t. Dominated convergence applies to the product. Expanding the finite product and integrating e^{2πitΣ n_i v_i} over t kills every nonresonant frequency and retains exactly the displayed sum. QED.

The formula is valid for any number k of integer speeds and any additive relations among them. It is not a positivity estimate: the nonzero resonant terms can have either sign. Bounding them sharply enough for the full LRC remains open.

## Rank and dimension caveat

For integer v_i, the orbit t↦(v_1 t,...,v_k t) lies on a **one-dimensional subtorus**, not a k-dimensional equidistributed torus. The relation lattice {n∈Z^k: Σ n_i v_i=0} has rank k−1 for nonzero primitive V. In particular, no argument may replace S_δ(V) with the independent-coordinate product (1−2δ)^k. The Fourier formula makes all integer relations explicit.

## Exact obstruction example

At δ=1/5:
- V=(1,2,3): S=2/15, while independent-coordinate heuristic (3/5)^3=27/125.
- V=(1,2,4): S=1/5, while the same heuristic is 27/125.

Thus two distinct three-speed sets at the same threshold have different safe-time measures; neither equals the naive independent-product prediction. The exact rational endpoint sweep and verification code are in src/experiment_36_fourier.py.

For V=(1,14,15) at δ=1/16, S=13/20, consistent with Experiment 25.

## What has and has not been proved

**Proved:** the Fejér-regularized resonance identity for every finite k and integer speed vector, with no unlicensed interchange of conditionally convergent Fourier sums. Exact obstruction examples. This is standard harmonic-analysis machinery, not claimed as a novel theorem.

**Not proved:** a uniform lower bound at δ=1/(k+1) for every V, a 16-runner theorem, or the variable-q additive-triple minimization formula. Existing positive-measure arguments for additive triples do not extend automatically to arbitrary k.

## Literature / novelty

The nearest primary-source literature remains Perarnau–Serra (2016), *Correlation Among Runners and Some Results on the Lonely Runner Conjecture*, EJC 23(1) P1.50, DOI 10.37236/5123; the full publisher PDF directly studies correlated runner time sets. The Perarnau–Serra 2025 survey covers Fourier and other approaches. Both entries already exist in references/lonely_runner.bib; no duplicate or unverified new entry has been appended. This experiment adds a proof and computational artifact, not a newly sourced paper.
