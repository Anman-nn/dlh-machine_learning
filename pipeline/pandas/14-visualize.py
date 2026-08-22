#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

df.rename(columns={'Timestamp': 'Date'}, inplace=True)
df = df.drop(columns=['Weighted_Price'])
df['Date'] = pd.to_datetime(df['Date'], unit='s').dt.normalize()
df = df.set_index('Date').sort_index()
df.Close = df.Close.ffill()
df["High"] = df["High"].fillna(df["Close"])
df["Low"] = df["Low"].fillna(df["Close"])
df["Open"] = df["Open"].fillna(df["Close"])
df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)
df = df.loc['2017']
grouped = df.groupby(df.index).agg({'High':'max', 'Low':'min', 
                                    'Open':'mean', 'Close':'mean',
                                    'Volume_(BTC)':'sum', 'Volume_(Currency)':'sum'
})

for col in ["High", "Low", "Open", "Close", "Volume_(BTC)", "Volume_(Currency)"]:
    plt.plot(grouped.index, grouped[col], label=col)
    plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
plt.legend()
plt.show()