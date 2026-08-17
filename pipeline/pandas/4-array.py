#!/usr/bin/env python3
'''Module Pandas is the best!!!'''


def array(df):
    last10 = df.iloc[-10:]
    return last10.to_numpy()
