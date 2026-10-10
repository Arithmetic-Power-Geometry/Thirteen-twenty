#!/usr/bin/env python3
"""Experiment 36: exact rational safe-time measure for arbitrary integer speeds."""
from fractions import Fraction
from math import lcm
def safe_measure(q, speeds):
    D=q
    for v in speeds: D=lcm(D,q*abs(v))
    cuts={0,D}
    for v in speeds:
        v=abs(v)
        s=D//(q*v)
        for j in range(v):
            cuts.add((q*j+1)*s)
            cuts.add((q*(j+1)-1)*s)
    pts=sorted(cuts); good=0
    for lo,hi in zip(pts,pts[1:]):
        mid2=lo+hi;P=2*D
        if all(q*min((v*mid2)%P,P-(v*mid2)%P)>=P for v in speeds):
            good+=hi-lo
    return Fraction(good,D)
if __name__=="__main__":
    cases=[(5,(1,2,3),Fraction(2,15)),(5,(1,2,4),Fraction(1,5)),(16,(1,14,15),Fraction(13,20))]
    for q,v,expected in cases:
        got=safe_measure(q,v)
        print(q,v,str(got),str(Fraction(q-2,q)**len(v)))
        assert got==expected
