#!/usr/bin/python3
""" Get header"""
import urllib.request
import sys


req = urllib.request.urlopen(sys.argv[1])
with req as response:
    header = response.getheader('X-Request-Id')
print(header)
