# CS-004 — Correct classical exact admission baselines

**Status:** code and tests committed; runtime benchmarks and independent execution pending.

## Algorithms

1. `linear_query`: O(k) worst-case scan of k maximal safe intervals.
2. `binary_query`: binary-search first interval whose right endpoint >= r+p, then scan later windows; O(log k + k) worst-case.
3. `AdmissionIndex`: segment tree storing each safe-window length, binary searches by right and left endpoints, then leftmost length-eligible range query; O(k) additional storage/build and O(log k) worst-case per query. Classical data structure, **not novel**.

### Why right-endpoint binary search alone is insufficient

The first window with U>=r+p may be shorter than p, while a later window fits. Returning NO after testing only the first window is incorrect. The implementation explicitly checks later windows. This is a crucial adversarial test and a reason to insist on differential testing.

## Correctness argument for AdmissionIndex

Let i be the first window with U_i>=r+p. Earlier windows cannot contain [s,s+p] for any s>=r. If i fits within deadline, return max(r,L_i). Otherwise, any feasible later window j>i must have L_j<=d-p and length U_j-L_j>=p. Conversely, every later window satisfying both inequalities admits a task starting at L_j (which is >=r because intervals are disjoint and j>i). The binary search computes the allowed prefix of later windows and the segment tree returns its earliest member of length >=p. This is sound and complete.

## Complexity

Window extraction O((a+b)log(a+b)) rational comparisons; k=O(a+b). Index construction O(k), indexed query O(log k) exact comparisons, plus bit-arithmetic costs. Since frequencies are binary-encoded, preprocessing is pseudopolynomial. These are existing techniques, not a Q1-level breakthrough.

## Reproduce

```bash
python3 -m unittest discover -s tests -v
```

Tested logically by differential-test design, but this report does not claim tests have executed. Follow-up: record execution outputs and benchmark latency, memory, preprocessing, certificate sizes and scaling.
