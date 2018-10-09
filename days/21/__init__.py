import config


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

    def distance(self):
        pass

    def __add__(self):
        pass

    def __eq__(self):
        pass


#t1 = Tour('New York, NY', 'Lansing, MI', 'Sacramento, CA')
#t2 = Tour('New York, NY', 'Sacramento, CA')
