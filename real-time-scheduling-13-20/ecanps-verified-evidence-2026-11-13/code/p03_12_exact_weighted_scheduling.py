"""P03-12: exact tiny-instance weighted scheduling oracle and bound comparison.

Enumerates finite canonical start candidates (releases, component left edges,
and finishes of earlier jobs) via recursive subset search. The recursion also
considers idle gaps by trying every remaining job at its earliest legal finish.
For nonpreemptive single-machine schedules, an optimal sequence can be
left-shifted so each chosen job starts at its earliest legal opportunity.
"""
from fractions import Fraction as F
from random import Random

from p03_06_indexed_implicit_query import components, earliest_oracle
from p03_11_component_packing_bound import (
    packing_upper_bound, admissibility_bound,
)

def exact_opt(intervals, jobs):
    """jobs = (release,processing,deadline,nonnegative_weight)."""
    if any(p<=0 or w<0 or r>d for r,p,d,w in jobs):
        raise ValueError("invalid job")
    n=len(jobs)
    memo={}
    def visit(mask,t):
        key=(mask,t)
        if key in memo: return memo[key]
        best=F(0)
        for j,(r,p,d,w) in enumerate(jobs):
            if mask>>j & 1: continue
            f=earliest_oracle(intervals,max(t,r),p,d)
            if f is not None:
                best=max(best,w+visit(mask|(1<<j),f))
        memo[key]=best
        return best
    return visit(0,F(0))

def independently_enumerated_schedule(intervals,jobs):
    """Independent exhaustive permutation/subsequence oracle for tiny n."""
    from itertools import permutations
    best=F(0)
    for k in range(len(jobs)+1):
        for order in permutations(range(len(jobs)),k):
            t=F(0)
            total=F(0)
            for j in order:
                r,p,d,w=jobs[j]
                f=earliest_oracle(intervals,max(t,r),p,d)
                if f is None: break
                t=f
                total+=w
            else:
                best=max(best,total)
    return best

def run():
    rng=Random(20261113)
    tested=0
    strict=0
    gap=F(0)
    for a,b in ((1,1),(1,14),(2,3)):
        intervals=components(a,b)
        lengths=[u-l for l,u in intervals]
        for _ in range(90):
            n=rng.randrange(1,7)
            jobs=[]
            for j in range(n):
                r=F(rng.randrange(0,17),16)
                p=F(rng.randrange(1,9),32)
                d=F(rng.randrange(0,17),16)
                w=F(rng.randrange(0,11))
                if r>d: r,d=d,r
                jobs.append((r,p,d,w))
            opt=exact_opt(intervals,jobs)
            independent=independently_enumerated_schedule(intervals,jobs)
            pack=packing_upper_bound(lengths,[(p,w) for _,p,_,w in jobs])
            individual=admissibility_bound(lengths,[(p,w) for _,p,_,w in jobs])
            assert opt==independent,(a,b,jobs,opt,independent)
            assert opt<=pack<=individual,(a,b,jobs,opt,pack,individual)
            strict+=(pack<individual)
            gap+=pack-opt
            tested+=1
    print(f"PASS: {tested} exact scheduling instances; "
          f"strict_packing_vs_individual={strict}; "
          f"total_packing_minus_opt={gap}; zero mismatches")

if __name__=="__main__":
    run()
