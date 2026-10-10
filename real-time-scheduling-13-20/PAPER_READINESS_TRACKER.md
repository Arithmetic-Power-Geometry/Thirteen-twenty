# Paper readiness tracker — 10 October 2026

## Implementation progress

- [x] CS-001–003 exact rational single-job solver
- [x] CS-004 classical baseline algorithms
- [x] CS-005 conditional contiguous-slot theorem
- [x] CS-006 explicit-output lower bound
- [x] CS-007 restricted equal-job capacity theorem
- [x] CS-008 independent certificate verifier
- [x] CS-009 phase-shift and jitter robustness solver
- [x] CS-010 CI workflow, test harness and benchmark script **committed**
- [ ] CS-010 inspect completed CI runs, fix failures, archive verified raw data and repeat benchmarks

## Three high-level gates remain before a defensible full paper draft

1. [ ] **Execution and reproducibility audit:** confirm GitHub Actions results for Python 3.11/3.12, repair test/code failures, inspect artifacts, run repeated fair experiments, independently verify claims.
2. [ ] **Novelty and verified bibliography:** demonstrate a genuinely new additive-frequency-specific algorithmic/complexity or rigorously evidenced systems result; verify closest literature and full bibliography. This gate is open-ended and not assured by the preceding implementation.
3. [ ] **Full paper writing and pre-submission audit:** claim–proof–artifact alignment, complete citations, figures, tables, algorithms, reproducible provenance, no internal instructions.

This is a **three-gate workflow**, not a guarantee of a Q1 paper in three routine steps. A draft can be started earlier as a working paper, but Q1-level novelty has not been demonstrated.

## Next action

Inspect Actions runs and artifacts at https://github.com/Arithmetic-Power-Geometry/Thirteen-twenty/actions. Do not report CS-010 experiments as passed until actual logs and JSON are reviewed. Do not treat the 13/20 safe-time measure as a 65% throughput guarantee.
