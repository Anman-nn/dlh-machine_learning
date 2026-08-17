#!/usr/bin/env python3
'''Module Pandas is the best!!!'''


def array(df):
    import pandas as pd
    last10 = df.iloc[-10:]
    return last10.to_numpy()
