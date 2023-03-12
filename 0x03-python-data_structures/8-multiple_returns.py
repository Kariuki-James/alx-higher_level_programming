#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence is None:
        return (0, None)

    str_len = len(sentence)
    return (str_len, sentence[0])
