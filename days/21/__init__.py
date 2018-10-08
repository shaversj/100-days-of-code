import config


class Tour:
    def __init__(self, origin, *destination):
        self.origin = origin
        self.destination = destination

    def __str__(self):
        """
        Returns the cities and states associated with the tour.

        >>> Tour('New York, NY', 'Lansing, MI', 'Sacramento, CA')
        >>> print(t1)
        New York, NY; Lansing, MI; Sacramento, CA
        """
        return self.origin + '; ' + '; '.join(i for i in self.destination)

    def distance(self):
        pass

    def __add__(self):
        pass

    def __eq__(self):
        pass


t1 = Tour('New York, NY', 'Lansing, MI', 'Sacramento, CA')
t2 = Tour('New York, NY', 'Sacramento, CA')

print(t2)
