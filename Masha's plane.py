class PlaneEconom:
    def __init__(self, price, ranges, baggage, insurance_price, food):
        self.price = price
        self.ranges = ranges
        self.baggage = baggage
        self.insurance_price = insurance_price
        self.food = food

    def __str__(self):
        return f"Полёт за {self.price}$!"

    def food(self):
        print('В стоимость билета входит {self.food}')

    def info(self):
        print()
        print('За данную цену получите следующие условия полёта:')
        print()
        print(f'Дальность полёта составляет: {self.ranges}м, в стоимость билета входит {self.baggage} и {self.food}, а также страховка на сумму {self.insurance_price}$!')


class PlaneStandart(PlaneEconom):
    def __init__(self, price, ranges, baggage, insurance_price, food, movie):
        super().__init__(price, ranges, baggage, insurance_price, food)
        self.movie = movie

    def movies(self):
        print(f'С экранов планшетов, встроенных в подголовники, вам будут доступны следующие фильмы: {self.movie}!')

    def info(self):
        super().info()
        self.movies()

class PlaneBusinnes(PlaneStandart):
    def __init__(self, price, ranges, baggage, insurance_price, food, movie, drink, music):
        super().__init__(price, ranges, baggage, insurance_price, food, movie)
        self.drink = drink
        self.music = music

    def musics(self):
        print(f'Вашему вниманию живое выступление музыкантов {self.music}!')

    def drinks(self):
        print(f'В баре доступны следующие алкогольные напитки: {self.drink}!')

    def info(self):
        super().info()
        self.drinks()
        self.musics()


result = [PlaneEconom(1850, 10000, 'сумка', 1000, 'завтрак'),
          PlaneStandart(2750, 10000, 'чемодан', 2000, 'завтрак', 'Титаник'),
          PlaneBusinnes(5000, 10000, 'сумка и два чемодана', 10000, 'завтрак, обед и ужин', 'Титаник, Жизнь зла, Мальчишник в вегасе', 'пиво, тоник, текила', 'Madonna, Linkin Park, Beyonce')]

def printHead(s):
      print("=" * 79)
      print(s)
      print("=" * 79)

# Выводит содержимое трюма в виде таблицы
def printList():
      printHead("Добро пожаловать на борт A380!")
      for i in range(len(result)):
            print(f"{(i + 1)}. {result[i]} ({3 - i}-й класс)")

playGame = True
while playGame:
        print("\n")        # Выводим пустую строку, чтобы красиво
        printList()       # Выводим все товары в виде таблицы
        print()
        
        n = int(input("Меня зовут Мария, чем могу помочь?\nВведите, пожалуйста, номер товара, который интересует (0 - выход): "))
        if n == 0:
            playGame = False
        elif n > 0 and n <= len(result):
            result[n - 1].info()
print("Успешного полёта!")
