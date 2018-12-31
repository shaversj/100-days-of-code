""" from selenium import webdriver
browser = webdriver.Safari()
browser.get('') """

from requests_html import HTMLSession
import requests

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

        podcast_number = x[0:-4]

        url = 'https://raw.githubusercontent.com/mikeckennedy/talk-python-transcripts/master/transcripts/{}'.format(
            x)

        response = requests.get(url).text

        insert_into_database(podcast_number, response)


def insert_into_database(podcast_number, data):
    pass


get_transcript_names()
get_transcripts()
