# Experiment 91 — Verified bibliography and execution register

Date: 2026-10-10.

## Primary-source-verified literature
1. Giri, Vikram; Kravitz, Noah. *The structure of Lonely Runner spectra*. Mathematical Proceedings of the Cambridge Philosophical Society, 180(2), 343–361 (2026); first published online 24 October 2025. DOI: 10.1017/S0305004125101497. Cambridge publisher: https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/structure-of-lonely-runner-spectra/6C8CF8635B7AD8470B1A0104914BA041 . Author names, title, issue, pages and DOI independently checked against the publisher. This article proves spectral structure and discusses finite checking; it does NOT prove unrestricted LRC. Already in references/lonely_runner.bib, so not duplicated.
2. Malikiosis, Romanos Diogenes; Santos, Francisco; Schymura, Matthias. *Linearly exponential checking is enough for the lonely runner conjecture and some of its variants*. Forum of Mathematics, Sigma, 13, e164 (2025). DOI: 10.1017/fms.2025.10107. Cambridge publisher: https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/linearly-exponential-checking-is-enough-for-the-lonely-runner-conjecture-and-some-of-its-variants/A51A991DE89B8C9C2E2FF13FBD4501DA . Authors, title, year, journal, article identifier and DOI independently checked against the publisher. Already in references/lonely_runner.bib, so not duplicated.

## BibTeX audit
Both primary-source-verified DOI strings already occur in the master BibTeX file. No newly used source requires an append; no duplicate was added. The entire master bibliography has NOT been audited entry-by-entry.

## Exact executed audit
Using Python integer modular arithmetic, the Experiment 91 overlap identity and pairwise inequality were checked on 1139 primitive speed vectors. Counts: k=3,N=15: 409 tested, 357 additional pairwise certificates; k=4,N=12: 479 tested, 16 additional; k=5,N=10: 251 tested, zero additional. All 1139 have at least one safe grid vertex. The script experiments/experiment_91_overlap_excess.py reproduces these tests.

## Mathematical priority and Q1 gate
The identity G=sum(v)-(k-1)L+E and bound E>=2P/k are elementary finite-set multiplicity arguments. They provide an exact all-dimensional certificate but are not shown to be new relative to standard union-bound and covering multiplicity inequalities. This result alone does not establish Q1-level novelty or solve the conjecture. The pairwise certificate loses power for the tested five-speed range, so an all-dimensional solution requires substantially stronger arithmetic structure.
