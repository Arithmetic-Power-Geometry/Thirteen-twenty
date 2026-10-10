#!/usr/bin/env python3
"""Experiment 84: exact modular boundary witness and exhaustive primitive census."""
from itertools import combinations
from math import gcd
from fractions import Fraction as F

def modular_witness(speeds):
    v=tuple(sorted(speeds))
    k=len(v)
    q=k+1
    if k<2 or min(v)<=0 or len(set(v))!=k:raise ValueError("Distinct positive integer speeds required")
    for a in v:
        m=q*a
        for n in range(1,m//2+1):
            if n%q==0:continue
            if all(a<=((b*n)%m)<=(q-1)*a for b in v):
                return a,n,F(n,m)
    return None

def check(v):
    w=modular_witness(v)
    if w is None:return False
    a,n,t=w
    q=len(v)+1
    assert all(min((b*t)%1,1-(b*t)%1)>=F(1,q) for b in v)
    return True

def census(k,N):
    count=0
    for v in combinations(range(1,N+1),k):
        if gcd(*v)!=1:continue
        count+=1
        assert check(v),("candidate counterexample (not independently confirmed)",v)
    return count

if __name__=="__main__":
    expected={(3,15):409,(4,12):479,(5,12):786}
    total=0
    for (k,N),want in expected.items():
        got=census(k,N)
        assert got==want,(k,N,got,want)
        total+=got
        print("PASS k",k,"N",N,"primitive",got,"failures",0)
    assert total==1674
    print("PASS: 1674 exact modular witnesses")
