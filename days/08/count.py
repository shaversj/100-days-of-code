import string
from collections import Counter


def remove_punctuation(data: str) -> str:
    """Removes all punctuation from the string.
    """
    for c in string.punctuation:
        data = data.replace(c, "")
    return(data)


def count_words_len(data: str):
    """Count number of words in a string using length.

    >>> count_words_len('Columbus is a great place to live.')
    7
    >>> count_words_len('I love Python.')
    3
    >>> count_words_len('Did you ever think you would sell your house?')
    9
    """

    data = remove_punctuation(data)
    data = data.lower()

    # Split the str by whitespace.
    data = data.split()

    return(len(data))


def count_words(data: str):
    """Count number of words in a string using a for loop.

    >>> count_words('Columbus is a great place to live.')
    7
    >>> count_words('I love Python.')
    3
    >>> count_words('Did you ever think you would sell your house?')
    9
    """

    data = remove_punctuation(data)
    data = data.lower()

    # Split the str by whitespace.
    data = data.split()

    word_count = 0
    for word in data:
        word_count += 1

    return((word_count))


def print_summary(data: str) -> str:
    """Counts the number of individual words in a string and prints a summary of how many times each word is mentioned in the string.

    >>> print_summary('Columbus is a great place to live.')
    columbus 1
    is 1
    a 1
    great 1
    place 1
    to 1
    live 1
    >>> print_summary('I love Python. Do you love Python?')
    i 1
    love 2
    python 2
    do 1
    you 1
    >>> print_summary('Did you ever think you would sell your house?')
    did 1
    you 2
    ever 1
    think 1
    would 1
    sell 1
    your 1
    house 1
    """

    data = remove_punctuation(data)
    data = data.lower()

    # Split the str by whitespace.
    data = (Counter(data.split()))

    for word, count in data.items():
        print(word, count)


if __name__ == "__main__":
    data = input('Input a string for the function to count:')
    print(
        f'Your string has a total of {count_words(data)} words!')
    print_summary(data)
    # print(count_words_len(data))
