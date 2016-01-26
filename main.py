import os

from utils.scraper import main as scrape
from utils.dl import main as download


def main():
    directory = os.path.expanduser("~/Desktop/xkcd/")
    if not os.path.exists(directory):
        os.mkdir(directory)

    for i in range(1, scrape() + 1):
        if download(i, scrape(i)):
            print('Downloaded post {}'.format(i))

if __name__ == '__main__':
    main()
