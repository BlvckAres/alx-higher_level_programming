#!/usr/bin/python3
def max_integer(my_list=[]):
    largest = 0
    if len(my_list) == 0:
        largest = None
        return largest
    else:
        for x in my_list:
            if x > largest:
                largest = x
        return largest
