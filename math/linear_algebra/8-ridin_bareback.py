#!/usr/bin/env python3
"""Documentatio of the module"""


def mat_mul(mat1, mat2):
    """def mat_mul(mat1, mat2)"""

    if len(mat1[0]) != len(mat2):
        return None
    trans_mat2 = []

    for i in range(len(mat2[0])):
        row = []
        for m in mat2:
            row.append(m[i])
        trans_mat2.append(row)
    res_mat = []

    for row1 in mat1:
        res_row = []
        for row2 in trans_mat2:
            res_row.append(sum([a * b for a, b in zip(row1, row2)]))
        res_mat.append(res_row)
    return res_mat
