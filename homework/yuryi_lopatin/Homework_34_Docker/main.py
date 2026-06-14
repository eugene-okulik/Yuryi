from datetime import datetime
from time import sleep
import requests


while True:
    requests.get('https://google.com')
    print(datetime.now())
    sleep(2)
