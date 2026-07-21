#!/usr/bin/env python3
'''Module for the project Probability'''

import numpy as np

class Normal:
    '''Define a class Normal'''


    def __init__(self, data=None, mean=0., stddev=1.):
        self.mean = mean
        self.stddev = stddev
        if stddev <= 0:
            raise ValueError('stddev must be a positive value')
        if data is None:
            return (mean, stddev)
        return (np.mean(data), np.std(data))