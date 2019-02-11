#!/usr/bin/python

import json

class MyPowerList(object):

    def __init__(self):
        self.data = []

    def add_item(self, item):
        self.data.append(item)

    def remove_nth(self, index):
        self.data.pop(index)

    def sorted(self):
        for sub_index in range(len(self.data)-1,0,-1):
            for i in range(sub_index):
                if self.data[i]>self.data[i+1]:
                    temp = self.data[i]
                    self.data[i] = self.data[i+1]
                    self.data[i+1] = temp
        return self.data

    def merge(self, to_merge, method="Rmerge"):
        if method == "Rmerge":
            self.data.extend(to_merge)
        elif method == "Lmerge":
            to_merge.extend(self.data)
            self.data = to_merge

    def saveToTextFile(self, filename):
        with open(filename, "w") as target:
            target.write(json.dumps(self.data))

    def readFromTextFile(self, filename):
        with open(filename, "r") as target:
            self.data = json.loads(target.read())
