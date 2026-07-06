#!/usr/bin/env python3
'''Module for project Calculus'''


def poly_derivative(poly):
    '''function poly_derivative'''
    res = []
    for i in range(1,len(poly)):
      res.append(i*poly[i])
    return res
