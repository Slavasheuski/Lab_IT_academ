from math import*

def circle_area(r):
    return pi * pow(r, 2)


def ball_volume(r):
    return (4 / 3) * pi * pow(r, 3)

r_circle = int(input('Введите радиус круга(см): '))
r_ball = int(input('Введите радиус шара(см): '))

print(str(circle_area(r_circle)) + ' см2')
print(str(ball_volume(r_ball)) + ' см3')

circle_area_2 = lambda r: pi * pow(r, 2)
ball_volume_2 = lambda r: (4 / 3) * pi * pow(r, 3)

print(str(round(circle_area_2(r_circle), 2)) + ' см2')
print(str(round(ball_volume_2(r_ball), 2)) + ' см3')

