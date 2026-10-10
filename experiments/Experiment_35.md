# Experiment 35 — Sharp global additive-triple safe-time measure at q=20

Date: 2026-10-10. Status: fixed-q computer-assisted theorem, not a uniform q theorem.

For positive integers a,b, F_(1/20)(a,b) is the Lebesgue measure of times t in [0,1] with ||at||,||bt||,||(a+b)t||>=1/20.

**Theorem:** F_(1/20)(a,b) >= (20-3)(20-4)/(20*19) = 68/95.

The bound is attained by (a,b)=(1,18), and by its swaps and common integer multiples. Among normalized coprime pairs with a<=b, equality is unique.

## Proof (analytic infinite-to-finite reduction + exact certificate)

Scaling reduces to coprime a,b and symmetry to a<=b. The established discrepancy estimate yields
F_(1/q)(a,b) >= (1-3/q)^2 - 2/b.

The gap from the mean to the claimed sharp bound is 3(q-3)/(q²(q-1)), hence all b>=B_q:=ceil(2q²(q-1)/(3(q-3))) satisfy the claim. At q=20, B_20=299.

The remaining 1<=a<=b<299, gcd(a,b)=1, were checked using exact integer interval endpoints and midpoint predicates. Result: 27,054 normalized pairs; zero violations; unique equality (1,18). Data: data/experiment_35_results.csv. Independent Python reimplementation: src/experiment_35_verify.py. The primary run used a separate JS exact integer implementation. For each candidate interval, endpoint D=q*a*b*(a+b) and integer cross-multiplication avoid floating-point uncertainty.

## All-dimensions attempt and barrier

The universal q conjecture F_(1/q)(a,b)>=(q-3)(q-4)/(q(q-1)) for every q>=5 remains open. Its finite cutoff is B_q=Theta(q²); the number of coprime candidate pairs is Theta(q^4), so proving one q at a time does not yield a proof for all q. A higher-dimensional torus/Fourier or additive-combinatorial argument might provide a uniform bound, but has NOT yet done so.

For k unrelated relative speeds, the appropriate torus has rank up to k; the special additive relation c=a+b forces a rank-two torus. The rank-two measure proof cannot simply be lifted to sixteen runners. No high-dimensional LRC theorem is asserted.

## Literature and novelty
Bohman–Holzman–Kleitman (2001), *Six Lonely Runners*, The Electronic Journal of Combinatorics 8(2), R3, DOI 10.37236/1602, is newly added to references/lonely_runner.bib with publisher-verified metadata. Its covering-set formulation underscores that time-interval geometry is classical. The direct closest-prior-art risk remains Perarnau–Serra (2016) on runner correlations, and their 2025 survey. No originality or full Lonely Runner Conjecture solution is claimed.
