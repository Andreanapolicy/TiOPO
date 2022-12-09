def convertLinkToAbsolutePath(mainUrl, link):
    extensions = {
        'rar',
        'pdf',
        'mp4',
        'doc',
        'docx',
        'xls',
        'png',
        'jpg',
        'jpeg',
        'zip',
        'webp',
        'webm',
        'gif'
    }

    for extension in extensions:
        if link.find(extension) != -1:
            return None

    if link == '#':
        return mainUrl

    if mainUrl in link:
        return link

    if 'tel:' in link or 'mailto:' in link:
        return None

    if link.startswith('http'):
        return None

    return mainUrl + link