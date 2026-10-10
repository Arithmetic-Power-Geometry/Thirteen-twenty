#!/usr/bin/env python3
"""Experiment 46: exact safe-measure and isolated-witness classification."""
from fractions import Fraction as F
from itertools import combinations

def safe_measure(v):
    q=len(v)+1
    breaks={F(0),F(1)}
    for a in v:
        for j in range(a+1):
            for s in (-1,1):
                x=F(q*j+s,q*a)
                if 0<=x<=1:breaks.add(x)
    xs=sorted(breaks)
    def safe(t):return all(min((a*t)%1,1-(a*t)%1)>=F(1,q) for a in v)
    intervals=[(l,r) for l,r in zip(xs,xs[1:]) if safe((l+r)/2)]
    isolated=[x for x in xs if safe(x) and not any(l<=x<=r for l,r in intervals)]
    return sum((r-l for l,r in intervals),F(0)),len(intervals),len(isolated)

if __name__=='__main__':
    print("k,total,positive_measure,tight_only,no_witness")
    for k in range(2,6):
        count=positive=tight=zero=0
        for v in combinations(range(1,10),k):
            m,n,z=safe_measure(v);count+=1
            if m>0:positive+=1
            elif z:tight+=1
            else:zero+=1
        print(k,count,positive,tight,zero,sep=",")
    for v in [(1,2,3),(1,2,3,4),(1,2,3,4,5),(1,2,4,8)]:
        print("example",v,safe_measure(v))
