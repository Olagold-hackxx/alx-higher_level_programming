#!/usr/bin/python3
"""Print response body"""
import requests


if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    the_page = req.text
    print('Body response:')
    print('\t- type: {}'.format(type(the_page)))
    print('\t- content: {}'.format(the_page))
