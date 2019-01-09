import sqlite3
import spacy
import pandas as pd

conn = sqlite3.connect('podcast_data.sqlite')
c = conn.cursor()


table_name = 'podcast'
time = 'time'
podcast_num = 'podcast'
speaker = 'speaker'
content = 'content'


c.execute(
    'SELECT * FROM {tn} WHERE {p}="1"'.format(tn=table_name, p=podcast_num))

all_rows = c.fetchall()

nlp = spacy.load('en_core_web_sm')

df = pd.read_sql_query("select * from podcast where podcast='1'", conn)

print(df['content'])
