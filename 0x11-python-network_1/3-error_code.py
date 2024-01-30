#!/usr/bin/python3
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
    except HTTPError as err:
        print('Error code: {}'.format(err.code))
    else:
        print(body.decode('utf-8'))
