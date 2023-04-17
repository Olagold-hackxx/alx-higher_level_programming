#!/usr/bin/python3
"""
 Module that manages id attribute in all your future classes and to avoid
duplicating the same code (by extension, same bugs)
"""
import json


class Base:
    """
    Class Base will be the “base” of all other classes
    in this project. The goal of it is to manage id attribute in
    all your future classes and to avoid duplicating the
    same code (by extension, same bugs)
    Private class attribute XXX
    class constructor: def __init__(self, id=None)::
    if id is not None, assign the public instance attribute
    id with this argument value
    you can assume id is an integer and
    you don’t need to test the type of it
    otherwise, increment __nb_objects and assign
    the new value to the public instance attribute id
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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        list_dictionary = []
        with open(cls.__name__ + '.json', "w") as f:
            if list_objs is None:
                return f.write('[]')
            else:
                for i in list_objs:
                    list_dictionary.append(i.to_dictionary())
                return f.write(cls.to_json_string(list_dictionary))
            