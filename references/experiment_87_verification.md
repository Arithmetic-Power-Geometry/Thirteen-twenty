# Experiment 87 — Priority, source verification, and execution status

Date: 2026-10-10.

## Sources
1. Beck, Matthias and Everett, Samuel (2026). *Lonely Runner Relations*. arXiv:2609.06259v2, https://arxiv.org/abs/2609.06259 . Primary arXiv abstract confirms authors, title, short-relation theorem and publication as preprint. Existing BibTeX key BeckEverett2026, not duplicated.
2. Arbiter (2026). *Lonely Runner Conjecture*, public project page https://arbiter.wiki/problems/lonely-runner . The visible update dated July 29, 2026 describes a 'Theorem R: valuation rigidity of counterexamples' with the same prime-shift mechanism and condition b*ceil(2p/(n+1))<p. This establishes a priority warning against claiming Experiment 87 as independently novel. The page is a public research project record, NOT an independently verified peer-reviewed journal paper; attribution and proof have not been independently audited. A clearly marked @misc online source was appended as Arbiter2026ValuationRigidity.
3. Perarnau, Guillem and Serra, Oriol (2025 revision). *The Lonely Runner Conjecture turns 60*, arXiv:2409.20160. Existing bibliography entry; background only, not needed for the proof.

## Verification status
The mathematical prime-shift argument is self-contained and has been checked symbolically. The exact Fraction script experiments/experiment_87_prime_shifts.py has been committed and includes exhaustive bounded test loops, but those loops were NOT executed in the present turn. Do not report a numeric number of passing cases or say the script passed until independently run. The sample vector (1,6,10,14,22) satisfies the sufficient condition, subject to the four-speed lower-dimensional theorem; the code constructs the witness.

## Novelty and solution status
The main prime-shift criterion is already publicly reported by July 2026. Experiment 87 provides a clean self-contained proof and exact modular formulation, not a claim of first discovery. It does not prove unrestricted LRC. The entire bibliography has not been verified entry-by-entry; only the sources used in this experiment were checked.
