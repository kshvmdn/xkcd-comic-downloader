import os
import requests
import re
import urllib.request
from bs4 import BeautifulSoup

# def get_latest_comic():
#     latest_comic = requests.get("http://xkcd.com/").content
#     lc_soup = BeautifulSoup(latest_comic, "html.parser")

#      # "Permanent link to this comic: http://xkcd.com/1564/"
#     lc_string = lc_soup.find(string=re.compile("Permanent"))

#     # Parse comic id from lc_string => 1564
#     lc_id = int(re.search(r'\d+', lc_string).group())

#     return lc_id

# img_dir = os.path.expanduser("~/Desktop/xkcd_comics/")

# if not os.path.exists(img_dir):
#     os.mkdir(img_dir)

# for i in range(0, get_latest_comic()):
#     current_working_comic = requests.get("http://xkcd.com/"+str(i+1)+"/").content
#     cwc_soup = BeautifulSoup(current_working_comic,"html.parser")

#     cwc_img_block = cwc_soup.find("div", {"id":"comic"})
#     cwc_img_tag = cwc_img_block.find("img")
#     cwc_url = "http:" + cwc_img_tag["src"]

#     file_path = os.path.expanduser("~/Desktop/xkcd_comics/xkcd_"+str(i+1)+".jpg")
#     #print(file_path)

#     if not os.path.exists(file_path):
#         urllib.request.urlretrieve(cwc_url, file_path)


def request():
    """Return html body for xkcd homepage"""
    return requests.get('http://xkcd.com/')


def parse(response):
    """Parse  xkcd.com html body for latest xkcd comic number"""
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find(text=re.compile('Permanent link to this comic:'))[-6:].replace('/', '')
    

if __name__ == '__main__':
    print(parse(request()))