import textblob


def parse_txt():
    blob = textblob.TextBlob(open("cnn.txt").read())

    # Parse txt by sentence
    for item in blob.sentences:
        print(item)

    # Parse all words
    for word in blob.words:
        print(word)


def sentiment():
    # TextBlob can calculate the "sentiment" of a sentence. "Sentiment" is a measurement of the emotional content of the sentence: the number is positive (between 0 and 1) if the sentence says something "good" and negative (between 0 and -1) if the sentence says something "bad."
    """
    A "CNN Sucks" sticker was also on the van. -0.3
    """

    blob = textblob.TextBlob(open("cnn.txt").read())

    for item in blob.sentences:
        if item.sentiment.polarity < 0:
            print(item, item.sentiment.polarity)
        # print(item.sentiment)


def noun_phrases():
    # A "noun phrase" is a kind of phrase you find in a sentence. It consists of a noun and all of that noun's "surrounding matter," such as any adjectives that modify the noun. TextBlob makes it very easy to extract noun phrases from a given text, using its .noun_phrases attribute:
    """
    Example output:

    dna
    cell phone tower
    auto parts store
    florida
    56-year-old man
    nationwide manhunt
    pipe bombs
    prominent critics
    donald trump
    criminal complaint
    """

    blob = textblob.TextBlob(open("cnn.txt").read())

    for item in blob.noun_phrases:
        print(item)


def part_of_speech():
    # TextBlob can also tell us what part of speech each word in a text corresponds to. It can tell us if a word in a sentence is functioning as a noun, an adjective, a verb, etc. In NLP, associating a word with a part of speech is called "tagging."
    # Part of speech tags: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    """
    Example output:

    A DT
    key JJ
    break NN
    in IN
    the DT
    case NN
    for IN
    investigators NNS
    """

    blob = textblob.TextBlob(
        "A key break in the case for investigators came Thursday, according to a criminal complaint and multiple law enforcement officials, when they traced five packages to the Opa-Locka processing and distribution center outside of Miami.")

    for word, pos in blob.tags:
        print(word, pos)


# parse_txt()
sentiment()
# noun_phrases()
# part_of_speech()
