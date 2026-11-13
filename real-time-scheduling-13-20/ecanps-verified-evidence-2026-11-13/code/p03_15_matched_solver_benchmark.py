"""P03-15: matched exact-DP versus CP-SAT benchmark, deterministic tiny cases.

Reports end-to-end wall time (including model construction) and proven optimum.
Not a scalability or speedup claim: instances are intentionally small.
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
    rows=[]
    for a,b in ((1,1),(1,14),(2,3)):
        iv=components(a,b)
        for n in (3,5,7):
            for replicate in range(3):
                jobs=[]
                for _ in range(n):
                    r=F(rng.randrange(17),16)
                    d=F(rng.randrange(17),16)
                    if r>d: r,d=d,r
                    p=F(rng.randrange(1,9),32)
                    w=F(rng.randrange(1,11))
                    jobs.append((r,p,d,w))
                t0=perf_counter()
                dp=exact_opt(iv,jobs)
                dp_seconds=perf_counter()-t0
                t0=perf_counter()
                cp=cpsat_opt(iv,jobs)
                cp_seconds=perf_counter()-t0
                assert dp==cp,(a,b,n,replicate,dp,cp)
                rows.append((dp_seconds,cp_seconds))
    dp_median=median(r[0] for r in rows)
    cp_median=median(r[1] for r in rows)
    print(f"PASS: {len(rows)} matched exact-DP vs proven CP-SAT optima; zero mismatches")
    print(f"OBSERVED: dp_median_seconds={dp_median:.6f}; "
          f"cpsat_median_seconds={cp_median:.6f}; "
          "includes Python invocation and model construction; tiny synthetic cases")
    print("LIMIT: not a scalability, solver superiority, or novelty claim")

if __name__=="__main__":
    run()
