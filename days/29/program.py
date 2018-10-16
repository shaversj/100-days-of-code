import bs4
import requests
import pandas as pd
import urllib.request
import ssl


"""
User Story: As a user, I want to see the address of a house on a map.

User Story: As a user, I will be given a list of houses that will be in an upcoming sheriff sale.

Scrape: https://sheriff.co.delaware.oh.us/sheriff-sales/

Capture all of the information below from the webpage:
Date
Address
Property Description
Case Number
Appraisal Value
Deposit	Purchaser
Purchaser Price




"""

URL = 'https://sheriff.co.delaware.oh.us/sheriff-sales/'


def pull_site():
    raw_site_page = requests.get(URL)
    raw_site_page.raise_for_status()
    return raw_site_page


def scrape_website(site):

    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    table_rows = soup.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        print(row)


def scrape_with_pandas():
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(URL, context=context)
    html = response.read()
    df = pd.read_html(html, header=0)

    # convert to json
    address_list = df[0].to_json(orient='records')
    test = json.loads(address_list)
    # Retrieve Addresses to Map.
    for k in test:
        print(k[Address])

    # for df in dfs:
    #    print(df)


def add_geocode_addresses():
    """
    https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY

    Retrieve lat and long for each address.
    """

    pass


def plot_addresses():
    pass


if __name__ == "__main__":
    site = pull_site()
    scrape_website(site)
