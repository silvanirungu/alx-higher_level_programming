#!/usr/bin/python3
<<<<<<< HEAD
def safe_function(fct, *args):
    import sys
    try:
        ret = fct(*args)
        return ret
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
=======
from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return res
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
