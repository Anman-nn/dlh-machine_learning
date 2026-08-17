#!/usr/bin/env python3
'''Module Pandas is the best!!!'''


def array(df):
    '''def array(df)'''
    last10 = df[['High', 'Close']].iloc[-10:]
    return last10.to_numpy()
