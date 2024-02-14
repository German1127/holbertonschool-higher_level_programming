#!/usr/bin/python3
"""this function"""


def write_file(filename="", text=""):
    """function"""
    with open(filename, 'w', encoding="UTF-8") as p:
        p.write(text)
        return len(text)
