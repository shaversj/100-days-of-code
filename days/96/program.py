import sqlite3

conn = sqlite3.connect('podcast_data.sqlite')
c = conn.cursor()

createTable = """CREATE TABLE podcast(
    podcast_num INTEGER,
    time FLOAT,
    speaker TEXT,
    content TEXT
);"""

c.execute(createTable)

with open('003.txt') as f:
    for line in f:
        if line.isspace():
            continue
        else:
            try:
                line = line.strip().split(" ", 1)
                c.execute(
                    "INSERT INTO podcast (podcast_num, time, content) VALUES ('003', ?, ?)", (line[0], line[1],))

                conn.commit()

            except IndexError as e:
                print(e)
                continue
