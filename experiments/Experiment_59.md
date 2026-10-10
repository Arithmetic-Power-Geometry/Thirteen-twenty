# Experiment 59 — Divisor-free high-speed extension theorem

Date: 2026-10-10
Status: proved conditional induction in every finite dimension; novelty NOT established; unrestricted LRC NOT solved.

## Theorem 59.1 (high-speed extension)
Let k>=2. Let v_1,...,v_{k-1} be distinct positive integers, M=max_i v_i, and suppose there exists t0 with ||v_i t0||>=1/k for all i. If V is an additional positive integer speed satisfying V>=k(k+1)M/2, then there exists t with ||v_i t||>=1/(k+1) for all original speeds and ||Vt||>=1/(k+1).

## Proof
Choose an integer n such that t=(n+1/2)/V is nearest to t0 on the real line. Since these half-integer-phase times are spaced by 1/V, |t-t0|<=1/(2V). The function x->||x|| is 1-Lipschitz, so ||v_i t||>=||v_i t0||-v_i|t-t0|>=1/k-M/(2V)>=1/(k+1). The new runner satisfies ||Vt||=1/2>=1/(k+1). QED.

## Corollary 59.2 (lacunary infinite families)
Let 1<=v_1<...<v_k be integers such that for every j=2,...,k, v_j>=j(j+1)v_{j-1}/2. Then the LRC holds for all k moving speeds. Proof: for j=1 choose t=1/(2v_1), yielding distance 1/2. Apply Theorem 59.1 successively with the prior j-1 speeds and the new speed v_j, noting the maximum old speed is v_{j-1}. QED.

## Example
V=(1,3,18,180): step j=2 requires 3>=3; j=3 requires 18>=6*3; j=4 requires 180>=10*18. Thus the four-speed instance is certified without exhaustive search.

## Why it is not a solution
Most speed vectors are not lacunary and do not satisfy the separation hypothesis. The theorem depends on the lower-dimensional instance and only handles sufficiently large new speeds. This is a valid conditional reduction, not a universal induction.

## Novelty audit and literature
The Lipschitz perturbation and half-integer phase trick are elementary; no originality is claimed. Closely related established finite-reduction and structural approaches:
- Malikiosis, Romanos Diogenes; Santos, Francisco; Schymura, Matthias (2025), Linearly exponential checking is enough for the lonely runner conjecture and some of its variants, Forum of Mathematics, Sigma 13, e164, DOI 10.1017/fms.2025.10107 (publisher verified).
- Beck, Matthias; Everett, Samuel (2026), Lonely Runner Relations, arXiv:2609.06259 (primary arXiv verified).
Both records already occur in references/lonely_runner.bib. No duplicate reference is warranted.

## Research gate
To solve unrestricted LRC, eliminate the growth requirement or combine this lemma with a proof for every remaining bounded-ratio configuration. Neither has been achieved.
