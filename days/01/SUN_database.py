from collections import Counter
import pprint


def count_images_by_category(input_file):
    """ (file open for reading) -> str, int

    Read the file and return the number of images in each category. The list will be sorted by the category with the most images.

    >>> count_images_by_category(input_file)
    abbey           33
    airplane_cabin  11
    airport_terminal 22
    alley           13
    athletic_field  45

    """
    category = []

    for line in input_file:
        line = line.rsplit('/')
        category.append(line[2])

    return category


if __name__ == '__main__':
    with open('Training_01.txt', "r") as input_file:
        answer = count_images_by_category(input_file)
        pprint.pprint(Counter(answer))
