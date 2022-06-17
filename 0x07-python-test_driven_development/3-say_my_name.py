#!/usr/bin/python3
""" Gets and prints users first and last name """


def say_my_name(first_name, last_name=""):
    """
    Prints out "My name is <first_name> <last_name>"
    where fist_name and last_name are the args``first_name``
    and ``last_name`` respectively.

    Args:
       first_name (str): first arg to be printed
       last_name (str): last arg to be printed
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
