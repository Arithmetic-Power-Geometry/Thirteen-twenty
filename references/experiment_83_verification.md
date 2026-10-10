# Experiment 83 — Verified bibliography and exact-audit register

Date: 2026-10-10. This register concerns Experiment 83's actual sources; it is NOT a full-library verification.

## Primary-source verification
1. Perarnau, Guillem; Serra, Oriol. *The Lonely Runner Conjecture turns 60*. arXiv:2409.20160v3 (revised 12 August 2025), https://arxiv.org/abs/2409.20160 . Primary arXiv record confirms both authors, title, identifier and survey scope. Existing repository BibTeX record includes the identifier; do not duplicate.
2. Beck, Matthias; Everett, Samuel. *Lonely Runner Relations*. arXiv:2609.06259, https://arxiv.org/abs/2609.06259 . Primary arXiv record confirms authors, title and short-integer-relation result. Existing BibTeX key BeckEverett2026; do not duplicate.
3. Bedert, Benjamin. *Riesz products and the Lonely Runner Conjecture: A wider gap of loneliness*. arXiv:2511.16636 (submitted 20 November 2025), https://arxiv.org/abs/2511.16636 . Primary arXiv record confirms author, title, identifier and the claimed lower-bound improvement 1/(2n)+1/n^(5/3+o(1)). Existing key Bedert2025Riesz; do not duplicate.

All three identifiers were checked as already present in references/lonely_runner.bib. There are no genuinely new cited items to append. Other BibTeX entries were not individually checked.

## Verification execution
The exact rational forbidden-interval partition was independently executed in Python for k=2 through k=10, checking every odd truncation order m<k. All 9 cases passed, with exact zero safe-time measure, exact binomial defect identity, and the strict quantitative upper bound. The committed program extends pointwise checks to k<=40 and contains the same rational interval audit for k<=10. The higher-range assertions in the committed script were not separately executed in this turn; the mathematical proof is independent of those checks.

## Novelty and limitations
The precise all-order no-go statement is proved in Experiment 83. Its ingredients are standard binomial identities, Bonferroni truncation and tight consecutive-speed circle packing. Independent originality and publication-level novelty have not been established; no claim of a universal LRC solution is warranted.
