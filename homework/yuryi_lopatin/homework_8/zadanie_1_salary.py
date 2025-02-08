import random
from random import choice

salary = int(input('Enter number'))
random_bonus = choice([True, False])

if random_bonus:
    print(f'{salary}, {random_bonus} - {salary + int(random_bonus * 100)}')
else:
    print(f'{salary}, {random_bonus} - {salary}')
