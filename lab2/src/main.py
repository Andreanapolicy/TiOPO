import requests
from bs4 import BeautifulSoup

URL = 'http://links.qatl.ru/'

class UrlResponse:
    def __init__(self, url, code):
        self.url = url
        self.url = code


def getHtmlDocument(url):
    html_text = requests.get(url).text
    return BeautifulSoup(html_text, 'html.parser')

def getAllLinksFromDocument(document):
    needfulLinks = []

    for links in document.findAll('a', href=True):
        needfulLinks.append(links.get('href'))

    return needfulLinks

def getAllUrlResponses(links):
    def convertLinkToAbsolutePath(mainUrl, link):
        if link == '#':
            return mainUrl

        if link.startswith('http'):
            return link

        return mainUrl + link

    [print(convertLinkToAbsolutePath(URL, link)) for link in links]


print(getAllUrlResponses(getAllLinksFromDocument(getHtmlDocument(URL))))