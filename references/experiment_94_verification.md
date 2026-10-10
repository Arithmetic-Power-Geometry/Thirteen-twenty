# Experiment 94 — Primary literature verification and execution register

Date: 2026-10-10.

## Verified references
1. Blanco, Mónica; Criado, Francisco; Santos, Francisco (2026). *Coloopless zonotopes and counterexamples to the Shifted Lonely Runner Conjecture*. arXiv:2603.24784v3, revised 2 October 2026. Primary arXiv record https://arxiv.org/abs/2603.24784 checked for author names, current title, version, revision date and abstract. The paper gives counterexamples to the SHIFTED LRC (starting at n=5) and the Lonely Vector Property; these are NOT counterexamples to the ordinary unrestricted LRC. Updated the existing key BlancoCriadoSantos2026 in references/lonely_runner.bib from v2 to v3; no duplicate was added. Commit 79a0ca14f26ec25682ca8a55b3d9dc21f7397e4c.
2. Malikiosis, Romanos Diogenes; Santos, Francisco; Schymura, Matthias (2025). *Linearly exponential checking is enough for the lonely runner conjecture and some of its variants*. Forum of Mathematics, Sigma 13, e164. DOI 10.1017/fms.2025.10107. Publisher record https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/linearly-exponential-checking-is-enough-for-the-lonely-runner-conjecture-and-some-of-its-variants/A51A991DE89B8C9C2E2FF13FBD4501DA checked for title, authors, DOI, volume and year. Existing master BibTeX entry retained.

The scope is these two literature records, not a complete line-by-line verification of all entries in the master BibTeX.

## Independently executed exact checks
Python integer-only audit, executed locally before committing the code: 527 primitive speed vectors with (k,N)=(3,12),(4,10),(5,9). Each checks the exact counts of safe grid vertices G, safe cells H and components C, and verifies G=H+C and all three reflection parity formulas. All 527 passed.

## Novelty and Q1 decision
The reflection parity theorem is a self-contained elementary involution argument, valuable as a strong internal consistency check on grid computations but not independently established as novel. It does not improve the best known finite-checking bound, settle the conjecture, or establish Q1-level mathematical significance. The bibliography correction is substantive for citation accuracy, but it is not a mathematical breakthrough.

## Verdict
All-dimensional theorem proved; 527 checks passed; primary-source bibliography updated; unrestricted LRC remains open; Q1 breakthrough not established.
