#!/usr/bin/python

import sys
import math

if len(sys.argv) != 2:
    print("Please provide a file with dataset")
    sys.exit(0)

dataset = []

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        for item in line.split():
            if item.isdigit():
                dataset.append(int(item))

mean = sum(dataset) / len(dataset)
acc = 0.0

for x in dataset:
    acc += (x - mean) ** 2

stddev = math.sqrt(acc / mean)
print("Mean is {}".format(mean))
print("Standard deviation is {}".format(stddev))
