import unicodedata

with open('003.txt') as f:
    for line in f:
        if line[0].isdigit() and ': ' in line:
            try:
                # Remove \xa0 non-breaking spaces from line
                line = unicodedata.normalize('NFKD', line)
                line = line.split(" ", 2)

                timestamp = line[0]
                speaker = line[1][0:-1]  # Remove colon from name
                content = line[2]

                c.execute(
                    "INSERT INTO podcast (podcast, timestamp, speaker, content) VALUES ('003', ?, ?)", (timestamp, speaker, content,))

                conn.commit()

            except IndexError as e:
                print(e, line)
                continue

        elif line[0].isdigit():
            try:
                line = unicodedata.normalize('NFKD', line)
                line = line.strip().split(" ", 1)

                timestamp = line[0]
                content = line[1]

                c.execute(
                    "INSERT INTO podcast (podcast, timestamp, content) VALUES ('003', ?, ?)", (timestamp, content,))

                conn.commit()

            except IndexError as e:
                print(e, line)
                continue
