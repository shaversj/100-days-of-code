import config
import requests


class Tour:
    def __init__(self, origin, *destination):
        self.origin = origin
        self.destination = destination

    def __str__(self):
        """
        Returns the cities and states associated with the tour.
        __str__ ==> easy to read representation of your class (human consumption)

        >>> Tour('New York, NY', 'Lansing, MI', 'Sacramento, CA')
        >>> print(t1)
        New York, NY; Lansing, MI; Sacramento, CA
        """
        return self.origin + '; ' + '; '.join(i for i in self.destination)

    def __repr__(self):
        """
        __repr__ ==> unambiguous and meant for developers.

        >>> Tour('New York, NY', 'Lansing, MI', 'Sacramento, CA')
        >>> print(repr(t1))
        Tour(New York, NY, ('Lansing, MI', 'Sacramento, CA'))
        """

        return '{self.__class__.__name__}({self.origin}, {self.destination})'.format(self=self)

    def distance(self, *mode: str):
        """
        This method takes a single (optional) argument indicating a mode – one of the strings ‘driving’ (default), ‘bicycling’, or ‘walking’. It returns the total distance (in meters) covered by the tour for the indicated mode. This method is where you will use urllib functions to get data from the web to find the distances between consecutive locations in the tour and calculate the total distance. If a response does not contain a distance value, the method should raise a ValueError exception.

        """
        formatted_destination = ("|".join(self.destination))
        #mode = mode

        api_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=' + \
            self.origin + '&destinations=' + formatted_destination + \
            '&' + 'mode=' + str(mode) + '&' + 'key=' + config.api_key

        r = requests.get(api_url)

        response = r.json()

        tour_mileage = response["rows"][0]["elements"][1]["distance"]["text"]

        return tour_mileage

    def destinations(self):
        return("|".join(self.destination))

    def __add__(self):
        pass

    def __eq__(self):
        pass


# t1 = Tour('New York, NY', 'Lansing, MI', 'Sacramento, CA')
# t2 = Tour('New York, NY', 'Sacramento, CA')
