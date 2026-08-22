#!/usr/bin/env python3
'''Module Pandas is the best!!!'''


def analyze(df):
    return df.drop(columns=['Timestamp']).describe()
