#!/usr/bin/env python3
"""Experiment 96: independent exact audit of isolated safe-time collision theorem."""
from fractions import Fraction as F
from itertools import combinations
from math import gcd,lcm

def collision(V):
    q=len(V)+1
    candidates=set(); bound=0
    for a,b in combinations(V,2):
        g=gcd(a,b)
        if ((a+b)//g)%q:
            continue
        bound+=2*g
        for x in range(a):
            t=F(q*x+1,q*a)
            if (b*t)%1==F(q-1,q):candidates.add(t)
            t=F(q*x+q-1,q*a)
            if (b*t)%1==F(1,q):candidates.add(t)
    return candidates,bound

def direct(V):
    q=len(V)+1; L=lcm(*V); M=q*L
    good=lambda j:all(L<=(v*j)%M<=(q-1)*L for v in V)
    cell=lambda j:all(2*L<=(v*(2*j+1))%(2*M)<=2*(q-1)*L for v in V)
    return {F(j,M) for j in range(M) if good(j) and not cell((j-1)%M) and not cell(j)}

def main():
    counts=[]
    for k,N in ((3,14),(4,11),(5,9)):
        tested=0; isolated=0
        for V in combinations(range(1,N+1),k):
            if gcd(*V)!=1:continue
            candidates,bound=collision(V)
            actual=direct(V)
            assert actual<=candidates,(V,actual-candidates)
            assert len(candidates)<=bound
            tested+=1;isolated+=len(actual)
        counts.append((k,N,tested,isolated))
    assert counts==[(3,14,325,256),(4,11,325,378),(5,9,126,60)],counts
    print("PASS",counts,"vectors",sum(x[2] for x in counts),
          "isolated points",sum(x[3] for x in counts))
    for V in ((1,2,3),(1,3,4,7),(1,2,3,4),(1,3,9)):
        cand,bound=collision(V)
        actual=direct(V)
        print(V,"candidates",len(cand),"bound",bound,"isolated",len(actual),
              "witnesses",sorted(actual))

if __name__=="__main__":main()
