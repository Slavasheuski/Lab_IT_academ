import numpy as np
import matplotlib.pyplot as plt


all_x = []
all_y = []

while True:
    x = float(input('Введите значение x от 0 до 100: '))
    y = float(input('Введите значение y от -100 до 100: '))
        
    all_x.append(x) 
    all_y.append(y)

    q = input('Добавим ещё значения?(y/n): ')
    if q == 'n':
        break
    
x1 = np.array(all_x, dtype=float)
y1 = np.array(all_y, dtype=float)

fig, axes = plt.subplots()

axes.bar(x1, y1)

axes.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(15)    #  ширина Figure
fig.set_figheight(6)    #  высота Figure

plt.show()


plt.plot(x1, y1)           
plt.grid()
plt.show()
