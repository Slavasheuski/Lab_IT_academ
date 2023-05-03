import numpy as np
import matplotlib.pyplot as plt

price = [16556, 16950, 20766, 22864, 23239, 22869, 21833, 24436]

my_dict = {}

for i in range(1, len(price)):
    my_dict[i] = my_dict.get(i, (price[i] - price[i-1]) / price[i-1] * 100)

count_up = 0
count_down = 0

for num in my_dict.values():
    if num > 0:
        count_up += 1
    else:
        count_down += 1

if count_up > count_down:
    print('Тренд восходящий')
else:
    print('Тренд нисходящий')

fig, axes = plt.subplots()

axes.bar([j for j, a in my_dict.items() if a < 0], [k for k in my_dict.values() if k < 0], color='red')
axes.bar([j for j, a in my_dict.items() if a > 0], [k for k in my_dict.values() if k > 0], color='blue')


axes.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(5)
fig.set_figheight(6)
plt.show()

plt.plot([j for j in my_dict], [k for k in my_dict.values()])
plt.grid()
plt.show()
