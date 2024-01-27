#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for x in my_string:
        if x.lower() != 'c':
            new_string += x
            print(x)
