import sys
import unittest
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from exact_admission import safe_windows,measure,admit
from robustness import shifted_safe_windows,shifted_measure,robust_admit,verify_robust_yes


class RobustnessTests(unittest.TestCase):
    def test_zero_phase_equivalence(self):
        for b in range(1,16):
            for a in range(1,b+1):
                self.assertEqual(shifted_safe_windows(a,b),safe_windows(a,b))
                self.assertEqual(shifted_measure(a,b),measure(a,b))

    def test_zero_jitter_equivalence(self):
        for a,b in ((1,1),(1,14),(3,5)):
            for p in (F(1,100),F(1,10)):
                status,s=robust_admit(a,b,(0,0,0),0,1,p,0)
                expected,_=admit(a,b,0,1,p)
                self.assertEqual(status,expected)
                if status=="YES":
                    self.assertTrue(verify_robust_yes(a,b,(0,0,0),0,1,p,0,s))

    def test_jitter_monotonicity(self):
        for a,b in ((1,14),(3,5)):
            for phases in ((0,0,0),(F(1,7),F(1,11),F(1,13))):
                results=[robust_admit(a,b,phases,0,1,F(1,100),e)[0]
                         for e in (F(0),F(1,1000),F(1,100),F(1,10))]
                self.assertEqual(results,sorted(results,reverse=True))

    def test_nonzero_phase(self):
        phases=(F(1,7),F(1,11),F(1,13))
        status,s=robust_admit(1,14,phases,0,1,F(1,100),F(1,1000))
        if status=="YES":
            self.assertTrue(verify_robust_yes(1,14,phases,0,1,F(1,100),F(1,1000),s))

    def test_invalid(self):
        with self.assertRaises(ValueError):
            robust_admit(1,14,(0,0,0),0,1,F(1,100),-1)


if __name__=="__main__":
    unittest.main()
