#!/usr/bin/env python3
"""Experiment 79: exact rational verification of the pair-tree no-go theorem."""
from fractions import Fraction as Q
from itertools import combinations
from math import gcd

def b2(x):
    x=x%1
    return x*x-x+Q(1,6)

def overlap(a,b,q):
    g=gcd(a,b)
    A,B=a//g,b//g
    d=Q(1,q)
    return 4*d*d+(b2((A-B)*d)-b2((A+B)*d))/Q(A*B)

def verify(v):
    k=len(v)
    q=k+1
    assert k>=4 and len(set(v))==k and min(v)>0
    bound=Q(q*q,4*(q-4))
    edges=[]
    for a,b in combinations(v,2):
        g=gcd(a,b)
        p=(a//g)*(b//g)
        w=overlap(a,b,q)
        assert abs(w-Q(4,q*q))<=Q(1,4*p)
        edges.append((a,b,p,w))
    condition=all(p>bound for _,_,p,_ in edges)
    if condition:
        assert all(w<Q(1,q) for _,_,_,w in edges)
    print("k",k,"q",q,"speeds",v)
    print("all_pair_products_above_threshold",condition)
    print("threshold",bound,"max_overlap",max(w for *_,w in edges),"1/q",Q(1,q))
    return condition

if __name__=="__main__":
    assert verify((11,13,17,19))
    assert verify((11,13,17,19,23))
    assert verify((11,13,17,19,23,29))
    assert verify((11,13,17,19,23,29,31))
    print("PASS: exact arithmetic all tests")
