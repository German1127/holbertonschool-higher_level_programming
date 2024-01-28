#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = my_list.copy()
    for x in new:
        if x % 2 == 0:
            return True
        else:
            return False
