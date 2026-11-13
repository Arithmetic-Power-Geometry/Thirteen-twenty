"""P03-16: stratified larger matched exact-DP/CP-SAT evaluation.

Correctness and descriptive timing only: DP has no hard wall-clock cap.
CP-SAT must prove OPTIMAL within its existing 15-second cap.
"""
from fractions import Fraction as F
from random import Random
from statistics import median
from time import perf_counter

from p03_06_indexed_implicit_query import components
from p03_12_exact_weighted_scheduling import exact_opt
from p03_14_cpsat_independent import cpsat_opt

def run():
    rng=Random(20261113)
    for a,b in ((1,1),(1,14),(2,3)):
        iv=components(a,b)
        for n in (8,10,12):
            dptimes=[]
            cptimes=[]
            for replicate in range(3):
                jobs=[]
                for j in range(n):
                    r=F(rng.randrange(17),16)
                    d=F(rng.randrange(17),16)
                    if r>d:r,d=d,r
                    p=F(rng.randrange(1,9),32)
                    w=F(rng.randrange(1,11))
                    jobs.append((r,p,d,w))
                t=perf_counter()
                dp=exact_opt(iv,jobs)
                dptimes.append(perf_counter()-t)
                t=perf_counter()
                cp=cpsat_opt(iv,jobs)
                cptimes.append(perf_counter()-t)
                assert dp==cp,(a,b,n,replicate,dp,cp)
            print(f"PASS: calendar={a},{b} n={n} cases=3 "
                  f"dp_median_seconds={median(dptimes):.6f} "
                  f"cpsat_median_seconds={median(cptimes):.6f} zero_mismatches")
    print("PASS: 27 stratified exact matches; no claim of equal time budgets")

if __name__=="__main__":
    run()
