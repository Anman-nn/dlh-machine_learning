#!/usr/bin/env python3
def matrix_shape(matrix):
    """Returns the sixe of any dimentional matrix"""
    x = []
    while isinstance(matrix, list):
        x.append(len(matrix))
        if not matrix:
            break
        matrix = matrix[0]
    return x
