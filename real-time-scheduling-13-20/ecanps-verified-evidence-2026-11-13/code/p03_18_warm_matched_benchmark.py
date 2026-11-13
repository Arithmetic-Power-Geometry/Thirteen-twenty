"""P03-18: paired in-process warm benchmark with objective verification.

Both algorithms run on identical instances after imports; CP-SAT model-build
and solve are included, while interpreter startup is excluded. A pilot study,
not a statistically powered performance or novelty claim.
"""
from fractions import Fraction as F
from random import Random
from statistics import median
from time import perf_counter

from p03_06_indexed_implicit_query import components
from p03_12_exact_weighted_scheduling import exact_opt
from p03_14_cpsat_independent import cpsat_opt

def generate(a,b,n,seed):
    rng=Random(seed)
    jobs=[]
    for _ in range(n):
        r=F(rng.randrange(17),16)
        d=F(rng.randrange(17),16)
        if r>d:r,d=d,r
        p=F(rng.randrange(1,9),32)
        w=F(rng.randrange(1,11))
        jobs.append((r,p,d,w))
    return components(a,b),jobs

def run():
    # Warm imports and solver initialization on a distinct case.
    warm=generate(1,1,2,1)
    assert exact_opt(*warm)==cpsat_opt(*warm)
    records=[]
    for a,b in ((1,1),(1,14),(2,3)):
        for n in (8,12,16):
            times={"dp":[],"cpsat":[]}
            for replicate in range(5):
                intervals,jobs=generate(a,b,n,20261113+10000*a+100*b+10*n+replicate)
                # Alternate ordering to reduce consistent first-run advantage.
                order=("dp","cpsat") if replicate%2==0 else ("cpsat","dp")
                outputs={}
                for name in order:
                    start=perf_counter()
                    outputs[name]=(exact_opt(intervals,jobs) if name=="dp"
                                   else cpsat_opt(intervals,jobs))
                    times[name].append(perf_counter()-start)
                assert outputs["dp"]==outputs["cpsat"],(a,b,n,replicate,outputs)
            row=(a,b,n,median(times["dp"]),median(times["cpsat"]))
            records.append(row)
            print(f"STRATUM a={a} b={b} n={n} repetitions=5 "
                  f"dp_median_s={row[3]:.6f} cpsat_median_s={row[4]:.6f} "
                  "zero_mismatches",flush=True)
    print(f"PASS: {len(records)*5} matched warm-process optima; "
          "zero mismatches; no solver-superiority claim",flush=True)

if __name__=="__main__":
    run()
