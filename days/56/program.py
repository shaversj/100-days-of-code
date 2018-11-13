import csv
import collections
import syllapy

data = []
data_2017 = []
j_names_m = set()

Record = collections.namedtuple(
    'Record', "State, Sex, Year, Name, Occurance")


def main():
    init()

    for i in data:
        if i.Name.startswith('M') and i.Sex == 'F' and i.Year == 2017:
            count = syllapy.count(i.Name)
            if count == 2:
                print(i.Name, count, i.Occurance)


def top_name():
    max_occur = 0
    name = ''
    year = 0

    for i in data:
        if i.Sex == 'F' and i.Year == 2017:
            if max_occur < i.Occurance:
                max_occur = i.Occurance
                name = i.Name
                sex = i.Sex
                year = i.Year
    print(name, sex, year, max_occur)


def init():
    with open('OH.txt') as f:
        fields = ["State", "Sex", "Year", "Name", "Occurance"]
        reader = csv.DictReader(f, fieldnames=fields)
        for row in reader:
            line = parse_row(row)
            data.append(line)


def parse_row(row):
    row['State'] = str(row['State'])
    row['Sex'] = str(row['Sex'])
    row['Year'] = int(row['Year'])
    row['Name'] = str(row['Name'])
    row['Occurance'] = int(row['Occurance'])

    r = Record(**row)

    return r


if __name__ == '__main__':
    main()
