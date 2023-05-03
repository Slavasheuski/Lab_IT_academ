def drag_force(v):
    for i in v:
        print('Сила лобового сопротивления при скорости', i, 'м/с равна: ', i ** 2, 'Н')

v = []

while True:
    v.append(int(input('Введите скорость машины(м/с): ')))
    
    question = input('Хотите ли ввести ещё скорость?(да/нет): ').lower()
    if question == 'нет':
        break


drag_force(v)
