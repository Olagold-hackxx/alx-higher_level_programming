#!/usr/bin/python3
"""Send POST request"""
import requests
from sys import argv


req = requests.post(argv[1], data={'email': argv[2]})
print(req.text)
