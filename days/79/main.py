from iss import ISS

test = ISS()

print()
print(f'There are {test.count_people()} people in space right now!')
print()
print('The following people are in space:')
print(f'{test.lookup_names()}')
print()
