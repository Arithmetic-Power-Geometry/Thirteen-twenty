# Experiment 62 — Quantitative safe-set overlap via periodic discrepancy

Date: 2026-10-10
Status: proved an all-dimensional quantitative inequality. This is a classical bounded-variation/discrepancy mechanism; no originality or unrestricted LRC claim.

## Setup
Fix k>=2, q=k+1 and k-1 distinct positive integer speeds A. Put delta=1/q and let S={t in R/Z: ||a*t||>=delta for all a in A}. Suppose S is a finite union of c disjoint closed arcs of positive length, allowing singleton components separately; let s=mu(S)>0. Let V be a further distinct positive integer speed.

## Theorem 62.1 (quantitative overlap)
mu({t in S: ||V*t||>=delta}) >= (1-2*delta)*s - (2*delta*(1-2*delta)*c)/V.
Consequently, if V>2*delta*c/s, the k-speed configuration has a positive-measure safe set.

## Proof
Let g(x)=1_{||x||>=delta}-(1-2*delta), a one-periodic function of mean zero. A primitive G(x)=integral_0^x g(u)du has oscillation (maximum minus minimum) equal to 2*delta*(1-2*delta): on the forbidden central arc g=-(1-2*delta), and on the allowed complementary arc g=2*delta. For any real interval [a,b], integration and periodicity give
integral_a^b g(V*t)dt=[G(V*b)-G(V*a)]/V,
whose absolute value is at most 2*delta*(1-2*delta)/V.
Sum this bound over the c positive-length arc components of S, using periodic lifts. The total integral of 1_{||Vt||>=delta} over S is at least (1-2*delta)*s - 2*delta*(1-2*delta)*c/V. If V>2*delta*c/s this is strictly positive, proving the consequence. QED.

## Boundary caution
This theorem only guarantees a positive-measure witness under its strict inequality. It cannot detect isolated safe points, which have s=0. It is NOT an unconditional solution to the conjecture.

## Why this differs from Experiment 61
Experiment 61 proves existence from one long safe component. Experiment 62 supplies a quantitative LOWER BOUND ON THE MEASURE of all k-speed safe times, using the entire old safe set and its component count. The sufficient inequality V>2*c/(q*s) is generally no stronger than the longest-component criterion, because the longest component has length >=s/c. Thus this is a different quantitative conclusion, NOT a stronger universal existence theorem.

## Checkable example
Take k=3, q=4, A={1,3}, V=4. The safe set S has two components [1/4,5/12] and [7/12,3/4], each length 1/6, so s=1/3 and c=2. The bound gives (1/2)*(1/3) - (1/4)*2/4 = 1/24 > 0. The actual three-speed safe set has positive measure; t=5/12 is an explicit witness.

## Literature and priority
- Terence Tao (2018), Some remarks on the lonely runner conjecture, Contributions to Discrete Mathematics 13(2), DOI 10.55016/ojs/cdm.v13i2.62728. Publisher verified. Existing bibliography entry should be reused.
- Guillem Perarnau and Oriol Serra (2025), The Lonely Runner Conjecture turns 60, Computer Science Review 58, 100798, DOI 10.1016/j.cosrev.2025.100798. Publisher verified. Existing bibliography entry should be reused.
The interval-discrepancy calculation is standard and must not be presented as new without a specific prior-art exclusion.

## Verdict
A rigorously proved all-dimensional quantitative measure bound; no universal existence, no established Q1 novelty, no solution of unrestricted LRC. Next genuine hurdle: derive a universal lower bound on s/c, or a different certificate that also handles zero-measure tight instances.
