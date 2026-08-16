#!/usr/bin/env python3
'''Module Pandas in the best!!!'''

import pandas as pd


def from_numpy(array):
    colnames = [chr(65+i) for i in range(array.shape[1])]
    return pd.DataFrame(array, columns=colnames)
