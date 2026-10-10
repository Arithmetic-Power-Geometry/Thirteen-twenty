import sys
import unittest
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from exact_admission import safe_windows
from multi_job_equal import equal_job_capacity,decide_equal_jobs,verify_equal_jobs


class EqualJobTests(unittest.TestCase):
    def test_exact_capacity_and_witness(self):
        for b in range(1,18):
            for a in range(1,b+1):
                for p in (F(1,100),F(1,20),F(1,5)):
                    n, sched, alloc=equal_job_capacity(a,b,0,1,p)
                    expected=sum(int((v-u)//p) for u,v in safe_windows(a,b))
                    self.assertEqual(n,expected)
                    self.assertEqual(len(sched),n)
                    for start,end in sched:
                        self.assertEqual(end-start,p)
                        self.assertTrue(any(u<=start and end<=v for u,v in safe_windows(a,b)))
                    self.assertTrue(all(sched[i][1]<=sched[i+1][0] for i in range(len(sched)-1)))
                    for jobs in (0,n,n+1):
                        answer=decide_equal_jobs(a,b,0,1,p,jobs)
                        self.assertEqual(answer["decision"],"YES" if jobs<=n else "NO")
                        self.assertTrue(verify_equal_jobs(a,b,0,1,p,jobs,answer))

    def test_clipped_release_deadline(self):
        n,sched,_=equal_job_capacity(1,14,F(1,4),F(3,4),F(1,100))
        self.assertTrue(all(F(1,4)<=s and e<=F(3,4) for s,e in sched))
        self.assertEqual(len(sched),n)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            equal_job_capacity(1,14,0,1,0)
        with self.assertRaises(ValueError):
            decide_equal_jobs(1,14,0,1,F(1,100),-1)


if __name__=="__main__":
    unittest.main()
