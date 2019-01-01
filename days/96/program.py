import re
import sqlite3
import requests
from requests_html import HTMLSession

conn = sqlite3.connect('podcast_data.sqlite')
c = conn.cursor()

createTable = """CREATE TABLE podcast(
    podcast INTEGER,
    time TEXT,
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

    # "00:01:45"
    # "1:40"
    timeRegex = re.compile(r'(\d\d:)?\d?\d:\d\d')
    time_match = re.search(timeRegex, line)

    if time_match:
        # print(time_match.group())
        if ': ' in line[5:30]:
            # Jay Miller:
            # Michael:
            time = time_match.group()

            speakerRegex = re.compile(r'[a-zA-z]+\s?[a-zA-z]+?:')
            speaker_match = re.search(speakerRegex, line)

            contentRegex = re.compile(r':\s.+')
            content_match = re.search(contentRegex, line)

            if speaker_match and content_match:
                speaker = speaker_match.group()
                speaker = speaker[0:-1]

                content = content_match.group()
                content = content[2:]

                c.execute("INSERT INTO podcast (podcast, time, speaker, content) VALUES (?, ?, ?, ?)", (
                    podcast, time, speaker, content,))

                conn.commit()

        else:
            time = time_match.group()

            contentRegex = re.compile(r'[a-zA-z].+')
            content_match = re.search(contentRegex, line)

            if content_match:

                content = content_match.group()

                c.execute(
                    "INSERT INTO podcast (podcast, time, content) VALUES (?, ?, ?)", (podcast, time, content,))

                conn.commit()


get_transcript_names()
get_transcripts()
