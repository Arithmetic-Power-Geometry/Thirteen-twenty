"""P03-14 independent OR-Tools CP-SAT verification of exact scheduling optima.

Optional dependency: pip install ortools
This is an exact integer-time model of rational instances after scaling by LCM
of all calendar endpoints, releases, processing times and deadlines.
"""
from fractions import Fraction as F
from math import lcm
from random import Random

from p03_06_indexed_implicit_query import components
from p03_12_exact_weighted_scheduling import exact_opt
from p03_13_window_aware_bound import window_aware_bound

def cpsat_opt(intervals,jobs):
    from ortools.sat.python import cp_model
    denominators=[v.denominator for iv in intervals for v in iv]
    denominators += [v.denominator for job in jobs for v in job]
    scale=lcm(*denominators) if denominators else 1
    def integer(v):
        result=v*scale
        assert result.denominator==1
        return result.numerator
    model=cp_model.CpModel()
    active=[]
    selected=[]
    for j,(r,p,d,w) in enumerate(jobs):
        if w.denominator!=1:
            raise ValueError("this CP-SAT experiment requires integral weights")
        choices=[]
        for i,(left,right) in enumerate(intervals):
            lower=max(left,r)
            upper=min(right,d)
            if lower+p>upper: continue
            lit=model.NewBoolVar(f"use_{j}_{i}")
            start=model.NewIntVar(integer(lower),integer(upper-p),f"start_{j}_{i}")
            end=model.NewIntVar(integer(lower+p),integer(upper),f"end_{j}_{i}")
            interval=model.NewOptionalIntervalVar(start,integer(p),end,lit,f"job_{j}_{i}")
            active.append(interval)
            choices.append(lit)
        chosen=model.NewBoolVar(f"selected_{j}")
        model.Add(sum(choices)==chosen)
        selected.append(chosen)
    model.AddNoOverlap(active)
    model.Maximize(sum(integer(jobs[j][3])*selected[j] for j in range(len(jobs))))
    solver=cp_model.CpSolver()
    solver.parameters.max_time_in_seconds=15
    solver.parameters.num_search_workers=1
    solver.parameters.random_seed=20261113
    status=solver.Solve(model)
    if status!=cp_model.OPTIMAL:
        raise RuntimeError(f"CP-SAT not proven optimal: {solver.StatusName(status)}")
    return F(round(solver.ObjectiveValue()),scale)

def run():
    rng=Random(20261113)
    count=0
    for a,b in ((1,1),(1,14),(2,3)):
        iv=components(a,b)
        for _ in range(5):
            jobs=[]
            for j in range(rng.randrange(1,6)):
                r=F(rng.randrange(17),16)
                d=F(rng.randrange(17),16)
                if r>d:r,d=d,r
                p=F(rng.randrange(1,9),32)
                w=F(rng.randrange(11))
                jobs.append((r,p,d,w))
            exact=exact_opt(iv,jobs)
            independent=cpsat_opt(iv,jobs)
            window=window_aware_bound(iv,jobs)
            assert exact==independent<=window,(a,b,jobs,exact,independent,window)
            count+=1
    print(f"PASS: {count} exact independent OR-Tools CP-SAT scheduling optima; zero mismatches")

if __name__=="__main__":
    run()
