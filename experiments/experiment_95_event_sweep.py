#!/usr/bin/env python3
"""Experiment 95: exact rational boundary-event sweep for Lonely Runner safe sets."""
from fractions import Fraction as F
from math import lcm, gcd
from itertools import combinations

def safe(t, V, q):
    return all(F(1,q) <= (v*t)%1 <= F(q-1,q) for v in V)

def sweep(V):
    q=len(V)+1
    B={F(0),F(1)}
    for v in V:
        for n in range(v):
            B.add(F(q*n+1,q*v))
            B.add(F(q*n+q-1,q*v))
    E=sorted(B)
    vertex=[safe(x,V,q) for x in E[:-1]]
    cell=[safe((a+b)/2,V,q) for a,b in zip(E,E[1:])]
    assert not vertex[0]
    assert all(not cell[i] or (vertex[i] and vertex[(i+1)%len(vertex)])
               for i in range(len(cell)))
    C=sum(vertex[i] and not cell[i-1] for i in range(len(vertex)))
    L=lcm(*V); M=q*L
    H=sum(int((E[i+1]-E[i])*M) for i,c in enumerate(cell) if c)
    G=H+C
    return G,H,C,len(E)-1,next((E[i] for i,v in enumerate(vertex) if v),None)

def brute(V):
    q=len(V)+1; L=lcm(*V); M=q*L
    vertices=[all(L <= (v*j)%M <= (q-1)*L for v in V) for j in range(M)]
    cells=[all(2*L <= (v*(2*j+1))%(2*M) <= 2*(q-1)*L for v in V)
           for j in range(M)]
    C=sum(vertices[j] and not cells[(j-1)%M] for j in range(M))
    return sum(vertices),sum(cells),C

def main():
    counts=[]
    for k,N in ((2,12),(3,10),(4,8),(5,7)):
        count=0
        for V in combinations(range(1,N+1),k):
            if gcd(*V)!=1: continue
            G,H,C,n,w=sweep(V)
            assert (G,H,C)==brute(V),(V,(G,H,C),brute(V))
            assert (w is None)==(G==0)
            count+=1
        counts.append((k,N,count))
    assert counts==[(2,12,45),(3,10,109),(4,8,69),(5,7,21)]
    V=(101,103,107,109,113)
    G,H,C,n,w=sweep(V)
    M=6*lcm(*V)
    assert (M,n,G,H,C,w)==(82261868142,1059,11732278703,11732278616,87,F(1,606))
    assert sweep((1,3,4,7))==(4,0,4,27,F(1,5))
    print("PASS",counts,"total",sum(x[2] for x in counts))
    print("large:",V,"M",M,"events",n,"G,H,C",G,H,C,"witness",w)
    print("tight:",(1,3,4,7),sweep((1,3,4,7)))

if __name__=="__main__":main()
