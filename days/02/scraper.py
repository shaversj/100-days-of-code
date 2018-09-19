import requests
import bs4

URL = 'https://www.huffingtonpost.com'


def pull_site():

    raw_site_page = requests.get(URL)
    raw_site_page.raise_for_status()
    return raw_site_page


def scrape(site):
    articles = []

    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    frontpage_articles = soup.select('.card__headline__text')

    for titles in frontpage_articles:
        articles.append(titles.getText())

    for titles in articles:
        print(titles, end=' ')


if __name__ == "__main__":
    site = pull_site()
    scrape(site)
