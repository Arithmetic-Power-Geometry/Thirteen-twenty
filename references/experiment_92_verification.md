# Experiment 92 — Literature verification, computational audit, and Q1 gate

Date: 2026-10-10. Verification scope: the three works used for current comparison, NOT every record in the master bibliography.

## Literature checked
1. Malikiosis, Romanos Diogenes; Santos, Francisco; Schymura, Matthias (2025). *Linearly exponential checking is enough for the lonely runner conjecture and some of its variants*. Forum of Mathematics, Sigma 13, e164. DOI 10.1017/fms.2025.10107. Primary Cambridge publisher record: https://doi.org/10.1017/fms.2025.10107 . Previously verified publisher metadata and DOI. Existing BibTeX DOI found in references/lonely_runner.bib.
2. Zhang, Yuhan (2026). *Tight instances of the Lonely Runner Conjecture: complete classification of one-entry modifications, a new infinite family, and the growth bound*. arXiv:2608.13599v2. Primary record https://arxiv.org/abs/2608.13599 . v2 dated 11 September 2026; exact title and author checked against the arXiv-indexed version record. Existing BibTeX arXiv identifier found, so no duplicate.
3. Allikvere, Jaan (2026). *Fourteen and fifteen lonely runners*. arXiv:2609.02604v2. Primary record https://arxiv.org/abs/2609.02604 . v2 dated 25 September 2026, 15 pages, reports computer-assisted proofs for fourteen and fifteen runners, with Zenodo certificates. These remain preprint claims pending independent validation/peer review. Existing BibTeX arXiv identifier found, so no duplicate.

No newly USED literature source is absent from the bibliography. The master references/lonely_runner.bib is unchanged to avoid duplicate entries. Its other entries have NOT been comprehensively reverified in this experiment.

## Executed exact verification
The committed Python program was executed locally using integer arithmetic. All 3,157 primitive-vector pair comparisons passed, across (k,N)=(2,16),(3,12),(4,10),(5,9). It compares the CRT formula against direct evaluation on the full grid qL, without floating point. The initial draft incorrectly scaled local grid-vertex counts by the global refinement factor. That failed a regression and was corrected by separately counting forbidden open cells and vertices; the FINAL program passed all checks. The correction is included in the theorem proof.

## Mathematical novelty and publication gate
The formula gives an exact O(q(A+B)) pair-overlap algorithm, useful when qL is large and reduced pair speeds A,B are small. It uses classical generalized CRT and elementary grid topology, and no priority search establishes it as independently novel. It does not give a universal lower bound on the number of safe residues. It therefore does not solve unrestricted LRC and does not independently reach Q1-journal-level mathematical significance. A defensible computational publication would need benchmark comparisons, genuinely better complexity for a well-defined subproblem, and independent validation.

## Verdict
All-dimensional pairwise formula proved. 3,157 tests passed. Bibliography deduplicated. Unrestricted LRC open; Q1 novelty not established.
