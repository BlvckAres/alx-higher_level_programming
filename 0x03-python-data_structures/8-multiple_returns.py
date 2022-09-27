#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple1 = ()
    if len(sentence) == 0:
        first = 0
    else:
        num = len(sentence)
        first = sentence[0]
        new_tuple1 = (num, first)
        return new_tuple1
