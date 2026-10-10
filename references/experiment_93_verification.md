# Experiment 93 — Source verification and research novelty audit

Date: 2026-10-10.

## Verified primary literature

1. Malikiosis, Romanos Diogenes; Santos, Francisco; Schymura, Matthias (2025). *Linearly exponential checking is enough for the lonely runner conjecture and some of its variants*. *Forum of Mathematics, Sigma*, **13**, e164. DOI: **10.1017/fms.2025.10107**. Primary publisher: https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/linearly-exponential-checking-is-enough-for-the-lonely-runner-conjecture-and-some-of-its-variants/A51A991DE89B8C9C2E2FF13FBD4501DA . Publisher verifies title, authors, 2025 publication, journal, DOI and bound binom(k+1,2)^(k-1) for the finite-checking problem. Existing DOI confirmed in references/lonely_runner.bib; do not duplicate.
2. Giri, Vikram; Kravitz, Noah (2026). *The structure of Lonely Runner spectra*. *Mathematical Proceedings of the Cambridge Philosophical Society*, **180**(2), 343–361. DOI: **10.1017/S0305004125101497**. Primary publisher: https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/structure-of-lonely-runner-spectra/6C8CF8635B7AD8470B1A0104914BA041 . Publisher confirms title, authors and first-online date 24 October 2025; existing bibliography includes 2026 issue metadata and DOI. Do not duplicate.

## Bibliography policy

Both sources used for the literature comparison are already in references/lonely_runner.bib with the correct DOI. **No new literature was used requiring a new BibTeX entry.** No duplicates were appended. This register does NOT claim that all other bibliography entries have been individually verified.

## Executed verification

A local Python exact-integer script independently compared generalized-CRT counts against full-grid enumeration for 3,211 subset instances from primitive full vectors at (k,N)=(3,10),(4,9),(5,8). Passed: 1,637 pairs, 1,169 triples, 405 quadruples. No discrepancies. The committed script reproduces these tests and asserts the totals. The mathematical proof does not depend on the computation.

## Novelty and Q1 decision

The generalized-CRT count is a rigorous extension of Experiment 92 to arbitrary intersection order, but generalized CRT and inclusion–exclusion are classical. The algorithm can be exponential in subset size and no state-of-the-art benchmark or new asymptotic result has been demonstrated. It does NOT establish a Q1-journal-level original contribution on its own. Unrestricted LRC remains open.
