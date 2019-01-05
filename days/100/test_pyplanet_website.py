import unittest
from selenium import webdriver

# Coding challenge from https://pybit.es/codechallenge32.html


class PyPlanet(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()

    def test_home_page(self):
        driver = self.driver
        driver.get('https://pyplanet.herokuapp.com')
        self.assertIn("PyBites 100 Days of Django", driver.title)

        login_link = driver.find_element_by_css_selector(
            '#login > a:nth-child(1)').text
        self.assertIn('Login', login_link)

        home_link = driver.find_element_by_css_selector(
            '#login > a:nth-child(2)').text
        self.assertIn('Home', home_link)

        article_link = driver.find_element_by_css_selector(
            'body > main > ul > li > a').text
        self.assertIn('PyPlanet Article Sharer App', article_link)

    def test_article_sharer_app(self):
        driver = self.driver
        driver.get('https://pyplanet.herokuapp.com/')
        article_link = driver.find_element_by_css_selector(
            'body > main > ul > li > a')
        article_link.click()

        table_header = driver.find_element_by_css_selector(
            'body > main > table > thead > tr > th').text
        self.assertIn('Title', table_header)

        list_of_entries = driver.find_elements_by_tag_name("td")
        number_of_actual_entries = len(list_of_entries)
        expected_number_of_entries = int(100)
        self.assertIs(expected_number_of_entries, number_of_actual_entries)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
