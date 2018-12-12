from iss import ISS

test = ISS()

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
