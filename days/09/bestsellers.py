bestsellers_list = []


def read_data(filename):
    """
    The program will input the data set and construct a list of books. If the list of books cannot be constructed, the program will display an appropriate error message and halt.
    """

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().split("\t")
            bestsellers_list.append(line)


def search_by_years():
    """
    Prompt the user for two years (a starting year and an ending year), then display all books which reached the #1 spot between those two years (inclusive). For example, if the user entered “1970” and “1973”, display all books which reached #1 in 1970, 1971, 1972 or 1973.
    """
    pass


def search_by_month_and_year():
    """
    Prompt the user to enter a month and year, then display all books which reached #1 during that month. For example, if the user entered “7” and “1985”, display all books which reached #1 during the month of July in 1985.
    """

    pass


def search_by_author(author_search_string: str):
    """
    Prompt the user for a string, then display all books whose author’s name contains that string (regardless of case). For example, if the user enters “ST”, display all books whose author’s name contains (or matches) the string “ST”, “St”, “sT” or “st”.

    >>> search_by_author('Tolkein')
    Silmarillion, by J. R. R. Tolkein (10/2/1977)
    The Children of the Hurin, by J.R.R. Tolkein (5/6/2007)
    """

    for title, author, publisher, date, genre in bestsellers_list:
        if author_search_string in author:
            print(f'{title.strip()}, by {author.strip()} ({date.strip()})')


def search_by_title(title_search_string: str):
    """
    Prompt the user for a string, then display all books whose title contains that string (regardless of case). For example, if the user enters “secret”, three books are found: “The Secret of Santa Vittoria” by Robert Crichton, “The Secret Pilgrim” by John le Carré, and “Harry Potter and the Chamber of Secrets”.

    >>> search_by_title('Secret')
    Harry Potter and the Chamber of Secrets, by J. K. Rowling (6/20/1999)
    The Secret of Santa Vittoria, by Robert Crichton (11/20/1966)
    The Secret Pilgrim, by John le Carre (1/20/1991)
    """

    # Use str.strip() to remove the whitespace before the string is printed.
    for title, author, publisher, date, genre in bestsellers_list:
        if title_search_string in title:
            print(f'{title.strip()}, by {author.strip()} ({date.strip()})')


if __name__ == "__main__":
    filename = input('Please enter the filename: ' "")
    read_data(filename)

    """
    # Search by Author
    author_search_string = str(input())
    author_search_string = author_search_string.capitalize()
    search_by_author(author_search_string)
    """

    # Search by Title
    title_search_string = str(input())
    title_search_string = title_search_string.capitalize()
    search_by_title(title_search_string)
