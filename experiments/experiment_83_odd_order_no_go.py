#!/usr/bin/env python3
"""Experiment 83: exact rational verification of fixed-order Bonferroni no-go."""
from fractions import Fraction as F
from math import comb

def partial(n,m):
    return sum(((-1)**j*comb(n,j) for j in range(min(n,m)+1)))

def check_pointwise():
    checks=0
    for k in range(2,41):
        for m in range(1,k,2):
            for n in range(k+1):
                expected=(1 if n==0 else -comb(n-1,m))
                assert partial(n,m)==expected,(k,m,n)
                checks+=1
            assert F(2*comb(k-1,m),k*(k+1))>0
    return checks

def exact_consecutive(k):
    q=k+1
    pts={F(0),F(1)}
    for v in range(1,k+1):
        for n in range(v+1):
            for sign in (-1,1):
                t=F(q*n+sign,q*v)
                if 0<=t<=1:pts.add(t)
    pts=sorted(pts)
    hist=[F(0)]*(k+1)
    for a,b in zip(pts,pts[1:]):
        t=(a+b)/2
        N=sum(min((v*t)%1,1-(v*t)%1)<F(1,q) for v in range(1,k+1))
        hist[N]+=b-a
    assert sum(hist)==1 and hist[0]==0
    for m in range(1,k,2):
        cert=sum(((-1)**j*sum((comb(n,j)*hist[n] for n in range(j,k+1)),F(0)) for j in range(m+1)),F(0))
        defect=sum((comb(n-1,m)*hist[n] for n in range(1,k+1)),F(0))
        assert cert==-defect
        assert cert<=-F(2*comb(k-1,m),k*q)
        print("k",k,"order",m,"C_m",cert,"bound",-F(2*comb(k-1,m),k*q))
    return len(pts)-1

if __name__=="__main__":
    n=check_pointwise()
    cells=sum(exact_consecutive(k) for k in range(2,11))
    print("PASS",n,"pointwise identities and",cells,"exact rational cells")
