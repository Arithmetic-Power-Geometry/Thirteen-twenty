"""P03-23 finite-certificate integrity gate.

Runs the existing independent integer-union verifier once and checks its
reported full-range count, extremum, and canonical ordered-record digest.
Does not modify the historical Thirteen-twenty repository.
"""
import json
import subprocess
import sys
from pathlib import Path
from fractions import Fraction as F

EXPECTED_DIGEST="ff2f21b9027c255d6236ba8c70e693c8f8989ed384dc33942194589e833ca1a8"
def run():
    script=Path(__file__).with_name("independent_union.py")
    p=subprocess.run([sys.executable,str(script)],capture_output=True,text=True,check=True)
    result=json.loads(p.stdout)
    assert result["status"]=="PASS",result
    assert result["count"]==11698,result
    assert result["failures"]==[],result
    assert len(result["equalities"])==1,result
    eq=result["equalities"][0]
    assert eq[:2]==[1,14] and F(eq[2],eq[3])==F(13,20),result
    minimum=result["minimum"]
    assert minimum[:2]==[1,14] and F(minimum[2],minimum[3])==F(13,20),result
    assert result["records_sha256"]==EXPECTED_DIGEST,result
    print("PASS: full finite certificate 11698 primitive pairs, zero violations, "
          "unique equality (1,14), minimum 13/20, exact canonical SHA-256 "
          +EXPECTED_DIGEST)
    print("LIMIT: verifies current independent-union output against recorded "
          "digest; does not compare original C++ per-pair records or prove "
          "the analytic grid-discrepancy lemma")

if __name__=="__main__":
    run()
