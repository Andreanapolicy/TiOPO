import requests

class UrlResponse:
    def __init__(self, url, code):
        self.url = url
        self.url = code


def getUrlResponse(link):
    try:
        requestResult = requests.head(link)
        return UrlResponse(link, requestResult.status_code)
    except requests.ConnectionError:
        return UrlResponse(link, 500)