"""P03-13: exact window-aware component assignment relaxation.

Jobs may be assigned to a calendar component only if that component contains
an uninterrupted processing window inside [release, deadline]. This remains a
multiple-knapsack relaxation: job ordering and within-component window clashes
are ignored.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

from p03_06_indexed_implicit_query import components
from p03_11_component_packing_bound import packing_upper_bound
from p03_12_exact_weighted_scheduling import exact_opt

def window_aware_bound(intervals,jobs):
    """Exact small-instance relaxation; jobs=(r,p,d,w)."""
    if any(p<=0 or w<0 or r>d for r,p,d,w in jobs):
        raise ValueError("invalid job")
    n=len(jobs)
    m=len(intervals)
    lengths=[u-l for l,u in intervals]
    allowed=[
        [max(l,r)+p<=min(u,d) for l,u in intervals]
        for r,p,d,w in jobs
    ]
    sums=[F(0)]*(1<<n)
    weights=[F(0)]*(1<<n)
    for mask in range(1,1<<n):
        bit=mask & -mask
        j=bit.bit_length()-1
        prev=mask^bit
        sums[mask]=sums[prev]+jobs[j][1]
        weights[mask]=weights[prev]+jobs[j][3]
    reachable={0}
    for i in range(m):
        admissible=0
        for j in range(n):
            if allowed[j][i]: admissible |= 1<<j
        fits=[mask for mask in range(1<<n)
              if mask & ~admissible == 0 and sums[mask]<=lengths[i]]
        nxt=set(reachable)
        for used in reachable:
            for subset in fits:
                if used & subset == 0: nxt.add(used|subset)
        reachable=nxt
    return max((weights[mask] for mask in reachable),default=F(0))

def test():
    rng=Random(20261113)
    checked=0
    tightened=0
    strictly_better_than_opt=0
    for a,b in ((1,1),(1,14),(2,3)):
        iv=components(a,b)
        lengths=[u-l for l,u in iv]
        for _ in range(70):
            jobs=[]
            for j in range(rng.randrange(1,6)):
                r=F(rng.randrange(17),16)
                d=F(rng.randrange(17),16)
                if r>d:r,d=d,r
                p=F(rng.randrange(1,9),32)
                w=F(rng.randrange(11))
                jobs.append((r,p,d,w))
            opt=exact_opt(iv,jobs)
            window=window_aware_bound(iv,jobs)
            pack=packing_upper_bound(lengths,[(p,w) for r,p,d,w in jobs])
            assert opt<=window<=pack,(a,b,jobs,opt,window,pack)
            tightened+=window<pack
            strictly_better_than_opt+=window>opt
            checked+=1
    # Two individually fitting jobs have disjoint allowed components;
    # the window-aware assignment can exclude a job with an impossible window.
    iv=[(F(0),F(1,2))]
    jobs=[(F(0),F(1,4),F(1,2),F(7)),
          (F(1,2),F(1,4),F(1),F(11))]
    assert window_aware_bound(iv,jobs)==F(7)
    assert packing_upper_bound([F(1,2)],[(p,w) for r,p,d,w in jobs])==F(18)
    print(f"PASS: {checked} exact scheduling-bound comparisons; "
          f"window_strictly_tighter_than_packing={tightened}; "
          f"window_still_above_opt={strictly_better_than_opt}; "
          "hand_example=7_vs_18")

if __name__=="__main__":
    test()
