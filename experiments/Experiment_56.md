# Experiment 56 — Modular arithmetic witness and its exact limitation

Date: 2026-10-10
Status: elementary proved infinite-family result in all finite dimensions. Not novel; does NOT solve unrestricted LRC.

## Theorem 56.1
Let k>=2 and q=k+1. For any k distinct positive integer speeds v_1,...,v_k with q not dividing any v_i, the time t=1/q satisfies ||v_i*t||>=1/q simultaneously.

## Proof
Each v_i has a nonzero residue r_i in {1,...,q-1} modulo q. Thus ||v_i/q||=min(r_i,q-r_i)/q>=1/q. QED.

## Stronger arithmetic witness family
For any integer j, if for every i the residue (j*v_i mod q) lies in {1,...,q-1}, then t=j/q is safe. In particular, if gcd(j,q)=1, this is equivalent to no v_i divisible by q, so varying j among units does not fix any q-divisible speed.

## Obstruction
If q divides some v_i, then every time t=j/q fails for that speed, since v_i*j/q is an integer. Therefore the entire denominator-q witness family cannot handle such a vector, even though LRC may still hold. This is an obstruction to the certificate, not a counterexample to LRC.

## Example
For k=3, q=4, speeds (1,2,3), t=1/4 works. Speeds (1,2,4) include a multiple of 4; all j/4 fail for speed 4, but t=1/3 works: distances are 1/3, 1/3, 1/3, exceeding the LRC threshold 1/4.

## Next gate
Search for a nontrivial universal combination of denominators or an arithmetic obstruction theorem that goes beyond finite testing. Any claimed universal proof must cover vectors with multiples of q and all tight configurations.

## Literature and novelty
This modular witness is elementary and overlaps Experiment 38. Do NOT claim new novelty. Relevant primary literature: Perarnau and Serra (2025), The Lonely Runner Conjecture turns 60, Computer Science Review 58, 100798, DOI 10.1016/j.cosrev.2025.100798; Malikiosis, Santos and Schymura (2025), Linearly-exponential checking is enough for the lonely runner conjecture and some of its variants, Forum of Mathematics, Sigma 13, e164, DOI 10.1017/fms.2025.10107; Beck and Everett (2026), Lonely Runner Relations, arXiv:2609.06259. Check existing references/lonely_runner.bib before appending duplicates.

## Verdict
An infinite family in every dimension is proved. The general LRC remains unsolved. Q1 novelty of this theorem alone: none.
