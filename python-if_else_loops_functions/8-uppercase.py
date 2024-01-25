#!/usr/bin/python3
def uppercase(str):
    for x in range(len(str)):
        if ord(str[x]) >= 97 and ord(str[x]) <= 122:
            num = 32
        else:
            num = 0
        print("{:c}".format(ord(str[x]) - num), end='')
    print()
