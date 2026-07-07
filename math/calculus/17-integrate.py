#!/usr/bin/env python3
'''Module for project Calculus'''


def poly_integral(poly, C=0):
    '''poly integral'''
    if not isinstance(poly, list) or poly == [] or None in poly:
        return None

    if poly == [0]:
        return [C]

    res = [C]
    for i in range(len(poly)):
        if poly[i] % (i + 1) == 0:
            res.append(poly[i] // (i + 1))
        else:
            res.append(poly[i] / (i + 1))

    return res
