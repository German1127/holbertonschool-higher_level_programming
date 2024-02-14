#!/usr/bin/python3
"""function"""

import json


def save_to_json_file(my_obj, filename):
    """json"""
    with open(filename, "w") as p:
        json.dump(my_obj, p)
