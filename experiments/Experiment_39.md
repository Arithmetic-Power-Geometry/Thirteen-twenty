# Experiment 39 — Universal bounded-speed-ratio theorem in every dimension

Date: 2026-10-10.

## Theorem 39.1 (all dimensions, including arbitrary positive real speeds)

Let k>=1, and let 0<v_1<...<v_k be distinct positive **real** relative speeds. If v_k/v_1<=k, then

t=k/((k+1)v_k)

satisfies ||v_i t||>=1/(k+1) for all i=1,...,k.

**Proof.** From v_i>=v_1>=v_k/k we have
v_i*t >= (v_k/k)*k/((k+1)v_k)=1/(k+1).
Also v_i<=v_k gives
v_i*t<=k/(k+1)=1-1/(k+1).
Hence the fractional part of every v_i*t lies in [1/(k+1),1-1/(k+1)], so its distance to the nearest integer is >=1/(k+1). QED.

The theorem also holds without distinctness, but LRC usually takes distinct nonzero relative speeds. This is a *sufficient condition*, not a full proof of LRC.

## Strength beyond Experiment 38

Experiment 38 required integer speeds all nonzero modulo k+1. Experiment 39 works for arbitrary real speeds, even if some speeds are multiples of k+1. For example k=5, V=(3,6,9,12,15) has v_max/v_min=5 and explicit witness t=1/18. For k=15, V=(16,17,...,30) satisfies v_max/v_min=30/16<15 and t=15/(16*30)=1/32.

This proof works in all dimensions because it relies on a shared interval for the rescaled speed coordinates, not on independence or higher-dimensional equidistribution.

## Sharpness of this certificate construction

For the *particular witness* t=k/((k+1)v_max), the condition v_min>=v_max/k is exactly what guarantees that all v_i*t lie in [1/(k+1),k/(k+1)]. If the ratio exceeds k, this witness may fail, but a different witness may exist. The theorem is not claimed to characterize all feasible configurations.

## Verification

The independent exact rational Python script `src/experiment_39_spread.py` exhaustively checks all distinct k-speed subsets of {1,...,12} for k=2,...,6 and tests every returned certificate with rational arithmetic. It also checks three examples and one out-of-class example. The proof is analytic and does not rely on these computations.

## Relation to prior literature / novelty

A published 2025 survey by Perarnau and Serra, *The Lonely Runner Conjecture turns 60*, Computer Science Review 58, 100798, DOI 10.1016/j.cosrev.2025.100798, and Tao's 2018 paper already document elementary reductions and broad LRC context. A 2026 publicly available manuscript also explicitly states a bounded-ratio witness theorem of this form; accordingly **the bounded-ratio lemma is not claimed to be new**. The 2025 survey and Tao are already in `references/lonely_runner.bib`; no duplicate or unverified new literature is appended. The manuscript's identity and peer-review status are not verified and it is not added to the bibliography.

## What remains unsolved

The unbounded-ratio cases v_max/v_min>k, for arbitrary k, are not covered. The general sixteen-runner Lonely Runner Conjecture remains unsolved by this project. A proof for the full conjecture must handle arbitrarily large speed ratios or use an independent finite-speed reduction plus exhaustive verified certification.
