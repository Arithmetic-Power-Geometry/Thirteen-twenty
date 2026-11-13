"""P03-06: exact indexed gcd-scaled calendar queries and independent oracle."""
from bisect import bisect_left
from fractions import Fraction as F
from random import Random
from time import perf_counter

def safe(t, a, b):
    def dist(x):
        z = x % 1
        return min(z, 1-z)
    return all(dist(t*v) >= F(1,16) for v in (a,b,a+b))

def components(a,b):
    cuts = {F(0),F(1)}
    for v in (a,b,a+b):
        for k in range(v+1):
            for sign in (-1,1):
                x = F(16*k+sign,16*v)
                if 0 <= x <= 1: cuts.add(x)
    points = sorted(cuts)
    elementary = [(l,u) for l,u in zip(points,points[1:]) if safe((l+u)/2,a,b)]
    merged = []
    for l,u in elementary:
        if merged and merged[-1][1] == l:
            merged[-1] = (merged[-1][0],u)
        else:
            merged.append((l,u))
    return merged

class CalendarIndex:
    def __init__(self, intervals):
        self.intervals = intervals
        self.ends = [u for _,u in intervals]
        self.n = len(intervals)
        self.size = 1
        while self.size < self.n: self.size *= 2
        self.tree = [F(0)] * (2*self.size)
        for i,(l,u) in enumerate(intervals):
            self.tree[self.size+i] = u-l
        for i in range(self.size-1,0,-1):
            self.tree[i] = max(self.tree[2*i],self.tree[2*i+1])

    def first_fit(self, start, need):
        def descend(node, lo, hi):
            if hi <= start or self.tree[node] < need: return None
            if hi-lo == 1: return lo if lo < self.n else None
            mid = (lo+hi)//2
            left = descend(node*2,lo,mid)
            return left if left is not None else descend(node*2+1,mid,hi)
        return descend(1,0,self.size)

def earliest_implicit(index, g, r, p, d):
    if p <= 0 or r >= 1 or r+p > d: return None
    R = g*r
    k = R.numerator // R.denominator
    if k >= g: return None
    x = R-k
    h = g*p
    j = bisect_left(index.ends, x)
    candidate = None
    if j < index.n:
        l,u = index.intervals[j]
        s = max(l,x)
        if s+h <= u: candidate = F(k)+s+h
    if candidate is None:
        i = index.first_fit(j+1,h)
        if i is not None:
            candidate = F(k)+index.intervals[i][0]+h
    if candidate is None and k+1 < g:
        i = index.first_fit(0,h)
        if i is not None:
            candidate = F(k+1)+index.intervals[i][0]+h
    if candidate is None: return None
    finish = candidate/g
    return finish if finish <= d else None

def earliest_oracle(intervals, r, p, d):
    if p <= 0: return None
    for l,u in intervals:
        f = max(l,r)+p
        if f <= u and f <= d: return f
    return None

def test():
    # Regression: elementary threshold cuts inside a connected safe interval
    # must NOT split a nonpreemptive processing window.
    assert components(1,1)[0] == (F(1,16), F(15,32))
    whole = CalendarIndex(components(1,1))
    assert earliest_implicit(whole,1,F(0),F(13,32),F(1)) == F(15,32)
    assert earliest_oracle(components(1,1),F(0),F(13,32),F(1)) == F(15,32)
    rng = Random(20261113)
    checked = 0
    for a,b in [(1,1),(1,14),(2,3),(3,5),(4,7),(5,9)]:
        primitive = components(a,b)
        index = CalendarIndex(primitive)
        for g in (1,2,3,5):
            explicit = components(g*a,g*b)
            for z in range(100):
                r = F(rng.randrange(65),64)
                p = F(rng.randrange(1,33),64)
                d = F(rng.randrange(65),64)
                if z==0: r=d=F(1)
                if z==1: r=F(0);d=F(1)
                if z==2 and primitive:
                    p=(primitive[0][1]-primitive[0][0])/g
                    r=F(0);d=F(1)
                got=earliest_implicit(index,g,r,p,d)
                want=earliest_oracle(explicit,r,p,d)
                assert got==want, (a,b,g,r,p,d,got,want)
                checked += 1
    print(f"PASS: {checked} exact indexed-versus-independent-oracle comparisons, zero mismatches")
    return checked

if __name__ == "__main__":
    test()
