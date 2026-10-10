# CS-001 / CS-002 / CS-003 — Exact reference admission oracle

**Status:** source and deterministic tests committed; full external execution and independent cross-language verification still pending.

## Implemented

- Exact rational safe-window extraction for aligned integer frequencies a,b,a+b at threshold 1/16.
- Exact measure computation by summing disjoint positive-length windows.
- One-job nonpreemptive admission with release/deadline/duration, returning a rational YES witness or complete safe-window list for NO.
- YES verifier; NO verifier that independently reconstructs windows (not a compact certificate).
- Regression checks for sharp pair (1,14), small-range 13/20 lower bound, gcd scaling, midpoint validity, feasible and infeasible tasks.

## How to run

From this folder:

```bash
python3 exact_admission.py 1 14 0 1 1/100
python3 -m unittest discover -s tests -v
```

## Proof sketch for positive-duration one-job admission

Every eligibility predicate changes only at exact rational boundaries t=(j+1/16)/v or (j+15/16)/v. Each open cell has constant feasibility; an exact midpoint decides it. Adjacent feasible cells are merged, giving maximal positive-length eligible windows. An execution interval of positive length is feasible iff it is contained in one such window. For each window [L,U], the earliest start respecting release is max(r,L); this is feasible iff max(r,L)+p <= min(d,U). Exhausting windows yields a complete NO decision.

## Complexity and limitations

There are O(a+b) rational boundaries. Sorting takes O((a+b)log(a+b)) rational comparisons; the scan takes O(a+b) exact arithmetic operations. With binary-encoded a,b this is pseudopolynomial. Python Fraction arithmetic is exact but not optimized. Complete-window NO certificates are linear in the explicit boundary count; no succinct complexity result has been proved. Endpoint-only feasible instants are irrelevant for positive-duration tasks. No multi-job solver or algorithmic breakthrough is claimed.

## Independent verification still required

1. Execute the committed tests in a pinned environment and archive stdout, Python version, machine information and SHA-256.
2. Compare against parent C++ checker for broad coprime pairs, including (1,14).
3. Build a structurally independent union-of-forbidden-interval oracle.
4. Add adversarial edge tests and a verified test-data CSV.
5. Complete CS-004 baselines and prove a genuinely new result before claiming Q1 novelty.
