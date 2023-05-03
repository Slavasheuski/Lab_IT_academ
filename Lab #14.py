import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv


url = 'https://cars.av.by/filter?year[min]=2018&year[max]=2020&seller_type[0]=1&page=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='listing-item listing-item--color listing-item--top')

with open('data.csv', 'w', encoding = 'utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Марка', 'Модель','Цена, BYN', 'Год'])

    for n, i in enumerate(items, start=1):
        itemModel = ' '.join(i.find('span', class_ = 'link-text').text.strip().split(' ')[1:])
        itemMarka = i.find('span', class_ = 'link-text').text.strip().split(' ')[0]
        itemPrice = int(''.join(i.find('div', class_ = 'listing-item__price').text.strip().split())[:-2])
        itemYear = int(i.find('div', class_ = 'listing-item__params').text.strip()[:4])
        writer.writerow([itemMarka, itemModel, itemPrice, itemYear])

    num = 2
    while num < 10:
        try:
            page = 'page=' + str(num)
            newUrl = url.replace('page=1', page)
            response = requests.get(newUrl)
            soup = BeautifulSoup(response.text, 'lxml')
            items = soup.find_all('div', class_='listing-item listing-item--color listing-item--top')
            for n, i in enumerate(items, start=n+1):
                itemModel = ' '.join(i.find('span', class_ = 'link-text').text.strip().split(' ')[1:])
                itemMarka = i.find('span', class_ = 'link-text').text.strip().split(' ')[0]
                itemPrice = int(''.join(i.find('div', class_ = 'listing-item__price').text.strip().split())[:-2])
                itemYear = int(i.find('div', class_ = 'listing-item__params').text.strip()[:4])
                writer.writerow([itemMarka, itemModel, itemPrice, itemYear])
            num += 1
        except:
            break

df = pd.read_csv('data.csv')
df.sort_values('Цена, BYN', ascending=False)

pd.set_option('display.max_rows', None) # Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_colwidth', None)# Сброс ограничений на количество символов в записи
pd.set_option('display.max_rowwidth', None)

print(df)

