#!/usr/bin/env python3
'''Module of Advanced Linear Algebra'''


def determinant(matrix):
    '''calculates the determinant of a matrix'''

    import numpy as np

    if matrix == [[]]:
        return 1

    if not isinstance(matrix, list):
        raise TypeError('matrix must be a list of lists\n' \
        'matrix must be a list of lists\nmatrix must be a list of lists')

    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")

    mat = np.asarray(matrix)
    if mat.ndim != 2:
        raise TypeError('matrix must be a list of lists')

    return round(np.linalg.det(mat))
