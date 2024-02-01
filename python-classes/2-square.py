#!/usr/bin/python3
"""class"""


class Square:
    """class square"""

    def __init__(self, size=0):
        """__init__ is constructor"""
        self.__size = size

        """chek is size int"""
    def size(self, new_size):
        if type(new_size) is not int:
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
