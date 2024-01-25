#!/usr/bin/python3
for x in range(0, 10):
    for r in range(x + 1, 10):
        if x == 8 and r == 9:
            print("{}{}".format(x, r))
        else:
            print("{}{}".format(x, r), end=", ")