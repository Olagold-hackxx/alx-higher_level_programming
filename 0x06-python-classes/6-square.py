#!/usr/bin/python3
""" Coordinates of a square """

class Square:
    """
    Print coordinates of a square and the square in space and #
    Private instance attribute: XXXX
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
    size must be an integer:
        else raise a TypeError exception with the message0
            "size must be an integer"
    if size is less than 0:
        raise a ValueError exception with the message
            "size must be >= 0"
    Private instance attribute: XXXX
    property def position(self): to retrieve it
    property setter def position(self, value): to set it:
    position must be a tuple of 2 positive integers:
        else raise a TypeError exception with the message:
            position must be a tuple of 2 positive integers
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method:
        def area(self): that returns the current square area
        def my_print(self):
            prints in stdout the square with the character #:
            if size is equal to 0, print an empty line
            position should be use by using space,
                position[1] should print new line
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize class square
        Arg:
            size (int): size of square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        return position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        set position of square
        Arg:
            position (tuple): position of square
        if position is not a tuple of 2 positive int raise TypeError
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        return area of ``size``
        """
        return self.__size**2

    def my_print(self):
        """
        print a square in # with size ``size``
        """
        if self.__size == 0:
            print()
        else:
            [print() for i in range(self.__position[1])]
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
