#!/usr/bin/env python3
"""Experiment 29: exact bounded search for a global reciprocal-threshold minimizer.
Run: python3 src/experiment_29_scan.py [max_b]
Prints one CSV row per q. No numerical floating-point comparisons.
"""
from math import gcd
from fractions import Fraction
import sys

QS = [5,6,7,8,9,10,12,16,20,24,32]

def measure(q,a,b):
    c=a+b
    D=q*a*b*c
    cuts={0,D}
    for v in (a,b,c):
        step=D//(q*v)
        for j in range(v):
            cuts.add((q*j+1)*step)
            cuts.add((q*(j+1)-1)*step)
    points=sorted(cuts)
    period=2*D
    good=0
    for L,U in zip(points,points[1:]):
        mid2=L+U
        if all(q*min((v*mid2)%period,period-(v*mid2)%period)>=period for v in (a,b,c)):
            good+=U-L
    return Fraction(good,D)

def run(limit=100):
    print("q,pairs_tested,minimum_numerator,minimum_denominator,number_of_minimizers,minimizers,formula_matches")
    for q in QS:
        minimum=None
        pairs=[]
        count=0
        for b in range(1,limit+1):
            for a in range(1,b+1):
                if gcd(a,b)!=1: continue
                count+=1
                f=measure(q,a,b)
                if minimum is None or f<minimum:
                    minimum=f
                    pairs=[(a,b)]
                elif f==minimum:
                    pairs.append((a,b))
        formula=Fraction((q-3)*(q-4),q*(q-1))
        print(f"{q},{count},{minimum.numerator},{minimum.denominator},{len(pairs)},"
              f"\"{' '.join(f'{a}:{b}' for a,b in pairs)}\",{int(minimum==formula)}")
if __name__=="__main__":
    run(int(sys.argv[1]) if len(sys.argv)>1 else 100)
