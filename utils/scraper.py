import requests, re, bs4

BASE_URL = 'http://xkcd.com/'


def scrape(post=None):
    parse = parse_latest if post is None else parse_url
    return parse(request(post))


def request(post=None):
    """Return html body for xkcd homepage or requested comic if post not None"""

    url = BASE_URL if post is None else BASE_URL + str(post)
    return requests.get(url)


def parse_latest(response):
    """Parse latest post number from response body"""
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    # "Permanent link to this comic: http://xkcd.com/1634/" => 1634
    if soup.find(text=re.compile('Permanent link to this comic:')):
        latest_post = soup.find(text=re.compile('Permanent link to this comic:')).split('/')[-2]
        return int(latest_post)
    return None


def parse_url(response):
    """Parse comic img src from response body"""
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    # https://xkcd.com/327/ => //imgs.xkcd.com/comics/exploits_of_a_mom.png
    if soup.find(id='comic').find('img'):
        return 'http:' + soup.find(id='comic').find('img')['src']
    return None
