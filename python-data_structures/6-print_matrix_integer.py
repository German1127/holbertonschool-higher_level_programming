#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        i = 0
        for j in x:
            len_matrix = len(x)
            i += 1
            print("{:d}".format(j), end="")
            if i != len_matrix:
                print(" ", end="")
        print("")
