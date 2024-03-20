#!/usr/bin/python3
<<<<<<< HEAD
"""script that takes in a URL and displays the body of the response 
(decoded in utf-8)
"""
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
=======
"""
handle http error
"""

import urllib.request
import sys
from  urllib.error import HTTPError
if __name__ == '__main__':
    url = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('ascii'))
    except HTTPError as err:
        print('Error code: {}'.format(err.code))
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
