import unittest
import json

import ex_14

class TestMyPowerList(unittest.TestCase):

    def setUp(self):
        self.pl = ex_14.MyPowerList()
        self.pl.add_item(5)
        self.pl.add_item(2)
        self.pl.add_item(3)
        self.pl.add_item(1)

    def test_add_item(self):
        self.assertEqual([5,2,3,1], self.pl.data)

    def test_remove_item(self):
        self.pl.remove_nth(1)
        self.assertEqual([5,3,1], self.pl.data)

    def test_sorted(self):
        sorted_list = self.pl.sorted()
        self.assertEqual([1,2,3,5], sorted_list)

    def test_rmerge(self):
        self.pl.merge([6,9,8], "Rmerge")
        self.assertEqual([5,2,3,1,6,9,8], self.pl.data)

    def test_lmerge(self):
        self.pl.merge([6,9,8], "Lmerge")
        self.assertEqual([6,9,8,5,2,3,1], self.pl.data)

    def test_save_to_file(self):
        self.pl.saveToTextFile("list.txt")
        with open("list.txt", "r") as f:
            saved = json.loads(f.read())
        self.assertEqual(saved, self.pl.data)

    def test_read_from_file(self):
        self.pl.add_item(5)
        self.pl.add_item(2)
        self.pl.add_item(3)
        self.pl.saveToTextFile("list.txt")
        self.pl.data = []
        self.pl.readFromTextFile("list.txt")
        self.assertEqual([5,2,3,1,5,2,3], self.pl.data)

if __name__ == '__main__':
    unittest.main()
