(sentence):
    if len(sentence) == 0:
        return 0, None
    else:
        return len(sentence), sentence[0]
