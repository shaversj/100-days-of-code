import os
import csv
from collections import Counter

votes = []


def main():

    read_data()
    counter_results()
    # count_and_print_results()
    # count_and_print_results() uses more code to return the the same results as counter_results().


def read_data():
    """
    Process the polling data and add it to a data structure
    """
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'election_data_1.csv')

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for line in reader:
            votes.append(line.get('Candidate'))


def calculate_winner():
    data = Counter(votes)
    return (max(data, key=data.get))


def counter_results():
    """
    Use Counter to calculate the total votes and store the values in a dictionary.

    A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values.

    You can access the elements the same way you would another dictionary.
    """

    data = Counter(votes)
    total = len(votes)

    print('---------------------------------------')
    print('-----------Election Results------------')
    print('---------------------------------------')
    print(f'Total Votes:      {total}')
    print('---------------------------------------')
    for k, v in data.items():
        print(f'{k}:    {round(int(v) / int(total) * 100.0)}%    {v}')
    print('---------------------------------------')
    print(f'Winner: {calculate_winner()}')
    print('---------------------------------------')


def count_and_print_results():
    """Count the number of votes for each candidate.

    >>>>
    Total Votes:      803000
    ---------------------------------------
    Vestal:   48%     385440
    Torres:   44%     353320
    Seth:     5%      40150
    Cordin:   3%      24090
    ---------------------------------------
    Winner: Vestal
    ---------------------------------------

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
    print(f'Total Votes:      {total}')
    print('---------------------------------------')
    print(
        f'Vestal:   {round(int(count_vestal) / int(total) * 100.0)}%     {(count_vestal)}')
    print(
        f'Torres:   {round(int(count_torres) / int(total) * 100.0)}%     {(count_torres)}')
    print(
        f'Seth:     {round(int(count_seth) / int(total) * 100.0)}%      {(count_seth)}')
    print(
        f'Cordin:   {round(int(count_cordin) / int(total) * 100.0)}%      {(count_cordin)}')
    print('---------------------------------------')
    print(f'Winner: {calculate_winner()}')
    print('---------------------------------------')


if __name__ == "__main__":
    main()
