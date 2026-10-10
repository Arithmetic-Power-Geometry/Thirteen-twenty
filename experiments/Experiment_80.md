# Experiment 80 — Third-order Bonferroni succeeds beyond the pairwise-tree barrier

Date: 2026-10-10
Status: exact all-dimensional inequality plus rational certificate for a specific four-speed instance. Unrestricted Lonely Runner Conjecture NOT solved.

## Theorem 80.1 (all dimensions)
Let V={v_1,...,v_k}, k>=3, be distinct positive integer speeds, q=k+1, and B_i={t mod 1: ||v_i*t||<1/q}. Put
S2=sum_{i<j} mu(B_i intersection B_j),
S3=sum_{i<j<l} mu(B_i intersection B_j intersection B_l).
Then
mu({t: ||v_i*t||>=1/q for all i}) >= 1-2k/q+S2-S3.
In particular, strict positivity of the right side proves the LRC assertion for V, with a positive-measure set of safe times.

## Proof
At a fixed time t let N(t) be the number of forbidden sets B_i containing t. For every nonnegative integer N,
1_{N>=1} <= N - binom(N,2) + binom(N,3).
Indeed the right side equals 1 for N=1,2,3, and for N>=4 it is 1+binom(N-1,3)>=1. Integrate over t. The integral of N is sum_i mu(B_i)=2k/q; integrals of binom(N,2) and binom(N,3) are S2 and S3. Thus the union of forbidden sets has measure at most 2k/q-S2+S3, and its complement (safe times) has the asserted lower bound. QED.

## Exact positive certificate not covered by Experiment 70/79
For V=(11,13,17,19), q=5, exact rational boundary-sweep calculations give
S2=221262/230945,
S3=59522/230945,
1-8/5+S2-S3=23173/230945 >0.
Hence the safe-time set has positive measure.

The pairwise-tree sufficient condition cannot succeed on this V: every pair is coprime and the smallest pair product is 11*13=143>25/4=q^2/[4(q-4)]. Theorem 79.1 therefore forces every pair overlap to be <1/5 and every spanning-tree sum <3/5, below the necessary threshold for the pair-tree certificate. Thus the third-order bound succeeds on an instance where the pairwise-tree certificate provably fails.

## Additional exact regressions
V=(1,2,4,8): S2=19/20, S3=3/10, lower=1/20>0.
V=(1,3,5,7): S2=164/175, S3=48/175, lower=11/175>0.
V=(1,2,3,4): lower=-1/10 (inconclusive).
V=(1,3,4,7): lower=-2/35 (inconclusive, although the vector is known tight).

## Reproducibility
Code: experiments/experiment_80_triple_bonferroni.py. Every measure is computed by exact rational partition of the circle at all forbidden-set endpoints; each cell midpoint has constant membership in each forbidden set. The script asserts the five exact rational cases and independently computes exact full safe-set measure as a cross-check. No floating point.

## Novelty and literature
Bonferroni inequalities and inclusion-exclusion are classical. The result is a reproducible methodological advance within this experiment series, not a claim of a novel mathematical theorem or a solution of LRC. Related Fourier pairwise methods: Jensen (2026), Mixed thresholds in the Lonely Runner Conjecture, arXiv:2605.27941. Related short-relation framework: Beck and Everett (2026), Lonely Runner Relations, arXiv:2609.06259. Both are already in references/lonely_runner.bib. These sources do not supply novelty for the Bonferroni inequality.

## Next research direction
Search for a dimension-uniform, genuinely new lower bound on S2-S3, or a sparse higher-order dependency certificate. Merely computing finite triples does not prove LRC for all k or all speed vectors.
