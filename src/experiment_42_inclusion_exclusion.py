#!/usr/bin/env python3
"""Exact inclusion-exclusion modular-fiber certificate, arbitrary dimensions."""
from fractions import Fraction
from itertools import combinations, product

def distance(x):
    r=x%1
    return min(r,1-r)

def certificate(q,m,stable,moving,t0):
    assert all(a%m==0 and distance(a*t0)>=Fraction(1,q) for a in stable)
    sets=[{h for h in range(m) if distance(b*(t0+Fraction(h,m)))<Fraction(1,q)} for b in moving]
    terms=[]
    for r in range(1,len(sets)+1):
        terms.append(sum(len(set.intersection(*family)) for family in combinations(sets,r)))
    forbidden=sum((-1)**i*x for i,x in enumerate(terms))
    actual=len(set().union(*sets))
    assert forbidden==actual
    good=[h for h in range(m) if h not in set().union(*sets)]
    assert len(good)==m-forbidden
    return sets,terms,forbidden,good

def main():
    q,m=6,8
    A=(8,);B=(1,4,6,7);t0=Fraction(1,48)
    sets,terms,bad,good=certificate(q,m,A,B,t0)
    print('q,m,stable,moving,individual_sizes,inclusion_exclusion_terms,forbidden,valid_shifts,witness')
    print(q,m,A,B,[len(s) for s in sets],terms,bad,good,t0+Fraction(good[0],m),sep=',')
    assert bad==7 and good==[3]
    assert all(distance(v*(t0+Fraction(3,m)))>=Fraction(1,q) for v in A+B)
    for masks in product(range(8),repeat=4):
        ss=[{i for i in range(3) if mask>>i&1} for mask in masks]
        terms=[sum(len(set.intersection(*family)) for family in combinations(ss,r)) for r in range(1,5)]
        assert sum((-1)**i*x for i,x in enumerate(terms))==len(set().union(*ss))
    print('Exhaustive 4096 four-set systems: PASS')
if __name__=='__main__':main()
