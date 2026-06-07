#!/usr/bin/env python3
"""Documentatio of the module"""


def cat_matrices2D(mat1, mat2, axis=0):
    """sjkdhkjsdhfdsjkhf"""
    res = mat1.copy()
    if axis == 0:
        for row_m2 in mat2:
            if len(row_m2) != len(res[0]):
                return None
            res.append(row_m2)
        return res

    if axis == 1:
        if len(mat1) != len(mat2):
            return None
        for i in range(len(mat1)):
            res[i] += mat2[i]
        return res
