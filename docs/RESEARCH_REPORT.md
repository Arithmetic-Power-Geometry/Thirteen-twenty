# Experiment 25 — Sharp measure inequality for additive triples
Date: 2026-10-10

**Claim:** For all positive integers a,b, letting ||x|| be the distance to the nearest integer,
`F(a,b) = measure{t in [0,1] : ||at||, ||bt||, ||(a+b)t|| >= 1/16} >= 13/20`.
The bound is sharp at (a,b)=(1,14).

**Status:** Analytic reduction plus a finite exact-arithmetic certificate. Full independent reproduction and literature novelty review remain pending.

## Proof
Scaling gives F(da,db)=F(a,b), so assume gcd(a,b)=1. On the two-torus let A={||x||>=1/16} and H(x,y)=1_A(x)1_A(y)1_A(x+y).

Three forbidden strips have measure 1/8 each. Their pairwise intersections have measure 1/64 each; the triple intersection has measure 3/256. Inclusion–exclusion yields integral H = 169/256.

Write t=(k+x)/b with 0<=k<b, 0<=x<1. Then
`F(a,b)=(1/b) integral_0^1 sum_{k=0}^{b-1} H({a(k+x)/b},x) dx`.
As gcd(a,b)=1, k runs through a rotated equispaced b-point grid for each x. At fixed x, the first-coordinate allowed set A intersect (A-x) is the intersection of two circular arcs, a union of at most two connected arcs. Grid-count discrepancy is at most 1/b per arc, giving
`|F(a,b)-169/256| <= 2/b`.
Swap a,b to obtain `|F(a,b)-169/256| <= 2/max(a,b)`.

Since `169/256 - 13/20 = 13/1280`, this implies F(a,b)>=13/20 for max(a,b)>=197.

## Exact finite certificate
For the remaining coprime pairs 1<=a<=b<=196, use D=16ab(a+b). All boundary times have integer coordinates in [0,D], namely `(16j+1)*D/(16v)` and `(16j+15)*D/(16v)`, v in {a,b,a+b}, j=0,..,v-1. Sort boundaries, test one midpoint per open interval using integer modular arithmetic, and sum safe lengths N. Verify `20N>=13D`.

There are 11,698 coprime ordered pairs in this range. The exact certificate reports zero violations, and only (1,14) reaches equality, with N/D=2184/3360.

## Caution
A finite verified computation and classical interval discrepancy are not a proof of research originality. No claim that this solves the general 16-runner problem is made.

## Closest prior directions
- Perarnau and Serra (2016), correlation among runners, DOI 10.37236/5123.
- Giri and Kravitz (2025), Lonely Runner spectra.
- Beck and Everett (2026), Lonely Runner Relations, arXiv:2609.06259.
Check each relevant full theorem, not merely search snippets.

## Next experiment
General thresholds delta; higher-order speed relations; intersection estimates with arbitrary additional runners.