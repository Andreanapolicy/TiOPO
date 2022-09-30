def convertLinkToAbsolutePath(mainUrl, link):
    if link == '#':
        return mainUrl

    if mainUrl in link:
        return link

    if 'tel:' in link or 'mailto:' in link:
        return None

    if link.startswith('http'):
        return None

    return mainUrl + link