#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Compute the square value of all integers of a matrix

    """
    return ([list(map(lambda x: x * x, i)) for i in matrix])