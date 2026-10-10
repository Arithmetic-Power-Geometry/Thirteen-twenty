# Experiment 78 — Exact Fourier–Bernoulli pair-overlap formula

Date: 2026-10-10
Status: complete all-dimensional identity; 630 exact regression cases independently checked. No unrestricted LRC proof. Priority caution: Jensen (2026) gives an exact two-function integral formula.

## Theorem 78.1
For positive integers a,b and integer q>=3, let d=1/q and B_v={t in R/Z: ||v*t||<d}. Set g=gcd(a,b), A=a/g, B=b/g. Write P2(x)={x}^2-{x}+1/6, the second periodic Bernoulli polynomial. Then

mu(B_a intersection B_b) =
4*d^2 + [P2(d*(A-B))-P2(d*(A+B))]/(A*B).

This identity holds for arbitrary positive speeds and thresholds 0<d<1/2, not only d=1/q.

## Proof
Let f_d(x)=1 when ||x||<d, and 0 otherwise. Its Fourier coefficients are c_0=2d and c_n=sin(2*pi*n*d)/(pi*n) for nonzero integers n. The functions f_d(a*t) and f_d(b*t) have nonzero Fourier coefficients at multiples of a and b, respectively. By Parseval (or L2 approximation), their integral product is
4d^2+2*sum_{l>=1}sin(2*pi*B*l*d)*sin(2*pi*A*l*d)/(pi^2*A*B*l^2).
Use 2*sin(x)*sin(y)=cos(x-y)-cos(x+y) and the classical absolutely convergent Fourier identity
sum_{l>=1}cos(2*pi*l*x)/l^2=pi^2*P2(x).
Substitution gives the stated expression. Endpoint choices of forbidden arcs do not affect the integral. QED.

## Computational consequence
The pair overlap depends only on the reduced ratio A:B, not on the common factor g. The formula uses gcd and exact rational arithmetic; no interval enumeration proportional to max(a,b) is required. Combined with Experiment 70, a maximum spanning tree over the exact weights gives
mu(S)>=1-2k/(k+1)+W.
The resulting sufficient condition W>(k-1)/(k+1) certifies a positive-measure safe set. Failure of this inequality is inconclusive.

## Independent reproducibility audit
Program: experiments/experiment_78_fourier_overlap.py
Two independent calculations were compared for q=3,...,8 and every 1<=a<b<=15: 6*binom(15,2)=630 cases. The formula matched exact Fraction interval sweeps in all 630 cases, with zero discrepancies. Example weights:
- q=4, speeds (1,2,3): w12=1/4, w13=1/6, w23=1/4. Maximum tree weight 1/2 equals the threshold 1/2, so strict positivity is not certified (indeed this tight set has only isolated safe times).
- q=5, speeds (1,3,4,7): maximum tree weight 52/105, below threshold 3/5; again the criterion is inconclusive, consistent with its isolated safe times.
The code also computes exact spanning-tree weights for a five-speed high-ratio example.

## Literature and novelty
Alathea Jensen (2026), Mixed thresholds in the Lonely Runner Conjecture, arXiv:2605.27941, gives an exact two-function integral formula for unequal thresholds. Its primary arXiv record was checked 2026-10-10 and the entry Jensen2026 is already in references/lonely_runner.bib. Therefore the present equal-threshold formula is not asserted to be original without a detailed theorem-level comparison. The classical Fourier series for the periodic Bernoulli polynomial is standard. Experiment 70's tree bound is also classical.

## Honest verdict
A rigorously derived exact identity, with 630 executed independent rational checks and a faster reproducible pair-overlap engine. It does NOT prove LRC for arbitrary speed vectors. Independent Q1-level novelty: not established. The next step must derive a new unconditional arithmetic inequality rather than only repackage existing overlap identities.
