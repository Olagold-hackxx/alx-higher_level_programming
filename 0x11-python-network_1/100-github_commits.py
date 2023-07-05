#!/usr/bin/python3
"""Request commits via GitHub API
"""

import requests
from sys import argv

if __name__ == '__main__':

    repo = argv[1]
    owner = argv[2]

    url = 'https://api.github.com/repos/{}/{}/\
commits?per_page=10'.format(owner, repo)

    req = requests.get(url)

    req = req.json()

    for commit in req:
        print('{}: {}'.format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
