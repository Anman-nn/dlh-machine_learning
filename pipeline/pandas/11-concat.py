#!/usr/bin/env python3
'''Module Pandas is the best!!!'''


def concat(df1, df2):
    '''dsfsdfdsfsdf'''
    import pandas as pd
    index = __import__('10-index').index
    i_df1 = index(df1)
    i_df2 = index(df2)
    i_df2 = i_df2.loc[:1417411920]
    return pd.concat([i_df2, i_df1], 
                     axis=0,
                     keys=['bitstamp', 'coinbase']
    )

