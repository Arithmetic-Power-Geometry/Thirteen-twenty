import sys
import unittest
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from multi_job_equal import decide_equal_jobs
from certificate_verifier import (verify_yes_certificate,
                                  verify_no_capacity_certificate,
                                  _independent_safe_components)
from exact_admission import safe_windows


class IndependentCertificateTests(unittest.TestCase):
    def test_independent_components(self):
        for b in range(1,17):
            for a in range(1,b+1):
                self.assertEqual(_independent_safe_components(a,b),safe_windows(a,b))

    def test_valid_certificates(self):
        for a,b in ((1,1),(1,14),(3,7),(5,11)):
            for p in (F(1,200),F(1,40),F(1,5)):
                result=decide_equal_jobs(a,b,0,1,p,3)
                if result["decision"]=="YES":
                    self.assertTrue(verify_yes_certificate(a,b,0,1,p,3,result["schedule"]))
                else:
                    self.assertTrue(verify_no_capacity_certificate(a,b,0,1,p,3,result["capacity"]))

    def test_corrupt_yes_certificates(self):
        a,b,p=1,14,F(1,200)
        result=decide_equal_jobs(a,b,0,1,p,2)
        self.assertEqual(result["decision"],"YES")
        valid=result["schedule"]
        self.assertTrue(verify_yes_certificate(a,b,0,1,p,2,valid))
        self.assertFalse(verify_yes_certificate(a,b,0,1,p,2,valid[:1]))
        self.assertFalse(verify_yes_certificate(a,b,0,1,p,2,[valid[0],valid[0]]))
        self.assertFalse(verify_yes_certificate(a,b,0,1,p,2,[(F(0),p),valid[1]]))
        self.assertFalse(verify_yes_certificate(a,b,0,1,p,2,[(valid[0][0],valid[0][1]+p),valid[1]]))

    def test_corrupt_no_certificates(self):
        a,b,p=1,14,F(1,5)
        result=decide_equal_jobs(a,b,0,1,p,100)
        self.assertEqual(result["decision"],"NO")
        cap=result["capacity"]
        self.assertTrue(verify_no_capacity_certificate(a,b,0,1,p,100,cap))
        self.assertFalse(verify_no_capacity_certificate(a,b,0,1,p,100,cap+1))
        self.assertFalse(verify_no_capacity_certificate(a,b,0,1,p,cap,cap))


if __name__=="__main__":
    unittest.main()
