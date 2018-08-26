from urllib.request import urlopen


def download_simple(url):  # url(str)
    """The simplest download function
    """
    html = urlopen(url).read().decode()
    return html


print(download_simple('http://example.webscraping.com').strip())
