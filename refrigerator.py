def refrigerator(X, Y, H, A, B):
    if H < B and (X < A or Y < A):
        print('Холодильник проходит в дверной проём! Поздравляем!')
    else:
        print('Упс.. Не пройдёт! Выберите другой холодильник')

while True:
    ref_size = []
    for i in range(3):
        size = int(input('Введите сторону холодилька: '))
        ref_size.append(size)
                                 
    door_size = []
    for j in range(2):
        size = int(input('Введите сторону дверного проема: '))
        door_size.append(size)
                   
    if len(ref_size) == 3 and len(door_size) == 2:
        X, Y, H = ref_size
        A,B = door_size
        refrigerator(X, Y, H, A, B)
    else:
        print('Мало информации. Попробуйте ещё раз!')

    question = input('Хотите попробовать ещё раз? (Да/Нет) ').lower()
    if question == 'нет':
        print('Хорошего дня!')
        break
