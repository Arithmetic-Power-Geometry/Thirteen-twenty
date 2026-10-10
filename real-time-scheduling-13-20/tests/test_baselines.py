import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from exact_admission import safe_windows, admit, verify_yes
from baseline_admission import linear_query, binary_query, AdmissionIndex


class BaselineTests(unittest.TestCase):
    def test_all_small_instances(self):
        for b in range(1, 13):
            for a in range(1, b+1):
                windows = safe_windows(a, b)
                index = AdmissionIndex(a, b)
                for i in range(11):
                    r = Q(i, 12)
                    d = Q(1) if i % 2 == 0 else min(Q(1), r + Q(1, 4))
                    for p in (Q(1, 500), Q(1, 40), Q(1, 5)):
                        reference, cert = admit(a, b, r, d, p)
                        expected = cert if reference == "YES" else None
                        self.assertEqual(linear_query(windows, r, d, p), expected)
                        self.assertEqual(binary_query(windows, r, d, p), expected)
                        self.assertEqual(index.query(r, d, p), expected)
                        if expected is not None:
                            self.assertTrue(verify_yes(a, b, r, d, p, expected))

    def test_boundary_cases(self):
        for a, b in [(1, 1), (1, 14), (5, 7)]:
            windows = safe_windows(a, b)
            index = AdmissionIndex(a, b)
            for left, right in windows:
                p = right-left
                self.assertEqual(index.query(left, right, p), left)
                self.assertEqual(index.query(left, right, p + Q(1, 10000)), None)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            AdmissionIndex(1, 14).query(0, 1, 0)


if __name__ == "__main__":
    unittest.main()
