#!/usr/bin/python3
"""function"""

import json


def load_from_json_file(filename):
    """json"""
    with open(filename, "r") as p:
        data = json.load(p)
    return data
