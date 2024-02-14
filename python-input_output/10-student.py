#!/usr/bin/python3

"""class Student."""


class Student:
    """Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if not isinstance(attrs, list=[]):
            return self.__dict__
        else:
            dic = {}
            for x in attrs:
                if x in self.__dict__:
                    dic[x] = self.__dict__[x]
        return dic
