import requests
from bs4 import BeautifulSoup
from libs.Url import convertLinkToAbsolutePath
from libs.Common import getUniqueList
from libs.UrlResponse import getUrlResponse, getOnlyAvailableLinks
from libs.Reporter import writeUrlResponseReport

URL = 'http://links.qatl.ru/'

def getHtmlDocument(url):
    htmlText = requests.get(url).text
    return BeautifulSoup(htmlText, 'html.parser')

def getAllLinksFromDocument(document):
    needfulLinks = []

    for links in document.findAll('a', href=True):
        needfulLinks.append(links.get('href'))

    return needfulLinks

def getAllUrlResponses(links):
    convertedLinks = []
    [convertedLinks.append(convertLinkToAbsolutePath(URL, link)) for link in getUniqueList(links)]
    urlResponseList = []
    [urlResponseList.append(getUrlResponse(link)) for link in list(filter(None, convertedLinks))]
    return urlResponseList


def processAllLinksFromSite(linksToVisit, foundLinks):
    for link in linksToVisit:
        newLinks = getAllLinksFromDocument(getHtmlDocument(link))
        newLinks = [convertLinkToAbsolutePath(URL, link) for link in getUniqueList(newLinks)]
        newLinks = list(set(newLinks) - set(foundLinks))
        newLinks = list(filter(None, newLinks))
        foundLinks += newLinks
        availableLinks = []
        [availableLinks.append(linkResponse) for linkResponse in getOnlyAvailableLinks(newLinks)]
        linksToVisit += availableLinks


linksToVisit = [URL]
foundLinks = [URL]
processAllLinksFromSite(linksToVisit, foundLinks)

responses = getAllUrlResponses(foundLinks)
writeUrlResponseReport(responses)