#!/usr/bin/env python3
"""Experiment 97: exact modular generation and independent isolated-grid audit."""
from fractions import Fraction as F
from itertools import combinations
from math import gcd,lcm

def candidates(V):
    q=len(V)+1
    out=set()
    for a,b in combinations(V,2):
        g=gcd(a,b); A=a//g; B=b//g
        if (A+B)%q: continue
        c=(A+B)//q
        inv=pow(B,-1,A) if A>1 else 0
        m0=(-c*inv)%A if A>1 else 0
        for z in range(g):
            m=m0+z*A
            t=F(q*m+1,q*a)
            assert (b*t)%1==F(q-1,q)
            out.add(t)
            out.add(1-t)
    return out

def modular_isolated(V):
    q=len(V)+1
    return {t for t in candidates(V) if
            all(F(1,q)<=(v*t)%1<=F(q-1,q) for v in V)}

def direct_isolated(V):
    q=len(V)+1; L=lcm(*V); M=q*L
    def safe(j):
        return all(L<=(v*j)%M<=(q-1)*L for v in V)
    def cell(j):
        return all(2*L<=(v*(2*j+1))%(2*M)<=2*(q-1)*L for v in V)
    return {F(j,M) for j in range(M) if
            safe(j) and not cell(j) and not cell((j-1)%M)}

def main():
    counts=[]
    for k,N in ((3,14),(4,11),(5,9)):
        total=0; cand=0; isolated=0
        for V in combinations(range(1,N+1),k):
            if gcd(*V)!=1:continue
            c=candidates(V)
            actual=direct_isolated(V)
            found=modular_isolated(V)
            assert found==actual,(V,found,actual)
            assert found<=c
            total+=1; cand+=len(c); isolated+=len(actual)
        counts.append((k,N,total,cand,isolated))
    assert counts==[(3,14,325,432,256),(4,11,325,788,378),(5,9,126,110,60)]
    print("PASS",counts,"totals",tuple(sum(x[i] for x in counts) for i in (2,3,4)))
    for V in ((1,2,3),(1,3,4,7),(1,3,9),(1,2,3,4)):
        print(V,"candidates",len(candidates(V)),"isolated",sorted(modular_isolated(V)))

if __name__=="__main__":main()
