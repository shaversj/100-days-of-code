class Country:
    def __init__(self, name: str, population: int, area: int):
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, name):
        """
        Define a method named is_larger that takes two Country objects and returns True if and only if the first has a larger area than the second.
        """
        return self.area > name.area

    def population_density(self):
        return self.population / self.area

    def __str__(self):
        return f'{self.name} has a population of {self.population} and is {self.area} square km.'

    def __repr__(self):
        return '{self.__class__.__name__}({self.name}, {self.population}, {self.area})'.format(self=self)


def main():
    canada = Country('Canada', 34482779, 9984670)
    usa = Country('United States of America', 313914040, 9826675)
    print(canada.is_larger(usa))
    print(canada.population_density())
    print(usa)
    print(canada.__repr__)


if __name__ == "__main__":
    main()
