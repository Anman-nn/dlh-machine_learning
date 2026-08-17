#!/usr/bin/env python3
'''Module Pandas in the best!!!'''


def flip_switch(df):
    '''def flip_switch(df):'''
    return df.sort_values('Timestamp', ascending=False).T
