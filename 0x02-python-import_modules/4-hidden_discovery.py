#!/usr/bin/python3
import hidden_4

if __name__ != "__main__":
    exit(0)
for line in dir(hidden_4):
    if line[:2] != "__":
        print("{0:s}".format(line))
