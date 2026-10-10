# Experiment 82 — Fifth-order Bonferroni restores positivity on every lacunary geometric family

Date: 2026-10-10
Status: rigorous all-dimensional theorem for every fixed k>=5; not a proof of unrestricted LRC.

## Definitions
For k distinct positive integer speeds V, let q=k+1, delta=1/q, B_i={t in R/Z: ||v_i t||<delta}, and S_j=sum over all j-element index sets J of mu(intersection_{i in J} B_i). Define C5(V)=1-S1+S2-S3+S4-S5 for k>=5.

## Theorem 82.1 — universal fifth-order lower bound
For every k>=5 and every V, mu({t: ||v_i t||>=1/q for all i})>=C5(V).

Proof: at each t let n be the number of forbidden sets containing t. The odd-order Bonferroni inequality gives 1_{n=0}>=sum_{j=0}^5 (-1)^j binom(n,j). Indeed for n>=1 the right-hand side equals -binom(n-1,5)<=0 (using the standard partial alternating-binomial identity), and for n=0 both sides equal one. Integrating proves the bound. QED.

## Theorem 82.2 — strict positive asymptotic certificate for every k>=5
Fix k>=5 and V_N=(1,N,N^2,...,N^(k-1)), N>=2 integer. Then
lim_{N->infinity} C5(V_N)
= sum_{j=0}^5 (-1)^j binom(k,j) (2/(k+1))^j
= (k-1)(k^4+26k^3-34k^2+166k-15)/(15(k+1)^5)
>0.
Consequently there exists N0(k) such that C5(V_N)>0 for all N>=N0(k).

Proof: For each fixed index set J of size j<=5, the Fourier/Fejer approximation argument proved in Experiment 81 (and repeated in the verification notes) gives asymptotic independence:
mu(intersection_{i in J} B_{N^i}) -> (2/q)^j.
Briefly, approximate the indicator of the arc {||x||<1/q} in L1 by a Fejer polynomial with Fourier support [-M,M], bounded between 0 and 1. For N>M+1, the only frequency relation sum_{i in J} m_i N^i=0 with |m_i|<=M is the trivial one, by reducing modulo N at the least nonzero exponent. Products of bounded approximants telescope with L1 error at most j*epsilon. Taking epsilon to zero proves the joint limit. Summing over the finitely many index sets proves the displayed limit.

To verify the rational simplification, multiply the finite sum by 15(k+1)^5 and expand binomial coefficients; the result factors as (k-1)(k^4+26k^3-34k^2+166k-15). For k>=5 the quartic equals k^4+k^2(26k-34)+(166k-15), a sum of strictly positive terms. Hence the limit is positive. QED.

## Relation to Experiment 81
For every fixed k>=8, Experiment 81 proved the third-order limit C3(V_N)<0. Theorem 82.2 proves C5(V_N)>0 for all sufficiently large N on the SAME speed family. Thus increasing the truncation order from three to five strictly overcomes the earlier certificate obstruction. This does not imply fifth order works for arbitrary speeds.

## Independent explicit witness
For odd N, t=1/2 is safe, since every N^i is odd. For even N, t=N/[2(N+1)] is safe, since N^i is congruent to (-1)^i modulo N+1, so every distance equals N/[2(N+1)] >=1/(k+1). The Bonferroni theorem independently gives a positive-measure safe set for sufficiently large N.

## Computational checks
The exact rational polynomial identity, its sign for k=5,...,200, and the odd-order Bonferroni pointwise inequality for n=0,...,200 are checked in experiments/experiment_82_fifth_order.py. The theorem's asymptotic convergence is proved analytically, not inferred from finite tests. No explicit effective N0(k) is claimed.

## Novelty, references, and verdict
Odd-order Bonferroni inequalities, Fejer approximation and lacunary Fourier decorrelation are classical. The combination is a meaningful improvement over Experiment 81's third-order failure, but first-discovery or Q1-level novelty is not established.
Relevant existing entries in references/lonely_runner.bib: Malikiosis–Santos–Schymura (2025), Forum of Mathematics, Sigma 13 e164, DOI 10.1017/fms.2025.10107; Jensen (2026), arXiv:2605.27941; Beck–Everett (2026), arXiv:2609.06259. No duplicate entries should be appended.
Unrestricted LRC is NOT solved.
