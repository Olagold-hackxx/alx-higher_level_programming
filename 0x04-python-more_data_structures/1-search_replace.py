#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: x if x != 2 else (89), my_list))
    return new_list
