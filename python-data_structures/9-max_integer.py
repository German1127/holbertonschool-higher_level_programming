#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    list2 = my_list.copy()
    list2.sort()
    return list2[-1]
