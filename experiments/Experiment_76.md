# Experiment 76: exact Wills tightness certificate and priority correction

Date: 2026-10-10
Verdict: exact bounded proof, NOT a new theorem or a general solution.

## Theorem
For the four-speed set V=(1,3,4,7), the entire safe set at threshold 1/5 is exactly {1/5,2/5,3/5,4/5} modulo one. In particular the maximum loneliness is exactly 1/5.

## Exact proof
For each a in V, the truth of ||a*t||>=1/5 can change only at rational boundaries t=(5*n+1)/(5*a) or (5*n-1)/(5*a), restricted to [0,1]. Sort these boundaries together with 0 and 1. The exact script experiment_76_wills_certificate.py constructs 28 distinct boundaries, hence 27 open cells. Every speed's safety predicate is constant within each cell. It tests the exact rational midpoint of each of the 27 cells and records at least one speed violating the 1/5 threshold on each. It also evaluates all boundary points and verifies that exactly 1/5,2/5,3/5,4/5 are safe. The exhaustive cell and boundary checks prove the asserted set identity, since the cells and boundaries partition the circle.

Each j/5, j=1,2,3,4, is indeed safe because speeds (1,3,4,7) reduce to the complete nonzero residue system (1,3,4,2) modulo five, and multiplication by j permutes the nonzero residues. The maximum cannot exceed 1/5: a larger maximum would, by continuity, create a nonempty safe open interval, contradicted by the certified partition. Therefore maximum loneliness equals 1/5.

## Reproducibility
Run: python3 experiments/experiment_76_wills_certificate.py
The code uses fractions.Fraction throughout, asserts the four safe times and 27 forbidden open cells, and prints a rational certificate for every cell. No floating point.

## Independent audit of Experiment 75
A separate local exact-rational implementation reproduced 409 primitive triples from [1,15], with one tight and zero violations, and 479 primitive quadruples from [1,12], with two tight and zero violations. These finite findings are not a general proof.

## Literature and novelty correction
The tuple (1,3,4,7) is a classical Wills tight instance, not our discovery. It is explicitly listed in the Perarnau–Serra survey, The Lonely Runner Conjecture turns 60 (arXiv:2409.20160), and in Yuhan Zhang's 2026 complete one-entry classification (arXiv:2608.13599v2). Goddyn and Wong, Tight instances of the lonely runner, Integers 6 (2006), A38, is relevant historical work. These references are already in references/lonely_runner.bib; avoid duplicates. The reproducible exact certificate is an audit artifact, not an original theorem.

## Research conclusion
No unrestricted LRC solution and no independently novel Q1-level result. Further work must address genuinely unresolved configurations, not rediscover classified tight examples.
