from dataclasses import dataclass
import csv

data = []


@dataclass
class EPA:
    model: str
    hwy_mpg: float


with open('all_alpha_19.txt', 'r') as f:
    reader = csv.reader(f, dialect="excel-tab")
    # Skip Header
    next(reader, None)
    for line in reader:
        model = line[0]
        hwy_mpg = line[13]
        if '/' in hwy_mpg:
            # Some values contain '25/58' so I will need to split.
            hwy_mpg = line[13].split('/')
            hwy_mpg = hwy_mpg[0]
            data.append(EPA(model, int(hwy_mpg)))

        hwy_e = None
        data.append(EPA(model, int(hwy_mpg)))


def top_5_models(max_mpg: int):

    return {x.model for x in data if x.hwy_mpg == max_mpg}


def find_max_mpg():

    return(sorted_data[0].hwy_mpg)


def find_min_mpg():

    return(sorted_data[-1].hwy_mpg)


sorted_data = sorted(data, key=lambda x: x.hwy_mpg, reverse=True)

# print('\n'.join(top_5_models()))
max_mpg = find_max_mpg()
min_mpg = find_min_mpg()
print(top_5_models(max_mpg))
print(find_max_mpg())

print()
print(find_min_mpg())
