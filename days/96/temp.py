import requests
import io
import unicodedata
from pathlib import Path

response = requests.get(
    'https://raw.githubusercontent.com/mikeckennedy/talk-python-transcripts/master/transcripts/044.txt', stream=True)

for line in response.iter_lines(decode_unicode=True):
    print(line)


""" podcast_name = '044_ish.txt'

in_file_1 = Path.cwd() / "data" / podcast_name

with open(in_file_1, "wb") as code:
    code.write(response) """
