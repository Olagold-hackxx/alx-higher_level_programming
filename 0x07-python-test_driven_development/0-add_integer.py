#!/usr/bin/python3
"""
Name:
    0-add_integer

Description:
    This module add 2 integers or floats

Functions:
    add_integer(a, b):
        Return sum of a and b if both are either int or float
"""


def add_integer(a, b=98):
    """
    Add 2 integers or floats

    Args:
        a (int or float): Value a to be added to b
        b (int or float): Value b to be added to a

    Return:
        The result of the addition of a and b

    a and b must integers or floats

    Raises:
        TypeError: If `a` or `b` or both is not either int or float
            you get error message ``a must be an integer`` or
            ``b must be an integer``
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
