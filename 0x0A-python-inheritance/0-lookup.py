#!/usr/bin/python3
"""
Returns lists of available attributes and methods
"""

def lookup(obj):
    """ Return all available attributes and methos in a class"""
    list = dir(obj)
    return list