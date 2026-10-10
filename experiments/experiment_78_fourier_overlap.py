#!/usr/bin/env python3
"""Experiment 78: Bernoulli-Fourier pair-overlap formula and exact 630-case audit."""
from fractions import Fraction as Q
from itertools import combinations
from math import gcd

def bernoulli2(x):
    x=x%1
    return x*x-x+Q(1,6)

def pair_overlap(a,b,q):
    if a<=0 or b<=0 or q<3:
        raise ValueError("Positive speeds and integer q>=3 required")
    g=gcd(a,b); A=a//g; B=b//g
    d=Q(1,q)
    return 4*d*d+(bernoulli2(d*(A-B))-bernoulli2(d*(A+B)))/Q(A*B)

def independent_interval_sweep(a,b,q):
    d=Q(1,q)
    boundaries={Q(0),Q(1)}
    for v in (a,b):
        for n in range(v+1):
            for sign in (-1,1):
                t=Q(q*n+sign,q*v)
                if 0<=t<=1:boundaries.add(t)
    endpoints=sorted(boundaries)
    result=Q(0)
    for left,right in zip(endpoints,endpoints[1:]):
        mid=(left+right)/2
        if all(min((v*mid)%1,1-(v*mid)%1)<d for v in (a,b)):
            result+=right-left
    return result

def max_spanning_tree_weight(speeds):
    v=tuple(speeds)
    q=len(v)+1
    edges=sorted(((pair_overlap(a,b,q),i,j) for (i,a),(j,b) in combinations(enumerate(v),2)),reverse=True)
    parent=list(range(len(v)))
    def root(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    total=Q(0)
    chosen=[]
    for w,i,j in edges:
        x,y=root(i),root(j)
        if x!=y:
            parent[x]=y
            total+=w
            chosen.append((i,j,w))
            if len(chosen)==len(v)-1:break
    return total,chosen

def audit():
    checked=0
    for q in range(3,9):
        for a in range(1,16):
            for b in range(a+1,16):
                actual=pair_overlap(a,b,q)
                expected=independent_interval_sweep(a,b,q)
                assert actual==expected,(q,a,b,actual,expected)
                checked+=1
    assert checked==630
    print("PASS",checked,"exact rational overlap comparisons")
    for v in ((1,2,3),(1,3,4,7),(101,299,501,701,899)):
        w,edges=max_spanning_tree_weight(v)
        threshold=Q(len(v)-1,len(v)+1)
        print("speeds",v,"tree_weight",w,"threshold",threshold,
              "positive_measure_certified",w>threshold)
        print("tree_edges",edges)

if __name__=="__main__":
    audit()
