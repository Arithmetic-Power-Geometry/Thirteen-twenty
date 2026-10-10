#!/usr/bin/env python3
"""Experiment 39: bounded-spread witness for arbitrary dimension and real speeds.
Exact rational tests for representative integer vectors and exhaustive small tuples.
"""
from fractions import Fraction
from itertools import combinations

def certificate(speeds):
    speeds=tuple(Fraction(v) for v in speeds)
    k=len(speeds)
    assert k>=1 and all(v>0 for v in speeds)
    m=max(speeds)
    if k*min(speeds)<m:
        return None
    t=Fraction(k,k+1)/m
    assert all(min((v*t)%1,1-(v*t)%1)>=Fraction(1,k+1) for v in speeds)
    return t

if __name__=="__main__":
    for k in range(2,7):
        total=covered=0
        for vs in combinations(range(1,13),k):
            total+=1
            w=certificate(vs)
            if w is not None: covered+=1
        print(f"k={k}, total={total}, certified={covered}")
    for vs in [(3,6,9,12,15),(16,17,18,19,20),tuple(range(16,31))]:
        w=certificate(vs)
        print(f"speeds={vs}, witness={w}")
        assert w is not None
    assert certificate((2,3,5,7,11,13,17,19,23,29,31,37,41,43,47)) is None
