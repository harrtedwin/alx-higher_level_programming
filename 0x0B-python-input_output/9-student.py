#!/usr/bin/python3
"""class"""


class Student:
    """Module"""
    def __init__(self, first_name, last_name, age):
        """Comment"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Comment"""
        return self.__dict__
