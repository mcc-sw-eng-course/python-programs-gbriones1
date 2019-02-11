#!/usr/bin/python

import random
import sys

MIN = 0
MAX = 10

num = random.randint(MIN, MAX)
guess = -1
count = 0
while guess != num:
    guess = input("Guess a number between {} and {} (Type 'exit' to exit): ".format(MIN, MAX))
    if guess.isdigit():
        count += 1
        guess = int(guess)
        if guess < num:
            print("Too low")
        elif guess > num:
            print("Too high")
    else:
        if guess == 'exit':
            print("Bye")
            sys.exit(0)
        print("{} is not a valid number".format(guess))

print("You guessed the number in {} tries".format(count))
