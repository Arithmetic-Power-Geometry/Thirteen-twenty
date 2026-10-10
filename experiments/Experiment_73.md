# Experiment 73 — Odd-lattice phase alignment across arbitrarily separated speeds

Date: 2026-10-10
Status: proved all-dimensional explicit-witness family. This is elementary and not claimed as original research. Unrestricted LRC unsolved.

## Theorem 73.1 (odd-lattice band)
Let k>=2, q=k+1, and let v_1,...,v_k be distinct positive integer speeds. Suppose there is an integer B>=1 and odd integers o_i such that
|v_i-B*o_i| <= B*(q-2)/q
for every i. Then t=1/(2B) is a simultaneous safe time:
||v_i*t|| >= 1/q for every i.

## Proof
Write v_i=B*o_i+e_i with o_i odd. At t=1/(2B),
v_i*t=o_i/2+e_i/(2B).
Since o_i/2 is a half-integer, its distance to the nearest integer after perturbation is at least 1/2-|e_i|/(2B), by the 1-Lipschitz property of circular distance. By the hypothesis this is at least
1/2-(q-2)/(2q)=1/q.
Thus every runner is safe at the explicit time. QED.

## Corollary 73.2 (unbounded speed ratio, dense short relations)
For any fixed k>=2, any odd positive integers o_1<...<o_k, and any integer B>=1, the exact multiples v_i=B*o_i are safe at t=1/(2B). Taking o_k arbitrarily large makes max(v_i)/min(v_i) unbounded. More generally, integer perturbations e_i satisfying the theorem retain the witness, including perturbations that destroy common gcds.

## Worked example outside Experiment 72
k=5, q=6, B=100, v=(101,299,501,701,899), with odd centers (1,3,5,7,9) times B and errors (1,-1,1,1,-1). Here M/m=899/101>5, so Experiment 72's bounded-ratio criterion fails. The new time t=1/200 gives each nearest-integer distance 99/200 or 1/2, all >=1/6. The speeds satisfy additive relations 101+899=299+701=1000. This is a relation-bearing, high-ratio family.

## Limits
The hypothesis encodes simultaneous near-half-integer phase alignment; it does not follow for arbitrary speed sets. The conclusion is elementary and should not be advertised as a novel solution. This family is distinct from the bounded-ratio construction in Experiment 72 but belongs to the classical fixed-time modular witness paradigm.

## Literature checked
Perarnau, Guillem and Serra, Oriol, *The Lonely Runner Conjecture turns 60*, arXiv:2409.20160 (2024; revised 2025), survey of classical constructions. Beck, Matthias and Everett, Samuel, *Lonely Runner Relations*, arXiv:2609.06259 (2026), confirms that relation-bearing instances are central to the remaining problem. Both already present in references/lonely_runner.bib; no duplicate entries. Source links: https://arxiv.org/abs/2409.20160 and https://arxiv.org/abs/2609.06259.

## Research verdict
All-dimensional family proved; exact constructive witness; not a general solution; independent novelty not established. Future work must derive a witness from arbitrary speeds rather than assume phase alignment.
