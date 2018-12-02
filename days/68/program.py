from dataclasses import dataclass
from dataclass_csv import DataclassReader
#import ipdb

data = []


@dataclass(init=True)
class PopularNames:
    state: str
    sex: str
    year: int
    name: str
    occurance: int


# ipdb.set_trace()
with open('OH.TXT') as f:
    #fieldnames = 'state', 'sex', 'year', 'name', 'occurance'
    #reader = DataclassReader(f, PopularNames, fieldnames=fieldnames)
    reader = DataclassReader(f, PopularNames)
    for row in reader:
        data.append(row)


def top_20_names(year: int, sex: str):

    top_10_list = sorted(data, key=lambda x: x.occurance, reverse=True)
    count = 0
    for row in top_10_list:
        if row.year == year and row.sex == sex:
            if count == 20:
                break
            print(row.name, row.sex, row.occurance)
            count += 1


top_20_names(2017, 'M')

# Testing for Dash Dashboard. Plan on using the data below for a dashboard
""" years = {year.year for year in data}
print(years) """
