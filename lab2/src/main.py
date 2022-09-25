import requests
from bs4 import BeautifulSoup

vgm_url = 'http://links.qatl.ru/'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')

needfulLinks = []

for links in soup.findAll('a', href=True):
    needfulLinks.append(links.get('href'))

print(needfulLinks, '\n')