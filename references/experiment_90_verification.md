# Experiment 90 — Primary-source literature register, verification and Q1 gate

Date: 2026-10-10. Scope: references used to compare Experiment 90 against prior work, not an audit of all entries in the master BibTeX file.

## Independently checked primary records
1. Malikiosis, Romanos Diogenes; Santos, Francisco; Schymura, Matthias (2025). *Linearly exponential checking is enough for the lonely runner conjecture and some of its variants*. Forum of Mathematics, Sigma 13, e164. DOI 10.1017/fms.2025.10107. Primary publisher: https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/linearly-exponential-checking-is-enough-for-the-lonely-runner-conjecture-and-some-of-its-variants/A51A991DE89B8C9C2E2FF13FBD4501DA . Checked authors, title, 2025 journal publication, DOI, and bound binom(k+1,2)^(k-1). Existing DOI verified in references/lonely_runner.bib.
2. Beck, Matthias; Everett, Samuel (2026). *Lonely Runner Relations*. arXiv:2609.06259. Primary record: https://arxiv.org/abs/2609.06259 . Checked authors, title, 2026 preprint status and short-relation result for potential counterexamples or tight configurations. Existing arXiv identifier verified in master BibTeX.
3. Tao, Terence (2018). *Some remarks on the lonely runner conjecture*. Contributions to Discrete Mathematics 13(2). DOI 10.55016/ojs/cdm.v13i2.62728. Primary publisher record https://cdm.ucalgary.ca/article/view/62728 and existing master BibTeX identifier verified in earlier experiments. No new source needed.

All three sources already appear in references/lonely_runner.bib. There are **zero new literature records** to append for this experiment; duplicating entries would be incorrect. The master bibliography has not been comprehensively rechecked.

## Independent exact execution
The exact integer audit was run in the local container before GitHub commit. It checked 279 primitive speed vectors over (k,N)=(2,18),(3,10),(4,8). For each, it independently evaluated every grid vertex and every midpoint cell, checked G=H+C, and verified the exact forbidden-vertex count 2L-v for each speed. No assertion failed.
Selected exact outputs:
(1,2,3,4): M=60, G=4, H=0, C=4.
(1,3,4,7): M=420, G=4, H=0, C=4.
(1,3,9): M=36, G=7, H=2, C=5.
(2,3,5): M=120, G=10, H=6, C=4.

## Originality and publication-readiness
The cyclic-grid equivalence is a direct reformulation of the boundary observation in Experiment 84, and the component identity is elementary one-dimensional cell topology. Neither is shown to be novel relative to published discrete-geometric methods. The work does not outperform the dimension-dependent finite reduction in Malikiosis–Santos–Schymura (2025), and the common modulus q*lcm(V) is potentially huge. These facts do NOT support a claim that Q1-journal-level novelty has been achieved.

A credible next step would be to prove a genuinely stronger arithmetic bound on cyclic forbidden-set overlaps, or a new reduction of the modulus that outperforms established finite-checking bounds, with rigorous comparison and independent reproducibility.

## Verdict
All-dimensional structural theorem: proved.
Finite audit: 279 primitive vectors passed.
Unrestricted LRC: not solved.
Q1-level breakthrough: not established.
