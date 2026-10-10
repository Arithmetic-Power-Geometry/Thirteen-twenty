# Paper readiness tracker — 10 October 2026

## Implemented research/software stages

- [x] CS-001–003 exact rational reference solver and tests
- [x] CS-004 classical admission baselines and tests
- [x] CS-005 conditional contiguous-slot bound
- [x] CS-006 elementary explicit-output lower bound
- [x] CS-007 restricted equal-job capacity theorem and constructive solver
- [x] CS-008 independent exact YES/NO certificate verifier
- [x] CS-009 phase-shifted safe windows and adversarial jitter robustness theorem/solver/tests
- [ ] CS-010 execution, benchmarking and independent reproducibility

**Important:** Source committed is not equivalent to independently executed or validated results. None of the classical restricted scheduling formulas by itself establishes a novel Q1-level CS result.

## Four substantive gates remain before a defensible first full paper draft

1. [ ] **Originality gate:** genuinely new additive-frequency-specific theorem, complexity classification or compelling verified algorithmic improvement. Open-ended research task, not guaranteed.
2. [ ] **CS-010 execution and evidence:** run complete tests, fix any failures, archive machine/software details, raw timing and scaling results, source hashes, cross-language comparisons.
3. [ ] **Closest-prior-work literature audit:** verify sources, BibTeX and claim-by-claim novelty matrix.
4. [ ] **Paper writing and line-by-line audit:** write only established claims with proofs, experimental provenance, limitations, algorithms, figures, tables and accurate citations.

After drafting: specialist review, journal choice/formatting, revisions and submission. Q1 acceptance is never guaranteed.

## Scope warning

The 13/20 measure guarantee is for aligned phases. CS-009 provides an exact solver for shifted phases but **does not** prove the same measure guarantee for independent phase offsets. A large safe measure does not guarantee contiguous task capacity or multi-job admission.
