# Experiment 91 — Exact overlap-excess certificate

For k distinct positive speeds, put q=k+1, L=lcm(speeds), M=qL. For each grid index j, let b(j) count the speeds with ||v*j/M||<1/q. Define G as the number of indices with b(j)=0, P=sum_j b(j)(b(j)-1)/2, and E=sum_j max(b(j)-1,0).

## Theorem 1
G = sum(v) - (k-1)*L + E.

Proof: each speed v forbids 2L-v grid indices, so sum_j b(j)=2kL-sum(v). Since the indicator b(j)>0 equals b(j)-max(b(j)-1,0), the number of covered indices equals 2kL-sum(v)-E. Subtract from M=(k+1)L.

## Theorem 2
G >= sum(v)-(k-1)L+2P/k. In particular, k*sum(v)+2P > k*(k-1)*L implies G>0 and a safe time exists.

Proof: b(b-1)/2 <= k*max(b-1,0)/2 for every integer 0<=b<=k. Sum over indices, then apply Theorem 1.

## Exact bounded checks
Executed 1139 primitive vectors: k=3 speeds <=15 (409), k=4 <=12 (479), k=5 <=10 (251). The pairwise criterion newly certified 357, 16, and 0 vectors, respectively, compared with the baseline sum(v)>(k-1)L. All 1139 have G>0. Example (1,2,3): L=6,M=24,G=2,P=11,E=8. Example (1,2,3,6): L=6,M=30,G=8,P=19,E=14.

## Priority and limitations
This is an elementary counting identity and inequality, not a claim of independent novelty. It does not prove the unrestricted conjecture and is not established Q1-journal-level mathematics. Compare Malikiosis–Santos–Schymura (2025), DOI 10.1017/fms.2025.10107, and Giri–Kravitz (2026), DOI 10.1017/S0305004125101497. Both are already in the master bibliography.
