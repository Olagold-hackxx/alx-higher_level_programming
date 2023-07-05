#!/usr/bin/python3
""""""
import requests
from sys import argv


if type(argv[1]) is str and len(argv) >= 1:
    q = argv[1]
else:
    q=""
