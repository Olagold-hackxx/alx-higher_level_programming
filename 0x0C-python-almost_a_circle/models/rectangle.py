#!/usr/bin/python3
"""Contain class `Rectangle` that inherits from `Base` """


from models.base import Base


class Rectangle(Base):
    """
    Class `Rectangle` that inherits from `Base`:

    In the file models/rectangle.py
    Class Rectangle inherits from Base
    Private instance attributes, each with its own public getter and setter:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
    Call the super class with id - this super call with use the logic
    of the __init__ of the Base class
    Assign each argument width, height, x and y to the right attribute
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiate class object.
        Arguments
            width: width of rectangle
            height: height of rectangle
            x: x axis offset
            y: y axis offset
            id: object id
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value for width"""
        self.__width = value

    @property
    def height(self):
        """Return value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value for height"""
        self.__height = value

    @property
    def x(self):
        """Return value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the value for x"""
        self.__x = value

    @property
    def y(self):
        """Return value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the value for y"""
        self.__y = value
