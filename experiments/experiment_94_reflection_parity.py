#!/usr/bin/env python3
"""Experiment 94: integer-only audit of reflection parity invariants."""
from itertools import combinations
from math import gcd, lcm

def audit(V):
    k=len(V); q=k+1; L=lcm(*V); M=q*L
    vertex=[all(L <= (v*j)%M <= (q-1)*L for v in V) for j in range(M)]
    cell=[all(2*L <= (v*(2*j+1))%(2*M) <= 2*(q-1)*L for v in V) for j in range(M)]
    G=sum(vertex); H=sum(cell)
    C=sum(vertex[j] and not vertex[(j-1)%M] for j in range(M))
    odd=int(all(v%2 for v in V))
    assert G==H+C,(V,G,H,C)
    assert G%2==odd*(k%2),(V,G)
    assert H%2==odd*(1-k%2),(V,H)
    assert C%2==odd,(V,C)
    return G,H,C

def main():
    n=0
    for k,N in ((3,12),(4,10),(5,9)):
        for V in combinations(range(1,N+1),k):
            if gcd(*V)!=1:continue
            audit(V)
            n+=1
    assert n==527,n
    print("PASS:",n,"primitive vectors; G/H/C reflection parity and Euler identity")
    for V in ((1,2,3,4),(1,3,4,7),(1,3,9),(2,3,5)):
        print(V,audit(V))

if __name__=="__main__":main()
