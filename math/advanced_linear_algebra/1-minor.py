#!/usr/bin/env python3
'''Module of Advanced Linear Algebra'''


def minor(matrix):
    '''calculates the determinant of a matrix'''

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
    
    n = len(matrix)
    minors = []

    for i in range(n):
        row = []

        for j in range(n):
            submatrix = [
                [value for col_index, value in enumerate(r) if col_index != j]
                for row_index, r in enumerate(matrix) if row_index != i
            ]

            row.append(int(round(np.linalg.det(submatrix))))

        minors.append(row)

    return minors
