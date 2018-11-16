import csv
import collections
from flask import Flask
from flask_restful import Api
from flask import jsonify
from flask import request

app = Flask(__name__)
api = Api(app)

data = []

Record = collections.namedtuple(
    'Record', "State, Sex, Year, Name, Occurance")


""" def main():
    init()

    top_10(2015, 'M') """


@app.route("/top10")
def top_10():

    # http://127.0.0.1:5000/top10?Year=2017&Sex=F
    year = request.args.get('Year', default=1, type=int)
    sex = request.args.get('Sex', default=1, type=str)
    new_data = return_by_year_sex(year, sex)

    parsed = []
    for k, name in enumerate(new_data[:10], 1):
        State, Sex, Year, Name, Occurance = name
        dic = {
            'Name': Name,
            'Rank': k,
            'Sex': Sex,
            'Births': Occurance,
            'Year': Year

        }
        parsed.append(dic)

    return jsonify(parsed)


def return_by_year_sex(year, sex):

    by_year = [lines for lines in data if lines.Year ==
               year and lines.Sex == sex]

    return by_year


def init():
    with open('OH.txt') as f:
        fields = ["State", "Sex", "Year", "Name", "Occurance"]
        reader = csv.DictReader(f, fieldnames=fields)
        for row in reader:
            line = parse_row(row)
            data.append(line)


def parse_row(row):
    row['State'] = str(row['State'])
    row['Sex'] = str(row['Sex'])
    row['Year'] = int(row['Year'])
    row['Name'] = str(row['Name'])
    row['Occurance'] = int(row['Occurance'])

    r = Record(**row)

    return r


if __name__ == '__main__':
    init()
    app.run(debug=True)
