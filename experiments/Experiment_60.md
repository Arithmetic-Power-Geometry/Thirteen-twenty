# Experiment 60 — Sharper divisor-free induction using safe intervals

Date: 2026-10-10
Status: mathematically proved sufficient theorem in all finite dimensions; NOT unrestricted LRC; originality NOT established.

## Theorem 60.1
Let k>=2. Suppose distinct positive integer speeds v_1,...,v_{k-1} admit t0 with ||v_i*t0||>=1/k. Put M=max_i v_i. If an additional distinct positive speed V satisfies V>=k*M, then there exists t with ||v_i*t||>=1/(k+1) for every old speed and ||V*t||>=1/(k+1).

## Proof
Set epsilon=1/(k*(k+1)*M). Since x->||x|| is 1-Lipschitz, for any |t-t0|<=epsilon and each old speed,
||v_i*t|| >= 1/k - v_i*epsilon >= 1/k - M*epsilon = 1/(k+1).
Thus the old runners are simultaneously safe throughout the closed interval I=[t0-epsilon,t0+epsilon], of length 2/(k*(k+1)*M).
The new runner's forbidden set {t: ||V*t||<1/(k+1)} is a disjoint union of open intervals, each of length 2/((k+1)*V). If all points of I were forbidden, connectedness would force I into a single forbidden component. But |I| >= 2/((k+1)*V) by V>=k*M, impossible because a closed interval of at least that length cannot lie inside a strictly shorter-or-equal open interval. Hence I contains a time safe for the new runner, and all old runners remain safe there. QED.

## Corollary 60.2 (inductive lacunary family)
For increasing positive integer speeds v_1<...<v_k, if v_j>=j*v_{j-1} for each j=2,...,k, then LRC holds for all k moving speeds. Start with one runner, whose safe time is t=1/(2*v_1). At extension from j-1 to j speeds apply Theorem 60.1 with k=j.

## Improvement over Experiment 59
Experiment 59 requires V>=k*(k+1)*M/2; the new condition V>=k*M improves the threshold by factor (k+1)/2. The method uses the entire robust safe interval rather than forcing the new runner to a half-integer phase.

## Example
The speeds (1,2,6,24) satisfy v_2>=2*v_1, v_3>=3*v_2, v_4>=4*v_3, and are certified inductively.

## Novelty/prior-art caution
The argument is elementary. Speed separation, perturbation, and reduction arguments have significant prior art; no priority or Q1 novelty is asserted without theorem-level comparison. Verified relevant published sources:
- Romanos Diogenes Malikiosis, Francisco Santos, Matthias Schymura (2025), Linearly-exponential checking is enough for the lonely runner conjecture and some of its variants, Forum of Mathematics, Sigma 13, e164, DOI 10.1017/fms.2025.10107 (publisher).
- Vikram Giri and Noah Kravitz (2025), The structure of Lonely Runner spectra, Mathematical Proceedings of the Cambridge Philosophical Society, DOI 10.1017/S0305004125101497 (publisher).
These already appear in references/lonely_runner.bib. Do not duplicate.

## Research gate
A universal LRC proof would require handling all remaining configurations with V<k*M, not just those meeting the speed separation hypothesis. The current theorem does not establish that.
