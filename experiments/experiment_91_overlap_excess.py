#!/usr/bin/env python3
"""Exact integer audit for Experiment 91."""
from itertools import combinations
from math import gcd, lcm

def audit(v):
    k=len(v); L=lcm(*v); M=(k+1)*L
    counts=[sum(not(L <= (a*j)%M <= k*L) for a in v) for j in range(M)]
    G=counts.count(0)
    P=sum(b*(b-1)//2 for b in counts)
    E=sum(max(0,b-1) for b in counts)
    base=sum(v)-(k-1)*L
    assert G==base+E
    assert k*E>=2*P
    return base,G,P,E,L,M

def main():
    results=[]
    for k,N in ((3,15),(4,12),(5,10)):
        total=0; additional=0; failures=0
        for v in combinations(range(1,N+1),k):
            if gcd(*v)!=1:continue
            base,G,P,E,L,M=audit(v)
            total+=1
            additional+=(base<=0 and k*base+2*P>0)
            failures+=(G==0)
        results.append((k,N,total,additional,failures))
    assert results==[(3,15,409,357,0),(4,12,479,16,0),(5,10,251,0,0)]
    assert audit((1,2,3))==(-6,2,11,8,6,24)
    assert audit((1,2,3,6))==(-6,8,19,14,6,30)
    print("PASS",results)

if __name__=="__main__":main()
