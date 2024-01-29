#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = my_list[:]
    sum = sum(set(new))
    return sum
