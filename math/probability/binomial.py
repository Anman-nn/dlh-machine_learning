#!/usr/bin/env python3
'''Module for the project Probability'''


class Binomial:
    '''Define a class Binomial'''

def __init__(self, data=None, n=1, p=0.5):

    if data is None:
        if n <= 0:
            raise ValueError('n must be a positive value')
        if not 0 < p < 1:
            raise ValueError('p must be greater than 0 and less than 1')
        self.n = n
        self.p = p
    else:
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)

        p = 1 - (variance / mean)
        n = round(mean / p)
        p = mean / n
