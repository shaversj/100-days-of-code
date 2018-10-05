import string

dictOfDocs = {}
words = {}
dictOfWords = {}


def main():
    pass


def read_file() -> list:

    # Read the entire txt file as one string
    data = open('ap_docs2.txt').read()

    # Split the string at '<NEW DOCUMENT>'
    docs = data.split('<NEW DOCUMENT>')

    return docs, data


def strip_chars_from_str(data: str):
    """ Clean the data so that you can split the string into individual words. Find a more efficient way to clean the data."""
    data_lower = data.lower()
    data_lower = data_lower.replace('<new document>', "")
    data_lower = data_lower.replace('\n', "")
    data_lower = data_lower.replace('string.punctuation', "")
    data_lower = data_lower.replace('.', "")
    data_lower = data_lower.replace(',', "")


def add_numbers_to_docs(docs: list):

    # Add document numbers to seperated list.
    for k in range(0, len(docs)):
        dictOfDocs[k] = docs[k]


def build_search_set(words: list):
    """
    Create a dictionary that stores single words as the key, and value as the set of documents (numbers) that the word appears in.

    >>> dictOfWords
    {'on': {1, 2, 3} 'the': 1, 2, 3 'bright': 1, 'side': 1, 2 'of': 1, 2 'look': 1, 2 'very': 2, 'there': 3, 'moon': 2, 3}
    """

    for k, v in dictOfDocs.items():
        for word in words:
            if word not in v:
                dictOfWords[word] = k
            else:
                dictOfWords[word] += k
                break


def search_documents():
    """
    Search for documents that match the search words input by the user.
    """
    pass


def display_document():
    pass
