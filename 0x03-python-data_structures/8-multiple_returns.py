#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return_tuple = 0, None
        return return_tuple
    else:
        return_tuple = len(sentence), sentence[0]
        return return_tuple
