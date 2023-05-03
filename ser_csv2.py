import csv

filename = "20_02_23_b_data.csv"
# список покупок: вес и стоимость
shoplist = {"яблоки": [3, 5], "банана": [1, 5.6], "сметана": [1, 2.5], "арахис": [0.5, 5], "хлеб": [1, 1.8], "батон": [1, 1.5], "свекла": [1.5, 5], "чипсы": [3, 7.9], "cola": [1, 2.5], "сок": [3, 12.76], "печенье": [2, 8.45], "молоко": [1, 2.5]}

# Запись в файл
with open(filename, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "weight", "price"], quoting=csv.QUOTE_ALL)
    writer.writeheader()  # Записывает заголовки в файл
    for name, values in sorted(shoplist.items()):
        writer.writerow(dict(name=name, weight=values[0], price=values[1]))

# формите чтение из файла
with open(filename, 'r', encoding='utf-8') as f:
    text = csv.reader(f)
    for i in text:
        print(i)
