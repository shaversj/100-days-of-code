from iss import ISS
from iss import PassTime


test = ISS()

jack = PassTime(lat=40.2987, lon=83.0677)

print()
print(f'There are {test.number} people in space right now!')
print()
print('The following people are in space:')
print(f'{test.people}')
print()
print(f'Longitude: {test.longitude}')
print(f'Latitude: {test.latitude}')
print()
print(f'Timestamp: {test.timestamp}')

print()
print({jack.people})

print(jack.pass_time)
