#!/usr/bin/python3
def no_c(my_string):
    new = my_string[:]
    for x in new:
        if x == 'c' or x == 'C':
            continue
    print("{}".format(x), end="")
