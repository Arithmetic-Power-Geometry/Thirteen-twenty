"""P03-17: equal wall-clock bounded subprocess comparison of exact DP and CP-SAT.

Both solvers receive identical cases, separate fresh processes, and the same
external wall-time budget. Timeout is a reported outcome, not an error or an
invented optimality certificate. CP-SAT internally also has a 15-second limit,
but the parent-enforced 2-second wall budget is stricter.
"""
import argparse
import json
import subprocess
import sys
from fractions import Fraction as F
from random import Random
from time import perf_counter
from pathlib import Path

from p03_06_indexed_implicit_query import components
from p03_12_exact_weighted_scheduling import exact_opt
from p03_14_cpsat_independent import cpsat_opt

WALL_BUDGET_SECONDS=2.0

def instance(a,b,n,seed):
    rng=Random(seed)
    jobs=[]
    for _ in range(n):
        r=F(rng.randrange(17),16)
        d=F(rng.randrange(17),16)
        if r>d:r,d=d,r
        p=F(rng.randrange(1,9),32)
        w=F(rng.randrange(1,11))
        jobs.append((r,p,d,w))
    return components(a,b),jobs

def worker(solver,a,b,n,seed):
    intervals,jobs=instance(a,b,n,seed)
    optimum=exact_opt(intervals,jobs) if solver=="dp" else cpsat_opt(intervals,jobs)
    print(json.dumps({"status":"optimal","value":str(optimum)}),flush=True)

def bounded(solver,a,b,n,seed):
    cmd=[sys.executable,str(Path(__file__).resolve()),"--worker",solver,
         str(a),str(b),str(n),str(seed)]
    t0=perf_counter()
    try:
        result=subprocess.run(cmd,text=True,capture_output=True,
                              timeout=WALL_BUDGET_SECONDS,check=False)
    except subprocess.TimeoutExpired:
        return {"status":"timeout","seconds":WALL_BUDGET_SECONDS}
    elapsed=perf_counter()-t0
    if result.returncode!=0:
        return {"status":"error","seconds":elapsed,
                "message":result.stderr[-500:]}
    try:
        record=json.loads(result.stdout.strip())
    except (ValueError,TypeError):
        return {"status":"error","seconds":elapsed,"message":"invalid worker output"}
    return {**record,"seconds":elapsed}

def run():
    rows=[]
    for a,b in ((1,1),(1,14),(2,3)):
        for n in (8,12,16):
            seed=20261113+100*a+10*b+n
            dp=bounded("dp",a,b,n,seed)
            cp=bounded("cp",a,b,n,seed)
            if dp["status"]=="optimal" and cp["status"]=="optimal":
                assert dp["value"]==cp["value"],(a,b,n,dp,cp)
            rows.append((a,b,n,dp,cp))
            print("CASE "+json.dumps({"a":a,"b":b,"jobs":n,"dp":dp,"cpsat":cp},
                                     sort_keys=True),flush=True)
    matches=sum(d["status"]=="optimal" and c["status"]=="optimal"
                for _,_,_,d,c in rows)
    errors=sum(x["status"]=="error" for _,_,_,d,c in rows for x in (d,c))
    assert errors==0, "Solver errors must be fixed, not silently counted as timeouts"
    print(f"PASS: {len(rows)} matched cases; {matches} jointly proven optima; "
          f"zero mismatches; budget={WALL_BUDGET_SECONDS}s per solver "
          "including fresh Python startup; timeouts retained",flush=True)

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--worker",choices=("dp","cp"))
    p.add_argument("a",type=int,nargs="?")
    p.add_argument("b",type=int,nargs="?")
    p.add_argument("n",type=int,nargs="?")
    p.add_argument("seed",type=int,nargs="?")
    args=p.parse_args()
    if args.worker:
        worker(args.worker,args.a,args.b,args.n,args.seed)
    else:
        run()
