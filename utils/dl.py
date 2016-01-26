from os import path
from urllib import request


def main(post_number, url):
    fp = path.expanduser("~/Desktop/xkcd/{}.jpg".format(str(post_number)))

    if not path.exists(fp):
        request.urlretrieve(url, fp)
        return fp
    return None
