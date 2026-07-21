#!/usr/bin/env python3
'''Module for the project Probability'''


class Normal:
    '''Define a class Normal'''

    def __init__(self, data=None, mean=0., stddev=1.):
        self.mean = mean
        self.stddev = stddev
        if stddev <= 0:
            raise ValueError('stddev must be a positive value')
        if data is None:
            return (mean, stddev)
        if not isinstance(data, list):
            raise TypeError('data must be a list')

        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        stddev = variance ** 0.5
        return (mean, stddev)
