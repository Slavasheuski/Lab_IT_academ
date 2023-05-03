import yfinance as yf
import pandas as pd
import os
import plotly.express as px
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

if os.path.exists('sp500.csv'):
    sp500 = pd.read_csv('sp500.csv')
else:
    sp500 = yf.Ticker('^GSPC')
    sp500 = sp500.history(period = 'max')
    sp500.to_csv('sp500.csv')

sp500.index = pd.to_datetime(sp500.index)
print(sp500)

#fig = px.bar(sp500, y='High', x='Date', text_auto='.2s',
            #title="Статистика")
#fig.show()

def animate(i):
    data = pd.read_csv('sp500.csv')
    x = data['Date'][::356]
    y = data['High'][::356]

    plt.cla()
    plt.xticks(rotation=90)
    plt.plot(x, y)
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
