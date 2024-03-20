#!/usr/bin/python3
<<<<<<< HEAD
"""Fetches data from given URL"""


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')\
            as response:
        html = response.read()

        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode("utf-8", "replace")))
=======
"""
fetch a url
"""

import urllib.request
url = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(url) as response:
    body = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(body)))
    print('\t- content: {}'.format(body))
    print('\t- utf8 content: {}'.format(body.decode()))
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
