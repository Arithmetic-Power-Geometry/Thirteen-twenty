# Experiment 79 — A no-go theorem for the pair-overlap spanning-tree strategy

Date: 2026-10-10
Status: complete all-dimensional analytic theorem for k>=4; identifies an infinite class where the Experiment 70/78 certificate MUST fail. It does not imply the Lonely Runner Conjecture fails.

## Setup
Let k>=4, q=k+1, delta=1/q, and distinct positive integer speeds v_1,...,v_k. Let B_i={t mod 1: ||v_i*t||<delta}, w_ij=measure(B_i intersection B_j), and W=max over spanning trees T of sum_{ij in T}w_ij. Experiment 70 gives measure(safe times)>=1-2k/q+W, hence certifies positive safe measure only if W>(k-1)/q.

Write g_ij=gcd(v_i,v_j), A_ij=v_i/g_ij, C_ij=v_j/g_ij, and P_ij=A_ij*C_ij.

## Theorem 79.1: uniform discrepancy and no-go
For every pair,
|w_ij-4/q^2|<=1/(4 P_ij).
Consequently, if P_ij>q^2/[4(q-4)] for EVERY distinct pair, then
W<(k-1)/q.
In particular the spanning-tree sufficient condition W>(k-1)/q cannot hold. This is an intrinsic limitation of that specific method, not a counterexample to LRC.

## Proof
By Experiment 78, w_ij=4/q^2+[B2({(A_ij-C_ij)/q})-B2({(A_ij+C_ij)/q})]/P_ij, where B2(x)=x^2-x+1/6 on [0,1]. Since B2 has minimum -1/12 and maximum 1/6, the difference of two values is bounded in absolute value by 1/4. Thus |w_ij-4/q^2|<=1/(4P_ij).

If every P_ij>q^2/[4(q-4)], then 1/(4P_ij)<(q-4)/q^2 and
w_ij<4/q^2+(q-4)/q^2=1/q.
Every spanning tree has exactly k-1 edges; summing gives W<(k-1)/q. QED.

## Corollary 79.2: infinite families in every dimension k>=4
Choose k distinct primes all larger than q (or any pairwise-coprime positive integers with each pair product exceeding q^2/[4(q-4)]). Then P_ij=v_i*v_j and the no-go hypothesis holds. Such sets exist with arbitrarily large speeds in every dimension k>=4.

Example k=4, q=5, speeds (11,13,17,19). All reduced pair products >=143>25/4, so the tree method cannot certify positive measure for this vector, regardless of the exact edge weights. This says NOTHING negative about actual safe times.

## Research significance
This theorem diagnoses why iterating the pairwise-overlap maximum-spanning-tree approach is a dead end for generic large coprime speed sets. The discrepancy bound and no-go inequality are exact, dimension-uniform and independently reproducible. Their mathematical novelty relative to standard Bernoulli/Fourier bounds is not established. The strategic conclusion is to develop genuinely higher-order or signed-correlation methods, or leverage the short-relation structure of Beck–Everett (2026), rather than repeatedly optimizing pairwise trees.

## Literature
Jensen, Alathea (2026), Mixed thresholds in the Lonely Runner Conjecture, arXiv:2605.27941, Fourier two-function integral.
Beck, Matthias and Everett, Samuel (2026), Lonely Runner Relations, arXiv:2609.06259, short-relation structure.
Both references already exist in references/lonely_runner.bib; no duplicate BibTeX entries were added.

## Verdict
Complete all-dimensional NO-GO theorem for a particular proof method, not a universal LRC theorem. No unrestricted LRC solution; independent priority unverified.
