#!/usr/bin/env python3
def matrix_shape(matrix):
    x = len(matrix)
    try:
        y = len(matrix[0])
    except TypeError:
        y = 0
    return [x ,y]
