#!/usr/bin/python3
"""Square Class

A Square Class

"""


class Square:
    """The __init__ method initializes the size value of the square."""
    def __init__(self, size=0):
        """The __init__ method initializes the size value of the square."""
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """The __init__ method initializes the size value of the square."""

        return self.__size ** 2
