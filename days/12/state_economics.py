import csv
import time
import string
import operator
# import pylab

data = {}

state_with_max_gdp_in_region_results = []
state_with_min_gdp_in_region_results = []

state_with_max_income_in_region_results = []
state_with_min_income_in_region_results = []


def main():
    open_file()

    search_region = str(input(
        'Specify a region from this list -- far_west,great_lakes,mideast,new_england,plains,rocky_mountain,southeast,southwest: '""))

    search_region = search_region.title()
    print()

    print(f'Data for the {search_region} region:')
    print()

    find_state_with_max_gdp(search_region)
    print(
        f'{str(state_with_max_gdp_in_region_results[0])} has the highest GDP per capita at ${float(state_with_max_gdp_in_region_results[1]):,.2f}')
    print(
        f'{str(state_with_min_gdp_in_region_results[0])} has the lowest GDP per capita at ${float(state_with_min_gdp_in_region_results[1]):,.2f}')
    print()

    find_state_with_max_income(search_region)
    print(
        f'{str(state_with_max_income_in_region_results[0])} has the highest Income per capita at ${float(state_with_max_income_in_region_results[1]):,.2f}')

    print(
        f'{str(state_with_min_income_in_region_results[0])} has the lowest Income per capita at ${float(state_with_min_income_in_region_results[1]):,.2f}')

    print()

    print(f'Data for all states in the {search_region} region:')
    print()
    search_by_region(search_region)


def open_file():
    """
    Your program should prompt the user to enter a valid file name. If the file is not found print an error message and keep prompting until a valid file name is entered. This should be done using try and except. You likely already have this function from a previous project.
    """
    while True:
        file_name = input('Enter the name of a file to open: '"")
        try:
            print('Attempting to read file...')
            time.sleep(3)
            data_file = open(file_name, mode='r')
        except IOError:
            # Raised when an I/O operation (such as a print statement, the built-in open() function or a method of a file object) fails for an I/O-related reason, e.g., “file not found” or “disk full”.
            print('Bad file name. Please try again.')
        else:
            print('Found file!')
            time.sleep(1)
            print('Now processing...')
            csv_reader = csv.reader(data_file)
            parse_file(csv_reader)
            break  # exit loop but the finally block will still complete
        finally:
            try:
                data_file.close()
            except NameError:
                print('Trying again')


def parse_file(csv_reader):
    """
    Prompt the user to select a region to gather data from. You can then read the contents of the file into your data structure. If you use a dictionary, you likely want the state name as the key, and a list of data about the state as the value. If you use a list, you likely want the state name as the first item in the list followed by the remaining data. You will only need states from the selected region in your data structure.
    """

    # Skip Header in CSV
    next(csv_reader, None)

    for line in csv_reader:
        data[line[0]] = {'State': line[0], 'Region': line[1], 'Population (m)': line[2], 'GDP (b)': line[3], 'Income (b)': line[4], 'Subsidies (m)':
                         line[5], 'Compensation (b)': line[5], 'Taxes (b)': line[6], 'GDP per capita': (float(line[3]) * 1000000000) / (float(line[2]) * 1000000), 'Income per capita': (float(line[4]) * 1000000000) / (float(line[2]) * 1000000)}


def search_by_region(search_region):

    # Print header
    print('{:15s} {:14s}    {:7s}    {:10s}   {:13s}    {:16s}   {:9s}     {:14s}     {:17s}'.format(
        'State', 'Population (m)', 'GDP (b)', 'Income (b)', 'Subsidies (m)', 'Compensation (b)', 'Taxes (b)', 'GDP per capita', 'Income per capita'))

    for key, value in data.items():
        if search_region in value['Region']:
            print('{:15s} {:>14,.2f}    {:>7,.2f}    {:>10,.2f}   {:>13,.2f}    {:>16,.2f}   {:>9,.2f}     {:>14,.2f}     {:>17,.2f}'.format(
                value['State'], float(value['Population (m)']), float(value['GDP (b)']), float(value['Income (b)']), float(value['Subsidies (m)']), float(value['Compensation (b)']), float(value['Taxes (b)']), float(value['GDP per capita']), float(value['Income per capita'])))
        # print(value['Region'], value['Population (m)'])


def find_state_with_max_gdp(search_region):

    results = {}

    for key, value in data.items():
        if search_region in value['Region']:
            if key not in results:
                results[key] = value
            else:
                continue

    max_region_gdp_results = max((value['GDP per capita'], key)
                                 for (key, value) in results.items())

    min_region_gdp_results = min((value['GDP per capita'], key)
                                 for (key, value) in results.items())

    state_with_max_gdp_in_region_results.append(max_region_gdp_results[1])
    state_with_max_gdp_in_region_results.append(
        float(max_region_gdp_results[0]))

    state_with_min_gdp_in_region_results.append(min_region_gdp_results[1])
    state_with_min_gdp_in_region_results.append(
        float(min_region_gdp_results[0]))


def find_state_with_max_income(search_region):

    results = {}

    for key, value in data.items():
        if search_region in value['Region']:
            if key not in results:
                results[key] = value
            else:
                continue

    max_region_income_results = max((value['Income per capita'], key)
                                    for (key, value) in results.items())

    min_region_income_results = min((value['Income per capita'], key)
                                    for (key, value) in results.items())

    state_with_max_income_in_region_results.append(
        max_region_income_results[1])
    state_with_max_income_in_region_results.append(
        float(max_region_income_results[0]))

    state_with_min_income_in_region_results.append(
        min_region_income_results[1])
    state_with_min_income_in_region_results.append(
        float(min_region_income_results[0]))


def plot_by_region():
    pass


def plot_gression():
    pass


if __name__ == "__main__":
    main()
