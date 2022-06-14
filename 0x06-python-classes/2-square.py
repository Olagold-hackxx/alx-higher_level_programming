#!/usr/bin/python3
"""
Size Validation
"""
class Square:
    """
    Validates size of square
    Private instance attribute: XXXX
    Instantiation with optional size: def __init__(self, size=0):
    size must be an int:
        else raise a TypeError exception with the msg "size must be an integer"
    if size is < 0:
        raise a ValueError exception with the message size must be >= 0
    """
    def __init__(self, size=0):
        """
        Initialize class Square
        Args:
            size (int): size of square
                size must always be an int and >= 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
