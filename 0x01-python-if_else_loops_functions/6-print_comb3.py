#!/usr/bin/python3
for i in range(0, 10):
    for j in range (0, 10):
        if i >= j:
            continue
        elif i == 8 and j == 9:
            print("{0}{1}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
