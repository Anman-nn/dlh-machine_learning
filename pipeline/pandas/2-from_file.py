#!/usr/bin/env python3
'''Module Pandas in the best!!!'''

import pandas as pd


def from_file(filename, delimiter):
    '''Function def from_file(filename, delimiter)'''

    return pd.read_csv(filename, delimiter=delimiter)
