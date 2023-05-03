from math import*

c = 299792458
weights = []

while True:
    weights.append(int(input('Введите массу объекта(кг): ')))
    question = input('Может есть ещё один объект(да/нет): ').lower()
    if question == 'нет':
        break
    
for m in weights:
    E = m * pow(c, 2) / 1000000
    print('Энергия вашего объекта равна: ' + str(E) + 'МДж')
    

