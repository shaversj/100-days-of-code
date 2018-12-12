import requests
from dataclasses import dataclass


@dataclass
class ISS():

    api_url: str = 'http://api.open-notify.org/astros.json'

    def count_people(self):
        """Returns the current number of people in space. """

        r = requests.get(self.api_url)
        response = r.json()

        total_number_in_space = response['number']

        return total_number_in_space

    def lookup_names(self):
        """Returns the names of the people in space. """

        r = requests.get(self.api_url)
        response = r.json()

        list_of_people = [item.get('name') for item in response['people']]

        return '\n'.join(list_of_people)


class Location():
    pass


class Pass_Time():
    pass
