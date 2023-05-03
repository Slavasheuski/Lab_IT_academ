import pandas as pd
import matplotlib.pyplot as plt
from neuralprophet import NeuralProphet

df = pd.read_csv('lab23_1.csv')
df.plot(x='ds', y='y', title='Log daily page views')
plt.show()

#getting the train/test split
test_length = 365
df_train = df.iloc[:-test_length]
df_test = df.iloc[-test_length:]

m = NeuralProphet()
metrics = m.fit(df_train, freq="D")
future_df = m.make_future_dataframe(df_train, 
                                    periods = test_length, 
                                    n_historic_predictions=len(df_train))
forecast = m.predict(future_df)
print(forecast)

m.plot(forecast)
plt.show()
