# Experiment 48 — Universal first-moment certificate and a sharp obstruction to the union bound

Date: 2026-10-10
Status: proved elementary general-dimensional sufficient condition; not a solution of the Lonely Runner Conjecture. Novelty unverified; likely classical.

## Setup
Let v_1,...,v_k be nonzero integers, and 0<delta<=1/2. Write B_i={t in [0,1): ||v_i t||<delta}. Let S=[0,1)\(union_i B_i).

## Theorem 48.1 (uniform measure lower bound)
mu(S)>=max(0,1-2*k*delta).

### Proof
For any nonzero integer v, multiplication t->vt modulo 1 preserves Lebesgue measure, so mu(B_i)=2delta. Subadditivity gives mu(union_i B_i)<=2k delta. Therefore mu(S)>=1-2k delta; nonnegativity finishes the proof. QED.

## Corollary
If delta<1/(2k), the simultaneous safe-time set has positive measure for arbitrary nonzero integer speeds. At delta=1/(2k), it is nonempty as well: S is closed (intersection of complements of open sets), and the same inequality forces only mu(S)>=0, not existence. Existence at equality DOES NOT follow from this argument and is NOT claimed.

## Obstruction at the Lonely Runner threshold
At delta=1/(k+1), the bound is 1-2k/(k+1)=(1-k)/(k+1), negative for k>1. Hence the first-moment union bound cannot establish LRC in general. One needs overlap/correlation information or a different certificate.

## Independent exact check
For k=2, V=(1,2), delta=1/4, safe t=1/4 satisfies both distances >=1/4. This example is a sanity check only; it does not validate a universal stronger bound.

## Novelty
Measure preservation and the union bound are standard. The theorem is recorded as a baseline and obstruction, not a novel research result.

## Literature (primary metadata checked)
Perarnau and Serra (2016), Correlation Among Runners and Some Results on the Lonely Runner Conjecture, Electronic Journal of Combinatorics 23(1), P1.50, DOI 10.37236/5123.
Perarnau and Serra (2025), The Lonely Runner Conjecture turns 60, Computer Science Review 58, 100798, DOI 10.1016/j.cosrev.2025.100798.
Beck and Everett (2026), Lonely Runner Relations, arXiv:2609.06259 (preprint).

## Next research gate
Find a rigorously quantified overlap gain sufficient to overcome the deficit of the union bound for all k and all speed vectors. Do not infer a universal result from sampled speed families.
