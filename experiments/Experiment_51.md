# Experiment 51 — Second-factorial-moment certificate in every dimension

Date: 2026-10-10
Status: proved general-dimensional sufficient condition; classical moment method, NOT a solution of the Lonely Runner Conjecture. No novel theorem claimed.

## Statement
For k>=2 distinct positive integer speeds v_1,...,v_k and 0<delta<=1/2, define B_i={t in R/Z: ||v_i*t||<delta}, X(t)=sum_i 1_{B_i}(t), and
P_2=sum_{1<=i<j<=k} mu(B_i intersect B_j).
If
2 P_2 > k(2*k*delta-1),
then there exists a time t with ||v_i*t||>=delta for all i. In fact, the safe set has positive measure.

## Proof
For integer x in {1,...,k}, (x-1)(x-k)<=0. For x=0 this product equals k. Therefore pointwise
(X-1)(X-k) <= k*1_{X=0}.
Taking expectations with t uniform on [0,1) gives
k mu(X=0) >= E[X^2]-(k+1)E[X]+k.
Since E[X]=2*k*delta and E[X^2]=E[X]+2P_2, this becomes
mu(X=0) >= 1-2*k*delta+(2/k)*P_2.
Strict positivity of the right side gives the claim. QED.

## Corollary (LRC threshold)
At delta=1/(k+1), it suffices that
P_2 > k*(k-1)/(2*(k+1)).
This is an explicit all-dimensional pairwise-correlation certificate, not a proof that the condition always holds.

## Computation and verification protocol
Each B_i is a finite union of open rational intervals on [0,1). Use exact rational endpoints and interval intersections to calculate P_2. Compare the certified bound 1-2k delta+2P_2/k to the exact safe-set measure calculated from the union of all endpoints; assert the lower bound does not exceed the exact measure. Check k=2 and k=3 examples independently. No computational run is claimed in this note.

## Novelty and literature
The polynomial second-moment inequality is classical; the certificate is not claimed as new. Relevant prior work includes Perarnau and Serra (2016), *Correlation Among Runners and Some Results on the Lonely Runner Conjecture*, Electronic Journal of Combinatorics 23(1), P1.50, DOI 10.37236/5123; Tao (2018), *Some remarks on the lonely runner conjecture*, Contributions to Discrete Mathematics 13(2), DOI 10.55016/ojs/cdm.v13i2.62728; Beck and Everett (2026), *Lonely Runner Relations*, arXiv:2609.06259. These entries already exist in references/lonely_runner.bib; avoid duplicates.

## Scope limitation
Even a bound valid in every finite dimension does not settle LRC unless it proves safe-time existence for every admissible speed vector. This experiment does not. Future work should exploit arithmetic restrictions on attainable pairwise overlaps or derive a universal positive certificate.
