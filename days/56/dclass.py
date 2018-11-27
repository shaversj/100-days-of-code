from dataclasses import dataclass
import csv
from dataclass_csv import DataclassReader

data = []


@dataclass(init=False)
class PopularNames():
    state: str
    sex: str
    year: int
    name: str
    occurance: int


def load_data_from_csv():

    with open('OH.txt') as f:
        # fields = ["State", "Sex", "Year", "Name", "Occurance"]
        reader = csv.DictReader(f, delimiter=',')
        print(reader)
        # for row in reader:
        # line = PopularNames(*row)(int(row[4]))
        # line = row(int)
        # print(type(line.occurance))
        # line = PopularNames(*row)


def getkey(item):
    return item.occurance


def top_male_name():
    s_data = sorted(data, key=getkey, reverse=True)
    for i in s_data:
        if i.year == '2017':
            print(i)


""" with open('OH.txt') as f:
    #reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        # line = PopularNames(*row)
        # names = PopularNames(*reader)
        line = PopularNames(*row)
        print(type(line.occurance)) """

with open('OH_copy.txt') as f:
    #reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    reader = DataclassReader(f, PopularNames)
    for row in reader:
        # line = PopularNames(*row)
        # names = PopularNames(*reader)
        print(row)

# data = load_data_from_csv()
# print(type(data))
# print(top_male_name())
# print(data)

""" x = ['OH', 'F', '1910', 'Mary', 1099]
line = PopularNames(*x)

print(type(line.occurance)) """
