#!/usr/bin/python3
"""function"""


def append_write(filename="", text=""):
    """this function"""
    with open(filename, 'a', encoding="UTF-8") as p:
        p.write(text)
        return len(text)
