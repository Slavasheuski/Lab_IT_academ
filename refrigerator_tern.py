def refrigerator(X, Y, H, A, B):
    return 'Холодильник проходит в дверной проём! Поздравляем!' if H < B and (X < A or Y < A) else 'Упс.. Не пройдёт! Выберите другой холодильник'
    

print(refrigerator(10, 10, 10, 10, 10))
