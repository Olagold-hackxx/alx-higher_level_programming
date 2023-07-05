#!/usr/bin/python3
""" Get header"""
import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get(argv[1])
    header = req.headers['X-Request-Id']
    print(header)
