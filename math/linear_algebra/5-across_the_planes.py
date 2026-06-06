#!/usr/bin/env python3
"""Documentatio of the module"""


def add_matrices2D(mat1, mat2):
    res_mat = []
    for row1, row2 in zip(mat1, mat2):
        res_row = [a + b for a, b in zip(row1, row2)]
        res_mat.append(res_row)
    return res_mat
