import csv
import collections

data = []

Record = collections.namedtuple(
    'Record', "State, Sex, Year, Name, Occurance")


def main():
    init()

    top_10(2015, 'M')


def top_10(year, sex):

    # new_data = return_by_year_sex(2017, 'M')
    new_data = return_by_year_sex(year, sex)

    top_10 = [(k, name[3])
              for (k, name) in enumerate(new_data[:10], 1)]

    for item in top_10:
        print(*item)


def return_by_year_sex(year, sex):

    by_year = [lines for lines in data if lines.Year ==
               year and lines.Sex == sex]

    return by_year


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
