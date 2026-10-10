#!/usr/bin/env python3
"""Experiment 33, independent exact rational finite certificate for q=18."""
from math import gcd
Q=18
B=(2*Q*Q*(Q-1)+3*(Q-3)-1)//(3*(Q-3))
def measure(a,b):
    c=a+b;D=Q*a*b*c;P=2*D
    cuts={0,D}
    for v in (a,b,c):
        step=D//(Q*v)
        for j in range(v):
            cuts.add((Q*j+1)*step)
            cuts.add((Q*(j+1)-1)*step)
    ends=sorted(cuts);safe=0
    for L,U in zip(ends,ends[1:]):
        m=L+U
        if all(Q*min((v*m)%P,P-(v*m)%P)>=P for v in (a,b,c)):
            safe+=U-L
    return safe,D
if __name__=="__main__":
    count=viol=eq=0;pairs=[]
    for b in range(1,B):
        for a in range(1,b+1):
            if gcd(a,b)!=1:continue
            n,d=measure(a,b);count+=1
            diff=n*Q*(Q-1)-d*(Q-3)*(Q-4)
            if diff<0:viol+=1
            if diff==0:eq+=1;pairs.append((a,b))
    print(dict(q=Q,cutoff=B,checked=count,violations=viol,equalities=eq,pairs=pairs))
    assert (B,count,viol,eq,pairs)==(245,18176,0,1,[(1,16)])
