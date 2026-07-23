#!/usr/bin/env python3
'''Module for the project Probability'''


class Normal:
    '''Define a class Normal'''

    def __init__(self, data=None, mean=0., stddev=1.):
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")

            self.mean = float(mean)
            self.stddev = float(stddev)

        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.mean = sum(data) / len(data)
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            self.stddev = variance ** 0.5

    def z_score(self, x):
        '''returns z-score of x'''
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        '''returns x of z-score'''
        return z * self.stddev + self.mean

    def pdf(self, x):
        '''returns PDF(x)'''
        z = self.z_score(x)
        e = 2.7182818285
        pi = 3.1415926536
        pdf = (1 / (self.stddev * ((2 * pi) ** 0.5))) * (e ** (-(z ** 2) / 2))
        return pdf
