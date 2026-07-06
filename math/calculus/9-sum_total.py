#!/usr/bin/env python3
'''Module for project Calculus'''


def summation_i_squared(n):
    '''function summation_i_squared'''

    if n < 1:
        return None

    return n * (n + 1) * (2 * n + 1) // 6
