# Experiment 57 — One-exception modular lifting theorem

Date: 2026-10-10
Status: rigorous arbitrary-dimensional conditional lifting theorem, with an explicit infinite family. Does NOT prove unrestricted Lonely Runner Conjecture. Novelty unverified; related shifting methods already known.

## Theorem 57.1 (one exceptional speed)
Let k>=2, q=k+1, and let v_1,...,v_k be distinct positive integers. Suppose there is an integer m>=2 dividing v_1,...,v_{k-1}, while gcd(v_k,m)=1. Suppose there exists t0 such that ||v_i*t0||>=1/q for i<k. Then some h in {0,...,m-1} makes t=t0+h/m safe for all k speeds.

## Proof
For i<k, m divides v_i, hence v_i(t0+h/m) differs from v_i*t0 by an integer, preserving the distance to the nearest integer. For the exceptional speed, gcd(v_k,m)=1 means the m fractional phases v_k*t0+h*v_k/m, h=0,...,m-1, form a translate of the uniform m-point grid on the circle. One such point has distance to the nearest integer at least floor(m/2)/m (the farthest grid point from 0). For m>=2, floor(m/2)/m>=1/3. Since q=k+1>=3, 1/3>=1/q. Thus a shift h makes the exceptional speed safe without affecting the others. QED.

## Corollary 57.2 (unconditional infinite family in every k)
If v_1,...,v_{k-1} are distinct odd multiples of m, with m>=2, and gcd(v_k,m)=1, then t0=1/(2*m) gives ||v_i*t0||=1/2 for i<k. The theorem supplies a simultaneous safe time for all k speeds.

## Example
For k=4, m=5, V=(5,15,25,2), take t0=1/10. The first three runners are at half-integer positions. The exceptional runner can be made safe by some shift h/5; h=1 yields t=3/10, with ||2t||=2/5 and the other three at 1/2.

## Why this is not the full conjecture
The hypotheses require a common divisor for k-1 speeds and coprimality of the exception. General speed vectors need not have this structure. The conditional assumption that the divisible group already has a safe t0 also cannot be asserted for arbitrary k without solving an instance of LRC. The unconditional corollary covers only a restricted infinite family.

## Literature and priority
The shifting mechanism is elementary and resembles established shifting arguments; do not claim originality without theorem-level comparison. Relevant primary sources:
- Matthias Beck and Samuel Everett (2026), Lonely Runner Relations, arXiv:2609.06259, https://arxiv.org/abs/2609.06259 (verified primary arXiv abstract; relation-hyperplane theorem).
- Matthias Beck, Serkan Hosten, and Matthias Schymura (2016), Lonely Runner Polyhedra, arXiv:1606.01783, https://arxiv.org/abs/1606.01783 (verified primary arXiv abstract; polyhedral and parity families).
- Perarnau and Serra (2016), Correlation Among Runners and Some Results on the Lonely Runner Conjecture, Electronic Journal of Combinatorics 23(1), P1.50, DOI 10.37236/5123.

## Novelty verdict
Valid proof and infinite family in every k, but no established new Q1 theorem; the general LRC remains open.
