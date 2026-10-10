# Experiment 75 — Exact exhaustive audit and a nonconsecutive tight four-speed configuration

Date: 2026-10-10
Status: executed finite computation, with exact Fraction arithmetic. General LRC remains open.

## Reproducible algorithm
File: experiments/experiment_75_exact_audit.py. Enumerate strictly increasing k-tuples in [1,N] with gcd 1. For each tuple calculate the exact global maximum of min_i ||v_i*t|| over t mod 1 using the finite critical-time set:
- t=n/(v_i+v_j) for each i<j, 0<=n<v_i+v_j;
- t=(2h+1)/(2v_i) for 0<=h<v_i.
The proof of completeness is in Experiment 74. All values and comparisons are exact rational numbers; no floating-point tolerance.

## Executed results (2026-10-10)
Command: python experiments/experiment_75_exact_audit.py
k=3, N=15: 409 primitive tuples checked, 1 tight tuple, 0 violations.
Tight: (1,2,3).
k=4, N=12: 479 primitive tuples checked, 2 tight tuples, 0 violations.
Tight: (1,2,3,4) and (1,3,4,7).
The search excludes nonprimitive vectors, which are equivalent under positive common scaling of all speeds.

## Exact tight nonconsecutive witness
For (1,3,4,7), t=1/5 gives distances 1/5,2/5,1/5,2/5. The exhaustive exact optimizer returns maximum 1/5. The family has short relations 1+3=4 and 3+4=7, demonstrating that relation-bearing nonconsecutive configurations can be tight.

## Mathematical conclusion and limitations
These finite data are reproducible evidence, not a theorem about unbounded speeds. The finite optimizer is a known piecewise-linear critical-time method, and tight nonconsecutive examples have precedent in the literature. No independent priority claim is made for the specific tuple until a source-by-source comparison is completed.
In particular, absence of violations for k=4, N<=12 does not prove the conjecture for all four-speed tuples (though the four-speed case is independently known from prior literature). This is a regression/audit experiment rather than a Q1-level mathematical breakthrough.

## Literature
- Tao, Terence (2018), Some remarks on the lonely runner conjecture, Contributions to Discrete Mathematics 13(2), DOI 10.55016/ojs/cdm.v13i2.62728.
- Malikiosis, Romanos Diogenes; Santos, Francisco; Schymura, Matthias (2025), Linearly exponential checking is enough for the lonely runner conjecture and some of its variants, Forum of Mathematics, Sigma 13, e164.
- Perarnau, Guillem; Serra, Oriol (2025), The Lonely Runner Conjecture turns 60, Communications in Mathematics and Statistics survey preprint arXiv:2409.20160.
All are already present in references/lonely_runner.bib. No unverified new BibTeX records were appended.

## Research verdict
Verified bounded experiment; discovered a nonconsecutive tight example within the audit; no novel general theorem and NO solution of unrestricted LRC.
