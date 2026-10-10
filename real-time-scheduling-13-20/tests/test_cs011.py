import sys
import itertools
import unittest
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from exact_admission import safe_windows


def partition_feasible(weights):
    total=sum(weights)
    if total%2:
        return False
    return any(sum(weights[i] for i in range(len(weights)) if mask>>i&1)==total//2
               for mask in range(1<<len(weights)))


def two_window_schedule_feasible(weights):
    total=sum(weights)
    if total%2:
        return False
    b=total//2
    if b==0:
        return False
    cap=F(13,32)
    durations=[cap*F(w,b) for w in weights]
    return any(sum(durations[i] for i in range(len(weights)) if mask>>i&1)<=cap
               and sum(durations[i] for i in range(len(weights)) if not(mask>>i&1))<=cap
               for mask in range(1<<len(weights)))


class FixedFrequencyHardnessTests(unittest.TestCase):
    def test_windows(self):
        self.assertEqual(safe_windows(1,1),[(F(1,16),F(15,32)),(F(17,32),F(15,16))])

    def test_reduction_exhaustive_small(self):
        for n in range(1,6):
            for weights in itertools.product(range(1,5),repeat=n):
                self.assertEqual(partition_feasible(weights),two_window_schedule_feasible(weights),weights)


if __name__=="__main__":
    unittest.main()
