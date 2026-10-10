# Experiment 95 — Verified literature and independent execution register

**Audit date:** 2026-10-10. Scope: literature actually used for Experiment 95, not all 35 entries in the master bibliography.

## Primary sources verified online

1. Tao, Terence (2018). *Some remarks on the lonely runner conjecture*. *Contributions to Discrete Mathematics*, **13**(2). DOI: **10.55016/ojs/cdm.v13i2.62728**. Primary publisher: https://cdm.ucalgary.ca/article/view/62728 . The publisher page confirms author, title, DOI, publication date 2018-12-31, and volume/issue. Existing DOI found in references/lonely_runner.bib.
2. Malikiosis, Romanos Diogenes; Santos, Francisco; Schymura, Matthias (2025). *Linearly exponential checking is enough for the lonely runner conjecture and some of its variants*. *Forum of Mathematics, Sigma*, **13**, e164. DOI: **10.1017/fms.2025.10107**. Primary publisher: https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/linearly-exponential-checking-is-enough-for-the-lonely-runner-conjecture-and-some-of-its-variants/A51A991DE89B8C9C2E2FF13FBD4501DA . Publisher confirms authors, title, 2025 issue, DOI and the dimension-dependent finite-checking theorem. Existing DOI found in master bibliography.
3. Beck, Matthias; Everett, Samuel (2026). *Lonely Runner Relations*. arXiv:2609.06259. Primary preprint record: https://arxiv.org/abs/2609.06259 . arXiv confirms authors, title, 2026 preprint and its bounded-short-relation theorem for tight or counterexample configurations. Existing arXiv ID found in master bibliography.

All three sources were already present. **No new BibTeX entry was needed or appended.** The master file was not altered, avoiding duplicates. No claim is made that all 35 entries were independently verified this turn.

## Exact execution (local Python)

The file experiments/experiment_95_event_sweep.py was independently executed before its GitHub commit. It computes event points with Fraction arithmetic and compares (G,H,C) to a separate integer-only full-grid enumeration.

Results:
- k=2, speeds<=12: 45 primitive vectors, all passed.
- k=3, speeds<=10: 109 primitive vectors, all passed.
- k=4, speeds<=8: 69 primitive vectors, all passed.
- k=5, speeds<=7: 21 primitive vectors, all passed.
- Total 244 exact comparisons, zero failures.

Large instance V=(101,103,107,109,113):
- M=82,261,868,142 (NOT exhaustively enumerated);
- event intervals=1,059;
- G=11,732,278,703, H=11,732,278,616, C=87;
- rational witness=1/606.

Known tight instance (1,3,4,7): G=4,H=0,C=4, witness=1/5.

## Novelty and Q1 gate

The boundary event principle was already used in this project's Experiments 74 and 84; this experiment develops it into an exact output-sensitive sweep for topology and grid counts. Rational arrangement sweeps are classical, so a first-priority mathematical novelty claim is unwarranted. The method is not a proof of unrestricted LRC, and it is not a stronger dimension-only finite reduction than the 2025 published result.

**Verdict:** all-dimensional exact algorithm proved; 244 independent small-instance comparisons passed; large instance exact-sweep result verified internally, not by full-grid enumeration; unrestricted LRC unsolved; Q1-journal-level novelty not established.
