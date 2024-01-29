#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = my_list[:]
    for x in range(len(my_list)):
        new2 = sum(set(new))
    return new2
