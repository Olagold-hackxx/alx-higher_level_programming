#!/usr/bin/python3
"""Search JSON"""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'

    if len(argv) > 1:
        q = argv[1]
    else:
        q = ''
    req = requests.post(url, data={'q': q})
    try:
        req = req.json()

        if not req:
            print('No result')
        else:
            print('[{}] {}'.format(req.get('id'), req.get('name')))
    except ValueError:
        print('Not a valid JSON')
