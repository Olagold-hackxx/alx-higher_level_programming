#!/usr/bin/python3
""" Deserialize to JSON """


def from_json_string(my_str):
    """ Deserialize obj to json str"""

    import json

    return json.loads(my_str)
