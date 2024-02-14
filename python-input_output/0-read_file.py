#!/usr/bin/python3
"""this function reads files"""


def read_file(filename=""):
    """the function"""
    with open(filename, 'r', encoding="UTF-8") as p:
        print(f"{p.read()}", end="")
