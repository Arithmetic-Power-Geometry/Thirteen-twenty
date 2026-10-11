# Exact Scheduling with Additive-Frequency Availability Calendars

This directory contains computational artifacts for rational single-machine availability calendars, including additive-frequency calendars defined by the coupled frequencies a, b, and a+b.

## Research components

- [Formal problem definitions](FORMAL_PROBLEM_DEFINITIONS.md)
- [Experiments](experiments/)
- [Tests](tests/)
- [Literature](literature/)
- [Verified results](results/verification-2026-10-11/)

## Implementations

- `exact_admission.py`: exact admission computations.
- `baseline_admission.py`: baseline admission computations.
- `certificate_verifier.py`: feasibility certificate checks.
- `multi_job_equal.py`: equal-job scheduling computations.
- `robustness.py`: timing-robustness experiments.

The results directory records the mathematical verification counts and scheduling validation outcomes. The repository's source files and evidence should be interpreted according to the assumptions and input domains documented with each experiment.