import requests
import tabulate

space_url = 'http://api.open-notify.org/astros.json'
response = requests.get(space_url)
r = response.json()

print()
print(f'There are {r["number"]} people in space right now!')
print()
print(tabulate.tabulate(r['people'], headers='keys'))
print()
