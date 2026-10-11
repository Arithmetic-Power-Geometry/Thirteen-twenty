# Experiment 98 — Bibliography, proof, and execution register

Date: 2026-10-11.

## Primary-source literature verification

1. Beck, Matthias; Everett, Samuel (2026). *Lonely Runner Relations*. arXiv:2609.06259. Primary record: https://arxiv.org/abs/2609.06259 . Author names, title and the short-integer-relation necessary condition for tight/counterexample instances verified from the arXiv abstract. Already in references/lonely_runner.bib.
2. Malikiosis, Romanos Diogenes; Santos, Francisco; Schymura, Matthias (2025). *Linearly exponential checking is enough for the lonely runner conjecture and some of its variants*. *Forum of Mathematics, Sigma* **13**, e164. DOI 10.1017/fms.2025.10107. Primary publisher: https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/linearly-exponential-checking-is-enough-for-the-lonely-runner-conjecture-and-some-of-its-variants/A51A991DE89B8C9C2E2FF13FBD4501DA . Title, authors, journal, year, article number, and finite-checking scope verified. Already in references/lonely_runner.bib.

Both references were already present, so no duplicate BibTeX was appended. This is a two-source audit, not a full audit of all existing bibliography entries.

## Exact independent execution

Executed Python Fraction tests locally on 901 primitive vectors, checking the q-divisibility exclusion, exact endpoints, safe midpoints, immediately unsafe exterior points, and isolation criterion. Results:
- k=3,N=14: 325 vectors; 160 anchored; 77 isolated; 83 positive intervals.
- k=4,N=11: 325 vectors; 125 anchored; 76 isolated; 49 positive intervals.
- k=5,N=10: 251 vectors; 126 anchored; 55 isolated; 71 positive intervals.
- TOTAL 901 primitive vectors, 411 anchored, 208 isolated anchors, 203 positive-length anchored intervals.

The exact proof is independent of these computations. The repository's experiments/experiment_98_residue_anchor.py reproduces the checks.

## Mathematical novelty and journal readiness

The t=1/(k+1) residue certificate is immediate from modular arithmetic, and the component endpoint formula follows by taking the first safe-arc boundary on each side. This is a rigorous all-dimensional family theorem but does NOT establish a new Q1-level mathematical result or unrestricted LRC. The positive-density assertion is for independent uniform residue classes and must not be conflated with finite primitive-vector counts.

**Verdict:** theorem proved; 901 exact tests passed; two existing primary references verified and deduplicated; unrestricted LRC remains open; Q1 novelty not established.
