#!/usr/bin/python3
def best_score(a_dictionary):
    for x in a_dictionary:
        if a_dictionary[x] >= 12:
            return a_dictionary
        else:
            return None
