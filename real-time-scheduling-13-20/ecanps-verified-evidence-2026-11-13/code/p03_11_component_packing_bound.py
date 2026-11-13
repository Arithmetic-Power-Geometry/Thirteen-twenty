"""P03-11: exact component-packing upper bound for weighted nonpreemptive scheduling.

Release times and deadlines are deliberately relaxed; every feasible schedule
maps to a disjoint assignment of selected jobs to available components.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

def packing_upper_bound(lengths, jobs):
    """Return maximum total weight packable in components ignoring time windows.

    lengths: component lengths (nonnegative exact Fractions).
    jobs: (processing_time, nonnegative_weight) pairs.
    Exponential in job count; intended as a small-instance certificate.
    """
    if any(L < 0 for L in lengths):
        raise ValueError("negative component length")
    if any(p <= 0 or w < 0 for p,w in jobs):
        raise ValueError("positive processing and nonnegative weights required")
    n=len(jobs)
    sums=[F(0)]*(1<<n)
    weights=[F(0)]*(1<<n)
    for mask in range(1,1<<n):
        bit=mask & -mask
        j=bit.bit_length()-1
        rest=mask^bit
        sums[mask]=sums[rest]+jobs[j][0]
        weights[mask]=weights[rest]+jobs[j][1]
    reachable={0}
    for L in lengths:
        fits=[s for s in range(1<<n) if sums[s]<=L]
        nxt=set(reachable)
        for used in reachable:
            for subset in fits:
                if not (used & subset):
                    nxt.add(used|subset)
        reachable=nxt
    best=max((weights[mask] for mask in reachable),default=F(0))
    return best

def independent_assignment_oracle(lengths,jobs):
    """Independent brute-force assignment: each job omitted or assigned a component."""
    best=F(0)
    for choices in product(range(-1,len(lengths)),repeat=len(jobs)):
        loads=[F(0)]*len(lengths)
        value=F(0)
        for j,k in enumerate(choices):
            if k>=0:
                loads[k]+=jobs[j][0]
                value+=jobs[j][1]
        if all(loads[k]<=lengths[k] for k in range(len(lengths))):
            best=max(best,value)
    return best

def admissibility_bound(lengths,jobs):
    maxlen=max(lengths,default=F(0))
    return sum((w for p,w in jobs if p<=maxlen),F(0))

def test():
    rng=Random(20261113)
    checks=0
    strict=0
    for _ in range(250):
        m=rng.randrange(0,4)
        n=rng.randrange(0,7)
        lengths=[F(rng.randrange(1,9),8) for _ in range(m)]
        jobs=[(F(rng.randrange(1,9),8),F(rng.randrange(0,11))) for _ in range(n)]
        bound=packing_upper_bound(lengths,jobs)
        oracle=independent_assignment_oracle(lengths,jobs)
        naive=admissibility_bound(lengths,jobs)
        assert bound==oracle,(lengths,jobs,bound,oracle)
        assert bound<=naive,(lengths,jobs,bound,naive)
        strict+=(bound<naive)
        checks+=1
    # Two jobs fit individually but cannot both occupy one component.
    lengths=[F(3,5)]
    jobs=[(F(2,5),F(7)),(F(2,5),F(11))]
    assert packing_upper_bound(lengths,jobs)==F(11)
    assert admissibility_bound(lengths,jobs)==F(18)
    print(f"PASS: {checks} randomized exact packing-vs-independent-assignment comparisons; "
          f"strictly_tighter_than_individual_filter={strict}; "
          "hand_counterexample=11_vs_18")

if __name__=="__main__":
    test()
