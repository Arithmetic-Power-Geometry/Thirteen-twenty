#!/usr/bin/env python3
"""Experiment 93: exact generalized-CRT higher-order forbidden intersections."""
from itertools import combinations
from math import gcd, lcm

def crt_merge(x, m, y, n):
    d = gcd(m, n)
    if (y-x) % d:
        return None
    nn = n // d
    t = ((y-x)//d * pow(m//d, -1, nn)) % nn if nn > 1 else 0
    return ((x + m*t) % (m*nn), m*nn)

def forbidden(h, q, cell):
    return list(range(h)) + list(range((q-1)*h + (0 if cell else 1), q*h))

def count_crt(W, q, L):
    ell = lcm(*W)
    d = gcd(*W)
    r = L // ell
    def count(cell):
        states = {(0, 1)}
        for v in W:
            h = ell // v
            mod = q*h
            states = {z for x,m in states for y in forbidden(h,q,cell)
                      if (z := crt_merge(x,m,y,mod)) is not None}
        assert all(m == q*ell//d for x,m in states)
        return len(states)
    X = count(False)
    Y = count(True)
    return d*((r-1)*Y + X), X, Y

def brute(W, q, L):
    M = q*L
    return sum(all(not (L <= (v*j)%M <= (q-1)*L) for v in W)
               for j in range(M))

def main():
    counts = {}
    for k,N in ((3,10),(4,9),(5,8)):
        for V in combinations(range(1,N+1),k):
            if gcd(*V) != 1:
                continue
            L = lcm(*V)
            q = k+1
            for s in range(2,min(k,4)+1):
                for W in combinations(V,s):
                    ans,X,Y = count_crt(W,q,L)
                    direct = brute(W,q,L)
                    assert ans == direct, (V,W,ans,direct,X,Y)
                    counts[s] = counts.get(s,0)+1
    assert counts == {2:1637,3:1169,4:405}, counts
    print("PASS", counts, "total", sum(counts.values()))
    for V in ((1,2,3),(1,3,4,7),(1,2,3,6)):
        q=len(V)+1
        L=lcm(*V)
        print(V, "full intersection", count_crt(V,q,L), brute(V,q,L))

if __name__ == "__main__":
    main()
