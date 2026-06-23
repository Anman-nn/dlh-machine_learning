#!/usr/bin/env python3
'''Module of Advanced Linear Algebra'''


def inverse(matrix):
    '''def inverse(matrix):'''

    import numpy as np

    if not isinstance(matrix, list):
        raise TypeError(
            'matrix must be a list of lists\n'
            'matrix must be a list of lists\n'
            'matrix must be a list of lists')

    if any(len(row) != len(matrix) for row in matrix) or not matrix:
        raise ValueError("matrix must be a non-empty square matrix")
    
    if len(matrix[0]) == 1:
        return [[1]]
    
    matrix = np.array(matrix)
    if matrix.ndim != 2:
        raise TypeError('matrix must be a list of lists')

    n = matrix.shape[0]
    cofactors = []

    for i in range(n):
        row = []

        for j in range(n):
            submatrix = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            minor_det = round(np.linalg.det(submatrix))
            row.append(((-1) ** (i + j)) * int(minor_det))

        cofactors.append(row)

    det = np.linalg.det(matrix)

    if det == 0:
        return None

    inv_mat = np.round(np.transpose(cofactors) / det)
    return inv_mat.tolist()
