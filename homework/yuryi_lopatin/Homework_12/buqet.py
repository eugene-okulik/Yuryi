class Flowers():
    have_flower = True

    def __init__(self, name_flower, made_in, color, price, life_day, reserve):
        self.name_flower = name_flower
        self.made_in = made_in
        self.color = color
        self.price = price
        self.life_day = life_day
        self.reserve = reserve


class Garden(Flowers):

    def __init__(self, name_flower, made_in, color, price, life_day, reserve, ships, wild, poison):
        super().__init__(name_flower, made_in, color, price, life_day, reserve)
        self.ships = ships
        self.wild = wild
        self.poison = poison

    def print(self):
        if self.ships:
            return (f'Название: {self.name_flower}, Страна: {self.made_in}, Цвет: {self.color}, Цена: {self.price}, '
                    f'Свежесть: {self.life_day}, В букет: {self.reserve}')
        else:
            return (f'Название: {self.name_flower}, Страна: {self.made_in}, Цвет: {self.color}, Цена: {self.price}, '
                    f'Свежесть: {self.life_day}')


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


garden_roses = Garden('Rose', 'Rus', 'Red', 100, 1, True, True,
                      False, False)
garden_lilia = Garden('Lilia', 'Columbia', 'White', 150, 1, False,
                      False, True, True)
garden_hrisantema = Garden('Hrisantema', 'Iran', 'Yelow', 50, 2, True,
                           False, False, False)

bush_roses = Flowers('Bush_Rose', 'Rus', 'pink', 200, 3, True)
romashka = Flowers('Romashka', 'Spanish', 'White', 300, 4, True)
franzhepania = Flowers('Franzhepania', 'Thailand', 'White', 350, 1, False)
stevia = Flowers('Stevia', 'Iran', 'White', 25, 5, False)
cactus = Flowers('Cactus', 'Iran', 'Red', 400, 6, False)

buqet = Buqet()
buqet.add_flower(garden_roses)
buqet.add_flower(bush_roses)
buqet.add_flower(romashka)

print(f'букет из {len(buqet.flowers)} цветов')
print(f'Общая стоимость: {buqet.total_price()}')
print(f'Свежесть: {buqet.avg_life_day()}')

print(garden_roses.print())
print(garden_lilia.print())
print(garden_hrisantema.print())
