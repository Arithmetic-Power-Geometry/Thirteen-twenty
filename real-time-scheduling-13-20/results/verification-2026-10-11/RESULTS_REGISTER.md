# Verified results register — 2026-10-11

This register records results from the independent local checks of the exact additive-frequency measure and scheduling implementation. It is a research evidence index, not manuscript text or a claim of independent formal proof.

## Exact 13/20 certificate

- Bound: F(a,b) >= 13/20 for positive integer a,b, with the analytic tail and finite verification considered separately.
- C++ finite exact search: 11,698 coprime ordered representatives with 1 <= a <= b <= 196.
- Violations: 0.
- Equality cases: 1, at (a,b)=(1,14).
- Recorded exact equality fraction: 2184/3360 = 13/20.
- Independently implemented Python Fraction check: 128 pairs; 0 violations; F(1,14)=13/20; F(3,5)=213/320.
- Analytic cutoff is a mathematical argument and must not be conflated with C++ enumeration.

## Scheduling checks

- 15/15 Python unittest tests passed in local Step 2 reproduction (8 pre-existing and 7 independent-witness tests).
- 40 small exhaustive-oracle cases covered by existing tests.
- 16/16 deterministic small finite-grid instances had identical exact-DP and SciPy/HiGHS MILP objectives.
- Independent exact-rational witness checker verifies job indices, processing times, release/deadline constraints, calendar containment, non-overlap, and reported objective.
- Witness feasibility checking is not a separate proof of optimality; the MILP comparison is limited to the 16 finite-grid instances.
- MILP mean runtime was lower at job counts 8, 10, 12 in the recorded run.

## Paper reconciliation

- Current manuscript: 16 pages, 2 figures, 8 tables, 7 algorithms, 50 bibliography entries.
- Main numerical claims matched the available local computation records in Step 3.
- The final cleaned manuscript and supplementary code archive were generated locally, but publication of their exact bytes on GitHub requires a separate file upload.
- Prior archived CI evidence mentions 29 tests for each of two Python versions; the remote CI jobs were not independently rerun in the Step 3 audit.

## Limitations

The numbers above are an auditable result register, not a replacement for the exact source files, machine logs, binary archives, or a journal's review process. Do not cite this register as proof of independent reproduction by third parties.
