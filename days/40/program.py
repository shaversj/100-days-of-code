import config
import plotly
import bs4
import requests
import geocoder

results = []
latitude = []
longitude = []


def pull_site():

    URL = 'https://sheriff.co.delaware.oh.us/sheriff-sales/'

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
        results.append([i.text for i in td])

    # remove header
    del results[0]

    return results


def add_geocode_addresses():
    """Retrieve latitude and longitude for all scraped addresses."""

    for address in results:
        g = geocoder.google(str(address[1]), key=config.api_key)
        latitude.append(g.latlng[0])
        longitude.append(g.latlng[1])

    return latitude, longitude


def plot_map():

    plotly.tools.set_credentials_file(
        username=config.plotly_username, api_key=config.plotly_apikey)

    mapbox_access_token = config.map_token

    data = [
        plotly.graph_objs.Scattermapbox(
            lat=latitude,
            lon=longitude,
            mode='markers',
            marker=dict(
                size=9
            ),
            text=[address[1] for address in results],
        )
    ]

    layout = plotly.graph_objs.Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=40.2986724,
                lon=-83.067965
            ),
            pitch=0,
            zoom=10
        ),
    )

    fig = dict(data=data, layout=layout)
    plotly.plotly.iplot(fig, filename='Delaware County Sheriff Sale Map')


if __name__ == "__main__":
    site = pull_site()
    scrape_website(site)
    add_geocode_addresses()
    plot_map()
