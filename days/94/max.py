import random

S = random.sample(range(1, 100), 10)

print(S)


def find_max(a_list: list):
    """Find the max value in a list by creating a recursive function"""

    if len(a_list) == 1:
        return a_list[0]
    else:
        return max(a_list[0], find_max(a_list[1:]))


print(find_max(S))
