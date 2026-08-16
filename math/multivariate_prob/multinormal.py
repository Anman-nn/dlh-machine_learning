#!/usr/bin/env python3
'''Module for the Multivariate Probability'''


import numpy as np


class MultiNormal:
    """class MultiNormal distribution"""

    def __init__(self, data):
        """class MultiNormal distribution"""
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)

        centered = data - self.mean
        self.cov = (centered @ centered.T) / (n - 1)
