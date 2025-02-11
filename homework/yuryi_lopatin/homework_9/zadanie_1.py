import datetime
from time import strptime


my_time = 'Jan 15, 2023 - 12:05:33'

python_date = datetime.datetime.strptime(my_time, '%b %d, %Y - %H:%M:%S')
print(python_date)

human_date = python_date.strftime('month: %B')
print(human_date)
format_day = python_date.strftime('%d.%m.%Y, %H:%M')
print(format_day)
