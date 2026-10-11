# Experiment 97 — Verified literature and execution register

Date: 2026-10-11.

## Relevant sources checked against primary records

1. Beck, Matthias; Everett, Samuel (2026). *Lonely Runner Relations*. arXiv:2609.06259. Primary record: https://arxiv.org/abs/2609.06259 . The preprint proves a short-integer-relation necessary condition for counterexample or tight speed vectors; this is distinct from the isolated-witness modular construction. Author/title/arXiv ID checked. The ID already exists in references/lonely_runner.bib.
2. Zhang, Yuhan (2026). *Tight instances of the Lonely Runner Conjecture: complete classification of one-entry modifications, a new infinite family, and the growth bound*. arXiv:2608.13599v2. Primary record: https://arxiv.org/abs/2608.13599v2 . Current v2 title and scope checked, including complete classification of one-entry tight modifications. The master bibliography already contains the v2 title and arXiv identifier.
3. Malikiosis, Romanos Diogenes; Santos, Francisco; Schymura, Matthias (2025). *Linearly exponential checking is enough for the lonely runner conjecture and some of its variants*. Forum of Mathematics, Sigma 13, e164. DOI 10.1017/fms.2025.10107. Primary publisher: https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/linearly-exponential-checking-is-enough-for-the-lonely-runner-conjecture-and-some-of-its-variants/A51A991DE89B8C9C2E2FF13FBD4501DA . Existing DOI and metadata checked.

All three sources were already present in references/lonely_runner.bib. No new source requiring a BibTeX entry was introduced; no duplicate was appended. This is a three-source audit, not a full audit of all bibliography entries.

## Executed exact verification
Local Python exact-integer/Fraction script executed before GitHub commit. The committed experiments/experiment_97_isolated_modular.py reproduces the tested algorithm.

- k=3,N=14: 325 primitive vectors, 432 modular candidates, 256 isolated safe times.
- k=4,N=11: 325 primitive vectors, 788 candidates, 378 isolated safe times.
- k=5,N=9: 126 primitive vectors, 110 candidates, 60 isolated safe times.
- TOTAL: 776 vectors, 1,330 candidates, 694 isolated safe times.

Every modularly generated and phase-filtered isolated set was exactly equal to an independently computed set of safe full-grid vertices with both adjacent elementary cells unsafe. No mismatches.

## Priority and Q1 assessment
The theorem gives a complete constructive isolated-witness classification in all dimensions. It is an elementary extension of the repository's own Experiments 77 and 96; its use of CRT/modular inverses and active opposite constraints is classical. Independent priority and Q1-level mathematical originality have not been demonstrated. It does not imply that a safe time exists in arbitrary speed vectors. The unrestricted Lonely Runner Conjecture is not solved.

## Next proof obligation
Find an arithmetic condition forcing either a positive-length safe interval or at least one modularly generated candidate to survive all remaining speed constraints for every vector. Neither this experiment nor the cited literature establishes such a universal dichotomy.
