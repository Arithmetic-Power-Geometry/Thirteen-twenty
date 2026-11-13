"""P03-07 fair exact calendar query benchmark; timings are machine-specific."""
from fractions import Fraction as F
from random import Random
from statistics import median
from time import perf_counter
from p03_06_indexed_implicit_query import CalendarIndex, components, earliest_implicit

def explicit_indexed(index, r, p, d):
    if p <= 0 or r >= 1 or r+p > d: return None
    from bisect import bisect_left
    j=bisect_left(index.ends,r)
    if j < index.n:
        l,u=index.intervals[j]
        s=max(l,r)
        if s+p<=u:
            f=s+p
            return f if f<=d else None
    i=index.first_fit(j+1,p)
    if i is None:return None
    f=index.intervals[i][0]+p
    return f if f<=d else None

def bench(a,b,g,qcount=2000,repeats=3):
    rng=Random(20261113+g)
    queries=[]
    for _ in range(qcount):
        r=F(rng.randrange(0,1000),1000)
        p=F(rng.randrange(1,100),2000)
        d=F(rng.randrange(0,1001),1000)
        queries.append((r,p,d))
    times=[]
    for _ in range(repeats):
        t=perf_counter()
        primitive=CalendarIndex(components(a,b))
        implicit_build=perf_counter()-t
        t=perf_counter()
        expanded=CalendarIndex(components(g*a,g*b))
        explicit_build=perf_counter()-t
        t=perf_counter()
        implicit_results=[earliest_implicit(primitive,g,*query) for query in queries]
        implicit_query=perf_counter()-t
        t=perf_counter()
        explicit_results=[explicit_indexed(expanded,*query) for query in queries]
        explicit_query=perf_counter()-t
        assert implicit_results==explicit_results, (a,b,g)
        times.append((implicit_build,explicit_build,implicit_query,explicit_query))
    m=[median(x[i] for x in times) for i in range(4)]
    print(f"pair=({a},{b}) g={g} queries={qcount} "
          f"primitive_components={primitive.n} expanded_components={expanded.n} "
          f"build_implicit_s={m[0]:.6f} build_explicit_s={m[1]:.6f} "
          f"query_implicit_s={m[2]:.6f} query_explicit_s={m[3]:.6f} "
          "mismatches=0")

if __name__=="__main__":
    for a,b in [(1,14),(2,3)]:
        for g in (1,2,5,10):
            bench(a,b,g)
