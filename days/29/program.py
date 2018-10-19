import bs4
import requests
import pandas as pd
import urllib.request
import ssl
import geocoder
import gmplot
import config

delaware = {}
delaware_list = []
results = []
latitude = []
longitude = []


URL = 'https://sheriff.co.delaware.oh.us/sheriff-sales/'


def pull_site():
    try:
        raw_site_page = requests.get(URL)
    except requests.exceptions.RequestException as e:
        print(e)

    return raw_site_page


def scrape_website(site):

    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    table_rows = soup.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        delaware_list.append(row)

    for i in delaware_list:
        for p in i:
            print(p)


def scrape_website_v2(site):

    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    tds = [row.findAll('td') for row in soup.findAll('tr')]
    print(tds)


def scrape_website_v3(site):

    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    table_rows = soup.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td')
        results.append([i.text for i in td])

    # remove header
    del results[0]

    return results


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

    for address in results:

        g = geocoder.google(str(address[1]))
        latitude.append(g.latlng[0])
        longitude.append(g.latlng[1])

    return latitude, longitude


def plot_map():

    gmap = gmplot.GoogleMapPlotter(latitude[0], longitude[0], 13)
    gmap.apikey = config.api_key

    gmap.scatter(latitude, longitude, edge_width=10)
    gmap.draw('maps.html')


if __name__ == "__main__":
    site = pull_site()
    scrape_website_v3(site)
    add_geocode_addresses()
    plot_map()
