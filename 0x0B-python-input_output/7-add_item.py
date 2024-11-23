#!/usr/bin/python3
"""
Adds all arguments to a Python list, and then save
them to a JSON file
"""
import json
from sys import argv
from os.path import exists

if __name__ == "__main__":
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    ADD_STRING = "add_item.json"

    if not exists(ADD_STRING):
        with open(ADD_STRING, mode="w", encoding="utf-8") as f:
            f.write('[]')

    obj = load(ADD_STRING)
    for arg in argv[1:]:
        obj.append(arg)

    save(obj,  ADD_STRING)
