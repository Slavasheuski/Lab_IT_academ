import sympy as sp
import numpy as np
import math as mt
import matplotlib.pyplot as plt

while True:
    def resistance(car):
        Cx_dict = {'Alfa_Romeo 164': 0.30, 'Aston_Martin_DB7': 0.34, 'Audi_200': 0.33,
             'BMW_M3_E46': 0.32, 'Chevrolet_Camaro': 0.35, 'Ferrari_F50': 0.37,
             'Ford_Focus_ST': 0.34, 'Honda_S2000': 0.33, 'Lamborghini_Gallardo': 0.35,
             'Lotus_Elise': 0.34}
        C = sp.Symbol('Cx') 
        S, V, p = sp.symbols("S, V, ρ")
        p = 1.23
        S = 2
        V = [int(i) for i in range(25,250,10)]
        C = Cx_dict[car]
        result = []
        for j in V:
            F_АС = (C*S)*((j*1000/3600)**2*p/2)
            result.append(F_АС)
    
    
        plt.plot(result,V)           
        plt.grid()
        plt.title('График зависимости cилы аэродинамического сопротивления от скорости')
        plt.xlabel('Cила аэродинамического сопротивления (Н)')
        plt.ylabel('Скорость (км/ч)')
        plt.show()


    car = input('Выберите и введите марку и модель автомобиля из списка:\n Alfa_Romeo_164\n Aston_Martin_DB7\n Audi_200\n BMW_M3_E46\n Chevrolet_Camaro\n Ferrari_F50\n Ford_Focus_ST\n Honda_S2000\n Lamborghini_Gallardo\n Lotus_Elise\n')
    resistance(car)

    question = input('Хотите ли проверить ещё одну машину из списка? (да/нет)').lower()

    if question == 'нет':
        break
