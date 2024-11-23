#!/usr/bin/python3
"""
Square with size
"""


class Square:
    """
    A class that defines a square with private size
    """

    def __init__(self, size):
        """
        Initializing class Square
        Arg:
            size (int): size of square
        """
        self.__size = size

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
