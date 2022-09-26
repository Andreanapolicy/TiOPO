import requests
from bs4 import BeautifulSoup
from libs.Url import convertLinkToAbsolutePath
from libs.Common import getUniqueList

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
    convertedLinks = []
    [convertedLinks.append(convertLinkToAbsolutePath(URL, link)) for link in getUniqueList(links)]



getAllUrlResponses(getAllLinksFromDocument(getHtmlDocument(URL)))