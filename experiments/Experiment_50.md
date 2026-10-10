# Experiment 50 — Third-order Bonferroni certificate and prior-art correction

Date: 2026-10-10
Status: rigorous arbitrary-dimensional sufficient condition; NOT an unrestricted Lonely Runner Conjecture proof. Classical inclusion-exclusion; novelty not claimed.

## Prior-art correction (important)
Experiment 49's spanning-tree bound is precisely the classical Hunter/Bonferroni inequality already used for the Lonely Runner Conjecture in Lemma 13 of Perarnau and Serra (2016), *Correlation Among Runners and Some Results on the Lonely Runner Conjecture*, Electronic Journal of Combinatorics 23(1), P1.50, DOI 10.37236/5123. Do not describe Experiment 49 as a new theorem or publishable novelty. Primary publisher PDF: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v23i1p50/pdf/

## Theorem 50.1 (third-order Bonferroni bound)
Let k>=1, 0<delta<=1/2, and nonzero integer speeds v_1,...,v_k. Define B_i={t mod 1: ||v_i t||<delta}. Then
mu(intersection_i B_i^c) >= 1 - 2*k*delta + sum_{i<j} mu(B_i intersection B_j) - sum_{i<j<l} mu(B_i intersection B_j intersection B_l).

## Proof
At each t, let m be the number of forbidden sets B_i containing t. The right-side pointwise expression is
1-m+binom(m,2)-binom(m,3).
For m=0 it equals 1. For m>=1 it equals -binom(m-1,3), using 1-m+binom(m,2)-binom(m,3) = -binom(m-1,3), with binom(n,3)=0 for n<3. Thus it is <= 0 = 1_{m=0}. Integrate, and use mu(B_i)=2delta. QED.

## Corollary 50.2 (strict certificate at LRC threshold)
At delta=1/(k+1), if
sum_{i<j} mu(B_i intersect B_j) - sum_{i<j<l} mu(B_i intersect B_j intersect B_l) > (k-1)/(k+1),
then a simultaneous safe time exists, indeed the safe-time set has positive measure.

## Warning
The inequality is classical and may be weak or negative. It is not known from this experiment that the sufficient condition holds for all distinct speeds. Exact computation of overlaps for individual vectors is an instance certificate, not a universal proof. At equality the bound alone cannot certify existence.

## Experiment protocol
1. Normalize integer speeds by their gcd.
2. Compute each B_i as a finite union of rational open intervals on [0,1), handling periodic wrap.
3. Calculate all pairwise and triple intersections using exact rational interval arithmetic.
4. Check the displayed inequality; report a positive bound only when strict.
5. Independently compute the exact safe-time set from the union of interval endpoints for sampled vectors; check the lower bound does not exceed its actual measure.
6. Record failing cases as inconclusive, not counterexamples.

## Literature verification
Perarnau, Guillem and Serra, Oriol (2016), *Correlation Among Runners and Some Results on the Lonely Runner Conjecture*, The Electronic Journal of Combinatorics 23(1), P1.50, DOI 10.37236/5123. Publisher article and primary PDF inspected on 2026-10-10; Lemma 13 contains the tree inequality used in Experiment 49. Existing BibTeX key: PerarnauSerra2016 in references/lonely_runner.bib. No duplicate bibliography entry needed.

## Novelty verdict
The third-order inequality is standard inclusion-exclusion (Bonferroni). Experiment 50 is a validated methodological baseline, not an original solution or standalone Q1 contribution. The general LRC remains open in this work.
