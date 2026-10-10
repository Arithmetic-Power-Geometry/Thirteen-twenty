#!/usr/bin/env python3
"""Experiment 85: exact nested-interval constructive LRC theorem."""
from fractions import Fraction as F

def ceil_fraction(x):
    return -((-x.numerator)//x.denominator)

def construct(speeds):
    v=tuple(speeds)
    k=len(v)
    if k<2 or min(v)<=0 or any(a>=b for a,b in zip(v,v[1:])):
        raise ValueError("strictly increasing positive speeds required")
    q=k+1
    d=F(1,q)
    threshold=F(2*k,k-1)
    if any(F(b,a)<threshold for a,b in zip(v,v[1:])):
        raise ValueError("growth hypothesis fails")
    left,right=d/v[0],(1-d)/v[0]
    stages=[(left,right)]
    for a in v[1:]:
        n=ceil_fraction(a*left-d)
        new_left,new_right=(n+d)/a,(n+1-d)/a
        assert left<=new_left<new_right<=right
        left,right=new_left,new_right
        stages.append((left,right))
    assert right-left==F(k-1,(k+1)*v[-1])
    for t in (left,(left+right)/2,right):
        assert all(min((a*t)%1,1-(a*t)%1)>=d for a in v)
    return left,right,stages

def audit():
    count=0
    for k in range(2,31):
        for multiplier in (1,2,3,5,11):
            for ratio in (4,5,7):
                v=[multiplier*ratio**j for j in range(k)]
                left,right,_=construct(v)
                assert right>left
                count+=1
        if k>=3:
            v=[3**j for j in range(k)]
            construct(v)
            count+=1
    assert count==464
    print("PASS:",count,"exact all-stage nested interval constructions")
    for v in ((1,4),(1,3,9),(1,3,9,27),(1,3,9,27,81)):
        a,b,_=construct(v)
        print("speeds",v,"safe interval",a,b,"length",b-a,"witness",(a+b)/2)

if __name__=="__main__":
    audit()
