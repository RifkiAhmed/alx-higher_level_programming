#!/usr/bin/python3
from sys import argv
if __name__ != "__main__":
    exit(0)
argc = len(argv)
print("{0:d}".format(argc - 1), end="")
print(" argument" if argc <3 else " arguments", end="")
print("." if argc <2 else ":")
for i in range(1, argc):
    print("{0}: {1}".format(i, argv[i]))
