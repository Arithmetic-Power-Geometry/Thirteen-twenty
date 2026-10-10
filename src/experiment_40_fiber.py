#!/usr/bin/env python3
"""Experiment 40: exact modular-fiber certificate in arbitrary dimensions."""
from fractions import Fraction
from math import gcd
def distance(x):
 y=x%1
 return min(y,1-y)
def fiber(q,m,stable,moving,t0):
 assert all(v%m==0 for v in stable)
 assert all(distance(v*t0)>=Fraction(1,q) for v in stable)
 counts=[]
 for v in moving:
  g=gcd(v,m);orbit=m//g
  bound=g*((2*orbit+q-1)//q)
  bad=sum(distance(v*(t0+Fraction(h,m)))<Fraction(1,q) for h in range(m))
  assert bad<=bound,(v,bad,bound)
  counts.append((v,g,orbit,bad,bound))
 witnesses=[(h,t0+Fraction(h,m)) for h in range(m) if all(distance(v*(t0+Fraction(h,m)))>=Fraction(1,q) for v in stable+moving)]
 return counts,witnesses
def main():
 cases=[(6,11,[11,22,33],[1,2],Fraction(1,66)),(16,31,[31*i for i in range(1,11)],list(range(1,6)),Fraction(1,496))]
 print('q,m,k,stable,moving,sum_upper_bounds,actual_successful_shifts,first_witness')
 for q,m,A,B,t0 in cases:
  c,w=fiber(q,m,A,B,t0)
  print(f'{q},{m},{len(A)+len(B)},{len(A)},{len(B)},{sum(x[4] for x in c)},{len(w)},{w[0][1]}')
  print('per_runner(v,g,orbit,bad,bound):',c)
  assert sum(x[4] for x in c)<m and w
 for q in range(3,9):
  for m in range(2,20):
   for v in range(1,2*m+1):
    g=gcd(v,m);orbit=m//g
    bound=g*((2*orbit+q-1)//q)
    for d in range(0,2*q):
     t0=Fraction(d,2*q*m)
     bad=sum(distance(v*(t0+Fraction(h,m)))<Fraction(1,q) for h in range(m))
     assert bad<=bound,(q,m,v,d,bad,bound)
 print('Exhaustive bounded-orbit tests: passed.')
if __name__=='__main__':main()
