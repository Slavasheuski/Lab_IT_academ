import pandas as pd
import random

df = pd.DataFrame({'Занятие':[i for i in range(1, 28)] + ['Total']})
students = ['Маша','Влад','Алексей','Саша','Сергей','Мухаммед']

for student in students:
    grades = [random.randint(7,10) for _ in range(1, 28)]
    df[student] = grades + [sum(grades)]

print(df)
