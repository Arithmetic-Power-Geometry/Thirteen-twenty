#!/usr/bin/env python3
"""Experiment 86: exact rational safe-core and tail interval gluing."""
from fractions import Fraction as F

def ceil_q(x):
    return -((-x.numerator)//x.denominator)

def glue(k,core,interval,tail):
    q=k+1
    d=F(1,q)
    assert len(core)+len(tail)==k
    assert len(set(core+tail))==k and min(core+tail)>0
    left,right=interval
    assert left<right
    for t in (left,(left+right)/2,right):
        assert all(min((v*t)%1,1-(v*t)%1)>=d for v in core)
    for v in tail:
        assert v*(right-left)>=2*(1-d)
        n=ceil_q(v*left-d)
        newleft,newright=(n+d)/v,(n+1-d)/v
        assert left<=newleft<newright<=right
        left,right=newleft,newright
        for t in (left,(left+right)/2,right):
            assert all(min((a*t)%1,1-(a*t)%1)>=d for a in core+tail[:tail.index(v)+1])
    assert right-left==F(k-1,(k+1)*tail[-1])
    return left,right

def hybrid(k,scale=1):
    assert k>=4
    d=F(1,k+1)
    core=[scale,2*scale,3*scale]
    # Scaling all speeds by scale divides the original core interval by scale.
    I=(d/scale,(1-d)/(3*scale))
    width=I[1]-I[0]
    b=3*scale
    tail=[]
    for j in range(k-3):
        needed=2*(1-d)/width
        b=max(b+1,ceil_q(needed))
        tail.append(b)
        width=(1-2*d)/b
    return core+tail,glue(k,core,I,tail)

def main():
    count=0
    for k in range(4,31):
        for scale in (1,2,3,5,11):
            v,I=hybrid(k,scale)
            assert I[1]>I[0]
            count+=1
    v,I=hybrid(6)
    assert v==[1,2,3,12,29,70],v
    assert I[1]-I[0]==F(1,98)
    print("PASS",count,"exact hybrid constructions, k=4..30")
    print("k=6 speeds",v,"safe interval",I,"length",I[1]-I[0])

if __name__=="__main__":
    main()
