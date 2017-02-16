"""IOThomeinspector test file."""


from django.test import TestCase, Client
from .google_api import make_search, get_links, get_versions, scrape_soup
import bs4
from django.test.testcases import SimpleTestCase

class SearchResultTestCase(TestCase):
    """Tests for the make search method."""

    def setUp(self):
        """Set up for test case."""
        self.soups = make_search('Philips hue')

    def test_soups_return(self):
        """Test that the soups list being returned is getting appended to."""
        self.assertTrue(len(self.soups) == 3)

    def test_type_of_items_in_soups_is_beautiful_soup(self):
        """Test that the items in the soups list getting returned are beautiful soup objects."""
        for soup in self.soups:
            self.assertTrue(type(soup) == bs4.BeautifulSoup)

    def test_getting_the_right_html_firmware(self):
        """Test that the html in the beautiful soup object contains the search resaults for firmware updates."""
        self.assertTrue(str(self.soups[0].title) == '<title>Philips hue firmware update - Bing</title>')

    def test_getting_the_right_html_security(self):
        """Test that the html in the beautiful soup object contains the search resaults for security vulnerabilities."""
        self.assertTrue(str(self.soups[1].title) == '<title>Philips hue security vulnerabilities - Bing</title>')

    def test_soups_is_list(self):
        """Test that make search returns a list."""
        self.assertTrue(type(self.soups) == list)


class LinkFilterTestCase(TestCase):
    """Tests for the get links function."""

    def setUp(self):
        """Set up for test case."""
        self.links = get_links('Philips hue')
        self.soups = make_search('Philips hue')

    def test_link_buckets_type(self):
        """Test that the return of get links is a list of lists."""
        for links in self.links[0]:
            self.assertTrue(type(links) == list)

    def test_link_list_length(self):
        """Test that the length of the list returned by get links is the same as the number of search extensions we have."""
        self.assertTrue(len(self.links) == 2)

    def test_link_type(self):
        """Test that the type of the links is a string."""
        for links in self.links[0]:
            for link in links:
                self.assertTrue(type(link[0]) == str)

# class UserAgentHomeViewTestCase(TestCase):
#     """Test that home view returns user-agent info on browser."""
#     test_browser = Client(HTTP_USER_AGENT='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3011.0 Safari/537.36')
#     response = test_browser.get('/')
#     response.content.assertContains('Chrome')


class GetVersionsTestCase(TestCase):
    """Tests for get versions function."""

    def setUp(self):
        """Set up."""
        self.links = []
        for link in make_search('Samsung Family hub')[2].find_all('a'):
            if 'http://' not in str(link.get('href')):
                pass
            elif 'blog' in str(link.get('href')):
                pass
            elif 'go.microsoft' in str(link.get('href')):
                pass
            else:
                self.links.append(link)
        self.search_anticipated = get_versions('Philips hue', self.links)
        self.search_not_anticipated = get_versions('Samsung Family hub', self.links)

    def test_return_for_preset_url(self):
        """Test when user searches an item we accounted for, it returns a predictable number."""
        self.assertTrue(self.search_anticipated == '01036659')

