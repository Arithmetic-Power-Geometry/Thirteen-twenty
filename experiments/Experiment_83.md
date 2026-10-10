# Experiment 83 — Every fixed odd Bonferroni truncation fails on consecutive speeds

Date: 2026-10-10. Status: proved all-dimensional no-go theorem for a class of certificates. The unrestricted Lonely Runner Conjecture remains open.

## Theorem 83.1 (uniform no-go at every fixed odd order)
Let k>=2, q=k+1, and V_k=(1,2,...,k). For 1<=j<=k define
S_j=sum_{|J|=j} measure(intersection_{i in J} B_i),
B_i={t mod 1: ||it||<1/q}, and S_0=1.
For every odd integer m with 1<=m<k, define C_m=sum_{j=0}^m (-1)^j S_j.
Then
C_m(V_k) <= -[2/(k(k+1))]*binom(k-1,m)<0.
Consequently, no fixed odd truncation order m, independently of dimension, can yield a universally positive-measure Bonferroni certificate for LRC.

## Proof
(1) The safe-time set for V_k is finite. If t is safe, the q points 0,t,2t,...,kt on the unit circle have pairwise circular distance at least 1/q, since any difference is (i-j)t and 1<=|i-j|<=k. Ordering these q distinct points cyclically, every consecutive gap is at least 1/q; their gaps sum to 1. Therefore all gaps equal 1/q, and t is an integer multiple of 1/q. Thus the safe set has measure zero (indeed its points are precisely t=a/q with gcd(a,q)=1).

(2) Let N(t)=sum_{i=1}^k 1_{B_i}(t). At each t, the binomial theorem for counting subsets gives
sum_{j=0}^m (-1)^j binom(N(t),j) =
1 if N(t)=0, and (-1)^m binom(N(t)-1,m) if N(t)>=1.
For odd m, the latter is -binom(N(t)-1,m). Integrating and using that the safe set has measure zero yields
C_m(V_k)=-integral_{N(t)>=1} binom(N(t)-1,m) dt.

(3) For 0<t<1/(qk), all it satisfy 0<it<1/q, so N(t)=k. The same holds for 1-1/(qk)<t<1. These disjoint arcs have total measure 2/(qk). Therefore
C_m(V_k)<=-[2/(qk)]*binom(k-1,m)<0.
This proves the theorem.

## Exact defect identity (all V, not only consecutive)
For arbitrary distinct positive integer speeds V of size k and odd m<=k,
measure(safe times)=C_m(V)+integral_{N(t)>=1}binom(N(t)-1,m)dt.
This is a precise identity quantifying the information lost by truncating inclusion-exclusion. It does NOT establish a universal positive lower bound.

## Reproducibility
The program experiments/experiment_83_odd_order_no_go.py checks the pointwise binomial identity and exact rational gap bound across k=2,...,40 and all odd m<k; it independently partitions the circle to verify the identity for representative small k. The mathematical theorem does not depend on computation.

## Research significance and novelty
Experiments 81 and 82 compared third- and fifth-order methods on lacunary speed sets. Experiment 83 establishes a single theorem excluding every FIXED odd-order Bonferroni strategy on the canonical tight family in arbitrarily high dimensions. This avoids repeatedly testing higher orders as a purported route to a universal LRC proof. The ingredients (inclusion-exclusion, elementary circle packing) are classical; independent publication-level novelty is not established. The result does not preclude adaptive order, exact inclusion-exclusion, structural or Fourier methods.

## Literature
Perarnau, Guillem and Serra, Oriol, The Lonely Runner Conjecture turns 60, arXiv:2409.20160. Beck, Matthias and Everett, Samuel, Lonely Runner Relations, arXiv:2609.06259. Bedert, Benjamin, Riesz products and the Lonely Runner Conjecture: A wider gap of loneliness, arXiv:2511.16636. These sources are contextual; no source is required for the self-contained proof. All are already recorded in references/lonely_runner.bib; no duplicate entries added.

## Verdict
Proved an all-dimensional method limitation; no universal LRC solution; no independent priority claim.
