#!/usr/bin/env python3
"""Experiment 44: exact rational-interval witness for Q-independent speed blocks."""
from fractions import Fraction
from itertools import combinations
from math import isqrt

def sqrt2_interval():
    lo,hi=Fraction(7,5),Fraction(3,2)
    assert lo*lo<2<hi*hi
    return lo,hi

def prove_example():
    lo,hi=sqrt2_interval()
    t=Fraction(1,4)
    assert min(t,1-t)>Fraction(1,5)
    assert min(2*t,1-2*t)>Fraction(1,5)
    # sqrt(2)/4 in (7/20,3/8), both within (1/5,4/5)
    assert lo*t>Fraction(1,5) and hi*t<Fraction(4,5)
    # sqrt(2)/2 in (7/10,3/4), both within (1/5,4/5)
    assert lo*2*t>Fraction(1,5) and hi*2*t<Fraction(4,5)
    return t

def safe_block(q,speeds,t):
    return all(min((v*t)%1,1-(v*t)%1)>Fraction(1,q) for v in speeds)

def main():
    print('exact_example_time',prove_example())
    checked=0
    # For each integer block with <=3 distinct speeds in 1..10,
    # search exact rational times for strict separation at q=8.
    for size in (1,2,3):
        for block in combinations(range(1,11),size):
            witness=next((Fraction(j,120) for j in range(1,120)
                          if safe_block(8,block,Fraction(j,120))),None)
            assert witness is not None,block
            checked+=1
    print('rational_block_strict_certificates',checked)
    print('NOTE: finite block tests do not establish the Kronecker density theorem.')
if __name__=='__main__':main()
