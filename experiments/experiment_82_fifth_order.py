#!/usr/bin/env python3
"""Experiment 82: exact algebra and pointwise fifth-order certificate tests."""
from fractions import Fraction as Q
from math import comb

def c5_limit(k):
    if k<5: raise ValueError("k>=5")
    p=Q(2,k+1)
    return sum(((-1)**j*comb(k,j)*p**j for j in range(6)),Q(0))

def factored(k):
    return Q((k-1)*(k**4+26*k**3-34*k**2+166*k-15),15*(k+1)**5)

def pointwise_bound(n):
    lower=sum(((-1)**j*comb(n,j) for j in range(min(n,5)+1)))
    assert lower == (1 if n==0 else -comb(n-1,5) if n>=6 else 0)
    assert lower <= int(n==0)

def safe_witness(k,N):
    t=Q(1,2) if N%2 else Q(N,2*(N+1))
    for j in range(k):
        x=(pow(N,j)*t)%1
        assert min(x,1-x)>=Q(1,k+1)
    return t

def main():
    for n in range(201):pointwise_bound(n)
    for k in range(5,201):
        a,b=c5_limit(k),factored(k)
        assert a==b and a>0,(k,a,b)
    for k in range(5,21):
        for N in range(2,13):
            safe_witness(k,N)
    assert c5_limit(8)>0
    print("PASS: 201 pointwise inequalities, 196 polynomial identities and positivity checks, 176 explicit safe witnesses.")
    for k in (5,7,8,9,10,20,100):
        print("k",k,"fifth-order asymptotic certificate",c5_limit(k))

if __name__=="__main__":main()
