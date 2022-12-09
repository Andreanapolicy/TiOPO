from dataclasses import dataclass
from urllib.parse import urlparse


@dataclass
class Url:
    url: str
    previous_url: str
    status: int

    def __hash__(self):
        return url.__hash__()


def isValid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def checkExtension(url):
    blockList = {
        "jpeg",
        "jpg",
        "mp4",
        "gif",
        "doc",
        "png",
        "rar",
        "zip",
        "webp",
        "webm"
    }

    for extension in blockList:
        if url.find(extension) != -1:
            return True


def domain(url):
    return urlparse(url).netloc

