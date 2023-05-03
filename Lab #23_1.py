import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_csv('lab23_1.csv')
print(df)

dt = df.plot(x='ds', y='y')
plt.show()

y = df['y']
x = df['ds']

x = sm.add_constant(y)

model = sm.OLS(y,x).fit()
print(model.summary())

