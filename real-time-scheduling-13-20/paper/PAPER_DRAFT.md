# Exact Certification of Nonpreemptive Scheduling Under Additively Coupled Periodic Exclusions

**Research manuscript — working draft, 10 October 2026. Not approved for journal submission.**

**Mohammad Amir Khusru Akhtar**

## Abstract

We investigate finite-horizon, nonpreemptive single-machine scheduling under a structured availability calendar defined by three periodic exclusions with integer frequencies a, b, and a+b. An instant t in [0,1] is available when the distance to the nearest integer of each of at, bt, and (a+b)t is at least 1/16. We give an exact rational construction of maximal positive-length availability intervals and study single-job admission, multiple equal-duration jobs with common release and deadline, exact schedule certificates, and bounded timing jitter. The single-job decision is solved by checking the resulting intervals; for equal-duration jobs the maximum feasible count is the sum of floor-divided clipped interval lengths. For general job durations, we prove NP-completeness even when a=b=1, where the availability set consists of two equal-length intervals. Independent verification reconstructs excluded neighborhoods rather than reusing the scheduling oracle. Under common bounded time translation, robust admission reduces exactly to erosion of each available interval by the uncertainty radius. We provide reference implementations, regression tests and a continuous-integration benchmark protocol. The construction is pseudopolynomial in binary-encoded frequencies and the present empirical evaluation has not been independently completed. These results define a reproducible scheduling case study; the elementary algorithms and PARTITION reduction do not, by themselves, establish a novel algorithmic advance.

**Keywords:** real-time scheduling; periodic exclusion; exact arithmetic; nonpreemptive admission; certificate verification; robustness; complexity.

## 1. Introduction

A machine may be unavailable during periodic interference windows, maintenance cycles or resource exclusions. When several exclusion frequencies are related, the resulting feasible execution calendar has arithmetic structure. We consider three aligned constraints with frequencies a, b and a+b. Our central distinction is between the measure of all available instants and the existence of a *contiguous* interval long enough for a nonpreemptive job. A large total availability measure does not by itself imply that an individual job, or an arbitrary workload, can be admitted.

The model is a finite-horizon *availability-constrained* problem. It is not identical to pinwheel scheduling, where recurring tasks must be executed sufficiently frequently; this related field has substantial prior complexity results [JacobsLongo2014; FeinbergCurry2005; FujiwaraMiyagiOuchi2026; KanellopoulosEtAl2026]. Constrained nonpreemptive schedulability is also studied in [MayankMondal2020]. We therefore avoid claims that classical interval packing, segment trees or elementary PARTITION reductions are intrinsically novel.

The accompanying source repository supplies exact rational implementations and tests. Test success and measured performance must be reported only after inspecting archived CI results.

## 2. Availability model and exact boundaries

Let ||x|| denote distance to the nearest integer, and let

S(a,b)={t in [0,1]: ||at||>=1/16, ||bt||>=1/16, ||(a+b)t||>=1/16},

where a,b are positive integers. All three phases are aligned at t=0. Since each phase condition is closed, S(a,b) is a finite union of closed intervals and possibly isolated points. Isolated points cannot host a positive-duration job.

For each frequency v in {a,b,a+b}, changes in the phase predicate occur at (16j+1)/(16v) and (16j+15)/(16v), j=0,...,v-1. Collect these endpoints with 0 and 1, sort them, test exact rational midpoints, and merge adjacent feasible cells. This produces all maximal positive-length components [L_i,U_i]. The number of candidate boundaries is O(a+b), with O((a+b) log(a+b)) rational comparisons for sorting, plus exact predicate evaluation. These are arithmetic-operation bounds, not bit-complexity bounds.

The parent aligned-phase result motivating this application states that the safe-time measure is at least 13/20, with equality at (1,14) after normalization. That mathematical theorem requires its own complete proof and independent audit before it can be cited as an established result in a journal submission. None of the scheduling correctness arguments below relies on the sharp measure bound.

## 3. Single-job admission

For rational release r, deadline d and duration p>0 with 0<=r<=d<=1, a job is feasible exactly when some safe component satisfies

max(r,L_i)+p <= min(d,U_i).

**Proposition 1 (exact admission).** The preceding inequality is necessary and sufficient. A witness start is max(r,L_i). Necessity follows because a connected positive-duration execution interval cannot cross an excluded open gap. Sufficiency follows by direct containment.

The linear oracle scans all components. A binary-search-plus-scan implementation improves the starting position but remains O(k) worst-case. A segment-tree index over component lengths supports O(log k) exact queries after preprocessing, provided the component intersecting the release is checked separately and later components are searched by length and deadline. These are standard data-structural techniques.

## 4. Equal-duration multi-job capacity

Suppose N nonpreemptive jobs share the same rational release r, deadline d and duration p>0. Let

c_i = floor(max(0,min(U_i,d)-max(L_i,r))/p).

**Theorem 2 (exact equal-job capacity).** All N jobs can be scheduled if and only if N <= sum_i c_i.

*Proof.* Every positive-duration job must lie in one safe component. Component i can contain at most c_i nonoverlapping jobs by total occupied length. Conversely, start c_i jobs consecutively at max(L_i,r). Combining components yields exactly sum_i c_i nonoverlapping jobs. QED.

This formula is a standard interval-capacity identity. It demonstrates why a safe-time measure guarantee is not automatically a throughput guarantee: fractional remainders in separate components cannot be combined for a nonpreemptive job.

## 5. Variable-duration complexity

**Theorem 3 (weak NP-completeness at fixed frequencies).** Feasibility for an arbitrary finite list of positive rational nonpreemptive job durations, all released at 0 and due at 1, is NP-complete even with a=b=1.

*Proof.* Direct phase calculation yields exactly two safe components, [1/16,15/32] and [17/32,15/16], each of length 13/32. Given a PARTITION instance with positive integer weights w_i and even total 2B, set p_i=(13/32)(w_i/B). Total processing equals 13/16, the sum of both capacities. Because jobs cannot cross the unsafe gap, all jobs fit exactly when the weights can be divided into two groups of sum B. Restriction to even total preserves PARTITION hardness by doubling weights. Membership in NP follows from a two-bin assignment certificate whose rational sums are checked in polynomial time. QED.

The proof is a direct two-bin PARTITION reduction. It does not imply strong NP-hardness and is not claimed as a previously unknown complexity phenomenon.

## 6. Exact certificate verification

For YES instances with equal-duration jobs, a certificate lists N rational execution intervals. A separate checker validates release/deadline containment, exact durations, pairwise nonoverlap and avoidance of every forbidden periodic neighborhood. It constructs the forbidden neighborhoods directly instead of importing the reference safe-window routine.

For NO instances in this restricted model, the checker independently unions the forbidden neighborhoods, recovers all positive-length available components and recomputes the exact capacity of Theorem 2. It accepts only if the claimed capacity matches and N exceeds it. This is a recomputation-based checker, not a succinct proof system; its cost scales with the explicitly enumerated boundaries.

## 7. Phase offsets and worst-case jitter

For rational phase offsets phi_a, phi_b and phi_(a+b), replace the aligned predicate by ||vt+phi_v||>=1/16 for each v. The shifted components are constructed from exact boundary times t=(j +/- 1/16 - phi_v)/v within [0,1].

Assume an adversary may translate an entire nominal execution interval [s,s+p] by a common delta in [-epsilon,epsilon]. Actual execution must remain within [r,d] and one shifted safe component.

**Theorem 4 (robust admission).** A robust start exists exactly when some shifted safe component [L_i,U_i] satisfies

min(U_i,d)-max(L_i,r) >= p+2epsilon.

*Proof.* The union of all translated execution intervals is [s-epsilon,s+p+epsilon]. Robustness is equivalent to containment of this expanded interval in [r,d] intersected with a safe component. This is possible exactly when that intersection has length at least p+2epsilon. QED.

The 13/20 aligned-phase measure statement is not transferred to independently shifted phases. The interval-erosion identity is classical.

## 8. Reproducibility and evaluation status

The repository contains: `exact_admission.py`, `baseline_admission.py`, `multi_job_equal.py`, `certificate_verifier.py`, `robustness.py`, the test suite under `tests/`, and `experiments/cs010_benchmark.py`. The CI configuration is `.github/workflows/thirteen-twenty-cs010.yml`.

The planned benchmark evaluates five frequency pairs, 120 seeded exact rational admission queries per pair, three classical query methods, separate preprocessing time and independent YES/NO certificate checks. The benchmark records Python version, platform, random seed and source SHA-256 hashes.

**No runtime table or speedup claim is included:** successful CI logs and benchmark artifacts have not yet been inspected. The presence of a workflow file is not experimental evidence.

## 9. Discussion and limitations

The construction explicitly lists O(a+b) boundary events, so its complexity is pseudopolynomial in the binary-encoded frequency parameters. The lower-bound example in CS-006 demonstrates that explicit output can itself require Omega(b) components for some families; it does not rule out compressed implicit representations. The equal-job capacity theorem is a tractable special case, while arbitrary job sizes are NP-complete even for two fixed windows. The robustness result handles bounded common translation, not arbitrary clock drift or independent job jitter.

The principal unresolved scientific issue is priority and novelty. The scheduling components presented here are mathematically precise applications of classical interval methods to a structured arithmetic calendar. Without a new arithmetic-specific algorithmic insight, a stronger systems evaluation or a broader independently verified mathematical result, this manuscript should be treated as a working paper rather than as an established Q1-level contribution.

## 10. Conclusion

Exact rational interval construction permits deterministic nonpreemptive admission and checkable feasibility claims for a structured three-frequency exclusion calendar. Equal-duration multi-job capacity is exactly computable; variable-duration feasibility is weakly NP-complete even at fixed frequencies; and bounded translation jitter admits an exact interval-erosion test. The implementation and certificate checks provide a reproducible basis for further research. Publication readiness requires completed execution evidence, broader prior-work verification and a substantive originality assessment.

## References

[JacobsLongo2014] T. Jacobs and S. Longo. A New Perspective on the Windows Scheduling Problem. arXiv:1410.7237, 2014.

[FeinbergCurry2005] E. A. Feinberg and M. T. Curry. Generalized Pinwheel Problem. Mathematical Methods of Operations Research 62(1), 99–122, 2005. DOI:10.1007/s00186-005-0443-4.

[FujiwaraMiyagiOuchi2026] H. Fujiwara, K. Miyagi and K. Ouchi. Pinwheel Scheduling with Real Periods. Discrete Mathematics & Theoretical Computer Science 28(4), 2026. DOI:10.46298/dmtcs.17657.

[KanellopoulosEtAl2026] S. Kanellopoulos et al. Finite Pinwheel Scheduling: the k-Visits Problem. Proceedings of SODA 2026, 355–371. DOI:10.1137/1.9781611978971.16.

[MayankMondal2020] J. Mayank and A. Mondal. Polynomial Time Schedulability Test for Periodic Non-Preemptive 2-Task System. Information Processing Letters 154, 105867, 2020.

**Draft status:** complete first-pass narrative; not a journal-ready manuscript. Bibliography coverage is intentionally limited to the initially verified sources. No results, citations, figures or performance values have been fabricated.
