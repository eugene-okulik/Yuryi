class Flower():
    have_flower = True

    def __init__(self, name, made_in, color, price, life_day, reserve, stem_length):
        self.name = name
        self.made_in = made_in
        self.color = color
        self.price = price
        self.life_day = life_day
        self.reserve = reserve
        self.stem_length = stem_length


class Garden(Flower):

    def __init__(self, name, made_in, color, price, life_day, reserve, stem_length, ships, wild, poison):
        super().__init__(name, made_in, color, price, life_day, reserve, stem_length)
        self.ships = ships
        self.wild = wild
        self.poison = poison

    def print(self):
        if self.ships:
            return (f'Название: {self.name}, Страна: {self.made_in}, Цвет: {self.color}, Цена: {self.price}, '
                    f'Свежесть: {self.life_day}, Длина стебля: {self.stem_length} В букет: {self.reserve}')
        else:
            return (f'Название: {self.name}, Страна: {self.made_in}, Цвет: {self.color}, Цена: {self.price}, '
                    f'Свежесть: {self.life_day}, Длина стебля: {self.stem_length}')


class Bouquet():

    def __init__(self, name_bouquet='Букет', price=0):
        self.name_bouquet = name_bouquet
        self.flowers = []
        self.life_days = 0
        self.price = price

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_price(self):
        return sum(flower.price for flower in self.flowers)

    def avg_life_day(self):
        if len(self.flowers) == 0:
            return 0
        total_life_day = sum(flower.life_day for flower in self.flowers)
        return total_life_day / len(self.flowers)

    def sort_by(self, key, reverse=False):
        self.flowers.sort(key=lambda flower: getattr(flower, key), reverse=reverse)

    def search_by_life_day(self, min_days, max_days):
        result = [flower for flower in self.flowers if min_days <= flower.life_day <= max_days]
        return result

    def search_by_color(self, color):
        result = [flower for flower in self.flowers if flower.color.lower() == color.lower()]
        return result

    def search_by_price_range(self, min_price, max_price):
        result = [flower for flower in self.flowers if min_price <= flower.price <= max_price]
        return result

    def search_by_name(self, name):
        result = [flower for flower in self.flowers if flower.name.lower() == name.lower()]
        return result


garden_roses = Garden('Rose', 'Rus', 'Red', 100, 1, True, 14,
                      False, False, poison=False)
garden_lilia = Garden('Lilia', 'Columbia', 'White', 150, 1, True,
                      20, True, True, poison=True)
garden_Hrisantema = Garden('Hrisantema', 'Iran', 'Yelow', 50, 2, True, 18,
                           False, False, poison=False)

bush_roses = Flower('Bush_Rose', 'Rus', 'pink', 200, 3, True, 15)
romashka = Flower('Romashka', 'Spanish', 'White', 300, 4, True, 13)
franzhepania = Flower('Franzhepania', 'Thailand', 'White', 350, 1, False, 10)
stevia = Flower('Stevia', 'Iran', 'White', 25, 5, False, 12)
cactus = Flower('Cactus', 'Iran', 'Red', 400, 6, False, 9)

bouquet = Bouquet()
bouquet.add_flower(garden_roses)
bouquet.add_flower(bush_roses)
bouquet.add_flower(romashka)

print(f'букет из {len(bouquet.flowers)} цветов')
print(f'Общая стоимость: {bouquet.total_price()}')
print(f'Свежесть: {bouquet.avg_life_day()}')

print(garden_roses.print())
print(garden_lilia.print())
print(garden_Hrisantema.print())
