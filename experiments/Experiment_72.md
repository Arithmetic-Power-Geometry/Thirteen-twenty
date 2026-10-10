# Experiment 72 — Explicit safe time for bounded speed ratios

Date: 2026-10-10
Status: complete elementary all-dimensional existence proof for a nontrivial infinite family. Not an original universal solution.

## Theorem 72.1 (bounded-ratio witness)
Let k>=2 and 0<m=v_1<...<v_k=M be distinct positive integers (or positive real speeds). If M<=k*m, then t=1/(m+M) satisfies ||v_i*t||>=1/(k+1) for every i.

## Proof
For each i, m/(m+M)<=v_i/(m+M)<=M/(m+M). Since 0<m/(m+M)<=1/2<=M/(m+M)<1, the circular distance of any point in this interval from the nearest integer is at least m/(m+M). The ratio hypothesis gives (k+1)m>=m+M, so m/(m+M)>=1/(k+1). QED.

## Corollary 72.2 (all sufficiently high translates of a finite pattern)
For any k distinct fixed integers d_1<...<d_k, the speed family v_i=H+d_i with H+d_1>0 satisfies the conjecture whenever H+d_k<=k(H+d_1), i.e. (k-1)H>=d_k-k*d_1. The explicit witness is t=1/(2H+d_1+d_k). Thus every fixed finite additive pattern becomes provably safe under a sufficiently large positive translation, even though its short additive relations may persist or change.

## Corollary 72.3 (consecutive block)
Every k-speed consecutive block (H,H+1,...,H+k-1), H>=1, satisfies M=H+k-1<=kH and hence admits t=1/(2H+k-1). This covers infinitely many relation-bearing configurations for every k. For H=1 the witness equals 1/(k+1), the tight case.

## Sharpness of this specific witness rule
For t=1/(m+M), the minimum distance among all speeds in [m,M] equals m/(m+M), because the two endpoint speeds attain it. Therefore this particular witness meets the LRC threshold exactly when M<=k*m. This does not mean configurations with M>k*m are counterexamples or lack other witnesses.

## Research context
This is an elementary arc-containment / diameter-ratio observation, not a new mathematical result. It covers a different regime from the large-speed perturbation in Fan–Sun (2026), Lemma 13, and does not depend on positive-measure arguments. The primary source for general background is Tao (2018), Some remarks on the lonely runner conjecture, Contributions to Discrete Mathematics 13(2), DOI 10.55016/ojs/cdm.v13i2.62728; publisher metadata checked 2026-10-10. Existing BibTeX entry Tao2018 retained without duplication.

## Gap remaining
For unrestricted LRC, configurations with M>k*m and without an applicable other theorem remain unresolved. No reduction from that regime to this one has been proved. The all-dimensional statement above is a sufficient condition, not a complete proof.

## Verdict
Proved all dimensions for M<=k*m; no Q1-level novelty; unrestricted LRC UNSOLVED.
