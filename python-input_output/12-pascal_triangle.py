#!/usr/bin/python3


"""Triangle"""


def pascal_triangle(n):
    if n <= 0:
        return []

    x = [[1]]
    while len(x) is not n:
        tmp = [1]
        for i in range(len(x[-1]) - 1):
            tmp.append(x[-1][i] + x[-1][i + 1])
        tmp.append(1)
        x.append(tmp)
    return x
