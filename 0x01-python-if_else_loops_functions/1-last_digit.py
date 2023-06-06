#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    modulo = (-number)%10 * -1
else:
    modulo = number % 10
if modulo == 0:
    print(f"Last digit of {number} is {modulo} and is 0")
elif modulo < 0:
    print(f"Last digit of {number} is {modulo} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {modulo} and is greater than 5")
