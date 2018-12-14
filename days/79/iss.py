import requests
from dataclasses import dataclass, field
import time
import json


@dataclass
class ISS():

    api_url: str = 'http://api.open-notify.org/astros.json'
    location_api_url: str = 'http://api.open-notify.org/iss-now.json'

    number: int = field(init=False)
    people: list = field(init=False)
    longitude: float = field(init=False)
    latitude: float = field(init=False)
    timestamp: float = field(init=False)

    def __post_init__(self):
        self.number = ISS.count_people(self)
        self.people = ISS.lookup_names(self)
        self.longitude = ISS.find_longitude(self)
        self.latitude = ISS.find_latitude(self)
        self.timestamp = ISS.timestamp(self)

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

    def find_longitude(self):

        r = requests.get(self.location_api_url)
        response = r.json()

        longitude = response['iss_position'].get('longitude')

        return longitude

    def find_latitude(self):

        r = requests.get(self.location_api_url)
        response = r.json()

        latitude = response['iss_position'].get('latitude')

        return latitude

    def timestamp(self):
        """Convert unix time stamp into a more readable format. """

        r = requests.get(self.location_api_url)
        response = r.json()

        timestamp = response['timestamp']

        timestamp = time.ctime(int(timestamp))

        return timestamp


@dataclass
class PassTime():
    lat: float
    lon: float
    alt: float = None
    num: float = 5
    pass_time: list = None

    #lat = 40.2987
    #lon = 83.0677

    def __post_init__(self):
        self.pass_time = PassTime.getPassTime(self)

    def getPassTime(self):

        data = []
        pass_time_url = 'http://api.open-notify.org/iss-pass.json?lat={lat}&lon={lon}'.format(
            lat=self.lat, lon=self.lon)

        r = requests.get(pass_time_url)
        response = r.json()

        for x in response['response']:
            for k, v in x.items():
                if k == 'risetime':
                    x[k] = time.ctime(int(v))

        for x in response['response']:
            new_dict = {k: v for k, v in x.items()}
            data.append(new_dict)

        return json.dumps(data, indent=2)
