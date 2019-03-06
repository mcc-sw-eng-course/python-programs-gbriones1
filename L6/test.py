import unittest

from mySorter import mySorter

class TestMySorter(unittest.TestCase):

    def test_set_input_data(self):
        sorter = mySorter()
        self.assertTrue(sorter.set_input_data("valid.csv"))
        self.assertFalse(sorter.set_input_data("unexistent.csv"))
        self.assertFalse(sorter.set_input_data("incorrect.csv"))
    
    def test_set_output_data(self):
        sorter = mySorter([2,3,1,2,4,9])
        sorter.set_output_data("output.csv")
        new_sorter = mySorter()
        new_sorter.set_input_data("output.csv")
        self.assertTrue(sorter.alist == new_sorter.alist)

    def test_execute_merge_sort(self):
        alist = [5.28,66.24,85.4,4,5.5,8.95,15.4]
        sorter = mySorter(alist)
        sorter.execute_merge_sort()
        alist = sorted(alist)
        self.assertTrue(sorter.alist == alist)
        print("Merge sort data", sorter.get_performance_data())

    def test_execute_quick_sort(self):
        alist = [5.28,66.24,85.4,4,5.5,8.95,15.4]
        sorter = mySorter(alist)
        sorter.execute_quick_sort()
        alist = sorted(alist)
        self.assertTrue(sorter.alist == alist)
        print("Quick sort data", sorter.get_performance_data())

    def test_execute_heap_sort(self):
        alist = [5.28,66.24,85.4,4,5.5,8.95,15.4]
        sorter = mySorter(alist)
        sorter.execute_heap_sort()
        alist = sorted(alist)
        self.assertTrue(sorter.alist == alist)
        print("Heap sort data", sorter.get_performance_data())

    def test_execute_merge_sort_large(self):
        sorter = mySorter()
        sorter.set_input_data("large.csv")
        alist = sorted(sorter.alist)
        sorter.execute_merge_sort()
        self.assertTrue(sorter.alist == alist)
        print("Merge sort large data", sorter.get_performance_data())

    def test_execute_quick_sort_large(self):
        sorter = mySorter()
        sorter.set_input_data("large.csv")
        alist = sorted(sorter.alist)
        sorter.execute_quick_sort()
        self.assertTrue(sorter.alist == alist)
        print("Quick sort large data", sorter.get_performance_data())

    def test_execute_heap_sort_large(self):
        sorter = mySorter()
        sorter.set_input_data("large.csv")
        alist = sorted(sorter.alist)
        sorter.execute_heap_sort()
        self.assertTrue(sorter.alist == alist)
        print("Heap sort large data", sorter.get_performance_data())

if __name__ == '__main__':
    unittest.main()