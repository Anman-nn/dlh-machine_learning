#!/usr/bin/env python3
'''Module for project Calculus'''


def poly_integral(poly, C = 0):
    '''poly integral'''
    if not isinstance(poly, list):
        return None

    res = [C]
    for i in range(len(poly)):
        res.append(poly[i]/(i+1))

    return res
