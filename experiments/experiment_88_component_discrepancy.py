#!/usr/bin/env python3
"""Experiment 88: exact rational verification of component-sensitive safe-measure bound."""
from fractions import Fraction as F
from math import floor, ceil

def intersection(intervals, v, q):
    d = F(1, q)
    out = []
    for L, R in intervals:
        for n in range(floor(v*L)-1, ceil(v*R)+2):
            a = max(L, (n+d)/v)
            b = min(R, (n+1-d)/v)
            if a < b:
                out.append((a, b))
    return out

def measure(intervals):
    return sum((b-a for a,b in intervals), F(0))

def check(intervals, v, q):
    m = len(intervals)
    A = measure(intervals)
    d = F(1, q)
    actual = measure(intersection(intervals, v, q))
    lower = (1-2*d)*(A-2*d*m/v)
    assert actual >= lower, (intervals, v, q, actual, lower)
    return actual, lower

def main():
    count = 0
    for q in range(3,13):
        for v in range(1,25):
            for a in range(11):
                I = [(F(a,11), F(a+1,11))]
                check(I,v,q)
                count += 1
                if a < 9:
                    I2 = [(F(a,11), F(a+1,11)), (F(a+2,11), F(a+3,11))]
                    check(I2,v,q)
                    count += 1
    assert count == 4800
    actual, lower = check([(F(1,7), F(2,7))], 4, 7)
    assert (actual,lower) == (F(1,14),F(5,98))
    print("PASS:",count,"exact rational overlap tests")
    print("Example: actual",actual,"certified lower bound",lower)

if __name__ == "__main__":
    main()
