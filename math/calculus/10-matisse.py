#!/usr/bin/env python3
'''Module for project Calculus'''


def poly_derivative(poly):
    '''function poly_derivative'''

    if not isinstance(poly, list):
        return None
    if poly[1] == 0 and len(poly) == 2:
        return 0
    res = []
    for i in range(1,len(poly)):
        res.append(i*poly[i])
    return res
