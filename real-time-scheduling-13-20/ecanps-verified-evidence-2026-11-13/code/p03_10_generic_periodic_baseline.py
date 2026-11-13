"""P03-10: generic periodic index vs arithmetic-scaled index.

GenericPeriodicCalendar receives physical period, block count and within-period
intervals. It does NOT receive arithmetic frequencies (a,b) or their gcd.
All calculations use Fraction; no third-party dependencies.
"""
from bisect import bisect_left
from fractions import Fraction as F
from random import Random

from p03_06_indexed_implicit_query import (
    CalendarIndex, components, earliest_implicit, earliest_oracle,
)

class GenericPeriodicCalendar:
    def __init__(self, within_period, period, repetitions):
        if period <= 0 or repetitions < 1:
            raise ValueError("positive period and repetitions required")
        self.period = period
        self.repetitions = repetitions
        self.index = CalendarIndex(within_period)
        if any(not (0 <= l < u <= period) for l,u in within_period):
            raise ValueError("components must lie inside one period")
        if any(within_period[i][1] >= within_period[i+1][0]
               for i in range(len(within_period)-1)):
            raise ValueError("components must be strictly separated")

    def earliest(self, r, p, d):
        if p <= 0 or r >= self.period*self.repetitions or r+p > d:
            return None
        k = r // self.period
        if k >= self.repetitions:
            return None
        x = r-k*self.period
        ix = self.index
        j = bisect_left(ix.ends,x)
        finish = None
        if j < ix.n:
            l,u = ix.intervals[j]
            start = max(x,l)
            if start+p <= u:
                finish = k*self.period+start+p
        if finish is None:
            i = ix.first_fit(j+1,p)
            if i is not None:
                finish = k*self.period+ix.intervals[i][0]+p
        if finish is None and k+1 < self.repetitions:
            i = ix.first_fit(0,p)
            if i is not None:
                finish = (k+1)*self.period+ix.intervals[i][0]+p
        return finish if finish is not None and finish <= d else None

def run():
    rng = Random(20261113)
    count = 0
    for a,b in ((1,1),(1,14),(2,3),(3,5),(4,7),(5,9)):
        prim = components(a,b)
        arithmetic = CalendarIndex(prim)
        for g in (1,2,3,5,10):
            generic = GenericPeriodicCalendar(
                [(l/g,u/g) for l,u in prim], F(1,g), g)
            expanded = components(g*a,g*b)
            for z in range(100):
                r = F(rng.randrange(1001),1000)
                p = F(rng.randrange(1,301),1000)
                d = F(rng.randrange(1001),1000)
                if z==0: r=d=F(1)
                if z==1: r=F(0);d=F(1)
                if z==2 and prim:
                    p = (prim[0][1]-prim[0][0])/g
                    r=F(0);d=F(1)
                actual = generic.earliest(r,p,d)
                arithmetic_answer = earliest_implicit(arithmetic,g,r,p,d)
                oracle = earliest_oracle(expanded,r,p,d)
                assert actual == arithmetic_answer == oracle, (
                    a,b,g,r,p,d,actual,arithmetic_answer,oracle)
                count += 1
    # A generic non-arithmetic repeating calendar also works.
    pattern = [(F(1,10),F(1,5)),(F(2,5),F(3,5))]
    generic = GenericPeriodicCalendar(pattern,F(1),3)
    expanded = [(k+l,k+u) for k in range(3) for l,u in pattern]
    for _ in range(1000):
        r = F(rng.randrange(3001),1000)
        p = F(rng.randrange(1,701),1000)
        d = F(rng.randrange(3001),1000)
        assert generic.earliest(r,p,d) == earliest_oracle(expanded,r,p,d)
        count += 1
    print(f"PASS: {count} exact generic-periodic comparisons, zero mismatches")
    print("Novelty finding: periodic compression does not require additive frequencies.")

if __name__ == "__main__":
    run()
