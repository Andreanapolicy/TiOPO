import requests
from bs4 import BeautifulSoup

URL = 'http://links.qatl.ru/'

def getHtmlDocument(url):
    html_text = requests.get(url).text
    return BeautifulSoup(html_text, 'html.parser')

def getAllLinksFromDocument(document):
    needfulLinks = []

    for links in document.findAll('a', href=True):
        needfulLinks.append(links.get('href'))

    return needfulLinks

print(getAllLinksFromDocument(getHtmlDocument(URL)))