#!/usr/bin/python3
"""Finds peak in unsorted list of integers"""


def find_peak(list_of_integers):
    """Finds peak in unsorted list of integers"""

    if not list_of_integers:
        return None

    length = len(list_of_integers)
    mid = length // 2
    if length > 1:
        if mid >= mid - 1 and mid >= mid + 1:
            return mid
        if (mid == length - 1 or list_of_integers[mid] >=
            list_of_integers[mid + 1])\
                and (mid == 0 or list_of_integers[mid] >=
                     list_of_integers[mid - 1]):
            return list_of_integers[mid]
        if list_of_integers[0] >= list_of_integers[1]:
            return list_of_integers[0]
        if list_of_integers[-1] >= list_of_integers[-2]:
            return list_of_integers[-1]
    return find_peak(list_of_integers[mid:])
