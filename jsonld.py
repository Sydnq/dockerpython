
import urllib.request
from bs4 import BeautifulSoup
import json


def jsonld_extractor(url, tag):
    """
    Extract/retrieve company data based on Structured data, JSON-LD ,
    particular, if present/available.

    for more info on structured data and JSON-LD refer to :
    https://developers.google.com/search/docs/guides/intro-structured-data

    @param url          company url to retrieve the JSON-LD contents from o
    @param tag          search tag in the url/company page
    @return companies   list of parsed companies JSON-LD's
    """
    companies = []

    # check to see if url is not null
    if url:

        # fetch the web-page from the provided url and save it in response
        response = urllib.request.urlopen(url).read()
        # check to see if company page has been retrieved
        if response:
            # create soup object from the response
            soup = BeautifulSoup(response, 'html.parser')
            # parse the soup object and extract all the tags and append them
            # into the companies lis
            for link in soup.find_all(tag, type='application/ld+json'):
                # convert the data into json object
                texts = json.loads(link.text)
                # append the json-ld object to companies list
                companies.append(texts)

        return companies


if __name__ == '__main__':
    example_url = 'https://www.apple.com/lae/iphone-x/'
    tag_to_find = 'script'
    data = jsonld_extractor(example_url, tag_to_find)
    print(data[0])
