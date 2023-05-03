import pandas as pd
import quandl as qd

#Получить API KEY на сайте https://www.nasdaq.com/solutions/data-link-api
qd.ApiConfig.api_key = 'Tzk2TCGCG5kcyYE_zRP1'
msft_data = qd.get('EUR/USD', start_date = '2018-01-01', end_date = '2019-01-01')
print(msft_data)

close_price = msft_data[['Close']]
daily_return = close.price.pct_change()
daily_return.fillna(0, inplase=True)
print(daily_return)

adj_price = msft_data['Close']
mav = adj_price.rolling(window = 50).mean()
print(mav[-10:])

