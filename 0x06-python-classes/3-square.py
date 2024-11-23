#!/usr/bin/python3
"""
Area of square
"""


class Square:
    """
    Calculate area of a square.
    Private instance attribute: XXXX
    Instantiation with optional size: def __init__(self, size=0):
    size must be an integer:
        else raise a TypeError exception with the msg size must be an integer
    if size is less than 0:
        raise a ValueError exception with the message size must be >= 0
    Public instance method:
        def area(self): that returns the current square area
    """
    def __init__(self, size=0):
        """
        initializing class square.
        Arg:
            size(int): size of square
                size must always be int and >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        return area of the square of length ``size``
        """
        return self.__size**2
