# CS-004 — Classical exact admission baselines

Status: implementation and deterministic differential tests provided. Execution environment and performance evidence must be recorded separately.

## Baselines

1. Linear scan of maximal safe intervals: O(k) comparisons per query.
2. Sorted right endpoints + binary search: O(log k) comparisons per query after O(k) storage/preprocessing.
3. AdmissionIndex: same classical binary-search method, with endpoints cached across queries.

The safe-window construction itself uses O((a+b)log(a+b)) rational comparisons and O(a+b) space, where k <= O(a+b). These are arithmetic-operation bounds and are pseudopolynomial for binary-encoded frequencies. Do not claim any of these methods are original.

## Proof of binary query

For release r and processing p>0, any feasible safe interval [L,U] must satisfy U >= r+p. Right endpoints of disjoint ordered intervals are strictly increasing. Let [L*,U*] be the first with U* >= r+p. If this interval has L* > d-p, then every later interval has L >= L* > d-p and cannot fit the deadline. Otherwise s=max(r,L*) is feasible provided s+p <= min(U*,d). Thus checking the first candidate is sufficient. Exact endpoints mean no floating-point tolerance.

## Testing protocol

Run `python3 -m unittest discover -s tests -v`. Differential tests compare all three baselines against the reference exact oracle on small frequency pairs and rational task grids; also test maximal window lengths and invalid inputs.

## Next milestone

Measure preprocessing separately from repeated-query latency, memory and proof-check time. Use increasing a+b, normalized coprime pairs, adversarial tight deadlines and job-duration distributions. Record raw results and hashes. Then look for **special arithmetic structure** yielding more than standard binary search or a general scheduling result.
