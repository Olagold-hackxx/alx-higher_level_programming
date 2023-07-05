#!/usr/bin/python3
""" Get header"""
import requests
from sys import argv


req = requests.get(argv[1])
header = req.headers['X-Request-Id']
print(header)
