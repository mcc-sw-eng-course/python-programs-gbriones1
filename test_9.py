import unittest

import ex_9

class TestToRoman(unittest.TestCase):

    def test_to_roman(self):
        self.assertEqual("M\x1b[53mV\x1b[0mCMXCIX", ex_9.to_roman(4999))
        self.assertEqual("MMCDLXXV", ex_9.to_roman(2475))

if __name__ == '__main__':
    unittest.main()
