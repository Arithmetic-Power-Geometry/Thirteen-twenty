#!/usr/bin/env python3
"""Experiment 43: exact O(sum speeds) boundary witness decision for integer speeds."""
from fractions import Fraction
from itertools import combinations

def witness(q, speeds):
    speeds=tuple(sorted(set(speeds)))
    if q<2 or not speeds or any(not isinstance(v,int) or v<=0 for v in speeds):
        raise ValueError("q>=2, nonempty positive integer speeds")
    endpoints={Fraction(0)}
    for v in speeds:
        for j in range(v+1):
            for sign in (-1,1):
                t=Fraction(q*j+sign,q*v)
                if 0<=t<=1:endpoints.add(t)
    for t in sorted(endpoints):
        if all(q*min((v*t)%1,1-(v*t)%1)>=1 for v in speeds):
            return t,len(endpoints)
    return None,len(endpoints)

if __name__=="__main__":
    print("k,number_of_speed_sets,max_boundary_candidates,failures")
    for k in range(2,7):
        count=fail=max_candidates=0
        for speeds in combinations(range(1,13),k):
            t,n=witness(k+1,speeds)
            count+=1;max_candidates=max(max_candidates,n)
            if t is None:fail+=1
        print(k,count,max_candidates,fail,sep=",")
        assert fail==0
    for v in [(8,1,4,6,7),tuple(range(1,16)),(16,17,18,19,20)]:
        print("example",v,witness(len(v)+1,v))
