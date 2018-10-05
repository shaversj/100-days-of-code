dictOfDocs = {}
documents = {}


def main():
    pass


def parse_file():

    data = open('ap_docs2.txt').read()
    docs = data.split('<NEW DOCUMENT>')
    dictOfDocs = {k: docs[k] for k in range(0, len(docs))}


def search_documents():
    """
    Search for documents that match the search words input by the user.
    """
    pass


def display_document():
    pass
