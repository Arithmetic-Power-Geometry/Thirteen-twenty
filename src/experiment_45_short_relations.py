#!/usr/bin/env python3
"""Exact short-relation enumeration for the Beck–Everett 2026 criterion."""
from itertools import combinations, product

def short_relation(speeds, budget=None):
    speeds=tuple(int(x) for x in speeds)
    assert len(speeds)>=2 and all(x>0 for x in speeds)
    k=len(speeds); budget=2*k+3 if budget is None else budget
    def visit(i,remaining,total,coeff,used):
        if i==k:
            if used and total==0:return tuple(coeff)
            return None
        for a in range(-remaining,remaining+1):
            result=visit(i+1,remaining-abs(a),total+a*speeds[i],coeff+[a],used or a!=0)
            if result is not None:return result
        return None
    return visit(0,budget,0,[],False)

def main():
    cases=[(1,50,2500,125000),(101,103,107,109),(1,3,9,27),(1,20,400,8000)]
    print('speeds,budget,relation,classification')
    for speeds in cases:
        relation=short_relation(speeds)
        status='strict_safe_by_Beck_Everett' if relation is None else 'inconclusive'
        print('"'+':'.join(map(str,speeds))+'",'+str(2*len(speeds)+3)+',"'+('none' if relation is None else ':'.join(map(str,relation)))+'",'+status)
        if relation is not None:
            assert sum(a*v for a,v in zip(relation,speeds))==0
            assert 0<sum(map(abs,relation))<=2*len(speeds)+3
    checks=0
    for k in (2,3):
        B=2*k+3
        for speeds in combinations(range(1,8),k):
            found=short_relation(speeds)
            brute=any(any(a) and sum(map(abs,a))<=B and sum(x*y for x,y in zip(a,speeds))==0 for a in product(range(-B,B+1),repeat=k))
            assert (found is not None)==brute
            checks+=1
    print('independent_brute_force_crosschecks',checks)
if __name__=='__main__':main()
