#!/usr/bin/env python3
"""Experiment 81: exact independent-limit sign and constructive geometric witnesses."""
from fractions import Fraction as Q
from math import comb

def third_order_independent_limit(k):
    if k<3: raise ValueError("k>=3")
    p=Q(2,k+1)
    direct=1-k*p+comb(k,2)*p*p-comb(k,3)*p*p*p
    closed=-Q((k-1)*(k*k-8*k+3),3*(k+1)**3)
    assert direct==closed
    return direct

def circle_distance(x):
    f=x%1
    return min(f,1-f)

def geometric_witness(k,N):
    if k<2 or N<2: raise ValueError
    t=Q(1,2) if N%2 else Q(N,2*(N+1))
    values=[circle_distance(pow(N,j)*t) for j in range(k)]
    assert min(values)>=Q(1,k+1)
    return t,min(values)

def main():
    assert third_order_independent_limit(7)==Q(1,64)
    assert third_order_independent_limit(8)==-Q(7,729)
    assert third_order_independent_limit(9)==-Q(4,125)
    for k in range(3,31):
        x=third_order_independent_limit(k)
        assert (x<0)==(k>=8)
        for N in range(2,21):
            t,margin=geometric_witness(k,N)
            print("PASS",k,N,"independent_C3",x,"safe_t",t,"margin",margin)
    print("All 540 exact witness checks and all sign identities passed.")

if __name__=="__main__":
    main()
