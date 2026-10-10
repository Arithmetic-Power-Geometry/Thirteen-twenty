# CS-009 — Exact phase shifts and worst-case timing jitter

**Status:** mathematical model, exact solver and tests committed; independent execution/benchmarks pending. No claim that the 13/20 lower bound survives arbitrary independent phase offsets.

## Model

For frequencies v in {a,b,a+b}, define shifted safety by ||vt+phi_v|| >= 1/16 with independently specified rational phases phi_v. An execution interval is feasible only when every instant is safe. A nominal start s has common adversarial translation delta in [-epsilon,epsilon]; the actual interval is [s+delta,s+p+delta], and must remain inside the real release/deadline [r,d] and the safe set.

## Exact robust admission theorem

Let [L_i,U_i] denote maximal positive-length safe intervals for the shifted model. For p>0 and epsilon>=0, a robust nominal start exists iff there is some i such that

max(L_i,r)+2*epsilon+p <= min(U_i,d).

A valid nominal start is s=max(L_i,r)+epsilon.

### Proof

For all delta in [-epsilon,epsilon], the union of translated execution intervals equals [s-epsilon,s+p+epsilon]. The robust condition is equivalent to containment of this expanded interval in one safe component and [r,d]. This is possible exactly when the intersection of that component and [r,d] has length at least p+2epsilon. The formula and constructive start follow.

## Exact construction

For each v and phase phi_v, safety changes at t=(k +/- 1/16 - phi_v)/v inside (0,1). Sort exact rational boundaries, test one midpoint per open cell, merge adjacent feasible cells. Isolated safe points are immaterial for positive-duration jobs. No floating-point tolerance is used.

## Consequences

1. Robust feasibility is monotone nonincreasing in epsilon for fixed instance.
2. Each safe component loses 2epsilon of effective usable length, clipped at zero.
3. When phases are all zero and epsilon=0, this reduces to the original reference oracle.
4. The parent sharp 13/20 measure bound was established only for aligned phases; independent phase offsets change the mathematical problem. Do not transfer that bound without a separate proof.
5. The robust admission formula is standard interval erosion, not established original novelty.

## Reproduce

From folder root: `python3 -m unittest discover -s tests -v`.

## Limitations

Rational phases only; common adversarial time translation, not independent per-job jitter or drift. No probabilistic robustness, arbitrary-duration multi-job result, or Q1 novelty demonstrated. Phase-boundary enumeration is pseudopolynomial in frequencies and in the naive k-range implementation may also depend on phase numerator magnitude.
