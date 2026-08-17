#!/usr/bin/env python3
'''Module Pandas in the best!!!'''


def slice(df):
    '''function documentation'''
    rows = [i for i in range(1, df.shape[0]) if i%60 == 0]
    return df[['High', 'Low', 'Close', 'Volume_(BTC)']].loc[rows]
