import string


def find_duplicate_char(data: str):
    """
    Write a program to print duplicate characters from a given String, for example if String is "Java" then program should print "a".

    >>> find_duplicate_char('java')
    a
    >>> find_duplicate_char('JJava')
    j
    a
    >>> find_duplicate_char('happy')
    p
    """

    chars = []
    data = data.lower()

    for word in data:
        for c in word:
            if c in chars:
                print(c)
            else:
                chars.append(c)


def is_anagram(str1: str, str2: str):
    """
    A simple coding problem based upon String, but could also be asked with numbers. You need to write a Java program to check if two given strings are anagrams of Each other. Two strings are anagrams if they are written using the same exact letters, ignoring space, punctuation and capitalization. Each letter should have the same count in both strings. For example, Army and Mary are anagram of each other.

    >>> is_anagram('Army', 'Mary')
    True
    """

    str1 = str1.lower()
    str2 = str2.lower()

    str1 = str1.strip(string.punctuation)
    str2 = str2.strip(string.punctuation)

    print(sorted(str1) == sorted(str2))


def first_non_repeated_char(data: str):
    """
    Find the first non-repeated (unique) character in a given string. For example if given String is "Morning" then it should print "M".

    >>> first_non_repeated_char(geeksforgeeks)
    f
    >>> first_non_repeated_char(Morning)
    M
    """

    char_order = []
    chars = {}
    i = 1

    for word in data:
        for c in word:
            if c in chars:
                chars[c] = i + 1
            else:
                chars[c] = 1
                char_order.append(c)

    for c in char_order:
        if chars[c] == 1:
            return(c)
