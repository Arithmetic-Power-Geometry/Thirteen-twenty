#!/usr/bin/env python3
"""Experiment 89: exact rational deletion obstruction and primitive fragmentation."""
from fractions import Fraction as F
from math import gcd
from itertools import combinations

def merge(ints):
    ints=sorted((a,b) for a,b in ints if a<b)
    out=[]
    for a,b in ints:
        if out and a<=out[-1][1]:out[-1]=(out[-1][0],max(b,out[-1][1]))
        else:out.append((a,b))
    return out

def intersect(A,B):
    i=j=0;out=[]
    while i<len(A) and j<len(B):
        a=max(A[i][0],B[j][0]);b=min(A[i][1],B[j][1])
        if a<b:out.append((a,b))
        if A[i][1]<B[j][1]:i+=1
        else:j+=1
    return merge(out)

def safe_intervals(v,q):
    d=F(1,q)
    return [((n+d)/v,(n+1-d)/v) for n in range(v)]

def core_safe(v,q):
    out=[(F(0),F(1))]
    for a in v:out=intersect(out,safe_intervals(a,q))
    return out

def measure(S):return sum((b-a for a,b in S),F(0))

def audit():
    checked=0;zero_measure=0;positive=0
    for k,N in ((3,12),(4,10),(5,9)):
        for V in combinations(range(1,N+1),k):
            if gcd(*V)!=1:continue
            q=k+1
            S=core_safe(V,q)
            if S:positive+=1
            for idx,v in enumerate(V):
                T=core_safe(V[:idx]+V[idx+1:],q)
                A=measure(T);m=len(T)
                if A>0 and F(2*m,q*v)<A:
                    checked+=1
                    assert S,(V,idx,'violates safe-extension theorem')
                if not S and A>0:
                    assert A<=F(2*m,q*v)
                    zero_measure+=1
    print('primitive vectors with positive-measure safe sets',positive)
    print('certified deletion extensions',checked)
    print('zero-measure safe-set deletion checks',zero_measure)
    assert (positive,checked,zero_measure)==(522,274,21)
    for N in (7,10,31,100):
        S=core_safe((1,N),3);A=measure(S);m=len(S)
        assert N%3==1 and gcd(1,N)==1
        assert m==(N+2)//3 and A==F(N+2,9*N)
        assert F(m,1)/A==3*N
        print('N',N,'components',m,'safe measure',A,'m/A',F(m,1)/A)
    print('PASS: all exact rational checks')

if __name__=='__main__':audit()
