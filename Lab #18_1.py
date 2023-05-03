import requests
from bs4 import BeautifulSoup

import datetime
from collections import namedtuple

InnerBlock = namedtuple('Block', 'marka,model,price,year,url')

class Block(InnerBlock):

    def __str__(self):
        return f'{self.vacancy}\t\t{self.place}\t\t{self.num_id}\t\t{self.url}'


class Parser:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }

    def get_page(self, page = None):
        
        if page and page > 1:
            params['page'] = page

        url = 'https://job4u.ae/jobs-in-uae/uae/hospital-medical'
        r = self.session.get(url)
        return r.text

    @staticmethod
    def parse_date(item):
        params = item.strip().split(' ')
        print(params)
        
        if len(params) == 2:
            day, time = params
            if day == 'Сегодня':
                date = datetime.date.today()
            elif day == 'Вчера':
                date = datetime.date.today() - datetime.timedelta(days=1)
            else:
                print('Не смогли разобрать месяц:', item)
                return
            
            time = datetime.datetime.strptime(time, '%H:%M').time()
            return datetime.datetime.combine(date=date, time=time)

        elif len(params) == 3:
            day, month_hru, time = params
            day = int(day)
            months_map = {
                'января': 1,
                'февраля': 2,
                'марта': 3,
                'апреля': 4,
                'мая': 5,
                'июня': 6,
                'июля': 7,
                'августа': 8,
                'сентября': 9,
                'октября': 10,
                'ноября': 11,
                'декабря': 12,
            }
            month = months_map.get(month_hru)
            if not month:
                print('Не смогли разобрать месяц:', item)
                return

            today = datetime.datetime.today()
            time = datetime.datetime.strptime(time, '%H:%M')
            return datetime.datetime.combine(day=day, month = month, year = year, hour = time.hour, minute=time.minute)

        else:
            print('Не смогли разобрать формат:', item)
            return

    def parse_block(self, item):
        url_block = item.select_one('a.font-size-22 roboto-condensed no-decoration margin-right-5 black ')
        print(url_block)
        return
        href = url_block.get('href')
        if href:
            url = 'https://job4u.ae' + href
        else:
            url = None

        model = ' '.join(item.find('span', class_ = 'link-text').text.strip().split(' ')[1:])
        marka = item.find('span', class_ = 'link-text').text.strip().split(' ')[0]
        price = int(''.join(item.find('div', class_ = 'listing-item__price').text.strip().split())[:-2])
        year = int(item.find('div', class_ = 'listing-item__params').text.strip()[:4])
        
        # Выбрать блок с датой размещения объявления
        date = None
        date_block = item.find('div', class_ = 'listing-item__date')
        absolute_date = date_block.get('data-absolute-date')
        if absolute_date:
            date = self.parse_date(item = absolute_date)


        return Block(
            marka = marka,
            model = model,
            price = price,
            year = year,
            url = url
        )
        
    def get_blocks(self, page=None):
        text = self.get_page(page=page)
        soup = BeautifulSoup(text, 'lxml')
        
        container = soup.find_all('div', class_='panel panel-default margin-bottom-20')
        for item in container:
            block = self.parse_block(item = item)
            print(block)

    def parse_all(self):
        limit = 10
        for i in range(1, limit + 1):
            self.get_blocks(page = i)

def main():
    p = Parser()
    p.get_blocks()

if __name__ == '__main__':
    main()

