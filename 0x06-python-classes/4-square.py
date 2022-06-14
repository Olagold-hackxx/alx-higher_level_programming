#!/usr/bin/python3
""" Access and update private attributes """

class Square:
    """
    Access and update private attributes
    Private instance attribute: XXXX
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
    size must be an integer:
        else raise a TypeError exception with the message size must be an integer
    if size is less than 0:
        raise a ValueError exception with the message size must be >= 0
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method: 
        def area(self): that returns the current square area
    """
    def __init__(self, size=0):
        """
        Initialize class square
        Arg:
            size (int): size of square
        """
        self.__size = size
    @property
    def size(self):
        """
        return size
        """
        return self.__size
    @size.setter
    def size(self, value):
        """
        set the value of size
        Arg:
            value (int): value of size
        if size is not integer raise TypeError
        if size is less than 0 raise ValueError
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        """
        return area of ``size``
        """
        return self.__size**2
    
