#!/usr/bin/env python3
"""Experiment 77: exact gcd-normalized tightness obstruction census."""
from itertools import combinations
from math import gcd
from fractions import Fraction

def has_complementary_pair(v):
    q=len(v)+1
    return any(((a+b)//gcd(a,b))%q==0 for a,b in combinations(v,2))

def census(k,upper):
    n=excluded=0
    for v in combinations(range(1,upper+1),k):
        if gcd(*v)!=1:continue
        n+=1
        if not has_complementary_pair(v):excluded+=1
    return n,excluded

def verify_examples():
    assert has_complementary_pair((1,2,3,4))
    assert has_complementary_pair((1,3,4,7))
    for k,N,expected in [(3,15,(409,215)),(4,12,(479,141)),(5,12,(786,354))]:
        got=census(k,N)
        assert got==expected,(k,N,got,expected)
        print("PASS",k,N,"primitive",got[0],"excluded",got[1])

if __name__=="__main__":
    verify_examples()
