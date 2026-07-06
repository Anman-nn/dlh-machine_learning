#!/usr/bin/env python3
'''Module for project Calculus'''


def poly_derivative(poly):
    '''function poly_derivative'''

    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if len(poly) == 1:
        return [0]

    res = []
    for i in range(1,len(poly)):
        res.append(i*poly[i])
    return res
