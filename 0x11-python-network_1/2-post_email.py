#!/usr/bin/python3
"""Send POST request"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    values = {}
    values['email'] = argv[2]
    data = urllib.parse.urlencode(values)
    data = data.encode('utf8')
    req = urllib.request.Request(argv[1], data)

    with urllib.request.urlopen(req) as response:
        page = response.read()
        page = page.decode('utf8')
        print(page)
