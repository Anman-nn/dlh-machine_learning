#!/usr/bin/env python3
'''Module of Advanced Linear Algebra'''



def determinant(matrix):
    '''calculates the determinant of a matrix'''

    import numpy as np

    if matrix == [[]]:
        return 1

    if not isinstance(matrix, list):
        raise TypeError('matrix must be a list of lists')

    mat = np.asarray(matrix)

    if mat.ndim != 2:
        raise TypeError('matrix must be a list of lists') 

    if mat.shape[0] != mat.shape[1]:
        raise ValueError('matrix must be a square matrix')

    return round(np.linalg.det(mat))
