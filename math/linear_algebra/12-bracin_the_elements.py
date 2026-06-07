#!/usr/bin/env python3
"""Documentatio of the module"""


def np_elementwise(mat1, mat2):
    import numpy as np
    return tuple(
        mat1 + mat2,
        mat1 - mat2,
        mat1 * mat2,
        mat1 / mat2
    )
