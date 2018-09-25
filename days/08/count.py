import doctest
from collections import Counter
import pprint


def count_words(data: str) -> str:
    """Count Words in a String - Counts the number of individual words in a string.

    >>> count_words('Columbus is a great place to live.')
    7
    >>> count_words('I love Python.')
    3
    >>> count_word('Did you ever think you would sell your house?')
    9
    """

    # Split the str by whitespace.
    data = data.split()

    word_count = 0
    for word in data:
        word_count += 1

    return((word_count))


def print_summary(data: str) -> str:
    """Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.

    >>> count_words('Columbus is a great place to live.')
    Columbus 1
    is 1
    a 1
    great 1
    place 1
    to 1
    live 1
    >>> count_words('I love Python.')
    I 1
    Love 1
    Python 1
    >>> count_word('Did you ever think you would sell your house?')
    Did 1
    you 1
    ever 1
    think 1
    you 1
    would 1
    sell 1
    your 1
    house? 1
    """

    # Split the str by whitespace.
    data = (Counter(data.split()))

    print(data)


if __name__ == "__main__":
    nl = '\n'
    print(
        'Input a string and the function will return the total number of words and a summary of the number of characters')
    data = input("")
    print(f'Your string has {count_words(data)} total words.')
    print(print_summary(data))
