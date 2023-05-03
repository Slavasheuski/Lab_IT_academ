from math import*

result_circle = {}
result_ball = {}

while True:
    r_circle = int(input('Введите радиус круга(см): '))
    result_circle[r_circle] = result_circle.get(r_circle, 0) + 1

    r_ball = int(input('Введите радиус шара(см): '))
    result_ball[r_ball] = result_ball.get(r_ball, 0) + 1
    
    question = input('Ещё размеры есть?(да/нет)').lower()

    if question == 'нет':
        break
print()
    
for num in result_circle:
    print('Для значения радиуса ' + str(num) + 'см площадь круга равна ' + str(pi * pow(num, 2)) + ' см2')
    print()

for num_1 in result_ball:
    print('Для значения радиуса ' + str(num_1) + 'см объем шара равен ' + str((4 / 3) * pi * pow(num_1, 3)) + ' см3')
    print()
