#!/usr/bin/python

import sys

if len(sys.argv) != 2:
    print("Please provide a number")
    sys.exit(0)

num_str = sys.argv[1]
num = 0
try:
    num = int(num_str)
except:
    print("Input is not a valid integer")
    sys.exit(0)

fib = [1,1]

while len(fib) <= num:
    last = fib[len(fib)-1]
    pre_last = fib[len(fib)-2]
    fib.append(last+pre_last)

print("Last 10 numbers in fibbonacci: {}".format(fib[-11:num]))
