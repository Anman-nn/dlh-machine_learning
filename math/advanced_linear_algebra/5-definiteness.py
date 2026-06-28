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
    if eigenvalues > 0:
        return 'Positive definite'
    elif eigenvalues >= 0:
        return 'Positive semi-definite'
    elif eigenvalues < 0:
        return 'Negative definite'
    elif eigenvalues <= 0:
        return 'Negative semi-definite'  
    else:
        return None
