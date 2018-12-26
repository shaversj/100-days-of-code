import csv

data = []
ROE_DATA = {}

with open('SBUX.csv') as f:
    reader = csv.DictReader(f)
    for line in reader:
        data.append(line)


YEAR = 2003

while YEAR != 2009:

    ASE_YEAR = int(YEAR) - 1

    YEAR = str(YEAR)

    try:

        ASE = (float(data[6][str(ASE_YEAR)]) + float(data[6][YEAR]))//2

    except KeyError:

        ASE = float(data[6][YEAR])

        ROE = (float(data[3][YEAR])/float(data[1][YEAR])) * (float(data[1][YEAR]) /
                                                             float(data[5][YEAR])) * (float(data[5][YEAR])/ASE)

        ROE_DATA[YEAR] = ROE

        YEAR = int(YEAR)
        YEAR += 1

    else:

        ROE = (float(data[3][YEAR])/float(data[1][YEAR])) * (float(data[1][YEAR]) /
                                                             float(data[5][YEAR])) * (float(data[5][YEAR])/ASE)

        ROE_DATA[YEAR] = ROE

        YEAR = int(YEAR)
        YEAR += 1

for k, v in ROE_DATA.items():
    print("{} {:.2f}%".format(k, v * 100))
