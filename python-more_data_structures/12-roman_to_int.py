#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
    chek = 0
    sum = 0
    for x in reversed(roman_string):
        i = roman.get(x)
        if i < chek:
            sum -= i
        else:
            sum += i
        chek = i
    return sum
