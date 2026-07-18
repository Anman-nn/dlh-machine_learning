#!/usr/bin/env python3
'''Module for the project Probability'''


class Poisson:
    '''Define a class Poisson'''

    def __init__(self, data=None, lambtha=1.):
        if data is None:
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        '''Calculate the PMF for a given number of successes'''
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        fact = 1
        for i in range(1, k + 1):
            fact *= i
        return (self.lambtha ** k) * (2.7182818285 ** (-self.lambtha)) / fact

    def cdf(self, k):
        '''calculates CDF'''
        k = int(k)

        if k < 0:
            return 0

        total = 0
        for i in range(k + 1):
            total += self.pmf(i)

        return total
