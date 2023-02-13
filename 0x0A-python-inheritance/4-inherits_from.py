#!/usr/bin/python3
"""
Module contain a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False
"""
def inherits_from(obj, a_class):
    """ A function that returns True if obj is an instance of a class that inherited from a_class otherwise false """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
