#!/usr/bin/python3

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
