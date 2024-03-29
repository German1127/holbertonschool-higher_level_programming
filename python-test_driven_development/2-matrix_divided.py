#!/usr/bin/python3
"""2-matrix
"""


def matrix_divided(matrix, div):
    row_check = 0
    if not any(matrix):
        raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
    if matrix[0] is not None:
        row_check = len(matrix[0])
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
        for num in row:
            if type(num) is not int and type(num) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
        if len(row) != row_check:
            raise TypeError("Each row of the matrix must have the same size")

    return [[round(num / div, 2) for num in row] for row in matrix]
