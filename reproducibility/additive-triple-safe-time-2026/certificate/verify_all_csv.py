#!/usr/bin/env python3
"""Exact full coverage, rational inequality and equality verification for q=5,...,20."""
import csv,math,pathlib,collections
ROOT=pathlib.Path(__file__).resolve().parents[1]
files=sorted((ROOT/'results').glob('independent_q*_q*.csv'))
assert len(files)==4,files
seen=set();counts=collections.Counter();eq=collections.defaultdict(list)
for path in files:
    with path.open(newline='') as stream:
        for r in csv.DictReader(stream):
            q,a,b,n,d=(int(r[k]) for k in ('q','a','b','safe_numerator','denominator'))
            assert 5<=q<=20 and 1<=a<=b and math.gcd(a,b)==1
            B=(2*q*q*(q-1)+3*(q-3)-1)//(3*(q-3))
            assert b<B and (q,a,b) not in seen
            seen.add((q,a,b));counts[q]+=1
            assert d==q*a*b*(a+b) and 0<=n<=d
            diff=n*q*(q-1)-d*(q-3)*(q-4)
            assert diff>=0,(q,a,b)
            assert (diff==0)==bool(int(r['is_equality']))
            if diff==0:eq[q].append((a,b))
for q in range(5,21):
    B=(2*q*q*(q-1)+3*(q-3)-1)//(3*(q-3))
    expected=sum(math.gcd(a,b)==1 for b in range(1,B) for a in range(1,b+1))
    assert counts[q]==expected and eq[q]==[(1,q-2)],(q,counts[q],eq[q])
    print(f'q={q}: {counts[q]} primitive pairs; unique equality {eq[q][0]}')
assert sum(counts.values())==129568
print('PASS: 129568 distinct exact records, complete finite domains, no violations')
