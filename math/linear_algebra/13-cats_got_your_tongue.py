#!/usr/bin/env python3
"""Documentatio of the module"""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    '''np_cat(mat1, mat2, axis=0)'''
    return np.concatenate((mat1, mat2), axis)
