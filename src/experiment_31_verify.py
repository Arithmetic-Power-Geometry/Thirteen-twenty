#!/usr/bin/env python3
"""Experiment 31: exact independent finite certificates for q=11..16.
No third-party libraries. Run python3 src/experiment_31_verify.py
"""
from math import gcd

def measure(q,a,b):
    c=a+b
    D=q*a*b*c
    P=2*D
    cuts={0,D}
    for v in (a,b,c):
        s=D//(q*v)
        for j in range(v):
            cuts.add((q*j+1)*s)
            cuts.add((q*(j+1)-1)*s)
    pts=sorted(cuts)
    good=0
    for lo,hi in zip(pts,pts[1:]):
        m=lo+hi
        if all(q*min((v*m)%P,P-(v*m)%P)>=P for v in (a,b,c)):
            good+=hi-lo
    return good,D

def main():
    print("q,cutoff,finite_pairs,violations,equalities,equality_pair")
    for q in range(11,17):
        B=(2*q*q*(q-1)+3*(q-3)-1)//(3*(q-3))
        count=viol=eq=0
        equality_pair=""
        for b in range(1,B):
            for a in range(1,b+1):
                if gcd(a,b)!=1:
                    continue
                n,d=measure(q,a,b)
                count+=1
                diff=n*q*(q-1)-d*(q-3)*(q-4)
                if diff<0:
                    viol+=1
                if diff==0:
                    eq+=1
                    equality_pair=f"{a}:{b}"
        print(f"{q},{B},{count},{viol},{eq},{equality_pair}")
        assert viol==0 and eq==1 and equality_pair==f"1:{q-2}"
if __name__=="__main__":
    main()
