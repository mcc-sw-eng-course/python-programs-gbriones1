import csv

class mySorter():
    """ CLASS THAT HANDLES CSV FILES AND IMPLEMENTS METHODS FOR SORTING THEIR CONTENT"""
    
    def __init__(self, alist = None):
        self.alist = alist
        
    def set_input_data(self, file_path_name: str):
        """This methods sets the information about the file that will be used to read the data"""
        try:
            self.alist = []
            with open(file_path_name) as csvfile:
                readCSV = csv.reader(csvfile, delimiter = ',')
                for row in readCSV:
                    for element in row:
                        self.alist.append(float(element))
        except FileNotFoundError:
            print("File doesn't exist")
            return False
        except ValueError:
            print("A value found is not a number")
            return False
        return True
    
    def set_output_data(self, file_path_name: str):
        """This methods sets the information about the file that will be used to store the sorted data"""
        with open(file_path_name, 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',')
            filewriter.writerow(self.alist)
    
    def execute_merge_sort(self, arr):
        """This methods sorts the data contained in the file specified"""
        pass

    
    def execute_heap_sort(self):
        """This methods sorts the data contained in the file specified"""
        pass
    
    def execute_quick_sort(self):
        """This methods sorts the data contained in the file specified"""
        return self._quick_sort_recursion(self.alist, 0, len(self.alist)-1)
    
    def get_performance_data(self):
        """This method returns the performance data associated to the last sorting execution
            [Number of Records Sorted, TimeConsumed, StartTime, EndTime]"""
        pass
    
    def _partition(self, array, begin, end):
        pivot_idx = begin
        for i in range(begin+1, end+1):
            if array[i] <= array[begin]:
                pivot_idx += 1
                array[i], array[pivot_idx] = array[pivot_idx], array[i]
        array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
        return pivot_idx

    def _quick_sort_recursion(self, array, begin, end):
        if begin >= end:
            return
        pivot_idx = self._partition(array, begin, end)
        self._quick_sort_recursion(array, begin, pivot_idx-1)
        self._quick_sort_recursion(array, pivot_idx+1, end)

    def execute_merge_sort(self):
        self._merge_sort_recursion(self.alist)

    def _merge_sort_recursion(self, alist):
        #print("Splitting ",alist)
        if len(alist)>1:
            mid = len(alist)//2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            self._merge_sort_recursion(lefthalf)
            self._merge_sort_recursion(righthalf)

            i=0
            j=0
            k=0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist[k]=lefthalf[i]
                    i=i+1
                else:
                    alist[k]=righthalf[j]
                    j=j+1
                k=k+1

            while i < len(lefthalf):
                alist[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j < len(righthalf):
                alist[k]=righthalf[j]
                j=j+1
                k=k+1
        #print("Merging ",alist)
