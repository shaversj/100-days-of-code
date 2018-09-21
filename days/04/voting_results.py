import os
import csv
from collections import Counter


def main():
    """Election Results
    -------------------------
    Total Votes: 620100
    -------------------------
    Rogers: 36.0% (223236)
    Gomez: 54.0% (334854)
    Brentwood: 4.0% (24804)
    Higgins: 6.0% (37206)
    -------------------------
    Winner: Gomez
    -------------------------
    """
    pass


votes = []


def read_data():
    """
    Process the polling data and add it to a data structure
    """
    base_folder = os.path.dirname(__file__)
    filename1 = os.path.join(base_folder, 'data', 'election_data_1.csv')
    filename2 = os.path.join(base_folder, 'data', 'election_data_2.csv')

    # Read first file
    with open(filename1, 'r', encoding='utf-8') as f1:
        reader1 = csv.DictReader(f1)

        for line in reader1:
            votes.append(line.get('Candidate'))

    # Read second file
    with open(filename2, 'r', encoding='utf-8') as f2:
        reader2 = csv.DictReader(f2)

        for line in reader2:
            votes.append(line.get('Candidate'))


def most_common():
    data = Counter(votes)
    return(max(data, key=data.get))


def count_data():
    """Count the number of votes for each candidate.
    """

    total = len(votes)

    count_khan = 0
    count_correy = 0
    count_li = 0
    count_vestal = 0
    count_torres = 0
    count_otooley = 0
    count_seth = 0
    count_cordin = 0

    for name in votes:
        if name == 'Khan':
            count_khan += 1
        elif name == 'Correy':
            count_correy += 1
        elif name == 'Li':
            count_li += 1
        elif name == 'Vestal':
            count_vestal += 1
        elif name == 'Torres':
            count_torres += 1
        elif name == "O'Tooley":
            count_otooley += 1
        elif name == 'Seth':
            count_seth += 1
        elif name == 'Cordin':
            count_cordin += 1
        else:
            break

    print('---------------------------------------')
    print('-----------Election Results------------')
    print('---------------------------------------')
    print(f'Total Votes:     {total}')
    print('---------------------------------------')
    print(
        f'Khan:     {round(int(count_khan) / int(total) * 100.0)}%    {(count_khan)}')
    print(
        f'Correy:   {round(int(count_correy) / int(total) * 100.0)}%    {(count_correy)}')
    print(
        f'Li:       {round(int(count_li) / int(total) * 100.0)}%    {(count_li)}')
    print(
        f'Vestal:   {round(int(count_vestal) / int(total) * 100.0)}%     {(count_vestal)}')
    print(
        f'Torres:   {round(int(count_torres) / int(total) * 100.0)}%     {(count_torres)}')
    print(
        f'OTooley:  {round(int(count_otooley) / int(total) * 100.0)}%     {(count_otooley)}')
    print(
        f'Seth:     {round(int(count_seth) / int(total) * 100.0)}%     {(count_seth)}')
    print(
        f'Cordin:   {round(int(count_cordin) / int(total) * 100.0)}%     {(count_cordin)}')
    print('---------------------------------------')
    print(f'Winner: {most_common()}')
    print('---------------------------------------')


read_data()
count_data()
