#!/usr/bin/python3
i = 122
while i >= 97:
    print(chr(i), end="") if i % 2 == 0 else print(chr(65 + i - 97), end="")
    i-= 1
