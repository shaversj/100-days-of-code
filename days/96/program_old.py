import sqlite3
import unicodedata
import requests
from requests_html import HTMLSession

conn = sqlite3.connect('podcast_data.sqlite')
c = conn.cursor()

createTable = """CREATE TABLE podcast(
    podcast INTEGER,
    timestamp TEXT,
    speaker TEXT,
    content TEXT
);"""


c.execute(createTable)


transcript_names = []


def get_transcript_names():

    session = HTMLSession()

    r = session.get(
        'https://github.com/mikeckennedy/talk-python-transcripts/tree/master/transcripts')

    page_links = r.html.absolute_links

    for x in page_links:
        if '.txt' in x:
            transcript_names.append(x[-7:])

    transcript_names.sort()


def get_transcripts():
    for x in transcript_names:

        podcast = x[0:-4]

        url = 'https://raw.githubusercontent.com/mikeckennedy/talk-python-transcripts/master/transcripts/{}'.format(
            x)

        response = requests.get(url, stream=True)

        for line in response.iter_lines(decode_unicode=True):
            insert_into_database(podcast, line)


def insert_into_database(podcast, line):

    if line[:1].isdigit() and ': ' in line[:20]:

        try:
            # Remove \xa0 non-breaking spaces from line
            line = unicodedata.normalize('NFKD', line)
            line = line.split(" ", 2)
            timestamp = line[0]
            speaker = line[1][0:-1]  # Remove colon from name
            content = line[2]
            c.execute(
                "INSERT INTO podcast (podcast, timestamp, speaker, content) VALUES (?, ?, ?, ?)", (podcast, timestamp, speaker, content,))

            conn.commit()

        except IndexError as e:
            print(e, line)

    elif line[:1].isdigit():
        try:
            line = unicodedata.normalize('NFKD', line)
            line = line.strip().split(" ", 1)

            timestamp = line[0]
            content = line[1]

            c.execute(
                "INSERT INTO podcast (podcast, timestamp, content) VALUES (?, ?, ?)", (podcast, timestamp, content,))

            conn.commit()

        except IndexError as e:
            print(e, line)


get_transcript_names()
get_transcripts()
