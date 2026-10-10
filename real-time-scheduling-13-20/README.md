# Certified Real-Time Scheduling from the Sharp 13/20 Bound

**Status:** research plan, not a completed algorithmic breakthrough or Q1 acceptance claim. Initiated 10 October 2026.

This independent computer-science workstream uses the fixed additive-triple safe-time theorem from the parent repository. It studies provable nonpreemptive task admission, combinatorial scheduling, and machine-checkable feasibility / infeasibility evidence.

## Mathematical foundation

For positive integers a,b, let c=a+b and S(a,b)={t in [0,1]: ||at||,||bt||,||ct|| >= 1/16}. The parent research reports that the measure of S is at least 13/20, sharply at primitive (1,14), supported by an analytic finite reduction and exact enumeration. Revalidate the parent proof/certificates independently; do not claim this solves unrestricted lonely runners. The 13/20 measure is not a 65% throughput guarantee, a deadline guarantee, or a 65%-long contiguous slot.

## Computer science question

Given exact rational frequencies and job descriptions (release time r, deadline d, processing time p, preemption policy), decide and certify feasibility of one or multiple nonpreemptive jobs whose execution intervals must lie inside S. Find a structurally new algorithm, complexity theorem, lower bound, robust variant, or certificate-compression result beyond conventional sorted-interval scanning, interval scheduling and constraint programming.

## Folder guide

- [Q1 research blueprint](Q1_PAPER_BLUEPRINT.md)
- [Formal computational problems](FORMAL_PROBLEM_DEFINITIONS.md)
- [Experiment and artifact register](EXPERIMENT_REGISTER.md)
- [Novelty, correctness and submission gates](NOVELTY_AND_VERIFICATION_GATES.md)
- [Paper outline](PAPER_OUTLINE.md)

## Rules

1. Hold exclusion threshold fixed at 1/16; do not need an all-q proof.
2. Distinguish existing mathematical facts, elementary corollaries, conjectures, algorithms under investigation and measured experimental outcomes.
3. Exact arithmetic for decisions, independently verifiable certificates and reproducible code/data.
4. Compare against existing algorithmic baselines. Do not describe classical interval sorting as novel.
5. Software produces artifacts and evidence; paper writing is downstream and separate.
6. No guaranteed acceptance, Q1 status, or novelty without independent verification.
