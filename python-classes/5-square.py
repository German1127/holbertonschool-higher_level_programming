#!/usr/bin/python3
"""class"""


class Square:
    """class square"""

    def __init__(self, size=0):
        """__init__ is constructor"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        if type(new_size) is not int:
            raise TypeError("size must be an integer")
        if new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print()
