#!/usr/bin/env python3
"""Experiment 27: exact rational verification of a candidate closed formula.
Run: python3 src/experiment_27_exact.py [max_q]
No third-party dependencies. Not a proof for unbounded q.
"""
from fractions import Fraction
from math import gcd
import sys

def measure(q):
    if q < 5:
        raise ValueError("q must be at least 5")
    a,b,c=1,q-2,q-1
    D=q*b*c
    endpoints={0,D}
    for v in (a,b,c):
        step=D//(q*v)
        for j in range(v):
            endpoints.add((q*j+1)*step)
            endpoints.add((q*(j+1)-1)*step)
    pts=sorted(endpoints)
    good=0
    for L,U in zip(pts,pts[1:]):
        midpoint2=L+U
        period=2*D
        if all(q*min((v*midpoint2)%period,period-(v*midpoint2)%period)>=period for v in (a,b,c)):
            good+=U-L
    return Fraction(good,D)

def candidate(q):
    return Fraction((q-3)*(q-4),q*(q-1))

if __name__=="__main__":
    hi=int(sys.argv[1]) if len(sys.argv)>1 else 200
    for q in range(5,hi+1):
        exact=measure(q)
        expected=candidate(q)
        assert exact==expected,(q,exact,expected)
        if q in (5,6,8,16,20,32,hi):
            print(q,exact)
    print(f"All {hi-4} exact cases matched; no universal proof implied.")
