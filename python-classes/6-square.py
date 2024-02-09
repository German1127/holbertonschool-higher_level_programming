#!/usr/bin/python3
"""class"""


from typing import Self


class Square:
    """class square"""

    def __init__(self, size=0, position=(0, 0):
        self.__size = size
        Self.position = position
        
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position
        
    @size.setter
    def size(self, new_size):
        if type(new_size) is not int:
            raise TypeError("size must be an integer")
        if new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size

    @position.setter
    def position(self, value):
        message = 'position must be a tuple of 2 positive integers'
        if type(value) != tuple or len(value) != 2:
            raise TypeError(message)

    for items in value:
            if type(items) != int or items < 0:
                raise TypeError(message)
                
    self.__position = value

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
