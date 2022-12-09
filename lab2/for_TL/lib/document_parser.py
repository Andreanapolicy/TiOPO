import time
import requests

from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from url import Url, isValid, checkExtension, domain

RETRY_TIMEOUT = 60
REQUEST_TIMEOUT = 60
RETRY_COUNT = 5

VISITED_LINKS = set()
INVALID_LINKS = set()
result = set()

PREVIOUS_URL = ''

def retryingGetting(url):
    response = requests.Response
    for i in range(RETRY_COUNT):
        try:
            response = requests.get(url, timeout=REQUEST_TIMEOUT)
            if response.status_code < 500:
                return response
            time.sleep(RETRY_TIMEOUT)
        except Exception:
            response.status_code = 500
            return response

    return response


def findAllLinks(url):
    global PREVIOUS_URL

    links = set()

    if checkExtension(url):
        currentRequest = headRetry(url)
        result.add(Url(url, PREVIOUS_URL, currentRequest.status_code))
        return links

    currentRequest = retryingGetting(url)
    result.add(Url(url, PREVIOUS_URL, currentRequest.status_code))
    if currentRequest.status_code >= 400:
        return links

    soup = BeautifulSoup(currentRequest.content, 'html.parser')

    links = getFromHTMLDocument(url)
    return links

def getFromHTMLDocument(url):
    global PREVIOUS_URL

    links = set()
    for htmlLink in soup.findAll('a'):
        link = htmlLink.attrs.get('href')

        if link == '' or link is None:
            continue

        if urlparse(link).netloc == '':
            link = urljoin(url, link)

        link = constructUrl(link)
        if not isValid(link):
            INVALID_LINKS.add(link)
            continue

        if link in VISITED_LINKS:
            continue

        if domain(url) not in link:
            continue

        links.add(link)
        VISITED_LINKS.add(link)
        PREVIOUS_URL = url

    return links

def constructUrl(link):
    parsedValue = urlparse(link)
    link = parsedValue.scheme + '://' + parsedValue.netloc + parsedValue.path
    return link


def headRetry(url):
    response = requests.Response

    for i in range(RETRY_COUNT):
        response = requests.head(url, timeout=REQUEST_TIMEOUT)

        if response.status_code < 500:
            return response

        time.sleep(RETRY_TIMEOUT)
    return response


def parse(url):
    links = findAllLinks(url)

    for link in links:
        parse(link)