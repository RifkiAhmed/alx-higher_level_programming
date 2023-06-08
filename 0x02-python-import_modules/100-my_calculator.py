#!/usr/bin/python3
if __name__ != "__main__":
    exit(0)
from sys import argv
from calculator_1 import add, sub, mul, div
argc = len(argv)
if argc != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
a = int(argv[1])
b = int(argv[3])
if argv[2] == "+":
    print("{0:d} + {1:d} = {2:d}".format(a, b, add(a, b)))
elif argv[2] == "-":
    print("{0:d} - {1:d} = {2:d}".format(a, b, sub(a, b)))
elif argv[2] == "*":
    print("{0:d} * {1:d} = {2:d}".format(a, b, mul(a, b)))
elif argv[2] == "/":
    print("{0:d} / {1:d} = {2:d}".format(a, b, div(a, b)))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
