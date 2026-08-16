#!/usr/bin/env python3
'''Module Pandas in the best!!!'''

import pandas as pd


def rename(df):
    '''function Rename'''
    df.rename(columns={'Timestamp': 'Datetime'}, inplace=True)
    df['Datetime'] = pd.to_datetime(df['Datetime'])
    return df[['Datetime', 'Close']]
