import requests
from dataclasses import dataclass


@dataclass
class Space:

    base_url: str = 'http://api.open-notify.org/'


@dataclass
class People():

    api_url: str = 'http://api.open-notify.org/astros.json'

    def number_of_people_in_space(self):
        """Returns the current number of people in space. """

        r = requests.get(self.api_url)
        response = r.json()

        total_number_in_space = response['number']

        return total_number_in_space

    def who_is_in_space():
        """Returns the names of the people in space. """
        pass


class Location():
    pass


class Pass_Time():
    pass
