import random
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_value = 0
total_1 = 1000
total_2 = 1000
fieldnames = ['x_value','total_1', 'total_2']

with open('1.csv', 'w') as f:
    csv_writer = csv.DictWriter(f, fieldnames = fieldnames)
    csv_writer.writeheader()
    
while x_value < 50:
    with open('1.csv', 'a') as f:
        csv_writer = csv.DictWriter(f, fieldnames = fieldnames)
        
        info = {
            'x_value': x_value,
            'total_1': total_1,
            'total_2': total_2,
            }

        csv_writer.writerow(info)
        print(x_value, total_1, total_2)
        
        x_value += 1
        total_1 = total_1 + random.randint(-6, 8)
        total_2 = total_2 + random.randint(-5, 6)
    time.sleep(1)

def animate(i):
    data = pd.read_csv('1.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()

    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
