#!/usr/bin/python3
"""Coordinates of a square"""

import dis
import math


class MagicClass:
    """Coordinates of a square"""
    def __init__(self, radius=0):
        """Coordinates of a square"""
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
