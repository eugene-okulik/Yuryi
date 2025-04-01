import os
from datetime import timedelta
from datetime import datetime
from os.path import split


it_place = os.path.dirname(__file__)
homew_path = os.path.dirname(os.path.dirname(it_place))
eugene_ok_path = os.path.join(homew_path, 'eugene_okulik', 'hw_13', 'data.txt')

with open(eugene_ok_path, 'r', encoding='utf8') as file:
    lines = file.readlines()

date_string1 = lines[0].split(' - ')[0].split('. ')[1]
date_obj1 = datetime.strptime(date_string1, '%Y-%m-%d %H:%M:%S.%f')
print(date_obj1 + timedelta(days=7))

date_string2 = lines[1].split(' - ')[0].split('. ')[1]
date_obj2 = datetime.strptime(date_string2, '%Y-%m-%d %H:%M:%S.%f')
print(date_obj2.strftime("%A"))

date_string3 = lines[2].split(' - ')[0].split('. ')[1]
date_obj3 = datetime.strptime(date_string1, '%Y-%m-%d %H:%M:%S.%f')
days_ago = (datetime.now() - date_obj3)
print(f'C {date_obj3} прошло {days_ago}')
