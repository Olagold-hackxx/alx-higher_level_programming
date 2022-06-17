#!/usr/bin/python3
""" Print square with "#" """


def print_square(size):
    """
    prints square with size ``size``

    Arg:
        size (int): size of square
    """

    if type(size) != int or size is None:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
