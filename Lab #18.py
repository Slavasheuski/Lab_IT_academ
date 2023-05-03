import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go

url = 'https://job4u.ae/jobs-in-uae/uae/hospital-medical'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='panel panel-default margin-bottom-20')

'''
with open('data.csv', 'w', encoding = 'utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Job vacancy', 'Place','ID', 'Public date', 'url'])

    for n, i in enumerate(items, start=1):
        vacancy = i.find('div', class_ = 'col-md-12 col-sm-12 col-xs-12').text.strip().split('\n')[1]
        place = ''.join(i.find('div', class_ = 'col-md-12 col-sm-12 col-xs-12 small lightened').text.strip().split('|')[1].strip())
        num_id = i.find('span', class_ = 'small lightened').text.strip().split()[-1]
        url = i.find('a', class_ = 'font-size-22 roboto-condensed no-decoration margin-right-5 black')
        href = url.get('href')
        if href:
            url = 'https://job4u.ae' + href
        else:
            url = None

        date_block = i.find('div', class_ = 'col-md-12 col-sm-12 col-xs-12 small lightened').text.strip().split('|')[0].strip()
        params = date_block.strip().split(' ')
        if len(params) == 1:
            time = datetime.strptime(date_block, '%d.%m.%Y')

        elif len(params) == 3:
            tm, hru, t = params
            today = datetime.today()
            time = datetime.today() - timedelta(hours = int(tm))

        if time >= datetime.today() - timedelta(days = 7):
            print(vacancy, place, num_id, time, url)
            writer.writerow([vacancy, place, num_id, time, url])
        else:
            print('Bad vacancy')
            
    num = 2
    #225
    while num <= 225:
        page = 'page=' + str(num)
        url = 'https://job4u.ae/jobs-in-uae/uae/hospital-medical?page=1'
        newUrl = url.replace('page=1', page)
        response = requests.get(newUrl)
        soup = BeautifulSoup(response.text, 'lxml')
        items = soup.find_all('div', class_='panel panel-default margin-bottom-20')
        for n, i in enumerate(items, start=n+1):
            try:
                vacancy = i.find('div', class_ = 'col-md-12 col-sm-12 col-xs-12').text.strip().split('\n')[1]
                place = ''.join(i.find('div', class_ = 'col-md-12 col-sm-12 col-xs-12 small lightened').text.strip().split('|')[1].strip())
                num_id = i.find('span', class_ = 'small lightened').text.strip().split()[-1]
                url = i.find('a', class_ = 'font-size-22 roboto-condensed no-decoration margin-right-5 black')
                href = url.get('href')
                if href:
                    url = 'https://job4u.ae' + href
                else:
                    url = None
 
                date_block = i.find('div', class_ = 'col-md-12 col-sm-12 col-xs-12 small lightened').text.strip().split('|')[0].strip()
                params = date_block.strip().split(' ')
                if len(params) == 1:
                    time = datetime.strptime(date_block, '%d.%m.%Y')
            
                elif len(params) == 3:
                    tm, hru, t = params
                    today = datetime.today()
                    time = datetime.today() - timedelta(hours = int(tm))

                if time >= datetime.today() - timedelta(days = 7):
                    print(vacancy, place, num_id, time, url)
                    writer.writerow([vacancy, place, num_id, time, url])
                else:
                    print('Bad vacancy')

            except:
                print('Parsing is end')
                break
        num += 1
        print(f'Страница с вакансиями №{num}')
'''

df = pd.read_csv('data.csv')
df.sort_values('Job vacancy', ascending=False)

pd.set_option('display.max_rows', None) # Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_colwidth', None)# Сброс ограничений на количество символов в записи

print(df)
'''
fig = px.bar(df, x='Job vacancy', y='Place')
fig.show()
'''
import plotly.express as px

fig = px.bar(df, y='Place', x='Job vacancy', text_auto='.2s',
            title="Default: various text sizes, positions and angles")
fig.show()

