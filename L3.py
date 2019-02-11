#!/usr/bin/python3

import filecmp
import math
import os
import unittest
import shutil
import time

class TestMathCeil(unittest.TestCase):

    def test_math_ceil(self):
        # Test round up in real numbers
        self.assertEqual(math.ceil(3.3), 4)
        self.assertEqual(math.ceil(3.6), 4)
        self.assertEqual(math.ceil(-2.1), -2)
        self.assertEqual(math.ceil(-2.6), -2)
        self.assertEqual(math.ceil(7), 7)
        self.assertEqual(math.ceil(0), 0)
        self.assertEqual(math.ceil(-0), -0)

    def test_math_ceil_types(self):
        # Test type errors are raised when inputs are not valid
        self.assertRaises(TypeError, math.ceil, -5j)
        self.assertRaises(TypeError, math.ceil, "aaa")
        self.assertRaises(TypeError, math.ceil, [1,2,3])

    def test_math_ceil_range(self):
        self.assertRaises(OverflowError, math.ceil, 2e+308)
        self.assertRaises(OverflowError, math.ceil, -2e+308)
        self.assertEqual(math.ceil(1e-323), 1)
        self.assertEqual(math.ceil(1e-324), 0)


class TestMathFactorial(unittest.TestCase):

    def test_math_factorial(self):
        # Test proper calculation with integer inputs
        self.assertEqual(math.factorial(2), 2)
        self.assertEqual(math.factorial(3), 6)
        self.assertEqual(math.factorial(4), 24)

    def test_math_factorial_values(self):
        # Verifies that proper errors are raised when not accepted values are input
        self.assertRaises(ValueError, math.factorial, -1)
        self.assertRaises(ValueError, math.factorial, 3.3)
        self.assertRaises(ValueError, math.factorial, 7.7)

    def test_math_factorial_types(self):
        # Verifies if proper errors are raised when invalid type inputs
        self.assertRaises(TypeError, math.factorial, "aa")
        self.assertRaises(TypeError, math.factorial, [1,2,3])
        self.assertRaises(TypeError, math.factorial, {5:2, 'a':9})


class TestMathPow(unittest.TestCase):

    def test_math_pow(self):
        # Test proper calculation with real numbers
        self.assertEqual(math.pow(2,3), 8)
        self.assertEqual(math.pow(-2,3), -8)
        self.assertAlmostEqual(math.pow(2.2, 2), 4.84)
        self.assertAlmostEqual(math.pow(3.4, 2.5), 21.31558678)

    def test_math_pow_values(self):
        # Test proper error is raised when base is negative and exp is not an integer.
        self.assertRaises(ValueError, math.pow, -2, 3.3)

    def test_math_pow_types(self):
        # Checks proper errors are raised when unexpected types are entered as input
        self.assertRaises(TypeError, math.pow, "a", 7)
        self.assertRaises(TypeError, math.pow, 7, "a")
        self.assertRaises(TypeError, math.pow, "a", "a")
        self.assertRaises(TypeError, math.pow, [], 9)
        self.assertRaises(TypeError, math.pow, {}, 7)

    def test_math_pow_cross(self):
        self.assertEqual(math.pow(3.4, 2.5), 3.4**2.5)
        self.assertEqual(math.pow(5, 0), 5**0)
        self.assertEqual(math.pow(1.003654, 4568.4), 1.003654**4568.4)

    def test_math_pow_range(self):
        self.assertTrue(math.isinf(math.pow(2e+308, 2e+308)))


class TestFilecmp(unittest.TestCase):
    FILE1 = 'prueba1.rtf'
    FILE2 = 'prueba2.rtf'

    def setUp(self):
        with open(TestFilecmp.FILE1, 'w') as f:
            f.write("Archivo de prueba")
        shutil.copyfile(TestFilecmp.FILE1, TestFilecmp.FILE2)

    def tearDown(self):
        os.remove(TestFilecmp.FILE1)
        os.remove(TestFilecmp.FILE2)

    def test_filecmp(self):
        # Test proper evaluation of the method
        self.assertTrue(filecmp.cmp(TestFilecmp.FILE1, TestFilecmp.FILE2))
        with open("prueba1.rtf", "a") as f:
            f.write("Now the file has one more line!")
        self.assertFalse(filecmp.cmp(TestFilecmp.FILE1, TestFilecmp.FILE2))

    def test_filecmp_unexistent(self):
        self.assertRaises(OSError, filecmp.cmp, "Unexistent", TestFilecmp.FILE2)

    def test_filecmp_types(self):
        self.assertRaises(TypeError, filecmp.cmp, None, None)
        self.assertRaises(TypeError, filecmp.cmp, [], [])
        self.assertRaises(TypeError, filecmp.cmp, {}, {})

class TestTimeClock(unittest.TestCase):

    def test_time_clock(self):
        x = time.clock()
        self.assertGreater(time.clock(), x)

    def test_time_clock_types(self):
        self.assertRaises(TypeError, time.clock, None)

if __name__ == '__main__':
    unittest.main()
