def convertLinkToAbsolutePath(mainUrl, link):
    if link == '#':
        return mainUrl

    if mainUrl in link:
        return link

    if link.startswith('http'):
        return None

    return mainUrl + link