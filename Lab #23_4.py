import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import mplfinance as mpl
from mpl_finance import candlestick_ohlc
import datetime

data = pd.read_csv('btc1.csv')

change = data["Close"].diff()
change.dropna(inplace=True)

change_up = change.copy()
change_down = change.copy()

change_up[change_up<0] = 0
change_down[change_down>0] = 0

change.equals(change_up+change_down)

avg_up = change_up.rolling(14).mean()
avg_down = change_down.rolling(14).mean().abs()

rsi = 100 * avg_up / (avg_up + avg_down)
rsi.head(20)

plt.style.use('fivethirtyeight')

plt.rcParams['figure.figsize'] = (20, 20)

ax1 = plt.subplot2grid((10,1), (0,0), rowspan = 4, colspan = 1)
ax2 = plt.subplot2grid((10,1), (5,0), rowspan = 4, colspan = 1)

ax2.set_title('Bitcoin Close Price')
ax2.plot(data['Date'], data['Close'], linewidth=2)
plt.xticks(rotation=90, fontsize=10)

ax1.set_title('Relative Strength Index')
ax1.plot(rsi, color='orange', linewidth=1)

ax1.axhline(30, linestyle='--', linewidth=1.5, color='green')
ax1.axhline(70, linestyle='--', linewidth=1.5, color='red')

plt.show()
