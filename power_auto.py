import numpy as np

while True:
    def power(m, power_motor):
        P_ud = m * power_motor
        return f'Удельная мощность данного авто равна {np.array([P_ud])} кг/л.с.'
    
    m = float(input('Введите массу автомобиля(кг): '))
    p = float(input('Введите мощность двигателя автомобиля(л.с.): '))
    
    print(power(m, p))
    print()
    
    question = input('Хотите проверить ещё одну машину?(да/нет) ').lower()

    if question == 'нет':
        print('Пока!')
        break
