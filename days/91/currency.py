import requests


class Currency:

    def __init__(self, amount=0, code='USD'):

        self.amount = float(amount)
        self.code = code

    def convert_to(self, new_code):

        API_URL = 'http://free.currencyconverterapi.com/api/v3/convert?q={}_{}&compact=ultra'.format(
            self.code, new_code)

        response = requests.get(API_URL).json()

        conversion_rate = [v for k, v in response.items()]

        new_value = self.amount * conversion_rate[0]

        return Currency(new_value, new_code)

    def __add__(self, other):
        """For each method it should be able to handle operands of type Currency, float, or int (for example, your __add__ method should be able to handle curr1 + curr2, or handle curr1 + 5, or handle curr1 + 2.71). CLARIFICATION: for addition and subtraction return use self’s currency code."""

        if type(other) == int or type(other) == float:
            new_amount = self.amount + other
        else:
            new_amount = self.amount + other.amount

        return Currency(new_amount, self.code)

    def __sub__(self, other):

        if type(other) == int or type(other) == float:
            new_amount = self.amount - other
        else:
            new_amount = self.amount - other.amount

        return Currency(new_amount, self.code)

        pass

    def __str__(self):
        """Return the amount and type as a string"""

        return "{:.2f} {}".format(self.amount, self.code)

    def __repr__(self):

        pass
