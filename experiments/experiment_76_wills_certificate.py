#!/usr/bin/env python3
"""Experiment 76: exact finite rational certificate for the classical Wills set."""
from fractions import Fraction as Q
from itertools import combinations
from math import gcd

SPEEDS=(1,3,4,7)
DENOMINATOR=5

def safe(t):
    return all(min((a*t)%1,1-(a*t)%1)>=Q(1,DENOMINATOR) for a in SPEEDS)

def boundaries():
    b={Q(0),Q(1)}
    for a in SPEEDS:
        for n in range(a+1):
            for sign in (-1,1):
                t=Q(DENOMINATOR*n+sign,DENOMINATOR*a)
                if 0<=t<=1:b.add(t)
    return sorted(b)

def certify(verbose=True):
    b=boundaries()
    good=[t for t in b if safe(t)]
    cells=[]
    for left,right in zip(b,b[1:]):
        mid=(left+right)/2
        bad=[a for a in SPEEDS if min((a*mid)%1,1-(a*mid)%1)<Q(1,DENOMINATOR)]
        assert bad,(left,right)
        cells.append((left,right,bad[0]))
    assert good==[Q(i,5) for i in range(1,5)]
    assert len(b)==28 and len(cells)==27
    if verbose:
        print('boundary_count:',len(b),'open_cells:',len(cells))
        print('safe_times:',*[str(t) for t in good])
        print('every open cell is forbidden, witness speeds:')
        for left,right,a in cells:
            print(str(left),str(right),'forbidden_by',a)
        print('PASS: exact safe set is {1/5,2/5,3/5,4/5}')
    return good,cells

if __name__=='__main__':
    certify()
