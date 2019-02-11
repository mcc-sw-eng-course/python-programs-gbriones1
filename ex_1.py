#!/usr/bin/python

import sys

if len(sys.argv) <= 1:
    print("Please provide at least 2 numbers")
elif len(sys.argv) == 2:
    num_str = sys.argv[1]
    try:
        num = int(num_str)
        if not(num % 2):
            if not(num % 4):
                print("Number is evenly divisible by 4")
            else:
                print("Number is even")
        else:
            print("Number is odd")
    except:
        print("Input is not a valid integer")
else:
    num_str = sys.argv[1]
    check_str = sys.argv[2]
    try:
        num = int(num_str)
        check = int(check_str)
        if not(num % check):
            print("Number {} is evenly divisible by {}".format(num, check))
        else:
            print("Number {} is not evenly divisible by {}".format(num, check))
    except:
        print("Inputs are not valid integers")
