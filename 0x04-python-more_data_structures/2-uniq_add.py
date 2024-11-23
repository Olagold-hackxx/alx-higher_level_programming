#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    uniq_list = list(my_set)
    uniq_sum = 0
    for i in range(len(uniq_list)):
        uniq_sum += uniq_list[i]
    return uniq_sum
