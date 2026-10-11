# Experiment 96 — Literature and exact-verification register

Date: 2026-10-11.

## Literature verified against publisher sources

1. Czerwiński, Sebastian (2018). *The lonely runner problem for lacunary sequences*. Discrete Mathematics **341**(5), 1301–1306. DOI **10.1016/j.disc.2018.02.002**. Primary Elsevier publisher https://www.sciencedirect.com/science/article/pii/S0012365X18300335 confirms author, title, volume, issue, pages, date and DOI. Existing BibTeX key Czerwinski2018Lacunary and DOI verified in references/lonely_runner.bib. No duplicate appended.
2. Malikiosis, Romanos Diogenes; Santos, Francisco; Schymura, Matthias (2025). *Linearly exponential checking is enough for the lonely runner conjecture and some of its variants*. Forum of Mathematics, Sigma **13**, e164. DOI **10.1017/fms.2025.10107**. Primary Cambridge publisher https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/linearly-exponential-checking-is-enough-for-the-lonely-runner-conjecture-and-some-of-its-variants/A51A991DE89B8C9C2E2FF13FBD4501DA confirms title, authors, volume, date and DOI. Existing master BibTeX DOI verified. No duplicate appended.

These two references are background comparators; they are not claimed to prove or anticipate the specific bound of Experiment 96. This audit does not claim every other master bibliography record was reverified.

## Independent exact execution
Locally executed /tmp/exp96.py using exact fractions and independent integer-grid tests before creating the GitHub files. Its mathematical logic and asserted totals are reproduced in experiments/experiment_96_isolated_collisions.py.

Results:
- k=3, speeds <=14: 325 primitive vectors; 256 isolated safe points.
- k=4, speeds <=11: 325 primitive vectors; 378 isolated safe points.
- k=5, speeds <=9: 126 primitive vectors; 60 isolated safe points.
- Total 776 primitive vectors and 694 isolated safe points.
- Every isolated point was found in the union of opposite-boundary collision candidates; all candidate sets were bounded by 2 sum gcd(a,b) over qualifying pairs.

The direct-grid method is independent of the collision enumeration; the proof is independent of all computation.

## Novelty and journal gate
The opposite-boundary necessary condition q | (a+b)/gcd(a,b) appeared already in Experiment 77. The quantitative upper bound on the count of isolated safe times and the exact collision enumeration are this experiment's extension. Elementary CRT and a union bound make independent first-priority mathematical novelty uncertain. This does not imply existence of safe times in the absence of candidate collisions, and cannot solve unrestricted LRC.

**Status:** mathematical theorem proved, 776 exact vectors checked, literature deduplicated, unrestricted conjecture OPEN, Q1-level originality NOT ESTABLISHED.
