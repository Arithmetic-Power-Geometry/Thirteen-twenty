"""Deterministic CS-010 benchmark; outputs JSON with raw timings.

Run from project root: python3 experiments/cs010_benchmark.py
No third-party dependencies. Does NOT certify algorithmic novelty.
"""
import hashlib
import json
import platform
import random
import statistics
import sys
import time
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from exact_admission import safe_windows,admit
from baseline_admission import linear_query,binary_query,AdmissionIndex
from multi_job_equal import decide_equal_jobs
from certificate_verifier import verify_yes_certificate,verify_no_capacity_certificate


def digest():
    paths=[Path(__file__).resolve().parents[1]/p for p in
           ("exact_admission.py","baseline_admission.py","multi_job_equal.py",
            "certificate_verifier.py","robustness.py")]
    return {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}


def run():
    rng=random.Random(13020)
    rows=[]
    for a,b in ((1,14),(7,23),(19,61),(1,128),(37,131)):
        t0=time.perf_counter_ns()
        windows=safe_windows(a,b)
        build_windows_ns=time.perf_counter_ns()-t0
        t0=time.perf_counter_ns()
        index=AdmissionIndex(a,b)
        build_index_ns=time.perf_counter_ns()-t0
        jobs=[]
        for _ in range(120):
            r=F(rng.randrange(0,1000),1000)
            d=min(F(1),r+F(rng.randrange(1,301),1000))
            p=F(rng.randrange(1,101),1000)
            jobs.append((r,d,p))
        timings={}
        for name,fn in (("linear",lambda r,d,p:linear_query(windows,r,d,p)),
                        ("binary_scan",lambda r,d,p:binary_query(windows,r,d,p)),
                        ("segment_tree",lambda r,d,p:index.query(r,d,p))):
            samples=[]
            for r,d,p in jobs:
                t0=time.perf_counter_ns()
                answer=fn(r,d,p)
                samples.append(time.perf_counter_ns()-t0)
                expected=admit(a,b,r,d,p)
                if (expected[1] if expected[0]=="YES" else None)!=answer:
                    raise AssertionError((a,b,name,r,d,p,answer,expected))
            timings[name]={"median_ns":statistics.median(samples),
                           "p95_ns":sorted(samples)[int(.95*(len(samples)-1))],
                           "total_ns":sum(samples)}
        for count in (1,4):
            outcome=decide_equal_jobs(a,b,0,1,F(1,100),count)
            if outcome["decision"]=="YES":
                assert verify_yes_certificate(a,b,0,1,F(1,100),count,outcome["schedule"])
            else:
                assert verify_no_capacity_certificate(a,b,0,1,F(1,100),count,outcome["capacity"])
        rows.append({"a":a,"b":b,"components":len(windows),
                     "queries":len(jobs),"safe_window_build_ns":build_windows_ns,
                     "index_build_ns":build_index_ns,"query_timings":timings})
    return {"status":"completed","python":sys.version,"platform":platform.platform(),
            "seed":13020,"source_sha256":digest(),"cases":rows,
            "notes":"single-run timings; not statistically sufficient for performance claims"}


if __name__=="__main__":
    print(json.dumps(run(),indent=2,sort_keys=True))
