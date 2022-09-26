def convertLinkToAbsolutePath(mainUrl, link):
    if link == '#':
        return mainUrl

    if link.startswith('http'):
        return link

    return mainUrl + link


def getUniqueList(links):
    return list(set(links))