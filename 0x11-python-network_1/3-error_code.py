#!/usr/bin/python3
"""
handle http error
"""

import urllib.request
import sys
import urllib.error
if __name__ == '__main__':
    url = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
    except urllib.HTTPError as error:
        print('Error code: {}'.format(urllib.error.error.code))
    else:
        print(body.decode('utf-8'))
