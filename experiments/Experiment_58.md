# Experiment 58 — Multi-exception lifting: a rigorous new family, with prior-art boundary

Date: 2026-10-10
Status: proved exact lifting lemma for arbitrary finite dimension; special case of modular-fiber union-bound methods already documented in Experiment 40. No originality claim and NO unrestricted LRC solution.

## Theorem 58.1 (multiple exceptions under a prime shift)
Let k>=2, q=k+1, and p be a prime with p>=2. Partition k distinct positive integer speeds into a stable set A and an exceptional set E of size r. Assume p divides every speed in A, and p divides no speed in E. Assume there exists t0 with ||a*t0||>=1/q for every a in A. Define c=ceil(2*p/q). If r*c<p, then there exists h in {0,...,p-1} such that t=t0+h/p satisfies ||v*t||>=1/q for ALL speeds v in A union E.

## Proof
For each a in A, a*h/p is integral, so the safety of A is invariant under all p shifts. For each b in E, multiplication by b permutes residues modulo p. Thus the p phases b*t0+b*h/p form an equally spaced p-grid on the circle. The forbidden open arc ||x||<1/q has length 2/q, and contains at most ceil(2*p/q) grid points (possibly a conservative bound when endpoints align). Thus each exceptional speed excludes at most c choices of h. The union of all exceptional forbidden sets excludes at most r*c<p shifts. At least one shift remains and is safe for all speeds. QED.

## Corollary 58.2 (unconditional infinite family)
For any k>=3 and prime p>=2, choose k-r distinct speeds in A to be odd multiples of p, and r distinct speeds not divisible by p. If r*ceil(2*p/(k+1))<p, then t0=1/(2*p) makes A safe at distance 1/2, and Theorem 58.1 yields a safe time for all k speeds. This supplies an explicit infinite family in any dimension where the inequality admits r>=1.

## Example
k=6, q=7, p=3, r=2. Then c=ceil(6/7)=1 and r*c=2<3. Choose A=(3,9,15,21), E=(1,2), t0=1/6. The three candidates t0+h/3 are 1/6,1/2,5/6. At t=1/2 the stable odd multiples of 3 are at distance 1/2; speed 1 is at distance 1/2 but speed 2 fails. At t=1/6, speed 1 has distance 1/6>=1/7 and speed 2 has distance 1/3>=1/7, while stable speeds have distance 1/2. Thus t=1/6 is an explicit certificate.

## Limitation and novelty
This is not an unrestricted proof: an arbitrary vector need not contain a p-divisible stable set, and the strict inequality may fail. This exact union-bound fiber mechanism overlaps Experiment 40 and previously published arithmetic shifting methods. Record as an explicit, independently checkable multi-exception specialization, not a Q1 breakthrough.

## Literature
- Perarnau, Guillem and Serra, Oriol (2016), Correlation Among Runners and Some Results on the Lonely Runner Conjecture, Electronic Journal of Combinatorics 23(1), P1.50, DOI 10.37236/5123.
- Beck, Matthias and Everett, Samuel (2026), Lonely Runner Relations, arXiv:2609.06259.
- Blanco, Mónica; Criado, Francisco; Santos, Francisco (2026), Coloopless and cosimple zonotopes, and the Lonely Runner Conjectures, arXiv:2603.24784. Primary arXiv metadata checked 2026-10-10. IMPORTANT: the paper discusses counterexamples to the SHIFTED conjecture and Lonely Vector Property, NOT the classical LRC.

## Research status
General classical LRC remains unsolved. The new result is a restricted lifting certificate. For meaningful novelty, derive a bound that holds for all residue patterns, not merely r*c<p.
