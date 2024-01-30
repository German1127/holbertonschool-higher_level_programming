#!/usr/bin/python3
def common_elements(set_1, set_2):
    zipped = zip(set_1, set_2)
    for x in zipped:
        print(x)
