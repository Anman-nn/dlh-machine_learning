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
            self.n = int(n)
            self.p = float(p)

        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)

            p = 1 - (variance / mean)
            n = round(mean / p)
            p = mean / n
            self.n = int(n)
            self.p = float(p)
    def pmf(self, k):
        '''Calculates the value of the PMF'''
        k = int(k)

        if k < 0 or k > self.n:
            return 0

        def factorial(num):
            result = 1
            for i in range(1, num + 1):
                result *= i
            return result

        combination = factorial(self.n) / (
            factorial(k) * factorial(self.n - k)
        )

        return combination * (self.p ** k) * ((1 - self.p) ** (self.n - k))
        
