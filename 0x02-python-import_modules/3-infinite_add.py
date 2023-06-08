#!/usr/bin/python3
from sys import argv
if __name__ != "__main__":
    exit(0)
argc = len(argv)
if argc == 1:
    print(0)
    exit(0)
sum = 0
for i in range(1, argc):
    sum += int(argv[i])
print("{0:d}".format(sum))
