#!/usr/bin/env python3
'''Module Pandas in the best!!!'''


def prune(df):
    '''def prune(df):'''
    return df.loc[df.Close.notna()]
