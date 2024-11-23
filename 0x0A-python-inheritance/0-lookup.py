#!/usr/bin/python3
"""
Returns lists of available attributes and methods
"""


def lookup(obj):
    """ Return all available attributes and methods in a class"""
    obj_list = dir(obj)
    return obj_list
