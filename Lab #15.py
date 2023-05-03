import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'Э1': [2, 5, 3, 1, 4],
                  'Э2': [1, 2, 3, 4, 5],
                  'Э3': [2, 3, 5, 1, 4],
                  'Э4': [5, 4, 2, 3, 1],
                  'Э5': [3, 2, 4, 5, 1]},
index = ['A1', 'A2', 'A3', 'A4', 'A5'])

df['row_avr'] = df.mean(axis=1) #Расчитываем среднее и добавляем в табличку

print(df)

#Область доверительности рассчитается следующим образом:

mn = min(df['row_avr']) #минимальное место
mx = max(df['row_avr']) #максимальное место

kv = (mx - mn) / 4 #Квартиль будет равна
low = mn + kv #Нижняя граница доверительной области
high = mx - kv #Верхняя граница доверительной области


fig, ax = plt.subplots()

plt.title("Отчет") 
plt.xlabel("Альтернативные варианты") 
plt.ylabel("Среднее место среди экспертов") 
plt.plot(df['row_avr'], marker = 'o', markerfacecolor = 'yellow') 
plt.show()

