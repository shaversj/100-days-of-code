import random

""" Code a function that is able to compute the minimum value from an arbitrary set of arguments and an arbitarary set of object data types. The function should accept zero or more arguments, as many as you with to pass. Moreover, the function should work for all kinds of Python object types: numbers, strings, lists, lists of dictionaries, files and even None. """

a = random.sample(range(1000), 60)


def my_minimum(*values):

    return sorted(values)[0]


def min_2(*values):
    # Obtains a value so that it has something to compare to.
    result = values[0]

    for value in values:
        if value < result:
            result = value

    return result


def min_3(**values):
    my_list = list(values.values())
    return sorted(my_list)[0]


d = {"b": 9, "c": 2, "d": 3, "a": 4}
x = [4, 3, 2, 1]

print(a)
print()
print(min_2(*a))
print(my_minimum(*a))
print(min_3(**d))
print(min_2([1, 1], [2, 2], [3, 3], [1, 0]))
print(min_2("dd", "bb", "cc", "aa", "zz", "ee"))

# print(a)
# print()
# print(my_minimum(*d))
# my_minimum(x)
