#!/usr/bin/python3


def pascal_triangle(n):
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for x in range(n-1):
        triangle.append([a+b for a, b
                         in zip([0] + triangle[-1], triangle[-1] + [0])])
    return triangle
