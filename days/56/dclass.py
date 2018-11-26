from dataclasses import dataclass
import csv
import sys

data = []


@dataclass
class PopularNames:
    state: str
    sex: str
    year: int
    name: str
    occurance: int


def load_data_from_csv():

    with open('OH.txt') as f:
        #fields = ["State", "Sex", "Year", "Name", "Occurance"]
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            line = (PopularNames(row[0], row[1], row[2], row[3], row[4]))


def getkey(item):
    return item.occurance


def top_male_name():
    s_data = sorted(data, key=getkey, reverse=True)

    for i in s_data:
        if i.year == '2017':
            print(i)


load_data_from_csv()
print(type(data))
print(top_male_name())
