# Experiment 45 — Exact short-relation exclusion certificate (all dimensions)

Date: 2026-10-10. Status: **verified implementation of a published sufficient condition**, not a new proof of unrestricted LRC.

## Literature-derived theorem and contrapositive

Beck and Everett, *Lonely Runner Relations*, arXiv:2609.06259 (2026), prove that every counterexample **or tight instance** of LRC with k positive integer relative speeds has a nonzero integer vector m with m·v=0 and ||m||_1<=2k+3 (their theorem gives an additional flatness-based improvement). Therefore, **if there is no nonzero integer relation with ||m||_1<=2k+3, then lon(v)>1/(k+1)**. This is a direct contrapositive of prior work, **not an original theorem**. Applies in every finite dimension k.

## Exact decision algorithm

Enumerate all integer coefficients with total L1 budget 2k+3; check exact integer sum m·v. Negative exhaustive search certifies strict safety conditional on Beck–Everett; finding a relation is **inconclusive**, not a counterexample. Exponential runtime; no efficient algorithm claimed.

## Executed results

| Speeds | k | Budget | Relation found | Interpretation |
|---|---:|---:|---|---|
| (1,50,2500,125000) | 4 | 11 | none | strict safe by Beck–Everett |
| (101,103,107,109) | 4 | 11 | (-3,4,0,-1) | inconclusive |
| (1,3,9,27) | 4 | 11 | (-9,0,1,0) | inconclusive |
| (1,20,400,8000) | 4 | 11 | none | strict safe by Beck–Everett |

Executed the script with exact Python integers. Independently brute-force cross-checked 56 distinct two- and three-speed subsets of {1,...,7}, zero discrepancies.

## Novelty and scope

Unlike Experiments 40–43, this searches the arithmetic relation lattice rather than time shifts or forbidden sets. The criterion is already in Beck–Everett; these lacunary examples do not establish a new LRC subclass.

## Bibliography

Matthias Beck and Samuel Everett, *Lonely Runner Relations*, arXiv:2609.06259, submitted 5 September 2026; v2 September 2026, https://arxiv.org/abs/2609.06259. The existing verified key `BeckEverett2026` is retained in `references/lonely_runner.bib`. No duplicate or unverified entry appended.

## Unsolved

Configurations admitting short relations remain unresolved by this criterion; such relations do **not** imply counterexamples. No unrestricted LRC proof is claimed.
