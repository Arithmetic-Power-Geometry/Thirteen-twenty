#!/usr/bin/env python3
"""Experiment 80: exact third-order Bonferroni LRC certificate."""
from fractions import Fraction as F
from itertools import combinations

def intersection_measure(speeds,q):
    """Measure of simultaneous STRICT forbidden arcs, exactly."""
    points={F(0),F(1)}
    for a in speeds:
        for n in range(a+1):
            for sign in (-1,1):
                t=F(q*n+sign,q*a)
                if F(0)<=t<=F(1):points.add(t)
    pts=sorted(points)
    result=F(0)
    for left,right in zip(pts,pts[1:]):
        mid=(left+right)/2
        if all(min((a*mid)%1,1-(a*mid)%1)<F(1,q) for a in speeds):
            result+=right-left
    return result

def third_order_certificate(speeds):
    v=tuple(speeds)
    k=len(v)
    if k<3 or min(v)<=0 or len(set(v))!=k:
        raise ValueError("At least three distinct positive integer speeds required")
    q=k+1
    s2=sum((intersection_measure(p,q) for p in combinations(v,2)),F(0))
    s3=sum((intersection_measure(p,q) for p in combinations(v,3)),F(0))
    lower=F(1)-F(2*k,q)+s2-s3
    return s2,s3,lower

def exact_safe_measure(v):
    q=len(v)+1
    pts={F(0),F(1)}
    for a in v:
        for n in range(a+1):
            for sign in (-1,1):
                t=F(q*n+sign,q*a)
                if F(0)<=t<=F(1):pts.add(t)
    pts=sorted(pts)
    total=F(0)
    for left,right in zip(pts,pts[1:]):
        t=(left+right)/2
        if all(min((a*t)%1,1-(a*t)%1)>=F(1,q) for a in v):
            total+=right-left
    return total

def audit():
    examples=[
        ((11,13,17,19),F(221262,230945),F(59522,230945),F(23173,230945)),
        ((1,2,4,8),F(19,20),F(3,10),F(1,20)),
        ((1,3,5,7),F(164,175),F(48,175),F(11,175)),
        ((1,2,3,4),F(14,15),F(13,30),-F(1,10)),
        ((1,3,4,7),F(37,42),F(71,210),-F(2,35)),
    ]
    for v,a,b,c in examples:
        s2,s3,lower=third_order_certificate(v)
        assert (s2,s3,lower)==(a,b,c),(v,s2,s3,lower)
        exact=exact_safe_measure(v)
        assert exact>=lower,(v,exact,lower)
        print("PASS",v,"S2",s2,"S3",s3,"Bonferroni",lower,"exact_safe_measure",exact)
    print("All exact arithmetic tests passed")

if __name__=="__main__":
    audit()
