#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    if len(tuple_a) < 2:
        for i in range(len(list_a), 2):
            list_a.append(0)
    if len(tuple_b) < 2:
        for i in range(len(list_b), 2):
            list_b.append(0)
    new_list = [list_a[0] + list_b[0], list_a[1] + list_b[1]]
    new_tuple = tuple(new_list)
    return new_tuple
