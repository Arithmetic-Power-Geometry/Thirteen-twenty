import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from exact_admission import safe_windows,measure

class ComponentBoundTests(unittest.TestCase):
    def test_component_bound(self):
        for b in range(1,19):
            for a in range(1,b+1):
                w=safe_windows(a,b)
                self.assertLessEqual(len(w),2*(a+b))
                self.assertGreaterEqual(max((r-l for l,r in w),default=Q(0)),Q(13,40*(a+b)))
    def test_sharp_pair(self):
        self.assertEqual(measure(1,14),Q(13,20))
    def test_no_wraparound(self):
        for a,b in ((1,1),(1,14),(4,9)):
            w=safe_windows(a,b)
            self.assertTrue(all(u>0 and v<1 for u,v in w))
if __name__=="__main__":unittest.main()
