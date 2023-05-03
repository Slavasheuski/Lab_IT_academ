from sympy import *
import pandas as pd
import matplotlib.pyplot as plt


class Report:
    @staticmethod
    def growth_rate_chain(vol_of_sales):
        res_1 = ['-']
        for i in range(1, len(vol_of_sales)):
            res_1.append(round(vol_of_sales[i] / vol_of_sales[i - 1], 2))
        return res_1

    @staticmethod
    def growth_rate_bas(vol_of_sales):
        res_2 = ['-']
        for j in range(1, len(vol_of_sales)):
            res_2.append(round(vol_of_sales[j] / vol_of_sales[0], 2))
        return res_2

print('Темп рост цепной определяется по формуле:')
Tp, c, yi, yii = symbols('Tp ц y(i) y(0)')
print(Eq(Tp ** c,yi / yii))
print()

print('Темп рост базисный определяется по формуле:')
Tp, b, yi, yii = symbols('Tp б y(i) y(i-1)')
print(Eq(Tp ** b,yi / yii))
print()

print('Cреднемесячный темп роста объема продаж определяется по формуле:')
T, y_s, n = symbols('ΔT Σy(i) (n-1)')
print(Eq(T, y_s / n))
print()

a = Report()
vol_of_sales = [2.5, 3.0, 3.8, 4.2, 4.5]
chain = a.growth_rate_chain(vol_of_sales)
bas = a.growth_rate_bas(vol_of_sales)

avg = sum(chain[1:]) / (len(chain) - 1) * 100 - 100
print(f'Cреднемесячный темп роста объема продаж торговой организации: {round(avg)}%')
print()

df = pd.DataFrame([['Объем продаж, млн. руб.'] + vol_of_sales,
                  ['Темп роста (цепной)'] + chain,
                  ['Темп роста (базисный)'] + bas], 
columns=['Месяцы', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь'])

print(df)

fig, ax = plt.subplots()

plt.title("Отчет") 
plt.xlabel("Объем продаж, млн. руб.") 
plt.ylabel("Темп роста (цепной)") 
plt.plot(vol_of_sales, chain, marker = 'o', markerfacecolor = 'yellow') 
plt.show()

plt.title("Отчет") 
plt.xlabel("Объем продаж, млн. руб.") 
plt.ylabel("Темп роста (базисный)") 
plt.plot(vol_of_sales, bas, marker = 'o', markerfacecolor = 'yellow') 
plt.show()
