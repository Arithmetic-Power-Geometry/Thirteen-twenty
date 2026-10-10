import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from experiments.cs006_verify import verify, witnesses


class OutputLowerBoundTests(unittest.TestCase):
    def test_witnesses(self):
        for b in range(8, 70):
            self.assertGreaterEqual(verify(b), b//4-1)

    def test_explicit_examples(self):
        self.assertEqual(len(witnesses(8)), 2)
        self.assertGreaterEqual(len(witnesses(64)), 15)


if __name__=="__main__":
    unittest.main()
