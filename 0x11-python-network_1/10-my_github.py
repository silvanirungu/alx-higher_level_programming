#!/usr/bin/python3
""" get the id of my github account"""

import sys
import requests

if __name__ == "__main__":
    response = requests.get('https://api.github.com/user', auth=(sys.argv[1], sys.argv[2]))
    try:
        body = response.json()
        print(body['id'])
    except KeyError:
        print('None')
