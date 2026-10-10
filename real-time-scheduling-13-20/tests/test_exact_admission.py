"""Deterministic reference tests; run: python3 -m unittest discover -s tests -v"""
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from exact_admission import safe_windows, measure, admit, verify_yes, verify_no, phase_safe


class ExactAdmissionTests(unittest.TestCase):
    def test_sharp_pair(self):
        self.assertEqual(measure(1, 14), Q(13, 20))

    def test_gcd_scaling_small(self):
        for a, b in [(1, 1), (1, 2), (1, 14), (3, 5)]:
            self.assertEqual(measure(a, b), measure(2*a, 2*b))

    def test_small_pairs_bound(self):
        for b in range(1, 15):
            for a in range(1, b+1):
                self.assertGreaterEqual(measure(a, b), Q(13, 20))

    def test_midpoints_and_maximality(self):
        for a, b in [(1, 1), (1, 14), (3, 7)]:
            w = safe_windows(a, b)
            self.assertTrue(all(u < v for u, v in w))
            self.assertTrue(all(w[i][1] < w[i+1][0] for i in range(len(w)-1)))
            for u, v in w:
                self.assertTrue(all(phase_safe((u+v)/2, f) for f in (a, b, a+b)))

    def test_yes(self):
        a, b = 1, 14
        u, v = safe_windows(a, b)[0]
        p = (v-u)/2
        status, start = admit(a, b, u, v, p)
        self.assertEqual(status, "YES")
        self.assertTrue(verify_yes(a, b, u, v, p, start))

    def test_no(self):
        status, windows = admit(1, 14, Q(0), Q(1), Q(1))
        self.assertEqual(status, "NO")
        self.assertTrue(verify_no(1, 14, 0, 1, 1, windows))

    def test_zero_and_invalid(self):
        with self.assertRaises(ValueError):
            admit(1, 14, 0, 1, 0)
        with self.assertRaises(ValueError):
            safe_windows(0, 1)


if __name__ == "__main__":
    unittest.main()
