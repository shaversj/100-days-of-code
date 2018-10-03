import requests
import json


ZIP_CODE = input("Enter a valid zipcode ")

print()
print('-------------------')
print()

API_URL = 'http://api.openweathermap.org/data/2.5/weather'
PARAMS = {'zip': ZIP_CODE, 'units': 'imperial',
          'APPID': ''}

r = requests.get(API_URL, params=PARAMS)

print()
print('--------------------')
print()

data = json.loads(r.text)

print(f'The temperature in {data["name"]} is {data["main"]["temp"]} degrees')
