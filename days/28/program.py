import os
import csv
from data_types import Purchase
import statistics


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('---------------------------------')
    print('   Real Estate Data Mining App   ')
    print('---------------------------------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data',
                        'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        purchases = []

        for row in reader:
            # p = Purchase()
            # Creating a static method removes the need to use self and initialize the Class.
            # Representing the data in a class gives you the ability to make it easier to work with the data.
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        # print(purchases[0].__dict__)
        return purchases


def get_price(z):
    return z.price


def query_data(data):

    # if data was sorted by price
    data.sort(key=get_price)
    # most expensive house?
    high_purchase = data[-1]
    print(high_purchase.price)
    # least expensive house?
    low_purchase = data[0]
    print(low_purchase.price)
    # average price house? ...Using 'statistics'.
    prices = []
    for pur in data:
        prices.append(pur.price)

    avg_price = statistics.mean(prices)

    print(int(avg_price))
    # average price of 2 bedroom houses?
    prices = []

    for pur in data:
        if pur.beds == 2:
            prices.append(pur.price)

    avg_two_bedroom_price = statistics.mean(prices)

    print(int(avg_two_bedroom_price))


main()
