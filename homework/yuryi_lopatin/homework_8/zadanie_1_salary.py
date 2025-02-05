import random
from random import choice

salary = int(input('Enter number'))
random_bonus = choice([True, False])

if random_bonus:
    bonus = random.random
    print(f'{salary}, {random_bonus} - {salary + int(bonus() * 100)}')
else:
    final = salary
    print(f'{salary}, {random_bonus} - {final}')
