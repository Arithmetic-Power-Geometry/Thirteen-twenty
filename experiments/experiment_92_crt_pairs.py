#!/usr/bin/env python3
"""Experiment 92: exact CRT pair-overlap formula versus independent full-grid scan."""
from itertools import combinations
from math import gcd, lcm

def crt_pair(a, b, q, L):
    g = gcd(a, b)
    A, B = a // g, b // g
    assert L % lcm(a, b) == 0
    p, s = q * B, q * A
    d = gcd(p, s)
    assert d == q

    def compatible(cell):
        ca, cb = [0] * d, [0] * d
        for x in range(p):
            if x < B or (x >= (q-1)*B if cell else x > (q-1)*B):
                ca[x % d] += 1
        for y in range(s):
            if y < A or (y >= (q-1)*A if cell else y > (q-1)*A):
                cb[y % d] += 1
        return sum(x*y for x, y in zip(ca, cb))

    H = compatible(True)
    G = compatible(False)
    assert H >= G
    r = L // lcm(a, b)
    return g * ((r-1)*H + G)

def brute_pair(a, b, q, L):
    M = q*L
    return sum(
        not (L <= a*j % M <= (q-1)*L)
        and not (L <= b*j % M <= (q-1)*L)
        for j in range(M)
    )

def main():
    checked = 0
    for k, N in ((2,16),(3,12),(4,10),(5,9)):
        for v in combinations(range(1,N+1), k):
            if gcd(*v) != 1:
                continue
            L = lcm(*v)
            q = k+1
            for a,b in combinations(v,2):
                assert crt_pair(a,b,q,L) == brute_pair(a,b,q,L), (v,a,b)
                checked += 1
    assert checked == 3157
    print("PASS",checked,"exact CRT-vs-brute pair comparisons")
    for v in ((1,2,3),(1,2,3,6),(1,3,4,7)):
        L = lcm(*v)
        q = len(v)+1
        print(v, [(a,b,crt_pair(a,b,q,L)) for a,b in combinations(v,2)])

if __name__ == "__main__":
    main()
