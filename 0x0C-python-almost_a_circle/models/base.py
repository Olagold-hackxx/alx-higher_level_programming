#!/usr/bin/python3
"""
 Module that manages id attribute in all your future classes and to avoid
duplicating the same code (by extension, same bugs)
"""


class Base:
    """
    Class Base will be the “base” of all other classes
    in this project. The goal of it is to manage id attribute in
    all your future classes and to avoid duplicating the same code (by extension, same bugs)
    Private class attribute XXX
    class constructor: def __init__(self, id=None)::
    if id is not None, assign the public instance attribute id with this argument value
    you can assume id is an integer and you don’t need to test the type of it
    otherwise, increment __nb_objects and assign the new value to the public instance attribute id
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializing this class
        Args:
            id(int): Can be None, will be assigned else specified
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
