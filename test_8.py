import unittest

import ex_8

class TestMean(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(3, ex_8.get_mean([1,2,3,4,5]))

class TestStdDev(unittest.TestCase):

    def test_stddev(self):
        self.assertAlmostEqual(1.581138830084, ex_8.get_stddev([1,2,3,4,5]))
        self.assertAlmostEqual(13.284434142115, ex_8.get_stddev([10,2,38,23,38,23,21]))

class TestMedian(unittest.TestCase):

    def test_median(self):
        self.assertEqual(23, ex_8.get_median([10,2,38,23,38,23,21]))

class TestNQuartile(unittest.TestCase):

    def test_n_quartile(self):
        self.assertAlmostEqual(10, ex_8.get_n_quartile(1, [2,10,11,11,12,21]))
        self.assertAlmostEqual(11, ex_8.get_n_quartile(2, [2,10,11,11,12,21]))
        self.assertAlmostEqual(12, ex_8.get_n_quartile(3, [2,10,11,11,12,21]))

    def test_n_quartile_invalid(self):
        self.assertIsNone(ex_8.get_n_quartile(4, [2,10,11,11,12,21]))

class TestNPercentile(unittest.TestCase):

    def test_n_percentile(self):
        self.assertAlmostEqual(10, ex_8.get_n_percentile(25, [2,10,11,11,12,21]))
        self.assertAlmostEqual(11, ex_8.get_n_percentile(50, [2,10,11,11,12,21]))
        self.assertAlmostEqual(12, ex_8.get_n_percentile(75, [2,10,11,11,12,21]))
        self.assertAlmostEqual(10, ex_8.get_n_percentile(25, [2,10,11,11,12]))
        self.assertAlmostEqual(11, ex_8.get_n_percentile(50, [2,10,11,11,12]))
        self.assertAlmostEqual(11, ex_8.get_n_percentile(75, [2,10,11,11,12]))

if __name__ == '__main__':
    unittest.main()
