#!/usr/bin/python

import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

MAP = {
    1: ("I", "V"),
    2: ("X", "L"),
    3: ("C", "D"),
    4: ("M", "\033[53mV\033[0m"),
    5: ("\033[53mX\033[0m", "\033[53m\u0305L\033[0m"),
    6: ("\033[53mC\033[0m", "\033[53mD\033[0m"),
}

# if len(sys.argv) != 2:
#     print("Please provide 1 number")
#     sys.exit(1)
# if not sys.argv[1].isdigit():
#     print("Please provide a valid number")
#     sys.exit(1)
# number = int(sys.argv[1])
# max = (10**len(MAP)-10**(len(MAP)-1))-1
# if number > max:
#     print("Number is too huge, not enough roman characters to represent. Max is {}".format(max))
#     sys.exit(1)
# if number < 1:
#     print("Number is too small")
#     sys.exit(1)

def _to_roman_sub(position, digit):
    if digit == 0:
        return ""
    elif digit <= 3:
        return MAP[position][0]*digit
    elif digit == 4:
        return MAP[position][0]+MAP[position][1]
    elif digit == 5:
        return MAP[position][1]
    elif digit <= 8:
        return MAP[position][1]+(MAP[position][0]*(digit-5))
    elif digit == 9:
        return MAP[position][0]+MAP[position+1][0]

def to_roman(n):
    ns = str(n)
    roman = ""
    for index in range(len(ns)):
        digit = int(ns[index])
        roman += _to_roman_sub(len(ns)-index, digit)
    return roman
