#!/usr/bin/env python3
'''Module of Advanced Linear Algebra'''


import numpy as np

def definiteness(matrix):
    '''def definiteness(matrix)'''

    if not isinstance(matrix, np.ndarray):
        raise TypeError('matrix must be a numpy.ndarray')
    
    is_symmetric = np.array_equal(matrix, matrix.T)
    if not is_symmetric:
        return None

    eigenvalues = np.linalg.eigvalsh(matrix)
    if np.all(eigenvalues > 0):
        return 'Positive definite'
    elif np.any(eigenvalues >= 0):
        return 'Positive semi-definite'
    elif np.all(eigenvalues < 0):
        return 'Negative definite'
    elif np.any(eigenvalues <= 0):
        return 'Negative semi-definite'  
    else:
        return None
