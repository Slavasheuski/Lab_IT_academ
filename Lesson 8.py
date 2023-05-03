#Разработал: Славашевский Сергей Витальевич
#Designed by: Slavasheuski Siarhei Vitalevich

import sympy as sp
import numpy as np
import math as mt
import matplotlib.pyplot as plt

class Formula:
    
    _s = 0.47
    _v = 27
    _p = 1.23
    
    @staticmethod
    def func_x(c_x):
        res_1 = list(map(lambda x: x * ((Formula._p * Formula._v**2) / 2) * Formula._s, c_x))
        return res_1

    @staticmethod
    def func_y(c_y):
        res_2 = list(map(lambda y: y * ((Formula._p * Formula._v**2) / 2) * Formula._s, c_y))
        return res_2

    def __init__(self, c_x, c_y):
        self.x = self.func_x(c_x)
        self.y = self.func_y(c_y)

    def graph(self):
        plt.plot(self.x, self.y)           
        plt.grid()
        plt.title('График зависимости cилы аэродинамического сопротивления от подъемной силы')
        plt.xlabel('Подъемная сила (Н)')
        plt.ylabel('Сила аэродинамического сопротивления (Н)')
        plt.show()
        
c_y = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0], dtype=float)
c_x = np.array([0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1], dtype=float)

a = Formula(c_x, c_y)

a.graph()

class Formula_1(Formula):
    
    def graph(self):
        plt.plot(self.y, self.x)           
        plt.grid()
        plt.title('График зависимости cилы аэродинамического сопротивления от подъемной силы')
        plt.ylabel('Подъемная сила (Н)')
        plt.xlabel('Сила аэродинамического сопротивления (Н)')
        plt.show()

b = Formula_1(c_x, c_y)

b.graph()
