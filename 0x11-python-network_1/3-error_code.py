#!/usr/bin/python3
"""Send request and print response body or error code"""
import urllib.request
import urllib.error
from sys import argv


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
            print(the_page.decode('utf8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
