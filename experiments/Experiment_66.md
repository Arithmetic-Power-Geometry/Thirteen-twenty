# Experiment 66 — Quantitative count of the short-relation stratum

Date: 2026-10-10
Status: complete combinatorial proof; corollary of Beck–Everett (2026), and weaker than Czerwinski's 2012 random-runner theorem. Not a universal LRC proof or an originality claim.

## Statement
Fix k>=2, L=2k+3, N>=k. Choose an ordered k-tuple of distinct positive integer speeds uniformly from {1,...,N}; there are (N)_k=N(N-1)...(N-k+1) choices. Put R(k,L)=sum_{j=1}^{min(k,L)} binom(k,j)*2^j*binom(L,j).

## Theorem 66.1
The fraction of tuples admitting a nonzero m in Z^k with ||m||_1<=L and m dot v=0 is at most min(1,R(k,L)*N^(k-1)/(2*(N)_k)). Consequently, by Beck–Everett, at least the complementary fraction of speed vectors have maximum loneliness strictly greater than 1/(k+1). For each fixed k the exceptional fraction is O_k(1/N).

## Proof
Count coefficient vectors by the number j of nonzero entries. Choose their locations in binom(k,j) ways, their signs in 2^j ways, and their positive absolute values with sum at most L in binom(L,j) ways (stars and bars). This gives exactly R(k,L) nonzero coefficient vectors. Relations m and -m define the same equation; hence there are R(k,L)/2 sign-pairs. For each relation, choose a coordinate with nonzero coefficient. After fixing the other k-1 speed values in [N], the chosen speed is uniquely determined as a rational number and may fail to be a distinct integer in [N]; therefore there are at most N^(k-1) ordered tuples satisfying the relation. A union bound over sign-pairs gives at most R(k,L)*N^(k-1)/2 exceptional ordered tuples. Divide by (N)_k and cap at 1. Beck–Everett show that any tight instance or counterexample has such a short relation, so every tuple outside this union has loneliness strictly exceeding 1/(k+1). Since (N)_k~N^k for fixed k, the exceptional proportion is O_k(1/N). QED.

## Explicit numerical interpretation
This bound is deliberately conservative and can exceed one for realistic N; it is useful as an exact asymptotic and finite counting certificate, not as an efficient numerical solver. It does not say that tuples with a short relation violate LRC: the tight tuple (1,...,k) has many such relations and satisfies LRC.

## Originality and literature
The counting proof is elementary; the substantive structural theorem belongs to Matthias Beck and Samuel Everett, *Lonely Runner Relations* (2026), arXiv:2609.06259.
Sebastian Czerwinski, *Random runners are very lonely*, Journal of Combinatorial Theory, Series A 119(6) (2012), 1194–1199, DOI 10.1016/j.jcta.2012.02.002, proves a much stronger almost-sure loneliness result approaching 1/2. Publisher metadata checked 2026-10-10.
Do not claim novelty or a general solution based on this weaker corollary.

## Next genuine challenge
The O_k(1/N) arithmetic stratum contains tight instances for every k. Counting it as sparse does not prove safety inside it. A breakthrough must analyze the relation-bearing configurations, not merely their density.

## Verdict
Mathematical proof complete, all dimensions with fixed k and N>=k; no new Q1-level result, unrestricted LRC unsolved.
