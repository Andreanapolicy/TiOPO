import requests
from bs4 import BeautifulSoup
from libs.Url import convertLinkToAbsolutePath
from libs.Common import getUniqueList
from libs.UrlResponse import getUrlResponse
from libs.Reporter import writeUrlResponseReport

URL = 'http://links.qatl.ru/'

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
    urlResponseList = []
    [urlResponseList.append(getUrlResponse(link)) for link in convertedLinks]
    return urlResponseList


links = getAllLinksFromDocument(getHtmlDocument(URL))
responses = getAllUrlResponses(links)
writeUrlResponseReport(responses)