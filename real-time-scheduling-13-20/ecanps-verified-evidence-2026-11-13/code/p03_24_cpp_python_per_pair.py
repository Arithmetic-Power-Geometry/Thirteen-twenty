"""P03-24 compare every primitive-pair C++ midpoint result with Python union.

Compiles the archived original source snapshot; uses independent_union.measure
for each record, comparing fractions by integer cross multiplication.
"""
import csv
from fractions import Fraction
from math import gcd
from pathlib import Path
import subprocess
import tempfile
from independent_union import measure

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/"reference"/"original_checker_snapshot.cpp"
def run():
    with tempfile.TemporaryDirectory() as d:
        binary=Path(d)/"original_checker"
        output=Path(d)/"certificate.csv"
        subprocess.run(["g++","-std=c++17","-O2","-Wall","-Wextra",
                        str(SOURCE),"-o",str(binary)],check=True)
        proc=subprocess.run([str(binary),str(output)],capture_output=True,text=True,check=True)
        assert "tested=11698 violations=0 equality=1" in proc.stderr,proc.stderr
        count=0
        equalities=[]
        with output.open(newline="") as f:
            reader=csv.DictReader(f)
            assert reader.fieldnames==["a","b","numerator","denominator","equality"]
            for row in reader:
                a,b,n,d,e=(int(row[k]) for k in reader.fieldnames)
                assert 1<=a<=b<=196 and gcd(a,b)==1
                py_n,py_d=measure(a,b)
                assert n*py_d==py_n*d,(a,b,n,d,py_n,py_d)
                assert e==int(20*n==13*d),(a,b)
                if e:equalities.append((a,b))
                count+=1
        assert count==11698,count
        assert equalities==[(1,14)],equalities
        print("PASS: 11698 per-pair exact C++ midpoint vs Python forbidden-union "
              "cross-product comparisons; zero mismatches; equality (1,14)")
        print("SOURCE: archived legacy C++ snapshot; compare its Git blob SHA "
              "with recorded 0dfb2edb4421003ad96f0444ac3b36d770f45897")
if __name__=="__main__":
    run()
