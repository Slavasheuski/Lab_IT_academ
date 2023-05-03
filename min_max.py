def min_max(lst):
    print('Максимальный элемент равен: ', max(lst))
    print('Минимальный элемент равен: ', min(lst))
    rest = list(filter(lambda x: x != max(lst) and x != min(lst), lst))
    print('Остальные элементы: ', *rest)

min_max([1,2,3])

