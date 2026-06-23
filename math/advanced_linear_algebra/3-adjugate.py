#!/usr/bin/env python3
'''Module of Advanced Linear Algebra'''


def adjugate(matrix):
    '''def cofactor(matrix):'''

    import numpy as np

    if not isinstance(matrix, list):
        raise TypeError(
            'matrix must be a list of lists\n'
            'matrix must be a list of lists\n'
            'matrix must be a list of lists')

    if any(len(row) != len(matrix) for row in matrix) or not matrix:
        raise ValueError("matrix must be a non-empty square matrix")
    matrix = np.array(matrix)
    if matrix.ndim != 2:
        raise TypeError('matrix must be a list of lists')

    if len(matrix[0]) == 1:
        return [[1]]

    return matrix.T
