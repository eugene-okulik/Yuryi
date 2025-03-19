class Flowers():
    have_flower = True

    def __init__(self, name, made_in, color, price, life_day, reserve, stem_length):
        self.name = name
        self.made_in = made_in
        self.color = color
        self.price = price
        self.life_day = life_day
        self.reserve = reserve
        self.stem_length = stem_length


class Garden(Flowers):

    def __init__(self, name, made_in, color, price, life_day, reserve, stem_length, ships, wild, poison):
        super().__init__(name, made_in, color, price, life_day, reserve, stem_length)
        self.ships = ships
        self.wild = wild
        self.poison = poison

    def print(self):
        if self.ships:
            return (f'Название: {self.name}, Страна: {self.made_in}, Цвет: {self.color}, Цена: {self.price}, '
                    f'Свежесть: {self.life_day}, Длинна стебля: {self.stem_length} В букет: {self.reserve}')
        else:
            return (f'Название: {self.name}, Страна: {self.made_in}, Цвет: {self.color}, Цена: {self.price}, '
                    f'Свежесть: {self.life_day}, Длинна стебля: {self.stem_length}')


class Buqet(Flowers):

    def __init__(self, name_buqet='Букет', price=0):
        self.name_buqet = name_buqet
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

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda flower: flower.life_day, reverse=True)

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price, reverse=True)

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

    def sort_stem_length(self, min_stem_length, max_stem_length):
        result = [flower for flower in self.flowers if min_stem_length <= flower.stem_length <= max_stem_length]
        return result


garden_roses = Garden('Rose', 'Rus', 'Red', 100, 1, True, 14,
                      False, False, poison=False)
garden_lilia = Garden('Lilia', 'Columbia', 'White', 150, 1, True,
                      20, True, True, poison=True)
garden_Hrisantema = Garden('Hrisantema', 'Iran', 'Yelow', 50, 2, True,
                            18, False, False, poison=False)

bush_roses = Flowers('Bush_Rose', 'Rus', 'pink', 200, 3, True, 15)
romashka = Flowers('Romashka', 'Spanish', 'White', 300, 4, True, 13)
franzhepania = Flowers('Franzhepania', 'Thailand', 'White', 350, 1, False, 10)
stevia = Flowers('Stevia', 'Iran', 'White', 25, 5, False, 12)
cactus = Flowers('Cactus', 'Iran', 'Red', 400, 6, False, 9)

buqet = Buqet()
buqet.add_flower(garden_roses)
buqet.add_flower(bush_roses)
buqet.add_flower(romashka)

print(f'букет из {len(buqet.flowers)} цветов')
print(f'Общая стоимость: {buqet.total_price()}')
print(f'Свежесть: {buqet.avg_life_day()}')

print(garden_roses.print())
print(garden_lilia.print())
print(garden_Hrisantema.print())
