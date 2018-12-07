import csv
import os
from pathlib import Path

data_folder = Path.cwd() / 'data'


def main():
    get_file_names(data_folder)


def get_file_names(data_folder):

    for file_name in os.listdir(data_folder):
        full_path_to_file = data_folder / file_name
        read_file(full_path_to_file)


def read_file(filename: str):
    with open(filename) as txt_file:
        reader = csv.reader(txt_file)
        for line in reader:
            write_file(line)


def write_file(line: list):
    with open('names.csv', 'a', newline='') as new_file:
        writer = csv.writer(new_file)
        writer.writerow(line)


if __name__ == '__main__':
    main()
