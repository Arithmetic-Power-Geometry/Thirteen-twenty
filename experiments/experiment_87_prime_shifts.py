#!/usr/bin/env python3
"""Experiment 87: exact Fraction prime-shift theorem and modular bad sets."""
from fractions import Fraction as F
from math import ceil
from itertools import combinations

def safe(v,t,q):
    return all(min((a*t)%1,1-(a*t)%1)>=F(1,q) for a in v)

def lower_witness(v):
    q=len(v)+1
    for a in v:
        for n in range(1,q*a//2+1):
            t=F(n,q*a)
            if safe(v,t,q):return t
    return None

def bad_shifts(e,t0,p,q):
    return {j for j in range(p) if min((e*(t0+F(j,p)))%1,1-(e*(t0+F(j,p)))%1)<F(1,q)}

def verify(v,p):
    k=len(v);q=k+1
    D=[a for a in v if a%p==0]
    E=[a for a in v if a%p!=0]
    if not D or not E:return None
    if len(E)*ceil(F(2*p,q))>=p:return None
    t0=lower_witness(D)
    assert t0 is not None
    for d in D:
        assert all((d*(t0+F(j,p)))%1==(d*t0)%1 for j in range(p))
    bad=set()
    for e in E:
        b=bad_shifts(e,t0,p,q)
        assert len(b)<=ceil(F(2*p,q))
        bad|=b
    assert len(bad)<p
    j=next(j for j in range(p) if j not in bad)
    t=t0+F(j,p)
    assert safe(v,t,q)
    return t

def audit():
    checks=0
    for k in range(3,7):
        for v in combinations(range(1,19),k):
            for p in (2,3,5,7):
                if sum(a%p!=0 for a in v)==1:
                    if verify(v,p) is not None:checks+=1
    assert verify((1,6,10,14,22),2) is not None
    print("PASS",checks,"exact conditional prime-shift certificates")
    print("example witness",verify((1,6,10,14,22),2))

if __name__=="__main__":audit()
