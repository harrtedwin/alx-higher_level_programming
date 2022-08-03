#!/usr/bin/python3
"""the Square class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The square class"""
    def __init__(self, size):
        """Method"""
        self.integer_validator(size, size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
