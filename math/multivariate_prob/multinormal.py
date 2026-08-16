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

def pdf(self, x):
    """Calculate the PDF at a data point."""
    if not isinstance(x, np.ndarray):
        raise TypeError("x must be a numpy.ndarray")

    d = self.mean.shape[0]

    if x.shape != (d, 1):
        raise ValueError("x must have the shape ({}, 1)".format(d))

    pi = np.pi
    diff = x - self.mean
    det = np.linalg.det(self.cov)
    inv = np.linalg.inv(self.cov)

    exponent = -0.5 * (diff.T @ inv @ diff)
    denominator = np.sqrt(((2 * pi) ** d) * det)

    return float((1 / denominator) * np.exp(exponent))
