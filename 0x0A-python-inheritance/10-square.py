#!/usr/bin/python3
"""Coordinates of a square"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The square class"""
    def __init__(self, size):
        """The method"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
