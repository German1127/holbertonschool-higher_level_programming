#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    ordenado = sorted(my_list, reverse=True)
    for ordenado in my_list:
        print("{}".format(ordenado))
