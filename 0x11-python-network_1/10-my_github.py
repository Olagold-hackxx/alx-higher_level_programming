#!/usr/bin/python3
"""Request id from GitHub API
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/user'

    user = argv[1]
    token = argv[2]
    req = requests.get(url, auth=(user, token))
    print(req.json().get('id'))
