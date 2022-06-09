#!/usr/bin/python3
def max_integer(my_list=[]):
    _sum = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > _sum:
            _sum = my_list[i]
    return _sum
