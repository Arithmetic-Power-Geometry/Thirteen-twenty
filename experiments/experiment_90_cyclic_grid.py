#!/usr/bin/env python3
"""Experiment 90: exact integer cyclic-grid audit of three all-dimensional theorems."""
from math import gcd, lcm
from itertools import combinations

def audit(V):
    k=len(V); q=k+1; L=lcm(*V); M=q*L
    vertices=[
        all(L <= (v*j)%M <= (q-1)*L for v in V)
        for j in range(M)
    ]
    # Midpoint of each grid cell: exact modular test with denominator 2M.
    cells=[
        all(2*L <= (v*(2*j+1))%(2*M) <= 2*(q-1)*L for v in V)
        for j in range(M)
    ]
    G=sum(vertices)
    H=sum(cells)
    C=sum(vertices[j] and not vertices[(j-1)%M] for j in range(M))
    assert G==H+C, (V,G,H,C)
    for v in V:
        bad=sum(not (L <= (v*j)%M <= (q-1)*L) for j in range(M))
        assert bad==2*L-v,(V,v,bad,2*L-v)
    assert all(not cells[j] or (vertices[j] and vertices[(j+1)%M]) for j in range(M))
    return M,G,H,C

def main():
    checked=0
    for k,N in ((2,18),(3,10),(4,8)):
        for V in combinations(range(1,N+1),k):
            if gcd(*V)!=1:continue
            audit(V)
            checked+=1
    assert checked==279,checked
    for V in ((1,2,3,4),(1,3,4,7),(1,3,9),(2,3,5)):
        print(V, "M,G,H,C =",audit(V))
    print("PASS:",checked,"primitive vectors, all integer-only checks")

if __name__=="__main__":
    main()
