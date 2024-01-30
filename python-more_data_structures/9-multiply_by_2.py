#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for x in a_dictionary:
        new[x] = x * 2
        return new
