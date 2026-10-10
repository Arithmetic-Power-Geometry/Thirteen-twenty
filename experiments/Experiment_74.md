# Experiment 74 — Exact pair-sum optimizer and adversarial regression

Date: 2026-10-10
Status: exact finite algorithm and proof in all dimensions; NOT a solution of unrestricted LRC; classical critical-time geometry. Novelty not established.

## Theorem 74.1
For any distinct positive integer speeds v_1,...,v_k, k>=2, define F(t)=min_i ||v_i*t|| and F*=max_{t in R/Z}F(t). Then F* is attained either
(a) at t=(2h+1)/(2v_i) mod 1 for some i and integer h, or
(b) at t=n/(v_i+v_j) mod 1 for distinct i,j and integer n.
Hence F* is exactly computable by evaluating this finite rational candidate set. A rational safe witness for the k-runner threshold is a candidate with F(t)>=1/(k+1).

## Proof
F is continuous, piecewise affine, and periodic. Choose a maximizer t*. If some active function ||v_i*t*|| is at a cusp of its distance-to-integers graph, the cusp is at an integer or half-integer phase. If it is at an integer, F*=0; this is impossible because a sufficiently small positive t has every ||v_i*t||>0. Thus an active cusp is at half-integer phase, case (a).

Otherwise every active branch near t* is affine with slope +v_i or -v_i, and F is their pointwise minimum locally. If all active slopes are positive, F strictly increases to the right; if all negative, F strictly increases to the left. Thus at least one positive and one negative active slope exist. A positive slope means v_i*t* is in (n_i,n_i+1/2) and ||v_i*t*||=v_i*t*-n_i; a negative slope means v_j*t* is in (n_j-1/2,n_j) and ||v_j*t*||=n_j-v_j*t*. Equality of active values implies (v_i+v_j)*t*=n_i+n_j, case (b). QED.

## Algorithm
See experiments/experiment_74_exact.py. It enumerates half-integer cusp times and pair-sum fractions, evaluates F using Fraction and integer arithmetic, and returns a maximizing rational witness. Its arithmetic is exact and reproducible. This is a finite-instance algorithm, not a finite dimension-uniform proof: the candidate count grows with the speeds.

## Mathematical regression cases
- (1,2): maximum 1/3 at t=1/3.
- (1,2,3): maximum 1/4 at t=1/4.
- (1,3): maximum 1/2 at t=1/2 (cusp branch).
- (1,3,4): maximum at least 1/4 at t=1/4 is FALSE (speed 4 unsafe there), illustrating why every candidate must be checked against all speeds. A correct solver reports its actual optimum.

## Prior art / novelty
This finite candidate method is standard one-dimensional piecewise-linear optimization and overlaps prior critical-time/spectrum work. See Tao (2018), *Some remarks on the lonely runner conjecture*, DOI 10.55016/ojs/cdm.v13i2.62728, and Fan–Sun (2026), *Amending the Lonely Runner Spectrum Conjecture*, DOI 10.37236/13840. Both verified entries are already in references/lonely_runner.bib. No first-discovery claim.

## Research outcome
Unlike earlier ad hoc modular conditions, the algorithm is complete for EACH fixed integer speed vector and can independently audit proposed counterexamples and exact tightness. It cannot settle infinitely many vectors by finite tests without an additional bounded-counterexample theorem and complete exhaustive computation. The general Lonely Runner Conjecture is UNSOLVED.
