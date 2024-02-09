#!/usr/bin/python3
"""
This module has a class MyList that inherits from
list.
"""


class MyList(list):
    """
    class that inherits from list
    """
    def print_sorted(self):
        print(sorted(self))
