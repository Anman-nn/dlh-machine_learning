#!/usr/bin/env python3
"""Documentatio of the module"""


def matrix_transpose(matrix):
    """Returns the transpose matrix"""
    res = []
    for i in range(len(matrix[0])):
        row = []
        for m in matrix:
        row.append(m[i])
        res.append(row)
    return res
