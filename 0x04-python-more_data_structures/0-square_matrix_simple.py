#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    a_matrix = ([list(map(lambda x: x ** 2, row)) for row in matrix])
    return a_matrix
