#!/usr/bin/env python3
'''Module Pandas in the best!!!'''

import pandas as pd


def array(df):
    last10 = df.iloc[-10:]
    return last10.to_numpy()
