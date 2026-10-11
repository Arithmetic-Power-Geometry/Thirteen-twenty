#!/usr/bin/env python3
"""Exact forbidden-interval union certificate for q=5,...,20."""
import argparse,csv,math,pathlib,hashlib
def measure(q,a,b):
    c=a+b; D=q*a*b*c
    intervals=[]
    for v in (a,b,c):
        step=D//(q*v)
        for j in range(v+1):
            lo=max(0,(q*j-1)*step)
            hi=min(D,(q*j+1)*step)
            if lo<hi: intervals.append((lo,hi))
    intervals.sort()
    covered=0;left=right=0
    for lo,hi in intervals:
        if lo>right:
            covered+=right-left
            left,right=lo,hi
        else: right=max(right,hi)
    covered+=right-left
    return D-covered,D
def main():
    p=argparse.ArgumentParser();p.add_argument('--q-start',type=int,default=5);p.add_argument('--q-end',type=int,default=8);p.add_argument('--out',default=None);args=p.parse_args()
    out=pathlib.Path(args.out or pathlib.Path(__file__).resolve().parents[1]/'results'/'independent_q5_q8.csv')
    out.parent.mkdir(parents=True,exist_ok=True)
    with out.open('w',newline='') as fh:
        w=csv.writer(fh);w.writerow(['q','a','b','safe_numerator','denominator','is_equality'])
        for q in range(args.q_start,args.q_end+1):
            B=(2*q*q*(q-1)+3*(q-3)-1)//(3*(q-3))
            n=0;eq=[]
            for b in range(1,B):
                for a in range(1,b+1):
                    if math.gcd(a,b)!=1:continue
                    x,d=measure(q,a,b);n+=1
                    lhs=x*q*(q-1);rhs=d*(q-3)*(q-4)
                    assert lhs>=rhs,(q,a,b,x,d)
                    if lhs==rhs:eq.append((a,b))
                    w.writerow((q,a,b,x,d,int(lhs==rhs)))
            assert eq==[(1,q-2)],(q,eq)
            print(f'q={q} cutoff={B} pairs={n} equality={eq} violations=0')
    print('SHA256',hashlib.sha256(out.read_bytes()).hexdigest())
if __name__=='__main__':main()
