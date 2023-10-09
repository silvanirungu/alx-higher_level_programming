#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    mtp = tuple()
    if x == 0:
        mtp = x, None,
    else:
        mtp = x, sentence[0]
    return mtp
