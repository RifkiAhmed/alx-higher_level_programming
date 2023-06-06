#!/usr/bin/python3
for i in range(0, 8):
    for j in range(0, 10):
        if i == j or i > j:
            continue
        print("{0}{1}".format(i, j), end=", ")
print("{0}{1}".format(i + 1, j))
