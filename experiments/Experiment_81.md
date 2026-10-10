# Experiment 81 — An all-dimensional third-order barrier on geometric-speed families

Date: 2026-10-10
Status: rigorous asymptotic theorem for every fixed k>=8, plus explicit safe witness. The unrestricted Lonely Runner Conjecture is NOT solved.

## Problem
Experiment 80 used the third-order Bonferroni lower bound
C3(V)=1-2k/q+S2(V)-S3(V), q=k+1,
where S2 and S3 sum the measures of intersections of two and three forbidden sets B_v={t: ||vt||<1/q}. Does the bound become universally positive when speeds are sufficiently separated? No.

## Theorem 81.1 (rigorous all-dimensional obstruction)
For every fixed k>=8, consider the k distinct speeds
V_N=(1,N,N^2,...,N^{k-1}) for integers N>=2.
As N tends to infinity, for every fixed subset J of r distinct indices, r=1,2,3,
measure(intersection_{j in J} B_{N^j}) -> (2/q)^r.
Consequently,
lim_{N->infinity} C3(V_N)
=1-2k/q+binom(k,2)*(2/q)^2-binom(k,3)*(2/q)^3
= -(k-1)*(k^2-8k+3)/(3*(k+1)^3) <0.
Thus for every k>=8 there exists N_0(k) such that for all N>=N_0(k) the third-order certificate is NEGATIVE and cannot certify the existence of a safe time, even though the speed vector is safe.

## Proof of asymptotic independence
Let f(x)=1_{||x||<1/q} on the circle. Fix any subset J={j_1,...,j_r} of distinct nonnegative indices. Approximate f in L1 on the circle by a trigonometric polynomial P_M with bounded frequencies |m|<=M and L1 error <=epsilon; choose P_M as the Fejer mean of f so 0<=P_M<=1. Since each map t -> N^j*t mod 1 preserves Haar measure, telescoping products yields
|integral product_j f(N^{j}t)dt - integral product_j P_M(N^{j}t)dt| <= r*epsilon.
Expand the polynomial product in Fourier modes. Its integral vanishes unless sum_{j in J}m_j*N^j=0. For N>M+1, no nonzero integer coefficient vector with |m_j|<=M can satisfy this: taking the least exponent with nonzero coefficient and reducing the equality modulo N after factoring out its N-power forces that coefficient to be divisible by N, impossible. Hence only the zero-frequency tuple survives, and the polynomial integral equals (integral P_M)^r=(2/q)^r. Let epsilon->0. This proves the joint-intersection limits, and finite sums give the C3 limit.

For k>=8, k^2-8k+3>0, so the limiting C3 is strictly negative.

## Explicit safe witness for the very same family
If N is odd, choose t=1/2: all N^j*t are half-integers, and every circular distance equals 1/2.
If N is even, choose t=(N/2)/(N+1). Since N ≡ -1 (mod N+1), N^j*t mod 1 is ±(N/2)/(N+1); its nearest-integer distance equals N/[2(N+1)] >=1/q for k>=2 and N>=2. Thus every V_N is explicitly safe, independently of the Bonferroni certificate.

## Exact benchmarks
For k=7, the independent-limit third-order lower bound is 1/64 >0.
For k=8, it is -7/729 <0.
For k=9, it is -4/125 <0.
The sign changes at k=8 and stays negative thereafter.

## Significance and limitations
This is a dimension-uniform, rigorous asymptotic obstruction to the SPECIFIC third-order certificate of Experiment 80, not to the conjecture. It shows that merely improving numerical evaluation of S2 and S3 cannot yield a universal all-dimensional proof. Unlike Experiment 79, which concerned pairwise spanning trees, this addresses the complete third-order inclusion-exclusion truncation. The underlying Fourier mixing and Bonferroni algebra are classical; independent research novelty is NOT established.

## Literature and bibliography
- Terence Tao (2018), Some remarks on the lonely runner conjecture, Contributions to Discrete Mathematics 13(2), DOI 10.55016/ojs/cdm.v13i2.62728.
- Romanos Diogenes Malikiosis, Francisco Santos and Matthias Schymura (2025), Linearly-exponential checking is enough for the Lonely Runner Conjecture and some of its variants, Forum of Mathematics, Sigma 13, e164, arXiv:2411.06903.
- Alathea Jensen (2026), Mixed thresholds in the Lonely Runner Conjecture, arXiv:2605.27941.
All are present in references/lonely_runner.bib; no duplicates. Check the precise published article metadata against the publisher before manuscript submission.

## Research verdict
Proved a theorem for ALL k>=8 and an infinite family for each k, with a complete explicit safe witness. The LRC remains open in unrestricted dimension. This is a rigorous diagnostic result, not a solution or independently novel Q1 breakthrough.
