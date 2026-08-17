#!/usr/bin/env python3
'''Module Pandas in the best!!!'''


def fill(df):
    '''def fill(df):'''
    df1 = df.drop(columns=['Weighted_Price'])
    df1['Close'] = df1['Close'].ffill()
    df1["High"] = df1["High"].fillna(df1["Close"])
    df1["Low"] = df1["Low"].fillna(df1["Close"])
    df1["Open"] = df1["Open"].fillna(df1["Close"])
    df1['Volume_(BTC)'] = df1['Volume_(BTC)'].fillna(0)
    df1['Volume_(Currency)'] = df1['Volume_(Currency)'].fillna(0)
    return df1
